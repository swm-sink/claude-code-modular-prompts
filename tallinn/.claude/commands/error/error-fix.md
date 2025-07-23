---
name: /error-fix
description: Automated error remediation with safe fixes, validation, and rollback capabilities
usage: /error-fix [error_type] [fix_approach]
tools: Read, Write, Edit, Bash, Grep
---

# Automated error remediation with safe fixes, validation, and rollback capabilities

**Usage**: `/error-fix $ERROR_CONTEXT $DRY_RUN`

## Key Arguments

- **$ERROR_CONTEXT** (required): The full error message, stack trace, or path to a log file containing the error ...
- **$DRY_RUN** (optional): If true, shows the proposed code fix without applying it.

## Examples

```bash
/error fix "TypeError: Cannot read properties of null (reading 'id') at /app/src/services/userService.js:25:12"
```
*Automatically diagnose and propose a fix for a given error.*

```bash
/error fix "logs/production-error.log" dry_run=true
```
*Show the proposed fix for an error in a log file without applying it.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/context/find-relevant-code.md
 components/interaction/request-user-confirmation.md
 components/actions/apply-code-changes.md
 components/quality/anti-pattern-detection.md
 components/workflow/rollback-capabilities.md
 
 You are an automated error correction system. The user wants you to diagnose and fix an error.

 1. **Diagnose Error**:
 * First, perform a full diagnosis of the error using the `/error diagnose` command logic. This involves analyzing the context, finding relevant code, and identifying the root cause.

 2. **Generate Fix**:
 * Based on the diagnosis, generate the specific code changes required to fix the error.

 3. **Propose Fix**:
 * Present the proposed code changes to the user.
 * If `dry_run` is true, stop here.

 4. **Apply and Verify**:
 * If `dry_run` is false, ask for confirmation to apply the fix.
 * On confirmation, apply the changes.
 * Instruct the user to run the relevant tests to verify that the fix works and hasn't introduced regressions.

## Essential Component Logic


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

