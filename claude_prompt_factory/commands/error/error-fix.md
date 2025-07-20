# /error fix - Automated Error Fixing Command

**Purpose**: Automatically apply safe and verified fixes for diagnosed errors.

## Usage
```bash
/error fix [--auto] [--verify] [--dry-run]
```

## Workflow

The `/error fix` command follows a systematic process to automatically fix errors.

```xml
<error_fix_workflow>
  <step name="Diagnose Error">
    <description>First, run the `/error diagnose` command to get a detailed diagnosis of the error, including the root cause and suggested fixes.</description>
    <tool_usage>
      <tool>/error diagnose</tool>
      <description>Use the error diagnosis command to understand the issue.</description>
    </tool_usage>
  </step>
  
  <step name="Generate & Apply Fix">
    <description>Based on the diagnosis, generate a code patch to fix the error. If the `--dry-run` flag is used, display the proposed patch without applying it. If the `--auto` flag is used, apply the patch without confirmation.</description>
    <tool_usage>
      <tool>AI/Code Generation</tool>
      <description>Generate a code patch based on the error diagnosis.</description>
    </tool_usage>
  </step>
  
  <step name="Verify Fix">
    <description>If the `--verify` flag is used, run the relevant tests to ensure that the fix has resolved the error and has not introduced any regressions. If the verification fails, automatically roll back the changes.</description>
    <tool_usage>
      <tool>/test unit</tool>
      <description>Run unit tests to verify the fix.</description>
    </tool_usage>
  </step>
</error_fix_workflow>
```

## Configuration

The `/error fix` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/error fix">
  <setting name="default_fix_level" value="safe" description="The default fix level to use (e.g., 'safe', 'moderate', 'aggressive')." />
  <setting name="auto_verify" value="true" description="Whether to automatically run tests to verify fixes." />
</command>
```

## Use Cases

*   **Accelerated Debugging**: Quickly fix common errors without manual intervention.
*   **CI/CD Pipelines**: Automatically fix failing builds caused by simple errors.
*   **Code Maintenance**: Proactively fix known issues in the codebase.