# /git pr - Pull Request Creation Command

**Purpose**: Intelligently create pull requests with auto-generated descriptions, linked issues, and appropriate reviewers.

## Usage
```bash
/git pr "[title]" [--draft]
```

## Workflow

The `/git pr` command follows a systematic process to create high-quality pull requests.

```xml
<git_pr_workflow>
  <step name="Analyze Branch & Commits">
    <description>Analyze the current branch against the main branch to understand the changes. Extract commit messages and file changes to generate a comprehensive summary.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Use `git log` and `git diff` to analyze the branch.</description>
    </tool_usage>
  </step>
  
  <step name="Generate PR Description">
    <description>Generate a descriptive title and a comprehensive pull request description, including a summary of changes, motivation, testing instructions, and any breaking changes. It will also automatically link to any related issues found in the branch name or commit messages.</description>
  </step>
  
  <step name="Suggest Reviewers & Labels">
    <description>Suggest appropriate reviewers based on the `CODEOWNERS` file or `git blame` history. Also, suggest relevant labels based on the types of files changed.</description>
  </step>
  
  <step name="Create Pull Request">
    <description>Create the pull request on the Git hosting platform (e.g., GitHub, GitLab), including the generated title, description, reviewers, and labels.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Use the platform-specific CLI (e.g., `gh pr create`) to create the pull request.</description>
    </tool_usage>
  </step>
</git_pr_workflow>
```

## Smart Defaults
- **Draft Mode**: Support for creating draft pull requests for work in progress.
- **Template Selection**: Can use project-defined pull request templates.
- **Conflict Detection**: Detects and warns about merge conflicts.
- **CI/CD Integration**: Can integrate with CI/CD status checks.