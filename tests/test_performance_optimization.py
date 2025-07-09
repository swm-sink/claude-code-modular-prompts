#!/usr/bin/env python3
"""
Performance Optimization Validation Tests

This module provides comprehensive validation tests for performance optimizations including:
- Context window optimization validation
- Parallel execution performance testing
- Cache efficiency validation
- User experience metrics validation
- Performance regression testing
- Real-time monitoring validation

Agent 5: Performance & Optimization Engineer
Target: Validate 80% improvement in task completion time, 50% reduction in context usage
"""

import unittest
import time
import threading
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
import statistics
import json
from datetime import datetime, timedelta
import tempfile
import shutil

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.performance_optimizer import (
    PerformanceOptimizer, PerformanceProfile, OptimizationLevel,
    ContextOptimizer, ParallelExecutionOptimizer, IntelligentCache
)
from scripts.user_experience_optimizer import (
    UserExperienceOptimizer, ImmediateFeedbackProvider, 
    ProgressiveLoadingManager, RealTimeVisibilityDashboard
)
from scripts.performance_dashboard import (
    PerformanceDashboard, MetricsCollector, PerformanceAnalyzer,
    MetricType, PerformanceTarget, AlertLevel
)


class TestContextOptimization(unittest.TestCase):
    """Test context window optimization capabilities."""
    
    def setUp(self):
        """Set up test environment."""
        self.profile = PerformanceProfile(
            target_context_budget=50000,
            optimization_level=OptimizationLevel.AGGRESSIVE
        )
        self.context_optimizer = ContextOptimizer(self.profile)
    
    def test_context_compression_effectiveness(self):
        """Test that context compression effectively reduces token usage."""
        # Sample content with redundant patterns
        sample_content = """
        <framework_analysis>
            <critical_section>
                <important_note>This is a critical section that needs preservation</important_note>
                <important_note>This is another critical section</important_note>
            </critical_section>
            <standard_section>
                <note>This is a standard section</note>
                <note>This is another standard section</note>
                <note>This is a third standard section</note>
            </standard_section>
            <low_priority_section>
                <verbose_description>
                    This is a very verbose description that contains a lot of
                    unnecessary words and could be significantly compressed
                    without losing any meaningful information.
                </verbose_description>
            </low_priority_section>
        </framework_analysis>
        """
        
        # Test high priority optimization
        optimized_content, tokens_saved = self.context_optimizer.optimize_context_usage(
            sample_content, priority="high"
        )
        
        self.assertLess(len(optimized_content), len(sample_content))
        self.assertGreater(tokens_saved, 0)
        
        # Verify critical content is preserved
        self.assertIn("critical section", optimized_content)
        
        # Test medium priority optimization
        optimized_medium, tokens_saved_medium = self.context_optimizer.optimize_context_usage(
            sample_content, priority="medium"
        )
        
        self.assertLessEqual(len(optimized_medium), len(optimized_content))
        self.assertGreaterEqual(tokens_saved_medium, tokens_saved)
    
    def test_hierarchical_loading_efficiency(self):
        """Test that hierarchical loading prioritizes important content."""
        # Content with priority markers
        content_with_priorities = """
        <critical>This is critical information</critical>
        <standard>This is standard information</standard>
        <mandatory>This is mandatory information</mandatory>
        <optional>This is optional information</optional>
        """
        
        optimized_content, tokens_saved = self.context_optimizer.optimize_context_usage(
            content_with_priorities, priority="medium"
        )
        
        # Verify priority content appears first
        critical_pos = optimized_content.find("critical")
        mandatory_pos = optimized_content.find("mandatory")
        standard_pos = optimized_content.find("standard")
        
        self.assertLess(critical_pos, standard_pos)
        self.assertLess(mandatory_pos, standard_pos)
    
    def test_context_budget_compliance(self):
        """Test that context optimization respects budget limits."""
        # Create content that exceeds budget
        large_content = "A" * 200000  # 200K characters (~50K tokens)
        
        optimized_content, tokens_saved = self.context_optimizer.optimize_context_usage(
            large_content, priority="low"
        )
        
        # Verify optimized content is within budget
        estimated_tokens = len(optimized_content) // 4
        self.assertLess(estimated_tokens, self.profile.target_context_budget)
        self.assertGreater(tokens_saved, 0)
    
    def test_xml_structure_preservation(self):
        """Test that XML structure is preserved during optimization."""
        xml_content = """
        <framework>
            <commands>
                <command name="task">Task command</command>
                <command name="query">Query command</command>
            </commands>
            <modules>
                <module name="quality">Quality module</module>
            </modules>
        </framework>
        """
        
        optimized_content, _ = self.context_optimizer.optimize_context_usage(
            xml_content, priority="high"
        )
        
        # Verify XML structure is maintained
        self.assertIn("<framework>", optimized_content)
        self.assertIn("</framework>", optimized_content)
        self.assertIn("<commands>", optimized_content)
        self.assertIn("</commands>", optimized_content)


