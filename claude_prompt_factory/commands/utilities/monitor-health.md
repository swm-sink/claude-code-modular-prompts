# /monitor health - System Health Status Command

## Purpose
Comprehensive system health monitoring with service availability tracking and resource health assessment.

## Usage
```bash
/monitor health [scope] [--format=summary|detailed|json] [--interval=30s]
```

## Core Health Checks

### 🔋 System Resources
- **CPU utilization**: Load average, process health, thermal status
- **Memory usage**: Available RAM, swap usage, memory leaks detection
- **Disk health**: Space utilization, I/O performance, SMART status
- **Network connectivity**: Latency, bandwidth, connection pools

### 🚀 Service Availability
- **Application services**: Response time, error rates, uptime status
- **Database connections**: Query performance, connection pools, replication lag
- **External dependencies**: API endpoints, third-party services, CDN status
- **Background jobs**: Queue depth, processing rates, failed job counts

### 📊 Health Metrics
- **Response times**: P50, P95, P99 latencies across services
- **Error rates**: 4xx/5xx errors, timeout frequencies, failure patterns
- **Resource trends**: Historical usage patterns, capacity planning alerts
- **Dependency status**: Circuit breaker states, fallback activations

### 🚨 Health Assessment
- **Status levels**: Healthy, Degraded, Critical, Down
- **Root cause analysis**: Automated issue correlation and impact mapping
- **Recovery actions**: Self-healing triggers, escalation procedures
- **Capacity alerts**: Threshold breaches, predictive scaling triggers

## Health Report Output
- **Overall system status** (color-coded health indicators)
- **Service dependency map** (visual health topology)
- **Resource utilization trends** (historical and predictive analysis)
- **Actionable recommendations** (optimization and remediation steps)

## Integration Points
- Monitoring systems (Prometheus, Grafana, DataDog)
- Health check endpoints (application /health routes)
- Infrastructure monitoring (AWS CloudWatch, system metrics)
- Incident response workflows (PagerDuty, Slack notifications)