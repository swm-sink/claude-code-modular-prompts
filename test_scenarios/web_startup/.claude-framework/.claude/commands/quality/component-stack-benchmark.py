#!/usr/bin/env python3
"""
Component Stack Performance Benchmarking
Deep analysis of component loading efficiency and stack optimization.

Focus: Component dependency loading, stack efficiency, memory optimization
"""

import os
import sys
import time
import psutil
import json
import re
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple, Set
from datetime import datetime

@dataclass
class ComponentMetrics:
    """Individual component performance metrics"""
    name: str
    load_time_ms: float
    memory_usage_mb: float
    file_size_kb: float
    dependencies: List[str]
    imports: List[str]
    content_sections: int
    complexity_score: float

@dataclass
class StackMetrics:
    """Component stack performance metrics"""
    stack_name: str
    total_load_time_ms: float
    peak_memory_mb: float
    component_count: int
    dependency_depth: int
    loading_efficiency: float
    optimization_potential: str

class ComponentStackBenchmarker:
    """Advanced component stack performance analysis"""
    
    def __init__(self, components_dir: str):
        self.components_dir = Path(components_dir)
        self.component_cache = {}
        self.dependency_graph = {}
        
        # Stack definitions from integration-test-matrices.md
        self.component_stacks = {
            'orchestration': {
                'components': ['dag-orchestrator', 'task-execution', 'progress-tracking'],
                'load_order': ['dag-orchestrator', 'task-execution', 'progress-tracking'],
                'expected_load_time': 45,  # ms
                'dependencies': 3
            },
            'validation': {
                'components': ['validation-framework', 'security-validation', 'input-validation'],
                'load_order': ['validation-framework', 'input-validation', 'security-validation'],
                'expected_load_time': 25,  # ms
                'dependencies': 2
            },
            'context': {
                'components': ['hierarchical-loading', 'context-optimization', 'adaptive-thinking'],
                'load_order': ['hierarchical-loading', 'context-optimization', 'adaptive-thinking'],
                'expected_load_time': 65,  # ms
                'dependencies': 4
            },
            'intelligence': {
                'components': ['cognitive-architecture', 'pattern-extraction', 'multi-agent-coordination'],
                'load_order': ['cognitive-architecture', 'pattern-extraction', 'multi-agent-coordination'],
                'expected_load_time': 70,  # ms
                'dependencies': 5
            },
            'testing': {
                'components': ['testing-framework', 'framework-validation', 'mutation-testing'],
                'load_order': ['testing-framework', 'framework-validation', 'mutation-testing'],
                'expected_load_time': 40,  # ms
                'dependencies': 3
            },
            'error': {
                'components': ['error-handling', 'circuit-breaker', 'chaos-engineering'],
                'load_order': ['error-handling', 'circuit-breaker', 'chaos-engineering'],
                'expected_load_time': 30,  # ms
                'dependencies': 2
            },
            'performance': {
                'components': ['component-cache', 'framework-optimization', 'performance-optimization'],
                'load_order': ['component-cache', 'framework-optimization', 'performance-optimization'],
                'expected_load_time': 15,  # ms
                'dependencies': 1
            },
            'security': {
                'components': ['secure-config', 'owasp-compliance', 'anti-pattern-detection'],
                'load_order': ['secure-config', 'owasp-compliance', 'anti-pattern-detection'],
                'expected_load_time': 50,  # ms
                'dependencies': 4
            }
        }

    def find_component_file(self, component_name: str) -> Optional[Path]:
        """Find component file with intelligent matching"""
        # Direct match
        direct_matches = list(self.components_dir.glob(f'**/{component_name}.md'))
        if direct_matches:
            return direct_matches[0]
        
        # Try with underscores
        underscore_name = component_name.replace('-', '_')
        underscore_matches = list(self.components_dir.glob(f'**/{underscore_name}.md'))
        if underscore_matches:
            return underscore_matches[0]
        
        # Try partial matching
        for pattern in [f'**/*{component_name}*.md', f'**/*{component_name.split("-")[0]}*.md']:
            partial_matches = list(self.components_dir.glob(pattern))
            if partial_matches:
                return partial_matches[0]
        
        return None

    def analyze_component_content(self, file_path: Path) -> Tuple[List[str], List[str], int, float]:
        """Analyze component content for dependencies, imports, sections, and complexity"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract dependencies (imports and references)
            dependencies = []
            imports = []
            
            # Find @import statements
            import_matches = re.findall(r'@import\s+([^\s\n]+)', content, re.IGNORECASE)
            imports.extend(import_matches)
            
            # Find component references
            component_refs = re.findall(r'components/([^/\s)]+)', content)
            dependencies.extend(component_refs)
            
            # Find other dependencies
            dep_patterns = [
                r'requires:\s*([^\n]+)',
                r'depends_on:\s*([^\n]+)',
                r'uses:\s*([^\n]+)'
            ]
            
            for pattern in dep_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    deps = [d.strip() for d in match.split(',')]
                    dependencies.extend(deps)
            
            # Count content sections
            sections = len(re.findall(r'^#{1,6}\s', content, re.MULTILINE))
            
            # Calculate complexity score
            complexity_indicators = {
                'file_size': len(content),
                'sections': sections,
                'code_blocks': len(re.findall(r'```', content)),
                'imports': len(imports),
                'dependencies': len(dependencies),
                'tools_usage': len(re.findall(r'tools:\s*\[([^\]]+)\]', content, re.IGNORECASE)),
                'conditional_logic': len(re.findall(r'\bif\b|\bwhen\b|\bunless\b', content, re.IGNORECASE))
            }
            
            complexity_score = (
                complexity_indicators['file_size'] / 1000 +
                complexity_indicators['sections'] * 2 +
                complexity_indicators['code_blocks'] * 3 +
                complexity_indicators['imports'] * 5 +
                complexity_indicators['dependencies'] * 4 +
                complexity_indicators['tools_usage'] * 10 +
                complexity_indicators['conditional_logic'] * 2
            )
            
            return dependencies, imports, sections, complexity_score
            
        except Exception as e:
            print(f"Error analyzing component {file_path}: {e}")
            return [], [], 0, 0.0

    def measure_component_performance(self, component_name: str) -> Optional[ComponentMetrics]:
        """Measure individual component loading performance"""
        component_file = self.find_component_file(component_name)
        if not component_file:
            return None
        
        process = psutil.Process()
        memory_before = process.memory_info().rss / 1024 / 1024
        
        start_time = time.perf_counter()
        
        try:
            dependencies, imports, sections, complexity = self.analyze_component_content(component_file)
            
            # Simulate component processing overhead based on complexity
            processing_time = complexity * 0.001  # ms per complexity point
            time.sleep(processing_time / 1000)  # Convert to seconds
            
        except Exception as e:
            print(f"Error processing component {component_name}: {e}")
            return None
        
        end_time = time.perf_counter()
        memory_after = process.memory_info().rss / 1024 / 1024
        
        load_time_ms = (end_time - start_time) * 1000
        memory_usage_mb = memory_after - memory_before
        file_size_kb = component_file.stat().st_size / 1024
        
        return ComponentMetrics(
            name=component_name,
            load_time_ms=load_time_ms,
            memory_usage_mb=memory_usage_mb,
            file_size_kb=file_size_kb,
            dependencies=dependencies,
            imports=imports,
            content_sections=sections,
            complexity_score=complexity
        )

    def benchmark_component_stack(self, stack_name: str, stack_config: Dict) -> StackMetrics:
        """Benchmark complete component stack performance"""
        print(f"  📦 Benchmarking {stack_name} stack...")
        
        components = stack_config['components']
        load_order = stack_config['load_order']
        expected_time = stack_config['expected_load_time']
        
        total_load_time = 0
        peak_memory = 0
        loaded_components = 0
        total_complexity = 0
        
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024
        
        # Load components in specified order
        for component_name in load_order:
            component_metrics = self.measure_component_performance(component_name)
            
            if component_metrics:
                total_load_time += component_metrics.load_time_ms
                total_complexity += component_metrics.complexity_score
                loaded_components += 1
                
                current_memory = process.memory_info().rss / 1024 / 1024
                peak_memory = max(peak_memory, current_memory - initial_memory)
                
                print(f"    ✓ {component_name}: {component_metrics.load_time_ms:.2f}ms (complexity: {component_metrics.complexity_score:.1f})")
            else:
                print(f"    ✗ {component_name}: not found")
        
        # Calculate efficiency metrics
        if loaded_components > 0:
            loading_efficiency = (loaded_components / len(components)) * 100
            
            # Determine optimization potential
            if total_load_time <= expected_time * 0.5:
                optimization_potential = "excellent"
            elif total_load_time <= expected_time:
                optimization_potential = "good"
            elif total_load_time <= expected_time * 1.5:
                optimization_potential = "moderate"
            else:
                optimization_potential = "high"
        else:
            loading_efficiency = 0
            optimization_potential = "critical"
        
        # Calculate dependency depth (simplified)
        dependencies_value = stack_config.get('dependencies', 1)
        dependency_depth = dependencies_value if isinstance(dependencies_value, int) else len(dependencies_value)
        
        return StackMetrics(
            stack_name=stack_name,
            total_load_time_ms=total_load_time,
            peak_memory_mb=peak_memory,
            component_count=loaded_components,
            dependency_depth=dependency_depth,
            loading_efficiency=loading_efficiency,
            optimization_potential=optimization_potential
        )

    def run_comprehensive_benchmark(self) -> List[StackMetrics]:
        """Execute comprehensive component stack benchmarking"""
        print("🔧 Component Stack Performance Benchmarking")
        print("=" * 50)
        
        stack_results = []
        
        for stack_name, stack_config in self.component_stacks.items():
            stack_metrics = self.benchmark_component_stack(stack_name, stack_config)
            stack_results.append(stack_metrics)
            
            # Print summary for this stack
            efficiency_status = "✅" if stack_metrics.loading_efficiency >= 80 else "⚠️"
            performance_status = "🏆" if stack_metrics.optimization_potential in ["excellent", "good"] else "🔧"
            
            print(f"  {efficiency_status} {performance_status} {stack_name}: {stack_metrics.total_load_time_ms:.1f}ms "
                  f"({stack_metrics.component_count}/{len(stack_config['components'])} components, "
                  f"{stack_metrics.loading_efficiency:.0f}% efficiency)")
            print()
        
        return stack_results

    def generate_optimization_report(self, stack_results: List[StackMetrics]) -> str:
        """Generate detailed component stack optimization report"""
        report = []
        report.append("# Component Stack Performance Analysis Report")
        report.append(f"**Generated**: {datetime.now().isoformat()}")
        report.append(f"**Stacks Analyzed**: {len(stack_results)}")
        report.append("")
        
        # Executive summary
        total_load_time = sum(stack.total_load_time_ms for stack in stack_results)
        avg_efficiency = sum(stack.loading_efficiency for stack in stack_results) / len(stack_results)
        high_optimization = [stack for stack in stack_results if stack.optimization_potential == "high"]
        
        report.append("## Executive Summary")
        report.append("")
        report.append(f"- **Total Stack Load Time**: {total_load_time:.1f}ms")
        report.append(f"- **Average Loading Efficiency**: {avg_efficiency:.1f}%")
        report.append(f"- **Stacks Needing Optimization**: {len(high_optimization)}")
        report.append("")
        
        # Performance rankings
        sorted_stacks = sorted(stack_results, key=lambda s: s.total_load_time_ms)
        
        report.append("## Performance Rankings")
        report.append("")
        report.append("### Fastest Loading Stacks")
        for i, stack in enumerate(sorted_stacks[:3], 1):
            report.append(f"{i}. **{stack.stack_name}**: {stack.total_load_time_ms:.1f}ms ({stack.loading_efficiency:.0f}% efficiency)")
        report.append("")
        
        if len(sorted_stacks) > 3:
            report.append("### Slowest Loading Stacks")
            for i, stack in enumerate(sorted_stacks[-3:], 1):
                report.append(f"{i}. **{stack.stack_name}**: {stack.total_load_time_ms:.1f}ms ({stack.loading_efficiency:.0f}% efficiency)")
            report.append("")
        
        # Detailed stack analysis
        report.append("## Detailed Stack Analysis")
        report.append("")
        
        for stack in stack_results:
            report.append(f"### {stack.stack_name.title()} Stack")
            report.append("")
            report.append(f"- **Load Time**: {stack.total_load_time_ms:.1f}ms")
            report.append(f"- **Peak Memory**: {stack.peak_memory_mb:.1f}MB")
            report.append(f"- **Component Count**: {stack.component_count}")
            report.append(f"- **Loading Efficiency**: {stack.loading_efficiency:.1f}%")
            report.append(f"- **Optimization Potential**: {stack.optimization_potential}")
            report.append("")
            
            # Recommendations
            if stack.optimization_potential == "high":
                report.append("**Recommendations:**")
                report.append("- Consider component lazy loading")
                report.append("- Analyze component dependencies for circular references")
                report.append("- Implement component caching")
                report.append("")
            elif stack.optimization_potential == "moderate":
                report.append("**Recommendations:**")
                report.append("- Review component loading order")
                report.append("- Consider component bundling")
                report.append("")
        
        # Memory optimization
        high_memory_stacks = [stack for stack in stack_results if stack.peak_memory_mb > 5]
        if high_memory_stacks:
            report.append("## Memory Optimization Opportunities")
            report.append("")
            for stack in high_memory_stacks:
                report.append(f"- **{stack.stack_name}**: {stack.peak_memory_mb:.1f}MB peak usage")
            report.append("")
        
        return '\n'.join(report)

def main():
    """Main component stack benchmarking execution"""
    if len(sys.argv) != 2:
        print("Usage: python component-stack-benchmark.py <components_dir>")
        sys.exit(1)
    
    components_dir = sys.argv[1]
    
    benchmarker = ComponentStackBenchmarker(components_dir)
    
    # Run comprehensive benchmarking
    stack_results = benchmarker.run_comprehensive_benchmark()
    
    print("=" * 50)
    print(f"✅ Component Stack Benchmarking Complete")
    print(f"📊 {len(stack_results)} stacks analyzed")
    
    # Generate optimization report
    report = benchmarker.generate_optimization_report(stack_results)
    
    # Save results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results_file = f"component_stack_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump([asdict(stack) for stack in stack_results], f, indent=2)
    
    print(f"💾 Results saved to: {results_file}")
    print("\n" + report)

if __name__ == "__main__":
    main()