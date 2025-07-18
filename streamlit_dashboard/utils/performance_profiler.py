"""
Performance profiler for Streamlit dashboard components.
Identifies bottlenecks and provides optimization recommendations.
"""

import time
import psutil
import tracemalloc
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import sys
from contextlib import contextmanager
import gc

@dataclass
class PerformanceMetric:
    """Individual performance measurement"""
    name: str
    duration: float
    memory_before: float
    memory_after: float
    memory_peak: float
    cpu_percent: float
    
    @property
    def memory_used(self) -> float:
        """Memory used during operation (MB)"""
        return self.memory_after - self.memory_before
    
    @property
    def memory_growth(self) -> float:
        """Memory growth relative to initial (MB)"""
        return max(0, self.memory_after - self.memory_before)

@dataclass
class ComponentProfile:
    """Performance profile for a component"""
    component_name: str
    initialization_time: float
    render_time: Optional[float] = None
    memory_footprint: float = 0.0
    module_load_time: Optional[float] = None
    total_methods_tested: int = 0
    performance_score: float = 0.0
    bottlenecks: List[str] = None
    recommendations: List[str] = None
    
    def __post_init__(self):
        if self.bottlenecks is None:
            self.bottlenecks = []
        if self.recommendations is None:
            self.recommendations = []

