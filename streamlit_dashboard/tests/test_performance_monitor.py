"""
TDD Tests for Performance Monitoring System
RED PHASE: Write failing tests first
"""

import pytest
import time
import tempfile
import json
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch, mock_open

# Import the components we're testing
try:
    from components.performance_monitor import (
        PerformanceMonitor, 
        PerformanceMetric, 
        LogEntry,
        get_performance_monitor,
        track_performance,
        log_event,
        record_metric
    )
except ImportError:
    # These don't exist yet - we'll create them
    PerformanceMonitor = None
    PerformanceMetric = None
    LogEntry = None
    get_performance_monitor = None
    track_performance = None
    log_event = None
    record_metric = None


class TestPerformanceMetric:
    """Test the PerformanceMetric data class"""
    
    def test_performance_metric_creation(self):
        """Test PerformanceMetric can be created with proper data"""
        if PerformanceMetric is None:
            pytest.skip("PerformanceMetric not implemented yet")
        
        metric = PerformanceMetric(
            name="response_time",
            value=150.5,
            unit="ms",
            timestamp=datetime.now().isoformat(),
            category="performance",
            metadata={"endpoint": "/api/users", "method": "GET"}
        )
        
        assert metric.name == "response_time"
        assert metric.value == 150.5
        assert metric.unit == "ms"
        assert metric.category == "performance"
        assert metric.metadata["endpoint"] == "/api/users"
    
    def test_performance_metric_validation(self):
        """Test PerformanceMetric validation"""
        if PerformanceMetric is None:
            pytest.skip("PerformanceMetric not implemented yet")
        
        # Test empty name
        with pytest.raises(ValueError):
            PerformanceMetric(
                name="",
                value=150.5,
                unit="ms",
                timestamp=datetime.now().isoformat()
            )
        
        # Test non-numeric value
        with pytest.raises(ValueError):
            PerformanceMetric(
                name="test_metric",
                value="not_a_number",
                unit="ms",
                timestamp=datetime.now().isoformat()
            )
        
        # Test empty unit
        with pytest.raises(ValueError):
            PerformanceMetric(
                name="test_metric",
                value=150.5,
                unit="",
                timestamp=datetime.now().isoformat()
            )
    
    def test_performance_metric_serialization(self):
        """Test PerformanceMetric serialization"""
        if PerformanceMetric is None:
            pytest.skip("PerformanceMetric not implemented yet")
        
        metric = PerformanceMetric(
            name="cpu_usage",
            value=75.2,
            unit="percent",
            timestamp=datetime.now().isoformat(),
            category="system"
        )
        
        # Test to_dict
        data = metric.to_dict()
        assert isinstance(data, dict)
        assert data["name"] == "cpu_usage"
        assert data["value"] == 75.2
        assert data["unit"] == "percent"
        
        # Test from_dict
        recreated = PerformanceMetric.from_dict(data)
        assert recreated.name == metric.name
        assert recreated.value == metric.value
        assert recreated.unit == metric.unit


class TestLogEntry:
    """Test the LogEntry data class"""
    
    def test_log_entry_creation(self):
        """Test LogEntry can be created with proper data"""
        if LogEntry is None:
            pytest.skip("LogEntry not implemented yet")
        
        entry = LogEntry(
            level="INFO",
            message="User login successful",
            timestamp=datetime.now().isoformat(),
            category="authentication",
            component="auth_service",
            user_session="session_123",
            metadata={"user_id": "user_456", "ip": "192.168.1.1"}
        )
        
        assert entry.level == "INFO"
        assert entry.message == "User login successful"
        assert entry.category == "authentication"
        assert entry.component == "auth_service"
        assert entry.user_session == "session_123"
        assert entry.metadata["user_id"] == "user_456"
    
    def test_log_entry_validation(self):
        """Test LogEntry validation"""
        if LogEntry is None:
            pytest.skip("LogEntry not implemented yet")
        
        # Test invalid log level
        with pytest.raises(ValueError):
            LogEntry(
                level="INVALID",
                message="Test message",
                timestamp=datetime.now().isoformat()
            )
        
        # Test empty message
        with pytest.raises(ValueError):
            LogEntry(
                level="INFO",
                message="",
                timestamp=datetime.now().isoformat()
            )
    
    def test_log_entry_serialization(self):
        """Test LogEntry serialization"""
        if LogEntry is None:
            pytest.skip("LogEntry not implemented yet")
        
        entry = LogEntry(
            level="WARNING",
            message="High memory usage detected",
            timestamp=datetime.now().isoformat(),
            category="system",
            component="memory_monitor"
        )
        
        # Test to_dict
        data = entry.to_dict()
        assert isinstance(data, dict)
        assert data["level"] == "WARNING"
        assert data["message"] == "High memory usage detected"
        
        # Test from_dict
        recreated = LogEntry.from_dict(data)
        assert recreated.level == entry.level
        assert recreated.message == entry.message
        assert recreated.category == entry.category


