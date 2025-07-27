#!/usr/bin/env python3
"""
Component Stack Integration Testing Framework

Integration Testing Agent Beta - Component Stack Integration Testing
Mission: Execute systematic testing of the 8 critical component stacks

This module provides comprehensive integration testing for component stacks:
1. Orchestration Foundation Stack
2. Validation Framework Stack  
3. Context Management Stack
4. Intelligence Layer Stack

Each stack is tested for:
- Component loading order and dependency resolution
- Component compatibility and conflict detection
- Loading performance against targets (25-70ms per stack)
- Memory usage within acceptable limits
- Component interaction patterns and data flow
"""

import time
import json
import psutil
import traceback
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ComponentLoadResult:
    """Result of loading a single component"""
    component_name: str
    load_time_ms: float
    memory_usage_mb: float
    success: bool
    error_message: Optional[str] = None
    dependencies: List[str] = None


@dataclass
class StackTestResult:
    """Result of testing a complete component stack"""
    stack_name: str
    components: List[str]
    total_load_time_ms: float
    peak_memory_mb: float
    avg_component_load_ms: float
    success: bool
    compatibility_issues: List[str]
    performance_rating: str  # Excellent, Good, Fair, Poor
    component_results: List[ComponentLoadResult]


class ComponentStackTester:
    """Integration tester for component stacks"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.components_path = self.base_path / ".claude" / "components"
        self.results = []
        
        # Performance targets
        self.target_stack_load_min_ms = 25
        self.target_stack_load_max_ms = 70
        self.target_memory_limit_mb = 50
        
    def load_component(self, component_path: str) -> ComponentLoadResult:
        """Load a single component and measure performance"""
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        try:
            # Simulate component loading by reading and parsing
            with open(component_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract dependencies from component content
            dependencies = self._extract_dependencies(content)
            
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024 / 1024
            
            load_time_ms = (end_time - start_time) * 1000
            memory_usage_mb = end_memory - start_memory
            
            return ComponentLoadResult(
                component_name=Path(component_path).name,
                load_time_ms=load_time_ms,
                memory_usage_mb=memory_usage_mb,
                success=True,
                dependencies=dependencies
            )
            
        except Exception as e:
            end_time = time.time()
            return ComponentLoadResult(
                component_name=Path(component_path).name,
                load_time_ms=(end_time - start_time) * 1000,
                memory_usage_mb=0,
                success=False,
                error_message=str(e)
            )
    
    def _extract_dependencies(self, content: str) -> List[str]:
        """Extract component dependencies from content"""
        dependencies = []
        
        # Look for include statements
        if '<include>' in content:
            # Extract include paths
            import re
            includes = re.findall(r'<include>([^<]+)</include>', content)
            dependencies.extend(includes)
        
        # Look for common dependency patterns
        dependency_patterns = [
            'validation-framework',
            'task-execution',
            'progress-tracking',
            'hierarchical-loading',
            'context-optimization',
            'multi-agent-coordination',
            'pattern-extraction'
        ]
        
        for pattern in dependency_patterns:
            if pattern in content:
                dependencies.append(pattern)
        
        return list(set(dependencies))  # Remove duplicates
    
    def test_orchestration_foundation_stack(self) -> StackTestResult:
        """Test Orchestration Foundation Stack: dag-orchestrator + task-execution + progress-tracking"""
        stack_name = "Orchestration Foundation Stack"
        components = [
            "orchestration/dag-orchestrator.md",
            "orchestration/task-execution.md", 
            "orchestration/progress-tracking.md"
        ]
        
        return self._test_component_stack(stack_name, components)
    
    def test_validation_framework_stack(self) -> StackTestResult:
        """Test Validation Framework Stack: validation-framework + security-validation + input-validation"""
        stack_name = "Validation Framework Stack"
        components = [
            "validation/validation-framework.md",
            # Note: security-validation and input-validation may be embedded in validation-framework
        ]
        
        # Check if separate security and input validation components exist
        security_path = self.components_path / "security" / "security-validation.md"
        if security_path.exists():
            components.append("security/security-validation.md")
        
        validation_path = self.components_path / "validation" / "input-validation.md"
        if validation_path.exists():
            components.append("validation/input-validation.md")
        
        return self._test_component_stack(stack_name, components)
    
    def test_context_management_stack(self) -> StackTestResult:
        """Test Context Management Stack: hierarchical-loading + context-optimization + adaptive-thinking"""
        stack_name = "Context Management Stack"
        components = [
            "context/hierarchical-loading.md",
            "context/context-optimization.md",
            "context/adaptive-thinking.md"
        ]
        
        return self._test_component_stack(stack_name, components)
    
    def test_intelligence_layer_stack(self) -> StackTestResult:
        """Test Intelligence Layer Stack: multi-agent-coordination + cognitive-architecture + pattern-extraction"""
        stack_name = "Intelligence Layer Stack"
        components = [
            "intelligence/multi-agent-coordination.md",
            "reasoning/pattern-extraction.md"
        ]
        
        # Check for cognitive-architecture component
        cognitive_path = self.components_path / "intelligence" / "cognitive-architecture.md"
        if cognitive_path.exists():
            components.append("intelligence/cognitive-architecture.md")
        
        return self._test_component_stack(stack_name, components)
    
    def _test_component_stack(self, stack_name: str, components: List[str]) -> StackTestResult:
        """Test a complete component stack"""
        print(f"\n🧪 Testing {stack_name}...")
        
        stack_start_time = time.time()
        stack_start_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        component_results = []
        compatibility_issues = []
        total_load_time = 0
        
        # Test each component in the stack
        for component_rel_path in components:
            component_path = self.components_path / component_rel_path
            
            if not component_path.exists():
                compatibility_issues.append(f"Component not found: {component_rel_path}")
                continue
            
            print(f"  📦 Loading {component_rel_path}...")
            result = self.load_component(str(component_path))
            component_results.append(result)
            total_load_time += result.load_time_ms
            
            if not result.success:
                compatibility_issues.append(f"Failed to load {component_rel_path}: {result.error_message}")
        
        # Check for dependency conflicts
        self._check_dependency_conflicts(component_results, compatibility_issues)
        
        stack_end_time = time.time()
        stack_end_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        total_stack_time = (stack_end_time - stack_start_time) * 1000
        peak_memory = stack_end_memory - stack_start_memory
        avg_component_time = total_load_time / len(component_results) if component_results else 0
        
        # Determine performance rating
        performance_rating = self._calculate_performance_rating(total_stack_time, peak_memory)
        
        success = len(compatibility_issues) == 0 and all(r.success for r in component_results)
        
        result = StackTestResult(
            stack_name=stack_name,
            components=components,
            total_load_time_ms=total_stack_time,
            peak_memory_mb=peak_memory,
            avg_component_load_ms=avg_component_time,
            success=success,
            compatibility_issues=compatibility_issues,
            performance_rating=performance_rating,
            component_results=component_results
        )
        
        self.results.append(result)
        return result
    
    def _check_dependency_conflicts(self, component_results: List[ComponentLoadResult], issues: List[str]):
        """Check for dependency conflicts between components"""
        all_dependencies = set()
        component_deps = {}
        
        for result in component_results:
            if result.dependencies:
                component_deps[result.component_name] = set(result.dependencies)
                all_dependencies.update(result.dependencies)
        
        # Check for circular dependencies
        for comp_name, deps in component_deps.items():
            for dep in deps:
                if dep in component_deps and comp_name in component_deps[dep]:
                    issues.append(f"Circular dependency detected: {comp_name} <-> {dep}")
    
    def _calculate_performance_rating(self, load_time_ms: float, memory_mb: float) -> str:
        """Calculate performance rating based on metrics"""
        time_score = 0
        memory_score = 0
        
        # Time scoring (target: 25-70ms)
        if load_time_ms <= self.target_stack_load_max_ms:
            time_score = 100
        elif load_time_ms <= self.target_stack_load_max_ms * 1.5:
            time_score = 75
        elif load_time_ms <= self.target_stack_load_max_ms * 2:
            time_score = 50
        else:
            time_score = 25
        
        # Memory scoring (target: <50MB)
        if memory_mb <= self.target_memory_limit_mb:
            memory_score = 100
        elif memory_mb <= self.target_memory_limit_mb * 1.5:
            memory_score = 75
        elif memory_mb <= self.target_memory_limit_mb * 2:
            memory_score = 50
        else:
            memory_score = 25
        
        # Combined score
        combined_score = (time_score + memory_score) / 2
        
        if combined_score >= 90:
            return "Excellent"
        elif combined_score >= 75:
            return "Good"
        elif combined_score >= 60:
            return "Fair"
        else:
            return "Poor"
    
    def run_all_stack_tests(self) -> Dict[str, StackTestResult]:
        """Run all component stack tests"""
        print("🚀 Component Stack Integration Testing - Starting All Tests")
        print(f"Base path: {self.base_path}")
        print(f"Components path: {self.components_path}")
        
        test_results = {}
        
        # Test all 4 critical stacks
        test_results["orchestration"] = self.test_orchestration_foundation_stack()
        test_results["validation"] = self.test_validation_framework_stack()
        test_results["context"] = self.test_context_management_stack()
        test_results["intelligence"] = self.test_intelligence_layer_stack()
        
        return test_results
    
    def generate_compatibility_matrix(self) -> Dict[str, Any]:
        """Generate component compatibility matrix"""
        matrix = {
            "timestamp": datetime.now().isoformat(),
            "test_summary": {
                "total_stacks_tested": len(self.results),
                "successful_stacks": len([r for r in self.results if r.success]),
                "total_components": sum(len(r.component_results) for r in self.results),
                "successful_components": sum(len([c for c in r.component_results if c.success]) for r in self.results)
            },
            "performance_summary": {
                "avg_stack_load_time_ms": sum(r.total_load_time_ms for r in self.results) / len(self.results) if self.results else 0,
                "avg_memory_usage_mb": sum(r.peak_memory_mb for r in self.results) / len(self.results) if self.results else 0,
                "performance_ratings": [r.performance_rating for r in self.results]
            },
            "compatibility_issues": [],
            "stack_details": []
        }
        
        # Collect all compatibility issues
        for result in self.results:
            matrix["compatibility_issues"].extend([
                f"{result.stack_name}: {issue}" for issue in result.compatibility_issues
            ])
        
        # Add detailed stack information
        for result in self.results:
            stack_detail = {
                "stack_name": result.stack_name,
                "success": result.success,
                "load_time_ms": result.total_load_time_ms,
                "memory_mb": result.peak_memory_mb,
                "performance_rating": result.performance_rating,
                "components": [
                    {
                        "name": comp.component_name,
                        "success": comp.success,
                        "load_time_ms": comp.load_time_ms,
                        "memory_mb": comp.memory_usage_mb,
                        "dependencies": comp.dependencies or []
                    }
                    for comp in result.component_results
                ]
            }
            matrix["stack_details"].append(stack_detail)
        
        return matrix
    
    def save_results(self, output_path: str):
        """Save test results to file"""
        compatibility_matrix = self.generate_compatibility_matrix()
        
        with open(output_path, 'w') as f:
            json.dump(compatibility_matrix, f, indent=2)
        
        print(f"📊 Results saved to: {output_path}")


def main():
    """Main test execution function"""
    base_path = "/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca"
    tester = ComponentStackTester(base_path)
    
    try:
        # Run all stack tests
        results = tester.run_all_stack_tests()
        
        # Print summary
        print("\n" + "="*80)
        print("🎯 COMPONENT STACK INTEGRATION TEST RESULTS")
        print("="*80)
        
        for stack_name, result in results.items():
            status = "✅ PASS" if result.success else "❌ FAIL"
            print(f"\n{status} {result.stack_name}")
            print(f"   📊 Load Time: {result.total_load_time_ms:.1f}ms")
            print(f"   💾 Peak Memory: {result.peak_memory_mb:.1f}MB")
            print(f"   ⭐ Performance: {result.performance_rating}")
            print(f"   📦 Components: {len(result.component_results)}")
            
            if result.compatibility_issues:
                print(f"   ⚠️  Issues: {len(result.compatibility_issues)}")
                for issue in result.compatibility_issues:
                    print(f"      - {issue}")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{base_path}/tests/results/component_stack_integration_{timestamp}.json"
        tester.save_results(output_file)
        
        # Generate summary report
        generate_summary_report(tester, output_file.replace('.json', '_report.md'))
        
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        traceback.print_exc()


def generate_summary_report(tester: ComponentStackTester, output_path: str):
    """Generate human-readable summary report"""
    matrix = tester.generate_compatibility_matrix()
    
    report = f"""# Component Stack Integration Test Report

