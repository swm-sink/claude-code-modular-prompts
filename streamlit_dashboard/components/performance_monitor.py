"""
Performance Monitoring and Logging System for Streamlit Dashboard
Provides comprehensive monitoring, logging, and performance tracking capabilities
"""

import streamlit as st
import logging
import time
import psutil
import functools
import json
import os
from typing import Dict, Any, Optional, List, Callable
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict, deque
import threading
import gc


@dataclass
class PerformanceMetric:
    """Represents a performance metric measurement"""
    
    name: str
    value: float
    unit: str
    timestamp: str
    category: str = "general"
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate metric data"""
        if not self.name or self.name.strip() == "":
            raise ValueError("Metric name cannot be empty")
        
        if not isinstance(self.value, (int, float)):
            raise ValueError("Metric value must be numeric")
        
        if not self.unit or self.unit.strip() == "":
            raise ValueError("Metric unit cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PerformanceMetric':
        """Create from dictionary"""
        return cls(**data)


@dataclass
class LogEntry:
    """Represents a log entry with structured data"""
    
    level: str
    message: str
    timestamp: str
    category: str = "general"
    component: str = "unknown"
    user_session: str = "unknown"
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate log entry data"""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if self.level not in valid_levels:
            raise ValueError(f"Invalid log level: {self.level}")
        
        if not self.message or self.message.strip() == "":
            raise ValueError("Log message cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'LogEntry':
        """Create from dictionary"""
        return cls(**data)


class PerformanceMonitor:
    """Comprehensive performance monitoring system"""
    
    def __init__(self, log_dir: Path = None, max_metrics: int = 1000):
        """Initialize performance monitor"""
        self.log_dir = log_dir or Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        
        # Metrics storage
        self.metrics: deque = deque(maxlen=max_metrics)
        self.metrics_by_category: Dict[str, deque] = defaultdict(lambda: deque(maxlen=100))
        
        # Logging setup
        self.logger = self._setup_logging()
        
        # Performance tracking
        self.start_time = time.time()
        self.request_count = 0
        self.error_count = 0
        self.last_gc_time = time.time()
        
        # Thread-safe access
        self.lock = threading.Lock()
        
        # Initialize session tracking
        self.session_id = self._get_session_id()
    
    def _setup_logging(self) -> logging.Logger:
        """Setup structured logging"""
        logger = logging.getLogger("dashboard_performance")
        logger.setLevel(logging.INFO)
        
        # Clear existing handlers
        logger.handlers.clear()
        
        # File handler
        log_file = self.log_dir / f"dashboard_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        
        # Structured formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def _get_session_id(self) -> str:
        """Get or create session ID"""
        if 'session_id' not in st.session_state:
            st.session_state.session_id = f"session_{int(time.time() * 1000)}"
        return st.session_state.session_id
    
    def record_metric(self, name: str, value: float, unit: str, 
                     category: str = "general", metadata: Dict[str, Any] = None):
        """Record a performance metric"""
        with self.lock:
            metric = PerformanceMetric(
                name=name,
                value=value,
                unit=unit,
                timestamp=datetime.now().isoformat(),
                category=category,
                metadata=metadata or {}
            )
            
            self.metrics.append(metric)
            self.metrics_by_category[category].append(metric)
            
            # Log significant metrics
            if category in ["error", "warning"] or value > 1000:
                self.logger.info(f"Metric recorded: {name}={value}{unit} (category: {category})")
    
    def log_event(self, level: str, message: str, category: str = "general", 
                  component: str = "unknown", metadata: Dict[str, Any] = None):
        """Log an event with structured data"""
        log_entry = LogEntry(
            level=level,
            message=message,
            timestamp=datetime.now().isoformat(),
            category=category,
            component=component,
            user_session=self.session_id,
            metadata=metadata or {}
        )
        
        # Log to structured logger
        getattr(self.logger, level.lower())(
            f"[{component}] {message} - Session: {self.session_id}"
        )
        
        # Track error counts
        if level in ["ERROR", "CRITICAL"]:
            self.error_count += 1
    
    def measure_execution_time(self, func: Callable = None, category: str = "performance"):
        """Decorator to measure function execution time"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                
                try:
                    result = func(*args, **kwargs)
                    success = True
                    error_msg = None
                except Exception as e:
                    result = None
                    success = False
                    error_msg = str(e)
                    raise
                finally:
                    execution_time = (time.time() - start_time) * 1000  # Convert to ms
                    
                    # Record metric
                    self.record_metric(
                        name=f"{func.__name__}_execution_time",
                        value=execution_time,
                        unit="ms",
                        category=category,
                        metadata={
                            "function": func.__name__,
                            "success": success,
                            "error": error_msg
                        }
                    )
                    
                    # Log if slow
                    if execution_time > 500:  # 500ms threshold
                        self.log_event(
                            level="WARNING",
                            message=f"Slow execution: {func.__name__} took {execution_time:.2f}ms",
                            category="performance",
                            component=func.__module__,
                            metadata={"execution_time": execution_time}
                        )
                
                return result
            return wrapper
        
        if func is None:
            return decorator
        return decorator(func)
    
    def track_memory_usage(self):
        """Track current memory usage"""
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            
            self.record_metric(
                name="memory_usage",
                value=memory_info.rss / 1024 / 1024,  # Convert to MB
                unit="MB",
                category="system",
                metadata={
                    "virtual_memory": memory_info.vms / 1024 / 1024,
                    "memory_percent": process.memory_percent()
                }
            )
            
            # Track garbage collection
            if time.time() - self.last_gc_time > 60:  # Every minute
                gc_count = gc.get_count()
                self.record_metric(
                    name="gc_objects",
                    value=sum(gc_count),
                    unit="objects",
                    category="system",
                    metadata={"gc_count": gc_count}
                )
                self.last_gc_time = time.time()
                
        except Exception as e:
            self.log_event(
                level="ERROR",
                message=f"Failed to track memory usage: {str(e)}",
                category="monitoring",
                component="performance_monitor"
            )
    
    def track_cpu_usage(self):
        """Track CPU usage"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            
            self.record_metric(
                name="cpu_usage",
                value=cpu_percent,
                unit="percent",
                category="system",
                metadata={
                    "cpu_count": psutil.cpu_count(),
                    "load_avg": os.getloadavg() if hasattr(os, 'getloadavg') else None
                }
            )
            
        except Exception as e:
            self.log_event(
                level="ERROR",
                message=f"Failed to track CPU usage: {str(e)}",
                category="monitoring",
                component="performance_monitor"
            )
    
    def track_streamlit_metrics(self):
        """Track Streamlit-specific metrics"""
        try:
            # Track session state size
            session_state_size = len(st.session_state.keys())
            
            self.record_metric(
                name="session_state_keys",
                value=session_state_size,
                unit="keys",
                category="streamlit",
                metadata={
                    "session_id": self.session_id,
                    "keys": list(st.session_state.keys())
                }
            )
            
            # Track cache usage if available
            if hasattr(st, 'cache_data'):
                cache_stats = getattr(st.cache_data, 'get_stats', lambda: {})()
                if cache_stats:
                    self.record_metric(
                        name="cache_hits",
                        value=cache_stats.get('hits', 0),
                        unit="hits",
                        category="streamlit"
                    )
                    
                    self.record_metric(
                        name="cache_misses",
                        value=cache_stats.get('misses', 0),
                        unit="misses",
                        category="streamlit"
                    )
            
        except Exception as e:
            self.log_event(
                level="ERROR",
                message=f"Failed to track Streamlit metrics: {str(e)}",
                category="monitoring",
                component="performance_monitor"
            )
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get comprehensive metrics summary"""
        with self.lock:
            if not self.metrics:
                return {"total_metrics": 0, "categories": {}}
            
            summary = {
                "total_metrics": len(self.metrics),
                "categories": {},
                "time_range": {
                    "start": self.metrics[0].timestamp,
                    "end": self.metrics[-1].timestamp
                },
                "session_info": {
                    "session_id": self.session_id,
                    "uptime": time.time() - self.start_time,
                    "request_count": self.request_count,
                    "error_count": self.error_count
                }
            }
            
            # Category summaries
            for category, metrics in self.metrics_by_category.items():
                if metrics:
                    category_summary = {
                        "count": len(metrics),
                        "latest_timestamp": metrics[-1].timestamp,
                        "metric_types": list(set(m.name for m in metrics))
                    }
                    
                    # Calculate averages for numeric metrics
                    numeric_metrics = defaultdict(list)
                    for metric in metrics:
                        numeric_metrics[metric.name].append(metric.value)
                    
                    averages = {}
                    for name, values in numeric_metrics.items():
                        averages[name] = {
                            "avg": sum(values) / len(values),
                            "min": min(values),
                            "max": max(values),
                            "count": len(values)
                        }
                    
                    category_summary["averages"] = averages
                    summary["categories"][category] = category_summary
            
            return summary
    
    def get_recent_metrics(self, minutes: int = 10) -> List[PerformanceMetric]:
        """Get metrics from the last N minutes"""
        cutoff_time = datetime.now() - timedelta(minutes=minutes)
        
        recent_metrics = []
        for metric in self.metrics:
            metric_time = datetime.fromisoformat(metric.timestamp)
            if metric_time >= cutoff_time:
                recent_metrics.append(metric)
        
        return recent_metrics
    
    def export_metrics(self, file_path: Path = None) -> str:
        """Export metrics to JSON file"""
        if file_path is None:
            file_path = self.log_dir / f"metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with self.lock:
            metrics_data = {
                "export_timestamp": datetime.now().isoformat(),
                "session_id": self.session_id,
                "summary": self.get_metrics_summary(),
                "metrics": [metric.to_dict() for metric in self.metrics]
            }
            
            with open(file_path, 'w') as f:
                json.dump(metrics_data, f, indent=2)
            
            return str(file_path)
    
    def cleanup_old_logs(self, days: int = 7):
        """Clean up log files older than specified days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        for log_file in self.log_dir.glob("*.log"):
            try:
                file_date = datetime.fromtimestamp(log_file.stat().st_mtime)
                if file_date < cutoff_date:
                    log_file.unlink()
                    self.log_event(
                        level="INFO",
                        message=f"Cleaned up old log file: {log_file.name}",
                        category="maintenance",
                        component="performance_monitor"
                    )
            except Exception as e:
                self.log_event(
                    level="ERROR",
                    message=f"Failed to clean up log file {log_file.name}: {str(e)}",
                    category="maintenance",
                    component="performance_monitor"
                )
    
    def render_monitoring_dashboard(self):
        """Render the monitoring dashboard UI"""
        st.title("📊 Performance Monitoring Dashboard")
        
        # Real-time metrics
        st.subheader("🔄 Real-time Metrics")
        
        # Update metrics
        self.track_memory_usage()
        self.track_cpu_usage()
        self.track_streamlit_metrics()
        
        # Display current system metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            try:
                memory_metrics = [m for m in self.metrics if m.name == "memory_usage"]
                if memory_metrics:
                    latest_memory = memory_metrics[-1]
                    st.metric("Memory Usage", f"{latest_memory.value:.1f} MB")
                else:
                    st.metric("Memory Usage", "N/A")
            except:
                st.metric("Memory Usage", "Error")
        
        with col2:
            try:
                cpu_metrics = [m for m in self.metrics if m.name == "cpu_usage"]
                if cpu_metrics:
                    latest_cpu = cpu_metrics[-1]
                    st.metric("CPU Usage", f"{latest_cpu.value:.1f}%")
                else:
                    st.metric("CPU Usage", "N/A")
            except:
                st.metric("CPU Usage", "Error")
        
        with col3:
            uptime = time.time() - self.start_time
            st.metric("Uptime", f"{uptime/3600:.1f} hours")
        
        with col4:
            st.metric("Error Count", self.error_count)
        
        # Metrics summary
        st.subheader("📈 Metrics Summary")
        
        summary = self.get_metrics_summary()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.json(summary)
        
        with col2:
            st.markdown("**Recent Activity**")
            recent_metrics = self.get_recent_metrics(minutes=5)
            
            if recent_metrics:
                for metric in recent_metrics[-10:]:  # Show last 10
                    st.write(f"• {metric.name}: {metric.value} {metric.unit}")
            else:
                st.info("No recent metrics available")
        
        # Export functionality
        st.subheader("📤 Export & Maintenance")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Export Metrics"):
                try:
                    export_path = self.export_metrics()
                    st.success(f"Metrics exported to: {export_path}")
                except Exception as e:
                    st.error(f"Export failed: {str(e)}")
        
        with col2:
            if st.button("Clean Old Logs"):
                try:
                    self.cleanup_old_logs()
                    st.success("Old logs cleaned up successfully")
                except Exception as e:
                    st.error(f"Cleanup failed: {str(e)}")
        
        with col3:
            if st.button("Generate Test Metrics"):
                # Generate some test metrics for demonstration
                import random
                for i in range(10):
                    self.record_metric(
                        name=f"test_metric_{i}",
                        value=random.uniform(0, 100),
                        unit="units",
                        category="test"
                    )
                st.success("Test metrics generated")
    
    def render(self):
        """Main render method"""
        self.render_monitoring_dashboard()


# Global performance monitor instance
_performance_monitor = None

def get_performance_monitor() -> PerformanceMonitor:
    """Get or create global performance monitor instance"""
    global _performance_monitor
    if _performance_monitor is None:
        _performance_monitor = PerformanceMonitor()
    return _performance_monitor

def track_performance(category: str = "performance"):
    """Decorator for tracking function performance"""
    return get_performance_monitor().measure_execution_time(category=category)

def log_event(level: str, message: str, category: str = "general", 
              component: str = "unknown", metadata: Dict[str, Any] = None):
    """Convenience function for logging events"""
    get_performance_monitor().log_event(level, message, category, component, metadata)

def record_metric(name: str, value: float, unit: str, 
                 category: str = "general", metadata: Dict[str, Any] = None):
    """Convenience function for recording metrics"""
    get_performance_monitor().record_metric(name, value, unit, category, metadata)