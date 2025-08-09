---
name: agent-status
description: Monitor specialized agent performance, health, and resource utilization dashboard
usage: "agent-status [agent-name|all] [--format=dashboard|detailed|json] [--metrics=performance|health|usage]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS]
category: agents
argument-hint: "[agent-name|all] [--display-options]"
version: "1.0"
---

# Agent Status: Real-Time Agent Performance Dashboard

## Purpose: Comprehensive Agent Health and Performance Monitoring

The `/agent-status` command provides a real-time dashboard showing the health, performance, and utilization of your specialized agent team. This enables proactive monitoring, performance optimization, and early detection of issues that could impact agent effectiveness.

**Agent Status Philosophy**: Transparent performance visibility, predictive health monitoring, actionable performance insights, proactive issue detection, data-driven optimization guidance.

## 🎯 Real-Time Agent Monitoring Dashboard

### Multi-Dimensional Status Overview
- **Performance Metrics**: Real-time accuracy, response time, and quality measurements
- **Health Indicators**: Agent availability, context currency, and operational status
- **Usage Analytics**: Utilization patterns, task distribution, and collaboration frequency
- **Resource Monitoring**: Memory usage, response caching, and system resource consumption

### Predictive Health Monitoring
- **Trend Analysis**: Performance trend detection and degradation prediction
- **Alert Systems**: Proactive notifications for performance issues and maintenance needs
- **Capacity Planning**: Usage forecasting and resource requirement predictions
- **Quality Assurance**: Continuous validation of agent effectiveness and reliability

## 📊 Agent Status Dashboard

### Executive Summary View
```bash
/agent-status all --format=dashboard
```

```
═══════════════════════════════════════════════════════════════════════════════
                        SPECIALIZED AGENT STATUS DASHBOARD
═══════════════════════════════════════════════════════════════════════════════

🚀 SYSTEM OVERVIEW
   Active Agents: 8/14        Overall Health: EXCELLENT (98.2%)
   Total Queries: 1,247       Avg Response Time: 1.8s
   Success Rate: 96.4%        Last Update: 2 hours ago

┌─────────────────────┬──────────┬─────────────┬──────────────┬─────────────────┐
│ Agent               │ Status   │ Health      │ Performance  │ Last Activity   │
├─────────────────────┼──────────┼─────────────┼──────────────┼─────────────────┤
│ 🏗️  Architecture    │ ACTIVE   │ EXCELLENT   │ 98.1% ⚡     │ 14 minutes ago  │
│ ⚙️  Code Generation │ ACTIVE   │ GOOD        │ 94.7% ⚡     │ 6 minutes ago   │
│ 🧪 Testing         │ ACTIVE   │ EXCELLENT   │ 97.8% ⚡     │ 3 minutes ago   │
│ 🔍 Debugging       │ ACTIVE   │ GOOD        │ 93.2% ⚠️     │ 28 minutes ago  │
│ 📝 Documentation   │ ACTIVE   │ EXCELLENT   │ 96.5% ⚡     │ 45 minutes ago  │
│ 👥 Review          │ ACTIVE   │ GOOD        │ 95.1% ⚡     │ 12 minutes ago  │
│ 🏢 Domain Expert   │ ACTIVE   │ EXCELLENT   │ 98.7% ⚡     │ 8 minutes ago   │
│ ⚡ Performance     │ INACTIVE │ MAINTENANCE │ N/A          │ 2 days ago      │
│ 🛡️  Security       │ INACTIVE │ READY       │ N/A          │ Never activated │
│ 🔗 Integration     │ INACTIVE │ READY       │ N/A          │ 1 week ago      │
│ ♻️  Refactoring    │ INACTIVE │ READY       │ N/A          │ 3 days ago      │
│ 🔄 Migration       │ INACTIVE │ READY       │ N/A          │ Never activated │
│ 🚀 DevOps          │ INACTIVE │ READY       │ N/A          │ 1 week ago      │
│ 📊 Data            │ INACTIVE │ READY       │ N/A          │ 2 weeks ago     │
└─────────────────────┴──────────┴─────────────┴──────────────┴─────────────────┘

⚠️  ALERTS & RECOMMENDATIONS
  • Debugging Agent showing performance decline (93.2%) - Consider update
  • Performance Agent in maintenance mode - Check update status
  • Consider activating Security Agent for production readiness review
  • High usage on Architecture Agent - Monitor for capacity issues

📈 PERFORMANCE TRENDS (7 days)
  • Overall Success Rate: ↗️ +2.3% (week over week)
  • Average Response Time: ↘️ -0.4s (improved)
  • User Satisfaction: ↗️ +0.3 points (4.7/5.0 average)
```

### Detailed Agent Status View
```bash
/agent-status architecture --format=detailed
```

