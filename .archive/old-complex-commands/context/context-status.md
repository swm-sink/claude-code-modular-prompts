---
name: context-status
description: Comprehensive context system health monitoring, metrics display, and performance dashboard
usage: "context-status [dashboard|health|metrics|trends] [--detailed|--summary|--export]"
allowed-tools: [Read, LS, Glob, Grep, Write, Edit, Bash]
category: context
version: "1.0"
---

# Context Status: Comprehensive Context System Health Dashboard

## Purpose: Complete Context System Visibility & Health Monitoring

The `/context-status` command provides comprehensive monitoring and reporting of your context system's health, performance, and effectiveness. Through real-time metrics, trend analysis, and actionable insights, it ensures your context system maintains optimal performance and continues to deliver maximum value.

**Status Philosophy**: Proactive over reactive, actionable over informational, comprehensive over superficial, trends over snapshots.

## 📊 Context Status Modes

### Dashboard Mode
**Usage**: `/context-status dashboard [--live|--snapshot|--export]`

Real-time comprehensive dashboard of context system health and performance:

```
Context System Dashboard
========================
Last Updated: 2024-01-15 14:30:22

🎯 System Health Overview
┌─────────────────────────────────────────────────────────────┐
│ Overall Health Score: 9.2/10 (Excellent)                   │
│ Status: ✅ All Systems Operational                          │
│ Last Issues: None in past 7 days                           │
│ Recommendation: Minor optimization opportunity in Layer 3   │
└─────────────────────────────────────────────────────────────┘

📈 Performance Metrics (24h)
┌─────────────────────────────┬──────────┬──────────┬──────────┐
│ Metric                      │ Current  │ Average  │ Trend    │
├─────────────────────────────┼──────────┼──────────┼──────────┤
│ Context Effectiveness       │ 8.9/10   │ 8.7/10   │ ↗ +2.3%  │
│ Loading Performance         │ 1.2s     │ 1.4s     │ ↗ -14.3% │
│ Token Efficiency            │ 92.4%    │ 89.1%    │ ↗ +3.7%  │
│ User Satisfaction           │ 4.8/5    │ 4.6/5    │ ↗ +4.3%  │
│ Context Freshness          │ 96.8%    │ 94.2%    │ ↗ +2.8%  │
│ Navigation Efficiency      │ 89.3%    │ 87.6%    │ ↗ +1.9%  │
└─────────────────────────────┴──────────┴──────────┴──────────┘

🏗️ Context Architecture Health
┌─────────────────┬────────────┬────────────┬──────────────────┐
│ Layer           │ Files      │ Health     │ Last Updated     │
├─────────────────┼────────────┼────────────┼──────────────────┤
│ Foundation      │ 1 file     │ ✅ 9.8/10  │ 2 days ago       │
│ Domain          │ 4 files    │ ✅ 9.1/10  │ 1 day ago        │
│ Technical       │ 5 files    │ ⚠️ 8.4/10  │ 4 days ago       │
│ Workflow        │ 5 files    │ ✅ 9.0/10  │ 1 day ago        │
│ Agents          │ 4 files    │ ✅ 9.3/10  │ 6 hours ago      │
└─────────────────┴────────────┴────────────┴──────────────────┘

💡 Recent Activity
├── [14:15] Context refresh completed - Technical layer updated
├── [13:42] Optimization applied - 12% token reduction achieved
├── [12:18] Validation test passed - All context layers effective
├── [11:34] Navigation pattern updated - User experience improved
└── [10:57] Cross-reference integrity check passed

🎯 Action Items (2)
├── [High] Update deployment context in Technical layer (4 days overdue)
└── [Medium] Optimize cross-references in Domain layer (efficiency opportunity)
```

### Health Mode
**Usage**: `/context-status health [--detailed|--alerts|--history]`

Focused health assessment with issue identification and recommendations:

