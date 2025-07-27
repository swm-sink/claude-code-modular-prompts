---
name: /monitor-setup
description: Advanced monitoring setup with intelligent alerting, comprehensive dashboards, and predictive analytics
argument-hint: "[monitoring_scope] [analytics_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation:
  reason: "Duplicate functionality - consolidated in main /monitor command"
  replacement: "/monitor setup"
  deadline: "2025-08-25"
  status: "deprecated"
---
# /monitor setup - Advanced Monitoring Setup

⚠️ **DEPRECATED COMMAND** ⚠️

This command is deprecated and will be removed on **2025-08-25**.

**Reason**: Duplicate functionality - consolidated in main /monitor command  
**Replacement**: Use `/monitor setup` instead  
**Migration**: This functionality is now available through the main `/monitor` command

---

Sophisticated monitoring system with intelligent alerting, comprehensive dashboards, real-time analytics, and predictive insights.
## Usage
```bash
/monitor setup infrastructure               # Infrastructure monitoring setup
/monitor setup --comprehensive              # Comprehensive monitoring framework
/monitor setup --predictive                 # Predictive analytics monitoring
/monitor setup --intelligent                # AI-powered monitoring system
```
<command_file>
  <metadata>
    <n>/monitor setup</n>
    <purpose>Advanced monitoring setup with intelligent alerting, comprehensive dashboards, and predictive analytics</purpose>
    <usage>
      <![CDATA[
      /monitor setup [monitoring_scope] --analytics [analytics_level]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="monitoring_scope" type="string" required="false" default="infrastructure">
      <description>Scope of monitoring system to set up</description>
    </argument>
    <argument name="analytics_level" type="string" required="false" default="comprehensive">
      <description>Level of analytics and intelligence to implement</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Infrastructure monitoring setup</description>
      <usage>/monitor setup infrastructure</usage>
    </example>
    <example>
      <description>Comprehensive monitoring framework</description>
      <usage>/monitor setup --comprehensive</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced monitoring setup specialist. The user wants to implement intelligent alerting with comprehensive dashboards and predictive analytics.
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
<include component="components/analytics/business-intelligence.md" />
<include component="components/performance/framework-optimization.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/performance/framework-optimization.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>monitoring.setup.auto_discovery</value>
      <value>analytics.predictive.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file> 