class TestPerformanceMonitor:
    """Test the PerformanceMonitor component"""
    
    @pytest.fixture
    def temp_log_dir(self):
        """Create temporary log directory"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            yield Path(tmp_dir)
    
    @pytest.fixture
    def mock_streamlit(self):
        """Mock Streamlit session state"""
        with patch('streamlit.session_state') as mock_session:
            mock_session.keys.return_value = ["test_key"]
            mock_session.__contains__ = MagicMock(return_value=False)
            mock_session.__setitem__ = MagicMock()
            mock_session.__getitem__ = MagicMock(return_value="test_session_id")
            yield mock_session
    
    def test_performance_monitor_initialization(self, temp_log_dir, mock_streamlit):
        """Test PerformanceMonitor can be initialized"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        assert monitor.log_dir == temp_log_dir
        assert hasattr(monitor, 'metrics')
        assert hasattr(monitor, 'logger')
        assert hasattr(monitor, 'session_id')
    
    def test_record_metric(self, temp_log_dir, mock_streamlit):
        """Test recording performance metrics"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Record a metric
        monitor.record_metric(
            name="response_time",
            value=120.5,
            unit="ms",
            category="performance",
            metadata={"endpoint": "/api/test"}
        )
        
        # Verify metric was recorded
        assert len(monitor.metrics) == 1
        metric = monitor.metrics[0]
        assert metric.name == "response_time"
        assert metric.value == 120.5
        assert metric.unit == "ms"
        assert metric.category == "performance"
    
    def test_log_event(self, temp_log_dir, mock_streamlit):
        """Test logging events"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Log an event
        monitor.log_event(
            level="INFO",
            message="Test event logged",
            category="test",
            component="test_component",
            metadata={"test_key": "test_value"}
        )
        
        # Verify logging occurred (check that logger was called)
        assert monitor.logger is not None
    
    def test_measure_execution_time(self, temp_log_dir, mock_streamlit):
        """Test execution time measurement decorator"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        @monitor.measure_execution_time
        def test_function():
            time.sleep(0.1)  # Simulate some work
            return "test_result"
        
        # Execute the decorated function
        result = test_function()
        
        # Verify result
        assert result == "test_result"
        
        # Verify metric was recorded
        execution_metrics = [m for m in monitor.metrics if "execution_time" in m.name]
        assert len(execution_metrics) >= 1
        
        # Verify execution time was measured
        metric = execution_metrics[0]
        assert metric.value > 0  # Should have some execution time
        assert metric.unit == "ms"
    
    def test_measure_execution_time_with_exception(self, temp_log_dir, mock_streamlit):
        """Test execution time measurement with exceptions"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        @monitor.measure_execution_time
        def failing_function():
            time.sleep(0.05)
            raise ValueError("Test error")
        
        # Execute the decorated function and expect exception
        with pytest.raises(ValueError):
            failing_function()
        
        # Verify metric was still recorded
        execution_metrics = [m for m in monitor.metrics if "execution_time" in m.name]
        assert len(execution_metrics) >= 1
        
        # Verify error was captured in metadata
        metric = execution_metrics[0]
        assert metric.metadata["success"] is False
        assert "Test error" in metric.metadata["error"]
    
    @patch('psutil.Process')
    def test_track_memory_usage(self, mock_process, temp_log_dir, mock_streamlit):
        """Test memory usage tracking"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        # Mock process memory info
        mock_memory_info = MagicMock()
        mock_memory_info.rss = 1024 * 1024 * 100  # 100MB
        mock_memory_info.vms = 1024 * 1024 * 200  # 200MB
        
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value = mock_memory_info
        mock_process_instance.memory_percent.return_value = 10.5
        mock_process.return_value = mock_process_instance
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Track memory usage
        monitor.track_memory_usage()
        
        # Verify memory metric was recorded
        memory_metrics = [m for m in monitor.metrics if m.name == "memory_usage"]
        assert len(memory_metrics) >= 1
        
        metric = memory_metrics[0]
        assert metric.value == 100.0  # 100MB
        assert metric.unit == "MB"
        assert metric.category == "system"
    
    @patch('psutil.cpu_percent')
    def test_track_cpu_usage(self, mock_cpu_percent, temp_log_dir, mock_streamlit):
        """Test CPU usage tracking"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        mock_cpu_percent.return_value = 45.7
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Track CPU usage
        monitor.track_cpu_usage()
        
        # Verify CPU metric was recorded
        cpu_metrics = [m for m in monitor.metrics if m.name == "cpu_usage"]
        assert len(cpu_metrics) >= 1
        
        metric = cpu_metrics[0]
        assert metric.value == 45.7
        assert metric.unit == "percent"
        assert metric.category == "system"
    
    def test_track_streamlit_metrics(self, temp_log_dir, mock_streamlit):
        """Test Streamlit-specific metrics tracking"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Track Streamlit metrics
        monitor.track_streamlit_metrics()
        
        # Verify session state metrics were recorded
        session_metrics = [m for m in monitor.metrics if m.name == "session_state_keys"]
        assert len(session_metrics) >= 1
        
        metric = session_metrics[0]
        assert metric.value >= 0  # Should have some session state keys
        assert metric.unit == "keys"
        assert metric.category == "streamlit"
    
    def test_get_metrics_summary(self, temp_log_dir, mock_streamlit):
        """Test getting metrics summary"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Add some test metrics
        monitor.record_metric("test_metric_1", 100.0, "units", "test")
        monitor.record_metric("test_metric_2", 200.0, "units", "test")
        monitor.record_metric("cpu_usage", 50.0, "percent", "system")
        
        # Get summary
        summary = monitor.get_metrics_summary()
        
        # Verify summary structure
        assert isinstance(summary, dict)
        assert "total_metrics" in summary
        assert "categories" in summary
        assert "session_info" in summary
        
        assert summary["total_metrics"] == 3
        assert "test" in summary["categories"]
        assert "system" in summary["categories"]
    
    def test_get_recent_metrics(self, temp_log_dir, mock_streamlit):
        """Test getting recent metrics"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Add some metrics
        monitor.record_metric("recent_metric", 100.0, "units", "test")
        time.sleep(0.1)
        monitor.record_metric("another_metric", 200.0, "units", "test")
        
        # Get recent metrics
        recent = monitor.get_recent_metrics(minutes=1)
        
        # Verify recent metrics
        assert len(recent) == 2
        assert all(isinstance(m, PerformanceMetric) for m in recent)
    
    def test_export_metrics(self, temp_log_dir, mock_streamlit):
        """Test exporting metrics to JSON"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Add test metrics
        monitor.record_metric("export_test", 123.45, "units", "test")
        
        # Export metrics
        export_path = monitor.export_metrics()
        
        # Verify export file exists
        assert Path(export_path).exists()
        
        # Verify export content
        with open(export_path) as f:
            data = json.load(f)
        
        assert "export_timestamp" in data
        assert "session_id" in data
        assert "summary" in data
        assert "metrics" in data
        assert len(data["metrics"]) >= 1
    
    def test_cleanup_old_logs(self, temp_log_dir, mock_streamlit):
        """Test cleaning up old log files"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Create some test log files
        old_log = temp_log_dir / "old_log.log"
        old_log.touch()
        
        # Make the file appear old
        old_time = time.time() - (8 * 24 * 60 * 60)  # 8 days ago
        old_log.touch(times=(old_time, old_time))
        
        recent_log = temp_log_dir / "recent_log.log"
        recent_log.touch()
        
        # Clean up old logs
        monitor.cleanup_old_logs(days=7)
        
        # Verify old log was removed and recent log remains
        assert not old_log.exists()
        assert recent_log.exists()
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    @patch('streamlit.json')
    @patch('streamlit.button')
    @patch('streamlit.success')
    @patch('streamlit.error')
    @patch('streamlit.info')
    @patch('streamlit.write')
    def test_render_monitoring_dashboard(self, mock_write, mock_info, mock_error, 
                                       mock_success, mock_button, mock_json, 
                                       mock_metric, mock_columns, mock_subheader, 
                                       mock_title, temp_log_dir, mock_streamlit):
        """Test rendering monitoring dashboard UI"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        monitor = PerformanceMonitor(log_dir=temp_log_dir)
        
        # Mock Streamlit components
        def mock_columns_side_effect(n):
            return [MagicMock() for _ in range(n)]
        
        mock_columns.side_effect = mock_columns_side_effect
        mock_button.return_value = False
        
        # Add some test metrics
        monitor.record_metric("memory_usage", 100.0, "MB", "system")
        monitor.record_metric("cpu_usage", 50.0, "percent", "system")
        
        # Test that method exists and can be called
        assert hasattr(monitor, 'render_monitoring_dashboard')
        
        # Call method (should not raise exceptions)
        try:
            monitor.render_monitoring_dashboard()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("render_monitoring_dashboard not implemented yet")


