#!/usr/bin/env python3
"""
Advanced Component Stack Integration Testing

Integration Testing Agent Beta - Advanced Integration Analysis
Mission: Execute deep integration testing of component stacks with cross-stack compatibility matrix

This module provides advanced integration testing including:
- Cross-stack dependency analysis
- Component interaction pattern validation
- Data flow consistency testing
- Performance optimization analysis
- Memory efficiency optimization
- Integration pattern documentation
"""

import time
import json
import re
import psutil
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional, Set
from dataclasses import dataclass, asdict
from datetime import datetime
import itertools


@dataclass
class ComponentDependency:
    """Represents a dependency relationship between components"""
    source_component: str
    target_component: str
    dependency_type: str  # include, reference, data_flow, pattern_usage
    strength: float  # 0.0 - 1.0 indicating dependency strength
    bidirectional: bool = False


@dataclass
class InteractionPattern:
    """Represents an interaction pattern between components"""
    pattern_name: str
    components: List[str]
    data_flow: Dict[str, List[str]]  # component -> list of data outputs
    execution_order: List[str]
    performance_impact: float
    compatibility_score: float


@dataclass
class CrossStackResult:
    """Result of cross-stack integration testing"""
    stack_combination: Tuple[str, str]
    compatibility_score: float
    integration_patterns: List[InteractionPattern]
    dependency_conflicts: List[str]
    performance_impact: float
    recommended_load_order: List[str]
    optimization_opportunities: List[str]


