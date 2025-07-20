# /secure config - Security Configuration Command

**Purpose**: Configure comprehensive security settings for applications, including authentication, authorization, encryption, and security headers, to prevent vulnerabilities and ensure secure deployment.

## Usage
```bash
/secure config [component] [--strict] [--compliance=GDPR|HIPAA|SOC2|PCI-DSS]
```

## Workflow

The `/secure config` command follows a systematic process to configure security settings.

```xml
<security_config_workflow>
  <step name="Assess Current Security Gaps">
    <description>Analyze the existing codebase and configuration to identify current security gaps and areas for improvement.</description>
  </step>
  
  <step name="Configure Security Components">
    <description>Based on the assessment and user input, configure various security components such as authentication, authorization rules, security headers, encryption, and secrets management.</description>
    <component_options>
      <option name="Authentication">Configure multi-factor authentication, OAuth2/JWT, and session management.</option>
      <option name="Authorization">Implement role-based access control (RBAC) and other authorization rules.</option>
      <option name="Security Headers">Set Content Security Policy (CSP), HSTS, X-Frame-Options, and other relevant security headers.</option>
      <option name="Encryption">Set up AES-256-GCM, TLS 1.3, and certificate management for data at rest and in transit.</option>
      <option name="Secrets Management">Configure secure vaults, environment variables, and key rotation strategies.</option>
    </component_options>
    <tool_usage>
      <tool>Edit</tool>
      <description>Modify configuration files to apply security settings.</description>
    </tool_usage>
  </step>
  
  <step name="Validate & Audit Configuration">
    <description>Validate the applied security controls and generate an audit report to ensure compliance with specified standards (e.g., GDPR, HIPAA, SOC2, PCI-DSS).</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run security validation and audit tools.</description>
    </tool_usage>
  </step>
</security_config_workflow>
```

## Configuration Components
- Authentication: JWT tokens, OAuth2, session management, rate limiting
- Security Headers: Content Security Policy, CORS, clickjacking protection
- Encryption: Data-at-rest, data-in-transit, key management, certificate rotation
- Input Validation: Schema validation, XSS prevention, SQL injection protection
- Secrets: Environment variables, secure vaults, API key rotation
- Audit Logging: Security events, compliance reporting, threat detection