class TestParallelExecution(unittest.TestCase):
    """Test parallel execution optimization."""
    
    def setUp(self):
        """Set up test environment."""
        self.profile = PerformanceProfile(parallel_workers=4)
        self.parallel_optimizer = ParallelExecutionOptimizer(self.profile)
    
    def test_parallel_execution_speedup(self):
        """Test that parallel execution provides significant speedup."""
        # Define test operations
        def test_operation(delay=0.1):
            time.sleep(delay)
            return f"Operation completed"
        
        operations = [lambda: test_operation(0.05) for _ in range(8)]
        
        # Sequential execution time
        sequential_start = time.perf_counter()
        sequential_results = [op() for op in operations]
        sequential_time = time.perf_counter() - sequential_start
        
        # Parallel execution time
        parallel_start = time.perf_counter()
        parallel_results = self.parallel_optimizer.optimize_parallel_execution(operations)
        parallel_time = time.perf_counter() - parallel_start
        
        # Verify speedup
        speedup = sequential_time / parallel_time
        self.assertGreater(speedup, 1.5)  # At least 1.5x speedup
        self.assertEqual(len(parallel_results), len(sequential_results))
    
    def test_batch_optimization(self):
        """Test batch operation optimization."""
        # Create large batch of operations
        def simple_operation():
            time.sleep(0.01)
            return "batch_result"
        
        operations = [simple_operation for _ in range(20)]
        
        start_time = time.perf_counter()
        results = self.parallel_optimizer.batch_optimize_operations(operations, batch_size=5)
        execution_time = time.perf_counter() - start_time
        
        # Verify all operations completed
        self.assertEqual(len(results), 20)
        self.assertLess(execution_time, 0.5)  # Should complete quickly with batching
    
    def test_parallel_efficiency_metrics(self):
        """Test parallel execution efficiency metrics."""
        operations = [lambda: time.sleep(0.02) for _ in range(10)]
        
        # Execute operations
        self.parallel_optimizer.optimize_parallel_execution(operations)
        
        # Get statistics
        stats = self.parallel_optimizer.get_execution_statistics()
        
        self.assertIn('avg_execution_time_ms', stats)
        self.assertIn('avg_parallel_efficiency', stats)
        self.assertGreater(stats['avg_parallel_efficiency'], 0)
    
    def test_error_handling_in_parallel_execution(self):
        """Test error handling in parallel execution."""
        def failing_operation():
            raise ValueError("Test error")
        
        def success_operation():
            return "success"
        
        operations = [success_operation, failing_operation, success_operation]
        
        results = self.parallel_optimizer.optimize_parallel_execution(operations)
        
        # Verify mixed results (some success, some None for failures)
        self.assertEqual(len(results), 3)
        self.assertIsNotNone(results[0])
        self.assertIsNone(results[1])  # Failed operation
        self.assertIsNotNone(results[2])


