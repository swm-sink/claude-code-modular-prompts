---
name: /monitor-logs
description: Intelligent log monitoring with automated parsing, anomaly detection, and comprehensive analysis
usage: /monitor-logs [log_source] [analysis_type]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent log monitoring with automated parsing, anomaly detection, and comprehensive analysis

**Usage**: `/monitor-logs $LOG_SOURCE $QUERY $ANALYSIS_TYPE`

## Key Arguments

- **$LOG_SOURCE** (required): The source of the logs to monitor (e.g., file, stream, service)
- **$QUERY** (required): A query to filter or analyze the logs
- **$ANALYSIS_TYPE** (optional): The type of analysis to perform on the logs

## Examples

```bash
/monitor logs file "/var/log/syslog"
```
*Monitor a specific log file*

```bash
/monitor logs --stream "my_pod_name"
```
*Stream logs from a Kubernetes pod*

## Core Logic

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

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

