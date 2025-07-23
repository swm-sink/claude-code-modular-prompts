---
name: /secure-scan
description: Automated security scanning with vulnerability detection and compliance reporting
usage: /secure-scan [scan_type] [output_format]
tools: Read, Write, Edit, Bash, Grep
---

# Automated security scanning with vulnerability detection and compliance reporting

**Usage**: `/secure-scan $TARGET`

## Key Arguments

- **$TARGET** (optional): The scan target (e.g., 'all', 'code', 'dependencies', 'secrets').

## Examples

```bash
/secure scan
```
*Run a comprehensive scan on all targets.*

```bash
/secure scan target="secrets"
```
*Scan only for hardcoded secrets in the codebase.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/security/vulnerability-scanning.md
 components/security/dependency-scanning.md
 components/security/secret-detection.md
 components/analysis/severity-assessment.md
 
 You are a security scanner. The user wants to scan the project for vulnerabilities.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured security scanning tools (e.g., Snyk, Trivy, Gitleaks).
 2. **Determine Scan Scope**: Based on the `target` argument, determine which scans to run.
 3. **Execute Scans**:
 * Run the appropriate configured tool(s) for the specified target(s).
 * For `code`, run a static analysis tool (SAST).
 * For `dependencies`, run a dependency vulnerability scanner.
 * For `secrets`, run a secret scanning tool.
 4. **Generate Report**:
 * Aggregate and de-duplicate the findings from all the tools.
 * Create a report that lists all identified vulnerabilities, their severity, and recommended remediations.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

