# /secure scan - Security Vulnerability Scanner

**Purpose**: Perform comprehensive security vulnerability scanning and threat detection across codebases, dependencies, and runtime environments.

## Usage
```bash
/secure scan [target] [--level=quick|standard|deep]
```

## Workflow

The `/secure scan` command follows a systematic process to identify security vulnerabilities.

```xml
<security_scan_workflow>
  <step name="Determine Scan Scope & Level">
    <description>Based on the user's input, determine the target (code, dependencies, config, secrets, or all) and the scan level (quick, standard, or deep).</description>
  </step>
  
  <step name="Execute Security Checks">
    <description>Perform a series of security checks relevant to the target and scan level. This includes static analysis for code, vulnerability scanning for dependencies, and review of configuration and exposed secrets.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob</tool>
      <description>Scan relevant files for security patterns and vulnerabilities.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed security report in the specified format (summary, detailed, JSON, or SARIF), outlining all vulnerabilities found, their severity, and recommended remediations.</description>
    <output>A comprehensive security scan report.</output>
  </step>
</security_scan_workflow>
```

## Security Checks
### Code Analysis
- OWASP Top 10 vulnerability patterns
- SQL injection and XSS detection
- Authentication and authorization flaws
- Insecure cryptographic implementations

### Dependency Scanning
- Known CVE vulnerability matching
- License compliance verification
- Outdated package identification
- Supply chain risk assessment

### Configuration Review
- Security misconfigurations
- Exposed sensitive endpoints
- Insufficient access controls
- Weak encryption settings

## Output Formats
- **summary** - Executive vulnerability report
- **detailed** - Technical findings with remediation
- **json** - Machine-readable results
- **sarif** - Static analysis results format

## Examples
```bash
/secure scan quick code          # Fast code scan
/secure scan standard deps       # Dependency audit
/secure scan deep all --format json    # Complete scan
/secure scan critical --compliance pci # Compliance scan
```

## Integration
- CI/CD pipeline compatible
- Security gate enforcement
- Automated remediation suggestions
- Threat intelligence integration