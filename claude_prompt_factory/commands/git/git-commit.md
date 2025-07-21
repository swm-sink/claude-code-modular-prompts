---
description: Intelligent git commit automation with conventional commits, semantic analysis, and automated staging
argument-hint: "[commit_type] [scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /git commit - Intelligent Commit Automation

Advanced git commit system with conventional commit standards, semantic analysis, and intelligent staging automation.

## Usage
```bash
/git commit feat                             # Feature commit with auto-analysis
/git commit fix                              # Bug fix commit with context
/git commit --auto                           # Fully automated commit generation
/git commit --semantic                       # Semantic commit message analysis
```

  <claude_prompt>
    <prompt>
      You are a git expert. The user wants to create a high-quality commit.

      1.  **Analyze Changes**:
          *   If `auto_stage` is true, stage all changed files (`git add .`).
          *   Analyze the staged changes using `git diff --staged`.
          *   Based on the changes, determine the appropriate commit type (feat, fix, refactor, etc.) and scope.

      2.  **Generate Commit Message**:
          *   Generate a commit message that follows the Conventional Commits specification.
          *   The message should have a clear, concise subject line.
          *   The body should explain the "what" and "why" of the change.

      3.  **Propose Commit Command**:
          *   Present the final `git commit -m "..."` command to the user for them to execute.
    </prompt>
  </claude_prompt>

  <dependencies>
    <!-- This command interacts directly with git -->
  </dependencies>