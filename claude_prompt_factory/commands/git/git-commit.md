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

<command_file>
  <metadata>
    <n>/git commit</n>
    <purpose>Intelligent git commit automation with conventional commits, semantic analysis, and automated staging</purpose>
    <usage>
      <![CDATA[
      /git commit [commit_type] --scope [scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="commit_type" type="string" required="true" default="feat">
      <description>The type of commit (e.g., feat, fix, chore, refactor)</description>
    </argument>
    <argument name="scope" type="string" required="false">
      <description>The scope of the commit (e.g., api, db, ui)</description>
    </argument>
    <argument name="auto_stage" type="boolean" required="false" default="true">
      <description>Whether to automatically stage all changed files</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Create a feature commit with a scope</description>
      <usage>/git commit feat --scope "api"</usage>
    </example>
    <example>
      <description>Create a fix commit without auto-staging</description>
      <usage>/git commit fix --auto-stage false</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are a git expert. The user wants to create a high-quality commit.

**Commit Process:**
1. **Analyze Changes**: If `auto_stage` is true, stage all changed files (`git add .`). Analyze the staged changes using `git diff --staged`. Based on the changes, determine the appropriate commit type (feat, fix, refactor, etc.) and scope.
2. **Generate Commit Message**: Generate a commit message that follows the Conventional Commits specification. The message should have a clear, concise subject line. The body should explain the "what" and "why" of the change.
3. **Propose Commit Command**: Present the final `git commit -m "..."` command to the user for them to execute.

<include component="components/git/git-commit.md" />
<include component="components/workflow/command-execution.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/git/git-commit.md</component>
      <component>components/workflow/command-execution.md</component>
    </includes_components>
    <uses_config_values>
      <value>git.conventional_commits.enabled</value>
      <value>git.auto_stage.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file>