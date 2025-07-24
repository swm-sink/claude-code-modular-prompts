---
description: [BRIEF_DESCRIPTION] - clear, one-line description of what this command does
argument-hint: "[argument1] [argument2] [optional_argument]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /[COMMAND_NAME] - [TITLE]

[DETAILED_DESCRIPTION] - Comprehensive description of what this command accomplishes and when to use it.

## Usage
```bash
/[COMMAND_NAME] "[required_argument]" [optional_argument]
/[COMMAND_NAME] "[example_usage_1]"
/[COMMAND_NAME] "[example_usage_2]" optional_flag=true
```

## Arguments
- `[required_argument]` (required): [Description of what this argument does and expected format]
- `[optional_argument]` (optional): [Description of optional argument, default behavior]

## What It Does
1. **[Phase 1 Name]**: [Brief description of first major phase]
2. **[Phase 2 Name]**: [Brief description of second major phase]
3. **[Phase 3 Name]**: [Brief description of third major phase]
4. **[Phase 4 Name]**: [Brief description of fourth major phase]
5. **[Phase 5 Name]**: [Brief description of final phase]

<command_file>
  <metadata>
    <name>/[COMMAND_NAME]</name>
    <purpose>[DETAILED_PURPOSE] - what this command accomplishes end-to-end</purpose>
    <usage>
      <![CDATA[
      /[COMMAND_NAME] "[argument_description]" <optional_argument=default_value>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="[required_argument]" type="string" required="true">
      <description>[Detailed description of the required argument and its expected format/content]</description>
    </argument>
    <argument name="[optional_argument]" type="boolean" required="false" default="false">
      <description>[Detailed description of the optional argument and its behavior]</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>[Description of what this example demonstrates]</description>
      <usage>/[COMMAND_NAME] "[concrete_example_input]"</usage>
    </example>
    <example>
      <description>[Description of a more complex example]</description>
      <usage>/[COMMAND_NAME] "[complex_example]" optional_argument=true</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <![CDATA[
You are [ROLE_DESCRIPTION] - e.g., "a senior engineer specializing in X" or "an expert in Y domain".

      1.  **[Phase 1 Name]**:
          *   [Detailed description of what happens in this phase]
          *   [Specific actions or analysis to perform]
          *   
]]>
      <include component="components/[RELEVANT_COMPONENT_1].md" />
      <![CDATA[

      2.  **[Phase 2 Name]**:
          *   [Detailed description of what happens in this phase]
          *   [Specific actions or analysis to perform]
          *   
]]>
      <include component="components/[RELEVANT_COMPONENT_2].md" />
      <include component="components/interaction/progress-reporting.md" />
      <![CDATA[

      3.  **[Phase 3 Name]**:
          *   [Detailed description of what happens in this phase]
          *   [Specific actions or analysis to perform]
          *   
]]>
      <include component="components/interaction/request-user-confirmation.md" />
      <![CDATA[

      4.  **[Phase 4 Name]**:
          *   [Detailed description of what happens in this phase]
          *   [Specific actions or analysis to perform]
          *   
]]>
      <include component="components/actions/apply-code-changes.md" />
      <include component="components/workflow/error-handling.md" />
      <![CDATA[

      5.  **[Phase 5 Name]**:
          *   [Detailed description of what happens in this phase]
          *   [Final reporting and validation steps]
          *   
]]>
      <include component="components/workflow/report-generation.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/[RELATED_COMMAND_1]</command>
      <command>/[RELATED_COMMAND_2]</command>
    </chain>
    <includes_components>
      <component>components/[RELEVANT_COMPONENT_1].md</component>
      <component>components/[RELEVANT_COMPONENT_2].md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/workflow/report-generation.md</component>
    </includes_components>
  </dependencies>
</command_file>