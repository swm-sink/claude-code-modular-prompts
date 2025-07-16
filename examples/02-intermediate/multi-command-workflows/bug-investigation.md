# Bug Investigation Workflow Example

## Overview
This example demonstrates the powerful **query → task → validation** workflow for systematic bug investigation and resolution.

## The Problem Scenario
Your production API is returning 500 errors intermittently. Users report that user authentication sometimes fails, but it's not consistent. You need to investigate, identify root cause, and fix the issue.

## The Multi-Command Workflow

### Step 1: Research and Analysis - `/query`
```bash
/query "analyze authentication failures and 500 errors in user login system"
```

**What the Framework Does:**
- Scans codebase for authentication-related code
- Identifies error handling patterns
- Analyzes log files and error reporting
- Maps authentication flow and dependencies
- Identifies potential failure points

**Expected Framework Output:**
```
🔍 AUTHENTICATION SYSTEM ANALYSIS:

Code Components Found:
├── auth/
│   ├── models.py - User, Token models
│   ├── views.py - Login, logout, refresh endpoints  
│   ├── middleware.py - JWT token validation
│   └── serializers.py - User data serialization
├── utils/
│   ├── jwt_utils.py - Token generation/validation
│   └── rate_limiting.py - Login attempt limiting
└── settings/
    └── auth_config.py - Authentication configuration

Potential Issue Patterns:
⚠️  JWT token expiration handling inconsistent
⚠️  Database connection timeout in auth middleware  
⚠️  Race condition in token refresh mechanism
⚠️  Missing error handling in password verification

Critical Code Locations:
📍 auth/middleware.py:45 - JWT validation without timeout handling
📍 utils/jwt_utils.py:23 - Token refresh without atomic operations
📍 auth/views.py:78 - Login endpoint missing rate limit error handling

Database Analysis:
🔍 auth_user table: 50K+ records
🔍 auth_token table: 500K+ records (potential cleanup needed)
🔍 Failed login attempts: 2.3% of total requests

Recent Error Patterns:
❌ "JWT signature verification failed" - 15% of 500 errors
❌ "Database connection timeout" - 35% of 500 errors  
❌ "Token refresh conflict" - 25% of 500 errors
❌ "Rate limit exceeded" - 25% of 500 errors

HYPOTHESIS: Multiple concurrent token refresh requests causing database locks
```

### Step 2: Targeted Fix Implementation - `/task`
```bash
/task "fix JWT token refresh race condition and add proper error handling"
```

**What the Framework Does:**
- Creates failing tests that reproduce the race condition
- Implements atomic token refresh with database locks
- Adds proper error handling and timeout configuration
- Updates authentication middleware for robust error handling
- Adds monitoring and logging for auth failures

**Generated Test (TDD RED Phase):**
```python
# tests/auth/test_token_refresh_concurrency.py
import pytest
import threading
from django.test import TestCase
from django.contrib.auth.models import User
from auth.models import Token
from auth.utils.jwt_utils import refresh_token

class TokenRefreshConcurrencyTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        self.token = Token.objects.create(user=self.user)

    def test_concurrent_token_refresh_prevents_race_condition(self):
        """Test that concurrent token refresh requests don't create race conditions"""
        results = []
        errors = []
        
        def refresh_token_worker():
            try:
                new_token = refresh_token(self.token.key)
                results.append(new_token)
            except Exception as e:
                errors.append(e)
        
        # Simulate 10 concurrent refresh requests
        threads = []
        for _ in range(10):
            thread = threading.Thread(target=refresh_token_worker)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        # Should have exactly one successful refresh
        assert len(results) == 1
        assert len(errors) == 9  # 9 should get "refresh in progress" error
        
        # Verify token is still valid
        assert Token.objects.filter(user=self.user).count() == 1

    def test_jwt_validation_handles_database_timeout(self):
        """Test that JWT validation gracefully handles database timeouts"""
        # This test will initially FAIL - proving the bug exists
        with patch('auth.middleware.get_token_from_db') as mock_get_token:
            mock_get_token.side_effect = DatabaseTimeout("Connection timeout")
            
            response = self.client.get('/api/protected/', 
                                     HTTP_AUTHORIZATION=f'Bearer {self.token.key}')
            
            # Should return 503 Service Unavailable, not 500 Internal Error
            assert response.status_code == 503
            assert 'service temporarily unavailable' in response.json()['error'].lower()
```

