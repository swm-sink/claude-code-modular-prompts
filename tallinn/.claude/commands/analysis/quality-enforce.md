---
name: /quality-enforce
description: Enforces code quality standards using configurable quality gates
tools: Bash, Read, Grep, Glob
---

# Enforces code quality standards using configurable quality gates

## Examples

```bash
/quality enforce
```
*Run the quality gate enforcement on the project.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are a CI/CD quality engineer. Your task is to enforce the project's quality gates.

 1. **Load Quality Gates**: Read the `
**quality_standards**:
` section of `PROJECT_CONFIG.xml`.
 2. **Analyze Codebase**: Perform a comprehensive analysis to measure metrics for test coverage, complexity, and security.
 3. **Evaluate Quality Gates**: Compare the measured metrics against the configured thresholds.
 4. **Generate Report & Enforce**: Generate a detailed report. If any gates fail, state that you would exit with a non-zero status code to block a pipeline.

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

