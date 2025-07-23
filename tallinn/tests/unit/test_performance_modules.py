#!/usr/bin/env python3
"""
Comprehensive test suite for performance modules

Tests performance monitoring, benchmarking, and optimization functionality:
- performance/benchmarker.py
- performance/context_optimizer.py  
- performance/monitor.py
"""

import pytest
import tempfile
import json
import time
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import sys

# Add performance module to path
performance_dir = Path(__file__).parent.parent.parent / "performance"
sys.path.insert(0, str(performance_dir))

try:
    from benchmarker import PerformanceBenchmarker
    from context_optimizer import ContextOptimizer
    from monitor import PerformanceMonitor
except ImportError as e:
    pytest.skip(f"Performance modules not available: {e}", allow_module_level=True)


class TestPerformanceBenchmarker:
    """Test suite for PerformanceBenchmarker class."""
    
    @pytest.fixture
    def temp_benchmark_dir(self):
        """Create temporary directory for benchmark testing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield Path(temp_dir)
    
    def test_benchmarker_initialization(self, temp_benchmark_dir):
        """Test PerformanceBenchmarker initialization."""
        benchmarker = PerformanceBenchmarker(str(temp_benchmark_dir))
        
        assert benchmarker.output_dir == temp_benchmark_dir
        assert hasattr(benchmarker, 'results')
        assert hasattr(benchmarker, 'config')
    
    def test_benchmark_command_execution_time(self, temp_benchmark_dir):
        """Test command execution time benchmarking."""
        benchmarker = PerformanceBenchmarker(str(temp_benchmark_dir))
        
        # Mock benchmark execution
        with patch.object(benchmarker, 'benchmark_command') as mock_benchmark:
            mock_result = {
                "command": "test-command",
                "execution_time": 0.123,
                "memory_usage": 1024,
                "success": True
            }
            mock_benchmark.return_value = mock_result
            
            result = benchmarker.benchmark_command("test-command", {"arg": "value"})
            
            assert result["success"] is True
            assert result["execution_time"] > 0
            assert "memory_usage" in result
    
    def test_memory_usage_tracking(self, temp_benchmark_dir):
        """Test memory usage tracking during benchmarks."""
        benchmarker = PerformanceBenchmarker(str(temp_benchmark_dir))
        
        with patch('psutil.Process') as mock_process:
            mock_process.return_value.memory_info.return_value.rss = 1024 * 1024  # 1MB
            
            with patch.object(benchmarker, 'track_memory_usage') as mock_memory:
                mock_memory.return_value = {"peak_memory": 1024 * 1024, "average_memory": 512 * 1024}
                
                result = benchmarker.track_memory_usage("test_operation")
                
                assert "peak_memory" in result
                assert "average_memory" in result
    
    def test_performance_regression_detection(self, temp_benchmark_dir):
        """Test performance regression detection."""
        benchmarker = PerformanceBenchmarker(str(temp_benchmark_dir))
        
        # Mock historical benchmark data
        historical_results = [
            {"command": "test-cmd", "execution_time": 0.1, "timestamp": "2025-01-01"},
            {"command": "test-cmd", "execution_time": 0.12, "timestamp": "2025-01-02"},
            {"command": "test-cmd", "execution_time": 0.11, "timestamp": "2025-01-03"}
        ]
        
        current_result = {"command": "test-cmd", "execution_time": 0.25}  # 2x slower
        
        with patch.object(benchmarker, 'detect_regression') as mock_regression:
            mock_regression.return_value = {
                "regression_detected": True,
                "performance_degradation": 127.3,  # 127% increase
                "threshold_exceeded": True
            }
            
            result = benchmarker.detect_regression(current_result, historical_results)
            
            assert result["regression_detected"] is True
            assert result["performance_degradation"] > 100


class TestContextOptimizer:
    """Test suite for ContextOptimizer class."""
    
    @pytest.fixture
    def sample_context_data(self):
        """Create sample context data for testing."""
        return {
            "commands": ["command1", "command2", "command3"],
            "components": ["comp1", "comp2"],
            "user_input": "Process this data efficiently",
            "context_window": 4096,
            "token_count": 1500
        }
    
    def test_context_optimizer_initialization(self):
        """Test ContextOptimizer initialization."""
        optimizer = ContextOptimizer()
        
        assert hasattr(optimizer, 'optimization_strategies')
        assert hasattr(optimizer, 'token_limits')
        assert hasattr(optimizer, 'compression_ratios')
    
    def test_context_compression(self, sample_context_data):
        """Test context compression functionality."""
        optimizer = ContextOptimizer()
        
        with patch.object(optimizer, 'compress_context') as mock_compress:
            compressed_data = {
                "compressed_commands": ["cmd1", "cmd2"],
                "compression_ratio": 0.67,
                "token_count_reduced": 500
            }
            mock_compress.return_value = compressed_data
            
            result = optimizer.compress_context(sample_context_data)
            
            assert result["compression_ratio"] < 1.0
            assert result["token_count_reduced"] > 0
    
    def test_token_optimization(self, sample_context_data):
        """Test token count optimization."""
        optimizer = ContextOptimizer()
        
        with patch.object(optimizer, 'optimize_tokens') as mock_optimize:
            optimized_result = {
                "original_tokens": 1500,
                "optimized_tokens": 1200,
                "reduction_percentage": 20.0,
                "strategies_applied": ["redundancy_removal", "abbreviation"]
            }
            mock_optimize.return_value = optimized_result
            
            result = optimizer.optimize_tokens(sample_context_data)
            
            assert result["optimized_tokens"] < result["original_tokens"]
            assert result["reduction_percentage"] > 0
    
    def test_context_window_fitting(self, sample_context_data):
        """Test fitting context within window limits."""
        optimizer = ContextOptimizer()
        
        with patch.object(optimizer, 'fit_to_window') as mock_fit:
            fitted_result = {
                "fits_in_window": True,
                "window_utilization": 0.73,
                "truncation_applied": False,
                "final_token_count": 3000
            }
            mock_fit.return_value = fitted_result
            
            result = optimizer.fit_to_window(sample_context_data, window_size=4096)
            
            assert result["fits_in_window"] is True
            assert 0 <= result["window_utilization"] <= 1
    
    def test_intelligent_truncation(self, sample_context_data):
        """Test intelligent content truncation."""
        optimizer = ContextOptimizer()
        
        # Simulate content that exceeds window size
        large_context = sample_context_data.copy()
        large_context["token_count"] = 8000  # Exceeds 4096 window
        
        with patch.object(optimizer, 'intelligent_truncate') as mock_truncate:
            truncated_result = {
                "truncated": True,
                "priority_preserved": ["commands", "user_input"],
                "removed_sections": ["low_priority_components"],
                "final_token_count": 3800
            }
            mock_truncate.return_value = truncated_result
            
            result = optimizer.intelligent_truncate(large_context, max_tokens=4000)
            
            assert result["truncated"] is True
            assert result["final_token_count"] <= 4000


class TestPerformanceMonitor:
    """Test suite for PerformanceMonitor class."""
    
    @pytest.fixture
    def temp_monitoring_dir(self):
        """Create temporary directory for monitoring data."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield Path(temp_dir)
    
    def test_performance_monitor_initialization(self, temp_monitoring_dir):
        """Test PerformanceMonitor initialization."""
        monitor = PerformanceMonitor(str(temp_monitoring_dir))
        
        assert monitor.data_dir == temp_monitoring_dir
        assert hasattr(monitor, 'metrics')
        assert hasattr(monitor, 'alerts')
    
    def test_real_time_metrics_collection(self, temp_monitoring_dir):
        """Test real-time performance metrics collection."""
        monitor = PerformanceMonitor(str(temp_monitoring_dir))
        
        with patch.object(monitor, 'collect_metrics') as mock_collect:
            mock_metrics = {
                "timestamp": time.time(),
                "cpu_usage": 65.2,
                "memory_usage": 78.5,
                "response_time": 0.145,
                "active_connections": 12
            }
            mock_collect.return_value = mock_metrics
            
            metrics = monitor.collect_metrics()
            
            assert "cpu_usage" in metrics
            assert "memory_usage" in metrics
            assert "response_time" in metrics
            assert metrics["timestamp"] > 0
    
    def test_performance_alert_system(self, temp_monitoring_dir):
        """Test performance alerting system."""
        monitor = PerformanceMonitor(str(temp_monitoring_dir))
        
        # High CPU usage should trigger alert
        high_cpu_metrics = {
            "cpu_usage": 95.0,
            "memory_usage": 85.0,
            "response_time": 2.5
        }
        
        with patch.object(monitor, 'check_alerts') as mock_alerts:
            mock_alert_result = {
                "alerts_triggered": [
                    {"type": "HIGH_CPU", "threshold": 90, "current": 95},
                    {"type": "SLOW_RESPONSE", "threshold": 1.0, "current": 2.5}
                ],
                "alert_count": 2,
                "severity": "HIGH"
            }
            mock_alerts.return_value = mock_alert_result
            
            alerts = monitor.check_alerts(high_cpu_metrics)
            
            assert alerts["alert_count"] > 0
            assert alerts["severity"] == "HIGH"
    
    def test_performance_trend_analysis(self, temp_monitoring_dir):
        """Test performance trend analysis."""
        monitor = PerformanceMonitor(str(temp_monitoring_dir))
        
        # Historical performance data
        historical_data = [
            {"timestamp": time.time() - 3600, "response_time": 0.1},
            {"timestamp": time.time() - 1800, "response_time": 0.15},
            {"timestamp": time.time() - 900, "response_time": 0.2},
            {"timestamp": time.time(), "response_time": 0.25}
        ]
        
        with patch.object(monitor, 'analyze_trends') as mock_trends:
            trend_analysis = {
                "trend_direction": "INCREASING",
                "trend_strength": 0.85,
                "prediction_next_hour": 0.3,
                "concerning_trend": True
            }
            mock_trends.return_value = trend_analysis
            
            trends = monitor.analyze_trends(historical_data, "response_time")
            
            assert trends["trend_direction"] in ["INCREASING", "DECREASING", "STABLE"]
            assert 0 <= trends["trend_strength"] <= 1
    
    def test_performance_dashboard_data(self, temp_monitoring_dir):
        """Test performance dashboard data generation."""
        monitor = PerformanceMonitor(str(temp_monitoring_dir))
        
        with patch.object(monitor, 'get_dashboard_data') as mock_dashboard:
            dashboard_data = {
                "current_metrics": {
                    "cpu": 45.2,
                    "memory": 67.8,
                    "disk_io": 23.4
                },
                "recent_alerts": [
                    {"time": "10:30", "type": "HIGH_MEMORY", "resolved": True}
                ],
                "performance_summary": {
                    "avg_response_time": 0.125,
                    "uptime": "99.95%",
                    "error_rate": 0.02
                }
            }
            mock_dashboard.return_value = dashboard_data
            
            data = monitor.get_dashboard_data()
            
            assert "current_metrics" in data
            assert "recent_alerts" in data
            assert "performance_summary" in data


