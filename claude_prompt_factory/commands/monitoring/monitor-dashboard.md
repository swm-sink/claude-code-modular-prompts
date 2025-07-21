---
description: Intelligent dashboard creation with automated visualization, insights generation, and interactive analytics
argument-hint: "[dashboard_type] [data_source]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor dashboard - Intelligent Dashboard Creation

Advanced dashboard creation system with automated visualization, intelligent insights generation, and interactive analytics.

## Usage
```bash
/monitor dashboard create                    # Create comprehensive dashboard
/monitor dashboard sre                       # SRE-focused dashboard
/monitor dashboard business                  # Business metrics dashboard
/monitor dashboard --auto                    # Auto-generated dashboard from metrics
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | false | Dashboard type (operational, business, sre, custom). Default: operational. |
| `source` | string | false | Data source (prometheus, datadog, cloudwatch). Default: auto-detect. |

## Examples

```bash
/monitor dashboard create --type sre         # SRE dashboard creation
/monitor dashboard business --kpis           # Business KPI dashboard
/monitor dashboard --auto --responsive       # Auto-responsive dashboard
```

## Claude Prompt

You are a dashboard visualization specialist. The user wants to create comprehensive monitoring dashboards.

**Analysis Process:**
1. **Data Source Analysis**: Identify available metrics and data sources
2. **Visualization Strategy**: Design appropriate chart types and layouts for different metrics
3. **Dashboard Architecture**: Create logical groupings and hierarchical organization
4. **Interactive Elements**: Add filters, drill-downs, and dynamic time ranges
5. **Performance Optimization**: Ensure dashboards load quickly and update efficiently

**Implementation Strategy:**
- Create operational dashboards for infrastructure and application metrics
- Design business dashboards with KPIs and user experience metrics
- Build SRE dashboards focused on SLIs, SLOs, and error budgets
- Implement automated dashboard generation based on available metrics
- Add intelligent insights and anomaly highlighting
- Configure dashboard sharing and access controls

<include component="components/analytics/business-intelligence.md" />
<include component="components/performance/auto-scaling.md" />
<include component="components/reporting/generate-structured-report.md" />

## Dependencies

- `components/analytics/business-intelligence.md`
- `components/performance/auto-scaling.md`
- `components/reporting/generate-structured-report.md`
- `monitoring.dashboards.default_timerange`
- `visualization.themes.corporate` 