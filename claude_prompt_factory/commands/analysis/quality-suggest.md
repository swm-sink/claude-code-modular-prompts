---
description: Advanced quality suggestions with intelligent recommendations, automated improvements, and best practice guidance
argument-hint: "[suggestion_scope] [improvement_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /analyze quality-suggest - Advanced Quality Suggestions

Sophisticated quality suggestion system with intelligent recommendations, automated improvements, and comprehensive best practice guidance.

## Usage
```bash
/analyze quality-suggest comprehensive       # Comprehensive quality suggestions
/analyze quality-suggest --performance       # Performance improvement suggestions
/analyze quality-suggest --security          # Security enhancement suggestions
/analyze quality-suggest --maintainability   # Maintainability improvements
```

<command_file>
  <metadata>
    <name>/quality suggest</name>
    <purpose>Generates a prioritized, actionable list of quality improvement suggestions.</purpose>
    <usage>
      <![CDATA[
      /quality suggest <target_path=".">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target_path" type="string" required="false" default=".">
      <description>The file or directory to analyze. Defaults to the current directory.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Get quality improvement suggestions for the entire project.</description>
      <usage>/quality suggest</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a senior software architect. Your task is to provide a prioritized, actionable list of quality improvements.

      <include component="components/context/find-relevant-code.md" />

      Once the code is identified, perform the following:
      1.  **Analyze Code Quality**: Identify areas for improvement in performance, maintainability, security, and documentation.
      2.  **Prioritize Opportunities**: Prioritize the opportunities based on their potential impact and estimated effort.
      3.  **Generate Suggestions**: Generate a clear list of suggestions, complete with code examples.

      Your output should be a structured report, but instead of findings, the sections should be prioritized suggestions (e.g., "Priority 1: High Impact, Low Effort").

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>paths.source</value>
    </uses_config_values>
  </dependencies>
</command_file>
