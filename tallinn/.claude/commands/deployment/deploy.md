---
name: /deploy
description: Advanced deployment orchestration with intelligent strategies, rollback capabilities, and environment management
usage: /deploy [deployment_target] [strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced deployment orchestration with intelligent strategies, rollback capabilities, and environment management

**Usage**: `/deploy $TARGET $DRY_RUN`

## Key Arguments

- **$TARGET** (required): The deployment environment to target (e.g., 'staging', 'production').
- **$DRY_RUN** (optional): If true, outputs the deployment plan without executing it.

## Examples

```bash
/deploy
```
*Deploy the current branch to the staging environment.*

```bash
/deploy target="production" dry_run=true
```
*Perform a dry run of a deployment to the production environment.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/planning/create-step-by-step-plan.md
 components/interaction/request-user-confirmation.md
 components/reporting/generate-structured-report.md
 components/deployment/deployment-strategies.md
 components/deployment/environment-management.md
 
 You are a release engineer executing a deployment pipeline.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the deployment configuration for the specified `target` environment. This includes build, test, deploy, and health check commands.
 2. **Generate Deployment Plan**: Create a step-by-step deployment plan based on the configuration.
 3. **Dry Run Check**: If `dry_run` is true, present the plan and stop.
 4. **Execute Plan**: If `dry_run` is false, present the plan and ask for confirmation before executing each step.
 * **On Failure**: If any step fails, immediately stop and propose running the configured rollback commands.
 5. **Report Outcome**: After successful execution (or failure), generate a final report.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

