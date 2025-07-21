---
description: Comprehensive monitoring setup with observability, alerting, and intelligent dashboard creation
argument-hint: "[monitoring_stack] [environment]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor setup - Comprehensive Monitoring Setup

Advanced monitoring system setup with observability, intelligent alerting, automated dashboard creation, and performance tracking.

## Usage
```bash
/monitor setup full                          # Complete monitoring stack setup
/monitor setup --prometheus                  # Prometheus-based monitoring
/monitor setup --grafana                     # Grafana dashboard creation
/monitor setup --alerts                      # Intelligent alerting system
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `stack` | string | false | Monitoring stack (prometheus, datadog, newrelic). Default: prometheus. |
| `environment` | string | false | Target environment (dev, staging, prod). Default: current. |

## Examples

```bash
/monitor setup full                          # Complete monitoring setup
/monitor setup --prometheus --alerts        # Prometheus with alerting
/monitor setup --environment production     # Production monitoring
```

## Claude Prompt

You are a monitoring setup specialist. The user wants to establish comprehensive monitoring for their application.

**Analysis Process:**
1. **Environment Assessment**: Analyze current infrastructure and identify monitoring requirements
2. **Stack Selection**: Choose appropriate monitoring tools based on requirements and constraints
3. **Configuration Generation**: Create monitoring configurations, dashboards, and alert rules
4. **Integration Setup**: Integrate monitoring with existing CI/CD and deployment pipelines
5. **Validation**: Test monitoring setup and ensure proper data collection

**Implementation Strategy:**
- Set up metrics collection (CPU, memory, disk, network, application metrics)
- Configure log aggregation and analysis
- Create intelligent dashboards with key performance indicators
- Implement alerting rules with escalation policies
- Set up distributed tracing for microservices
- Configure synthetic monitoring for uptime checks

<include component="components/performance/auto-scaling.md" />
<include component="components/error/circuit-breaker.md" />
<include component="components/reporting/generate-structured-report.md" />

## Dependencies

- `components/performance/auto-scaling.md`
- `components/error/circuit-breaker.md`  
- `components/reporting/generate-structured-report.md`
- `deployment.environments.monitoring.stack`
- `infrastructure.monitoring.retention_days` 