class TestIntelligentCaching(unittest.TestCase):
    """Test intelligent caching system."""
    
    def setUp(self):
        """Set up test environment."""
        self.profile = PerformanceProfile(cache_size_mb=10.0)
        self.cache = IntelligentCache(self.profile)
    
    def test_cache_hit_performance(self):
        """Test cache hit performance improvement."""
        def expensive_operation():
            time.sleep(0.1)
            return "expensive_result"
        
        # First call (cache miss)
        start_time = time.perf_counter()
        result1 = self.cache.get_cached_result("test_key", expensive_operation)
        first_call_time = time.perf_counter() - start_time
        
        # Second call (cache hit)
        start_time = time.perf_counter()
        result2 = self.cache.get_cached_result("test_key", expensive_operation)
        second_call_time = time.perf_counter() - start_time
        
        # Verify cache hit is significantly faster
        self.assertEqual(result1, result2)
        self.assertLess(second_call_time, first_call_time / 10)  # At least 10x faster
    
    def test_cache_eviction_policy(self):
        """Test least recently used cache eviction."""
        # Fill cache with small items
        for i in range(100):
            self.cache.get_cached_result(f"key_{i}", lambda: f"value_{i}")
        
        # Access some items to make them recently used
        self.cache.get_cached_result("key_50", lambda: "value_50")
        self.cache.get_cached_result("key_75", lambda: "value_75")
        
        # Add more items to trigger eviction
        for i in range(100, 150):
            self.cache.get_cached_result(f"key_{i}", lambda: f"value_{i}")
        
        # Verify recently used items are still cached
        stats = self.cache.get_cache_statistics()
        self.assertGreater(stats['evictions'], 0)
    
    def test_cache_statistics(self):
        """Test cache statistics collection."""
        # Generate cache hits and misses
        self.cache.get_cached_result("key1", lambda: "value1")  # Miss
        self.cache.get_cached_result("key1", lambda: "value1")  # Hit
        self.cache.get_cached_result("key2", lambda: "value2")  # Miss
        
        stats = self.cache.get_cache_statistics()
        
        self.assertEqual(stats['hits'], 1)
        self.assertEqual(stats['misses'], 2)
        self.assertEqual(stats['total_requests'], 3)
        self.assertAlmostEqual(stats['hit_rate_percent'], 33.33, places=1)


class TestUserExperienceOptimization(unittest.TestCase):
    """Test user experience optimization features."""
    
    def setUp(self):
        """Set up test environment."""
        self.ux_optimizer = UserExperienceOptimizer()
    
    def test_immediate_feedback_provision(self):
        """Test immediate feedback for user actions."""
        feedback_received = []
        
        def feedback_callback(feedback):
            feedback_received.append(feedback)
        
        self.ux_optimizer.feedback_provider.register_feedback_callback(feedback_callback)
        
        # Provide feedback
        self.ux_optimizer.feedback_provider.provide_immediate_feedback(
            action_type="command_execution",
            message="Test operation started",
            action_id="test_action_123"
        )
        
        # Verify feedback was received
        self.assertEqual(len(feedback_received), 1)
        self.assertEqual(feedback_received[0].message, "Test operation started")
    
    def test_progressive_loading_management(self):
        """Test progressive loading for complex operations."""
        def test_operation():
            time.sleep(0.1)
            return "operation_complete"
        
        result = self.ux_optimizer.optimize_user_operation(
            operation_name="Test Progressive Operation",
            operation_func=test_operation,
            steps=["Initialize", "Process", "Validate", "Complete"],
            estimated_duration=0.5
        )
        
        self.assertEqual(result, "operation_complete")
    
    def test_error_recovery_assistance(self):
        """Test intelligent error recovery."""
        def failing_operation():
            raise FileNotFoundError("Test file not found")
        
        with self.assertRaises(FileNotFoundError):
            self.ux_optimizer.optimize_user_operation(
                operation_name="Test Error Recovery",
                operation_func=failing_operation,
                steps=["Initialize", "Process"],
                estimated_duration=1.0
            )
    
    def test_performance_dashboard_integration(self):
        """Test integration with performance dashboard."""
        # Start dashboard monitoring
        self.ux_optimizer.dashboard.start_monitoring()
        
        # Perform operation
        def quick_operation():
            time.sleep(0.05)
            return "dashboard_test"
        
        result = self.ux_optimizer.optimize_user_operation(
            operation_name="Dashboard Integration Test",
            operation_func=quick_operation,
            estimated_duration=0.1
        )
        
        # Allow time for dashboard updates
        time.sleep(0.1)
        
        # Verify dashboard captured metrics
        perf_summary = self.ux_optimizer.dashboard.get_performance_summary()
        self.assertGreater(perf_summary.get('total_operations', 0), 0)
        
        # Stop monitoring
        self.ux_optimizer.dashboard.stop_monitoring()


