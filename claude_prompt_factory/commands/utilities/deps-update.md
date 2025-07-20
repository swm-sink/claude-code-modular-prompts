# /deps update - Safe Dependency Update Command

**Purpose**: Safely update project dependencies with compatibility validation, automated testing, and rollback protection to prevent breaking changes.

## Usage
```bash
/deps update [--minor|--patch] [--test-after]
```

## Workflow

The `/deps update` command follows a systematic process to safely update dependencies.

```xml
<deps_update_workflow>
  <step name="Analyze Dependencies & Plan Updates">
    <description>Analyze the project's dependencies to identify outdated packages and plan the update strategy (e.g., minor updates only, patch updates only). Check for any known breaking changes.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate package manager command to check for outdated dependencies.</description>
    </tool_usage>
  </step>
  
  <step name="Update Dependencies Incrementally">
    <description>Update the dependencies incrementally, one at a time or in small, safe groups. Create a pre-update snapshot or backup to enable easy rollback.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate package manager command to update dependencies.</description>
    </tool_usage>
  </step>
  
  <step name="Validate Updates">
    <description>After each update, run the full test suite to ensure that the change has not introduced any regressions. If tests fail, automatically roll back the update.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the test suite and, if necessary, the package manager command to roll back the update.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed report of the updates, including version changes, any breaking change warnings, and a summary of the test results.</description>
    <output>A comprehensive dependency update report.</output>
  </step>
</deps_update_workflow>
```

## Key Features
- **Smart Updates**: Analyzes dependency compatibility before updating.
- **Incremental Updates**: Updates dependencies individually or in safe groups.
- **Test Validation**: Runs the full test suite after each update.
- **Breaking Change Detection**: Identifies potential API changes in new versions.
- **Automated Rollback**: Reverts updates on test failures or compatibility issues.