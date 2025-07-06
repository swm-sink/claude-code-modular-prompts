# /security - Financial-Grade Security Command

**Purpose**: Implement enterprise security patterns for financial systems, ensuring PCI DSS, SOX, and GDPR compliance.

## When to Use

Use `/security` for:
- Payment processing systems
- Authentication/authorization
- Data encryption requirements
- Compliance implementations
- Security audits
- Threat modeling

## Session Management

- **Recommends sessions** for compliance work (PCI DSS, SOX, GDPR)
- **Auto-creates session** for full security implementations
- **Tracks compliance checklist** in session updates
- **Documents security decisions** for audit trails
- Use `/session start` for major security features

## Compliance Standards

### PCI DSS Requirements
- Secure network configuration
- Cardholder data protection
- Vulnerability management
- Access control measures
- Regular monitoring
- Security policy

### SOX Compliance
- Access controls
- Audit trails
- Data integrity
- Change management
- Separation of duties

### GDPR Requirements  
- Data minimization
- Purpose limitation
- Consent management
- Right to erasure
- Data portability

## Security Patterns

### Authentication
```python
# Multi-factor authentication
class MFAAuthenticator:
    def authenticate(self, credentials: Credentials, mfa_token: str):
        # Time-based OTP validation
        # Rate limiting
        # Brute force protection
        # Session management
```

### Authorization
```python
# Role-based access control (RBAC)
@require_permission("payment.process")
@require_role(["admin", "payment_processor"])
def process_payment(amount: Decimal, card_token: str):
    # Audit log entry
    # Permission check
    # Data validation
```

### Encryption
```python
# Field-level encryption for PII
class EncryptedField:
    # AES-256-GCM encryption
    # Key rotation support
    # HSM integration
    # Audit trail
```

## Common Implementations

### Payment Processing
```bash
/security "Implement PCI-compliant payment system"

# Creates:
- Tokenization service
- Encrypted card vault
- Audit logging
- Network segmentation
- Key management
```

### User Authentication
```bash
/security "Add OAuth2 with MFA"

# Implements:
- OAuth2 authorization server
- TOTP/SMS second factor
- Session management
- Brute force protection
- Account lockout policies
```

### Data Protection
```bash
/security "Implement GDPR-compliant data handling"

# Provides:
- Consent management
- Data encryption at rest
- Pseudonymization
- Audit trails
- Data retention policies
```

## Security Audit Mode

```bash
/security --audit "Review application security"

# Analyzes:
- OWASP Top 10 vulnerabilities
- Dependency vulnerabilities
- Access control gaps
- Encryption weaknesses
- Compliance violations
```

### Audit Output
```
Security Audit Report
────────────────────

Critical Issues (2):
✗ SQL injection in UserRepository.find()
✗ Plaintext password in logs

High Priority (3):
⚠ Missing rate limiting on /api/auth
⚠ Outdated crypto library (CVE-2023-...)
⚠ Insufficient session timeout

Compliance Gaps:
✗ PCI DSS 3.4: Card data not encrypted
⚠ GDPR Art.25: No privacy by design
```

## Threat Modeling

### STRIDE Analysis
- **S**poofing identity
- **T**ampering with data
- **R**epudiation
- **I**nformation disclosure
- **D**enial of service
- **E**levation of privilege

### Implementation
```python
# Threat mitigation example
@rate_limit(calls=5, period=60)  # DoS protection
@require_https  # Spoofing protection
@sign_request  # Tampering protection
@audit_log  # Repudiation protection
def sensitive_operation():
    pass
```

## Security Standards

### Password Policy
```python
# NIST 800-63B compliant
PASSWORD_REQUIREMENTS = {
    "min_length": 12,
    "require_uppercase": False,  # NIST deprecated
    "require_special": False,    # NIST deprecated
    "check_breach_list": True,   # HaveIBeenPwned
    "prevent_common": True,      # Dictionary check
}
```

### API Security
```python
# OAuth2 + JWT with refresh tokens
@app.post("/auth/token")
@rate_limit(5, 300)  # 5 attempts per 5 minutes
async def login(credentials: OAuth2PasswordRequest):
    # Validate credentials
    # Generate access token (15 min)
    # Generate refresh token (7 days)
    # Audit log attempt
```

### Data Classification
```python
class DataClassification(Enum):
    PUBLIC = "public"
    INTERNAL = "internal"  
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"  # PII, payment data

# Automatic encryption for restricted data
@dataclass
class User:
    email: Annotated[str, DataClassification.CONFIDENTIAL]
    ssn: Annotated[str, DataClassification.RESTRICTED, Encrypted()]
```

## Examples

### Secure API Endpoint
```bash
/security "Create secure payment endpoint"

# Implements:
- Input validation
- Rate limiting
- Authentication check
- Authorization check
- Audit logging
- Error handling (no data leaks)
- Response signing
```

### Compliance Implementation
```bash
/security "Implement SOX compliance for financial reports"
# Auto-creates session #127 "SOX Compliance Implementation"

# Creates:
- Role separation → Updates session: "Implemented role matrix"
- Approval workflows → Updates session: "Added 2-factor approval"
- Immutable audit logs → Updates session: "Audit trail complete"
- Change tracking → Updates session: "Change log integrated"
- Access reviews → Updates session: "Quarterly review process"
# Completes session with compliance checklist
```

## Best Practices

1. **Defense in depth** - Multiple security layers
2. **Least privilege** - Minimal required access
3. **Fail secure** - Deny by default
4. **Audit everything** - Comprehensive logging
5. **Regular reviews** - Continuous improvement

## Token Optimization
- Security-focused responses
- Compliance checklists included
- Code examples minimal but complete
- Max 10k tokens per implementation