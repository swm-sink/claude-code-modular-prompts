# Query Command Documentation

## Overview
The `/query` command is designed for research, analysis, and understanding code without making any modifications. Use it to understand existing systems, analyze security, review architecture, and plan integrations.

## When to Use `/query`
- ✅ Understanding existing code
- ✅ Security analysis
- ✅ Architecture review
- ✅ Integration planning
- ✅ Performance analysis

## When to Use Other Commands
- `/task` for implementing specific changes
- `/feature` for adding new functionality
- `/auto` when ready to make changes but unsure of approach

## Usage Syntax
```bash
/query "specific question about your codebase or system"
```

## How It Works
The framework will:
1. **Analyze codebase**: Scan relevant files and components
2. **Map relationships**: Understand how components connect
3. **Identify patterns**: Find architectural patterns and conventions
4. **Document findings**: Create comprehensive analysis
5. **Suggest improvements**: Recommend optimizations (without implementing)
6. **Provide examples**: Show how to use the existing system

## Example Walkthrough

### Scenario: Understanding Django Authentication System
```bash
/query "how does the authentication system work in this Django project?"
```

### Phase 1: Codebase Analysis
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

### Phase 2: System Architecture Analysis
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
```

### Phase 3: Component Analysis
```
## Key Components

### Models (`src/auth/models.py`)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    two_factor_enabled = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

### Authentication Views (`src/auth/views.py`)
class LoginView(APIView):
    def post(self, request):
        # Custom login logic with rate limiting
        # Returns JWT token on success
        pass

class RegisterView(APIView):
    def post(self, request):
        # User registration with email verification
        pass

### Custom Permissions (`src/auth/permissions.py`)
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

### Phase 4: Integration and Usage Examples
```
💡 USAGE EXAMPLES

## For Developers

### 1. Authenticating API Requests
# Get JWT token
response = requests.post('/api/auth/login/', {
    'username': 'user@example.com',
    'password': 'password123'
})
token = response.json()['access_token']

# Use token in subsequent requests
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('/api/protected/', headers=headers)

### 2. Checking User Permissions
from auth.permissions import IsEmailVerified

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated, IsEmailVerified]
    
    def get(self, request):
        # Only authenticated, verified users can access
        pass

### 3. Extending User Profile
# Access user profile
user_profile = request.user.userprofile
if user_profile.two_factor_enabled:
    # Handle 2FA logic
    pass
```

### Phase 5: Architecture Insights
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
```

### Phase 6: Recommendations
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

## Command Variations

### More Specific Analysis
```bash
/query "what are the security vulnerabilities in the auth system?"
```

### Different Focus Areas
```bash
/query "how does the database schema support the auth system?"
```

### Integration Focused
```bash
/query "how does authentication integrate with the order system?"
```

### Performance Focused
```bash
/query "what are the performance bottlenecks in authentication?"
```

## Common Query Types

### Security Analysis
- Identify vulnerabilities and security patterns
- Analyze authentication and authorization flows
- Review security configurations and best practices

### Architecture Review
- Map system components and relationships
- Identify architectural patterns and anti-patterns
- Understand data flow and dependencies

### Integration Planning
- Understand how systems connect
- Identify integration points and APIs
- Plan new feature integration

### Performance Analysis
- Identify performance bottlenecks
- Analyze query patterns and optimizations
- Review caching and scaling strategies

## Next Steps After Query

1. **Deep Dive**: Use more specific queries for detailed analysis
2. **Security Review**: Focus on security aspects with targeted queries
3. **Integration Planning**: Understand how to integrate new features
4. **Implementation**: Use `/task` or `/feature` for actual changes

## Related Queries to Try

After understanding the auth system, you might want to explore:
- `/query "how does the user registration flow work?"`
- `/query "what are the security vulnerabilities in this auth system?"`
- `/query "how can I integrate social authentication?"`
- `/query "what are the performance bottlenecks in authentication?"`

## Related Documentation
- [Task Command](task-command.md) - For implementing specific changes
- [Feature Command](feature-command.md) - For adding new functionality
- [Auto Command](auto-command.md) - For intelligent command selection when ready to make changes