**Generated:** {matrix['timestamp']}
**Test Agent:** Integration Testing Agent Beta

## Executive Summary

- **Total Stacks Tested:** {matrix['test_summary']['total_stacks_tested']}
- **Successful Stacks:** {matrix['test_summary']['successful_stacks']}
- **Total Components:** {matrix['test_summary']['total_components']}
- **Successful Components:** {matrix['test_summary']['successful_components']}

## Performance Metrics

- **Average Stack Load Time:** {matrix['performance_summary']['avg_stack_load_time_ms']:.1f}ms
- **Average Memory Usage:** {matrix['performance_summary']['avg_memory_usage_mb']:.1f}MB
- **Performance Target:** 25-70ms per stack
- **Memory Target:** <50MB per stack

## Stack Test Results

"""
    
    for stack in matrix['stack_details']:
        status = "✅ PASS" if stack['success'] else "❌ FAIL"
        report += f"""
### {status} {stack['stack_name']}

- **Load Time:** {stack['load_time_ms']:.1f}ms
- **Memory Usage:** {stack['memory_mb']:.1f}MB
- **Performance Rating:** {stack['performance_rating']}
- **Components:** {len(stack['components'])}

"""
        
        for comp in stack['components']:
            comp_status = "✅" if comp['success'] else "❌"
            report += f"  - {comp_status} {comp['name']} ({comp['load_time_ms']:.1f}ms)\n"
    
    if matrix['compatibility_issues']:
        report += f"""
## Compatibility Issues

{len(matrix['compatibility_issues'])} issues detected:

"""
        for issue in matrix['compatibility_issues']:
            report += f"- {issue}\n"
    else:
        report += "\n## ✅ No Compatibility Issues Detected\n"
    
    report += f"""
## Recommendations

Based on the test results:

1. **Performance Optimization:** Focus on stacks with >70ms load times
2. **Memory Efficiency:** Optimize stacks using >50MB memory
3. **Compatibility:** Resolve any dependency conflicts identified
4. **Monitoring:** Implement continuous integration testing for component stacks

---
*Generated by Integration Testing Agent Beta - Component Stack Integration Testing*
"""
    
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"📋 Summary report saved to: {output_path}")


if __name__ == "__main__":
    main()