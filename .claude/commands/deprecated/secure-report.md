---
name: /secure-report
description: "Project analysis reporting with metrics, status tracking, and improvement recommendations"
argument-hint: "[report_type] [format]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-manage report"
---
# /secure report - Project Analysis Reporting

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-manage report`

This command has been consolidated into the new `/secure-manage` command with `report` mode for better organization and consistency.

---

Project analysis reporting with comprehensive metrics, status tracking, and summary reports.
## Usage
```bash
/secure report compliance            # Configuration compliance report
/secure report patterns             # Code pattern analysis report  
/secure report executive --format pdf # Executive summary in PDF
```
<command_file>
  <metadata>
    <name>/secure report</name>
    <purpose>Generates comprehensive project analysis reports with trends, improvement status, and configuration insights.</purpose>
    <usage>
      <![CDATA[
      /secure report <timeframe="30d">
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="timeframe" type="string" required="false" default="30d">
      <description>The time window for the report (e.g., '7d', '30d', '90d').</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Generate a security report for the last 30 days.</description>
      <usage>/secure report</usage>
    </example>
    <example>
      <description>Generate a security report for the last quarter.</description>
      <usage>/secure report timeframe="90d"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <!-- Command-specific components -->
      <include>components/reporting/generate-structured-report.md</include>
      You are a project analyst. The user wants a comprehensive report on the project's configuration and code quality.
      1.  **Read Configuration**: Read `project-config.yaml` to get the configured analysis and monitoring service integrations.
      2.  **Gather Analysis Data**:
          *   Fetch configuration and code quality data from the configured services for the specified `timeframe`.
          *   Incorporate results from recent analysis and audit runs.
      3.  **Analyze and Synthesize**:
          *   Analyze the data to identify improvement trends (e.g., new vs. resolved issues).
          *   Calculate key metrics like quality scores, time-to-resolve, and configuration compliance.
          *   Identify the highest-priority issues that need immediate attention.
      4.  **Generate Report**:
          *   Create a detailed analysis report with clear visualizations.
          *   Include a prioritized list of actionable recommendations.
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>analysis.scanning_service</value>
      <value>analysis.monitoring_service</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>