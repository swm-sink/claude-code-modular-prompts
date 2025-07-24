---
description: Quality metrics collection with comprehensive scoring, trend analysis, and benchmark comparison
argument-hint: "[metrics_scope] [time_period]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /quality metrics - Quality Metrics Framework

Advanced quality metrics system with comprehensive scoring, trend analysis, and benchmark comparison.

## Usage
```bash
/quality metrics overall                     # Overall quality score
/quality metrics trends                      # Quality trend analysis
/quality metrics benchmarks                  # Compare against benchmarks
/quality metrics dashboard                   # Generate quality dashboard
```

<command_file>
  <metadata>
    <name>/quality metrics</name>
    <purpose>Calculates and tracks code quality metrics, with support for trend analysis and benchmarks.</purpose>
    <usage>
      <![CDATA[
      /quality metrics <target_path=".">
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
      <description>Calculate quality metrics for the entire project.</description>
      <usage>/quality metrics</usage>
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

      You are a software quality analyst. The user wants you to calculate code quality metrics.

      <include component="components/context/find-relevant-code.md" />

      Once the code is identified, perform the following analysis:
      1.  **Calculate Metrics**: Analyze the codebase to calculate metrics for complexity, maintainability, test coverage, and technical debt.
      2.  **Perform Trend Analysis**: Compare current metrics against historical data to identify trends.
      3.  **Compare Against Benchmarks**: Compare metrics against industry standards to identify areas for improvement.

      <include component="components/quality/quality-metrics.md" />
      <include component="components/analytics/business-intelligence.md" />
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
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>paths.source</value>
    </uses_config_values>
  </dependencies>
</command_file>