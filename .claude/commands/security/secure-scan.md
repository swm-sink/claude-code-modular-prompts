---
name: /secure-scan
description: Automated security scanning with real-time vulnerability detection and fix suggestions (v2.0)
version: 2.0
usage: '/secure-scan [--type vulnerability|sast|dast|all] [--severity critical|high|medium|low] [--auto-fix] [--continuous]'
category: security
allowed-tools:
- Bash
- Read
- Write
- Grep
- Glob
- Edit
dependencies:
- /validate-component
- /monitor-alerts
- /quick-command
validation:
  pre-execution: Check for security scanning tools and project structure
  during-execution: Monitor scan progress and validate findings
  post-execution: Verify all critical vulnerabilities are addressed
progressive-disclosure:
  layer-integration: Layer 1 quick scans with auto-fix, Layer 2 detailed analysis, Layer 3 custom security rules
  escalation-path: Quick scan → targeted analysis → comprehensive audit
  de-escalation: Auto-fix reduces manual intervention needs
safety-measures:
  - Sanitize all scan outputs
  - Never commit fixes without review
  - Validate all suggested changes
  - Maintain backup before auto-fix
error-recovery:
  scan-timeout: Gracefully handle long-running scans with progress updates
  tool-missing: Suggest alternative scanning methods
  false-positives: Provide filtering and whitelisting options
---

# Code Analysis for [INSERT_PROJECT_NAME]

I'll perform comprehensive code analysis appropriate for your **[INSERT_SECURITY_LEVEL]** requirements and **[INSERT_USER_BASE]** user base.

## Analysis Configuration

- **Project**: [INSERT_PROJECT_NAME]
- **Analysis Level**: [INSERT_SECURITY_LEVEL]
- **Tech Stack**: [INSERT_TECH_STACK]
- **Primary Language**: [INSERT_PRIMARY_LANGUAGE]
- **API Style**: [INSERT_API_STYLE]

## Scan Types

### Dependency Analysis
Analyze dependencies for [INSERT_PRIMARY_LANGUAGE]:
```bash
/secure-scan --type vulnerability
```

### Static Analysis (SAST)
Code pattern analysis for [INSERT_TECH_STACK]:
```bash
/secure-scan --type sast
```

### Dynamic Analysis (DAST)
Runtime behavior analysis for [INSERT_API_STYLE] APIs:
```bash
/secure-scan --type dast
```

### Comprehensive Analysis
All code checks for [INSERT_SECURITY_LEVEL]:
```bash
/secure-scan --type all
```

## Analysis Requirements

### [INSERT_SECURITY_LEVEL] Level Checks
Your analysis level includes:
- OWASP Top 10 patterns
- Dependency compatibility analysis
- Hardcoded value detection
- Configuration review
- Access pattern validation

## Compliance for [INSERT_USER_BASE]

Based on your user base:
- Data protection requirements
- Privacy compliance
- Audit logging
- Encryption standards
- Access controls

## Integration with [INSERT_CI_CD_PLATFORM]

Automated analysis gates:
- Pre-commit pattern scanning
- PR code validation
- Build-time SAST
- Deployment configuration checks
- Continuous monitoring

## Remediation Guidance

For [INSERT_TEAM_SIZE] teams:
- Prioritized findings
- Fix recommendations
- Code examples
- Security best practices
- Team training needs

## Reporting

Analysis reports tailored for:
- Development team
- Quality team
- Management overview
- Compliance documentation
- [INSERT_WORKFLOW_TYPE] tracking

What type of code analysis would you like to run?