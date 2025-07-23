---
name: /api-version
description: API versioning strategy with backward compatibility, migration paths, and deprecation management
usage: /api-version [version_strategy] [migration_approach]
tools: Read, Write, Edit, Bash, Grep
---

# API versioning strategy with backward compatibility, migration paths, and deprecation management

**Usage**: `/api-version $INCREMENT`

## Key Arguments

- **$INCREMENT** (optional): The semantic version to increment (major, minor, or patch).

## Examples

```bash
/api version
```
*Perform a patch version increment.*

```bash
/api version increment="major"
```
*Perform a major version increment for a breaking change.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/planning/create-step-by-step-plan.md
 components/git/git-commit.md
 components/reporting/generate-structured-report.md
 components/analysis/dependency-mapping.md

You are an API release manager. The user wants to manage their API version.

 1. **Analyze Changes**: Analyze recent API changes to identify breaking changes and determine the appropriate version increment (major, minor, patch).
 2. **Implement Versioning**: Propose code changes to implement the new version, such as updating version headers or routing.
 3. **Plan Migration & Deprecation**: Create a migration guide for users, documenting breaking changes and setting a deprecation timeline for the old version.

 Your output should be a plan and the proposed code changes.

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

