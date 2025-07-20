# Quality Report Command

## Purpose
Generate comprehensive quality reports with trends, history, and improvement recommendations for codebase quality management.

## Usage
```bash
/quality report [scope] [format] [--timeframe=7d]
```

## Command Options
- `scope`: full|module|security|performance (default: full)
- `format`: console|markdown|json|html (default: console)
- `--timeframe`: 1d|7d|30d|90d (default: 7d)

## Features

### Quality Metrics Analysis
- Code coverage percentage and trends
- Complexity metrics (cyclomatic, cognitive)
- Duplication analysis and hotspots
- Security vulnerability assessment
- Performance benchmark comparisons

### Historical Tracking
- Quality score progression over time
- Regression identification and alerts
- Improvement milestone tracking
- Commit-level quality impact analysis

### Team Collaboration
- Shareable quality dashboards
- Team performance comparisons
- Quality gate compliance status
- Actionable improvement recommendations

### Report Formats
- **Console**: Interactive dashboard view
- **Markdown**: Documentation-ready reports
- **JSON**: API integration and automation
- **HTML**: Stakeholder presentation format

## Example Usage
```bash
/quality report security markdown --timeframe=30d
/quality report performance json
/quality report full html --timeframe=90d
```

## Report Sections
1. Executive summary with key metrics
2. Quality trends and historical analysis
3. Critical issues requiring immediate attention
4. Improvement recommendations with priority
5. Team performance insights
6. Quality gate compliance status