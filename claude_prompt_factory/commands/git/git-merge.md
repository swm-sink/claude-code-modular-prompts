# /git merge - Safe Git Merge Command

**Purpose**: Perform safe Git merges with comprehensive pre-merge validation and conflict resolution assistance.

## Usage
```bash
/git merge [branch]
```

## Workflow

The `/git merge` command follows a systematic process to perform safe Git merges.

```xml
<git_merge_workflow>
  <step name="Pre-Merge Validation">
    <description>Perform a series of pre-merge validation checks, including verifying a clean working directory, checking for remote updates, and previewing potential merge conflicts.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run `git fetch`, `git status`, and `git diff` to perform pre-merge checks.</description>
    </tool_usage>
  </step>
  
  <step name="Perform Merge">
    <description>Perform the merge using a safe, non-fast-forward strategy. If conflicts are detected, provide interactive assistance to resolve them.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run `git merge --no-ff` and, if necessary, `git mergetool`.</description>
    </tool_usage>
  </step>
  
  <step name="Post-Merge Validation">
    <description>After the merge is complete, run a series of post-merge quality gates, including running tests, verifying the build, and performing lint checks, to ensure the integrity of the merged codebase.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run tests, build, and lint commands.</description>
    </tool_usage>
  </step>
</git_merge_workflow>
```

## Quality Gates
- **Test Validation**: Runs tests before finalizing the merge.
- **Build Verification**: Ensures the build succeeds after the merge.
- **Lint Checks**: Validates code quality standards on the merged code.
- **Documentation Updates**: Checks for corresponding documentation changes.