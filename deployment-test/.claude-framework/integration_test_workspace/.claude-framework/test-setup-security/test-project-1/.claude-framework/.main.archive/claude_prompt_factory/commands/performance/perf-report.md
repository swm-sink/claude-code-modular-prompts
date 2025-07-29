---
description: Performance reporting with comprehensive metrics, trends, and recommendations
argument-hint: "[report_type] [time_period]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /perf report - Performance Reporting System

Comprehensive performance reporting with trend analysis, recommendations, and executive summaries.

## Usage
```bash
/perf report weekly                  # Weekly performance report
/perf report trends --period month  # Monthly trend analysis
/perf report executive              # Executive performance summary
```

<command_file>
  <metadata>
    <name>/perf report</name>
    <purpose>Generates comprehensive performance reports with trends, insights, and actionable recommendations.</purpose>
    <usage>
      <![CDATA[
      /perf report <timeframe="7d">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="timeframe" type="string" required="false" default="7d">
      <description>The time window for the report (e.g., '24h', '7d', '30d').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate a performance report for the last 7 days.</description>
      <usage>/perf report</usage>
    </example>
    <example>
      <description>Generate a performance report for the last 30 days.</description>
      <usage>/perf report timeframe="30d"</usage>
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
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/analysis/trend-analysis.md</include>
      <include>components/visualization/performance-charts.md</include>
      <include>components/analysis/performance-metrics.md</include>
      <include>components/optimization/recommendation-engine.md</include>
      
      You are a performance analyst. The user wants a report on application performance.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured monitoring and benchmarking data sources.
      2.  **Gather Performance Data**:
          *   Fetch performance data (e.g., response times, throughput, error rates) from the configured services for the specified `timeframe`.
          *   Incorporate data from recent benchmark runs.
      3.  **Analyze and Identify Trends**:
          *   Analyze the data to identify performance trends, patterns, and anomalies.
          *   Compare the current performance against historical baselines.
      4.  **Generate Report**:
          *   Create a comprehensive report with clear visualizations of key performance metrics.
          *   Highlight any significant performance regressions or improvements.
          *   Provide actionable recommendations for optimization.
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>monitoring.performance_monitoring_service</value>
      <value>performance.benchmark_tool</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>