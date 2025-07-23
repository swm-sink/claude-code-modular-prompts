---
description: API versioning strategy with backward compatibility, migration paths, and deprecation management
argument-hint: "[version_strategy] [migration_approach]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /api version - API Versioning Management

Comprehensive API versioning system with backward compatibility, migration strategies, and deprecation lifecycle management.

## Usage
```bash
/api version create v2.0                     # Create new API version
/api version migrate                         # Generate migration guide
/api version deprecate v1.0                  # Manage version deprecation
/api version --strategy semantic            # Implement semantic versioning
```

## Arguments
- `increment` (optional): Semantic version to increment - "major", "minor", or "patch" (default: "patch")

<command_file>
  <metadata>
    <name>/api version</name>
    <purpose>Manages API versions, including incrementing versions and planning deprecation strategies.</purpose>
    <usage>
      <![CDATA[
      /api version <increment="patch">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="increment" type="string" required="false" default="patch">
      <description>The semantic version to increment (major, minor, or patch).</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Perform a patch version increment.</description>
      <usage>/api version</usage>
    </example>
    <example>
      <description>Perform a major version increment for a breaking change.</description>
      <usage>/api version increment="major"</usage>
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
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/git/git-commit.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      
      <![CDATA[
You are an API release manager. The user wants to manage their API version.

      1.  **Analyze Changes**: Analyze recent API changes to identify breaking changes and determine the appropriate version increment (major, minor, patch).
      2.  **Implement Versioning**: Propose code changes to implement the new version, such as updating version headers or routing.
      3.  **Plan Migration & Deprecation**: Create a migration guide for users, documenting breaking changes and setting a deprecation timeline for the old version.

      Your output should be a plan and the proposed code changes.
]]>
    </prompt>
  </claude_prompt>

  <includes_components>
    <component>components/constitutional/safety-framework.md</component>
  </includes_components>
</command_file>