```
Context System Health Assessment
================================

🏥 Overall Health Diagnosis
├── System Status: ✅ Healthy (Minor Issues)
├── Health Score: 8.7/10 (Very Good)
├── Critical Issues: 0
├── Warning Issues: 2
├── Info Notifications: 3
└── Trend: ↗ Improving (7-day trend)

🔍 Detailed Health Analysis
├── Context Effectiveness Health
│   ├── ✅ Response Quality: 9.1/10 (Excellent)
│   ├── ✅ Domain Understanding: 8.9/10 (Very Good)
│   ├── ✅ Technical Accuracy: 8.8/10 (Very Good)
│   ├── ⚠️ Workflow Alignment: 8.2/10 (Good - Improvement Available)
│   └── ✅ Agent Specialization: 9.0/10 (Excellent)
│
├── Context Architecture Health
│   ├── ✅ Layer Structure: Optimal (5-layer hierarchy)
│   ├── ✅ Cross-Reference Integrity: 97.3% valid
│   ├── ⚠️ Content Currency: 89.4% current (some outdated content)
│   ├── ✅ Navigation Efficiency: 91.2% optimal paths
│   └── ✅ Token Efficiency: 92.1% value per token
│
├── Context Performance Health
│   ├── ✅ Loading Speed: 1.2s average (Target: <2s)
│   ├── ✅ Search Performance: 0.3s average (Target: <0.5s)
│   ├── ✅ Memory Usage: 45MB (Target: <100MB)
│   ├── ✅ Update Performance: 3.4s average (Target: <5s)
│   └── ✅ Cache Hit Rate: 84.3% (Target: >80%)
│
└── Context Maintenance Health
    ├── ℹ️ Last Refresh: 6 hours ago (Target: <24h)
    ├── ℹ️ Last Optimization: 2 days ago (Target: <7d)
    ├── ✅ Backup Status: Current (2 hours ago)
    ├── ℹ️ Validation Status: Passed (12 hours ago)
    └── ✅ Update History: 3 successful updates this week

⚠️ Issues Requiring Attention
├── [Warning] Technical layer context 4 days outdated
│   ├── Impact: Moderate - May affect deployment guidance
│   ├── Recommendation: Run `/refresh-context sync --layer technical`
│   └── Priority: High (Complete within 24 hours)
│
└── [Warning] Cross-references in Domain layer could be optimized
    ├── Impact: Low - Minor efficiency improvement available
    ├── Recommendation: Run `/optimize-context analyze --domain`
    └── Priority: Medium (Complete within 1 week)

💊 Health Improvement Recommendations
├── Schedule automatic refresh for Technical layer (daily)
├── Consider adding security specialist agent to Agent layer
├── Review and update workflow documentation (quarterly)
└── Implement performance monitoring alerts (proactive)
```

### Metrics Mode
**Usage**: `/context-status metrics [--performance|--usage|--effectiveness|--all]`

Detailed metrics analysis with historical trends and insights:

