---
description: Comprehensive security reporting with metrics, compliance status, and remediation tracking
argument-hint: "[report_type] [format]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-manage report"
---
# /secure report - Security Reporting System

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-manage report`

This command has been consolidated into the new `/secure-manage` command with `report` mode for better organization and consistency.

---

Advanced security reporting with comprehensive metrics, compliance tracking, and executive summaries.
## Usage
```bash
/secure report compliance            # Compliance status report
/secure report vulnerabilities      # Vulnerability assessment report  
/secure report executive --format pdf # Executive summary in PDF
```
<command_file>
  <metadata>
    <name>/secure report</name>
    <purpose>Generates comprehensive security reports with trends, remediation status, and compliance insights.</purpose>
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
      You are a security analyst. The user wants a comprehensive report on the project's security posture.
      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured security scanning and monitoring service integrations.
      2.  **Gather Security Data**:
          *   Fetch vulnerability and compliance data from the configured services for the specified `timeframe`.
          *   Incorporate results from recent `/secure scan` and `/secure audit` runs.
      3.  **Analyze and Synthesize**:
          *   Analyze the data to identify security trends (e.g., new vs. fixed vulnerabilities).
          *   Calculate key metrics like risk scores, time-to-remediate, and compliance status.
          *   Identify the highest-risk vulnerabilities that need immediate attention.
      4.  **Generate Report**:
          *   Create a detailed security report with clear visualizations.
          *   Include a prioritized list of actionable recommendations.
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>security.scanning_service</value>
      <value>security.monitoring_service</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>