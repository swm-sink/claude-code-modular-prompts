---
name: /git-commit
description: Intelligent git commit automation with conventional commits, semantic analysis, and automated staging
usage: /git-commit [commit_type] [scope]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent git commit automation with conventional commits, semantic analysis, and automated staging

**Usage**: `/git-commit $COMMIT_TYPE $SCOPE $AUTO_STAGE`

## Key Arguments

- **$COMMIT_TYPE** (required): The type of commit (e.g., feat, fix, chore, refactor)
- **$SCOPE** (optional): The scope of the commit (e.g., api, db, ui)
- **$AUTO_STAGE** (optional): Whether to automatically stage all changed files

## Examples

```bash
/git commit feat --scope "api"
```
*Create a feature commit with a scope*

```bash
/git commit fix --auto-stage false
```
*Create a fix commit without auto-staging*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/git/git-commit.md
 components/analysis/semantic-analysis.md
 components/interaction/request-user-confirmation.md
 components/workflow/staging-automation.md
 
You are a git expert. The user wants to create a high-quality commit.

**Commit Process:**
1. **Analyze Changes**: If `auto_stage` is true, stage all changed files (`git add .`). Analyze the staged changes using `git diff --staged`. Based on the changes, determine the appropriate commit type (feat, fix, refactor, etc.) and scope.
2. **Generate Commit Message**: Generate a commit message that follows the Conventional Commits specification. The message should have a clear, concise subject line. The body should explain the "what" and "why" of the change.
3. **Propose Commit Command**: Present the final `git commit -m "..."` command to the user for them to execute.

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

