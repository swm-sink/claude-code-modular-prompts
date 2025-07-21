---
description: Intelligent monitoring dashboards with automated visualization, customizable widgets, and comprehensive data integration
argument-hint: "[dashboard_type] [data_source]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor dashboard - Intelligent Monitoring Dashboards

Advanced monitoring dashboard system with automated visualization, highly customizable widgets, and comprehensive integration with various data sources.

## Usage
```bash
/monitor dashboard create "My Dashboard"     # Create a new dashboard
/monitor dashboard --add-widget "cpu_usage"  # Add a widget to a dashboard
/monitor dashboard --import "grafana"      # Import a dashboard from Grafana
/monitor dashboard --share "team@example.com" # Share a dashboard with others
```

<command_file>
  <metadata>
    <n>/monitor dashboard</n>
    <purpose>Intelligent monitoring dashboards with automated visualization, customizable widgets, and comprehensive data integration</purpose>
    <usage>
      <![CDATA[
      /monitor dashboard [action] "[name]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="action" type="string" required="true" default="create">
      <description>The action to perform on the dashboard (e.g., create, add-widget, import, share)</description>
    </argument>
    <argument name="name" type="string" required="true">
      <description>The name of the dashboard or widget</description>
    </argument>
    <argument name="data_source" type="string" required="false" default="prometheus">
      <description>The data source for the dashboard or widget</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Create a new dashboard</description>
      <usage>/monitor dashboard create "My Application Dashboard"</usage>
    </example>
    <example>
      <description>Add a widget to a dashboard</description>
      <usage>/monitor dashboard --add-widget "cpu_usage --dashboard My_Dashboard"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced monitoring dashboard specialist. The user wants to create, customize, and manage monitoring dashboards.

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

<include component="components/analytics/business-intelligence.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>dashboard.default_data_source</value>
      <value>dashboard.sharing.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Implementation
```yaml
dashboard_types:
  system:
    panels: [cpu, memory, disk, network]
    refresh: 30s
    alerts: critical_only
  
  application:
    panels: [requests, errors, latency, throughput]
    refresh: 10s
    alerts: all_levels
  
  infrastructure:
    panels: [services, containers, databases, queues]
    refresh: 60s
    alerts: availability

visualization:
  charts: [line, bar, gauge, heatmap]
  time_range: [1h, 24h, 7d, 30d]
  drill_down: enabled
```

## Features
- Real-time metrics display
- Interactive charts and graphs
- Alert status indicators
- Historical trend analysis
- Custom panel configuration
- Export and sharing options
- Mobile-responsive layout

## Output
Generates HTML dashboard with live data feeds and visualization components.