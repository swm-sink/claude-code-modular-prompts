---
description: Manages API versions, incrementing versions and planning deprecation strategies
argument-hint: "[increment]"
allowed-tools: Read, Write, Grep, Edit
---

# /api version - API Version Management

Manages API versions, including incrementing versions and planning deprecation strategies.

## Usage
```bash
/api version                    # Patch version increment (default)
/api version increment="major"  # Major version for breaking changes
/api version increment="minor"  # Minor version for new features
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
      <![CDATA[
You are an API release manager. The user wants to manage their API version.

      1.  **Analyze Changes**: Analyze recent API changes to identify breaking changes and determine the appropriate version increment (major, minor, patch).
      2.  **Implement Versioning**: Propose code changes to implement the new version, such as updating version headers or routing.
      3.  **Plan Migration & Deprecation**: Create a migration guide for users, documenting breaking changes and setting a deprecation timeline for the old version.

      Your output should be a plan and the proposed code changes.
]]>
    </prompt>
  </claude_prompt>

  <dependencies>
    <!-- This command is self-contained -->
  </dependencies>
</command_file>