**Generated Implementation (TDD GREEN Phase):**
```python
# auth/utils/jwt_utils.py
import threading
from django.db import transaction
from django.core.cache import cache
from django.utils import timezone
from .models import Token

# Thread-safe token refresh with atomic operations
_refresh_locks = {}
_refresh_lock = threading.Lock()

def refresh_token(old_token_key):
    """Atomic token refresh with race condition prevention"""
    
    # Get or create a lock for this specific token
    with _refresh_lock:
        if old_token_key not in _refresh_locks:
            _refresh_locks[old_token_key] = threading.Lock()
        token_lock = _refresh_locks[old_token_key]
    
    # Only one thread can refresh this token at a time
    if not token_lock.acquire(blocking=False):
        raise TokenRefreshInProgressError(
            "Token refresh already in progress. Please retry in a moment."
        )
    
    try:
        with transaction.atomic():
            # Re-fetch token within transaction to ensure consistency
            try:
                old_token = Token.objects.select_for_update().get(key=old_token_key)
            except Token.DoesNotExist:
                raise InvalidTokenError("Token not found")
            
            # Check if token was already refreshed by another request
            if old_token.refreshed_at and old_token.refreshed_at > timezone.now() - timezone.timedelta(seconds=30):
                # Token was recently refreshed, return the current one
                return old_token
            
            # Create new token atomically
            new_token = Token.objects.create(
                user=old_token.user,
                expires_at=timezone.now() + timezone.timedelta(hours=24)
            )
            
            # Mark old token as refreshed (but don't delete immediately for graceful transition)
            old_token.refreshed_at = timezone.now()
            old_token.replaced_by = new_token
            old_token.save()
            
            return new_token
            
    finally:
        token_lock.release()
        # Clean up lock after some time
        threading.Timer(60.0, lambda: _refresh_locks.pop(old_token_key, None)).start()

# auth/middleware.py  
import logging
from django.http import JsonResponse
from django.db import DatabaseError, OperationalError
from django.core.cache import cache

logger = logging.getLogger(__name__)

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process authentication with proper error handling
        auth_result = self.process_authentication(request)
        
        if auth_result['status'] == 'error':
            return JsonResponse(auth_result, status=auth_result['status_code'])
        
        if auth_result['user']:
            request.user = auth_result['user']
        
        response = self.get_response(request)
        return response

    def process_authentication(self, request):
        """Process JWT authentication with robust error handling"""
        
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return {'status': 'success', 'user': None}
        
        token_key = auth_header.split(' ')[1]
        
        # Try cache first (performance optimization)
        cache_key = f"auth_token_{token_key[:16]}"  # First 16 chars for security
        cached_user_id = cache.get(cache_key)
        
        if cached_user_id:
            try:
                user = User.objects.get(id=cached_user_id)
                return {'status': 'success', 'user': user}
            except User.DoesNotExist:
                cache.delete(cache_key)  # Clean up stale cache
        
        # Database lookup with timeout handling
        try:
            token = Token.objects.select_related('user').get(
                key=token_key,
                expires_at__gt=timezone.now(),
                refreshed_at__isnull=True  # Not replaced by refresh
            )
            
            # Cache for 5 minutes
            cache.set(cache_key, token.user.id, 300)
            
            return {'status': 'success', 'user': token.user}
            
        except Token.DoesNotExist:
            logger.warning(f"Invalid token attempt: {token_key[:8]}...")
            return {
                'status': 'error',
                'status_code': 401,
                'error': 'Invalid or expired token'
            }
            
        except (DatabaseError, OperationalError) as e:
            logger.error(f"Database error during authentication: {e}")
            return {
                'status': 'error', 
                'status_code': 503,
                'error': 'Authentication service temporarily unavailable'
            }
            
        except Exception as e:
            logger.error(f"Unexpected error during authentication: {e}")
            return {
                'status': 'error',
                'status_code': 500,
                'error': 'Internal authentication error'
            }
```

**Database Migration:**
```python
# migrations/0002_add_token_refresh_fields.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='refreshed_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='token',
            name='replaced_by',
            field=models.ForeignKey(
                'self', 
                null=True, 
                blank=True, 
                on_delete=models.SET_NULL
            ),
        ),
        migrations.AddIndex(
            model_name='token',
            index=models.Index(
                fields=['key', 'expires_at', 'refreshed_at'], 
                name='token_lookup_idx'
            ),
        ),
    ]
```