```
═══════════════════════════════════════════════════════════════════════════════
                        🏗️ ARCHITECTURE AGENT - DETAILED STATUS
═══════════════════════════════════════════════════════════════════════════════

📊 PERFORMANCE METRICS (Last 7 Days)
┌─────────────────────────────────┬─────────────┬──────────────┬──────────────┐
│ Metric                          │ Current     │ 7-Day Avg   │ Trend        │
├─────────────────────────────────┼─────────────┼──────────────┼──────────────┤
│ Response Accuracy               │ 98.1%       │ 97.4%       │ ↗️ +0.7%     │
│ Response Time (avg)             │ 1.3s        │ 1.5s        │ ↘️ -0.2s     │
│ Context Relevance              │ 96.8%       │ 95.9%       │ ↗️ +0.9%     │
│ User Satisfaction              │ 4.8/5.0     │ 4.6/5.0     │ ↗️ +0.2      │
│ Specialization Compliance      │ 100.0%      │ 100.0%      │ → Stable    │
└─────────────────────────────────┴─────────────┴──────────────┴──────────────┘

🎯 USAGE ANALYTICS
  Total Queries: 342 (↗️ +23% vs last week)
  Peak Usage: 2-4 PM weekdays
  Most Common Tasks:
    • System design consultation (34%)
    • Framework decision guidance (28%)
    • Performance architecture review (22%)
    • Integration pattern recommendations (16%)

🏥 HEALTH INDICATORS
  ✅ Context Currency: CURRENT (last updated 2 hours ago)
  ✅ Response Quality: EXCELLENT (>95% success rate)
  ✅ Resource Usage: NORMAL (12% of available capacity)
  ✅ Integration Status: ACTIVE (collaborates with 6 other agents)
  ⚠️  Knowledge Staleness: MINOR (3 days since project analysis)

📈 PERFORMANCE TRENDS
  30-Day Success Rate: 97.8% ↗️ (+1.2%)
  Response Time Evolution: Improving (-0.3s average)
  User Satisfaction Trend: Increasing (+0.4 points)
  
🔧 RECENT ACTIVITIES (Last 24 Hours)
  14:32 - System design consultation for microservices architecture
  14:18 - Framework comparison analysis (React vs Vue)
  13:45 - Performance trade-off analysis for caching strategy
  13:12 - Integration pattern recommendation for payment gateway
  12:58 - Code review for architectural compliance

💡 OPTIMIZATION RECOMMENDATIONS
  • Consider knowledge refresh - project patterns may have evolved
  • Performance is excellent, maintain current configuration
  • High usage indicates successful specialization
  • Monitor for capacity issues during peak hours
```

## 🔍 Performance Monitoring Systems

### Real-Time Performance Metrics
```bash
/agent-status all --metrics=performance --real-time
```

**Core Performance Indicators**:
- **Response Accuracy**: Percentage of correct and useful responses (target: >95%)
- **Response Time**: Average time to provide meaningful guidance (target: <2s)
- **Context Relevance**: How well responses match current project context (target: >90%)
- **Task Completion Rate**: Percentage of successfully completed task requests (target: >90%)
- **User Satisfaction**: Average user rating for agent contributions (target: >4.0/5.0)

### Advanced Analytics Dashboard
```bash
/agent-status all --metrics=usage --analytics=advanced
```

**Usage Pattern Analysis**:
- **Query Distribution**: Types of tasks handled by each agent
- **Temporal Patterns**: Peak usage times and seasonal variations  
- **Collaboration Networks**: How agents work together and hand off tasks
- **Efficiency Metrics**: Tasks completed per unit time and resource usage

### Health Monitoring System
```bash
/agent-status all --metrics=health --predictive-analysis
```

**Health Assessment Dimensions**:
- **Context Currency**: How current agent knowledge is relative to project state
- **Response Quality Stability**: Consistency of high-quality responses over time
- **Resource Utilization**: Memory, processing, and system resource usage
- **Integration Health**: Effectiveness of collaboration with other agents

## 🚨 Alert and Notification System

### Performance Degradation Alerts
```bash
/agent-status --alerts=performance --thresholds="accuracy<95%,response-time>3s"
```

**Alert Categories**:
- **🔴 CRITICAL**: Agent performance below minimum thresholds
- **🟡 WARNING**: Declining performance trends requiring attention
- **🔵 INFO**: Optimization opportunities and maintenance recommendations
- **🟢 SUCCESS**: Performance improvements and achievement milestones

### Predictive Maintenance Notifications
```bash
/agent-status --predictive --maintenance-alerts=enabled
```

**Predictive Indicators**:
- **Knowledge Staleness**: When agent knowledge becomes outdated
- **Performance Drift**: Gradual decline in response quality or speed
- **Capacity Issues**: Approaching resource limits or usage thresholds
- **Integration Problems**: Degrading collaboration with other agents

### Custom Alert Configuration
```bash
/agent-status --configure-alerts --agent=testing --custom-thresholds
```

**Configurable Alert Parameters**:
- **Performance Thresholds**: Custom success rate and response time limits
- **Usage Patterns**: Alert on unusual activity or absence of expected usage
- **Health Indicators**: Notifications for specific health metric changes
- **Integration Monitoring**: Alerts for collaboration effectiveness changes

