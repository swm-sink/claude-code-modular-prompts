# /perf monitor - Performance Monitoring Command

**Purpose**: Set up continuous performance monitoring with real-time metrics, trend analysis, and automated alerting.

## Usage
```bash
/perf monitor [--duration=<duration>] [--metrics=<metrics>]
```

## Workflow

The `/perf monitor` command follows a systematic process to monitor performance.

```xml
<perf_monitor_workflow>
  <step name="Initialize Monitor & Collect Metrics">
    <description>Initialize the performance monitor and begin collecting real-time metrics for the specified duration. The `--metrics` flag can be used to specify which metrics to collect (e.g., 'cpu,memory,io').</description>
    <tool_usage>
      <tool>Monitoring Tool</tool>
      <description>Use a monitoring tool (e.g., Prometheus, Datadog) to collect performance metrics.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Trends & Check Thresholds">
    <description>Analyze the collected metrics to identify performance trends and patterns. Check the metrics against predefined thresholds to detect any performance issues or anomalies.</description>
    <tool_usage>
      <tool>Analysis & Alerting Tool</tool>
      <description>Use a tool to analyze the metrics and trigger alerts if thresholds are breached.</description>
    </tool_usage>
  </step>
  
  <step name="Visualize & Generate Report">
    <description>Generate a performance dashboard to visualize the real-time metrics and trends. Create a report that summarizes the performance over the monitoring period and provides recommendations for any identified issues.</description>
    <output>A performance monitoring dashboard and report.</output>
  </step>
</perf_monitor_workflow>
```

## Configuration

The `/perf monitor` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/perf monitor">
  <setting name="default_duration" value="1h" description="The default duration for performance monitoring." />
  <setting name="default_metrics" value="cpu,memory" description="The default metrics to collect." />
  <setting name="alert_threshold_cpu" value="80" description="The CPU usage threshold for alerting (in percent)." />
  <setting name="alert_threshold_memory" value="85" description="The memory usage threshold for alerting (in percent)." />
</command>
```

## Use Cases

*   **Production Monitoring**: Continuously monitor the performance of production systems to ensure reliability and performance.
*   **Load Testing Analysis**: Analyze the performance of an application under heavy load to identify bottlenecks and scaling issues.
*   **Proactive Maintenance**: Detect and address performance issues before they impact users.