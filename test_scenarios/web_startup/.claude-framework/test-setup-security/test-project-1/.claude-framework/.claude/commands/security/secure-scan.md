---
name: /secure-scan
description: "Security scanning for [INSERT_PROJECT_NAME] with [INSERT_SECURITY_LEVEL] requirements"
usage: /secure-scan [--type vulnerability|sast|dast|all] [--severity critical|high|medium|low]
category: security
tools: Bash, Read, Write, Grep
---

# Security Scanning for [INSERT_PROJECT_NAME]

I'll perform comprehensive security scanning appropriate for your **[INSERT_SECURITY_LEVEL]** security requirements and **[INSERT_USER_BASE]** user base.

## Security Configuration

- **Project**: [INSERT_PROJECT_NAME]
- **Security Level**: [INSERT_SECURITY_LEVEL]
- **Tech Stack**: [INSERT_TECH_STACK]
- **Primary Language**: [INSERT_PRIMARY_LANGUAGE]
- **API Style**: [INSERT_API_STYLE]

## Scan Types

### Vulnerability Scanning
Scan dependencies for [INSERT_PRIMARY_LANGUAGE]:
```bash
/secure-scan --type vulnerability
```

### Static Analysis (SAST)
Code security analysis for [INSERT_TECH_STACK]:
```bash
/secure-scan --type sast
```

### Dynamic Analysis (DAST)
Runtime security testing for [INSERT_API_STYLE] APIs:
```bash
/secure-scan --type dast
```

### Comprehensive Scan
All security checks for [INSERT_SECURITY_LEVEL]:
```bash
/secure-scan --type all
```

## Security Requirements

### [INSERT_SECURITY_LEVEL] Level Checks
Your security level mandates:
- OWASP Top 10 coverage
- Dependency vulnerability scanning
- Secret detection
- Configuration security
- Access control validation

## Compliance for [INSERT_USER_BASE]

Based on your user base:
- Data protection requirements
- Privacy compliance
- Audit logging
- Encryption standards
- Access controls

## Integration with [INSERT_CI_CD_PLATFORM]

Automated security gates:
- Pre-commit secret scanning
- PR security validation
- Build-time SAST
- Deployment security checks
- Continuous monitoring

## Remediation Guidance

For [INSERT_TEAM_SIZE] teams:
- Prioritized findings
- Fix recommendations
- Code examples
- Security best practices
- Team training needs

## Reporting

Security reports tailored for:
- Development team
- Security team
- Management overview
- Compliance documentation
- [INSERT_WORKFLOW_TYPE] tracking

What type of security scan would you like to run?