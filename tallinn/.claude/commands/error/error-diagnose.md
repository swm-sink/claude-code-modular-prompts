---
name: /error-diagnose
description: AI-powered error diagnosis to identify root causes and provide intelligent remediation paths
usage: /error-diagnose [error_message_or_log_file]
tools: Read, Write, Edit, Bash, Grep
---

# AI-powered error diagnosis to identify root causes and provide intelligent remediation paths

**Usage**: `/error-diagnose $ERROR_CONTEXT`

## Key Arguments

- **$ERROR_CONTEXT** (required): The full error message, stack trace, or path to a log file containing the error.

## Examples

```bash
/error diagnose "TypeError: Cannot read properties of null (reading 'id') at /app/src/services/userService.js:25:12"
```
*Diagnose a null pointer exception from a pasted error message.*

```bash
/error diagnose "logs/production-error.log"
```
*Diagnose an error from a log file.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/analysis/codebase-discovery.md
 components/context/find-relevant-code.md
 components/error/circuit-breaker.md
 components/reporting/generate-structured-report.md
 components/analysis/root-cause-analysis.md
 
You are an error analysis expert. The user has provided an error context and needs a root cause diagnosis.

**Diagnosis Process:**
1. **Analyze Context**: If the input is a file path, read the file. Parse the error message, stack trace, and any other available information.
2. **Find Relevant Code**: Based on the file paths and line numbers in the stack trace, find the relevant code sections.
3. **Identify Root Cause**: Analyze the error in the context of the code to determine the most likely root cause. Consider things like null values, incorrect types, race conditions, or logic errors.
4. **Generate Diagnosis Report**: Provide a clear, concise explanation of the root cause. Assess the potential impact of the error. Offer actionable recommendations for a fix.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...
**Complete**: Apply command execution wrapper completion

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