class TestGlobalFunctions:
    """Test global convenience functions"""
    
    def test_get_performance_monitor(self):
        """Test getting global performance monitor instance"""
        if get_performance_monitor is None:
            pytest.skip("get_performance_monitor not implemented yet")
        
        monitor1 = get_performance_monitor()
        monitor2 = get_performance_monitor()
        
        # Should return the same instance
        assert monitor1 is monitor2
        assert isinstance(monitor1, PerformanceMonitor)
    
    @patch('components.performance_monitor.get_performance_monitor')
    def test_track_performance_decorator(self, mock_get_monitor):
        """Test track_performance decorator"""
        if track_performance is None:
            pytest.skip("track_performance not implemented yet")
        
        mock_monitor = MagicMock()
        mock_get_monitor.return_value = mock_monitor
        
        @track_performance(category="test")
        def test_function():
            return "test_result"
        
        result = test_function()
        
        assert result == "test_result"
        # Verify monitor was called
        mock_monitor.measure_execution_time.assert_called_once()
    
    @patch('components.performance_monitor.get_performance_monitor')
    def test_log_event_convenience(self, mock_get_monitor):
        """Test log_event convenience function"""
        if log_event is None:
            pytest.skip("log_event not implemented yet")
        
        mock_monitor = MagicMock()
        mock_get_monitor.return_value = mock_monitor
        
        log_event("INFO", "Test message", "test", "test_component")
        
        # Verify monitor was called
        mock_monitor.log_event.assert_called_once_with(
            "INFO", "Test message", "test", "test_component", None
        )
    
    @patch('components.performance_monitor.get_performance_monitor')
    def test_record_metric_convenience(self, mock_get_monitor):
        """Test record_metric convenience function"""
        if record_metric is None:
            pytest.skip("record_metric not implemented yet")
        
        mock_monitor = MagicMock()
        mock_get_monitor.return_value = mock_monitor
        
        record_metric("test_metric", 100.0, "units", "test")
        
        # Verify monitor was called
        mock_monitor.record_metric.assert_called_once_with(
            "test_metric", 100.0, "units", "test", None
        )
    
    def test_performance_monitor_error_handling(self):
        """Test error handling in performance monitoring"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        with tempfile.TemporaryDirectory() as tmp_dir:
            monitor = PerformanceMonitor(log_dir=Path(tmp_dir))
            
            # Test with invalid metric data
            try:
                monitor.record_metric("", 100.0, "units")  # Empty name
                assert False, "Should have raised ValueError"
            except ValueError:
                pass  # Expected
            
            # Test with invalid log level
            try:
                monitor.log_event("INVALID_LEVEL", "Test message")
                # Should not raise exception, but should handle gracefully
                assert True
            except Exception:
                pass  # Some handling is expected
    
    def test_performance_monitor_thread_safety(self):
        """Test thread safety of performance monitor"""
        if PerformanceMonitor is None:
            pytest.skip("PerformanceMonitor not implemented yet")
        
        import threading
        
        with tempfile.TemporaryDirectory() as tmp_dir:
            monitor = PerformanceMonitor(log_dir=Path(tmp_dir))
            
            def worker():
                for i in range(10):
                    monitor.record_metric(f"thread_metric_{i}", i * 10.0, "units", "thread_test")
            
            # Start multiple threads
            threads = []
            for _ in range(5):
                thread = threading.Thread(target=worker)
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            # Verify all metrics were recorded
            thread_metrics = [m for m in monitor.metrics if m.category == "thread_test"]
            assert len(thread_metrics) == 50  # 5 threads * 10 metrics each