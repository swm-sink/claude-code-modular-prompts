---
description: Advanced pattern analysis with design pattern detection, anti-pattern identification, and architectural insights
argument-hint: "[pattern_type] [analysis_scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /analyze patterns - Pattern Analysis Framework

Advanced pattern analysis system with design pattern detection, anti-pattern identification, and comprehensive architectural insights.

## Usage
```bash
/analyze patterns design                     # Detect design patterns in codebase
/analyze patterns anti                       # Identify anti-patterns and code smells
/analyze patterns architectural             # Analyze architectural patterns
/analyze patterns all                       # Comprehensive pattern analysis
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
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

      <![CDATA[
You are a software architect. The user wants you to analyze their codebase for design patterns.

      
]]>
      <include component="components/context/find-relevant-code.md" />
      <include component="components/analysis/codebase-discovery.md" />
      <include component="components/quality/anti-pattern-detection.md" />
      <include component="components/context/adaptive-thinking.md" />
      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/input-validation.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/context/find-relevant-code.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/context/adaptive-thinking.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>paths.source</value>
    </uses_config_values>
  </dependencies>
</command_file>