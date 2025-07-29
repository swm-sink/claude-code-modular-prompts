---
name: /monitor
description: "Comprehensive monitoring system with setup, alerts, dashboards, status monitoring, and configuration management"
usage: "[subcommand] [options]"
tools: Read, Write, Edit, Bash, Grep
---
# /monitor - Comprehensive Monitoring System
Advanced monitoring system with intelligent alerting, comprehensive dashboards, predictive analytics, and unified management capabilities.

## Usage
```bash
# Setup subcommands
/monitor setup infrastructure               # Infrastructure monitoring setup
/monitor setup --comprehensive             # Comprehensive monitoring framework
/monitor setup --predictive                # Predictive analytics monitoring
/monitor setup --intelligent               # AI-powered monitoring system

# Alerts subcommands
/monitor alerts prometheus "severity='critical'"    # Monitor alerts from Prometheus
/monitor alerts --correlate "high_cpu_usage"       # Correlate alerts related to a specific issue
/monitor alerts --analyze "db_latency"             # Analyze the root cause of an alert
/monitor alerts --incident "create"                # Create a new incident from an alert

# Dashboard subcommands
/monitor dashboard create "My Dashboard"            # Create a new dashboard
/monitor dashboard --add-widget "cpu_usage"        # Add a widget to a dashboard
/monitor dashboard --import "grafana"              # Import a dashboard from Grafana
/monitor dashboard --share "team@example.com"      # Share a dashboard with others

# Status subcommands
/monitor status --overall                           # Show overall monitoring status
/monitor status --services                          # Show service monitoring status
/monitor status --alerts                            # Show current alert status

# Config subcommands
/monitor config --view                              # View current configuration
/monitor config --set "key=value"                  # Set configuration values
/monitor config --export                            # Export configuration
```

<command_file>
  <metadata>
    <name>/monitor</name>
    <purpose>Comprehensive monitoring system with setup, alerts, dashboards, status monitoring, and configuration management</purpose>
    <usage>
      <![CDATA[
      /monitor [subcommand] [options] [arguments]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="subcommand" type="string" required="true">
      <description>The monitoring subcommand to execute (setup, alerts, dashboard, status, config)</description>
    </argument>
    <argument name="options" type="string" required="false">
      <description>Subcommand-specific options and flags</description>
    </argument>
    <argument name="arguments" type="string" required="false">
      <description>Additional arguments for the subcommand</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Set up comprehensive monitoring infrastructure</description>
      <usage>/monitor setup --comprehensive</usage>
    </example>
    <example>
      <description>Monitor critical alerts from Prometheus</description>
      <usage>/monitor alerts prometheus "severity='critical'"</usage>
    </example>
    <example>
      <description>Create a new monitoring dashboard</description>
      <usage>/monitor dashboard create "Application Performance"</usage>
    </example>
    <example>
      <description>Check overall monitoring system status</description>
      <usage>/monitor status --overall</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are a comprehensive monitoring system specialist. The user wants to manage a complete monitoring infrastructure with setup, alerting, dashboards, status monitoring, and configuration.

**Subcommand Routing:**
Based on the first argument, route to the appropriate monitoring functionality:

## SETUP SUBCOMMAND
When subcommand is "setup":
**Setup Process:**
1. **Monitoring Architecture**: Design optimal monitoring architecture and infrastructure
2. **Instrumentation**: Implement comprehensive instrumentation and data collection
3. **Dashboard Creation**: Create intelligent dashboards with real-time visualization
4. **Alerting System**: Establish smart alerting with anomaly detection
5. **Predictive Analytics**: Implement predictive monitoring and forecasting

**Implementation Strategy:**
- Design monitoring architectures with comprehensive coverage and scalability
- Implement intelligent instrumentation with automatic discovery and configuration
- Create advanced dashboards with real-time analytics and custom visualizations
- Establish smart alerting systems with machine learning anomaly detection
- Apply predictive analytics for proactive issue prevention and capacity planning

## ALERTS SUBCOMMAND
When subcommand is "alerts":
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

## DASHBOARD SUBCOMMAND
When subcommand is "dashboard":
**Dashboard Process:**
1. **Requirement Analysis**: Understand the user's requirements for the dashboard
2. **Data Source Integration**: Integrate with the necessary data sources (e.g., Prometheus, CloudWatch, Loki)
3. **Widget Configuration**: Configure widgets with appropriate visualizations and queries
4. **Dashboard Layout**: Arrange widgets in a clear, intuitive, and aesthetically pleasing layout
5. **Sharing & Collaboration**: Enable sharing and collaboration features for the dashboard

**Implementation Strategy:**
- Provide a user-friendly interface for creating and customizing dashboards
- Integrate with a wide range of data sources to provide a unified view of the system
- Offer a rich library of customizable widgets with various visualization options
- Use a flexible grid-based layout system to allow users to arrange widgets as they see fit
- Implement robust sharing and collaboration features with access control and versioning

## STATUS SUBCOMMAND
When subcommand is "status":
**Status Monitoring Process:**
1. **System Health Check**: Perform comprehensive health checks across all monitoring components
2. **Service Status**: Monitor the status of all monitored services and applications
3. **Alert Status**: Show current alert states and their severity levels
4. **Performance Metrics**: Display key performance indicators and system metrics
5. **Resource Utilization**: Monitor resource usage and capacity planning

**Implementation Strategy:**
- Provide real-time status updates for all monitoring components
- Display service health with clear visual indicators and status summaries
- Show active alerts with priority and escalation information
- Present performance metrics in an easily digestible format
- Monitor resource utilization with capacity planning recommendations

## CONFIG SUBCOMMAND
When subcommand is "config":
**Configuration Management Process:**
1. **Configuration View**: Display current monitoring system configuration
2. **Setting Management**: Allow modification of monitoring system settings
3. **Configuration Export**: Export configuration for backup or migration
4. **Configuration Import**: Import configuration from backup or other systems
5. **Validation**: Validate configuration changes before applying

**Implementation Strategy:**
- Provide a hierarchical view of all configuration settings
- Allow secure modification of configuration with validation
- Support configuration backup and restore capabilities
- Enable configuration migration between environments
- Implement configuration validation and rollback capabilities

<include component="components/analytics/business-intelligence.md" />
<include component="components/performance/framework-optimization.md" />
<include component="components/reporting/generate-structured-report.md" />
<include component="components/analysis/dependency-mapping.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/performance/framework-optimization.md</component>
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/analysis/dependency-mapping.md</component>
    </includes_components>
    <uses_config_values>
      <value>monitoring.setup.auto_discovery</value>
      <value>analytics.predictive.enabled</value>
      <value>monitoring.alerts.correlation_engine</value>
      <value>incident_management.auto_create</value>
      <value>dashboard.default_data_source</value>
      <value>dashboard.sharing.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file>