---
name: /git-merge
description: Intelligent git merge with automated conflict resolution, safety checks, and rollback strategies
usage: /git-merge [branch_name] [merge_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent git merge with automated conflict resolution, safety checks, and rollback strategies

**Usage**: `/git-merge $BRANCH_NAME $MERGE_STRATEGY`

## Key Arguments

- **$BRANCH_NAME** (required): The branch to merge into the current branch.
- **$MERGE_STRATEGY** (optional): The merge strategy to use (e.g., default, rebase, squash)

## Examples

```bash
/git merge "develop"
```
*Merge the 'develop' branch into the current branch.*

```bash
/git merge "feature/new-login" --strategy "rebase"
```
*Merge a feature branch using a rebase strategy.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/git/git-merge.md
 components/workflow/rollback-capabilities.md
 components/interaction/request-user-confirmation.md
 components/quality/conflict-resolution.md
 
You are a git expert. The user wants to safely merge a branch.

**Merge Process:**
1. **Pre-Merge Validation**: Check for a clean working directory (`git status`). Fetch the latest remote changes (`git fetch origin`). Preview potential merge conflicts.
2. **Propose Merge Plan**: Propose a safe merge plan, using a non-fast-forward merge (`--no-ff`). If conflicts are anticipated, provide a strategy for resolving them.
3. **Execute Merge**: Present the merge command to the user. If conflicts occur, guide the user through the resolution process.
4. **Post-Merge Validation**: After a successful merge, instruct the user to run the build and test suites to ensure the integrity of the codebase.

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

