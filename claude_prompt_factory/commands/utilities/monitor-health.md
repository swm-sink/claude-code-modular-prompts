---
description: Advanced health monitoring with intelligent diagnostics, predictive analysis, and comprehensive system wellness tracking
argument-hint: "[health_scope] [diagnostic_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor health - Advanced Health Monitoring

Sophisticated health monitoring system with intelligent diagnostics, predictive analysis, and comprehensive system wellness tracking.

## Usage
```bash
/monitor health system                       # System health monitoring
/monitor health --comprehensive              # Comprehensive health analysis
/monitor health --predictive                 # Predictive health monitoring
/monitor health --intelligent                # AI-powered health diagnostics
```

<command_file>
  <metadata>
    <n>/monitor health</n>
    <purpose>Advanced health monitoring with intelligent diagnostics, predictive analysis, and comprehensive system wellness tracking</purpose>
    <usage>
      <![CDATA[
      /monitor health [health_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="health_scope" type="string" required="false" default="system">
      <description>Scope of health monitoring to implement</description>
    </argument>
    <argument name="diagnostic_level" type="string" required="false" default="comprehensive">
      <description>Level of diagnostic analysis and intelligence</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>System health monitoring</description>
      <usage>/monitor health system</usage>
    </example>
    <example>
      <description>Comprehensive health analysis</description>
      <usage>/monitor health --comprehensive</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced health monitoring specialist. The user wants to implement intelligent diagnostics with predictive analysis and comprehensive wellness tracking.

**Health Monitoring Process:**
1. **Health Assessment**: Assess current system health and identify metrics
2. **Diagnostic Implementation**: Implement intelligent diagnostic systems
3. **Predictive Analysis**: Apply predictive health analysis and forecasting
4. **Wellness Tracking**: Create comprehensive wellness tracking and reporting
5. **Proactive Response**: Establish proactive health response and remediation

**Implementation Strategy:**
- Assess system health using comprehensive metrics and key performance indicators
- Implement intelligent diagnostic systems with anomaly detection and pattern analysis
- Apply predictive health analysis with machine learning forecasting models
- Create comprehensive wellness dashboards with real-time health visualization
- Establish proactive response systems with automated remediation and alerting

<include component="components/analytics/business-intelligence.md" />
<include component="components/reliability/chaos-engineering.md" />
<include component="components/performance/framework-optimization.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reliability/chaos-engineering.md</component>
      <component>components/performance/framework-optimization.md</component>
    </includes_components>
    <uses_config_values>
      <value>health_monitoring.predictive.enabled</value>
      <value>diagnostics.intelligence.level</value>
    </uses_config_values>
  </dependencies>
</command_file>

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