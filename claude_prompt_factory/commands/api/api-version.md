# /api version - API Version Management Command

**Purpose**: Manage API versions, including incrementing versions, planning deprecation strategies, and ensuring backward compatibility.

## Usage
```bash
/api version [--increment=major|minor|patch] [--deprecate=version]
```

## Workflow

The `/api version` command follows a systematic process to manage API versions.

```xml
<api_versioning_workflow>
  <step name="Analyze Changes">
    <description>Analyze the recent changes to the API to identify any breaking changes and determine the appropriate version increment (major, minor, or patch) based on semantic versioning.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Use `git diff` to analyze changes since the last version tag.</description>
    </tool_usage>
  </step>
  
  <step name="Implement Versioning">
    <description>Implement the new version by updating the API version headers, implementing version routing, and, if necessary, maintaining legacy endpoints with deprecation warnings.</description>
  </step>
  
  <step name="Plan Migration & Deprecation">
    <description>Create a migration guide that documents any breaking changes, provides code examples for the new version, and sets a clear deprecation timeline for the old version.</description>
  </step>
</api_versioning_workflow>
```

## Quality Gates
- **Semantic Versioning Compliance**: Ensures that version numbers are incremented correctly based on the nature of the changes.
- **Backward Compatibility Verification**: Verifies that non-breaking changes do not unintentionally break existing clients.
- **Migration Path Validation**: Validates that the provided migration path is clear and actionable for API consumers.
- **Consumer Impact Assessment**: Assesses the potential impact of the version change on API consumers.