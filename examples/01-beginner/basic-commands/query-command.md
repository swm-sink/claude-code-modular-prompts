# Query Research Example

## Overview
This example demonstrates how to use the `/query` command for research, analysis, and understanding code without making any modifications.

## Example Scenario
You've inherited a Django e-commerce codebase and need to understand how the authentication system works before making changes.

## Step-by-Step Walkthrough

### 1. Issue the Command
```bash
/query "how does the authentication system work in this Django project?"
```

### 2. Expected Framework Response
The framework will:
1. **Analyze codebase**: Scan authentication-related files
2. **Map relationships**: Understand how components connect
3. **Identify patterns**: Find architectural patterns and conventions
4. **Document findings**: Create comprehensive analysis
5. **Suggest improvements**: Recommend optimizations (without implementing)
6. **Provide examples**: Show how to use the existing system

### 3. Sample Framework Output - Analysis Phase
```
🔍 ANALYZING AUTHENTICATION SYSTEM...

📁 SCANNING CODEBASE:
- Found authentication models in: src/auth/models.py
- Found authentication views in: src/auth/views.py
- Found authentication serializers in: src/auth/serializers.py
- Found authentication URLs in: src/auth/urls.py
- Found authentication middleware in: src/middleware/auth.py
- Found authentication tests in: tests/auth/
- Found authentication templates in: templates/auth/

🔗 DEPENDENCY ANALYSIS:
- Uses Django's built-in authentication
- Extends User model with UserProfile
- Integrates with Django REST Framework
- Uses JWT tokens for API authentication
- Implements custom permissions system
```

### 4. Detailed System Analysis
```
📋 AUTHENTICATION SYSTEM ANALYSIS

## Architecture Overview
The authentication system follows Django best practices with custom extensions:

1. **User Model Extension**
   - Location: `src/auth/models.py`
   - Extends Django's User model via UserProfile
   - Adds: phone, date_of_birth, email_verified, two_factor_enabled

2. **Authentication Flow**
   - Web: Session-based authentication
   - API: JWT token authentication
   - Mobile: JWT with refresh tokens

3. **Security Features**
   - Password strength validation
   - Email verification required
   - Rate limiting on login attempts
   - Two-factor authentication (optional)
   - Session timeout configuration

## Key Components

### Models (`src/auth/models.py`)
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    two_factor_enabled = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
```

### Authentication Views (`src/auth/views.py`)
```python
class LoginView(APIView):
    def post(self, request):
        # Custom login logic with rate limiting
        # Returns JWT token on success
        pass

class RegisterView(APIView):
    def post(self, request):
        # User registration with email verification
        pass

class VerifyEmailView(APIView):
    def post(self, request):
        # Email verification logic
        pass
```

### Custom Permissions (`src/auth/permissions.py`)
```python
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read permissions for any request
        # Write permissions only to owner
        pass

class IsEmailVerified(BasePermission):
    def has_permission(self, request, view):
        # Require email verification for certain actions
        pass
```

## Authentication Middleware

The project uses custom middleware for authentication:

### JWT Middleware (`src/middleware/auth.py`)
- Extracts JWT tokens from request headers
- Validates token signature and expiration
- Sets request.user for authenticated requests
- Handles token refresh logic

### Rate Limiting Middleware
- Prevents brute force attacks
- Configurable limits per IP/user
- Integrates with Redis for distributed rate limiting

## URL Configuration

### Authentication URLs (`src/auth/urls.py`)
```python
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh-token/', RefreshTokenView.as_view(), name='refresh-token'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
```

## Database Schema

### User-Related Tables
1. `auth_user` - Django's built-in user table
2. `auth_userprofile` - Extended user information
3. `auth_emailverification` - Email verification tokens
4. `auth_loginattempt` - Failed login tracking
5. `auth_refreshtoken` - JWT refresh tokens

## Security Implementation

### Password Security
- Minimum 8 characters
- Requires uppercase, lowercase, numbers, symbols
- Uses Django's PBKDF2 hashing
- Password history tracking (last 5 passwords)

### Token Security
- JWT tokens with 15-minute expiration
- Refresh tokens with 7-day expiration
- Token rotation on refresh
- Blacklist for revoked tokens

### Rate Limiting
- 5 login attempts per IP per minute
- 10 registration attempts per IP per hour
- Progressive backoff for repeated failures

## Testing Coverage

### Test Files Location: `tests/auth/`
- `test_models.py` - Model validation tests
- `test_views.py` - API endpoint tests
- `test_permissions.py` - Permission logic tests
- `test_middleware.py` - Middleware functionality tests
- `test_security.py` - Security feature tests

### Current Test Coverage: 94%
- Models: 98% coverage
- Views: 92% coverage
- Permissions: 96% coverage
- Middleware: 90% coverage
```

### 5. Usage Examples
```
💡 USAGE EXAMPLES

## For Developers

### 1. Authenticating API Requests
```python
# Get JWT token
response = requests.post('/api/auth/login/', {
    'username': 'user@example.com',
    'password': 'password123'
})
token = response.json()['access_token']

# Use token in subsequent requests
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('/api/protected/', headers=headers)
```

