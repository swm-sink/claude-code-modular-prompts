# Monitor Dashboard Command

## Command
`/monitor dashboard [type] [options]`

## Purpose
Creates monitoring dashboards with key metrics visualization and system status overview.

## Usage
```bash
/monitor dashboard               # Full system dashboard
/monitor dashboard app          # Application metrics
/monitor dashboard infra        # Infrastructure status
/monitor dashboard custom      # Custom dashboard wizard
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