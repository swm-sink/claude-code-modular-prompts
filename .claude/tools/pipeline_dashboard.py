#!/usr/bin/env python3
"""
Pipeline Dashboard
Real-time monitoring and analytics dashboard for the continuous improvement pipeline.
"""

import json
import logging
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import statistics
from dataclasses import dataclass
from enum import Enum

class DashboardView(Enum):
    OVERVIEW = "overview"
    PERFORMANCE = "performance"
    IMPROVEMENTS = "improvements"
    TRENDS = "trends"
    DETAILED = "detailed"

@dataclass
class DashboardMetrics:
    total_improvements: int
    successful_improvements: int
    failed_improvements: int
    success_rate: float
    avg_response_time: float
    current_satisfaction: float
    trend_direction: str
    last_updated: datetime

class PipelineDashboard:
    """Real-time dashboard for continuous improvement pipeline monitoring."""
    
    def __init__(self, data_path: Optional[Path] = None):
        self.data_path = data_path or Path(".claude")
        self.metrics_path = self.data_path / "metrics"
        self.improvements_path = self.data_path / "improvements"
        self.reports_path = self.data_path / "reports"
        self.logs_path = self.data_path / "logs"
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def generate_dashboard(self, view: DashboardView = DashboardView.OVERVIEW) -> str:
        """Generate dashboard in markdown format."""
        if view == DashboardView.OVERVIEW:
            return self._generate_overview_dashboard()
        elif view == DashboardView.PERFORMANCE:
            return self._generate_performance_dashboard()
        elif view == DashboardView.IMPROVEMENTS:
            return self._generate_improvements_dashboard()
        elif view == DashboardView.TRENDS:
            return self._generate_trends_dashboard()
        elif view == DashboardView.DETAILED:
            return self._generate_detailed_dashboard()
        else:
            return self._generate_overview_dashboard()
    
    def _generate_overview_dashboard(self) -> str:
        """Generate overview dashboard."""
        try:
            metrics = self._collect_dashboard_metrics()
            recent_improvements = self._get_recent_improvements(limit=5)
            performance_summary = self._get_performance_summary()
            
            dashboard = f"""# Continuous Improvement Pipeline Dashboard

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## 📊 Executive Summary

### Key Metrics
| Metric | Value | Trend |
|--------|-------|-------|
| Success Rate | {metrics.success_rate:.1%} | {self._trend_icon(metrics.trend_direction)} |
| Total Improvements | {metrics.total_improvements} | - |
| Avg Response Time | {metrics.avg_response_time:.2f}s | {self._performance_trend_icon(metrics.avg_response_time)} |
| User Satisfaction | {metrics.current_satisfaction:.1f}/5.0 | {self._satisfaction_trend_icon(metrics.current_satisfaction)} |

### Health Status
{self._generate_health_status(metrics)}

## 🚀 Recent Improvements

{self._format_recent_improvements(recent_improvements)}

## 📈 Performance Summary

{self._format_performance_summary(performance_summary)}

## 🎯 Quick Actions

- [View Detailed Performance](./performance_dashboard.md)
- [Analyze Trends](./trends_dashboard.md)
- [Review All Improvements](./improvements_dashboard.md)
- [Check Pipeline Logs](./logs/)

---
*Dashboard automatically updated every 15 minutes*
"""
            
            return dashboard
            
        except Exception as e:
            self.logger.error(f"Failed to generate overview dashboard: {e}")
            return self._generate_error_dashboard(str(e))
    
    def _generate_performance_dashboard(self) -> str:
        """Generate detailed performance dashboard."""
        try:
            performance_data = self._collect_performance_data()
            
            dashboard = f"""# Performance Analytics Dashboard

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## 📊 Performance Metrics Overview

### Response Time Analysis
{self._generate_response_time_chart(performance_data['response_times'])}

### Success Rate Trends
{self._generate_success_rate_chart(performance_data['success_rates'])}

### Error Rate Analysis
{self._generate_error_rate_chart(performance_data['error_rates'])}

### Token Efficiency Trends
{self._generate_efficiency_chart(performance_data['token_efficiency'])}

## 🎯 Performance Targets

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Response Time (P95) | {performance_data['current']['response_time']:.2f}s | <3.0s | {self._status_icon(performance_data['current']['response_time'] < 3.0)} |
| Success Rate | {performance_data['current']['success_rate']:.1%} | >85% | {self._status_icon(performance_data['current']['success_rate'] > 0.85)} |
| Error Rate | {performance_data['current']['error_rate']:.1%} | <5% | {self._status_icon(performance_data['current']['error_rate'] < 0.05)} |
| Token Efficiency | {performance_data['current']['token_efficiency']:.1f} | >7.0 | {self._status_icon(performance_data['current']['token_efficiency'] > 7.0)} |

## 📈 Trend Analysis

{self._generate_performance_trends(performance_data)}

## 🔍 Detailed Metrics

{self._generate_detailed_performance_metrics(performance_data)}

---
*Performance data updated every 5 minutes*
"""
            
            return dashboard
            
        except Exception as e:
            self.logger.error(f"Failed to generate performance dashboard: {e}")
            return self._generate_error_dashboard(str(e))
    
    def _generate_improvements_dashboard(self) -> str:
        """Generate improvements tracking dashboard."""
        try:
            improvements_data = self._collect_improvements_data()
            
            dashboard = f"""# Improvements Tracking Dashboard

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## 📊 Improvements Overview

### Summary Statistics
- **Total Improvements:** {improvements_data['total']}
- **Completed:** {improvements_data['completed']} ({improvements_data['completed_percentage']:.1%})
- **In Progress:** {improvements_data['in_progress']}
- **Failed:** {improvements_data['failed']} ({improvements_data['failed_percentage']:.1%})

### Improvements by Category
{self._generate_category_breakdown(improvements_data['by_category'])}

### Improvements by Priority
{self._generate_priority_breakdown(improvements_data['by_priority'])}

## 🚀 Recent Improvements

{self._generate_improvements_timeline(improvements_data['recent'])}

## 📈 Success Rate Trends

{self._generate_improvement_success_chart(improvements_data['success_history'])}

## 🎯 Impact Analysis

{self._generate_impact_analysis(improvements_data['impact_data'])}

## 📋 Current Pipeline

{self._generate_current_pipeline_status()}

---
*Improvements data updated in real-time*
"""
            
            return dashboard
            
        except Exception as e:
            self.logger.error(f"Failed to generate improvements dashboard: {e}")
            return self._generate_error_dashboard(str(e))
    
    def _generate_trends_dashboard(self) -> str:
        """Generate trends analysis dashboard."""
        try:
            trends_data = self._collect_trends_data()
            
            dashboard = f"""# Trends Analysis Dashboard

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## 📈 Long-term Trends

### Performance Evolution
{self._generate_performance_evolution_chart(trends_data['performance'])}

### Quality Improvements Over Time
{self._generate_quality_evolution_chart(trends_data['quality'])}

### Efficiency Gains
{self._generate_efficiency_evolution_chart(trends_data['efficiency'])}

## 🔮 Predictive Analysis

{self._generate_predictive_analysis(trends_data['predictions'])}

## 📊 Correlation Analysis

{self._generate_correlation_analysis(trends_data['correlations'])}

## 🎯 Improvement Opportunities

{self._generate_opportunity_analysis(trends_data['opportunities'])}

## 📅 Seasonal Patterns

{self._generate_seasonal_analysis(trends_data['seasonal'])}

---
*Trends analysis updated weekly*
"""
            
            return dashboard
            
        except Exception as e:
            self.logger.error(f"Failed to generate trends dashboard: {e}")
            return self._generate_error_dashboard(str(e))
    
    def _collect_dashboard_metrics(self) -> DashboardMetrics:
        """Collect key metrics for dashboard overview."""
        try:
            # Load recent improvements
            improvements = self._load_all_improvements()
            
            total_improvements = len(improvements)
            successful_improvements = len([i for i in improvements if i.get('status') == 'completed'])
            failed_improvements = len([i for i in improvements if i.get('status') == 'failed'])
            
            success_rate = successful_improvements / total_improvements if total_improvements > 0 else 0
            
            # Load recent metrics
            recent_metrics = self._load_recent_metrics(days=7)
            
            if recent_metrics:
                avg_response_time = statistics.mean([m['response_time_p95'] for m in recent_metrics])
                current_satisfaction = recent_metrics[-1]['user_satisfaction']
            else:
                avg_response_time = 2.0
                current_satisfaction = 4.0
            
            # Determine trend direction
            trend_direction = self._calculate_trend_direction(recent_metrics)
            
            return DashboardMetrics(
                total_improvements=total_improvements,
                successful_improvements=successful_improvements,
                failed_improvements=failed_improvements,
                success_rate=success_rate,
                avg_response_time=avg_response_time,
                current_satisfaction=current_satisfaction,
                trend_direction=trend_direction,
                last_updated=datetime.now()
            )
            
        except Exception as e:
            self.logger.error(f"Failed to collect dashboard metrics: {e}")
            return DashboardMetrics(
                total_improvements=0,
                successful_improvements=0,
                failed_improvements=0,
                success_rate=0.0,
                avg_response_time=2.0,
                current_satisfaction=4.0,
                trend_direction="stable",
                last_updated=datetime.now()
            )
    
    def _load_all_improvements(self) -> List[Dict[str, Any]]:
        """Load all improvement records."""
        improvements = []
        
        if not self.improvements_path.exists():
            return improvements
        
        for improvement_file in self.improvements_path.glob("*.json"):
            try:
                with open(improvement_file, 'r') as f:
                    improvement = json.load(f)
                improvements.append(improvement)
            except Exception as e:
                self.logger.warning(f"Failed to load improvement {improvement_file}: {e}")
        
        return improvements
    
    def _load_recent_metrics(self, days: int = 30) -> List[Dict[str, Any]]:
        """Load recent metrics data."""
        metrics = []
        
        if not self.metrics_path.exists():
            return metrics
        
        # Load metrics from recent days
        for i in range(days):
            date = datetime.now() - timedelta(days=i)
            metrics_file = self.metrics_path / f"metrics_{date.strftime('%Y%m%d')}.json"
            
            if metrics_file.exists():
                try:
                    with open(metrics_file, 'r') as f:
                        daily_metrics = json.load(f)
                    metrics.extend(daily_metrics)
                except Exception as e:
                    self.logger.warning(f"Failed to load metrics {metrics_file}: {e}")
        
        return sorted(metrics, key=lambda x: x['timestamp'])
    
    def _calculate_trend_direction(self, metrics: List[Dict[str, Any]]) -> str:
        """Calculate overall trend direction from metrics."""
        if len(metrics) < 2:
            return "stable"
        
        # Calculate trends for key metrics
        success_rates = [m['success_rate'] for m in metrics[-7:]]  # Last 7 data points
        response_times = [m['response_time_p95'] for m in metrics[-7:]]
        
        if len(success_rates) >= 2:
            success_trend = success_rates[-1] - success_rates[0]
            response_trend = response_times[-1] - response_times[0]
            
            # Positive if success rate improving or response time decreasing
            if success_trend > 0.05 or response_trend < -0.5:
                return "improving"
            elif success_trend < -0.05 or response_trend > 0.5:
                return "declining"
        
        return "stable"
    
    def _generate_health_status(self, metrics: DashboardMetrics) -> str:
        """Generate health status indicators."""
        health_indicators = []
        
        # Success rate health
        if metrics.success_rate >= 0.9:
            health_indicators.append("🟢 **Success Rate:** Excellent")
        elif metrics.success_rate >= 0.8:
            health_indicators.append("🟡 **Success Rate:** Good")
        else:
            health_indicators.append("🔴 **Success Rate:** Needs Attention")
        
        # Response time health
        if metrics.avg_response_time < 2.0:
            health_indicators.append("🟢 **Performance:** Excellent")
        elif metrics.avg_response_time < 3.0:
            health_indicators.append("🟡 **Performance:** Good")
        else:
            health_indicators.append("🔴 **Performance:** Needs Attention")
        
        # Satisfaction health
        if metrics.current_satisfaction >= 4.5:
            health_indicators.append("🟢 **User Satisfaction:** Excellent")
        elif metrics.current_satisfaction >= 4.0:
            health_indicators.append("🟡 **User Satisfaction:** Good")
        else:
            health_indicators.append("🔴 **User Satisfaction:** Needs Attention")
        
        return "\n".join(health_indicators)
    
    def _get_recent_improvements(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get most recent improvements."""
        improvements = self._load_all_improvements()
        
        # Sort by creation date
        sorted_improvements = sorted(
            improvements,
            key=lambda x: x.get('created_at', ''),
            reverse=True
        )
        
        return sorted_improvements[:limit]
    
    def _format_recent_improvements(self, improvements: List[Dict[str, Any]]) -> str:
        """Format recent improvements for display."""
        if not improvements:
            return "*No recent improvements found*"
        
        formatted = []
        for improvement in improvements:
            status_icon = self._get_status_icon(improvement.get('status', 'unknown'))
            title = improvement.get('title', 'Untitled')
            category = improvement.get('category', 'unknown')
            priority = improvement.get('priority', 'medium')
            
            formatted.append(f"- {status_icon} **{title}** ({category}, {priority} priority)")
        
        return "\n".join(formatted)
    
    def _get_status_icon(self, status: str) -> str:
        """Get icon for improvement status."""
        icons = {
            'completed': '✅',
            'in_progress': '🔄',
            'failed': '❌',
            'planned': '📋',
            'identified': '🔍',
            'rolled_back': '↩️'
        }
        return icons.get(status, '❓')
    
    def _trend_icon(self, trend: str) -> str:
        """Get icon for trend direction."""
        icons = {
            'improving': '📈',
            'declining': '📉',
            'stable': '➡️'
        }
        return icons.get(trend, '➡️')
    
    def _performance_trend_icon(self, response_time: float) -> str:
        """Get performance trend icon."""
        if response_time < 2.0:
            return '🟢'
        elif response_time < 3.0:
            return '🟡'
        else:
            return '🔴'
    
    def _satisfaction_trend_icon(self, satisfaction: float) -> str:
        """Get satisfaction trend icon."""
        if satisfaction >= 4.5:
            return '😊'
        elif satisfaction >= 4.0:
            return '🙂'
        else:
            return '😐'
    
    def _status_icon(self, is_good: bool) -> str:
        """Get status icon for boolean condition."""
        return '✅' if is_good else '❌'
    
    def _get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary data."""
        metrics = self._load_recent_metrics(days=7)
        
        if not metrics:
            return {
                'avg_response_time': 2.0,
                'success_rate': 0.85,
                'improvement_count': 0
            }
        
        return {
            'avg_response_time': statistics.mean([m['response_time_p95'] for m in metrics]),
            'success_rate': statistics.mean([m['success_rate'] for m in metrics]),
            'improvement_count': len([m for m in metrics if m.get('improved', False)])
        }
    
    def _format_performance_summary(self, summary: Dict[str, Any]) -> str:
        """Format performance summary for display."""
        return f"""### Last 7 Days
- **Average Response Time:** {summary['avg_response_time']:.2f}s
- **Average Success Rate:** {summary['success_rate']:.1%}
- **Performance Improvements:** {summary['improvement_count']}"""
    
    def _collect_performance_data(self) -> Dict[str, Any]:
        """Collect detailed performance data."""
        metrics = self._load_recent_metrics(days=30)
        
        # Process metrics into charts and summaries
        response_times = [m['response_time_p95'] for m in metrics]
        success_rates = [m['success_rate'] for m in metrics]
        error_rates = [m['error_rate'] for m in metrics]
        token_efficiency = [m['token_efficiency'] for m in metrics]
        
        current_metrics = metrics[-1] if metrics else {}
        
        return {
            'response_times': response_times,
            'success_rates': success_rates,
            'error_rates': error_rates,
            'token_efficiency': token_efficiency,
            'current': {
                'response_time': current_metrics.get('response_time_p95', 2.0),
                'success_rate': current_metrics.get('success_rate', 0.85),
                'error_rate': current_metrics.get('error_rate', 0.05),
                'token_efficiency': current_metrics.get('token_efficiency', 7.0)
            }
        }
    
    def _generate_response_time_chart(self, data: List[float]) -> str:
        """Generate ASCII chart for response times."""
        if not data:
            return "*No response time data available*"
        
        # Simple ASCII chart
        chart = "```\nResponse Time Trend (Last 30 Days)\n"
        chart += self._create_ascii_chart(data, "Response Time (seconds)")
        chart += "\n```"
        
        return chart
    
    def _create_ascii_chart(self, data: List[float], title: str) -> str:
        """Create simple ASCII chart."""
        if not data:
            return "No data available"
        
        # Normalize data for chart
        min_val = min(data)
        max_val = max(data)
        
        if max_val == min_val:
            normalized = [5] * len(data)  # Flat line
        else:
            normalized = [(val - min_val) / (max_val - min_val) * 10 for val in data]
        
        # Create chart
        chart = f"{title}\n"
        chart += "┌" + "─" * 50 + "┐\n"
        
        for i in range(10, -1, -1):
            line = f"{i:2d} ┤"
            for val in normalized[-40:]:  # Last 40 points
                if val >= i:
                    line += "█"
                else:
                    line += " "
            line += "│\n"
            chart += line
        
        chart += "   └" + "─" * 50 + "┘\n"
        chart += f"    Min: {min_val:.2f}, Max: {max_val:.2f}, Latest: {data[-1]:.2f}"
        
        return chart
    
    def _generate_error_dashboard(self, error_message: str) -> str:
        """Generate error dashboard when data collection fails."""
        return f"""# Pipeline Dashboard - Error

**Error occurred:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## ❌ Dashboard Generation Failed

**Error Message:** {error_message}

## 🔧 Troubleshooting

1. Check if pipeline is running
2. Verify data directory permissions
3. Check log files for detailed errors
4. Ensure all required dependencies are installed

## 📞 Support

If the issue persists, please check the pipeline logs at `.claude/logs/` for more details.

---
*This is an automatically generated error report*
"""
    
    def save_dashboard(self, view: DashboardView = DashboardView.OVERVIEW, output_path: Optional[Path] = None) -> Path:
        """Save dashboard to file."""
        dashboard_content = self.generate_dashboard(view)
        
        if output_path is None:
            output_path = self.data_path / f"{view.value}_dashboard.md"
        
        with open(output_path, 'w') as f:
            f.write(dashboard_content)
        
        self.logger.info(f"Dashboard saved to {output_path}")
        return output_path
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Get raw dashboard data as JSON."""
        try:
            return {
                'metrics': self._collect_dashboard_metrics().__dict__,
                'recent_improvements': self._get_recent_improvements(),
                'performance_summary': self._get_performance_summary(),
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            self.logger.error(f"Failed to get dashboard data: {e}")
            return {'error': str(e), 'timestamp': datetime.now().isoformat()}

def main():
    """Main entry point for the dashboard generator."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Pipeline Dashboard Generator")
    parser.add_argument('--view', choices=[v.value for v in DashboardView], 
                       default='overview', help="Dashboard view to generate")
    parser.add_argument('--output', type=Path, help="Output file path")
    parser.add_argument('--data-path', type=Path, help="Data directory path")
    parser.add_argument('--json', action='store_true', help="Output raw JSON data")
    
    args = parser.parse_args()
    
    dashboard = PipelineDashboard(data_path=args.data_path)
    
    if args.json:
        data = dashboard.get_dashboard_data()
        print(json.dumps(data, indent=2))
    else:
        view = DashboardView(args.view)
        output_path = dashboard.save_dashboard(view, args.output)
        print(f"Dashboard generated: {output_path}")

if __name__ == "__main__":
    main()