### Step 3: Validation and Deployment - `/protocol`
```bash
/protocol "validate authentication fix and deploy to production safely"
```

**What the Framework Does:**
- Runs comprehensive test suite including new concurrency tests
- Performs load testing on authentication endpoints
- Validates database migration safety
- Creates deployment plan with rollback strategy
- Sets up monitoring for authentication metrics

**Framework Validation Output:**
```
🧪 COMPREHENSIVE TESTING RESULTS:

Unit Tests:
✅ test_concurrent_token_refresh_prevents_race_condition - PASSED
✅ test_jwt_validation_handles_database_timeout - PASSED  
✅ test_token_expiration_handling - PASSED
✅ test_invalid_token_responses - PASSED
✅ test_authentication_middleware_error_handling - PASSED

Integration Tests:
✅ test_full_authentication_flow - PASSED
✅ test_token_refresh_under_load - PASSED
✅ test_database_failover_handling - PASSED

Load Testing:
✅ 1000 concurrent login requests - 0% errors
✅ 500 concurrent token refresh requests - 0% race conditions
✅ Database connection pool handling - PASSED
✅ Average response time: 120ms (previously 850ms)

Security Validation:
✅ Token expiration properly enforced
✅ Race condition vulnerability eliminated
✅ Error messages don't leak sensitive information
✅ Rate limiting working correctly

Database Migration:
✅ Migration tested on copy of production data
✅ Rollback procedure validated
✅ Index creation impact: <2 second downtime
✅ Backward compatibility confirmed

🚀 DEPLOYMENT PLAN:

1. Deploy during low-traffic window (2:00 AM UTC)
2. Database migration (estimated 30 seconds)
3. Application deployment with rolling restart
4. Monitor authentication error rates for 1 hour
5. Rollback triggers:
   - Auth error rate > 1% 
   - Response time > 500ms
   - Database connection issues

📊 MONITORING SETUP:
- Authentication success/failure rates
- Token refresh performance metrics  
- Database connection pool status
- Error rate by endpoint
- Response time percentiles

✅ PRODUCTION READINESS: CONFIRMED
```

## Key Learning Points

### ✅ Multi-Command Workflow Benefits
1. **Systematic Investigation**: `query` provides comprehensive understanding before action
2. **Targeted Implementation**: `task` focuses on specific fix with TDD
3. **Production Safety**: `protocol` ensures robust deployment with monitoring

### 📚 Workflow Pattern Applications
- **Bug Investigation**: Research → Fix → Validate
- **Performance Issues**: Analyze → Optimize → Monitor
- **Security Vulnerabilities**: Assess → Patch → Verify
- **Feature Problems**: Understand → Implement → Deploy

### 🔍 When to Use This Workflow
- ✅ Complex production issues requiring investigation
- ✅ Problems affecting multiple system components
- ✅ High-stakes fixes that need careful validation
- ✅ Issues requiring deep understanding before action

### 🚀 Command Synergy
Each command builds on the previous:
- **`/query`** → Provides context and understanding
- **`/task`** → Uses that context for targeted implementation  
- **`/protocol`** → Ensures production-ready deployment

## Variations and Extensions

### For Different Problem Types:
```bash
# Performance investigation
/query "analyze slow database queries and response times"
/task "optimize database queries and add caching"
/protocol "deploy performance improvements with monitoring"

# Security issue
/query "investigate potential SQL injection vulnerability"
/task "implement parameterized queries and input validation"
/protocol "deploy security fixes with penetration testing"

# Integration problem
/query "analyze third-party API integration failures"
/task "implement retry logic and circuit breaker pattern"
/protocol "deploy integration improvements with fallback monitoring"
```

### For Team Workflows:
```bash
# Code review integration
/query "analyze code review feedback and technical debt"
/task "refactor code based on review recommendations"
/protocol "validate refactoring and merge with team approval"
```

## Success Metrics

After implementing this workflow, you should see:
- **Faster Problem Resolution**: Systematic approach reduces investigation time
- **Higher Fix Quality**: TDD ensures robust solutions
- **Reduced Production Risk**: Protocol validation prevents deployment issues
- **Better Team Confidence**: Predictable, proven workflow for complex issues

This workflow transforms chaotic debugging into a systematic, reliable process that consistently delivers high-quality solutions.