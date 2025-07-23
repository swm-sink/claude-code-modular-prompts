# Performance Monitoring Infrastructure

## Comprehensive Performance Monitoring and Analytics

This system provides real-time performance monitoring, metrics collection, and automated optimization recommendations for the Claude Code Modular Prompts framework.

### Core Monitoring System

```python
import time
import json
import threading
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta
from collections import defaultdict, deque
from enum import Enum
import statistics
import logging
from pathlib import Path

class MetricType(Enum):
    COUNTER = "counter"
    GAUGE = "gauge" 
    HISTOGRAM = "histogram"
    TIMER = "timer"

class AlertSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class MetricValue:
    timestamp: float
    value: float
    labels: Dict[str, str] = field(default_factory=dict)

@dataclass 
class PerformanceMetric:
    name: str
    metric_type: MetricType
    description: str
    values: deque = field(default_factory=lambda: deque(maxlen=1000))
    unit: str = ""
    
    def add_value(self, value: float, labels: Dict[str, str] = None):
        """Add a new metric value"""
        self.values.append(MetricValue(
            timestamp=time.time(),
            value=value,
            labels=labels or {}
        ))

@dataclass
class Alert:
    id: str
    metric_name: str
    severity: AlertSeverity
    message: str
    threshold: float
    current_value: float
    timestamp: float
    resolved: bool = False
    resolution_timestamp: Optional[float] = None

class PerformanceMonitor:
    """Comprehensive performance monitoring system"""
    
    def __init__(self, 
                 retention_hours: int = 24,
                 alert_check_interval: int = 30):
        self.metrics: Dict[str, PerformanceMetric] = {}
        self.alerts: Dict[str, Alert] = {}
        self.alert_handlers: List[Callable] = []
        self.retention_hours = retention_hours
        self.alert_check_interval = alert_check_interval
        self.monitoring_enabled = True
        self.lock = threading.RLock()
        
        # Performance targets
        self.targets = {
            'cache_hit_ratio': {'min': 75.0, 'optimal': 85.0},
            'response_time_ms': {'max': 100.0, 'optimal': 50.0},
            'token_reduction_percentage': {'min': 30.0, 'optimal': 45.0},
            'memory_usage_mb': {'max': 200.0, 'warning': 150.0},
            'component_load_time_ms': {'max': 50.0, 'optimal': 20.0}
        }
        
        # Initialize core metrics
        self._initialize_core_metrics()
        
        # Start background monitoring
        self._start_background_monitoring()
    
    def _initialize_core_metrics(self):
        """Initialize core performance metrics"""
        core_metrics = [
            ('cache_hit_ratio', MetricType.GAUGE, 'Cache hit ratio percentage', '%'),
            ('cache_miss_ratio', MetricType.GAUGE, 'Cache miss ratio percentage', '%'),
            ('response_time_ms', MetricType.HISTOGRAM, 'Response time in milliseconds', 'ms'),
            ('token_reduction_percentage', MetricType.GAUGE, 'Token reduction percentage', '%'),
            ('memory_usage_mb', MetricType.GAUGE, 'Memory usage in megabytes', 'MB'),
            ('component_load_time_ms', MetricType.HISTOGRAM, 'Component load time', 'ms'),
            ('parallel_load_count', MetricType.COUNTER, 'Number of parallel loads', 'count'),
            ('optimization_success_rate', MetricType.GAUGE, 'Optimization success rate', '%'),
            ('error_rate', MetricType.GAUGE, 'Error rate percentage', '%'),
            ('throughput_requests_per_second', MetricType.GAUGE, 'Requests per second', 'rps')
        ]
        
        for name, metric_type, description, unit in core_metrics:
            self.register_metric(name, metric_type, description, unit)
    
    def register_metric(self, 
                       name: str, 
                       metric_type: MetricType,
                       description: str,
                       unit: str = ""):
        """Register a new metric"""
        with self.lock:
            if name not in self.metrics:
                self.metrics[name] = PerformanceMetric(
                    name=name,
                    metric_type=metric_type,
                    description=description,
                    unit=unit
                )
                logging.info(f"Registered metric: {name}")
    
    def record_metric(self, 
                     name: str, 
                     value: float,
                     labels: Dict[str, str] = None):
        """Record a metric value"""
        if not self.monitoring_enabled:
            return
        
        with self.lock:
            if name in self.metrics:
                self.metrics[name].add_value(value, labels)
                self._check_alerts(name, value)
            else:
                logging.warning(f"Metric {name} not registered")
    
    def record_timer(self, name: str, labels: Dict[str, str] = None):
        """Return a context manager for timing operations"""
        return TimerContext(self, name, labels)
    
    def get_metric_stats(self, 
                        name: str, 
                        time_window_minutes: int = 10) -> Dict:
        """Get comprehensive statistics for a metric"""
        if name not in self.metrics:
            return {}
        
        metric = self.metrics[name]
        cutoff_time = time.time() - (time_window_minutes * 60)
        
        # Filter values within time window
        recent_values = [
            mv.value for mv in metric.values 
            if mv.timestamp >= cutoff_time
        ]
        
        if not recent_values:
            return {'status': 'no_recent_data'}
        
        return {
            'name': name,
            'current_value': recent_values[-1],
            'count': len(recent_values),
            'min': min(recent_values),
            'max': max(recent_values),
            'mean': statistics.mean(recent_values),
            'median': statistics.median(recent_values),
            'p95': self._percentile(recent_values, 95),
            'p99': self._percentile(recent_values, 99),
            'std_dev': statistics.stdev(recent_values) if len(recent_values) > 1 else 0,
            'unit': metric.unit,
            'time_window_minutes': time_window_minutes
        }
    
    def get_performance_dashboard(self) -> Dict:
        """Get comprehensive performance dashboard"""
        dashboard = {
            'timestamp': datetime.now().isoformat(),
            'monitoring_status': 'active' if self.monitoring_enabled else 'disabled',
            'targets_status': self._check_all_targets(),
            'key_metrics': {},
            'alerts': {
                'active_count': len([a for a in self.alerts.values() if not a.resolved]),
                'critical_count': len([
                    a for a in self.alerts.values() 
                    if not a.resolved and a.severity == AlertSeverity.CRITICAL
                ]),
                'recent_alerts': self._get_recent_alerts(hours=1)
            },
            'performance_trends': self._analyze_performance_trends(),
            'system_health': self._assess_system_health()
        }
        
        # Get stats for key metrics
        key_metrics = [
            'cache_hit_ratio', 'response_time_ms', 'token_reduction_percentage',
            'memory_usage_mb', 'error_rate', 'throughput_requests_per_second'
        ]
        
        for metric_name in key_metrics:
            dashboard['key_metrics'][metric_name] = self.get_metric_stats(metric_name)
        
        return dashboard
    
    def _check_all_targets(self) -> Dict:
        """Check all performance targets"""
        target_status = {}
        
        for metric_name, targets in self.targets.items():
            stats = self.get_metric_stats(metric_name, 5)  # 5 minute window
            
            if 'current_value' not in stats:
                target_status[metric_name] = {'status': 'no_data'}
                continue
            
            current_value = stats['current_value']
            status = {'current_value': current_value}
            
            # Check minimum targets
            if 'min' in targets:
                status['min_target'] = targets['min']
                status['min_met'] = current_value >= targets['min']
            
            # Check maximum targets  
            if 'max' in targets:
                status['max_target'] = targets['max']
                status['max_met'] = current_value <= targets['max']
            
            # Check optimal targets
            if 'optimal' in targets:
                status['optimal_target'] = targets['optimal']
                if 'min' in targets:
                    status['optimal_met'] = current_value >= targets['optimal']
                else:
                    status['optimal_met'] = current_value <= targets['optimal']
            
            target_status[metric_name] = status
        
        return target_status
    
    def _analyze_performance_trends(self) -> Dict:
        """Analyze performance trends over time"""
        trends = {}
        
        key_metrics = ['cache_hit_ratio', 'response_time_ms', 'token_reduction_percentage']
        
        for metric_name in key_metrics:
            if metric_name not in self.metrics:
                continue
            
            # Get data for last hour
            metric = self.metrics[metric_name]
            cutoff_time = time.time() - 3600  # 1 hour
            
            recent_values = [
                mv.value for mv in metric.values 
                if mv.timestamp >= cutoff_time
            ]
            
            if len(recent_values) < 5:
                trends[metric_name] = {'status': 'insufficient_data'}
                continue
            
            # Calculate trend direction
            half_point = len(recent_values) // 2
            first_half_avg = statistics.mean(recent_values[:half_point])
            second_half_avg = statistics.mean(recent_values[half_point:])
            
            change_percentage = ((second_half_avg - first_half_avg) / first_half_avg) * 100
            
            trends[metric_name] = {
                'trend_direction': 'improving' if change_percentage > 2 else 'stable' if abs(change_percentage) <= 2 else 'declining',
                'change_percentage': round(change_percentage, 2),
                'current_value': recent_values[-1],
                'hour_ago_value': recent_values[0],
                'volatility': 'high' if statistics.stdev(recent_values) > statistics.mean(recent_values) * 0.1 else 'low'
            }
        
        return trends
    
    def _assess_system_health(self) -> Dict:
        """Assess overall system health"""
        target_status = self._check_all_targets()
        active_alerts = len([a for a in self.alerts.values() if not a.resolved])
        critical_alerts = len([
            a for a in self.alerts.values() 
            if not a.resolved and a.severity == AlertSeverity.CRITICAL
        ])
        
        # Calculate health score (0-100)
        health_score = 100
        
        # Deduct for missed targets
        for metric, status in target_status.items():
            if 'min_met' in status and not status['min_met']:
                health_score -= 15
            if 'max_met' in status and not status['max_met']:
                health_score -= 15
        
        # Deduct for alerts
        health_score -= (active_alerts * 5)
        health_score -= (critical_alerts * 15)
        
        health_score = max(0, health_score)
        
        # Determine health status
        if health_score >= 90:
            health_status = 'excellent'
        elif health_score >= 75:
            health_status = 'good'
        elif health_score >= 50:
            health_status = 'fair'
        else:
            health_status = 'poor'
        
        return {
            'health_score': health_score,
            'health_status': health_status,
            'active_alerts': active_alerts,
            'critical_alerts': critical_alerts,
            'targets_met': sum(1 for status in target_status.values() 
                             if status.get('min_met', True) and status.get('max_met', True)),
            'total_targets': len(target_status),
            'recommendations': self._generate_health_recommendations(health_score, target_status)
        }
    
    def _generate_health_recommendations(self, health_score: int, target_status: Dict) -> List[str]:
        """Generate health improvement recommendations"""
        recommendations = []
        
        if health_score < 75:
            # Check specific issues
            cache_status = target_status.get('cache_hit_ratio', {})
            if cache_status.get('min_met') == False:
                recommendations.append("Cache hit ratio below target - consider increasing cache size or reviewing component priorities")
            
            response_status = target_status.get('response_time_ms', {})
            if response_status.get('max_met') == False:
                recommendations.append("Response time exceeds target - enable parallel loading and optimize hot components")
            
            token_status = target_status.get('token_reduction_percentage', {})
            if token_status.get('min_met') == False:
                recommendations.append("Token reduction below target - review optimization strategies and enable aggressive compression")
            
            memory_status = target_status.get('memory_usage_mb', {})
            if memory_status.get('max_met') == False:
                recommendations.append("Memory usage high - implement cache eviction and reduce component sizes")
        
        if not recommendations:
            recommendations.append("System performing well - continue monitoring")
        
        return recommendations
    
    def _check_alerts(self, metric_name: str, value: float):
        """Check if metric value triggers alerts"""
        if metric_name not in self.targets:
            return
        
        targets = self.targets[metric_name]
        alert_triggered = False
        severity = AlertSeverity.LOW
        message = ""
        threshold = 0.0
        
        # Check for threshold violations
        if 'max' in targets and value > targets['max']:
            alert_triggered = True
            severity = AlertSeverity.HIGH if value > targets['max'] * 1.2 else AlertSeverity.MEDIUM
            message = f"{metric_name} exceeds maximum threshold"
            threshold = targets['max']
        
        elif 'min' in targets and value < targets['min']:
            alert_triggered = True
            severity = AlertSeverity.HIGH if value < targets['min'] * 0.8 else AlertSeverity.MEDIUM
            message = f"{metric_name} below minimum threshold"  
            threshold = targets['min']
        
        if alert_triggered:
            alert_id = f"{metric_name}_{int(time.time())}"
            alert = Alert(
                id=alert_id,
                metric_name=metric_name,
                severity=severity,
                message=message,
                threshold=threshold,
                current_value=value,
                timestamp=time.time()
            )
            
            self.alerts[alert_id] = alert
            self._trigger_alert_handlers(alert)
    
    def _trigger_alert_handlers(self, alert: Alert):
        """Trigger all registered alert handlers"""
        for handler in self.alert_handlers:
            try:
                handler(alert)
            except Exception as e:
                logging.error(f"Alert handler failed: {e}")
    
    def add_alert_handler(self, handler: Callable[[Alert], None]):
        """Add an alert handler function"""
        self.alert_handlers.append(handler)
    
    def resolve_alert(self, alert_id: str):
        """Resolve an active alert"""
        if alert_id in self.alerts and not self.alerts[alert_id].resolved:
            self.alerts[alert_id].resolved = True
            self.alerts[alert_id].resolution_timestamp = time.time()
    
    def _get_recent_alerts(self, hours: int = 1) -> List[Dict]:
        """Get recent alerts within time window"""
        cutoff_time = time.time() - (hours * 3600)
        
        recent_alerts = [
            asdict(alert) for alert in self.alerts.values()
            if alert.timestamp >= cutoff_time
        ]
        
        return sorted(recent_alerts, key=lambda x: x['timestamp'], reverse=True)
    
    def _percentile(self, values: List[float], p: int) -> float:
        """Calculate percentile value"""
        if not values:
            return 0.0
        
        sorted_values = sorted(values)
        k = (len(sorted_values) - 1) * (p / 100)
        f = int(k)
        c = k - f
        
        if f == len(sorted_values) - 1:
            return sorted_values[f]
        else:
            return sorted_values[f] * (1 - c) + sorted_values[f + 1] * c
    
    def _start_background_monitoring(self):
        """Start background monitoring tasks"""
        def cleanup_old_data():
            """Cleanup old metric data"""
            while self.monitoring_enabled:
                try:
                    cutoff_time = time.time() - (self.retention_hours * 3600)
                    
                    with self.lock:
                        for metric in self.metrics.values():
                            # Remove old values
                            while (metric.values and 
                                   metric.values[0].timestamp < cutoff_time):
                                metric.values.popleft()
                        
                        # Clean up old resolved alerts
                        old_alerts = [
                            alert_id for alert_id, alert in self.alerts.items()
                            if (alert.resolved and 
                                alert.resolution_timestamp and
                                alert.resolution_timestamp < cutoff_time)
                        ]
                        
                        for alert_id in old_alerts:
                            del self.alerts[alert_id]
                    
                    time.sleep(self.alert_check_interval * 60)  # Check every N minutes
                
                except Exception as e:
                    logging.error(f"Background monitoring error: {e}")
                    time.sleep(60)
        
        # Start cleanup thread
        cleanup_thread = threading.Thread(target=cleanup_old_data, daemon=True)
        cleanup_thread.start()
    
    def export_metrics(self, format: str = 'json') -> str:
        """Export metrics in specified format"""
        if format == 'json':
            return json.dumps(self.get_performance_dashboard(), indent=2)
        elif format == 'prometheus':
            return self._export_prometheus_format()
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def _export_prometheus_format(self) -> str:
        """Export metrics in Prometheus format"""
        lines = []
        
        for metric in self.metrics.values():
            if not metric.values:
                continue
            
            # Add metric metadata
            lines.append(f"# HELP {metric.name} {metric.description}")
            lines.append(f"# TYPE {metric.name} {metric.metric_type.value}")
            
            # Add latest value
            latest_value = metric.values[-1]
            labels = ','.join([f'{k}="{v}"' for k, v in latest_value.labels.items()])
            label_str = f"{{{labels}}}" if labels else ""
            
            lines.append(f"{metric.name}{label_str} {latest_value.value} {int(latest_value.timestamp * 1000)}")
        
        return '\n'.join(lines)
    
    def shutdown(self):
        """Shutdown monitoring system"""
        self.monitoring_enabled = False
        logging.info("Performance monitoring system shutdown")

class TimerContext:
    """Context manager for timing operations"""
    
    def __init__(self, monitor: PerformanceMonitor, metric_name: str, labels: Dict[str, str] = None):
        self.monitor = monitor
        self.metric_name = metric_name
        self.labels = labels or {}
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.start_time:
            duration_ms = (time.time() - self.start_time) * 1000
            self.monitor.record_metric(self.metric_name, duration_ms, self.labels)

class PerformanceProfiler:
    """Advanced performance profiler with component-level insights"""
    
    def __init__(self, monitor: PerformanceMonitor):
        self.monitor = monitor
        self.active_profiles = {}
        self.profile_results = {}
    
    def start_profile(self, profile_name: str):
        """Start a performance profile"""
        self.active_profiles[profile_name] = {
            'start_time': time.time(),
            'operations': [],
            'memory_start': self._get_memory_usage()
        }
    
    def record_operation(self, profile_name: str, operation: str, duration_ms: float):
        """Record an operation within a profile"""
        if profile_name in self.active_profiles:
            self.active_profiles[profile_name]['operations'].append({
                'operation': operation,
                'duration_ms': duration_ms,
                'timestamp': time.time()
            })
    
    def end_profile(self, profile_name: str) -> Dict:
        """End a profile and return results"""
        if profile_name not in self.active_profiles:
            return {}
        
        profile_data = self.active_profiles[profile_name]
        end_time = time.time()
        
        results = {
            'profile_name': profile_name,
            'total_duration_ms': (end_time - profile_data['start_time']) * 1000,
            'operations': profile_data['operations'],
            'memory_usage_mb': self._get_memory_usage() - profile_data['memory_start'],
            'operation_count': len(profile_data['operations']),
            'average_operation_time': statistics.mean([
                op['duration_ms'] for op in profile_data['operations']
            ]) if profile_data['operations'] else 0
        }
        
        self.profile_results[profile_name] = results
        del self.active_profiles[profile_name]
        
        return results
    
    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        try:
            import psutil
            process = psutil.Process()
            return process.memory_info().rss / 1024 / 1024
        except ImportError:
            return 0.0
    
    def get_profile_summary(self) -> Dict:
        """Get summary of all completed profiles"""
        if not self.profile_results:
            return {'status': 'no_profiles'}
        
        return {
            'total_profiles': len(self.profile_results),
            'profiles': list(self.profile_results.keys()),
            'average_duration_ms': statistics.mean([
                p['total_duration_ms'] for p in self.profile_results.values()
            ]),
            'total_operations': sum([
                p['operation_count'] for p in self.profile_results.values()
            ])
        }

# Integration class for the framework
class FrameworkMonitoringIntegration:
    """Integration class for monitoring the Claude Code framework"""
    
    def __init__(self):
        self.monitor = PerformanceMonitor()
        self.profiler = PerformanceProfiler(self.monitor)
        
        # Add default alert handlers
        self.monitor.add_alert_handler(self._log_alert)
        self.monitor.add_alert_handler(self._handle_critical_alerts)
    
    def monitor_cache_operation(self, cache_stats: Dict):
        """Monitor cache operations"""
        if 'hit_ratio' in cache_stats:
            self.monitor.record_metric('cache_hit_ratio', cache_stats['hit_ratio'])
        
        if 'memory_usage_mb' in cache_stats:
            self.monitor.record_metric('memory_usage_mb', cache_stats['memory_usage_mb'])
    
    def monitor_component_loading(self, load_time_ms: float, component_path: str):
        """Monitor component loading performance"""
        self.monitor.record_metric(
            'component_load_time_ms', 
            load_time_ms,
            {'component': component_path}
        )
    
    def monitor_token_optimization(self, optimization_result):
        """Monitor token optimization results"""
        self.monitor.record_metric(
            'token_reduction_percentage',
            optimization_result.reduction_percentage
        )
        
        success_rate = 100.0 if optimization_result.quality_score > 0.8 else 0.0
        self.monitor.record_metric('optimization_success_rate', success_rate)
    
    def monitor_parallel_loading(self, load_count: int, total_time_ms: float):
        """Monitor parallel loading operations"""
        self.monitor.record_metric('parallel_load_count', load_count)
        self.monitor.record_metric('response_time_ms', total_time_ms)
    
    def _log_alert(self, alert: Alert):
        """Log alert to console/file"""
        logging.warning(f"ALERT [{alert.severity.value}]: {alert.message} "
                       f"(current: {alert.current_value}, threshold: {alert.threshold})")
    
    def _handle_critical_alerts(self, alert: Alert):
        """Handle critical alerts"""
        if alert.severity == AlertSeverity.CRITICAL:
            # Could integrate with external alerting systems
            logging.critical(f"CRITICAL ALERT: {alert.message}")
    
    def get_framework_health_report(self) -> Dict:
        """Get comprehensive framework health report"""
        dashboard = self.monitor.get_performance_dashboard()
        profile_summary = self.profiler.get_profile_summary()
        
        return {
            'monitoring_dashboard': dashboard,
            'profiling_summary': profile_summary,
            'framework_optimization_status': self._assess_optimization_status(dashboard),
            'recommendations': self._generate_framework_recommendations(dashboard)
        }
    
    def _assess_optimization_status(self, dashboard: Dict) -> Dict:
        """Assess overall framework optimization status"""
        targets_status = dashboard.get('targets_status', {})
        
        # Check key performance indicators
        cache_optimal = targets_status.get('cache_hit_ratio', {}).get('min_met', False)
        response_optimal = targets_status.get('response_time_ms', {}).get('max_met', False)  
        token_optimal = targets_status.get('token_reduction_percentage', {}).get('min_met', False)
        
        optimization_score = sum([cache_optimal, response_optimal, token_optimal]) / 3 * 100
        
        return {
            'optimization_score': optimization_score,
            'cache_optimization': 'optimal' if cache_optimal else 'needs_improvement',
            'response_optimization': 'optimal' if response_optimal else 'needs_improvement',
            'token_optimization': 'optimal' if token_optimal else 'needs_improvement',
            'overall_status': 'optimal' if optimization_score >= 90 else 'good' if optimization_score >= 70 else 'needs_improvement'
        }
    
    def _generate_framework_recommendations(self, dashboard: Dict) -> List[str]:
        """Generate framework-specific optimization recommendations"""
        recommendations = []
        targets_status = dashboard.get('targets_status', {})
        
        # Cache optimization recommendations
        cache_status = targets_status.get('cache_hit_ratio', {})
        if not cache_status.get('min_met', True):
            recommendations.append("Enable cache preloading for hot components")
            recommendations.append("Increase cache size allocation")
        
        # Response time recommendations  
        response_status = targets_status.get('response_time_ms', {})
        if not response_status.get('max_met', True):
            recommendations.append("Enable parallel component loading")
            recommendations.append("Implement component bundling for related components")
        
        # Token optimization recommendations
        token_status = targets_status.get('token_reduction_percentage', {})
        if not token_status.get('min_met', True):
            recommendations.append("Apply aggressive token optimization strategy")
            recommendations.append("Review component content for redundancy")
        
        return recommendations
    
    def shutdown(self):
        """Shutdown monitoring system"""
        self.monitor.shutdown()

# Usage Example
if __name__ == "__main__":
    # Initialize monitoring
    framework_monitor = FrameworkMonitoringIntegration()
    
    # Example: Monitor a cache operation
    framework_monitor.monitor_cache_operation({
        'hit_ratio': 82.5,
        'memory_usage_mb': 45.2
    })
    
    # Example: Monitor component loading
    framework_monitor.monitor_component_loading(
        25.5, 
        "components/reporting/generate-structured-report.md"
    )
    
    # Get health report
    health_report = framework_monitor.get_framework_health_report()
    print(f"Framework optimization score: {health_report['framework_optimization_status']['optimization_score']}")
    
    # Export metrics
    metrics_json = framework_monitor.monitor.export_metrics('json')
    print("Metrics exported successfully")
    
    # Shutdown
    framework_monitor.shutdown()
```

This monitoring system provides:
- **Real-time performance tracking** with comprehensive metrics collection
- **Intelligent alerting** with severity-based notifications and automatic resolution
- **Performance dashboards** with trend analysis and health scoring
- **Automated recommendations** based on performance patterns and target deviations
- **Profiling capabilities** for detailed component-level performance analysis
- **Multiple export formats** (JSON, Prometheus) for integration with external systems
- **Background cleanup** to prevent memory bloat from metric retention