---
description: Advanced log monitoring utilities with intelligent analysis, pattern detection, and comprehensive troubleshooting
argument-hint: "[log_scope] [analysis_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /monitor logs - Advanced Log Monitoring Utilities

Sophisticated log monitoring utilities with intelligent analysis, pattern detection, and comprehensive troubleshooting capabilities.

## Usage
```bash
/monitor logs analyze                        # Intelligent log analysis
/monitor logs --patterns                     # Pattern detection and analysis
/monitor logs --troubleshoot                 # Comprehensive troubleshooting
/monitor logs --comprehensive                # Comprehensive log monitoring
```

## Log Levels
- **error** - Error and exception tracking
- **warn** - Warning and performance issues
- **info** - General application events
- **debug** - Detailed diagnostic information
- **trace** - Full execution tracing

## Source Types
- **app** - Application logs
- **system** - System and infrastructure logs
- **access** - HTTP/API access logs
- **security** - Security and audit logs
- **all** - All log sources (default)

## Analysis Features
### Pattern Detection
- Error clustering and frequency analysis
- Performance degradation patterns
- Security threat indicators
- Anomaly detection algorithms

### Log Aggregation
- Multi-source log correlation
- Time-series trend analysis
- User journey reconstruction
- Service dependency mapping

### Search Capabilities
- Full-text search with regex support
- Structured query language
- Time-range filtering
- Multi-dimensional pivoting

## Output Formats
- **stream** - Real-time log streaming
- **summary** - Aggregated insights report
- **alerts** - Critical issue notifications
- **export** - Structured data export

## Examples
```bash
/monitor logs error app          # Application errors
/monitor logs warn --last 1h     # Recent warnings
/monitor logs all --pattern "timeout"    # Timeout events
/monitor logs debug --follow     # Live debugging
```

## Integration
- Real-time alerting system
- Dashboard visualization
- Incident response automation
- Log retention policies