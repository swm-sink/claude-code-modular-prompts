# /git commit - Intelligent Commit Message Generator

**Purpose**: Generate intelligent, meaningful commit messages following the Conventional Commits format, with automated staging and quality validation.

## Usage
```bash
/git commit "[description]" [--type=feat|fix|docs|style|refactor|test|chore]
```

## Workflow

The `/git commit` command follows a systematic process to create high-quality commits.

```xml
<git_commit_workflow>
  <step name="Analyze & Stage Changes">
    <description>Analyze the changed files to determine the appropriate commit type and scope. Stage the relevant files for a coherent commit.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Use `git status` and `git diff` to analyze changes, and `git add` to stage them.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Commit Message">
    <description>Generate a commit message that follows the Conventional Commits standard, including the type, scope, description, and any breaking changes.</description>
  </step>
  
  <step name="Validate & Commit">
    <description>Validate the commit message format and run any pre-commit hooks (linting, formatting, tests). If validation passes, create the commit.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run pre-commit hooks and then `git commit`.</description>
    </tool_usage>
  </step>
</git_commit_workflow>
```

## Conventional Commit Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation