"""
Prometheus Performance Monitor

This module provides real-time performance monitoring with Prometheus metrics
integration for comprehensive system observability.
"""

import time
import psutil
import threading
from typing import Dict, Any, Optional, List, Callable
from datetime import datetime
from contextlib import contextmanager
from dataclasses import dataclass

try:
    from prometheus_client import (
        Counter, Histogram, Gauge, Summary, CollectorRegistry,
        start_http_server, generate_latest, CONTENT_TYPE_LATEST
    )
    PROMETHEUS_AVAILABLE = True
except ImportError:
    PROMETHEUS_AVAILABLE = False
    # Mock classes for when prometheus_client is not available
    class MockMetric:
        def __init__(self, *args, **kwargs):
            pass
        def inc(self, *args, **kwargs):
            pass
        def observe(self, *args, **kwargs):
            pass
        def set(self, *args, **kwargs):
            pass
        def labels(self, *args, **kwargs):
            return self
    
    Counter = Histogram = Gauge = Summary = MockMetric
    CollectorRegistry = MockMetric


@dataclass
class SystemMetrics:
    """Container for system-level metrics"""
    cpu_percent: float
    memory_used_mb: float
    memory_percent: float
    disk_usage_percent: float
    network_bytes_sent: int
    network_bytes_recv: int
    timestamp: datetime


