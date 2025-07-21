---
description: Advanced dashboard monitoring utilities with intelligent visualization, real-time analytics, and comprehensive insights
argument-hint: "[dashboard_type] [visualization_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor dashboard - Advanced Dashboard Monitoring Utilities

Sophisticated dashboard monitoring utilities with intelligent visualization, real-time analytics, and comprehensive insights generation.

## Usage
```bash
/monitor dashboard create                    # Create intelligent dashboards
/monitor dashboard --real-time               # Real-time monitoring dashboards
/monitor dashboard --analytics               # Advanced analytics dashboards
/monitor dashboard --comprehensive           # Comprehensive monitoring visualization
```

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