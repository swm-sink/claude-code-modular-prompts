# /docs update - Documentation Synchronization Command

**Purpose**: Synchronize documentation with code changes, intelligently updating technical details while preserving custom content.

## Usage
```bash
/docs update [target] [--sync] [--drift-check]
```

## Workflow

The `/docs update` command follows a systematic process to keep documentation in sync with the codebase.

```xml
<docs_update_workflow>
  <step name="Analyze Codebase">
    <description>Scan the target codebase for changes, including function signatures, class structures, module exports, and configuration changes.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Analyze the codebase for changes relevant to documentation.</description>
    </tool_usage>
  </step>
  <step name="Detect Documentation Drift">
    <description>Compare the documentation against the current codebase to detect outdated examples, missing sections, and deprecated content.</description>
  </step>
  <step name="Intelligent Update">
    <description>Update the documentation to reflect the latest code changes, preserving user customizations and editorial content where possible.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Update the documentation files.</description>
    </tool_usage>
  </step>
  <step name="Conflict Resolution">
    <description>Highlight breaking changes, suggest content updates, and flag sections that require manual review.</description>
  </step>
</docs_update_workflow>
```

## Output
Documentation updates with change summary and drift report.