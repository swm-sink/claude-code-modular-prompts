# /protocol - Production-Ready Development

**Purpose**: Enforce production standards with mandatory TDD, security reviews, and performance validation for enterprise systems.

## When to Use

Use `/protocol` for:
- Production feature development
- High-stakes implementations
- Financial systems
- Healthcare applications
- Regulated environments
- Mission-critical code

## Session Management

- **Always creates session** for production work
- **Tracks all quality gates** in session
- **Documents design decisions** and ADRs
- **Links compliance artifacts**
- **Mandatory for audit trail**

## Strict Enforcement

### Mandatory Requirements
1. **TDD Coverage**: 95% minimum
2. **Security Review**: Threat model required
3. **Performance Baseline**: <200ms p95
4. **Documentation**: API and architecture
5. **Error Handling**: Comprehensive
6. **Monitoring**: Metrics and alerts

### Quality Gates
```python
# Automated checks before completion
PROTOCOL_GATES = {
    "tests_pass": True,           # All tests green
    "coverage_met": ">= 95%",     # Line coverage
    "security_scan": "pass",      # No vulnerabilities
    "performance": "< 200ms",     # Response time
    "docs_complete": True,        # All docs updated
    "code_review": "approved"     # Peer reviewed
}
```

## Development Phases

### 1. Design Phase
```markdown
# Mandatory design documents
- Architecture Decision Record (ADR)
- Threat Model (STRIDE)
- Performance Budget
- API Specification
- Test Strategy
```

### 2. Implementation Phase
```python
# TDD with comprehensive scenarios
- Happy path tests
- Edge case tests
- Error condition tests
- Performance tests
- Security tests
- Integration tests
```

### 3. Validation Phase
```bash
# Automated validation suite
- Unit test execution
- Integration test execution
- Security scanning (SAST/DAST)
- Performance benchmarking
- Documentation generation
- Compliance checking
```

### 4. Deployment Phase
```yaml
# Production readiness checklist
deployment:
  - feature_flags: configured
  - rollback_plan: documented
  - monitoring: enabled
  - alerts: configured
  - runbook: created
  - capacity: validated
```

## Security Requirements

### Threat Modeling
```python
# STRIDE analysis for every feature
threats = {
    "Spoofing": "Multi-factor authentication",
    "Tampering": "Request signing + audit logs",
    "Repudiation": "Non-repudiable audit trail",
    "Information Disclosure": "Encryption + access control",
    "Denial of Service": "Rate limiting + circuit breakers",
    "Elevation of Privilege": "Least privilege + RBAC"
}
```

### Security Controls
```python
# Mandatory for data handling
@require_encryption
@audit_log
@access_control("data.read")
@rate_limit(100, 60)  # 100 req/min
async def get_sensitive_data(user_id: UUID):
    # Input validation
    # Authorization check
    # Data masking
    # Audit trail
```

## Performance Standards

### Benchmarking
```python
# Required for all endpoints
@benchmark
async def api_endpoint():
    # Measure: Response time
    # Measure: Memory usage
    # Measure: CPU usage
    # Alert if > 200ms
```

### Optimization Requirements
```python
# Database queries
- Use indexes
- Avoid N+1
- Implement pagination
- Cache appropriately

# API responses  
- Compress large payloads
- Use ETags
- Implement partial responses
- Stream when appropriate
```

## Error Handling

### Comprehensive Coverage
```python
# Every possible error handled
try:
    result = await process_payment(amount)
except InsufficientFundsError:
    # Specific handling
    await notify_user(error_type="insufficient_funds")
except PaymentGatewayError:
    # Retry with backoff
    await retry_with_backoff(process_payment, amount)
except Exception as e:
    # Generic handling with monitoring
    await alert_oncall(error=e)
    raise ServiceUnavailableError()
```

### Error Response Standards
```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "User-friendly message",
    "details": {
      "field": "email",
      "reason": "Invalid format"
    },
    "request_id": "uuid",
    "documentation": "https://api.docs/errors#INVALID_INPUT"
  }
}
```

## Documentation Requirements

### API Documentation
```python
# OpenAPI/Swagger required
@router.post(
    "/users",
    response_model=UserResponse,
    status_code=201,
    summary="Create a new user",
    description="""
    Creates a new user account with the provided details.
    Sends welcome email on success.
    """,
    responses={
        201: {"description": "User created successfully"},
        400: {"description": "Invalid input data"},
        409: {"description": "User already exists"}
    }
)
```

### Architecture Documentation
```markdown
# Required documents
1. System Architecture Diagram
2. Data Flow Diagrams  
3. Deployment Architecture
4. Disaster Recovery Plan
5. Scaling Strategy
```

## Monitoring & Observability

### Metrics Collection
```python
# Business metrics
record_metric("user.signup", 1, tags={"plan": "premium"})
record_metric("payment.processed", amount, tags={"currency": "USD"})

# Technical metrics
record_metric("api.latency", response_time, tags={"endpoint": "/users"})
record_metric("db.query.time", query_time, tags={"query": "get_user"})
```

### Alerting Rules
```yaml
alerts:
  - name: high_error_rate
    condition: error_rate > 1%
    duration: 5m
    severity: critical
    
  - name: slow_response
    condition: p95_latency > 200ms
    duration: 10m
    severity: warning
```

## Compliance Features

### Audit Logging
```python
# Every significant action logged
@audit_log(
    action="user.data.access",
    pii_fields=["email", "ssn"],
    retention_days=2555  # 7 years
)
async def access_user_data(user_id: UUID):
    # Compliance-ready logging
    # Immutable audit trail
    # Searchable by compliance team
```

### Data Governance
```python
# GDPR compliance built-in
@personal_data(
    purpose="authentication",
    legal_basis="consent",
    retention_period="90_days_after_deletion"
)
class User:
    email: str
    name: str
```

## Examples

### Financial Transaction
```bash
/protocol "Implement wire transfer processing"
# Auto-creates session #129 "Protocol: Wire Transfer System"

# Enforces:
- PCI DSS compliance → Session: "PCI checklist complete"
- SOX audit requirements → Session: "SOX controls implemented"
- 99.99% accuracy requirement → Session: "Error rate: 0.001%"
- Sub-second processing → Session: "p95: 450ms achieved"
- Complete audit trail → Session: "Immutable logs verified"
# Session closed only when ALL gates pass
```

### Healthcare Feature
```bash
/protocol "Add patient record system"

# Ensures:
- HIPAA compliance
- Encryption at rest/transit
- Access control audit
- Data integrity checks
- Disaster recovery plan
```

## Token Optimization
- Production-focused guidance
- Compliance checklists
- Security patterns emphasized
- Max 12k tokens for complex systems