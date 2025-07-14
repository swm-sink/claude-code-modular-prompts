# Monitoring Data

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-12   | organized |

## Purpose

Real-time monitoring data, operational dashboards, and current system status tracking for immediate operational awareness.

## Contents

### Real-Time Data
- `*-latest.json` - Current monitoring snapshots
- `framework-health-*.json` - Framework health tracking
- `integration-test-*.json` - Integration test results
- `trace-compliance-*.json` - Compliance monitoring

### Dashboard Files
- `dashboard-*.html` - Operational dashboards
- `dashboard-data-*.json` - Dashboard data sources
- `dashboard-*.log` - Dashboard generation logs

### Historical Data
- Timestamped monitoring results
- Daily operational snapshots
- System health evolution tracking

## Data Sources

Consolidated from:
- `reports/current/` - Real-time monitoring data
- `reports/daily/` - Daily monitoring snapshots  
- `reports/dashboard/` - Operational dashboards

## Organization

Files are organized by:
- **Current Data**: Latest monitoring snapshots with `-latest` suffix
- **Historical Data**: Timestamped files for trend analysis
- **Dashboards**: Interactive monitoring interfaces

## Usage

Reference these files for:
- Current system health assessment
- Real-time operational monitoring
- Historical trend analysis
- Dashboard-based system visualization
- Compliance monitoring and validation