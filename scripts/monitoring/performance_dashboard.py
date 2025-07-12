#!/usr/bin/env python3
"""
Performance Dashboard for Claude Code Modular Framework

This module provides a comprehensive real-time performance dashboard with:
- Real-time performance metrics visualization
- Token usage tracking and optimization insights
- Context window utilization monitoring
- Parallel execution efficiency tracking
- Cache performance analytics
- User experience metrics
- Performance regression detection

Agent 5: Performance & Optimization Engineer
Target: Real-time visibility, predictive optimization, 99.9% uptime monitoring
"""

import json
import time
import threading
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
import statistics
import logging
from collections import deque
from enum import Enum
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MetricType(Enum):
    """Types of performance metrics."""
    EXECUTION_TIME = "execution_time"
    CONTEXT_USAGE = "context_usage"
    CACHE_EFFICIENCY = "cache_efficiency"
    PARALLEL_EFFICIENCY = "parallel_efficiency"
    USER_SATISFACTION = "user_satisfaction"
    SYSTEM_RESOURCES = "system_resources"
    ERROR_RATE = "error_rate"


class AlertLevel(Enum):
    """Alert severity levels."""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass
class PerformanceMetric:
    """Individual performance metric."""
    metric_id: str
    metric_type: MetricType
    value: float
    timestamp: datetime
    context: Dict[str, Any]
    tags: List[str]


@dataclass
class PerformanceAlert:
    """Performance alert."""
    alert_id: str
    level: AlertLevel
    message: str
    metric_type: MetricType
    threshold_value: float
    actual_value: float
    timestamp: datetime
    resolved: bool = False


@dataclass
class PerformanceTarget:
    """Performance target definition."""
    target_id: str
    metric_type: MetricType
    target_value: float
    comparison_operator: str  # >, <, >=, <=, ==
    description: str
    alert_level: AlertLevel


class MetricsCollector:
    """Collects performance metrics from various sources."""
    
    def __init__(self, max_metrics_per_type: int = 1000):
        self.metrics_store = {}
        self.max_metrics_per_type = max_metrics_per_type
        self.collection_active = False
        self.collectors = {}
        
    def register_collector(self, metric_type: MetricType, collector_func: callable):
        """Register a metric collector function."""
        self.collectors[metric_type] = collector_func
    
    def start_collection(self, interval_seconds: float = 1.0):
        """Start continuous metrics collection."""
        self.collection_active = True
        
        def collection_loop():
            while self.collection_active:
                self._collect_all_metrics()
                time.sleep(interval_seconds)
        
        collection_thread = threading.Thread(target=collection_loop, daemon=True)
        collection_thread.start()
        logger.info(f"Metrics collection started with {interval_seconds}s interval")
    
    def stop_collection(self):
        """Stop metrics collection."""
        self.collection_active = False
        logger.info("Metrics collection stopped")
    
    def _collect_all_metrics(self):
        """Collect metrics from all registered collectors."""
        for metric_type, collector_func in self.collectors.items():
            try:
                metric_data = collector_func()
                if metric_data:
                    self._store_metric(metric_type, metric_data)
            except Exception as e:
                logger.error(f"Error collecting {metric_type}: {e}")
    
    def _store_metric(self, metric_type: MetricType, metric_data: Dict[str, Any]):
        """Store a metric in the metrics store."""
        if metric_type not in self.metrics_store:
            self.metrics_store[metric_type] = deque(maxlen=self.max_metrics_per_type)
        
        metric = PerformanceMetric(
            metric_id=str(uuid.uuid4()),
            metric_type=metric_type,
            value=metric_data.get('value', 0.0),
            timestamp=datetime.now(),
            context=metric_data.get('context', {}),
            tags=metric_data.get('tags', [])
        )
        
        self.metrics_store[metric_type].append(metric)
    
    def get_metrics(self, metric_type: MetricType, 
                   limit: Optional[int] = None, 
                   since: Optional[datetime] = None) -> List[PerformanceMetric]:
        """Get metrics of a specific type."""
        if metric_type not in self.metrics_store:
            return []
        
        metrics = list(self.metrics_store[metric_type])
        
        # Filter by time
        if since:
            metrics = [m for m in metrics if m.timestamp >= since]
        
        # Apply limit
        if limit:
            metrics = metrics[-limit:]
        
        return metrics
    
    def get_latest_metric(self, metric_type: MetricType) -> Optional[PerformanceMetric]:
        """Get the latest metric of a specific type."""
        metrics = self.get_metrics(metric_type, limit=1)
        return metrics[0] if metrics else None


