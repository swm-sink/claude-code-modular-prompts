---
name: /security
description: Advanced security analysis with threat detection, vulnerability assessment, and automated compliance checking
usage: /security [security_scope] [analysis_depth]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced security analysis with threat detection, vulnerability assessment, and automated compliance checking

**Usage**: `/security $TARGET_PATH`

## Key Arguments

- **$TARGET_PATH** (optional): The file or directory to analyze. Defaults to the current directory.

## Examples

```bash
/analyze security
```
*Run a security analysis on the entire project.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

 You are a principal security engineer. Your task is to perform a comprehensive security analysis.

 Once the code is identified, perform the following:
 1. **Scan for Vulnerabilities**: Scan the codebase for a wide range of security vulnerabilities, including the OWASP Top 10, hard-coded secrets, and insecure dependencies.
 2. **Analyze Security Patterns**: Analyze authentication, authorization, input validation, and data encryption patterns for weaknesses.
 3. **Generate Report**: Generate a prioritized report of vulnerabilities by severity.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...
**Complete**: Apply command execution wrapper completion

### Error Handling
**Standardized Error Handling**: Implement consistent error handling, validation, and recovery patterns across all commands. Provide standardized error detection, classification, user feedback, and recovery options. Ensure graceful d...


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

