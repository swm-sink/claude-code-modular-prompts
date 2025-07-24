---
description: [CORE_DESCRIPTION] - foundational functionality for the Claude Code Prompt Factory
argument-hint: "[core_argument]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, Task
category: core
priority: high
---

# /[CORE_NAME] - [CORE_TITLE]

[DETAILED_DESCRIPTION] - Core functionality that provides foundational capabilities for the entire Claude Code Prompt Factory system.

## Core Responsibility
This core component is responsible for [PRIMARY_RESPONSIBILITY] and ensures [SYSTEM_BEHAVIOR] across all commands and components.

## Usage
```bash
/[CORE_NAME] "[core_argument]"
/[CORE_NAME] "[example_usage_1]"
/[CORE_NAME] init
/[CORE_NAME] validate
```

## Arguments
- `[core_argument]` (required): [Description of core argument and its impact on system behavior]
- `init` (optional): Initialize core functionality
- `validate` (optional): Validate core system integrity

## Core Operations
1. **[Core Operation 1]**: [Fundamental system operation]
2. **[Core Operation 2]**: [Essential system behavior]  
3. **[Core Operation 3]**: [Critical system function]
4. **[Core Operation 4]**: [Base system capability]

<command_file>
  <metadata>
    <name>/[CORE_NAME]</name>
    <purpose>[CORE_PURPOSE] - foundational system capability that enables [SYSTEM_CAPABILITY]</purpose>
    <category>core</category>
    <priority>high</priority>
    <usage>
      <![CDATA[
      /[CORE_NAME] "[core_argument]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="[core_argument]" type="string" required="true">
      <description>[Detailed description of core argument and its system-wide impact]</description>
    </argument>
    <argument name="mode" type="string" required="false" default="standard">
      <description>Operation mode: standard, init, validate, or debug</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>[Description of standard core operation]</description>
      <usage>/[CORE_NAME] "[standard_example]"</usage>
    </example>
    <example>
      <description>[Description of initialization operation]</description>
      <usage>/[CORE_NAME] "init"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <![CDATA[
You are the [CORE_ROLE] responsible for [CORE_RESPONSIBILITY]. Your role is foundational to the entire Claude Code Prompt Factory system.

      1.  **[Core Phase 1]**:
          *   [Critical system operation or validation]
          *   [Foundational setup or configuration]
          *   
]]>
      <include component="components/[CORE_COMPONENT_1].md" />
      <include component="components/analysis/codebase-discovery.md" />
      <![CDATA[

      2.  **[Core Phase 2]**:
          *   [Essential system behavior or routing]
          *   [Core decision-making or processing]
          *   
]]>
      <include component="components/planning/create-step-by-step-plan.md" />
      <include component="components/interaction/progress-reporting.md" />
      <![CDATA[

      3.  **[Core Phase 3]**:
          *   [System validation or integrity checks]
          *   [Core functionality execution]
          *   
]]>
      <include component="components/workflow/error-handling.md" />
      <![CDATA[

      4.  **[Core Phase 4]**:
          *   [System reporting or status updates]
          *   [Core operation completion and handoff]
          *   
]]>
      <include component="components/workflow/report-generation.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <system_requirements>
      <requirement>Core system integrity validation</requirement>
      <requirement>Component dependency resolution</requirement>
      <requirement>Command routing and execution</requirement>
    </system_requirements>
    <includes_components>
      <component>components/[CORE_COMPONENT_1].md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/workflow/report-generation.md</component>
    </includes_components>
  </dependencies>
</command_file>