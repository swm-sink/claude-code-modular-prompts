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

<command_file>
  <metadata>
    <n>/git merge</n>
    <purpose>Intelligent git merge with automated conflict resolution, safety checks, and rollback strategies</purpose>
    <usage>
      <![CDATA[
      /git merge [branch_name] --strategy [merge_strategy]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="branch_name" type="string" required="true">
      <description>The branch to merge into the current branch.</description>
    </argument>
    <argument name="merge_strategy" type="string" required="false" default="default">
      <description>The merge strategy to use (e.g., default, rebase, squash)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Merge the 'develop' branch into the current branch.</description>
      <usage>/git merge "develop"</usage>
    </example>
    <example>
      <description>Merge a feature branch using a rebase strategy.</description>
      <usage>/git merge "feature/new-login" --strategy "rebase"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/git/git-merge.md</include>
      <include>components/workflow/rollback-capabilities.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/quality/conflict-resolution.md</include>
      
You are a git expert. The user wants to safely merge a branch.

**Merge Process:**
1. **Pre-Merge Validation**: Check for a clean working directory (`git status`). Fetch the latest remote changes (`git fetch origin`). Preview potential merge conflicts.
2. **Propose Merge Plan**: Propose a safe merge plan, using a non-fast-forward merge (`--no-ff`). If conflicts are anticipated, provide a strategy for resolving them.
3. **Execute Merge**: Present the merge command to the user. If conflicts occur, guide the user through the resolution process.
4. **Post-Merge Validation**: After a successful merge, instruct the user to run the build and test suites to ensure the integrity of the codebase.

    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/git/git-merge.md</component>
      <component>components/workflow/command-execution.md</component>
    </includes_components>
    <uses_config_values>
      <value>git.default_merge_strategy</value>
      <value>git.auto_resolve_conflicts</value>
    </uses_config_values>
  </dependencies>
</command_file>