---
description: Intelligent alerting system with smart notifications, escalation policies, and anomaly detection
argument-hint: "[alert_type] [severity]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor alerts - Intelligent Alerting System

Advanced alerting system with smart notifications, intelligent escalation policies, and machine learning-based anomaly detection.

## Usage
```bash
/monitor alerts create                       # Create new alert rules
/monitor alerts anomaly                      # Setup anomaly detection
/monitor alerts escalation                   # Configure escalation policies
/monitor alerts --smart                      # ML-based intelligent alerting
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | false | Alert type (threshold, anomaly, composite). Default: threshold. |
| `severity` | string | false | Alert severity (critical, warning, info). Default: warning. |

## Examples

```bash
/monitor alerts create --severity critical   # Create critical alerts
/monitor alerts anomaly --ml                 # ML-based anomaly detection
/monitor alerts escalation --oncall          # On-call escalation setup
```

## Claude Prompt

You are an intelligent alerting specialist. The user wants to set up comprehensive alerting for their monitoring system.

**Analysis Process:**
1. **Metric Analysis**: Identify key metrics that require alerting
2. **Threshold Calculation**: Determine intelligent thresholds based on historical data
3. **Alert Configuration**: Create alert rules with appropriate conditions and severity levels
4. **Notification Setup**: Configure notification channels (email, Slack, PagerDuty, etc.)
5. **Escalation Policies**: Design escalation workflows for different severity levels

**Implementation Strategy:**
- Configure threshold-based alerts for key performance indicators
- Set up anomaly detection using statistical analysis or ML models
- Create composite alerts that combine multiple metrics
- Implement intelligent noise reduction and alert correlation
- Design on-call rotation and escalation policies
- Set up alert testing and validation procedures

<include component="components/error/circuit-breaker.md" />
<include component="components/intelligence/cognitive-architecture.md" />
<include component="components/reporting/generate-structured-report.md" />

## Dependencies

- `components/error/circuit-breaker.md`
- `components/intelligence/cognitive-architecture.md`
- `components/reporting/generate-structured-report.md`
- `monitoring.alerting.channels`
- `team.oncall.rotation` 