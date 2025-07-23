---
# YAML FRONTMATTER - REQUIRED FOR ALL COMMANDS
description: "[BRIEF_DESCRIPTION] - Clear, action-oriented one-line description"
argument-hint: "[arg1] [arg2] [optional_arg]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
template-version: "2.0"
compliance-level: "strict"
---

# /[COMMAND_NAME] - [TITLE]

[DETAILED_DESCRIPTION] - Comprehensive description with clear use cases and expected outcomes.

## Usage
```bash
/[COMMAND_NAME] "[required_argument]" [optional_argument]
```

## Arguments
- `[required_argument]` (required): [Description with format/constraints]
- `[optional_argument]` (optional, default: "[default_value]"): [Description]

## What It Does
1. **[Phase 1]**: [Description]
2. **[Phase 2]**: [Description]  
3. **[Phase 3]**: [Description]
4. **[Phase 4]**: [Description]
5. **[Phase 5]**: [Description]

<command_file>
  <metadata>
    <name>/[COMMAND_NAME]</name>
    <purpose>[DETAILED_PURPOSE]</purpose>
    <usage>
      <![CDATA[
      /[COMMAND_NAME] "[argument_description]" <optional_arg=default>
      ]]>
    </usage>
    <template_version>2.0</template_version>
  </metadata>

  <arguments>
    <argument name="[required_argument]" type="string" required="true">
      <description>[Detailed description]</description>
      <validation>[Validation rules]</validation>
    </argument>
    <argument name="[optional_argument]" type="string" required="false" default="[default_value]">
      <description>[Detailed description]</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>[Example description]</description>
      <usage>/[COMMAND_NAME] "[example_input]"</usage>
      <expected_outcome>[Expected result]</expected_outcome>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <![CDATA[
You are [ROLE_DESCRIPTION].

1. **[Phase 1]**:
   - [Detailed action]
   - [Specific requirement]
]]>
      <include component="components/[COMPONENT].md" />
      <![CDATA[

2. **[Phase 2]**:
   - [Detailed action]
   - [Specific requirement]
]]>
      <include component="components/interaction/progress-reporting.md" />
      <![CDATA[

3. **[Phase 3]**:
   - [Detailed action]
   - [Specific requirement]
]]>
      <include component="components/interaction/request-user-confirmation.md" />
      <![CDATA[

4. **[Phase 4]**:
   - [Detailed action]
   - [Specific requirement]
]]>
      <include component="components/actions/apply-code-changes.md" />
      <include component="components/workflow/error-handling.md" />
      <![CDATA[

5. **[Phase 5]**:
   - [Final validation]
   - [Report generation]
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
      <component>components/[COMPONENT].md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/workflow/report-generation.md</component>
    </includes_components>
  </dependencies>

  <validation>
    <xml_well_formed>true</xml_well_formed>
    <required_sections>
      <section>metadata</section>
      <section>arguments</section>
      <section>claude_prompt</section>
      <section>dependencies</section>
    </required_sections>
  </validation>
</command_file>