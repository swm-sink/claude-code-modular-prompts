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

## Arguments

```yaml
timeframe:
  type: string
  description: The time window for the report (e.g., '24h', '7d', '30d').
  default: 7d
```

## Examples

```yaml
timeframe:
  type: string
  description: The time window for the report (e.g., '24h', '7d', '30d').
  default: 7d
```

## Dependencies

```yaml
monitoring.logging_service:
  type: string
  description: The service responsible for collecting application logs.
monitoring.error_tracking_service:
  type: string
  description: The service responsible for tracking and analyzing application errors.
```

<include component="components/analytics/business-intelligence.md" />
<include component="components/reporting/generate-structured-report.md" />
<include component="components/context/adaptive-thinking.md" />
<include component="components/interaction/progress-reporting.md" />