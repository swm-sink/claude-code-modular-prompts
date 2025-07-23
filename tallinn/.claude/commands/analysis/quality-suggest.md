---
name: /quality-suggest
description: Advanced quality suggestions with intelligent recommendations, automated improvements, and best practice guidance
usage: /quality-suggest [suggestion_scope] [improvement_level]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced quality suggestions with intelligent recommendations, automated improvements, and best practice guidance

**Usage**: `/quality-suggest $TARGET_PATH`

## Key Arguments

- **$TARGET_PATH** (optional): The file or directory to analyze. Defaults to the current directory.

## Examples

```bash
/quality suggest
```
*Get quality improvement suggestions for the entire project.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

 You are a senior software architect. Your task is to provide a prioritized, actionable list of quality improvements.

 Once the code is identified, perform the following:
 1. **Analyze Code Quality**: Identify areas for improvement in performance, maintainability, security, and documentation.
 2. **Prioritize Opportunities**: Prioritize the opportunities based on their potential impact and estimated effort.
 3. **Generate Suggestions**: Generate a clear list of suggestions, complete with code examples.

 Your output should be a structured report, but instead of findings, the sections should be prioritized suggestions (e.g., "Priority 1: High Impact, Low Effort").

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

