---
name: /secure-audit
description: Comprehensive code audit with multi-layer security analysis and automated scanning (v1.0)
version: "1.0"
usage: '/secure-audit [--scope full|code|infrastructure|compliance] [--report-format detailed|executive|compliance] [--severity critical|high|medium|low] [--fix-mode suggest|apply]'
category: security
allowed-tools:
- Bash
- Read
- Write
- Grep
- Glob
- Edit
dependencies:
- /secure-scan
- /validate-component
- /monitor-alerts
validation:
  pre-execution: Verify project structure and security tool availability
  during-execution: Real-time vulnerability detection and classification
  post-execution: Generate comprehensive security report with remediation plan
progressive-disclosure:
  layer-integration: Layer 1 auto-scans common vulnerabilities, Layer 2 offers focused audits, Layer 3 enables custom security rule creation
  escalation-path: /secure-scan → /secure-audit → custom security framework
  de-escalation: Automated fixes for common issues reduce need for manual audit
safety-measures:
  - Never expose sensitive data in reports
  - Sanitize all file paths and credentials
  - Validate all external tool outputs
  - Maintain audit trail of all actions
error-recovery:
  partial-scan-failure: Continue with available tools and note limitations
  permission-errors: Gracefully handle restricted access with clear reporting
  tool-unavailability: Fallback to manual inspection methods
---

# Code Audit for [INSERT_PROJECT_NAME]

I'll perform a comprehensive code audit of **[INSERT_PROJECT_NAME]** aligned with your **[INSERT_SECURITY_LEVEL]** requirements and **[INSERT_USER_BASE]** compliance needs.

## Audit Configuration

- **Project**: [INSERT_PROJECT_NAME]
- **Security Level**: [INSERT_SECURITY_LEVEL]
- **Tech Stack**: [INSERT_TECH_STACK]
- **Compliance**: Based on [INSERT_USER_BASE]

## Audit Scopes

### Full Code Audit
Complete code assessment:
```bash
/secure-audit --scope full
```
- Code quality review
- Infrastructure audit
- Access control review
- Compliance validation

### Code Quality Audit
Source code focus:
```bash
/secure-audit --scope code
```
- [INSERT_PRIMARY_LANGUAGE] code issues
- Dependency analysis
- Secret detection
- Code quality metrics

### Infrastructure Audit
[INSERT_DEPLOYMENT_TARGET] configuration:
```bash
/secure-audit --scope infrastructure
```
- Configuration review
- Network configuration
- Access controls
- Encryption status

### Compliance Audit
[INSERT_USER_BASE] requirements:
```bash
/secure-audit --scope compliance
```
- Regulatory compliance
- Data protection
- Privacy controls
- Audit trail review

## [INSERT_SECURITY_LEVEL] Checks

Your analysis level includes:
- OWASP Top 10 patterns
- Authentication mechanisms
- Authorization controls
- Data encryption standards
- API security ([INSERT_API_STYLE])
- Session management
- Input validation

## Automated Analysis

### Static Analysis
For [INSERT_TECH_STACK]:
- Code pattern analysis
- Configuration analysis
- Dependency checking
- License compliance

### Dynamic Analysis
Runtime behavior testing:
- API testing
- Input validation testing
- Authentication flow testing
- Session management tests

## Manual Review Areas

### Architecture Review
- System design review
- Data flow analysis
- Component boundaries
- Risk modeling

### Access Control
For [INSERT_TEAM_SIZE] teams:
- User permissions
- Role definitions
- Service accounts
- API keys management

## Reporting Options

### Executive Summary
High-level overview:
```bash
/secure-audit --report-format executive
```
- Risk summary
- Critical findings
- Recommendations
- Compliance status

### Detailed Report
Technical deep-dive:
```bash
/secure-audit --report-format detailed
```
- Full vulnerability list
- Code examples
- Remediation steps
- Timeline estimates

### Compliance Report
Regulatory focus:
```bash
/secure-audit --report-format compliance
```
- Standards mapping
- Gap analysis
- Evidence collection
- Certification readiness

## Integration Points

### With [INSERT_CI_CD_PLATFORM]
- Automated audit triggers
- Pipeline integration
- Fail-fast on critical issues
- Trend tracking

### With [INSERT_WORKFLOW_TYPE]
- Approval workflows
- Issue tracking
- Remediation planning
- Progress monitoring

## Risk Scoring

Based on:
- Severity levels
- Exploitability
- Business impact
- Data sensitivity

## Remediation Guidance

For each finding:
- Risk assessment
- Fix recommendations
- Code examples
- Testing approach
- Verification steps

Which type of code audit would you like to perform?