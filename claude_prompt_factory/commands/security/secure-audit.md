# /secure audit - Security Compliance Audit Command

**Purpose**: Perform a comprehensive security compliance audit across code, configuration, and access controls, and generate an automated report.

## Usage
```bash
/secure audit [scope] [--standard=owasp|iso27001|nist]
```

## Workflow

The `/secure audit` command follows a systematic process to perform a security compliance audit.

```xml
<security_audit_workflow>
  <step name="Define Audit Scope & Standard">
    <description>Based on the user's input, define the audit scope (e.g., code, configuration, access controls) and the compliance standard (e.g., OWASP, ISO 27001, NIST) to audit against.</description>
  </step>
  
  <step name="Execute Audit Checks">
    <description>Perform a series of audit checks across the defined scope, evaluating authentication mechanisms, authorization patterns, input validation, cryptographic practices, configuration settings, and logging compliance.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan relevant files and configurations for compliance issues.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Audit Report">
    <description>Generate a comprehensive audit report that includes a risk assessment, identified compliance gaps, a remediation roadmap, and a verification checklist for post-fix validation.</description>
    <output>A detailed security compliance audit report.</output>
  </step>
</security_audit_workflow>
```

## Core Audit Areas

### 🔐 Access Control Review
- **Authentication mechanisms**: Multi-factor, OAuth2/JWT validation
- **Authorization patterns**: RBAC, ABAC implementation review
- **Session management**: Token lifecycle, expiration policies
- **Privilege escalation**: Least privilege principle compliance

### 🛡️ Code Security Analysis
- **Input validation**: SQL injection, XSS, command injection vectors
- **Cryptographic practices**: AES-256-GCM, key management, secure random
- **Dependency scanning**: Known vulnerabilities, license compliance
- **Secret detection**: Hardcoded credentials, API keys, tokens

### ⚙️ Configuration Security
- **Environment isolation**: Production, staging, development separation
- **Security headers**: HTTPS, CSP, HSTS, X-Frame-Options
- **Error handling**: Information disclosure prevention
- **Logging compliance**: Audit trails, PII protection, retention

### 📊 Compliance Standards
- **OWASP Top 10**: Web application security risks assessment
- **ISO 27001**: Information security management compliance
- **NIST Framework**: Cybersecurity framework alignment
- **GDPR/CCPA**: Data protection regulation compliance