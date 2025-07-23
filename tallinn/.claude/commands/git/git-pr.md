---
name: /git-pr
description: Intelligent pull request automation with automated review, validation, and CI/CD integration
usage: /git-pr [pr_action] [target_branch]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent pull request automation with automated review, validation, and CI/CD integration

**Usage**: `/git-pr $TITLE $DRAFT`

## Key Arguments

- **$TITLE** (required): The title of the pull request.
- **$DRAFT** (optional): If true, creates the pull request as a draft.

## Examples

```bash
/git pr "feat: Add user profile management"
```
*Create a new pull request for a feature branch.*

```bash
/git pr "WIP: Refactor authentication service" draft=true
```
*Create a draft pull request for a work-in-progress.*

## Core Logic

You are a git expert. The user wants to create a high-quality pull request.

 1. **Analyze Branch**:
 * Analyze the commits on the current branch compared to the main branch (`git log main..HEAD`).
 * Summarize the changes based on the commit messages.
 2. **Generate PR Description**:
 * Create a comprehensive PR description that includes:
 * A summary of the changes.
 * The motivation behind the changes.
 * Steps for testing and verification.
 * Automatically find and link any related issues (e.g., closes #123) mentioned in commit messages.
 3. **Suggest Reviewers**:
 * Suggest a list of reviewers by analyzing `git blame` on the changed files to see who has the most context.
 4. **Propose PR Command**:
 * Construct the full command to create the pull request using the platform's CLI (e.g., `gh pr create`).
 * Include the title, the generated body, suggested reviewers, and the draft flag.
 * Present the command to the user for execution.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

