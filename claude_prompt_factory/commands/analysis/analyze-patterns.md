---
description: Detects design patterns, identifies violations and anti-patterns
argument-hint: "[target_path]"
allowed-tools: Read, Grep, Glob
---

# /analyze patterns - Design Pattern Analysis

Detects design patterns, identifies violations and anti-patterns, and suggests architectural improvements.

## Usage
```bash
/analyze patterns              # Analyze entire project
/analyze patterns src/         # Analyze specific directory
```

## Arguments
- `target_path` (optional): File or directory to analyze (default: current directory)

<command_file>
  <metadata>
    <name>/analyze patterns</name>
    <purpose>Detects design patterns, identifies violations and anti-patterns, and suggests architectural improvements.</purpose>
    <usage>
      <![CDATA[
      /analyze patterns <target_path=".">
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
      <description>Analyze design patterns in the entire project.</description>
      <usage>/analyze patterns</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a software architect. The user wants you to analyze their codebase for design patterns.

      <include component="components/context/find-relevant-code.md" />

      Once the code is identified, perform the following analysis:
      1.  **Detect Design Patterns**: Identify common design patterns (e.g., Gang of Four, architectural, domain-specific).
      2.  **Identify Violations & Anti-Patterns**: Detect violations of established patterns and common anti-patterns.
      3.  **Generate Improvement Suggestions**: Suggest opportunities for new patterns, refactoring, and fixing anti-patterns.

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