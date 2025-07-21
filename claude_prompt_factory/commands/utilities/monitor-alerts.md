---
description: Intelligent alert monitoring with automated correlation, root cause analysis, and comprehensive incident management
argument-hint: "[alert_source] [analysis_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor alerts - Intelligent Alert Monitoring

Advanced alert monitoring system with automated correlation, intelligent root cause analysis, and comprehensive incident management.

## Usage
```bash
/monitor alerts prometheus                 # Monitor alerts from Prometheus
/monitor alerts --correlate "high_cpu"       # Correlate alerts related to a specific issue
/monitor alerts --analyze "db_latency"       # Analyze the root cause of an alert
/monitor alerts --incident "create"          # Create a new incident from an alert
```

<command_file>
  <metadata>
    <n>/monitor alerts</n>
    <purpose>Intelligent alert monitoring with automated correlation, root cause analysis, and comprehensive incident management</purpose>
    <usage>
      <![CDATA[
      /monitor alerts [alert_source] "[query]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="alert_source" type="string" required="true" default="prometheus">
      <description>The source of the alerts to monitor (e.g., prometheus, cloudwatch, datadog)</description>
    </argument>
    <argument name="query" type="string" required="true">
      <description>A query to filter or analyze alerts</description>
    </argument>
    <argument name="analysis_level" type="string" required="false" default="high">
      <description>Level of root cause analysis to perform</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Monitor alerts from Prometheus</description>
      <usage>/monitor alerts prometheus "severity='critical'"</usage>
    </example>
    <example>
      <description>Correlate alerts related to a specific issue</description>
      <usage>/monitor alerts --correlate "high_cpu_usage"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
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

<include component="components/analysis/dependency-mapping.md" />
<include component="components/analytics/business-intelligence.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>monitoring.alerts.correlation_engine</value>
      <value>incident_management.auto_create</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Core Alert Management

### 🚨 Alert Configuration
- **Threshold rules**: CPU, memory, disk, network capacity limits
- **Performance alerts**: Response time, error rate, throughput degradation
- **Business metrics**: SLA violations, conversion rate drops, revenue impact
- **Security alerts**: Failed logins, suspicious activity, policy violations

### 📊 Alert Rules Engine
- **Dynamic thresholds**: ML-based anomaly detection and adaptive baselines
- **Composite conditions**: Multi-metric correlation and dependency logic
- **Time-based rules**: Business hours vs. off-hours alert sensitivity
- **Escalation policies**: Notification hierarchy and timeout handling

### 🔧 Alert Tuning
- **Noise reduction**: Flapping detection, duplicate suppression, smart grouping
- **Sensitivity adjustment**: False positive reduction, alert fatigue prevention
- **Correlation analysis**: Root cause identification, related alert grouping
- **Feedback loops**: Alert effectiveness scoring, auto-tuning based on resolution

### 📱 Notification Management
- **Multi-channel delivery**: Email, SMS, Slack, PagerDuty, webhook integration
- **Escalation ladders**: Primary → Secondary → Manager notification chains
- **Acknowledgment tracking**: Response times, resolution status, follow-up actions
- **Alert history**: Pattern analysis, recurring issue identification, trend reporting

## Alert Lifecycle
- **Detection** (automated monitoring and threshold evaluation)
- **Notification** (immediate stakeholder alerting via configured channels)
- **Acknowledgment** (incident ownership and response initiation)
- **Investigation** (root cause analysis and impact assessment)
- **Resolution** (problem remediation and service restoration)
- **Post-mortem** (lessons learned and prevention strategy updates)

## Integration Points
- Monitoring systems (Prometheus, Grafana, DataDog, New Relic)
- Incident management (PagerDuty, OpsGenie, VictorOps)
- Communication platforms (Slack, Teams, Discord webhooks)
- ITSM tools (ServiceNow, Jira Service Desk, Zendesk)