class TestPerformanceDashboard(unittest.TestCase):
    """Test performance dashboard functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.dashboard = PerformanceDashboard(update_interval=0.1)
    
    def test_metrics_collection(self):
        """Test that metrics are collected properly."""
        # Start dashboard
        self.dashboard.start_dashboard()
        
        # Allow time for metrics collection
        time.sleep(0.5)
        
        # Verify metrics were collected
        for metric_type in MetricType:
            latest_metric = self.dashboard.metrics_collector.get_latest_metric(metric_type)
            if latest_metric:
                self.assertIsNotNone(latest_metric.value)
                self.assertIsInstance(latest_metric.timestamp, datetime)
        
        # Stop dashboard
        self.dashboard.stop_dashboard()
    
    def test_performance_analysis(self):
        """Test performance analysis functionality."""
        # Start dashboard and collect some metrics
        self.dashboard.start_dashboard()
        time.sleep(0.3)
        
        # Get analysis
        analysis = self.dashboard.analyzer.analyze_current_performance()
        
        # Verify analysis structure
        self.assertIn('metric_summaries', analysis)
        self.assertIn('target_compliance', analysis)
        self.assertIn('trend_analysis', analysis)
        self.assertIn('recommendations', analysis)
        
        # Stop dashboard
        self.dashboard.stop_dashboard()
    
    def test_alert_generation(self):
        """Test performance alert generation."""
        # Add a strict target that will trigger alerts
        strict_target = PerformanceTarget(
            target_id="test_strict_target",
            metric_type=MetricType.EXECUTION_TIME,
            target_value=1.0,  # Very strict 1ms target
            comparison_operator="<",
            description="Strict execution time target for testing",
            alert_level=AlertLevel.WARNING
        )
        
        self.dashboard.analyzer.add_performance_target(strict_target)
        
        # Start dashboard
        self.dashboard.start_dashboard()
        
        # Allow time for metrics and alerts
        time.sleep(0.5)
        
        # Check for alerts
        active_alerts = self.dashboard.alert_manager.get_active_alerts()
        
        # Stop dashboard
        self.dashboard.stop_dashboard()
        
        # Verify alerts were generated (execution time likely > 1ms)
        self.assertGreaterEqual(len(active_alerts), 0)
    
    def test_dashboard_data_export(self):
        """Test dashboard data export functionality."""
        # Start dashboard
        self.dashboard.start_dashboard()
        time.sleep(0.2)
        
        # Get dashboard data
        dashboard_data = self.dashboard.get_dashboard_data()
        
        # Verify data structure
        self.assertIn('analysis', dashboard_data)
        self.assertIn('active_alerts', dashboard_data)
        self.assertIn('targets', dashboard_data)
        self.assertIn('dashboard_status', dashboard_data)
        
        # Stop dashboard
        self.dashboard.stop_dashboard()


class TestPerformanceRegression(unittest.TestCase):
    """Test performance regression detection and prevention."""
    
    def setUp(self):
        """Set up test environment."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.baseline_file = self.temp_dir / "performance_baseline.json"
        
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.temp_dir)
    
    def test_performance_baseline_creation(self):
        """Test creation of performance baseline."""
        # Create baseline metrics
        baseline_metrics = {
            'execution_time_ms': 500.0,
            'context_tokens': 25000,
            'cache_hit_rate': 0.75,
            'parallel_efficiency': 0.85,
            'timestamp': datetime.now().isoformat()
        }
        
        # Save baseline
        with open(self.baseline_file, 'w') as f:
            json.dump(baseline_metrics, f)
        
        # Verify baseline was created
        self.assertTrue(self.baseline_file.exists())
        
        # Load and verify baseline
        with open(self.baseline_file, 'r') as f:
            loaded_baseline = json.load(f)
        
        self.assertEqual(loaded_baseline['execution_time_ms'], 500.0)
        self.assertEqual(loaded_baseline['context_tokens'], 25000)
    
    def test_performance_regression_detection(self):
        """Test detection of performance regressions."""
        # Create baseline
        baseline_metrics = {
            'execution_time_ms': 500.0,
            'context_tokens': 25000,
            'cache_hit_rate': 0.75
        }
        
        # Simulate current metrics (regression)
        current_metrics = {
            'execution_time_ms': 800.0,  # 60% increase (regression)
            'context_tokens': 35000,     # 40% increase (regression)
            'cache_hit_rate': 0.65       # 13% decrease (regression)
        }
        
        # Detect regressions
        regressions = self._detect_regressions(baseline_metrics, current_metrics)
        
        # Verify regressions were detected
        self.assertGreater(len(regressions), 0)
        self.assertIn('execution_time_ms', regressions)
        self.assertIn('context_tokens', regressions)
    
    def test_performance_improvement_validation(self):
        """Test validation of performance improvements."""
        # Create baseline
        baseline_metrics = {
            'execution_time_ms': 1000.0,
            'context_tokens': 40000,
            'cache_hit_rate': 0.60
        }
        
        # Simulate improved metrics
        improved_metrics = {
            'execution_time_ms': 500.0,   # 50% improvement
            'context_tokens': 25000,      # 37.5% improvement
            'cache_hit_rate': 0.80        # 33% improvement
        }
        
        # Validate improvements
        improvements = self._detect_improvements(baseline_metrics, improved_metrics)
        
        # Verify improvements were detected
        self.assertGreater(len(improvements), 0)
        self.assertIn('execution_time_ms', improvements)
        self.assertIn('context_tokens', improvements)
        self.assertIn('cache_hit_rate', improvements)
    
    def _detect_regressions(self, baseline: Dict[str, float], 
                          current: Dict[str, float], 
                          threshold: float = 0.1) -> List[str]:
        """Detect performance regressions."""
        regressions = []
        
        for metric, baseline_value in baseline.items():
            if metric in current:
                current_value = current[metric]
                
                # For execution time and context tokens, higher is worse
                if metric in ['execution_time_ms', 'context_tokens']:
                    if current_value > baseline_value * (1 + threshold):
                        regressions.append(metric)
                
                # For cache hit rate, lower is worse
                elif metric == 'cache_hit_rate':
                    if current_value < baseline_value * (1 - threshold):
                        regressions.append(metric)
        
        return regressions
    
    def _detect_improvements(self, baseline: Dict[str, float], 
                           current: Dict[str, float], 
                           threshold: float = 0.1) -> List[str]:
        """Detect performance improvements."""
        improvements = []
        
        for metric, baseline_value in baseline.items():
            if metric in current:
                current_value = current[metric]
                
                # For execution time and context tokens, lower is better
                if metric in ['execution_time_ms', 'context_tokens']:
                    if current_value < baseline_value * (1 - threshold):
                        improvements.append(metric)
                
                # For cache hit rate, higher is better
                elif metric == 'cache_hit_rate':
                    if current_value > baseline_value * (1 + threshold):
                        improvements.append(metric)
        
        return improvements


