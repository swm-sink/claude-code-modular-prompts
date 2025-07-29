---
description: Real-time performance monitoring with alerting and automated issue detection
argument-hint: "[monitor_type] [alert_threshold]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /perf monitor - Performance Monitoring System

Real-time performance monitoring with intelligent alerting, anomaly detection, and automated diagnostics.

## Usage
```bash
/perf monitor start                  # Start performance monitoring
/perf monitor cpu --threshold 80    # Monitor CPU with 80% alert threshold
/perf monitor memory --auto-alert   # Monitor memory with automatic alerting
```

<command_file>
  <metadata>
    <name>/perf monitor</name>
    <purpose>Sets up continuous performance monitoring with real-time metrics, trend analysis, and alerting.</purpose>
    <usage>
      <![CDATA[
      /perf monitor <duration="1h">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="duration" type="string" required="false" default="1h">
      <description>The duration for the monitoring session (e.g., '10m', '1h', '6h').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Monitor the application's performance for one hour.</description>
      <usage>/perf monitor</usage>
    </example>
    <example>
      <description>Run a short 10-minute monitoring session.</description>
      <usage>/perf monitor duration="10m"</usage>
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
      <include>components/monitoring/real-time-monitoring.md</include>
      <include>components/monitoring/alerting-systems.md</include>
      <include>components/analysis/anomaly-detection.md</include>
      <include>components/visualization/performance-dashboards.md</include>
      
      You are a site reliability engineer. The user wants to set up performance monitoring.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured monitoring service integration (e.g., Prometheus, Datadog) and alerting thresholds.
      2.  **Generate Setup Plan**:
          *   Propose a plan to configure and start a monitoring session for the specified `duration`.
          *   The plan should include collecting key metrics (CPU, memory, I/O, latency).
          *   It should also include setting up alerts based on the configured thresholds.
      3.  **Provide Dashboard/Query**:
          *   Generate the configuration or query needed for the monitoring service to display a real-time performance dashboard.
      4.  **Generate Report**:
          *   After the monitoring session, provide a summary report of the performance, highlighting any anomalies or threshold breaches.
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>monitoring.performance_monitoring_service</value>
      <value>monitoring.alerting.cpu_threshold</value>
      <value>monitoring.alerting.memory_threshold</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>