class AdvancedIntegrationTester:
    """Advanced integration tester for component stacks"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.components_path = self.base_path / ".claude" / "components"
        self.stacks = {
            "orchestration": ["orchestration/dag-orchestrator.md", "orchestration/task-execution.md", "orchestration/progress-tracking.md"],
            "validation": ["validation/validation-framework.md"],
            "context": ["context/hierarchical-loading.md", "context/context-optimization.md", "context/adaptive-thinking.md"],
            "intelligence": ["intelligence/multi-agent-coordination.md", "reasoning/pattern-extraction.md", "intelligence/cognitive-architecture.md"]
        }
        self.component_cache = {}
        self.dependency_graph = {}
        self.interaction_patterns = []
        
    def load_and_analyze_component(self, component_path: str) -> Dict[str, Any]:
        """Load component and extract detailed analysis"""
        if component_path in self.component_cache:
            return self.component_cache[component_path]
        
        full_path = self.components_path / component_path
        if not full_path.exists():
            return None
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        analysis = {
            'path': component_path,
            'name': Path(component_path).stem,
            'content': content,
            'dependencies': self._extract_dependencies(content),
            'data_inputs': self._extract_data_inputs(content),
            'data_outputs': self._extract_data_outputs(content),
            'patterns_used': self._extract_patterns(content),
            'performance_hints': self._extract_performance_hints(content),
            'memory_usage': self._estimate_memory_usage(content),
            'complexity_score': self._calculate_complexity(content)
        }
        
        self.component_cache[component_path] = analysis
        return analysis
    
    def _extract_dependencies(self, content: str) -> List[ComponentDependency]:
        """Extract detailed dependency information"""
        dependencies = []
        
        # Include statements
        include_pattern = r'<include>([^<]+)</include>'
        includes = re.findall(include_pattern, content)
        for include in includes:
            dependencies.append(ComponentDependency(
                source_component="current",
                target_component=include,
                dependency_type="include",
                strength=1.0
            ))
        
        # Component references
        component_refs = [
            'validation-framework', 'task-execution', 'progress-tracking',
            'hierarchical-loading', 'context-optimization', 'adaptive-thinking',
            'multi-agent-coordination', 'pattern-extraction', 'cognitive-architecture',
            'dag-orchestrator'
        ]
        
        for ref in component_refs:
            if ref in content:
                # Count occurrences to determine strength
                count = content.count(ref)
                strength = min(count / 10.0, 1.0)  # Normalize to 0-1
                dependencies.append(ComponentDependency(
                    source_component="current",
                    target_component=ref,
                    dependency_type="reference",
                    strength=strength
                ))
        
        return dependencies
    
    def _extract_data_inputs(self, content: str) -> List[str]:
        """Extract data input requirements"""
        inputs = []
        
        # Look for input patterns
        input_patterns = [
            r'input[s]?[\"\\s]*:[\"\\s]*([^\"\\n]+)',
            r'<argument[^>]*name=[\"\\s]*([^\"\\s>]+)',
            r'requires?[\"\\s]*:[\"\\s]*([^\"\\n]+)',
            r'context[\"\\s]*:[\"\\s]*([^\"\\n]+)'
        ]
        
        for pattern in input_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            inputs.extend(matches)
        
        return list(set(inputs))  # Remove duplicates
    
    def _extract_data_outputs(self, content: str) -> List[str]:
        """Extract data output specifications"""
        outputs = []
        
        # Look for output patterns
        output_patterns = [
            r'output[s]?[\"\\s]*:[\"\\s]*([^\"\\n]+)',
            r'returns?[\"\\s]*:[\"\\s]*([^\"\\n]+)',
            r'generates?[\"\\s]*:[\"\\s]*([^\"\\n]+)',
            r'<o>([^<]+)</o>'
        ]
        
        for pattern in output_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            outputs.extend(matches)
        
        return list(set(outputs))
    
    def _extract_patterns(self, content: str) -> List[str]:
        """Extract patterns and frameworks used"""
        patterns = []
        
        # Common patterns
        pattern_keywords = [
            'pattern', 'framework', 'architecture', 'strategy', 'algorithm',
            'protocol', 'methodology', 'approach', 'design', 'paradigm'
        ]
        
        for keyword in pattern_keywords:
            pattern = f'{keyword}[s]?[\"\\s]*:?[\"\\s]*([A-Za-z][A-Za-z0-9_\\-\\s]*)'
            matches = re.findall(pattern, content, re.IGNORECASE)
            patterns.extend([m.strip() for m in matches if len(m.strip()) > 3])
        
        return list(set(patterns))
    
    def _extract_performance_hints(self, content: str) -> Dict[str, Any]:
        """Extract performance-related information"""
        hints = {
            'cache_usage': 'cache' in content.lower(),
            'parallel_processing': any(word in content.lower() for word in ['parallel', 'concurrent', 'async']),
            'optimization': 'optimization' in content.lower(),
            'lazy_loading': 'lazy' in content.lower(),
            'compression': 'compression' in content.lower(),
            'token_efficiency': 'token' in content.lower()
        }
        
        # Extract timing references
        timing_pattern = r'(\\d+(?:\\.\\d+)?)\\s*(ms|milliseconds?|s|seconds?)'
        timings = re.findall(timing_pattern, content.lower())
        if timings:
            hints['timing_references'] = timings
        
        return hints
    
    def _estimate_memory_usage(self, content: str) -> float:
        """Estimate memory usage based on content complexity"""
        # Base memory for content size
        base_memory = len(content) / 1024 / 1024  # MB
        
        # Complexity multipliers
        multipliers = {
            'xml': 1.2 if '<' in content and '>' in content else 1.0,
            'json': 1.1 if '{' in content and '}' in content else 1.0,
            'patterns': 1.0 + (content.count('pattern') * 0.1),
            'complexity': 1.0 + (content.count('complex') * 0.05)
        }
        
        total_multiplier = 1.0
        for mult in multipliers.values():
            total_multiplier *= mult
        
        return base_memory * total_multiplier
    
    def _calculate_complexity(self, content: str) -> float:
        """Calculate component complexity score (0-10)"""
        factors = {
            'length': min(len(content) / 10000, 3.0),  # 0-3 based on length
            'xml_structure': content.count('<') / 100,  # XML complexity
            'patterns': len(re.findall(r'<[^>]+>', content)) / 50,  # Tag complexity
            'logic': content.count('if') + content.count('for') + content.count('while'),  # Logical complexity
            'references': len(re.findall(r'[a-zA-Z-]+\\.md', content)) / 10  # Reference complexity
        }
        
        complexity = sum(min(value, 2.0) for value in factors.values())
        return min(complexity, 10.0)
    
    def build_dependency_graph(self) -> Dict[str, Set[str]]:
        """Build comprehensive dependency graph across all components"""
        print("🔗 Building dependency graph...")
        
        graph = {}
        
        # Load all components and build relationships
        for stack_name, components in self.stacks.items():
            for component_path in components:
                analysis = self.load_and_analyze_component(component_path)
                if not analysis:
                    continue
                
                comp_name = analysis['name']
                graph[comp_name] = set()
                
                # Add dependencies
                for dep in analysis['dependencies']:
                    if dep.dependency_type in ['include', 'reference']:
                        # Normalize dependency name
                        dep_name = dep.target_component.replace('.md', '').split('/')[-1]
                        graph[comp_name].add(dep_name)
        
        self.dependency_graph = graph
        return graph
    
    def analyze_cross_stack_compatibility(self) -> List[CrossStackResult]:
        """Analyze compatibility between different stacks"""
        print("🔄 Analyzing cross-stack compatibility...")
        
        results = []
        stack_names = list(self.stacks.keys())
        
        # Test all pairs of stacks
        for stack1, stack2 in itertools.combinations(stack_names, 2):
            result = self._test_stack_combination(stack1, stack2)
            results.append(result)
        
        return results
    
    def _test_stack_combination(self, stack1: str, stack2: str) -> CrossStackResult:
        """Test compatibility between two specific stacks"""
        print(f"  🧪 Testing {stack1} ↔ {stack2}")
        
        # Load components from both stacks
        stack1_components = [self.load_and_analyze_component(comp) for comp in self.stacks[stack1]]
        stack2_components = [self.load_and_analyze_component(comp) for comp in self.stacks[stack2]]
        
        # Filter out None results
        stack1_components = [c for c in stack1_components if c]
        stack2_components = [c for c in stack2_components if c]
        
        # Analyze compatibility
        compatibility_score = self._calculate_compatibility_score(stack1_components, stack2_components)
        interaction_patterns = self._identify_interaction_patterns(stack1_components, stack2_components)
        dependency_conflicts = self._find_dependency_conflicts(stack1_components, stack2_components)
        performance_impact = self._calculate_performance_impact(stack1_components, stack2_components)
        load_order = self._determine_optimal_load_order(stack1_components, stack2_components)
        optimizations = self._identify_optimization_opportunities(stack1_components, stack2_components)
        
        return CrossStackResult(
            stack_combination=(stack1, stack2),
            compatibility_score=compatibility_score,
            integration_patterns=interaction_patterns,
            dependency_conflicts=dependency_conflicts,
            performance_impact=performance_impact,
            recommended_load_order=load_order,
            optimization_opportunities=optimizations
        )
    
    def _calculate_compatibility_score(self, stack1_components: List[Dict], stack2_components: List[Dict]) -> float:
        """Calculate compatibility score between two stacks"""
        score = 1.0
        
        # Check for conflicting patterns
        stack1_patterns = set()
        stack2_patterns = set()
        
        for comp in stack1_components:
            stack1_patterns.update(comp['patterns_used'])
        
        for comp in stack2_components:
            stack2_patterns.update(comp['patterns_used'])
        
        # Overlapping patterns are good for compatibility
        overlap = len(stack1_patterns & stack2_patterns)
        total_patterns = len(stack1_patterns | stack2_patterns)
        
        if total_patterns > 0:
            pattern_compatibility = overlap / total_patterns
            score *= (0.5 + pattern_compatibility * 0.5)
        
        # Check memory compatibility
        total_memory = sum(comp['memory_usage'] for comp in stack1_components + stack2_components)
        if total_memory > 100:  # MB threshold
            score *= 0.8
        
        # Check complexity compatibility
        avg_complexity = sum(comp['complexity_score'] for comp in stack1_components + stack2_components) / len(stack1_components + stack2_components)
        if avg_complexity > 7:
            score *= 0.9
        
        return score
    
    def _identify_interaction_patterns(self, stack1_components: List[Dict], stack2_components: List[Dict]) -> List[InteractionPattern]:
        """Identify interaction patterns between stacks"""
        patterns = []
        
        # Look for data flow patterns
        for comp1 in stack1_components:
            for comp2 in stack2_components:
                # Check if output of comp1 matches input of comp2
                output_input_matches = set(comp1['data_outputs']) & set(comp2['data_inputs'])
                
                if output_input_matches:
                    pattern = InteractionPattern(
                        pattern_name=f"{comp1['name']}_to_{comp2['name']}_data_flow",
                        components=[comp1['name'], comp2['name']],
                        data_flow={comp1['name']: list(output_input_matches)},
                        execution_order=[comp1['name'], comp2['name']],
                        performance_impact=comp1['complexity_score'] + comp2['complexity_score'],
                        compatibility_score=len(output_input_matches) / max(len(comp1['data_outputs']), 1)
                    )
                    patterns.append(pattern)
        
        return patterns
    
    def _find_dependency_conflicts(self, stack1_components: List[Dict], stack2_components: List[Dict]) -> List[str]:
        """Find dependency conflicts between stacks"""
        conflicts = []
        
        # Check for circular dependencies
        all_components = stack1_components + stack2_components
        comp_names = {comp['name'] for comp in all_components}
        
        for comp in all_components:
            for dep in comp['dependencies']:
                dep_name = dep.target_component.replace('.md', '').split('/')[-1]
                if dep_name in comp_names:
                    # Check for circular reference
                    for other_comp in all_components:
                        if other_comp['name'] == dep_name:
                            for other_dep in other_comp['dependencies']:
                                other_dep_name = other_dep.target_component.replace('.md', '').split('/')[-1]
                                if other_dep_name == comp['name']:
                                    conflicts.append(f"Circular dependency: {comp['name']} ↔ {dep_name}")
        
        return conflicts
    
    def _calculate_performance_impact(self, stack1_components: List[Dict], stack2_components: List[Dict]) -> float:
        """Calculate performance impact of combining stacks"""
        # Base impact from complexity
        total_complexity = sum(comp['complexity_score'] for comp in stack1_components + stack2_components)
        
        # Memory impact
        total_memory = sum(comp['memory_usage'] for comp in stack1_components + stack2_components)
        
        # Interaction overhead
        interaction_count = len(stack1_components) * len(stack2_components)
        
        # Normalize to 0-1 scale where 0 is no impact, 1 is high impact
        performance_impact = min((total_complexity / 50 + total_memory / 100 + interaction_count / 100) / 3, 1.0)
        
        return performance_impact
    
    def _determine_optimal_load_order(self, stack1_components: List[Dict], stack2_components: List[Dict]) -> List[str]:
        """Determine optimal loading order for components"""
        all_components = stack1_components + stack2_components
        
        # Sort by dependency count (fewer dependencies first) and complexity
        def sort_key(comp):
            dep_count = len(comp['dependencies'])
            complexity = comp['complexity_score']
            return (dep_count, complexity)
        
        sorted_components = sorted(all_components, key=sort_key)
        return [comp['name'] for comp in sorted_components]
    
    def _identify_optimization_opportunities(self, stack1_components: List[Dict], stack2_components: List[Dict]) -> List[str]:
        """Identify optimization opportunities"""
        opportunities = []
        
        all_components = stack1_components + stack2_components
        
        # Check for caching opportunities
        cache_users = [comp for comp in all_components if comp['performance_hints']['cache_usage']]
        if len(cache_users) > 1:
            opportunities.append("Implement shared caching layer across components")
        
        # Check for parallel processing opportunities
        parallel_capable = [comp for comp in all_components if comp['performance_hints']['parallel_processing']]
        if len(parallel_capable) > 1:
            opportunities.append("Implement parallel component loading")
        
        # Check for high memory usage
        high_memory = [comp for comp in all_components if comp['memory_usage'] > 10]
        if high_memory:
            opportunities.append("Optimize memory usage for large components")
        
        # Check for compression opportunities
        large_components = [comp for comp in all_components if comp['complexity_score'] > 7]
        if large_components:
            opportunities.append("Implement component compression for complex components")
        
        return opportunities
    
    def generate_comprehensive_compatibility_matrix(self) -> Dict[str, Any]:
        """Generate comprehensive compatibility matrix with all analysis results"""
        print("📊 Generating comprehensive compatibility matrix...")
        
        # Build dependency graph
        dependency_graph = self.build_dependency_graph()
        
        # Analyze cross-stack compatibility
        cross_stack_results = self.analyze_cross_stack_compatibility()
        
        # Compile comprehensive results
        matrix = {
            "timestamp": datetime.now().isoformat(),
            "test_metadata": {
                "testing_agent": "Integration Testing Agent Beta",
                "test_type": "Advanced Component Stack Integration",
                "base_path": str(self.base_path),
                "components_analyzed": len(self.component_cache)
            },
            "dependency_analysis": {
                "total_components": len(dependency_graph),
                "dependency_graph": {comp: list(deps) for comp, deps in dependency_graph.items()},
                "circular_dependencies": self._find_circular_dependencies(dependency_graph),
                "isolated_components": [comp for comp, deps in dependency_graph.items() if not deps]
            },
            "cross_stack_compatibility": [
                {
                    "stack_combination": f"{result.stack_combination[0]} ↔ {result.stack_combination[1]}",
                    "compatibility_score": result.compatibility_score,
                    "performance_impact": result.performance_impact,
                    "dependency_conflicts": result.dependency_conflicts,
                    "optimization_opportunities": result.optimization_opportunities,
                    "recommended_load_order": result.recommended_load_order,
                    "interaction_patterns": [
                        {
                            "pattern_name": pattern.pattern_name,
                            "components": pattern.components,
                            "compatibility_score": pattern.compatibility_score,
                            "performance_impact": pattern.performance_impact
                        }
                        for pattern in result.integration_patterns
                    ]
                }
                for result in cross_stack_results
            ],
            "performance_analysis": {
                "component_complexity": {
                    comp_path: analysis['complexity_score']
                    for comp_path, analysis in self.component_cache.items()
                },
                "memory_usage": {
                    comp_path: analysis['memory_usage']
                    for comp_path, analysis in self.component_cache.items()
                },
                "optimization_summary": self._generate_optimization_summary(cross_stack_results)
            },
            "recommendations": self._generate_recommendations(cross_stack_results, dependency_graph)
        }
        
        return matrix
    
    def _find_circular_dependencies(self, graph: Dict[str, Set[str]]) -> List[List[str]]:
        """Find circular dependencies in the graph"""
        visited = set()
        rec_stack = set()
        cycles = []
        
        def dfs(node, path):
            if node in rec_stack:
                # Found cycle
                cycle_start = path.index(node)
                cycles.append(path[cycle_start:] + [node])
                return
            
            if node in visited:
                return
            
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in graph.get(node, set()):
                dfs(neighbor, path + [node])
            
            rec_stack.remove(node)
        
        for node in graph:
            if node not in visited:
                dfs(node, [])
        
        return cycles
    
    def _generate_optimization_summary(self, cross_stack_results: List[CrossStackResult]) -> Dict[str, Any]:
        """Generate optimization summary"""
        all_opportunities = []
        for result in cross_stack_results:
            all_opportunities.extend(result.optimization_opportunities)
        
        # Count frequency of optimization types
        optimization_counts = {}
        for opp in all_opportunities:
            optimization_counts[opp] = optimization_counts.get(opp, 0) + 1
        
        return {
            "total_opportunities": len(all_opportunities),
            "optimization_types": optimization_counts,
            "priority_optimizations": sorted(optimization_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        }
    
    def _generate_recommendations(self, cross_stack_results: List[CrossStackResult], dependency_graph: Dict[str, Set[str]]) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        # Check overall compatibility
        avg_compatibility = sum(result.compatibility_score for result in cross_stack_results) / len(cross_stack_results)
        if avg_compatibility < 0.7:
            recommendations.append("Consider refactoring components to improve cross-stack compatibility")
        
        # Check for high-impact combinations
        high_impact = [result for result in cross_stack_results if result.performance_impact > 0.6]
        if high_impact:
            recommendations.append("Optimize high-performance-impact stack combinations")
        
        # Check dependency complexity
        max_deps = max(len(deps) for deps in dependency_graph.values()) if dependency_graph else 0
        if max_deps > 5:
            recommendations.append("Reduce component dependencies to improve modularity")
        
        # Check for common optimization opportunities
        all_optimizations = []
        for result in cross_stack_results:
            all_optimizations.extend(result.optimization_opportunities)
        
        common_optimizations = {opt: all_optimizations.count(opt) for opt in set(all_optimizations)}
        most_common = max(common_optimizations.items(), key=lambda x: x[1]) if common_optimizations else None
        
        if most_common and most_common[1] > 1:
            recommendations.append(f"Priority optimization: {most_common[0]}")
        
        return recommendations
    
    def save_results(self, output_path: str):
        """Save comprehensive results"""
        matrix = self.generate_comprehensive_compatibility_matrix()
        
        with open(output_path, 'w') as f:
            json.dump(matrix, f, indent=2)
        
        print(f"📊 Advanced integration results saved to: {output_path}")
        
        # Generate human-readable report
        report_path = output_path.replace('.json', '_report.md')
        self._generate_detailed_report(matrix, report_path)
    
    def _generate_detailed_report(self, matrix: Dict[str, Any], output_path: str):
        """Generate detailed human-readable report"""
        report = f"""# Advanced Component Stack Integration Analysis Report

