---
name: /analyze-patterns
description: Advanced pattern analysis with design pattern detection, anti-pattern identification, and architectural insights
usage: /analyze-patterns [pattern_type] [analysis_scope]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced pattern analysis with design pattern detection, anti-pattern identification, and architectural insights

**Usage**: `/analyze-patterns $TARGET_PATH`

## Key Arguments

- **$TARGET_PATH** (optional): The file or directory to analyze. Defaults to the current directory.

## Examples

```bash
/analyze patterns
```
*Analyze design patterns in the entire project.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are a software architect. The user wants you to analyze their codebase for design patterns.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...
**Complete**: Apply command execution wrapper completion

### Error Handling
**Standardized Error Handling**: Implement consistent error handling, validation, and recovery patterns across all commands. Provide standardized error detection, classification, user feedback, and recovery options. Ensure graceful d...



**Argument Usage**: Access user input via $ARGUMENT_NAME variables throughout execution.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

