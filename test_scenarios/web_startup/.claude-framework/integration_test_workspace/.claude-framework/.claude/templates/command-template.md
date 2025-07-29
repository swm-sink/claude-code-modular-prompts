---
description: Brief, clear description of what this command does
argument-hint: "[required_arg] [optional_arg]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /command-name - Brief Title

Clear description of the command's purpose and functionality.

## Usage
```bash
/command-name required_arg                   # Basic usage
/command-name --flag                         # With flags
/command-name required_arg optional_arg      # Full usage
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `required_arg` | string | true | What it does |
| `optional_arg` | string | false | What it does (default: value) |

## Examples

```bash
/command-name example_value                  # Description of example
/command-name --common-flag                  # Description of flag usage
```

<command_file>
  <metadata>
    <name>/command-name</name>
    <purpose>Brief purpose statement</purpose>
    <usage>
      <![CDATA[
      /command-name [required_arg] [optional_arg]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="required_arg" type="string" required="true">
      <description>Description of required argument</description>
    </argument>
    <argument name="optional_arg" type="string" required="false" default="default_value">
      <description>Description of optional argument</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Basic usage example</description>
      <usage>/command-name example_value</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard components (always include) -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/category/specific-component.md</include>
      
You are a [role] specialist. The user wants to [accomplish what].

**Process:**
1. **Step 1**: Clear action description
2. **Step 2**: Next action description  
3. **Step 3**: Final action description

**Implementation Strategy:**
- Bullet point of what to do
- Another action item
- Final consideration

    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/category/specific-component.md</component>
    </includes_components>
    <uses_config_values>
      <value>config.section.property</value>
    </uses_config_values>
  </dependencies>
</command_file>