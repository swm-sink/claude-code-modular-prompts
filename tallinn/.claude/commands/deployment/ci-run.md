---
name: /ci-run
description: Advanced CI execution with intelligent pipeline optimization, parallel processing, and automated quality gates
usage: /ci-run [execution_mode] [optimization_level]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced CI execution with intelligent pipeline optimization, parallel processing, and automated quality gates

**Usage**: `/ci-run $PIPELINE_NAME`

## Key Arguments

- **$PIPELINE_NAME** (required): The name of the CI pipeline to execute as defined in the project's CI configurat...

## Examples

```bash
/ci run "main-build"
```
*Run the 'main-build' pipeline.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/deployment/pipeline-optimization.md
 components/actions/parallel-execution.md
 components/quality/quality-gates.md
 components/monitoring/pipeline-monitoring.md
 
 You are a CI/CD orchestrator. The user wants to run a specific CI pipeline.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` and the CI configuration file (e.g., `.github/workflows/main.yml`) to understand the available pipelines and the CI platform.
 2. **Validate Pipeline**: Verify that the requested `pipeline_name` is a valid pipeline.
 3. **Generate Execution Command**: Construct the platform-specific command to trigger the pipeline (e.g., using `gh workflow run`, `glab ci run`).
 4. **Monitor Progress**: Propose commands to monitor the pipeline's progress and fetch the results.
 5. **Report Results**: After completion, generate a report on the outcome.

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