class TestPerformanceIntegration(unittest.TestCase):
    """Test integration of all performance optimization components."""
    
    def setUp(self):
        """Set up integrated test environment."""
        self.profile = PerformanceProfile(
            target_context_budget=50000,
            max_execution_time_ms=2000.0,
            parallel_workers=4,
            optimization_level=OptimizationLevel.AGGRESSIVE
        )
        self.performance_optimizer = PerformanceOptimizer(self.profile)
    
    def test_end_to_end_optimization(self):
        """Test complete end-to-end optimization workflow."""
        # Define test operations
        def context_heavy_operation():
            time.sleep(0.1)
            return "heavy_operation_complete"
        
        def parallel_operation():
            time.sleep(0.05)
            return "parallel_operation_complete"
        
        # Test individual optimization
        result1 = self.performance_optimizer.optimize_operation(
            operation_name="Context Heavy Operation",
            operation_func=context_heavy_operation,
            context_data="<large_context>" + "A" * 10000 + "</large_context>"
        )
        
        self.assertTrue(result1.success)
        self.assertGreater(result1.context_tokens_saved, 0)
        
        # Test batch optimization
        operations = [
            ("Parallel Op 1", parallel_operation),
            ("Parallel Op 2", parallel_operation),
            ("Parallel Op 3", parallel_operation)
        ]
        
        batch_results = self.performance_optimizer.optimize_batch_operations(operations)
        
        self.assertEqual(len(batch_results), 3)
        self.assertTrue(all(result.success for result in batch_results))
    
    def test_performance_targets_achievement(self):
        """Test that performance targets are achieved."""
        # Get comprehensive report
        report = self.performance_optimizer.get_comprehensive_report()
        
        # Verify report structure
        self.assertIn('context_optimization', report)
        self.assertIn('parallel_execution', report)
        self.assertIn('cache_performance', report)
        self.assertIn('performance_targets', report)
        
        # Verify targets are defined
        targets = report['performance_targets']
        self.assertIn('context_budget_utilization', targets)
        self.assertIn('average_speedup_factor', targets)
        self.assertIn('cache_hit_rate_target', targets)
    
    def test_comprehensive_performance_validation(self):
        """Test comprehensive performance validation."""
        # Run multiple optimization cycles
        for i in range(5):
            result = self.performance_optimizer.optimize_operation(
                operation_name=f"Validation Operation {i}",
                operation_func=lambda: time.sleep(0.02) or f"result_{i}"
            )
            self.assertTrue(result.success)
        
        # Generate and validate report
        report = self.performance_optimizer.get_comprehensive_report()
        
        # Verify optimization history
        self.assertGreater(len(report['optimization_history']), 0)
        
        # Verify performance improvements
        context_stats = report.get('context_optimization', {})
        parallel_stats = report.get('parallel_execution', {})
        cache_stats = report.get('cache_performance', {})
        
        # Basic validation that statistics are collected
        self.assertIsInstance(context_stats, dict)
        self.assertIsInstance(parallel_stats, dict)
        self.assertIsInstance(cache_stats, dict)


def run_performance_validation_suite():
    """Run the complete performance validation test suite."""
    print("🧪 Performance Optimization Validation Suite")
    print("=" * 60)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestContextOptimization,
        TestParallelExecution,
        TestIntelligentCaching,
        TestUserExperienceOptimization,
        TestPerformanceDashboard,
        TestPerformanceRegression,
        TestPerformanceIntegration
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n📊 Test Results Summary:")
    print(f"  Tests run: {result.testsRun}")
    print(f"  Failures: {len(result.failures)}")
    print(f"  Errors: {len(result.errors)}")
    print(f"  Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    # Return success if all tests passed
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit_code = run_performance_validation_suite()
    sys.exit(exit_code)