```
Context System Metrics Analysis
===============================

📊 Context Effectiveness Metrics
┌─────────────────────────────────────────────────────────────┐
│ Response Quality Metrics (30-day trend)                     │
│                                                             │
│ 10.0 ┤                                              ╭─╮    │
│  9.5 ┤                                         ╭────╯ │    │
│  9.0 ┤                                    ╭────╯      │    │
│  8.5 ┤                               ╭────╯           │    │
│  8.0 ┤                          ╭────╯                │    │
│  7.5 ┤                     ╭────╯                     │    │
│  7.0 ┤                ╭────╯                          │    │
│  6.5 ┤           ╭────╯                               │    │
│  6.0 ┤      ╭────╯                                    │    │
│      └──────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
│      Jan 1   5    10   15   20   25   30  Feb 2    7   12 │
│                                                             │
│ Current: 9.2/10 | Peak: 9.3/10 | Average: 8.4/10         │
│ Trend: ↗ Consistently improving (+18% over 30 days)       │
└─────────────────────────────────────────────────────────────┘

🏃 Performance Metrics
├── Context Loading Performance
│   ├── Average Load Time: 1.2s (↗ -14% improvement)
│   ├── 95th Percentile: 2.1s (Target: <3s) ✅
│   ├── Slowest Layer: Technical (1.8s average)
│   └── Fastest Layer: Foundation (0.4s average)
│
├── Search & Navigation Performance
│   ├── Average Search Time: 0.31s (↗ -8% improvement)
│   ├── Search Success Rate: 94.2% (↗ +3.1% improvement)
│   ├── Navigation Efficiency: 89.3% optimal paths
│   └── Cross-reference Resolution: 0.18s average
│
├── Token Efficiency Metrics
│   ├── Token Usage per Response: 2,847 avg (↗ -12% reduction)
│   ├── Value per Token Score: 8.4/10 (↗ +6% improvement)
│   ├── Context Utilization Rate: 78.3% (Target: >70%) ✅
│   └── Redundancy Elimination: 15.2% content optimized
│
└── System Resource Metrics
    ├── Memory Usage: 45MB average (Peak: 67MB)
    ├── CPU Usage: 3.2% average (Peak: 8.7%)
    ├── Storage Usage: 12.4MB context files
    └── Cache Efficiency: 84.3% hit rate

📈 Usage Pattern Analysis
├── Most Accessed Context
│   ├── 1. technical/architecture.md (127 accesses this week)
│   ├── 2. domain/business-rules.md (89 accesses this week)
│   ├── 3. workflows/development.md (76 accesses this week)
│   ├── 4. CLAUDE.md (foundation) (203 accesses this week)
│   └── 5. agents/domain-expert.md (54 accesses this week)
│
├── Access Pattern Insights
│   ├── Peak Usage: 10-11 AM, 2-4 PM (development hours)
│   ├── Most Common Paths: Foundation → Technical → Workflow
│   ├── Average Session Duration: 12.4 minutes
│   └── Context Switch Rate: 3.2 switches per session
│
├── User Behavior Patterns
│   ├── Search vs Browse: 65% browse, 35% search
│   ├── Layer Preference: Technical (40%), Domain (28%), Workflow (22%)
│   ├── Cross-reference Following: 73% of links followed
│   └── Return Visit Rate: 82% return within 24 hours
│
└── Feature Utilization
    ├── Navigation Commands: 89% usage rate
    ├── Testing Commands: 34% usage rate
    ├── Update Commands: 67% usage rate
    └── Optimization Commands: 23% usage rate

🎯 Context Quality Indicators
├── Content Freshness
│   ├── ✅ Foundation Layer: 100% current
│   ├── ✅ Domain Layer: 92% current (1 outdated section)
│   ├── ⚠️ Technical Layer: 78% current (needs refresh)
│   ├── ✅ Workflow Layer: 94% current
│   └── ✅ Agent Layer: 97% current
│
├── Cross-reference Health
│   ├── Valid References: 97.3% (742/763 total)
│   ├── Broken References: 2.7% (21 broken links)
│   ├── Bidirectional Consistency: 94.8%
│   └── Navigation Path Efficiency: 91.2%
│
├── Content Effectiveness
│   ├── Information Density: 8.7/10 (High value content)
│   ├── Actionability Score: 8.9/10 (Very actionable)
│   ├── Specificity Score: 9.1/10 (Project-specific)
│   └── User Satisfaction: 4.8/5 stars
│
└── Maintenance Health
    ├── Update Frequency: 2.3 updates/week (Target: 2-4)
    ├── Validation Pass Rate: 96.8% (Last 30 tests)
    ├── Optimization Frequency: Monthly (Target: Bi-weekly)
    └── Backup Success Rate: 100% (Daily automated)
```

### Trends Mode
**Usage**: `/context-status trends [--weekly|--monthly|--quarterly|--custom]`

Historical trend analysis with predictive insights and recommendations:

```
Context System Trend Analysis
=============================

📈 Performance Trend Analysis (90-day period)

Context Effectiveness Trends:
├── Overall Trend: ↗ Strongly Positive (+24% improvement)
├── Best Month: February 2024 (9.1/10 average)
├── Improvement Rate: +2.1% per month
├── Seasonality: Higher effectiveness during sprint cycles
└── Prediction: 9.5/10 effectiveness by April 2024

Performance Improvement Trends:
├── Loading Speed: ↗ 31% faster (2.1s → 1.2s average)
├── Token Efficiency: ↗ 18% improvement (more value per token)
├── User Satisfaction: ↗ 15% increase (4.2 → 4.8 stars)
├── Search Accuracy: ↗ 12% improvement (83% → 94% success)
└── Content Currency: ↗ 8% fresher (85% → 92% current)

📊 Usage Pattern Trends
├── Usage Growth: ↗ 43% increase in context interactions
├── Feature Adoption: 
│   ├── Navigation: 67% → 89% adoption (+33%)
│   ├── Testing: 15% → 34% adoption (+127%)
│   ├── Updates: 45% → 67% adoption (+49%)
│   └── Optimization: 8% → 23% adoption (+188%)
├── User Engagement: ↗ 28% increase in session duration
└── Context Switching: ↗ 15% more efficient navigation

🔮 Predictive Insights
├── Next Month Predictions:
│   ├── Effectiveness Score: 9.4/10 (↗ +3.3%)
│   ├── Loading Performance: 1.1s (↗ -8% faster)
│   ├── Usage Volume: +12% more interactions
│   └── User Satisfaction: 4.9/5 stars
│
├── Quarterly Projections:
│   ├── System Maturity: Reaching optimization plateau
│   ├── Maintenance Needs: Increasing (more complex system)
│   ├── Training Requirements: New team member onboarding
│   └── Infrastructure: May need performance scaling
│
└── Risk Indicators:
    ├── 🟡 Technical debt accumulation in complex contexts
    ├── 🟡 User expectation inflation (higher standards)
    ├── 🟢 System stability (no critical issues projected)
    └── 🟢 Team adoption (high engagement trend)

💡 Strategic Recommendations
├── Short-term (1-4 weeks):
│   ├── Address technical layer staleness immediately
│   ├── Implement automated refresh for high-change areas
│   ├── Optimize cross-references for navigation efficiency
│   └── Add performance monitoring alerts
│
├── Medium-term (1-3 months):
│   ├── Develop advanced agent specializations
│   ├── Implement machine learning for optimization
│   ├── Create user-specific context customization
│   └── Build integration with development tools
│
└── Long-term (3+ months):
    ├── Design scalable context architecture for growth
    ├── Plan for multi-project context management
    ├── Develop context sharing and collaboration features
    └── Create advanced analytics and insights platform
```

## 📊 Advanced Analytics Features

### Custom Metric Tracking
Track project-specific metrics and KPIs:
```
Custom Metrics Configuration:
├── Team Productivity Metrics
│   ├── Time saved per context interaction
│   ├── Questions answered without human intervention
│   ├── Code review efficiency improvement
│   └── Onboarding time reduction
│
├── Project-Specific Metrics
│   ├── Domain knowledge accuracy
│   ├── Technical decision alignment
│   ├── Process adherence measurement
│   └── Quality standard compliance
│
└── Business Impact Metrics
    ├── Developer satisfaction scores
    ├── Knowledge retention rates
    ├── Context system ROI
    └── Team collaboration efficiency
```

### Alert System
Proactive monitoring with intelligent alerting:
```
Alert Configuration:
├── Performance Alerts
│   ├── Loading time exceeds threshold (>3s)
│   ├── Context effectiveness drops (<8.0)
│   ├── Search success rate falls (<90%)
│   └── Memory usage spikes (>100MB)
│
├── Health Alerts
│   ├── Context becomes stale (>7 days)
│   ├── Broken references exceed limit (>5%)
│   ├── Validation failures occur
│   └── Update operations fail
│
└── Usage Alerts
    ├── Unusual usage pattern detection
    ├── User satisfaction decline
    ├── Feature adoption stagnation
    └── System underutilization warning
```

### Export and Integration
Share status data with other tools and teams:
```
Export Options:
├── Dashboard Exports
│   ├── PDF reports for stakeholders
│   ├── JSON data for integrations
│   ├── CSV data for analysis
│   └── API endpoints for real-time data
│
├── Integration Points
│   ├── Project management tools
│   ├── Team communication platforms
│   ├── Development metrics dashboards
│   └── Performance monitoring systems
│
└── Automated Reporting
    ├── Weekly status emails
    ├── Monthly health reports
    ├── Quarterly trend analysis
    └── Real-time status dashboards
```

## 🎯 Integration with Context System

The context status system integrates seamlessly with all other context commands:
- **Generate**: Status tracks generation success and effectiveness
- **Navigate**: Status monitors navigation patterns and efficiency
- **Test**: Status incorporates test results into health scores
- **Update**: Status tracks update frequency and success rates
- **Refresh**: Status monitors refresh patterns and currency
- **Optimize**: Status measures optimization impact and effectiveness

---

**Remember**: Context status monitoring is about maintaining a healthy, high-performing context system that continues to provide maximum value to your development team. Use these insights to make data-driven decisions about context system improvements and optimizations.