class PrometheusPerformanceMonitor:
    """Real-time performance monitoring with Prometheus integration"""
    
    def __init__(self, registry: Optional[CollectorRegistry] = None, port: int = 8000):
        self.registry = registry or CollectorRegistry()
        self.port = port
        self.monitoring_active = False
        self._monitoring_thread = None
        
        # Initialize Prometheus metrics
        self._init_prometheus_metrics()
        
        # System monitoring state
        self.process = psutil.Process()
        self._last_network_stats = None
        
        # Internal tracking
        self.system_metrics_history: List[SystemMetrics] = []
        self.max_history_size = 1000
    
    def _init_prometheus_metrics(self):
        """Initialize Prometheus metrics collectors"""
        # Command execution metrics
        self.command_duration = Histogram(
            'command_execution_duration_seconds',
            'Duration of command executions',
            ['command_name', 'status'],
            registry=self.registry
        )
        
        self.command_counter = Counter(
            'command_executions_total',
            'Total number of command executions',
            ['command_name', 'status'],
            registry=self.registry
        )
        
        # System resource metrics
        self.cpu_usage = Gauge(
            'system_cpu_usage_percent',
            'Current CPU usage percentage',
            registry=self.registry
        )
        
        self.memory_usage = Gauge(
            'system_memory_usage_mb',
            'Current memory usage in MB',
            registry=self.registry
        )
        
        self.memory_percent = Gauge(
            'system_memory_usage_percent',
            'Current memory usage percentage',
            registry=self.registry
        )
        
        self.disk_usage = Gauge(
            'system_disk_usage_percent',
            'Current disk usage percentage',
            registry=self.registry
        )
        
        # Network metrics
        self.network_bytes_sent = Counter(
            'network_bytes_sent_total',
            'Total network bytes sent',
            registry=self.registry
        )
        
        self.network_bytes_recv = Counter(
            'network_bytes_received_total',
            'Total network bytes received',
            registry=self.registry
        )
        
        # Performance metrics
        self.cache_hit_ratio = Gauge(
            'cache_hit_ratio',
            'Current cache hit ratio',
            ['cache_type'],
            registry=self.registry
        )
        
        self.context_compression_ratio = Gauge(
            'context_compression_ratio',
            'Context window compression efficiency',
            registry=self.registry
        )
        
        # Component loading metrics
        self.component_load_duration = Summary(
            'component_load_duration_seconds',
            'Duration of component loading operations',
            ['component_name'],
            registry=self.registry
        )
        
        self.active_components = Gauge(
            'active_components_total',
            'Number of currently active components',
            registry=self.registry
        )
    
    def start_monitoring(self):
        """Start background system monitoring"""
        if self.monitoring_active:
            return
        
        self.monitoring_active = True
        self._monitoring_thread = threading.Thread(
            target=self._monitor_system_metrics,
            daemon=True
        )
        self._monitoring_thread.start()
        
        # Initialize network baseline
        self._last_network_stats = psutil.net_io_counters()
    
    def stop_monitoring(self):
        """Stop background system monitoring"""
        self.monitoring_active = False
        if self._monitoring_thread:
            self._monitoring_thread.join(timeout=2.0)
    
    def _monitor_system_metrics(self):
        """Background thread for continuous system monitoring"""
        while self.monitoring_active:
            try:
                # Collect system metrics
                cpu_percent = psutil.cpu_percent(interval=1.0)
                memory = psutil.virtual_memory()
                disk = psutil.disk_usage('/')
                
                # Update Prometheus gauges
                self.cpu_usage.set(cpu_percent)
                self.memory_usage.set(memory.used / 1024 / 1024)  # Convert to MB
                self.memory_percent.set(memory.percent)
                self.disk_usage.set(disk.percent)
                
                # Network metrics
                current_network = psutil.net_io_counters()
                if self._last_network_stats:
                    bytes_sent_delta = current_network.bytes_sent - self._last_network_stats.bytes_sent
                    bytes_recv_delta = current_network.bytes_recv - self._last_network_stats.bytes_recv
                    
                    self.network_bytes_sent.inc(bytes_sent_delta)
                    self.network_bytes_recv.inc(bytes_recv_delta)
                
                self._last_network_stats = current_network
                
                # Store metrics history
                metrics = SystemMetrics(
                    cpu_percent=cpu_percent,
                    memory_used_mb=memory.used / 1024 / 1024,
                    memory_percent=memory.percent,
                    disk_usage_percent=disk.percent,
                    network_bytes_sent=current_network.bytes_sent,
                    network_bytes_recv=current_network.bytes_recv,
                    timestamp=datetime.now()
                )
                
                self._add_to_history(metrics)
                
            except Exception as e:
                print(f"Error collecting system metrics: {e}")
            
            time.sleep(5.0)  # Collect metrics every 5 seconds
    
    def _add_to_history(self, metrics: SystemMetrics):
        """Add metrics to history with size limit"""
        self.system_metrics_history.append(metrics)
        if len(self.system_metrics_history) > self.max_history_size:
            self.system_metrics_history.pop(0)
    
    @contextmanager
    def measure_command(self, command_name: str):
        """Context manager for measuring command execution"""
        start_time = time.time()
        status = 'success'
        
        try:
            yield
        except Exception as e:
            status = 'error'
            raise
        finally:
            duration = time.time() - start_time
            
            # Record metrics
            self.command_duration.labels(
                command_name=command_name,
                status=status
            ).observe(duration)
            
            self.command_counter.labels(
                command_name=command_name,
                status=status
            ).inc()
    
    def record_cache_performance(self, cache_type: str, hit_ratio: float):
        """Record cache hit ratio"""
        self.cache_hit_ratio.labels(cache_type=cache_type).set(hit_ratio)
    
    def record_context_compression(self, compression_ratio: float):
        """Record context window compression ratio"""
        self.context_compression_ratio.set(compression_ratio)
    
    def measure_component_loading(self, component_name: str):
        """Context manager for measuring component loading"""
        return self.component_load_duration.labels(component_name=component_name).time()
    
    def update_active_components(self, count: int):
        """Update the count of active components"""
        self.active_components.set(count)
    
    def get_current_system_metrics(self) -> SystemMetrics:
        """Get current system metrics snapshot"""
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        network = psutil.net_io_counters()
        
        return SystemMetrics(
            cpu_percent=cpu_percent,
            memory_used_mb=memory.used / 1024 / 1024,
            memory_percent=memory.percent,
            disk_usage_percent=disk.percent,
            network_bytes_sent=network.bytes_sent,
            network_bytes_recv=network.bytes_recv,
            timestamp=datetime.now()
        )
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get comprehensive metrics summary"""
        if not self.system_metrics_history:
            return {"error": "No metrics history available"}
        
        recent_metrics = self.system_metrics_history[-10:]  # Last 10 entries
        
        avg_cpu = sum(m.cpu_percent for m in recent_metrics) / len(recent_metrics)
        avg_memory = sum(m.memory_used_mb for m in recent_metrics) / len(recent_metrics)
        avg_memory_percent = sum(m.memory_percent for m in recent_metrics) / len(recent_metrics)
        
        return {
            "current_metrics": self.get_current_system_metrics().__dict__,
            "averages_last_10": {
                "cpu_percent": avg_cpu,
                "memory_used_mb": avg_memory,
                "memory_percent": avg_memory_percent
            },
            "history_size": len(self.system_metrics_history),
            "monitoring_active": self.monitoring_active,
            "prometheus_available": PROMETHEUS_AVAILABLE
        }
    
    def export_metrics(self) -> str:
        """Export Prometheus metrics in text format"""
        if not PROMETHEUS_AVAILABLE:
            return "# Prometheus client not available\n"
        
        return generate_latest(self.registry).decode('utf-8')
    
    def start_http_server(self):
        """Start Prometheus HTTP metrics server"""
        if not PROMETHEUS_AVAILABLE:
            print("Prometheus client not available. Cannot start HTTP server.")
            return False
        
        try:
            start_http_server(self.port, registry=self.registry)
            print(f"Prometheus metrics server started on port {self.port}")
            return True
        except Exception as e:
            print(f"Failed to start Prometheus server: {e}")
            return False
    
    def get_performance_alerts(self) -> List[Dict[str, Any]]:
        """Check for performance issues and return alerts"""
        alerts = []
        current = self.get_current_system_metrics()
        
        # CPU usage alert
        if current.cpu_percent > 80:
            alerts.append({
                "type": "high_cpu_usage",
                "severity": "warning",
                "value": current.cpu_percent,
                "threshold": 80,
                "message": f"High CPU usage: {current.cpu_percent:.1f}%"
            })
        
        # Memory usage alert
        if current.memory_percent > 85:
            alerts.append({
                "type": "high_memory_usage",
                "severity": "critical" if current.memory_percent > 95 else "warning",
                "value": current.memory_percent,
                "threshold": 85,
                "message": f"High memory usage: {current.memory_percent:.1f}%"
            })
        
        # Disk usage alert
        if current.disk_usage_percent > 90:
            alerts.append({
                "type": "high_disk_usage",
                "severity": "critical" if current.disk_usage_percent > 95 else "warning",
                "value": current.disk_usage_percent,
                "threshold": 90,
                "message": f"High disk usage: {current.disk_usage_percent:.1f}%"
            })
        
        return alerts


class MetricsCollector:
    """Simplified metrics collector for environments without Prometheus"""
    
    def __init__(self):
        self.metrics: Dict[str, List[float]] = {}
        self.counters: Dict[str, int] = {}
        self.gauges: Dict[str, float] = {}
        self.start_time = time.time()
    
    def record_duration(self, name: str, duration: float):
        """Record a duration measurement"""
        if name not in self.metrics:
            self.metrics[name] = []
        self.metrics[name].append(duration)
    
    def increment_counter(self, name: str, value: int = 1):
        """Increment a counter"""
        if name not in self.counters:
            self.counters[name] = 0
        self.counters[name] += value
    
    def set_gauge(self, name: str, value: float):
        """Set a gauge value"""
        self.gauges[name] = value
    
    def get_summary(self) -> Dict[str, Any]:
        """Get metrics summary"""
        summary = {
            "uptime_seconds": time.time() - self.start_time,
            "counters": self.counters.copy(),
            "gauges": self.gauges.copy(),
            "metrics_summary": {}
        }
        
        for name, values in self.metrics.items():
            if values:
                summary["metrics_summary"][name] = {
                    "count": len(values),
                    "min": min(values),
                    "max": max(values),
                    "avg": sum(values) / len(values),
                    "total": sum(values)
                }
        
        return summary


# Global monitor instance
if PROMETHEUS_AVAILABLE:
    monitor = PrometheusPerformanceMonitor()
else:
    monitor = MetricsCollector()


# Convenience functions
def start_performance_monitoring():
    """Start performance monitoring"""
    if hasattr(monitor, 'start_monitoring'):
        monitor.start_monitoring()


def stop_performance_monitoring():
    """Stop performance monitoring"""
    if hasattr(monitor, 'stop_monitoring'):
        monitor.stop_monitoring()


def measure_command_execution(command_name: str):
    """Get context manager for measuring command execution"""
    if hasattr(monitor, 'measure_command'):
        return monitor.measure_command(command_name)
    else:
        # Fallback for simplified collector
        return _simple_measure_context(command_name)


@contextmanager
def _simple_measure_context(name: str):
    """Simple measurement context for fallback collector"""
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        if hasattr(monitor, 'record_duration'):
            monitor.record_duration(name, duration)


def get_performance_summary() -> Dict[str, Any]:
    """Get performance summary"""
    if hasattr(monitor, 'get_metrics_summary'):
        return monitor.get_metrics_summary()
    elif hasattr(monitor, 'get_summary'):
        return monitor.get_summary()
    else:
        return {"error": "No monitoring available"}


def record_cache_hit_ratio(cache_type: str, ratio: float):
    """Record cache hit ratio"""
    if hasattr(monitor, 'record_cache_performance'):
        monitor.record_cache_performance(cache_type, ratio)
    elif hasattr(monitor, 'set_gauge'):
        monitor.set_gauge(f"cache_hit_ratio_{cache_type}", ratio)


def export_prometheus_metrics() -> str:
    """Export Prometheus metrics"""
    if hasattr(monitor, 'export_metrics'):
        return monitor.export_metrics()
    else:
        return "# Prometheus not available\n"