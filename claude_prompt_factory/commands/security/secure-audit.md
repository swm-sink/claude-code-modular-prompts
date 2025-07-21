---
description: Comprehensive security audit with OWASP compliance checking and vulnerability assessment
argument-hint: "[scope] [severity_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /secure audit - Comprehensive Security Audit

Advanced security audit system with OWASP compliance, vulnerability assessment, and automated remediation recommendations.

## Usage
```bash
/secure audit full                    # Complete security audit
/secure audit dependencies           # Focus on dependency vulnerabilities  
/secure audit code --severity high   # Code audit for high-severity issues
```

## Arguments

```bash
/secure audit <standard="owasp">
```

### Standard
- `owasp`: OWASP Top 10 (2021)
- `nist`: NIST SP 800-53
- `iso27001`: ISO 27001

### Scope
- `full`: Comprehensive audit of all code, configuration, and access controls.
- `dependencies`: Focus on third-party dependencies and their vulnerabilities.
- `code`: Specific code audit for a given severity level (e.g., `--severity high`).

## Examples

```bash
/secure audit
```

```bash
/secure audit standard="nist"
```

## Analysis

You are a security auditor. The user wants to perform a compliance audit.

1.  **Define Scope**: Based on the chosen `standard`, define the full scope of the audit. This includes checking access control, code security, and configuration.
2.  **Execute Audit Checks**:
    *   Scan the codebase and configuration files for compliance gaps related to the standard.
    *   For example, for OWASP, this would involve looking for potential injection flaws, broken authentication, sensitive data exposure, etc.
    *   <include component="components/context/find-relevant-code.md" />
3.  **Generate Audit Report**:
    *   Create a comprehensive audit report that includes:
        *   A risk assessment matrix.
        *   A detailed list of all identified compliance gaps with severity levels.
        *   A prioritized remediation roadmap.
    *   <include component="components/reporting/generate-structured-report.md" />

## Dependencies

```bash
/secure audit
```

```bash
/secure audit standard="nist"
```

```bash
/secure audit code --severity high
```
