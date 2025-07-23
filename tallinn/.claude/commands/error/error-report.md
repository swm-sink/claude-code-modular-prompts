---
name: /error-report
description: Comprehensive error reporting with metrics, trend analysis, and actionable insights
usage: /error-report [report_type] [time_period]
tools: Read, Write, Edit, Bash, Grep
---

# Comprehensive error reporting with metrics, trend analysis, and actionable insights

**Usage**: `/error-report $REPORT_TYPE $TIME_PERIOD`

## Key Arguments

- **$REPORT_TYPE** (optional): The type of error report to generate (e.g., summary, trends, critical)
- **$TIME_PERIOD** (optional): The time window for the report (e.g., '24h', '7d', '30d')

## Examples

```bash
/error report summary --period 7d
```
*Generate a summary error report for the last week*

```bash
/error report trends --period week
```
*Analyze weekly error trends*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/analytics/business-intelligence.md
 components/reporting/generate-structured-report.md
 components/analysis/trend-analysis.md
 components/visualization/performance-charts.md
 components/analytics/data-aggregation.md
 
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

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