**Generated:** {matrix['timestamp']}
**Testing Agent:** {matrix['test_metadata']['testing_agent']}
**Analysis Type:** {matrix['test_metadata']['test_type']}

## Executive Summary

- **Components Analyzed:** {matrix['test_metadata']['components_analyzed']}
- **Total Dependencies:** {matrix['dependency_analysis']['total_components']}
- **Cross-Stack Combinations:** {len(matrix['cross_stack_compatibility'])}
- **Circular Dependencies:** {len(matrix['dependency_analysis']['circular_dependencies'])}

## Dependency Analysis

### Dependency Graph Overview
"""
        
        for comp, deps in matrix['dependency_analysis']['dependency_graph'].items():
            if deps:
                report += f"- **{comp}:** depends on {', '.join(deps)}\\n"
        
        if matrix['dependency_analysis']['circular_dependencies']:
            report += f"""
### ⚠️ Circular Dependencies Detected
{len(matrix['dependency_analysis']['circular_dependencies'])} circular dependencies found:
"""
            for i, cycle in enumerate(matrix['dependency_analysis']['circular_dependencies'], 1):
                report += f"{i}. {' → '.join(cycle)}\\n"
        else:
            report += "\\n### ✅ No Circular Dependencies Detected\\n"
        
        report += f"""