class PerformanceProfiler:
    """Comprehensive performance profiler for dashboard components"""
    
    def __init__(self):
        """Initialize the performance profiler"""
        self.metrics: List[PerformanceMetric] = []
        self.component_profiles: Dict[str, ComponentProfile] = {}
        self.baseline_memory = self._get_memory_usage()
        
    @contextmanager
    def profile_operation(self, operation_name: str):
        """Context manager to profile an operation"""
        # Start profiling
        tracemalloc.start()
        memory_before = self._get_memory_usage()
        cpu_start = psutil.cpu_percent()
        start_time = time.time()
        
        try:
            yield
        finally:
            # End profiling
            end_time = time.time()
            duration = end_time - start_time
            memory_after = self._get_memory_usage()
            
            # Get peak memory usage
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            memory_peak = peak / 1024 / 1024  # Convert to MB
            
            cpu_end = psutil.cpu_percent()
            avg_cpu = (cpu_start + cpu_end) / 2
            
            # Create metric
            metric = PerformanceMetric(
                name=operation_name,
                duration=duration,
                memory_before=memory_before,
                memory_after=memory_after,
                memory_peak=memory_peak,
                cpu_percent=avg_cpu
            )
            
            self.metrics.append(metric)
    
    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        process = psutil.Process()
        return process.memory_info().rss / 1024 / 1024
    
    def profile_component_initialization(self, component_class, framework_path: Path, component_name: str):
        """Profile component initialization"""
        
        with self.profile_operation(f"{component_name}_initialization"):
            component = component_class(framework_path=framework_path)
        
        # Extract initialization metrics
        init_metric = self.metrics[-1]
        
        profile = ComponentProfile(
            component_name=component_name,
            initialization_time=init_metric.duration,
            memory_footprint=init_metric.memory_used
        )
        
        # Test module loading if available
        if hasattr(component, '_load_all_modules'):
            with self.profile_operation(f"{component_name}_module_loading"):
                try:
                    modules = component._load_all_modules()
                    profile.module_load_time = self.metrics[-1].duration
                except Exception as e:
                    profile.bottlenecks.append(f"Module loading failed: {e}")
        
        # Generate performance score and recommendations
        profile.performance_score = self._calculate_performance_score(profile)
        profile.recommendations = self._generate_recommendations(profile)
        
        self.component_profiles[component_name] = profile
        return component
    
    def _calculate_performance_score(self, profile: ComponentProfile) -> float:
        """Calculate performance score (0-100)"""
        score = 100.0
        
        # Initialization time penalty
        if profile.initialization_time > 2.0:
            score -= 30
        elif profile.initialization_time > 1.0:
            score -= 15
        elif profile.initialization_time > 0.5:
            score -= 5
        
        # Module loading time penalty
        if profile.module_load_time is not None:
            if profile.module_load_time > 3.0:
                score -= 25
            elif profile.module_load_time > 1.0:
                score -= 10
        
        # Memory usage penalty
        if profile.memory_footprint > 100:  # MB
            score -= 20
        elif profile.memory_footprint > 50:
            score -= 10
        elif profile.memory_footprint > 20:
            score -= 5
        
        # Bottleneck penalty
        score -= len(profile.bottlenecks) * 10
        
        return max(0, score)
    
    def _generate_recommendations(self, profile: ComponentProfile) -> List[str]:
        """Generate performance recommendations"""
        recommendations = []
        
        if profile.initialization_time > 1.0:
            recommendations.append("Consider lazy initialization of heavy components")
            recommendations.append("Optimize import statements and dependencies")
        
        if profile.module_load_time and profile.module_load_time > 2.0:
            recommendations.append("Implement module caching to reduce load times")
            recommendations.append("Consider parallel module loading")
        
        if profile.memory_footprint > 50:
            recommendations.append("Review memory usage - consider data structure optimization")
            recommendations.append("Implement memory cleanup in component lifecycle")
        
        if len(profile.bottlenecks) > 0:
            recommendations.append("Address identified bottlenecks for better performance")
        
        if profile.performance_score < 70:
            recommendations.append("Component performance is below optimal - review critical paths")
        
        return recommendations
    
    def profile_dashboard_workflow(self, framework_path: Path):
        """Profile a complete dashboard workflow"""
        
        print("🔬 Profiling Complete Dashboard Workflow")
        print("=" * 50)
        
        # Add parent directory to path for imports
        parent_dir = Path(__file__).parent.parent
        if str(parent_dir) not in sys.path:
            sys.path.insert(0, str(parent_dir))
        
        # Profile key components
        components_to_test = [
            ("InteractivePromptBuilder", "components.interactive_prompt_builder", "InteractivePromptBuilder"),
            ("FrameworkOverview", "components.framework_overview", "FrameworkOverview"),
            ("CommandExplorer", "components.command_explorer", "CommandExplorer"),
            ("ContextAwareAnalyzer", "components.context_aware_analyzer", "ContextAwareAnalyzer"),
        ]
        
        for display_name, module_path, class_name in components_to_test:
            print(f"\n📊 Profiling {display_name}...")
            
            try:
                # Dynamic import
                module = __import__(module_path, fromlist=[class_name])
                component_class = getattr(module, class_name)
                
                # Profile the component
                self.profile_component_initialization(component_class, framework_path, display_name)
                
                profile = self.component_profiles[display_name]
                print(f"  ⏱️  Initialization: {profile.initialization_time:.3f}s")
                print(f"  💾 Memory: {profile.memory_footprint:.1f}MB")
                print(f"  📈 Score: {profile.performance_score:.1f}/100")
                
                if profile.module_load_time:
                    print(f"  📦 Module Load: {profile.module_load_time:.3f}s")
                
            except Exception as e:
                print(f"  ❌ Failed to profile {display_name}: {e}")
    
    def generate_performance_report(self) -> Dict[str, Any]:
        """Generate comprehensive performance report"""
        
        total_components = len(self.component_profiles)
        avg_init_time = sum(p.initialization_time for p in self.component_profiles.values()) / max(1, total_components)
        avg_memory = sum(p.memory_footprint for p in self.component_profiles.values()) / max(1, total_components)
        avg_score = sum(p.performance_score for p in self.component_profiles.values()) / max(1, total_components)
        
        # Identify slow components
        slow_components = [
            name for name, profile in self.component_profiles.items() 
            if profile.initialization_time > 1.0
        ]
        
        # Identify memory-heavy components
        memory_heavy = [
            name for name, profile in self.component_profiles.items()
            if profile.memory_footprint > 30
        ]
        
        # Overall optimization opportunities
        optimization_opportunities = []
        
        if avg_init_time > 0.5:
            optimization_opportunities.append("Overall initialization time high - consider lazy loading")
        
        if avg_memory > 25:
            optimization_opportunities.append("Memory usage above optimal - review data structures")
        
        if slow_components:
            optimization_opportunities.append(f"Slow components need attention: {', '.join(slow_components)}")
        
        if avg_score < 80:
            optimization_opportunities.append("Overall performance below target - systematic optimization needed")
        
        return {
            "summary": {
                "total_components_tested": total_components,
                "average_initialization_time": avg_init_time,
                "average_memory_footprint": avg_memory,
                "average_performance_score": avg_score,
                "overall_grade": self._calculate_overall_grade(avg_score)
            },
            "component_profiles": {name: profile for name, profile in self.component_profiles.items()},
            "bottlenecks": {
                "slow_components": slow_components,
                "memory_heavy_components": memory_heavy
            },
            "optimization_opportunities": optimization_opportunities,
            "detailed_metrics": [
                {
                    "name": metric.name,
                    "duration": metric.duration,
                    "memory_used": metric.memory_used,
                    "cpu_percent": metric.cpu_percent
                } for metric in self.metrics
            ]
        }
    
    def _calculate_overall_grade(self, avg_score: float) -> str:
        """Calculate overall performance grade"""
        if avg_score >= 90:
            return "A+ (Excellent)"
        elif avg_score >= 80:
            return "A (Very Good)"
        elif avg_score >= 70:
            return "B (Good)"
        elif avg_score >= 60:
            return "C (Acceptable)"
        else:
            return "D (Needs Improvement)"
    
    def print_performance_summary(self):
        """Print a formatted performance summary"""
        report = self.generate_performance_report()
        
        print("\n" + "=" * 60)
        print("📊 DASHBOARD PERFORMANCE REPORT")
        print("=" * 60)
        
        summary = report["summary"]
        print(f"🎯 Overall Grade: {summary['overall_grade']}")
        print(f"📈 Average Performance Score: {summary['average_performance_score']:.1f}/100")
        print(f"⏱️  Average Initialization Time: {summary['average_initialization_time']:.3f}s")
        print(f"💾 Average Memory Footprint: {summary['average_memory_footprint']:.1f}MB")
        
        print(f"\n📋 Components Tested: {summary['total_components_tested']}")
        
        # Component details
        for name, profile in report["component_profiles"].items():
            print(f"\n🔧 {name}:")
            print(f"   ⏱️  Init: {profile.initialization_time:.3f}s")
            print(f"   💾 Memory: {profile.memory_footprint:.1f}MB")
            print(f"   📈 Score: {profile.performance_score:.1f}/100")
            
            if profile.module_load_time:
                print(f"   📦 Module Load: {profile.module_load_time:.3f}s")
            
            if profile.bottlenecks:
                print(f"   ⚠️  Bottlenecks: {len(profile.bottlenecks)}")
        
        # Optimization opportunities
        if report["optimization_opportunities"]:
            print(f"\n💡 Optimization Opportunities:")
            for i, opportunity in enumerate(report["optimization_opportunities"], 1):
                print(f"   {i}. {opportunity}")
        
        # Bottom line
        if summary["average_performance_score"] >= 80:
            print("\n🎉 Dashboard performance is good! Minor optimizations available.")
        elif summary["average_performance_score"] >= 60:
            print("\n👍 Dashboard performance is acceptable. Some optimization recommended.")
        else:
            print("\n⚠️  Dashboard performance needs attention. Optimization required.")

def run_performance_analysis():
    """Run complete performance analysis"""
    
    # Initialize profiler
    profiler = PerformanceProfiler()
    
    # Get framework path
    framework_path = Path(__file__).parent.parent.parent / ".claude"
    
    if not framework_path.exists():
        print(f"⚠️  Framework path not found: {framework_path}")
        print("📝 Using current directory for testing...")
        framework_path = Path.cwd()
    
    # Run profiling
    profiler.profile_dashboard_workflow(framework_path)
    
    # Generate and display report
    profiler.print_performance_summary()
    
    return profiler

if __name__ == "__main__":
    run_performance_analysis()