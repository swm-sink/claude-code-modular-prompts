---
name: /dev-build
description: Advanced development build system with intelligent optimization, parallel processing, and automated quality checks
usage: /dev-build [build_type] [optimization_level]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced development build system with intelligent optimization, parallel processing, and automated quality checks

**Usage**: `/dev-build $TARGET`

## Key Arguments

- **$TARGET** (optional): The build target to run (e.g., 'all', 'frontend', 'backend', 'tests').

## Examples

```bash
/dev build
```
*Run a full project build.*

```bash
/dev build target="frontend"
```
*Build only the frontend assets.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/actions/parallel-execution.md
 components/performance/auto-scaling.md
 components/quality/quality-metrics.md
 
 You are a build automation tool. The user wants to run a development build.

 1. **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to find the build commands associated with the specified `target`.
 2. **Propose Build Script**: Construct a build script using the configured commands.
 3. **Execute Script**: Present the script to the user for confirmation. Upon approval, execute the script.
 4. **Monitor and Report**: Monitor the build progress and provide a clear report on the outcome, including any errors with context.

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

