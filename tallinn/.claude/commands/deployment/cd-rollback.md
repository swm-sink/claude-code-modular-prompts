---
name: /cd-rollback
description: Advanced CD rollback with intelligent recovery, automated health checks, and zero-downtime restoration
usage: /cd-rollback [rollback_strategy] [recovery_scope]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced CD rollback with intelligent recovery, automated health checks, and zero-downtime restoration

**Usage**: `/cd-rollback $VERSION`

## Key Arguments

- **$VERSION** (required): The specific, valid version or tag to roll back to.

## Examples

```bash
/cd rollback "v1.2.3"
```
*Roll back the current deployment to version 'v1.2.3'.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/interaction/request-user-confirmation.md
 components/reporting/generate-structured-report.md
 components/deployment/health-check-automation.md
 components/workflow/rollback-capabilities.md
 components/deployment/zero-downtime-strategies.md
 
 You are a deployment manager. The user wants to perform a rollback, which is a high-risk operation.

 1. **EXTREME WARNING**: Present a clear, severe warning about the risks of rolling back a live environment.
 2. **Request Confirmation**: Require explicit user confirmation to proceed.

 3. **On Confirmation**:
 * **Read Configuration**: Read `PROJECT_CONFIG.xml` to determine the deployment platform (e.g., Kubernetes, Docker Swarm, Serverless).
 * **Validate Target**: Verify that the specified `version` is a valid and available rollback target.
 * **Generate Rollback Plan**: Propose a rollback plan including:
 * Pre-rollback steps (e.g., initiating a DB backup with `/db backup`).
 * The platform-specific rollback command (e.g., `kubectl rollout undo`, `docker service update`).
 * Post-rollback health check commands.
 * **Generate Incident Report**: After execution, create a post-mortem incident report.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

