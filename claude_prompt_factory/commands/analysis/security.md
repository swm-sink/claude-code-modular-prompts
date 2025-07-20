# /analyze security - Security Analysis Command

**Purpose**: Perform a comprehensive security analysis of the codebase, based on OWASP standards, and provide a prioritized list of vulnerabilities with recommended fixes.

## Usage
```bash
/analyze security [target] [--level=basic|deep] [--fix]
```

## Workflow

The `/analyze security` command follows a systematic process to identify and report security vulnerabilities.

```xml
<security_analysis_workflow>
  <step name="Scan for Vulnerabilities">
    <description>Perform a comprehensive scan of the codebase to identify a wide range of security vulnerabilities, including the OWASP Top 10, hard-coded secrets, and insecure dependencies.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob</tool>
      <description>Scan the codebase for common vulnerability patterns.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Security Patterns">
    <description>Analyze the codebase's security patterns, including authentication, authorization, input validation, and data encryption, to identify any weaknesses or misconfigurations.</description>
  </step>
  
  <step name="Generate Prioritized Report">
    <description>Generate a detailed security report that prioritizes vulnerabilities by severity and provides clear, actionable recommendations for how to fix them. If the `--fix` flag is used, the command will also attempt to automatically apply the recommended fixes.</description>
    <output>A comprehensive security report with a prioritized list of vulnerabilities and recommended fixes.</output>
  </step>
</security_analysis_workflow>
```

## Security Checks
- SQL injection vulnerabilities
- Cross-site scripting (XSS)
- Insecure authentication
- Sensitive data exposure
- Security misconfigurations
- Vulnerable dependencies
- Insufficient logging

## Output Format
```
SECURITY ANALYSIS REPORT
━━━━━━━━━━━━━━━━━━━━━
Critical Issues: X
High Priority: Y
Medium Priority: Z

[CRITICAL] Issue description
  Location: file:line
  Impact: Explanation
  Fix: Specific recommendation
```

## Options
- `--level`: Analysis depth (basic/deep/paranoid)
- `--fix`: Attempt automatic fixes
- `--report`: Generate detailed report
- `--owasp`: Include OWASP mapping

## Related Commands
- `/fix security` - Fix security issues
- `/security harden` - Security hardening
- `/audit trail` - Add audit logging