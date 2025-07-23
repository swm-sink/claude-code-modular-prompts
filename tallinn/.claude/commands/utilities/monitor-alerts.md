---
name: /monitor-alerts
description: Intelligent alert monitoring with automated correlation, root cause analysis, and comprehensive incident management
usage: /monitor-alerts [alert_source] [analysis_level]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent alert monitoring with automated correlation, root cause analysis, and comprehensive incident management

**Usage**: `/monitor-alerts $ALERT_SOURCE $QUERY $ANALYSIS_LEVEL`

## Key Arguments

- **$ALERT_SOURCE** (required): The source of the alerts to monitor (e.g., prometheus, cloudwatch, datadog)
- **$QUERY** (required): A query to filter or analyze alerts
- **$ANALYSIS_LEVEL** (optional): Level of root cause analysis to perform

## Examples

```bash
/monitor alerts prometheus "severity='critical'"
```
*Monitor alerts from Prometheus*

```bash
/monitor alerts --correlate "high_cpu_usage"
```
*Correlate alerts related to a specific issue*

## Core Logic

You are an advanced alert monitoring specialist. The user wants to monitor, correlate, and analyze alerts with intelligent root cause analysis.

**Alert Monitoring Process:**
1. **Alert Aggregation**: Aggregate alerts from various sources
2. **Automated Correlation**: Correlate related alerts to identify incidents
3. **Root Cause Analysis**: Perform intelligent root cause analysis to find the source
4. **Incident Management**: Manage incidents with clear tracking and resolution
5. **Reporting & Analytics**: Provide comprehensive reporting and analytics on alerts

**Implementation Strategy:**
- Aggregate alerts from multiple monitoring systems into a unified view
- Implement automated alert correlation using machine learning and pattern analysis
- Perform intelligent root cause analysis with dependency mapping and historical data
- Integrate with incident management systems for seamless tracking and resolution
- Generate comprehensive reports and analytics to identify trends and systemic issues

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

