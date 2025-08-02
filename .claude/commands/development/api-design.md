---
name: /api-design
description: Design RESTful APIs with enterprise patterns and automated scaffolding (v1.0)
version: "1.0"
usage: '/api-design [endpoint-name] [http-method] [options]'
category: development
allowed-tools:
- Write
- Edit
- Read
- Grep
- Bash
dependencies:
- /dev-setup
- /protocol
- /test
validation:
  pre-execution: "Validate API design patterns and REST compliance"
  during-execution: "Monitor schema validation and endpoint consistency"
  post-execution: "Verify generated API documentation and test coverage"
progressive-disclosure:
  layer-integration: "Layer 1: Basic endpoints, Layer 2: Authentication/validation, Layer 3: Full API architecture"
  options:
    - name: basic
      description: "Simple CRUD endpoints with standard patterns"
    - name: advanced
      description: "Complex APIs with versioning, pagination, filtering"
    - name: enterprise
      description: "Full API gateway with rate limiting, caching, monitoring"
safety-checks:
  - "SQL injection prevention in query builders"
  - "Authentication token validation"
  - "Rate limiting configuration"
  - "CORS policy verification"
error-recovery:
  - "Rollback API changes on validation failure"
  - "Generate API migration scripts"
  - "Preserve existing endpoint functionality"
performance:
  - "Response time optimization"
  - "Database query efficiency"
  - "Caching strategy implementation"
---

# API Design for lusaka (v1.0)

I'll help you design **RESTful** APIs with enterprise-grade patterns, automated scaffolding, and comprehensive validation.

## 🚀 Progressive Disclosure Layers

### Layer 1: Quick API Generation (30 seconds)
```bash
/api-design users GET    # Generate basic user list endpoint
/api-design posts POST   # Create post creation endpoint
```

### Layer 2: Enhanced API Features (5 minutes)
```bash
/api-design users GET --with-pagination --with-filtering
/api-design auth POST --with-jwt --with-refresh-tokens
```

### Layer 3: Enterprise Architecture (15-30 minutes)
```bash
/api-design --enterprise --with-gateway --with-monitoring
```

## Project API Configuration
- **API Style**: RESTful with OpenAPI 3.0 specification
- **Primary Language**: Python with type hints
- **Database**: PostgreSQL with connection pooling
- **Authentication**: JWT with refresh tokens
- **Documentation**: Auto-generated Swagger/ReDoc

## 🛡️ Security-First Design

### Authentication & Authorization
- JWT token validation with expiry
- Role-based access control (RBAC)
- API key management for services
- OAuth2 integration ready

### Security Headers
```python
# Automated security headers
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'
```

## 📋 API Design Patterns

### RESTful Best Practices
- Consistent naming conventions (`/api/v1/resources`)
- Proper HTTP status codes
- HATEOAS support
- Content negotiation

### Response Format
```json
{
  "data": {...},
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "version": "1.0",
    "pagination": {...}
  },
  "errors": []
}
```

## 🔧 Integration Features

### Database Integration
- Automatic migration generation
- Query optimization hints
- Connection pool management
- Transaction handling

### Testing Integration
```bash
# Auto-generated test suites
pytest tests/api/test_endpoints.py
pytest tests/api/test_authentication.py
pytest tests/api/test_validation.py
```

## 📊 Performance Optimization

### Caching Strategy
- Redis integration for response caching
- ETags for conditional requests
- Cache invalidation patterns
- CDN-ready headers

### Rate Limiting
```python
# Configurable rate limits
@rate_limit("100/hour")
@rate_limit("10/minute") 
def api_endpoint():
    pass
```

## 🚨 Error Handling

### Structured Error Responses
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [{
      "field": "email",
      "issue": "Invalid email format"
    }]
  }
}
```

## 📝 Auto-Generated Documentation

### OpenAPI Specification
- Interactive API explorer
- Code generation for clients
- Postman collection export
- API versioning support

## 🎯 Quick Start Examples

### Basic CRUD API
```bash
/api-design products --crud --with-validation
```

### Authenticated API
```bash
/api-design orders --auth-required --roles="admin,user"
```

### Microservice API
```bash
/api-design payment-service --microservice --with-events
```

---

What API endpoint would you like to design for lusaka? I can help with:
- 🚀 Quick endpoint generation
- 🔒 Secure API patterns  
- 📊 Performance optimization
- 🧪 Test suite generation
- 📝 API documentation