class PerformanceAnalyzer:
    """Analyzes performance metrics and generates insights."""
    
    def __init__(self, metrics_collector: MetricsCollector):
        self.metrics_collector = metrics_collector
        self.performance_targets = {}
        self.trend_analysis_window = 100  # Number of metrics to analyze for trends
        
    def add_performance_target(self, target: PerformanceTarget):
        """Add a performance target for monitoring."""
        self.performance_targets[target.target_id] = target
    
    def analyze_current_performance(self) -> Dict[str, Any]:
        """Analyze current performance across all metrics."""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'metric_summaries': {},
            'target_compliance': {},
            'trend_analysis': {},
            'recommendations': []
        }
        
        # Analyze each metric type
        for metric_type in MetricType:
            metrics = self.metrics_collector.get_metrics(metric_type, limit=self.trend_analysis_window)
            
            if metrics:
                analysis['metric_summaries'][metric_type.value] = self._summarize_metrics(metrics)
                analysis['trend_analysis'][metric_type.value] = self._analyze_trends(metrics)
        
        # Check target compliance
        for target_id, target in self.performance_targets.items():
            compliance = self._check_target_compliance(target)
            analysis['target_compliance'][target_id] = compliance
        
        # Generate recommendations
        analysis['recommendations'] = self._generate_recommendations(analysis)
        
        return analysis
    
    def _summarize_metrics(self, metrics: List[PerformanceMetric]) -> Dict[str, Any]:
        """Summarize a list of metrics."""
        if not metrics:
            return {}
        
        values = [m.value for m in metrics]
        
        return {
            'count': len(metrics),
            'latest_value': values[-1],
            'average': statistics.mean(values),
            'median': statistics.median(values),
            'min': min(values),
            'max': max(values),
            'std_dev': statistics.stdev(values) if len(values) > 1 else 0,
            'p95': sorted(values)[int(len(values) * 0.95) - 1] if len(values) > 1 else values[0],
            'time_range': {
                'start': metrics[0].timestamp.isoformat(),
                'end': metrics[-1].timestamp.isoformat()
            }
        }
    
    def _analyze_trends(self, metrics: List[PerformanceMetric]) -> Dict[str, Any]:
        """Analyze trends in metrics."""
        if len(metrics) < 10:
            return {'trend': 'insufficient_data'}
        
        values = [m.value for m in metrics]
        
        # Split into first and second half
        mid_point = len(values) // 2
        first_half = values[:mid_point]
        second_half = values[mid_point:]
        
        first_avg = statistics.mean(first_half)
        second_avg = statistics.mean(second_half)
        
        trend_direction = 'improving' if second_avg < first_avg else 'degrading'
        trend_magnitude = abs(second_avg - first_avg) / first_avg * 100 if first_avg != 0 else 0
        
        # Volatility analysis
        volatility = statistics.stdev(values) / statistics.mean(values) * 100 if statistics.mean(values) != 0 else 0
        
        return {
            'trend': trend_direction,
            'magnitude_percent': trend_magnitude,
            'volatility_percent': volatility,
            'first_half_avg': first_avg,
            'second_half_avg': second_avg,
            'data_points': len(values)
        }
    
    def _check_target_compliance(self, target: PerformanceTarget) -> Dict[str, Any]:
        """Check if a performance target is being met."""
        latest_metric = self.metrics_collector.get_latest_metric(target.metric_type)
        
        if not latest_metric:
            return {
                'compliant': False,
                'reason': 'no_data',
                'target_value': target.target_value,
                'actual_value': None
            }
        
        actual_value = latest_metric.value
        target_value = target.target_value
        
        # Check compliance based on operator
        if target.comparison_operator == '>':
            compliant = actual_value > target_value
        elif target.comparison_operator == '<':
            compliant = actual_value < target_value
        elif target.comparison_operator == '>=':
            compliant = actual_value >= target_value
        elif target.comparison_operator == '<=':
            compliant = actual_value <= target_value
        elif target.comparison_operator == '==':
            compliant = abs(actual_value - target_value) < 0.001
        else:
            compliant = False
        
        return {
            'compliant': compliant,
            'target_value': target_value,
            'actual_value': actual_value,
            'difference': actual_value - target_value,
            'difference_percent': ((actual_value - target_value) / target_value * 100) if target_value != 0 else 0
        }
    
    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate optimization recommendations based on analysis."""
        recommendations = []
        
        # Check execution time
        exec_time_summary = analysis['metric_summaries'].get('execution_time', {})
        if exec_time_summary:
            avg_time = exec_time_summary.get('average', 0)
            if avg_time > 2000:  # 2 seconds
                recommendations.append(f"⚠️ High execution time ({avg_time:.1f}ms) - consider parallel processing")
            elif avg_time > 1000:  # 1 second
                recommendations.append(f"🔧 Moderate execution time ({avg_time:.1f}ms) - optimization opportunity")
        
        # Check context usage
        context_summary = analysis['metric_summaries'].get('context_usage', {})
        if context_summary:
            avg_usage = context_summary.get('average', 0)
            if avg_usage > 40000:  # 40K tokens
                recommendations.append(f"📝 High context usage ({avg_usage:.0f} tokens) - implement hierarchical loading")
        
        # Check cache efficiency
        cache_summary = analysis['metric_summaries'].get('cache_efficiency', {})
        if cache_summary:
            avg_hit_rate = cache_summary.get('average', 0)
            if avg_hit_rate < 0.5:  # 50% hit rate
                recommendations.append(f"🗄️ Low cache hit rate ({avg_hit_rate:.1%}) - optimize caching strategy")
        
        # Check trends
        for metric_type, trend_data in analysis['trend_analysis'].items():
            if trend_data.get('trend') == 'degrading' and trend_data.get('magnitude_percent', 0) > 10:
                recommendations.append(f"📉 {metric_type.replace('_', ' ').title()} degrading by {trend_data['magnitude_percent']:.1f}%")
        
        return recommendations if recommendations else ["✅ All metrics within acceptable ranges"]


class AlertManager:
    """Manages performance alerts and notifications."""
    
    def __init__(self, analyzer: PerformanceAnalyzer):
        self.analyzer = analyzer
        self.active_alerts = {}
        self.alert_history = deque(maxlen=500)
        self.alert_handlers = []
        
    def register_alert_handler(self, handler: callable):
        """Register an alert handler function."""
        self.alert_handlers.append(handler)
    
    def check_alerts(self):
        """Check for performance alerts."""
        current_time = datetime.now()
        
        # Check each performance target
        for target_id, target in self.analyzer.performance_targets.items():
            compliance = self.analyzer._check_target_compliance(target)
            
            if not compliance['compliant']:
                # Create or update alert
                alert = PerformanceAlert(
                    alert_id=f"{target_id}_{current_time.strftime('%Y%m%d_%H%M%S')}",
                    level=target.alert_level,
                    message=f"{target.description}: {compliance['actual_value']:.2f} {target.comparison_operator} {target.target_value:.2f}",
                    metric_type=target.metric_type,
                    threshold_value=target.target_value,
                    actual_value=compliance['actual_value'],
                    timestamp=current_time
                )
                
                self._trigger_alert(alert)
    
    def _trigger_alert(self, alert: PerformanceAlert):
        """Trigger a performance alert."""
        # Check if similar alert is already active
        similar_active = any(
            a.metric_type == alert.metric_type and 
            a.level == alert.level and 
            not a.resolved
            for a in self.active_alerts.values()
        )
        
        if not similar_active:
            self.active_alerts[alert.alert_id] = alert
            self.alert_history.append(alert)
            
            # Notify handlers
            for handler in self.alert_handlers:
                try:
                    handler(alert)
                except Exception as e:
                    logger.error(f"Alert handler error: {e}")
    
    def resolve_alert(self, alert_id: str):
        """Resolve an active alert."""
        if alert_id in self.active_alerts:
            self.active_alerts[alert_id].resolved = True
            del self.active_alerts[alert_id]
    
    def get_active_alerts(self) -> List[PerformanceAlert]:
        """Get all active alerts."""
        return list(self.active_alerts.values())
    
    def get_alert_history(self, limit: int = 50) -> List[PerformanceAlert]:
        """Get alert history."""
        return list(self.alert_history)[-limit:]


class PerformanceDashboard:
    """Main performance dashboard coordinator."""
    
    def __init__(self, update_interval: float = 5.0):
        self.metrics_collector = MetricsCollector()
        self.analyzer = PerformanceAnalyzer(self.metrics_collector)
        self.alert_manager = AlertManager(self.analyzer)
        self.update_interval = update_interval
        self.dashboard_active = False
        
        # Register default collectors
        self._register_default_collectors()
        
        # Register default performance targets
        self._register_default_targets()
        
        # Register default alert handler
        self.alert_manager.register_alert_handler(self._console_alert_handler)
    
    def _register_default_collectors(self):
        """Register default metric collectors."""
        
        def collect_execution_time():
            # Simulate execution time collection
            import random
            return {
                'value': random.uniform(100, 1000),  # 100-1000ms
                'context': {'operation': 'framework_operation'},
                'tags': ['execution', 'performance']
            }
        
        def collect_context_usage():
            # Simulate context usage collection
            import random
            return {
                'value': random.uniform(10000, 45000),  # 10-45K tokens
                'context': {'type': 'token_count'},
                'tags': ['context', 'tokens']
            }
        
        def collect_cache_efficiency():
            # Simulate cache efficiency collection
            import random
            return {
                'value': random.uniform(0.4, 0.9),  # 40-90% hit rate
                'context': {'cache_type': 'intelligent_cache'},
                'tags': ['cache', 'efficiency']
            }
        
        def collect_system_resources():
            # Collect actual system resources if available
            try:
                import psutil
                return {
                    'value': psutil.cpu_percent(),
                    'context': {
                        'memory_percent': psutil.virtual_memory().percent,
                        'cpu_count': psutil.cpu_count()
                    },
                    'tags': ['system', 'resources']
                }
            except ImportError:
                import random
                return {
                    'value': random.uniform(20, 80),
                    'context': {'memory_percent': random.uniform(30, 70)},
                    'tags': ['system', 'resources']
                }
        
        # Register collectors
        self.metrics_collector.register_collector(MetricType.EXECUTION_TIME, collect_execution_time)
        self.metrics_collector.register_collector(MetricType.CONTEXT_USAGE, collect_context_usage)
        self.metrics_collector.register_collector(MetricType.CACHE_EFFICIENCY, collect_cache_efficiency)
        self.metrics_collector.register_collector(MetricType.SYSTEM_RESOURCES, collect_system_resources)
    
    def _register_default_targets(self):
        """Register default performance targets."""
        targets = [
            PerformanceTarget(
                target_id="execution_time_target",
                metric_type=MetricType.EXECUTION_TIME,
                target_value=2000.0,  # 2 seconds
                comparison_operator="<",
                description="Execution time should be under 2 seconds",
                alert_level=AlertLevel.WARNING
            ),
            PerformanceTarget(
                target_id="context_usage_target",
                metric_type=MetricType.CONTEXT_USAGE,
                target_value=40000.0,  # 40K tokens
                comparison_operator="<",
                description="Context usage should be under 40K tokens",
                alert_level=AlertLevel.WARNING
            ),
            PerformanceTarget(
                target_id="cache_efficiency_target",
                metric_type=MetricType.CACHE_EFFICIENCY,
                target_value=0.7,  # 70% hit rate
                comparison_operator=">",
                description="Cache hit rate should be above 70%",
                alert_level=AlertLevel.INFO
            ),
            PerformanceTarget(
                target_id="system_resources_target",
                metric_type=MetricType.SYSTEM_RESOURCES,
                target_value=80.0,  # 80% CPU
                comparison_operator="<",
                description="CPU usage should be under 80%",
                alert_level=AlertLevel.CRITICAL
            )
        ]
        
        for target in targets:
            self.analyzer.add_performance_target(target)
    
    def _console_alert_handler(self, alert: PerformanceAlert):
        """Default console alert handler."""
        level_icons = {
            AlertLevel.INFO: "ℹ️",
            AlertLevel.WARNING: "⚠️",
            AlertLevel.CRITICAL: "🚨"
        }
        
        icon = level_icons.get(alert.level, "❓")
        timestamp = alert.timestamp.strftime("%H:%M:%S")
        
        print(f"[{timestamp}] {icon} {alert.level.value.upper()}: {alert.message}")
    
    def start_dashboard(self):
        """Start the performance dashboard."""
        self.dashboard_active = True
        
        # Start metrics collection
        self.metrics_collector.start_collection(interval_seconds=1.0)
        
        # Start dashboard update loop
        def dashboard_loop():
            while self.dashboard_active:
                self._update_dashboard()
                time.sleep(self.update_interval)
        
        dashboard_thread = threading.Thread(target=dashboard_loop, daemon=True)
        dashboard_thread.start()
        
        logger.info(f"Performance dashboard started with {self.update_interval}s update interval")
    
    def stop_dashboard(self):
        """Stop the performance dashboard."""
        self.dashboard_active = False
        self.metrics_collector.stop_collection()
        logger.info("Performance dashboard stopped")
    
    def _update_dashboard(self):
        """Update dashboard display."""
        # Check for alerts
        self.alert_manager.check_alerts()
        
        # Get current analysis
        analysis = self.analyzer.analyze_current_performance()
        
        # Display dashboard
        self._display_dashboard(analysis)
    
    def _display_dashboard(self, analysis: Dict[str, Any]):
        """Display the performance dashboard."""
        print("\n" + "="*80)
        print("🚀 PERFORMANCE DASHBOARD")
        print("="*80)
        
        # Display current metrics
        print("\n📊 Current Metrics:")
        for metric_type, summary in analysis['metric_summaries'].items():
            if summary:
                latest = summary.get('latest_value', 0)
                avg = summary.get('average', 0)
                p95 = summary.get('p95', 0)
                
                metric_display = metric_type.replace('_', ' ').title()
                print(f"  {metric_display}:")
                print(f"    Latest: {latest:.2f} | Average: {avg:.2f} | P95: {p95:.2f}")
        
        # Display target compliance
        print("\n🎯 Target Compliance:")
        for target_id, compliance in analysis['target_compliance'].items():
            if compliance:
                status = "✅ PASS" if compliance['compliant'] else "❌ FAIL"
                target_val = compliance['target_value']
                actual_val = compliance['actual_value']
                print(f"  {target_id}: {status} (Target: {target_val:.2f}, Actual: {actual_val:.2f})")
        
        # Display active alerts
        active_alerts = self.alert_manager.get_active_alerts()
        if active_alerts:
            print(f"\n🚨 Active Alerts ({len(active_alerts)}):")
            for alert in active_alerts[-5:]:  # Show last 5
                print(f"  {alert.level.value.upper()}: {alert.message}")
        
        # Display recommendations
        recommendations = analysis.get('recommendations', [])
        if recommendations:
            print("\n💡 Recommendations:")
            for rec in recommendations[:3]:  # Show top 3
                print(f"  {rec}")
        
        print("="*80)
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Get comprehensive dashboard data."""
        analysis = self.analyzer.analyze_current_performance()
        
        return {
            'analysis': analysis,
            'active_alerts': [asdict(alert) for alert in self.alert_manager.get_active_alerts()],
            'alert_history': [asdict(alert) for alert in self.alert_manager.get_alert_history(10)],
            'targets': {tid: asdict(target) for tid, target in self.analyzer.performance_targets.items()},
            'dashboard_status': 'active' if self.dashboard_active else 'inactive'
        }
    
    def save_dashboard_snapshot(self, output_path: Optional[Path] = None) -> Path:
        """Save dashboard snapshot to file."""
        if output_path is None:
            output_path = Path("reports/performance") / f"dashboard_snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        dashboard_data = self.get_dashboard_data()
        
        with open(output_path, 'w') as f:
            json.dump(dashboard_data, f, indent=2, default=str)
        
        logger.info(f"Dashboard snapshot saved to: {output_path}")
        return output_path


def demonstrate_performance_dashboard():
    """Demonstrate performance dashboard capabilities."""
    print("📊 Performance Dashboard Demonstration")
    print("=" * 60)
    
    # Initialize dashboard
    dashboard = PerformanceDashboard(update_interval=2.0)
    
    # Start dashboard
    dashboard.start_dashboard()
    
    print("🚀 Dashboard started - monitoring performance...")
    print("   Press Ctrl+C to stop monitoring")
    
    try:
        # Run for demonstration
        time.sleep(15)  # Monitor for 15 seconds
        
        # Save snapshot
        snapshot_path = dashboard.save_dashboard_snapshot()
        print(f"📸 Dashboard snapshot saved to: {snapshot_path}")
        
    except KeyboardInterrupt:
        print("\n⏹️  Monitoring stopped by user")
    
    finally:
        # Stop dashboard
        dashboard.stop_dashboard()
        print("✅ Performance dashboard demonstration complete")
    
    return 0


if __name__ == "__main__":
    exit_code = demonstrate_performance_dashboard()
    exit(exit_code)