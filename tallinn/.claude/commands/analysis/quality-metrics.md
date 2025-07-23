---
name: /quality-metrics
description: Quality metrics collection with comprehensive scoring, trend analysis, and benchmark comparison
usage: /quality-metrics [metrics_scope] [time_period]
tools: Read, Write, Edit, Bash, Grep
---

# Quality metrics collection with comprehensive scoring, trend analysis, and benchmark comparison

**Usage**: `/quality-metrics $TARGET_PATH`

## Key Arguments

- **$TARGET_PATH** (optional): The file or directory to analyze. Defaults to the current directory.

## Examples

```bash
/quality metrics
```
*Calculate quality metrics for the entire project.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

 You are a software quality analyst. The user wants you to calculate code quality metrics.

 Once the code is identified, perform the following analysis:
 1. **Calculate Metrics**: Analyze the codebase to calculate metrics for complexity, maintainability, test coverage, and technical debt.
 2. **Perform Trend Analysis**: Compare current metrics against historical data to identify trends.
 3. **Compare Against Benchmarks**: Compare metrics against industry standards to identify areas for improvement.

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

