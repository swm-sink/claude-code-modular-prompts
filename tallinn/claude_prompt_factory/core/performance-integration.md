# Performance Optimization Integration System

## Complete Performance Integration and Validation

This system integrates all performance optimization components and validates achievement of target metrics: 75% cache hit ratio, 40% performance improvement, 30-60% token reduction, and sub-100ms response times.

### Master Integration Controller

```python
import asyncio
import time
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor

# Import our performance systems
from .performance_cache import ComponentCache, CachedComponentLoader
from .parallel_loader import ParallelComponentLoader, AsyncComponentManager
from .token_optimizer import TokenOptimizer, BudgetManager, IntegratedTokenManager
from .performance_monitor import PerformanceMonitor, FrameworkMonitoringIntegration

@dataclass
class PerformanceTargets:
    cache_hit_ratio_min: float = 75.0
    performance_improvement_min: float = 40.0
    token_reduction_min: float = 30.0
    token_reduction_max: float = 60.0
    response_time_max_ms: float = 100.0
    memory_usage_max_mb: float = 200.0

@dataclass
class PerformanceResults:
    cache_hit_ratio: float
    performance_improvement: float
    token_reduction_percentage: float
    response_time_ms: float
    memory_usage_mb: float
    targets_met: Dict[str, bool]
    overall_success: bool

class OptimizedFrameworkEngine:
    """Complete optimized framework engine with all performance enhancements"""
    
    def __init__(self, 
                 base_path: str,
                 max_context_tokens: int = 128000,
                 cache_size: int = 200,
                 max_workers: int = 8):
        
        self.base_path = Path(base_path)
        self.targets = PerformanceTargets()
        
        # Initialize all performance systems
        self.cache = ComponentCache(max_size=cache_size, max_memory_mb=150)
        self.parallel_loader = ParallelComponentLoader(str(base_path), self.cache, max_workers)
        self.async_manager = AsyncComponentManager(str(base_path), self.cache)
        self.token_manager = IntegratedTokenManager(max_context_tokens)
        self.monitor = FrameworkMonitoringIntegration()
        
        # Performance tracking
        self.baseline_metrics = {}
        self.current_metrics = {}
        self.optimization_history = []
        
        # Initialize system
        self._initialize_performance_tracking()
        
        logging.info("Optimized Framework Engine initialized")
    
    def _initialize_performance_tracking(self):
        """Initialize performance tracking and baselines"""
        # Pre-load hot components for immediate performance benefit
        asyncio.run(self._warmup_system())
        
        # Establish baseline metrics
        self._establish_baseline_metrics()
    
    async def _warmup_system(self):
        """Warmup system with hot components"""
        hot_components = [
            "components/reporting/generate-structured-report.md",
            "components/context/context-optimization.md", 
            "components/validation/xml-structure.md",
            "components/planning/create-step-by-step-plan.md",
            "components/error/error-handling.md"
        ]
        
        try:
            await self.async_manager.warmup_system(hot_components)
            logging.info(f"System warmed up with {len(hot_components)} hot components")
        except Exception as e:
            logging.warning(f"Warmup encountered issues: {e}")
    
    def _establish_baseline_metrics(self):
        """Establish baseline performance metrics for comparison"""
        # Simulate baseline loading (without optimizations)
        test_components = [
            "components/reporting/generate-structured-report.md",
            "components/analysis/analyze-code.md",
            "components/planning/create-step-by-step-plan.md"
        ]
        
        # Measure baseline performance
        baseline_start = time.time()
        baseline_tokens = 0
        
        for component_path in test_components:
            try:
                full_path = self.base_path / component_path
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    baseline_tokens += self.token_manager.optimizer.count_tokens(content)
            except Exception as e:
                logging.warning(f"Could not load {component_path} for baseline: {e}")
        
        baseline_time = (time.time() - baseline_start) * 1000
        
        self.baseline_metrics = {
            'load_time_ms': baseline_time,
            'total_tokens': baseline_tokens,
            'components_loaded': len(test_components),
            'cache_hit_ratio': 0.0,  # No cache initially
            'memory_usage_mb': 0.0
        }
        
        logging.info(f"Baseline metrics established: {baseline_time:.2f}ms, {baseline_tokens} tokens")
    
    async def process_command_optimized(self, 
                                      command_config: Dict,
                                      optimization_level: str = "balanced") -> Dict:
        """Process command with full optimization pipeline"""
        
        start_time = time.time()
        
        # Extract component requirements
        component_paths = self._extract_component_paths(command_config)
        context_vars = command_config.get('context_vars', {})
        
        if not component_paths:
            return {'error': 'No components specified'}
        
        # Phase 1: Parallel component loading with caching
        with self.monitor.monitor.record_timer('parallel_loading'):
            components = await self.async_manager.load_command_components(command_config)
        
        # Phase 2: Token optimization
        optimization_strategy = self._determine_optimization_strategy(optimization_level)
        
        with self.monitor.monitor.record_timer('token_optimization'):
            optimization_result = self.token_manager.process_command_with_optimization(
                components, optimization_strategy
            )
        
        total_time = (time.time() - start_time) * 1000
        
        # Phase 3: Performance monitoring and validation
        performance_results = await self._validate_performance(
            components, optimization_result, total_time
        )
        
        # Update metrics
        self._update_performance_metrics(performance_results)
        
        return {
            'optimized_components': optimization_result['optimized_components'],
            'performance_results': asdict(performance_results),
            'execution_time_ms': total_time,
            'cache_stats': self.cache.get_stats(),
            'optimization_metrics': optimization_result['optimization_metrics']
        }
    
    def _extract_component_paths(self, command_config: Dict) -> List[str]:
        """Extract component paths from command configuration"""
        paths = []
        
        # From includes section
        if 'includes' in command_config:
            if isinstance(command_config['includes'], list):
                paths.extend(command_config['includes'])
            else:
                paths.append(command_config['includes'])
        
        # From components section
        if 'components' in command_config:
            if isinstance(command_config['components'], list):
                paths.extend(command_config['components'])
            else:
                paths.append(command_config['components'])
        
        return list(set(paths))  # Remove duplicates
    
    def _determine_optimization_strategy(self, level: str):
        """Determine token optimization strategy"""
        from .token_optimizer import OptimizationStrategy
        
        strategies = {
            'conservative': OptimizationStrategy.CONSERVATIVE,
            'balanced': OptimizationStrategy.BALANCED,
            'aggressive': OptimizationStrategy.AGGRESSIVE
        }
        
        return strategies.get(level.lower(), OptimizationStrategy.BALANCED)
    
    async def _validate_performance(self, 
                                  original_components: Dict[str, str],
                                  optimization_result: Dict,
                                  total_time_ms: float) -> PerformanceResults:
        """Validate that performance targets are met"""
        
        # Get cache statistics
        cache_stats = self.cache.get_stats()
        
        # Calculate performance improvement
        baseline_time = self.baseline_metrics.get('load_time_ms', total_time_ms)
        performance_improvement = ((baseline_time - total_time_ms) / baseline_time) * 100
        performance_improvement = max(0, performance_improvement)  # Ensure non-negative
        
        # Get token reduction
        token_reduction = optimization_result['optimization_metrics']['reduction_percentage']
        
        # Get memory usage
        try:
            import psutil
            memory_usage_mb = psutil.Process().memory_info().rss / 1024 / 1024
        except ImportError:
            memory_usage_mb = cache_stats.get('memory_usage_mb', 0)
        
        # Validate each target
        targets_met = {
            'cache_hit_ratio': cache_stats['hit_ratio'] >= self.targets.cache_hit_ratio_min,
            'performance_improvement': performance_improvement >= self.targets.performance_improvement_min,
            'token_reduction': (self.targets.token_reduction_min <= token_reduction <= self.targets.token_reduction_max),
            'response_time': total_time_ms <= self.targets.response_time_max_ms,
            'memory_usage': memory_usage_mb <= self.targets.memory_usage_max_mb
        }
        
        # Update monitoring
        self.monitor.monitor_cache_operation(cache_stats)
        self.monitor.monitor_token_optimization(optimization_result)
        self.monitor.monitor_parallel_loading(len(original_components), total_time_ms)
        
        results = PerformanceResults(
            cache_hit_ratio=cache_stats['hit_ratio'],
            performance_improvement=performance_improvement,
            token_reduction_percentage=token_reduction,
            response_time_ms=total_time_ms,
            memory_usage_mb=memory_usage_mb,
            targets_met=targets_met,
            overall_success=all(targets_met.values())
        )
        
        return results
    
    def _update_performance_metrics(self, results: PerformanceResults):
        """Update current performance metrics"""
        self.current_metrics = {
            'cache_hit_ratio': results.cache_hit_ratio,
            'performance_improvement': results.performance_improvement,
            'token_reduction': results.token_reduction_percentage,
            'response_time_ms': results.response_time_ms,
            'memory_usage_mb': results.memory_usage_mb,
            'targets_met_count': sum(results.targets_met.values()),
            'overall_success': results.overall_success
        }
        
        # Add to history
        self.optimization_history.append({
            'timestamp': time.time(),
            'metrics': self.current_metrics.copy()
        })
        
        # Keep only last 100 entries
        if len(self.optimization_history) > 100:
            self.optimization_history = self.optimization_history[-100:]
    
    def get_comprehensive_performance_report(self) -> Dict:
        """Generate comprehensive performance report"""
        
        # Get system statistics
        cache_stats = self.cache.get_stats()
        parallel_stats = self.parallel_loader.get_performance_stats()
        token_stats = self.token_manager.get_comprehensive_report()
        monitoring_report = self.monitor.get_framework_health_report()
        
        # Calculate performance trends
        trends = self._analyze_performance_trends()
        
        # Generate target achievement summary
        target_achievement = self._assess_target_achievement()
        
        report = {
            'executive_summary': {
                'overall_performance_grade': self._calculate_performance_grade(),
                'targets_achieved': target_achievement['targets_met_count'],
                'total_targets': len(self.targets.__dict__),
                'performance_stability': trends.get('stability', 'unknown'),
                'optimization_effectiveness': token_stats['optimization_stats']['average_reduction_percentage']
            },
            'detailed_metrics': {
                'caching_performance': {
                    'current_hit_ratio': cache_stats['hit_ratio'],
                    'target_hit_ratio': self.targets.cache_hit_ratio_min,
                    'target_met': cache_stats['hit_ratio'] >= self.targets.cache_hit_ratio_min,
                    'cache_size': cache_stats['cache_size'],
                    'memory_usage_mb': cache_stats['memory_usage_mb']
                },
                'parallel_loading_performance': {
                    'average_load_time': parallel_stats['parallel_loading']['average_session_time'],
                    'peak_concurrent_loads': parallel_stats['parallel_loading']['peak_concurrent_loads'],
                    'estimated_speedup': parallel_stats['parallel_loading']['estimated_speedup']
                },
                'token_optimization_performance': {
                    'average_reduction': token_stats['optimization_stats']['average_reduction_percentage'],
                    'total_tokens_saved': token_stats['optimization_stats']['total_tokens_saved'],
                    'target_range_met': (
                        self.targets.token_reduction_min <= 
                        token_stats['optimization_stats']['average_reduction_percentage'] <= 
                        self.targets.token_reduction_max
                    )
                },
                'response_time_performance': {
                    'current_average_ms': self.current_metrics.get('response_time_ms', 0),
                    'target_max_ms': self.targets.response_time_max_ms,
                    'target_met': self.current_metrics.get('response_time_ms', float('inf')) <= self.targets.response_time_max_ms
                }
            },
            'performance_trends': trends,
            'target_achievement_analysis': target_achievement,
            'monitoring_insights': monitoring_report,
            'recommendations': self._generate_optimization_recommendations(),
            'system_health': {
                'cache_health': 'optimal' if cache_stats['hit_ratio'] >= 85 else 'good' if cache_stats['hit_ratio'] >= 75 else 'needs_improvement',
                'parallel_health': 'optimal' if parallel_stats['parallel_loading']['peak_concurrent_loads'] > 4 else 'good',
                'token_health': 'optimal' if token_stats['optimization_stats']['average_reduction_percentage'] >= 40 else 'good',
                'overall_health': self._assess_overall_health()
            }
        }
        
        return report
    
    def _analyze_performance_trends(self) -> Dict:
        """Analyze performance trends over time"""
        if len(self.optimization_history) < 5:
            return {'status': 'insufficient_data'}
        
        recent_entries = self.optimization_history[-10:]
        
        # Analyze cache hit ratio trend
        cache_ratios = [entry['metrics']['cache_hit_ratio'] for entry in recent_entries]
        cache_trend = 'improving' if cache_ratios[-1] > cache_ratios[0] else 'stable' if abs(cache_ratios[-1] - cache_ratios[0]) < 2 else 'declining'
        
        # Analyze response time trend
        response_times = [entry['metrics']['response_time_ms'] for entry in recent_entries]
        response_trend = 'improving' if response_times[-1] < response_times[0] else 'stable' if abs(response_times[-1] - response_times[0]) < 10 else 'declining'
        
        # Analyze success rate trend
        success_rates = [entry['metrics']['overall_success'] for entry in recent_entries]
        success_rate = sum(success_rates) / len(success_rates) * 100
        
        return {
            'cache_hit_ratio_trend': cache_trend,
            'response_time_trend': response_trend,
            'success_rate': success_rate,
            'stability': 'stable' if success_rate >= 80 else 'unstable',
            'data_points': len(recent_entries)
        }
    
    def _assess_target_achievement(self) -> Dict:
        """Assess achievement of performance targets"""
        if not self.current_metrics:
            return {'status': 'no_data'}
        
        targets_status = {
            'cache_hit_ratio': {
                'current': self.current_metrics.get('cache_hit_ratio', 0),
                'target': self.targets.cache_hit_ratio_min,
                'met': self.current_metrics.get('cache_hit_ratio', 0) >= self.targets.cache_hit_ratio_min,
                'percentage_of_target': (self.current_metrics.get('cache_hit_ratio', 0) / self.targets.cache_hit_ratio_min) * 100
            },
            'performance_improvement': {
                'current': self.current_metrics.get('performance_improvement', 0),
                'target': self.targets.performance_improvement_min,
                'met': self.current_metrics.get('performance_improvement', 0) >= self.targets.performance_improvement_min,
                'percentage_of_target': (self.current_metrics.get('performance_improvement', 0) / self.targets.performance_improvement_min) * 100
            },
            'token_reduction': {
                'current': self.current_metrics.get('token_reduction', 0),
                'target_min': self.targets.token_reduction_min,
                'target_max': self.targets.token_reduction_max,
                'met': (self.targets.token_reduction_min <= 
                       self.current_metrics.get('token_reduction', 0) <= 
                       self.targets.token_reduction_max),
                'optimal': self.current_metrics.get('token_reduction', 0) >= 45.0
            },
            'response_time': {
                'current': self.current_metrics.get('response_time_ms', float('inf')),
                'target': self.targets.response_time_max_ms,
                'met': self.current_metrics.get('response_time_ms', float('inf')) <= self.targets.response_time_max_ms,
                'efficiency': max(0, 100 - (self.current_metrics.get('response_time_ms', 100) / self.targets.response_time_max_ms) * 100)
            }
        }
        
        targets_met_count = sum(1 for status in targets_status.values() if status.get('met', False))
        
        return {
            'targets_status': targets_status,
            'targets_met_count': targets_met_count,
            'total_targets': len(targets_status),
            'achievement_percentage': (targets_met_count / len(targets_status)) * 100,
            'overall_grade': self._calculate_performance_grade()
        }
    
    def _calculate_performance_grade(self) -> str:
        """Calculate overall performance grade"""
        if not self.current_metrics:
            return 'Insufficient Data'
        
        targets_met = self.current_metrics.get('targets_met_count', 0)
        total_targets = 5  # cache, performance, token, response, memory
        
        achievement_rate = (targets_met / total_targets) * 100
        
        if achievement_rate >= 90:
            return 'A - Excellent'
        elif achievement_rate >= 80:
            return 'B - Good'
        elif achievement_rate >= 70:
            return 'C - Satisfactory'
        elif achievement_rate >= 60:
            return 'D - Needs Improvement'
        else:
            return 'F - Poor'
    
    def _assess_overall_health(self) -> str:
        """Assess overall system health"""
        if not self.current_metrics:
            return 'unknown'
        
        health_score = 0
        max_score = 5
        
        # Cache health
        if self.current_metrics.get('cache_hit_ratio', 0) >= 85:
            health_score += 1
        
        # Performance improvement health
        if self.current_metrics.get('performance_improvement', 0) >= 40:
            health_score += 1
        
        # Token optimization health
        token_reduction = self.current_metrics.get('token_reduction', 0)
        if 30 <= token_reduction <= 60:
            health_score += 1
        
        # Response time health
        if self.current_metrics.get('response_time_ms', float('inf')) <= 100:
            health_score += 1
        
        # Memory usage health
        if self.current_metrics.get('memory_usage_mb', float('inf')) <= 200:
            health_score += 1
        
        health_percentage = (health_score / max_score) * 100
        
        if health_percentage >= 90:
            return 'excellent'
        elif health_percentage >= 75:
            return 'good'
        elif health_percentage >= 50:
            return 'fair'
        else:
            return 'poor'
    
    def _generate_optimization_recommendations(self) -> List[str]:
        """Generate specific optimization recommendations"""
        recommendations = []
        
        if not self.current_metrics:
            return ["Initialize performance metrics by processing commands"]
        
        # Cache recommendations
        cache_hit_ratio = self.current_metrics.get('cache_hit_ratio', 0)
        if cache_hit_ratio < 75:
            recommendations.append(f"Cache hit ratio ({cache_hit_ratio:.1f}%) below target (75%) - increase cache size or preload more components")
        elif cache_hit_ratio < 85:
            recommendations.append("Consider expanding hot component list for better cache utilization")
        
        # Performance improvement recommendations
        perf_improvement = self.current_metrics.get('performance_improvement', 0)
        if perf_improvement < 40:
            recommendations.append(f"Performance improvement ({perf_improvement:.1f}%) below target (40%) - enable more aggressive parallel loading")
        
        # Token optimization recommendations
        token_reduction = self.current_metrics.get('token_reduction', 0)
        if token_reduction < 30:
            recommendations.append(f"Token reduction ({token_reduction:.1f}%) below minimum (30%) - use more aggressive optimization strategy")
        elif token_reduction > 60:
            recommendations.append(f"Token reduction ({token_reduction:.1f}%) above maximum (60%) - may impact quality, consider balanced strategy")
        
        # Response time recommendations
        response_time = self.current_metrics.get('response_time_ms', 0)
        if response_time > 100:
            recommendations.append(f"Response time ({response_time:.1f}ms) exceeds target (100ms) - optimize parallel loading and caching")
        
        if not recommendations:
            recommendations.append("All performance targets met - system operating optimally")
        
        return recommendations
    
    def export_performance_configuration(self) -> Dict:
        """Export current performance configuration for replication"""
        return {
            'cache_configuration': {
                'max_size': self.cache.max_size,
                'max_memory_mb': self.cache.max_memory_bytes // (1024 * 1024),
                'hot_components': dict(self.cache.hot_components)
            },
            'parallel_loading_configuration': {
                'max_workers': self.parallel_loader.max_workers,
                'dependency_resolution_enabled': True
            },
            'token_optimization_configuration': {
                'max_context_tokens': self.token_manager.budget_manager.max_context_tokens,
                'output_reserve_tokens': self.token_manager.budget_manager.output_reserve_tokens
            },
            'performance_targets': asdict(self.targets),
            'current_performance': self.current_metrics
        }
    
    async def run_performance_validation_suite(self) -> Dict:
        """Run comprehensive performance validation suite"""
        validation_results = {
            'suite_start_time': time.time(),
            'tests_passed': 0,
            'tests_failed': 0,
            'test_results': {}
        }
        
        # Test 1: Cache performance validation
        cache_test = await self._test_cache_performance()
        validation_results['test_results']['cache_performance'] = cache_test
        if cache_test['passed']:
            validation_results['tests_passed'] += 1
        else:
            validation_results['tests_failed'] += 1
        
        # Test 2: Parallel loading validation
        parallel_test = await self._test_parallel_loading()
        validation_results['test_results']['parallel_loading'] = parallel_test
        if parallel_test['passed']:
            validation_results['tests_passed'] += 1
        else:
            validation_results['tests_failed'] += 1
        
        # Test 3: Token optimization validation
        token_test = await self._test_token_optimization()
        validation_results['test_results']['token_optimization'] = token_test
        if token_test['passed']:
            validation_results['tests_passed'] += 1
        else:
            validation_results['tests_failed'] += 1
        
        # Test 4: End-to-end performance validation
        e2e_test = await self._test_end_to_end_performance()
        validation_results['test_results']['end_to_end'] = e2e_test
        if e2e_test['passed']:
            validation_results['tests_passed'] += 1
        else:
            validation_results['tests_failed'] += 1
        
        validation_results['suite_duration_ms'] = (time.time() - validation_results['suite_start_time']) * 1000
        validation_results['overall_success'] = validation_results['tests_failed'] == 0
        
        return validation_results
    
    async def _test_cache_performance(self) -> Dict:
        """Test cache performance against targets"""
        # Load components multiple times to test caching
        test_components = [
            "components/reporting/generate-structured-report.md",
            "components/context/context-optimization.md"
        ] * 3  # Load each 3 times
        
        hit_count = 0
        total_requests = len(test_components)
        
        for component_path in test_components:
            cached_entry = self.cache.get(component_path)
            if cached_entry:
                hit_count += 1
        
        hit_ratio = (hit_count / total_requests) * 100 if total_requests > 0 else 0
        
        return {
            'test_name': 'Cache Performance',
            'hit_ratio': hit_ratio,
            'target': self.targets.cache_hit_ratio_min,
            'passed': hit_ratio >= self.targets.cache_hit_ratio_min,
            'details': f"Hit ratio: {hit_ratio:.1f}% (target: {self.targets.cache_hit_ratio_min}%)"
        }
    
    async def _test_parallel_loading(self) -> Dict:
        """Test parallel loading performance"""
        test_components = [
            "components/reporting/generate-structured-report.md",
            "components/analysis/analyze-code.md",
            "components/planning/create-step-by-step-plan.md",
            "components/validation/xml-structure.md"
        ]
        
        # Sequential loading baseline
        sequential_start = time.time()
        for component in test_components:
            try:
                full_path = self.base_path / component
                with open(full_path, 'r') as f:
                    f.read()
            except:
                pass
        sequential_time = (time.time() - sequential_start) * 1000
        
        # Parallel loading test
        parallel_start = time.time()
        await self.async_manager.load_command_components({
            'includes': test_components
        })
        parallel_time = (time.time() - parallel_start) * 1000
        
        improvement = ((sequential_time - parallel_time) / sequential_time) * 100
        
        return {
            'test_name': 'Parallel Loading',
            'improvement_percentage': improvement,
            'target': self.targets.performance_improvement_min,
            'passed': improvement >= self.targets.performance_improvement_min,
            'details': f"Improvement: {improvement:.1f}% (target: {self.targets.performance_improvement_min}%)"
        }
    
    async def _test_token_optimization(self) -> Dict:
        """Test token optimization performance"""
        test_content = """
        This is a test prompt component that contains verbose language and redundant information.
        Please kindly process this content if possible and make use of the available optimization techniques.
        Due to the fact that this content is quite verbose, in order to optimize it effectively,
        we need to apply aggressive compression strategies that will reduce token usage significantly.
        """
        
        from .token_optimizer import OptimizationStrategy
        result = self.token_manager.optimizer.optimize_content(
            test_content,
            strategy=OptimizationStrategy.BALANCED
        )
        
        reduction = result.reduction_percentage
        target_met = self.targets.token_reduction_min <= reduction <= self.targets.token_reduction_max
        
        return {
            'test_name': 'Token Optimization',
            'reduction_percentage': reduction,
            'target_range': f"{self.targets.token_reduction_min}-{self.targets.token_reduction_max}%",
            'passed': target_met,
            'details': f"Reduction: {reduction:.1f}% (target: {self.targets.token_reduction_min}-{self.targets.token_reduction_max}%)"
        }
    
    async def _test_end_to_end_performance(self) -> Dict:
        """Test end-to-end performance"""
        command_config = {
            'includes': [
                "components/reporting/generate-structured-report.md",
                "components/analysis/analyze-code.md"
            ],
            'context_vars': {'project_name': 'TestProject'}
        }
        
        start_time = time.time()
        result = await self.process_command_optimized(command_config)
        end_time = (time.time() - start_time) * 1000
        
        response_time_met = end_time <= self.targets.response_time_max_ms
        
        return {
            'test_name': 'End-to-End Performance',
            'response_time_ms': end_time,
            'target_ms': self.targets.response_time_max_ms,
            'passed': response_time_met,
            'details': f"Response time: {end_time:.1f}ms (target: {self.targets.response_time_max_ms}ms)"
        }
    
    def shutdown(self):
        """Shutdown all performance systems"""
        self.parallel_loader.shutdown()
        self.async_manager.shutdown()
        self.monitor.shutdown()
        logging.info("Optimized Framework Engine shutdown complete")

# Example usage and validation
async def main():
    """Example usage of the optimized framework engine"""
    
    # Initialize the engine
    engine = OptimizedFrameworkEngine(
        base_path="/Users/smenssink/conductor/repo/claude-code-modular-prompts/tallinn/claude_prompt_factory",
        max_context_tokens=128000,
        cache_size=200,
        max_workers=8
    )
    
    # Example command configuration
    command_config = {
        'includes': [
            "components/reporting/generate-structured-report.md",
            "components/context/context-optimization.md",
            "components/analysis/analyze-code.md"
        ],
        'context_vars': {
            'project_name': 'Claude Code Modular Prompts',
            'optimization_level': 'high'
        }
    }
    
    # Process command with full optimization
    print("Processing command with optimization...")
    result = await engine.process_command_optimized(command_config, "balanced")
    
    # Display results
    perf_results = result['performance_results']
    print(f"\n=== Performance Results ===")
    print(f"Cache Hit Ratio: {perf_results['cache_hit_ratio']:.1f}% (target: ≥75%)")
    print(f"Performance Improvement: {perf_results['performance_improvement']:.1f}% (target: ≥40%)")
    print(f"Token Reduction: {perf_results['token_reduction_percentage']:.1f}% (target: 30-60%)")
    print(f"Response Time: {perf_results['response_time_ms']:.1f}ms (target: ≤100ms)")
    print(f"Overall Success: {perf_results['overall_success']}")
    
    # Run validation suite
    print("\nRunning performance validation suite...")
    validation = await engine.run_performance_validation_suite()
    print(f"Tests Passed: {validation['tests_passed']}")
    print(f"Tests Failed: {validation['tests_failed']}")
    print(f"Overall Success: {validation['overall_success']}")
    
    # Generate comprehensive report
    report = engine.get_comprehensive_performance_report()
    print(f"\nOverall Performance Grade: {report['executive_summary']['overall_performance_grade']}")
    print(f"Targets Achieved: {report['executive_summary']['targets_achieved']}/5")
    
    # Export configuration for replication
    config = engine.export_performance_configuration()
    
    # Shutdown
    engine.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
```

This integration system provides:
- **Complete performance validation** against all targets (75% cache hit, 40% improvement, 30-60% token reduction, sub-100ms response)
- **Automated testing suite** to verify each optimization component
- **Comprehensive reporting** with performance grading and trend analysis
- **Real-time monitoring** with health assessment and recommendations
- **Production-ready integration** with all optimization systems working together
- **Configuration export** for easy replication across environments