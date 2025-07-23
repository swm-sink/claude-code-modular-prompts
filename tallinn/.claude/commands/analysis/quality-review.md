---
name: /quality-review
description: Comprehensive quality review with automated code review, best practices validation, and improvement recommendations
usage: /quality-review [review_scope] [quality_standard]
tools: Read, Write, Edit, Bash, Grep
---

# Comprehensive quality review with automated code review, best practices validation, and improvement recommendations

**Usage**: `/quality-review $TARGET_PATH`

## Key Arguments

- **$TARGET_PATH** (optional): The file or directory to review. Defaults to the current directory.

## Examples

```bash
/quality review
```
*Review the entire project's code quality.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

 You are a principal software engineer performing a code review.

 Once the code is identified, perform a deep analysis covering:
 - **Coding standards**: Compliance with project conventions.
 - **Design patterns**: Correct usage and opportunities for improvement.
 - **Error handling**: Completeness and correctness.
 - **Test coverage**: Adequacy and quality of tests.
 - **Security**: Adherence to best practices.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...
**Complete**: Apply command execution wrapper completion

### Error Handling

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