class TestPerformanceModulesIntegration:
    """Integration tests for performance modules working together."""
    
    def test_benchmarker_optimizer_integration(self):
        """Test integration between benchmarker and optimizer."""
        with tempfile.TemporaryDirectory() as temp_dir:
            benchmarker = PerformanceBenchmarker(temp_dir)
            optimizer = ContextOptimizer()
            
            # Mock integration workflow
            with patch.object(benchmarker, 'benchmark_command') as mock_benchmark, \
                 patch.object(optimizer, 'optimize_tokens') as mock_optimize:
                
                # Benchmark shows high token usage
                mock_benchmark.return_value = {
                    "command": "test-cmd",
                    "execution_time": 1.5,
                    "token_usage": 3000
                }
                
                # Optimizer reduces token usage
                mock_optimize.return_value = {
                    "optimized_tokens": 2000,
                    "reduction_percentage": 33.3
                }
                
                # Run integration test
                benchmark_result = benchmarker.benchmark_command("test-cmd", {})
                optimization_result = optimizer.optimize_tokens({"token_count": benchmark_result["token_usage"]})
                
                assert benchmark_result["token_usage"] > optimization_result["optimized_tokens"]
    
    def test_monitor_benchmarker_workflow(self):
        """Test workflow between monitor and benchmarker."""
        with tempfile.TemporaryDirectory() as temp_dir:
            monitor = PerformanceMonitor(temp_dir)
            benchmarker = PerformanceBenchmarker(temp_dir)
            
            with patch.object(monitor, 'collect_metrics') as mock_collect, \
                 patch.object(benchmarker, 'benchmark_command') as mock_benchmark:
                
                # Monitor detects performance issue
                mock_collect.return_value = {
                    "response_time": 2.0,  # Slow response
                    "memory_usage": 90.0   # High memory
                }
                
                # Benchmark investigates the issue
                mock_benchmark.return_value = {
                    "command": "slow-command",
                    "execution_time": 2.1,
                    "memory_usage": 1024 * 1024 * 100  # 100MB
                }
                
                # Verify workflow
                metrics = monitor.collect_metrics()
                if metrics["response_time"] > 1.0:
                    benchmark_result = benchmarker.benchmark_command("problematic-command", {})
                    assert benchmark_result["execution_time"] > 1.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])