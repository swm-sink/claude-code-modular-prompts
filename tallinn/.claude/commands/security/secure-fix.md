---
name: /secure-fix
description: Automated security issue remediation with validation and rollback capabilities
usage: /secure-fix [issue_type] [fix_level]
tools: Read, Write, Edit, Bash, Grep
---

# Automated security issue remediation with validation and rollback capabilities

**Usage**: `/secure-fix $VULNERABILITY`

## Key Arguments

- **$VULNERABILITY** (required): The specific vulnerability to fix, identified by an ID from a scan or a clear de...

## Examples

```bash
/secure fix "CVE-2023-12345"
```
*Fix a specific vulnerability identified by a security scanner (e.g., CVE-2023-12345).*

```bash
/secure fix "Potential SQL injection in user search API endpoint"
```
*Fix a described vulnerability like a potential SQL injection.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/context/find-relevant-code.md
 components/interaction/request-user-confirmation.md
 components/actions/apply-code-changes.md
 components/security/vulnerability-remediation.md
 components/testing/test-generation.md
 
 You are a security remediation specialist. The user wants you to fix a specific security vulnerability.

 1. **Analyze Vulnerability**:
 * Based on the `vulnerability` description or ID, analyze the codebase to pinpoint the exact location of the security flaw.
 2. **Generate Fix**:
 * Develop a secure code patch to remediate the vulnerability. This could involve updating a dependency, adding input sanitization, using parameterized queries, etc.
 3. **Ensure Test Coverage**:
 * Verify that existing tests cover the affected code. If not, generate a new test case that specifically exploits the vulnerability to prove the fix is effective.
 4. **Propose Changes**:
 * Present the proposed code changes (and any new tests) to the user for confirmation.
 5. **Apply and Verify**:
 * On confirmation, apply the changes.
 * Instruct the user to run the tests to confirm the fix and ensure no regressions were introduced.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