## 📈 Trend Analysis and Forecasting

### Performance Trend Dashboard
```bash
/agent-status all --trends=30-days --forecast=performance
```

**Trend Visualization**:
```
Architecture Agent Performance Trends (30 Days)
Response Accuracy:     ████████████████████▲ 98.1% (↗️ +2.1%)
Response Time:         ████████████████████▼ 1.3s  (↘️ -0.4s)
User Satisfaction:     █████████████████████ 4.8/5 (↗️ +0.3)

Performance Forecast (Next 30 Days):
• Expected accuracy: 98.5% ± 0.3% (stable/improving)
• Predicted response time: 1.2s ± 0.2s (improving)
• Forecasted satisfaction: 4.9/5 ± 0.1 (improving)
```

### Capacity Planning Analytics
```bash
/agent-status --capacity-analysis --planning-horizon=90-days
```

**Capacity Insights**:
- **Usage Growth Projections**: Predicted increase in agent utilization
- **Resource Requirements**: Future hardware and system resource needs
- **Scaling Recommendations**: When to consider agent optimization or distribution
- **Performance Impact**: How usage growth may affect response quality

### Historical Performance Analysis
```bash
/agent-status architecture --history=6-months --comparative-analysis
```

**Historical Analysis Features**:
- **Performance Evolution**: How agent capabilities have improved over time
- **Usage Pattern Changes**: Evolution of task types and usage frequency
- **Effectiveness Improvements**: Measured improvements in problem resolution
- **User Satisfaction Trends**: Long-term user experience and satisfaction changes

## 🎛️ Status Customization and Views

### Customizable Dashboard Views
```bash
/agent-status --create-view="development-focus" --agents="architecture,testing,code-gen,review"
/agent-status --create-view="production-ops" --agents="devops,performance,security,monitoring"
```

**Custom View Features**:
- **Role-Based Dashboards**: Different views for developers, DevOps, and managers
- **Project Phase Views**: Status displays optimized for development phases
- **Priority-Based Filtering**: Show only agents relevant to current work focus
- **Team Collaboration Views**: Status information optimized for team coordination

### Export and Integration Options
```bash
/agent-status all --export=json --integration=slack,email,dashboard
```

**Integration Capabilities**:
- **JSON Export**: Structured data export for custom dashboards and analysis
- **Slack Integration**: Real-time status updates and alerts in team channels  
- **Email Reports**: Scheduled status reports and performance summaries
- **API Endpoints**: Programmatic access to status data for custom integrations

### Mobile and Remote Access
```bash
/agent-status --mobile-view --simplified-metrics --critical-alerts-only
```

**Remote Monitoring Features**:
- **Mobile-Optimized Views**: Status information formatted for mobile devices
- **Critical Alert Focus**: Show only the most important status information
- **Offline Status Caching**: Basic status information available without connectivity
- **Push Notifications**: Critical alerts delivered to mobile devices

## ⚡ Usage Examples

### Daily Status Check
```bash
# Quick overview of all agents
/agent-status all --format=dashboard

# Detailed review of active agents
/agent-status --active-only --format=detailed
```

### Performance Monitoring
```bash
# Real-time performance tracking
/agent-status all --metrics=performance --live-updates

# Performance comparison over time
/agent-status architecture testing --trends=7-days --compare
```

### Health and Maintenance
```bash
# Comprehensive health assessment
/agent-status all --health-check --maintenance-recommendations

# Alert configuration and monitoring
/agent-status --setup-alerts --performance-monitoring=enabled
```

### Team and Project Views
```bash
# Development team dashboard
/agent-status --view=development --active-only

# Production readiness status
/agent-status security devops performance --production-check
```

## 🔗 Integration with Agent Management Ecosystem

### Seamless Command Integration
- **Performance-Based Recommendations**: Links to `/activate-agent` for underutilized capabilities
- **Maintenance Triggers**: Direct links to `/update-agents` when staleness detected
- **Testing Integration**: Performance data feeds into `/test-agents` scenarios
- **Coordination Optimization**: Status data improves `/coordinate-agents` efficiency

### Automated Response Integration
- **Auto-Updates**: Performance degradation triggers automatic agent updates
- **Load Balancing**: Status monitoring enables intelligent agent workload distribution  
- **Predictive Maintenance**: Status trends trigger proactive maintenance workflows
- **Quality Assurance**: Continuous status monitoring ensures agent effectiveness

## 🚀 Success Criteria

**Visibility**: Complete real-time visibility into agent performance and health (100% coverage)
**Predictive Accuracy**: Alert system predicts issues before they impact user experience (>90% accuracy)
**Actionable Insights**: Status information provides clear guidance for optimization and maintenance
**Integration Effectiveness**: Status monitoring improves overall agent ecosystem performance

**🎯 Final Result**: Complete transparency into your specialized agent team's performance, health, and utilization with predictive insights that enable proactive optimization and maintenance for sustained high-quality AI assistance.