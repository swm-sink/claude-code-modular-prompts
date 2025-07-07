# Production Standards - Quality Gates

**Purpose**: Define mandatory quality, security, and performance standards for production code.

## Quality Gates

### Before Code Complete
```
✓ All tests passing
✓ Coverage ≥90%
✓ Zero linting errors
✓ Type checking passes
✓ Documentation updated
✓ Session shows TDD compliance
```

### Before Deployment
```
✓ Security scan passed
✓ Performance validated
✓ Error handling complete
✓ Monitoring configured
✓ Rollback plan ready
✓ Session completed with outcomes
```

## Security Requirements

### Data Protection
```python
# Mandatory for sensitive data
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3+)
- Field-level encryption for PII
- Secure key management
```

### Authentication & Authorization
```python
# Required patterns
- Multi-factor authentication
- Role-based access control
- Session management
- Rate limiting
- Audit logging
```

### Common Vulnerabilities
```
✓ SQL injection prevention
✓ XSS protection  
✓ CSRF tokens
✓ Input validation
✓ Output encoding
```

## Performance Standards

### Response Time
- **API Endpoints**: <200ms (p95)
- **Web Pages**: <3s initial load
- **Database Queries**: <100ms
- **Background Jobs**: SLA defined

### Resource Usage
```yaml
limits:
  memory: <512MB per instance
  cpu: <80% sustained
  connections: Pooled and limited
  disk: Monitored and alerted
```

### Optimization Requirements
- Database queries indexed
- N+1 queries eliminated
- Caching strategy defined
- CDN for static assets

## Error Handling

### Comprehensive Coverage
```python
try:
    result = risky_operation()
except SpecificError as e:
    # Specific handling
    log_error(e, context)
    return graceful_fallback()
except Exception as e:
    # Generic handling
    alert_oncall(e)
    return safe_default()
finally:
    # Cleanup always runs
    release_resources()
```

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User-friendly message",
    "details": {...},
    "request_id": "uuid",
    "help": "link_to_docs"
  }
}
```

## Monitoring & Observability

### Required Metrics
```python
# Business metrics
- User actions
- Transaction volumes
- Error rates
- Success rates

# Technical metrics  
- Response times
- Resource usage
- Queue depths
- Cache hit rates
```

### Logging Standards
```python
logger.info("action_completed", 
    user_id=user.id,
    action="purchase",
    amount=100.00,
    duration_ms=45
)
```

### Alerting Rules
```yaml
- metric: error_rate > 1%
  window: 5m
  severity: warning

- metric: response_time_p95 > 500ms  
  window: 10m
  severity: critical
```

## Documentation Requirements

### Session Integration
- Development sessions tracked in GitHub issues
- Major decisions documented in session
- TDD cycle progress recorded
- Deployment linked to development session

### Code Documentation
```python
def process_payment(
    amount: Decimal,
    currency: str,
    card_token: str
) -> PaymentResult:
    """Process a payment transaction.
    
    Args:
        amount: Payment amount in minor units
        currency: ISO 4217 currency code
        card_token: Tokenized card from vault
        
    Returns:
        PaymentResult with transaction details
        
    Raises:
        InsufficientFunds: If account balance too low
        PaymentGatewayError: If gateway unavailable
    """
```

### API Documentation
- OpenAPI/Swagger spec
- Example requests/responses
- Error scenarios
- Rate limits
- Authentication

## Deployment Checklist

### Pre-deployment
```
□ Feature flags configured
□ Database migrations tested
□ Performance benchmarked
□ Security scan completed
□ Documentation updated
□ AI session linked to deployment
```

### Deployment Process
```
□ Blue-green deployment
□ Canary rollout (5% → 25% → 100%)
□ Health checks passing
□ Metrics normal
□ No error spike
```

### Post-deployment
```
□ Monitor metrics for 30min
□ Check error rates
□ Verify performance
□ Update status page
□ Notify stakeholders
□ Update session with deployment results
```

## Compliance

### Data Privacy (GDPR)
- Data minimization
- Purpose limitation  
- Consent management
- Right to deletion
- Audit trail

### Financial (PCI DSS)
- No card data storage
- Tokenization required
- Network segmentation
- Access logging
- Regular audits

## Best Practices

1. **Fail Safe**: Default to secure state
2. **Defense in Depth**: Multiple layers
3. **Least Privilege**: Minimal access
4. **Audit Everything**: Complete trail
5. **Monitor Proactively**: Alert before issues
6. **Track Development**: AI sessions for context
7. **Link Everything**: Sessions to PRs to deployments

These standards are mandatory for production code.