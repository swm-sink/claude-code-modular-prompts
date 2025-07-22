---
description: Comprehensive error reporting with metrics, trend analysis, and actionable insights
argument-hint: "[report_type] [time_period]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /error report - Error Analytics & Reporting

Advanced error reporting system with trend analysis, root cause correlation, and actionable insights.

## Usage
```bash
/error report summary                        # Generate error summary report
/error report trends --period week          # Weekly error trend analysis
/error report critical                      # Focus on critical error patterns
/error report dashboard                     # Create interactive error dashboard
```

<command_file>
  <metadata>
    <n>/error report</n>
    <purpose>Comprehensive error reporting with metrics, trend analysis, and actionable insights</purpose>
    <usage>
      <![CDATA[
      /error report [report_type] --period [time_period]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="report_type" type="string" required="false" default="summary">
      <description>The type of error report to generate (e.g., summary, trends, critical)</description>
    </argument>
    <argument name="time_period" type="string" required="false" default="7d">
      <description>The time window for the report (e.g., '24h', '7d', '30d')</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate a summary error report for the last week</description>
      <usage>/error report summary --period 7d</usage>
    </example>
    <example>
      <description>Analyze weekly error trends</description>
      <usage>/error report trends --period week</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/analytics/business-intelligence.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/analysis/trend-analysis.md</include>
      <include>components/visualization/performance-charts.md</include>
      <include>components/analytics/data-aggregation.md</include>
      
You are an advanced error reporting and analytics specialist. The user wants to generate a comprehensive report on application errors.

**Error Reporting Process:**
1. **Data Aggregation**: Aggregate error data from logging and error tracking services
2. **Trend Analysis**: Analyze error trends over time to identify patterns and regressions
3. **Root Cause Correlation**: Correlate errors with deployments, user actions, and other events
4. **Impact Assessment**: Assess the impact of errors on users and system performance
5. **Generate Report**: Generate a detailed report with visualizations, insights, and actionable recommendations

**Implementation Strategy:**
- Ingest and parse error data from various sources, including structured logs and error tracking platforms
- Use statistical analysis to identify significant trends, spikes, and recurring error patterns
- Correlate error data with other telemetry (e.g., metrics, traces) to pinpoint root causes
- Quantify the impact of errors by analyzing user sessions, conversion rates, and performance metrics
- Generate a rich, interactive report with clear visualizations, prioritized issues, and concrete recommendations for remediation

    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/context/adaptive-thinking.md</component>
      <component>components/interaction/progress-reporting.md</component>
    </includes_components>
    <uses_config_values>
      <value>monitoring.logging_service</value>
      <value>monitoring.error_tracking_service</value>
    </uses_config_values>
  </dependencies>
</command_file>