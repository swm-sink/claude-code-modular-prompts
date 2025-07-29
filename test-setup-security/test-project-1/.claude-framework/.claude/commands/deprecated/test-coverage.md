---
name: /test-coverage
description: "Advanced test coverage analysis with intelligent gap detection, quality metrics, and comprehensive coverage optimization"
argument-hint: "[coverage_scope] [analysis_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/test"
migration_path: "/test coverage or /test --coverage"
removal_version: "2.0.0"
---
# /test coverage - Advanced Test Coverage Analysis

## ⚠️ DEPRECATION NOTICE

**This command is deprecated and will be removed in version 2.0.0.**

- **Deprecated Date**: 2025-07-25
- **Migration Path**: Use `/test coverage` or `/test --coverage` instead
- **Reason**: Command functionality has been consolidated into the unified `/test` command
- **Timeline**: This command will continue to work until version 2.0.0

### Migration Examples:
```bash
# Old usage:
/test coverage analyze
/test coverage --gaps
/test coverage --quality

# New usage:
/test coverage
/test --coverage
/test coverage --gaps
/test coverage --quality
```

---

Sophisticated test coverage analysis system with intelligent gap detection, quality metrics, and comprehensive coverage optimization.
## Usage
```bash
/test coverage analyze                       # Coverage analysis and reporting
/test coverage --gaps                        # Coverage gap detection
/test coverage --quality                     # Quality-focused coverage analysis
/test coverage --comprehensive               # Comprehensive coverage optimization
```
<command_file>
  <metadata>
    <name>/test coverage</name>
    <purpose>Analyzes test coverage, generates comprehensive reports, and tracks coverage metrics.</purpose>
    <usage>
      <![CDATA[
      /test coverage <path="./src">
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="path" type="string" required="false" default="./src">
      <description>The source directory to analyze for test coverage.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Calculate test coverage for the entire 'src' directory.</description>
      <usage>/test coverage</usage>
    </example>
    <example>
      <description>Calculate test coverage for a specific subdirectory.</description>
      <usage>/test coverage path="./src/api"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
      You are a quality assurance analyst. The user wants to analyze the project's test coverage.
      1.  **Read Configuration**: Read `project-config.yaml` to get the configured test command and coverage options.
      2.  **Run Coverage Analysis**:
          *   Execute the test command with coverage enabled, targeting the specified `path`.
      3.  **Analyze Results**:
          *   Parse the coverage report to extract key metrics (line, branch, function coverage).
          *   Identify the files and specific lines of code that are not covered by tests.
      4.  **Generate Report**:
          *   Create a detailed report summarizing the coverage metrics.
          *   Highlight the top 5 least-covered files that need attention.
          *   Provide actionable recommendations for improving test coverage.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>testing.test_command</value>
      <value>testing.coverage_options</value>
      <value>paths.source</value>
    </uses_config_values>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>