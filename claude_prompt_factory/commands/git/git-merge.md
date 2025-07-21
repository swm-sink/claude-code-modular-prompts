---
description: Intelligent git merge with automated conflict resolution, safety checks, and rollback strategies
argument-hint: "[branch_name] [merge_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /git merge - Intelligent Merge Automation

Advanced git merge system with automated conflict resolution, comprehensive safety checks, and intelligent rollback strategies.

## Usage
```bash
/git merge feature-branch                    # Smart merge with conflict detection
/git merge --auto-resolve                    # Automated conflict resolution
/git merge --safe                            # Safety-first merge with validation
/git merge --strategy rebase                 # Rebase merge strategy
```

## Arguments

<argument_list>
  <argument name="branch" type="string" required="true">
    <description>The branch to merge into the current branch.</description>
  </argument>
</argument_list>

## Examples

<example_list>
  <example>
    <description>Merge the 'develop' branch into the current branch.</description>
    <usage>/git merge "develop"</usage>
  </example>
</example_list>

## Claude Prompt

<claude_prompt>
  <prompt>
    You are a git expert. The user wants to safely merge a branch.

    1.  **Pre-Merge Validation**:
        *   Check for a clean working directory (`git status`).
        *   Fetch the latest remote changes (`git fetch origin`).
        *   Preview potential merge conflicts.
    2.  **Propose Merge Plan**:
        *   Propose a safe merge plan, using a non-fast-forward merge (`--no-ff`).
        *   If conflicts are anticipated, provide a strategy for resolving them.
    3.  **Execute Merge**:
        *   Present the merge command to the user.
        *   If conflicts occur, guide the user through the resolution process.
    4.  **Post-Merge Validation**:
        *   After a successful merge, instruct the user to run the build and test suites to ensure the integrity of the codebase.
  </prompt>
</claude_prompt>

## Dependencies

<dependencies>
  <chain>
    <command>/dev build</command>
    <command>/dev test</command>
  </chain>
</dependencies>