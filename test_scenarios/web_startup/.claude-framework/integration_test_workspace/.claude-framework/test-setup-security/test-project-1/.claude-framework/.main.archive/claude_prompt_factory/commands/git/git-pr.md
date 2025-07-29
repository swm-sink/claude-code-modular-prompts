---
description: Intelligent pull request automation with automated review, validation, and CI/CD integration
argument-hint: "[pr_action] [target_branch]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /git pr - Intelligent Pull Request Automation

Advanced PR system with automated review, comprehensive validation, intelligent CI/CD integration, and merge automation.

## Usage
```bash
/git pr create                               # Create PR with auto-generated description
/git pr review                               # Automated code review and validation
/git pr merge                                # Intelligent merge with safety checks
/git pr --auto                               # Fully automated PR workflow
```

<command_file>
  <metadata>
    <name>/git pr</name>
    <purpose>Intelligently creates pull requests with auto-generated descriptions, linked issues, and reviewers.</purpose>
    <usage>
      <![CDATA[
      /git pr "[title]" <draft=false>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="title" type="string" required="true">
      <description>The title of the pull request.</description>
    </argument>
    <argument name="draft" type="boolean" required="false" default="false">
      <description>If true, creates the pull request as a draft.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Create a new pull request for a feature branch.</description>
      <usage>/git pr "feat: Add user profile management"</usage>
    </example>
    <example>
      <description>Create a draft pull request for a work-in-progress.</description>
      <usage>/git pr "WIP: Refactor authentication service" draft=true</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a git expert. The user wants to create a high-quality pull request.

      1.  **Analyze Branch**:
          *   Analyze the commits on the current branch compared to the main branch (`git log main..HEAD`).
          *   Summarize the changes based on the commit messages.
      2.  **Generate PR Description**:
          *   Create a comprehensive PR description that includes:
              *   A summary of the changes.
              *   The motivation behind the changes.
              *   Steps for testing and verification.
          *   Automatically find and link any related issues (e.g., closes #123) mentioned in commit messages.
      3.  **Suggest Reviewers**:
          *   Suggest a list of reviewers by analyzing `git blame` on the changed files to see who has the most context.
      4.  **Propose PR Command**:
          *   Construct the full command to create the pull request using the platform's CLI (e.g., `gh pr create`).
          *   Include the title, the generated body, suggested reviewers, and the draft flag.
          *   Present the command to the user for execution.
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>git.hosting_platform</value>
      <value>git.main_branch</value>
    </uses_config_values>
  </dependencies>
</command_file>