### 2. Checking User Permissions
```python
# In your views
from auth.permissions import IsEmailVerified

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated, IsEmailVerified]
    
    def get(self, request):
        # Only authenticated, verified users can access
        pass
```

### 3. Extending User Profile
```python
# Access user profile
user_profile = request.user.userprofile
if user_profile.two_factor_enabled:
    # Handle 2FA logic
    pass
```

## For Frontend Integration

### 1. Login Flow
```javascript
// Login request
const loginUser = async (email, password) => {
  const response = await fetch('/api/auth/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: email, password })
  });
  
  const data = await response.json();
  localStorage.setItem('access_token', data.access_token);
  localStorage.setItem('refresh_token', data.refresh_token);
};
```

### 2. Token Refresh
```javascript
// Auto-refresh tokens
const refreshToken = async () => {
  const refresh = localStorage.getItem('refresh_token');
  const response = await fetch('/api/auth/refresh-token/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh_token: refresh })
  });
  
  const data = await response.json();
  localStorage.setItem('access_token', data.access_token);
};
```
```

### 6. Architecture Insights
```
🏗️ ARCHITECTURAL INSIGHTS

## Strengths
✅ Follows Django best practices
✅ Comprehensive security implementation
✅ Well-tested with high coverage
✅ Separation of concerns (models, views, permissions)
✅ Extensible user profile system
✅ Both web and API authentication support

## Areas for Improvement
⚠️ JWT tokens could use shorter expiration
⚠️ Missing social authentication integration
⚠️ Rate limiting could be more granular
⚠️ Password reset flow lacks additional security
⚠️ No audit logging for authentication events

## Integration Points
🔗 Connects to: User management, Order system, Admin interface
🔗 Dependencies: Django REST Framework, Redis, Celery
🔗 External services: Email service, SMS provider (for 2FA)

## Configuration Files
📝 Settings: `settings/auth.py`
📝 Environment: `.env` (JWT secrets, Redis config)
📝 Celery: `celery_config.py` (async email sending)
```

### 7. Recommended Next Steps
```
🎯 RECOMMENDATIONS

## Immediate Actions
1. **Security Review**: Audit JWT token expiration times
2. **Documentation**: Update API documentation with auth examples
3. **Testing**: Add integration tests for complete auth flows
4. **Monitoring**: Implement authentication event logging

## Future Enhancements
1. **Social Auth**: Add Google/Facebook login options
2. **Biometrics**: Support for fingerprint/face authentication
3. **SSO**: Single sign-on integration for enterprise
4. **Audit Trail**: Comprehensive authentication event logging

## Code Quality
1. **Refactoring**: Extract common validation logic
2. **Type Hints**: Add type annotations for better IDE support
3. **Error Handling**: Standardize error responses
4. **Performance**: Optimize token validation queries

## Related Queries to Try
- `/query "how does the user registration flow work?"`
- `/query "what are the security vulnerabilities in this auth system?"`
- `/query "how can I integrate social authentication?"`
```

### 8. Dependencies and Relationships
```
📊 SYSTEM DEPENDENCIES

## Direct Dependencies
- Django Authentication Framework
- Django REST Framework
- PyJWT for token handling
- Redis for rate limiting
- Celery for async tasks

## Dependent Systems
- User Profile Management
- Order Processing System
- Admin Interface
- API Gateway
- Mobile Application

## Configuration Dependencies
- Environment variables for JWT secrets
- Redis configuration for rate limiting
- Email service configuration
- SMS service for 2FA
```

## Key Learning Points

### ✅ What the Framework Does Well
- **No Code Changes**: Pure analysis without modifications
- **Comprehensive Understanding**: Maps entire system architecture
- **Security Focus**: Identifies security patterns and vulnerabilities
- **Practical Examples**: Shows how to actually use the system
- **Integration Awareness**: Understands how components connect

### 📚 Best Practices Demonstrated
1. **Research Before Change**: Understand before modifying
2. **System Mapping**: Visualize component relationships
3. **Security Analysis**: Identify security patterns and gaps
4. **Usage Documentation**: Provide practical examples
5. **Improvement Suggestions**: Recommend optimizations

### 🔍 Command Variations to Try
```bash
# More specific analysis
/query "what are the security vulnerabilities in the auth system?"

# Different focus areas
/query "how does the database schema support the auth system?"

# Integration focused
/query "how does authentication integrate with the order system?"

# Performance focused
/query "what are the performance bottlenecks in authentication?"
```

## Next Steps

1. **Deep Dive**: Use more specific queries for detailed analysis
2. **Security Review**: Focus on security aspects with targeted queries
3. **Integration Planning**: Understand how to integrate new features
4. **Performance Optimization**: Analyze performance characteristics

## Common Patterns

### When to Use `/query`
- ✅ Understanding existing code
- ✅ Security analysis
- ✅ Architecture review
- ✅ Integration planning
- ✅ Performance analysis

### When to Use Other Commands
- `/task` for implementing specific changes
- `/feature` for adding new functionality
- `/auto` when ready to make changes but unsure of approach

This example demonstrates the `/query` command's power for comprehensive code analysis and understanding without making any modifications to your codebase.