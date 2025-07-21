---
description: Comprehensive code analysis with quality metrics, pattern detection, and improvement recommendations
argument-hint: "[analysis_scope] [analysis_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /analyze code - Comprehensive Code Analysis

Advanced code analysis system with quality metrics, pattern detection, technical debt assessment, and improvement recommendations.

## Usage
```bash
/analyze code quality                        # Analyze code quality metrics
/analyze code patterns                       # Detect code patterns and anti-patterns
/analyze code security                       # Security-focused code analysis
/analyze code performance                    # Performance bottleneck analysis
```

## Arguments

<argument name="target_path" type="string" required="false" default=".">
  <description>The file or directory to analyze. Defaults to the current directory.</description>
</argument>
<argument name="focus" type="string" required="false" default="full">
  <description>The specific area to focus on (e.g., 'performance', 'security', 'quality').</description>
</argument>

## Examples

<example>
  <description>Run a full analysis on the entire project.</description>
  <usage>/analyze code</usage>
</example>
<example>
  <description>Analyze only the 'security' aspects of a specific file.</description>
  <usage>/analyze code "src/auth/service.py" focus="security"</usage>
</example>

## Claude Prompt

You are an expert code analyst. The user wants to perform a comprehensive analysis of their codebase.
Your analysis should focus on structure, patterns, complexity, and improvement opportunities.

<include component="components/analysis/codebase-discovery.md" />
<include component="components/quality/anti-pattern-detection.md" />
<include component="components/context/adaptive-thinking.md" />
<include component="components/reporting/generate-structured-report.md" />

## Dependencies

<includes_components>
  <component>components/analysis/codebase-discovery.md</component>
  <component>components/quality/anti-pattern-detection.md</component>
  <component>components/context/adaptive-thinking.md</component>
  <component>components/reporting/generate-structured-report.md</component>
</includes_components>
<uses_config_values>
  <value>paths.source</value>
  <value>paths.tests</value>
</uses_config_values>