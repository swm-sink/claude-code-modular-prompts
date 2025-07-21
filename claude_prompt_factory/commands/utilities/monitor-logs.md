---
description: Intelligent log monitoring with automated parsing, anomaly detection, and comprehensive analysis
argument-hint: "[log_source] [analysis_type]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor logs - Intelligent Log Monitoring

Advanced log monitoring system with automated parsing, intelligent anomaly detection, and comprehensive analysis capabilities.

## Usage
```bash
/monitor logs /var/log/app.log             # Monitor a specific log file
/monitor logs --stream "kubernetes_pod"    # Stream logs from a Kubernetes pod
/monitor logs --analyze "error_patterns"   # Analyze logs for error patterns
/monitor logs --anomaly-detection "true"   # Enable real-time anomaly detection
```

<command_file>
  <metadata>
    <n>/monitor logs</n>
    <purpose>Intelligent log monitoring with automated parsing, anomaly detection, and comprehensive analysis</purpose>
    <usage>
      <![CDATA[
      /monitor logs [log_source] "[query]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="log_source" type="string" required="true" default="file">
      <description>The source of the logs to monitor (e.g., file, stream, service)</description>
    </argument>
    <argument name="query" type="string" required="true">
      <description>A query to filter or analyze the logs</description>
    </argument>
    <argument name="analysis_type" type="string" required="false" default="anomaly_detection">
      <description>The type of analysis to perform on the logs</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Monitor a specific log file</description>
      <usage>/monitor logs file "/var/log/syslog"</usage>
    </example>
    <example>
      <description>Stream logs from a Kubernetes pod</description>
      <usage>/monitor logs --stream "my_pod_name"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced log monitoring specialist. The user wants to monitor, parse, and analyze logs with intelligent anomaly detection.

**Log Monitoring Process:**
1. **Log Ingestion**: Ingest logs from various sources (files, streams, services)
2. **Automated Parsing**: Automatically parse logs into a structured format
3. **Real-time Analysis**: Perform real-time analysis for patterns and anomalies
4. **Anomaly Detection**: Use machine learning to detect anomalies and outliers
5. **Reporting & Visualization**: Provide comprehensive reporting and visualization of log data

**Implementation Strategy:**
- Ingest logs from multiple sources with robust and scalable pipelines
- Implement automated log parsing for various formats (e.g., JSON, syslog, custom)
- Perform real-time analysis using powerful query languages and search capabilities
- Apply machine learning models for intelligent anomaly detection and pattern recognition
- Generate insightful reports and visualizations to help users understand their log data

<include component="components/analytics/business-intelligence.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>monitoring.logs.parser</value>
      <value>anomaly_detection.sensitivity</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Log Levels
- **error** - Error and exception tracking
- **warn** - Warning and performance issues
- **info** - General application events
- **debug** - Detailed diagnostic information
- **trace** - Full execution tracing

## Source Types
- **app** - Application logs
- **system** - System and infrastructure logs
- **access** - HTTP/API access logs
- **security** - Security and audit logs
- **all** - All log sources (default)

## Analysis Features
### Pattern Detection
- Error clustering and frequency analysis
- Performance degradation patterns
- Security threat indicators
- Anomaly detection algorithms

### Log Aggregation
- Multi-source log correlation
- Time-series trend analysis
- User journey reconstruction
- Service dependency mapping

### Search Capabilities
- Full-text search with regex support
- Structured query language
- Time-range filtering
- Multi-dimensional pivoting

## Output Formats
- **stream** - Real-time log streaming
- **summary** - Aggregated insights report
- **alerts** - Critical issue notifications
- **export** - Structured data export

## Examples
```bash
/monitor logs error app          # Application errors
/monitor logs warn --last 1h     # Recent warnings
/monitor logs all --pattern "timeout"    # Timeout events
/monitor logs debug --follow     # Live debugging
```

## Integration
- Real-time alerting system
- Dashboard visualization
- Incident response automation
- Log retention policies