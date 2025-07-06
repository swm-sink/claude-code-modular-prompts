# /security/audit - Security Auditing Module

**Purpose**: Comprehensive security auditing patterns for enterprise-grade code review and vulnerability assessment.

## Module Interface
- **Trigger**: Security audit requests, code review with security focus
- **Dependencies**: Uses patterns/tool-usage.md for Claude Code optimization
- **Session**: Creates GitHub issue for audit tracking
- **Output**: Security assessment report with actionable recommendations

## Core Capabilities

### Automated Security Scanning
```python
# Multi-tool security analysis
Bash("bandit -r src/ -f json -o security-report.json")
Bash("safety check --json --output safety-report.json") 
Bash("semgrep --config=security src/ --json")
```

### Threat Model Analysis
- Identify attack vectors and entry points
- Data flow security analysis
- Authentication/authorization review
- Input validation assessment
- Encryption and secrets management review

### Compliance Verification
- **PCI DSS**: Payment card industry standards
- **SOX**: Sarbanes-Oxley financial controls
- **GDPR**: Data privacy requirements
- **HIPAA**: Healthcare data protection

## Financial-Grade Standards

### Critical Security Patterns
- Zero-trust architecture validation
- Defense-in-depth implementation
- Principle of least privilege enforcement
- Secure-by-default configuration review

### Vulnerability Categories
1. **Authentication/Authorization** - Session management, token validation
2. **Input Validation** - SQL injection, XSS, CSRF protection
3. **Cryptography** - Encryption standards, key management
4. **Infrastructure** - Container security, network policies
5. **Data Protection** - PII handling, data retention policies

## Session Integration
Auto-creates GitHub issue with:
- Security audit checklist
- Findings and risk levels
- Remediation recommendations
- Compliance status tracking

## Usage Examples
```bash
/security/audit "Review authentication system for SOX compliance"
/security/audit "Full security assessment before production deployment"
```

**Token Budget**: <5k tokens (focused, efficient security patterns)