## Cross-Stack Compatibility Analysis

"""
        
        for combo in matrix['cross_stack_compatibility']:
            score = combo['compatibility_score']
            impact = combo['performance_impact']
            status = "✅ Excellent" if score > 0.8 else "⚠️ Good" if score > 0.6 else "❌ Needs Attention"
            
            report += f"""
### {status} {combo['stack_combination']}

- **Compatibility Score:** {score:.2f}/1.0
- **Performance Impact:** {impact:.2f}/1.0
- **Load Order:** {' → '.join(combo['recommended_load_order'])}

"""
            
            if combo['dependency_conflicts']:
                report += f"**⚠️ Dependency Conflicts:**\\n"
                for conflict in combo['dependency_conflicts']:
                    report += f"- {conflict}\\n"
            
            if combo['optimization_opportunities']:
                report += f"**🚀 Optimization Opportunities:**\\n"
                for opp in combo['optimization_opportunities']:
                    report += f"- {opp}\\n"
            
            if combo['interaction_patterns']:
                report += f"**🔗 Interaction Patterns:** {len(combo['interaction_patterns'])} detected\\n"
        
        report += f"""
## Performance Analysis

### Component Complexity Distribution
"""
        
        complexity_data = matrix['performance_analysis']['component_complexity']
        if complexity_data:
            avg_complexity = sum(complexity_data.values()) / len(complexity_data)
            high_complexity = [comp for comp, score in complexity_data.items() if score > 7]
            
            report += f"- **Average Complexity:** {avg_complexity:.1f}/10\\n"
            report += f"- **High Complexity Components:** {len(high_complexity)}\\n"
            
            if high_complexity:
                report += "  - " + "\\n  - ".join(high_complexity) + "\\n"
        
        report += f"""
