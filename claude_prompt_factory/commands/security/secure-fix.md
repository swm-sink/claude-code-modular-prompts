# /secure fix - Automated Security Remediation Command

**Purpose**: Automatically fix security vulnerabilities in code and dependencies, with verification and reporting.

## Usage
```bash
/secure fix [target] [--verify] [--backup]
```

## Workflow

The `/secure fix` command follows a systematic process to identify, apply, and verify security fixes.

```xml
<security_fix_workflow>
  <step name="Scan & Identify Vulnerabilities">
    <description>Perform a quick scan to identify security vulnerabilities in the target code and its dependencies.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob</tool>
      <description>Scan relevant files for security issues.</description>
    </tool_usage>
  </step>
  
  <step name="Apply Fixes">
    <description>Automatically apply fixes to identified vulnerabilities. This includes updating vulnerable dependencies and correcting insecure code patterns.</description>
    <tool_usage>
      <tool>Edit</tool>
      <description>Apply code changes for security fixes.</description>
      <tool>Bash</tool>
      <description>Update dependency versions.</description>
    </tool_usage>
  </step>
  
  <step name="Verify Fixes">
    <description>Run tests and perform additional security checks to ensure that the fixes have been successfully applied and have not introduced any regressions.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run existing test suite and security verification scripts.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed report of all applied fixes, their verification status, and any remaining issues.</description>
    <output>A comprehensive security fix report.</output>
  </step>
</security_fix_workflow>
```

## Fix Types
- Vulnerable dependency updates
- SQL injection prevention
- XSS sanitization patches
- Authentication hardening
- Input validation fixes
- Encryption implementation
- Logging security improvements

## Output Format
```
SECURITY FIX REPORT
━━━━━━━━━━━━━━━━━━━
Fixes Applied: X
Dependencies Updated: Y
Tests Passed: Z/Total

[FIXED] Vulnerability type
  File: path/to/file.ext:line
  Fix: Description of applied patch
  Status: ✓ Verified / ⚠ Needs Review
```

## Options
- `--verify`: Run comprehensive fix verification
- `--backup`: Create restore point before fixes
- `--report`: Generate detailed fix documentation
- `--safe-mode`: Apply only verified-safe fixes

## Related Commands
- `/analyze security` - Identify security issues
- `/security harden` - Apply security hardening