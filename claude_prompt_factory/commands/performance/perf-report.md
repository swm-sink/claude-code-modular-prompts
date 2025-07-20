# /perf report - Performance Reporting Command

**Purpose**: Generate comprehensive performance reports with trends, insights, and actionable recommendations.

## Usage
```bash
/perf report [--timeframe=<timeframe>] [--format=<format>]
```

## Workflow

The `/perf report` command follows a systematic process to generate performance reports.

```xml
<perf_report_workflow>
  <step name="Gather Performance Data">
    <description>Gather performance data from various sources, including monitoring tools, benchmarking results, and profiling data. The timeframe for the report can be specified with the `--timeframe` flag.</description>
    <tool_usage>
      <tool>API/Data Reader</tool>
      <description>Fetch performance data from various sources.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Data & Identify Trends">
    <description>Analyze the gathered data to identify performance trends, patterns, and anomalies. Calculate key performance metrics, such as response times, throughput, and error rates.</description>
    <tool_usage>
      <tool>Data Analysis</tool>
      <description>Use data analysis techniques to process the performance data.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Report & Recommendations">
    <description>Generate a comprehensive report that summarizes the findings and provides actionable recommendations for improvement. The format of the report can be specified with the `--format` flag (e.g., 'summary', 'detailed', 'dashboard').</description>
    <output>A detailed performance report.</output>
  </step>
</perf_report_workflow>
```

## Configuration

The `/perf report` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/perf report">
  <setting name="default_timeframe" value="7d" description="The default timeframe for performance reports." />
  <setting name="default_report_format" value="summary" description="The default format for performance reports." />
</command>
```

## Use Cases

*   **Performance Reviews**: Regularly review performance reports to track progress and identify areas for improvement.
*   **Capacity Planning**: Use performance data to forecast future resource needs and plan for scaling.
*   **Stakeholder Communication**: Communicate performance metrics and trends to stakeholders in a clear and concise format.