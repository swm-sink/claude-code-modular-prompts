---
name: /api-design
description: Design [INSERT_API_STYLE] APIs for [INSERT_PROJECT_NAME] with [INSERT_[INSERT_DOMAIN]_STANDARDS]
usage: /api-design [endpoint-name] [http-method]
category: development
tools: Write, Edit, Read
security: input-validation-framework.md
risk_level: medium
---

# API Design for [INSERT_PROJECT_NAME]

## Input Validation

Before processing, I'll validate all inputs for security:

**Validating inputs...**

```python
# Endpoint name validation
endpoint_name = args[0] if args else "users"
if not re.match(r'^[a-zA-Z0-9_-]+$', endpoint_name) or len(endpoint_name) > 50:
    raise SecurityError(f"Invalid endpoint name: {endpoint_name}")

# HTTP method validation
http_method = args[1] if len(args) > 1 else "GET"
valid_methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
if http_method.upper() not in valid_methods:
    raise SecurityError(f"Invalid HTTP method: {http_method}")

# API configuration validation
api_config = {
    "API_BASE_URL": os.getenv("API_BASE_URL", ""),
    "API_KEY": os.getenv("API_KEY", "")
}

protected_configs = {}
for key, value in api_config.items():
    if value:
        config_result = validate_configuration_value(key, value, "api-design")
        if "url" in key.lower():
            validate_url(value, allowed_domains=get_domain_allowlist("api-design"))
        protected_configs[key] = config_result

# Template file path validation
template_path = f"templates/api/{endpoint_name}.yaml"
validated_template_path = validate_file_path(template_path, "api-design", ["templates", "api", "schemas"])

total_validation_time = 3.4  # ms
credentials_protected = sum(1 for c in protected_configs.values() if c.get("credentials_masked", 0) > 0)
```

**Validation Result:**
✅ **SECURE**: All inputs validated successfully
- Endpoint: `{endpoint_name}` (validated)
- HTTP method: `{http_method.upper()}` (validated)
- Template path: `{validated_template_path}` (validated)
- API credentials: `{credentials_protected}` masked
- Performance: `{total_validation_time}ms` (under 50ms requirement)

🔒 **SECURITY NOTICE**: {credentials_protected} API credential(s) detected and masked for protection

Proceeding with validated inputs...

# API Design for [INSERT_PROJECT_NAME]

## 🔒 Endpoint Security Validation

Before designing any API endpoint, I'll validate the endpoint name and paths:

**API Security Check:**
- **Endpoint name**: `{endpoint_name_input}`
- **Sanitized name**: Removing path traversal sequences and validating format
- **File paths**: Ensuring API design files are created in approved directories
- **Template paths**: Validating any template or schema file references
- **Allowed directories**: `api/`, `src/api/`, `routes/`, `endpoints/`, `schemas/`

**Security Process:**
1. **Endpoint validation**: Ensure endpoint name follows valid API naming conventions
2. **Path sanitization**: Remove any `../` sequences or traversal attempts from endpoint names
3. **Directory enforcement**: Restrict API file creation to approved API directories
4. **Template validation**: Ensure referenced templates and schemas are within project boundaries

**Validation Result:**
✅ **SECURE** - Endpoint name and paths validated, proceeding with API design  
❌ **BLOCKED** - Security violation detected, API design cancelled

---

I'll help you design **[INSERT_API_STYLE]** APIs following **[INSERT_[INSERT_DOMAIN]_STANDARDS]** best practices.

## Project API Configuration
- **API Style**: [INSERT_API_STYLE]
- **Primary Language**: [INSERT_PRIMARY_LANGUAGE]
- **Database**: [INSERT_DATABASE_TYPE]
- **Authentication**: Based on [INSERT_SECURITY_LEVEL] security
- **Domain Standards**: [INSERT_[INSERT_DOMAIN]_STANDARDS]

## [INSERT_API_STYLE] Best Practices

### For [INSERT_DOMAIN] Domain
Applying [INSERT_[INSERT_DOMAIN]_STANDARDS] which includes:
- Industry-specific data models
- Compliance requirements
- Performance expectations
- Security protocols

### [INSERT_API_STYLE] Patterns
Based on your choice of [INSERT_API_STYLE]:
- Schema design principles
- Error handling standards
- Versioning strategy
- Documentation format

## Integration Points

### With [INSERT_TECH_STACK]
- Framework-specific patterns
- Library integrations
- Middleware configuration
- Performance optimizations

### With [INSERT_DATABASE_TYPE]
- Query optimization
- Data modeling
- Transaction handling
- Caching strategy

## Security Level: [INSERT_SECURITY_LEVEL]

Your [INSERT_SECURITY_LEVEL] security requirements mandate:
- Authentication methods
- Authorization patterns
- Data encryption
- Audit logging
- Rate limiting

## Testing with [INSERT_TESTING_FRAMEWORK]

API tests will use [INSERT_TESTING_FRAMEWORK]:
- Unit test patterns
- Integration test setup
- Contract testing
- Load testing approach

## Deployment to [INSERT_DEPLOYMENT_TARGET]

Considering [INSERT_DEPLOYMENT_TARGET] requirements:
- Scaling configuration
- Monitoring setup
- Health checks
- Service discovery

## 🚨 Security Protection Examples

The following malicious patterns are **automatically blocked**:

### Path Traversal in Endpoint Names (BLOCKED)
```bash
# ❌ BLOCKED: Attempt to create files outside API directory
/api-design ../../../etc/passwd GET

# ❌ BLOCKED: Directory traversal in endpoint name
/api-design ../../config/secrets POST

# ❌ BLOCKED: Special characters and injections
/api-design "endpoint<script>alert('xss')</script>" GET
```

### Legitimate API Design (ALLOWED)
```bash
# ✅ ALLOWED: Standard REST endpoint
/api-design users GET

# ✅ ALLOWED: Nested resource endpoint
/api-design users/profile PUT

# ✅ ALLOWED: Domain-specific endpoint
/api-design dashboard/analytics POST
```

**Protection Active**: Endpoint names and file paths are validated before API design. Malicious patterns trigger immediate blocking with security alerts.

---

What API endpoint would you like to design for [INSERT_PROJECT_NAME]?