### Memory Usage Analysis
"""
        
        memory_data = matrix['performance_analysis']['memory_usage']
        if memory_data:
            total_memory = sum(memory_data.values())
            high_memory = [comp for comp, usage in memory_data.items() if usage > 5]
            
            report += f"- **Total Estimated Memory:** {total_memory:.1f}MB\\n"
            report += f"- **High Memory Components:** {len(high_memory)}\\n"
        
        report += f"""
## Optimization Summary

"""
        
        opt_summary = matrix['performance_analysis']['optimization_summary']
        report += f"- **Total Opportunities:** {opt_summary['total_opportunities']}\\n"
        
        if opt_summary['priority_optimizations']:
            report += f"**Priority Optimizations:**\\n"
            for opt, count in opt_summary['priority_optimizations']:
                report += f"- {opt} (mentioned {count} times)\\n"
        
        report += f"""
## Recommendations

"""
        
        for i, rec in enumerate(matrix['recommendations'], 1):
            report += f"{i}. {rec}\\n"
        
        report += f"""
---
*Generated by Integration Testing Agent Beta - Advanced Component Stack Integration Testing*
*Analysis includes dependency mapping, cross-stack compatibility, performance impact assessment, and optimization recommendations*
"""
        
        with open(output_path, 'w') as f:
            f.write(report)
        
        print(f"📋 Detailed analysis report saved to: {output_path}")


def main():
    """Main execution function for advanced integration testing"""
    base_path = "/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca"
    tester = AdvancedIntegrationTester(base_path)
    
    try:
        print("🚀 Advanced Component Stack Integration Testing")
        print("="*80)
        
        # Generate comprehensive analysis
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{base_path}/tests/results/advanced_integration_analysis_{timestamp}.json"
        
        tester.save_results(output_file)
        
        print("\\n" + "="*80)
        print("✅ Advanced integration testing completed successfully")
        print("="*80)
        
    except Exception as e:
        print(f"❌ Advanced integration testing failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()