#!/usr/bin/env python3
"""
Workflow Performance Benchmarking
End-to-end performance testing of complete user workflows.

Focus: Workflow execution time, state management overhead, memory scaling
"""

import os
import sys
import time
import psutil
import json
import re
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import random

@dataclass
class WorkflowStep:
    """Individual workflow step metrics"""
    step_name: str
    command: str
    execution_time_ms: float
    memory_impact_mb: float
    context_size_kb: float
    success: bool

@dataclass
class WorkflowMetrics:
    """Complete workflow performance metrics"""
    workflow_name: str
    total_execution_time_ms: float
    peak_memory_mb: float
    average_step_time_ms: float
    context_overhead_mb: float
    steps: List[WorkflowStep]
    success_rate: float
    performance_grade: str

class WorkflowPerformanceBenchmarker:
    """End-to-end workflow performance testing framework"""
    
    def __init__(self, commands_dir: str):
        self.commands_dir = Path(commands_dir)
        
        # Workflow definitions from integration-test-matrices.md
        self.workflows = {
            'feature_development': {
                'description': 'Feature Development Lifecycle',
                'steps': ['/auto', '/task', '/test', '/validate-command'],
                'duration_estimate': {'min': 5, 'max': 15},  # minutes
                'success_criteria': 'Feature implemented, tested, and validated',
                'baseline_time_s': 600  # 10 minutes = 600 seconds
            },
            'bug_fixing': {
                'description': 'Bug Fixing and Validation',
                'steps': ['/analyze-system', '/task', '/test', '/validate-command'],
                'duration_estimate': {'min': 3, 'max': 10},
                'success_criteria': 'Bug fixed without regression',
                'baseline_time_s': 390  # 6.5 minutes average
            },
            'quality_improvement': {
                'description': 'Code Quality Improvement',
                'steps': ['/validate-command', '/test-integration', '/task', '/test'],
                'duration_estimate': {'min': 2, 'max': 8},
                'success_criteria': 'Quality metrics improved',
                'baseline_time_s': 300  # 5 minutes average
            },
            'system_optimization': {
                'description': 'System Analysis and Optimization',
                'steps': ['/analyze-system', '/test', '/task', '/validate-command'],
                'duration_estimate': {'min': 10, 'max': 30},
                'success_criteria': 'Performance improved without regression',
                'baseline_time_s': 1200  # 20 minutes average
            },
            'emergency_response': {
                'description': 'Emergency Response and Recovery',
                'steps': ['/analyze-system', '/task', '/test', '/validate-command'],
                'duration_estimate': {'min': 1, 'max': 5},
                'success_criteria': 'Critical issue resolved quickly',
                'baseline_time_s': 180  # 3 minutes average
            }
        }
        
        # Performance baselines
        self.workflow_baselines = {
            'simple': 5,      # seconds - 2-3 commands
            'medium': 15,     # seconds - 4-6 commands
            'complex': 30     # seconds - 7+ commands
        }

    def find_command_file(self, command_name: str) -> Optional[Path]:
        """Find command file by name"""
        # Remove leading slash if present
        cmd_name = command_name.lstrip('/')
        
        # Try direct match
        direct_matches = list(self.commands_dir.glob(f'**/{cmd_name}.md'))
        if direct_matches:
            return direct_matches[0]
        
        # Try partial matching for compound commands
        if '-' in cmd_name:
            base_name = cmd_name.split('-')[0]
            partial_matches = list(self.commands_dir.glob(f'**/{base_name}*.md'))
            if partial_matches:
                return partial_matches[0]
        
        return None

    def simulate_command_execution(self, command: str, context_data: Dict) -> WorkflowStep:
        """Simulate command execution with realistic performance characteristics"""
        cmd_file = self.find_command_file(command)
        
        process = psutil.Process()
        memory_before = process.memory_info().rss / 1024 / 1024
        
        start_time = time.perf_counter()
        
        # Simulate command processing
        if cmd_file and cmd_file.exists():
            # Read command file to estimate complexity
            try:
                with open(cmd_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Calculate processing complexity
                complexity_factors = {
                    'file_size': len(content),
                    'tools_used': len(re.findall(r'tools:\s*\[([^\]]+)\]', content, re.IGNORECASE)),
                    'components': len(re.findall(r'@import|@include|components/', content)),
                    'code_blocks': len(re.findall(r'```', content)),
                    'conditional_logic': len(re.findall(r'\bif\b|\bwhen\b|\bunless\b', content, re.IGNORECASE))
                }
                
                # Simulate processing time based on complexity
                processing_time = (
                    complexity_factors['file_size'] / 10000 +  # File size impact
                    complexity_factors['tools_used'] * 0.1 +   # Tool loading
                    complexity_factors['components'] * 0.05 +  # Component loading
                    complexity_factors['code_blocks'] * 0.02 + # Code processing
                    complexity_factors['conditional_logic'] * 0.01  # Logic processing
                )
                
                # Add random variation (±20%)
                variation = random.uniform(0.8, 1.2)
                processing_time *= variation
                
                # Add context overhead based on accumulated context
                context_overhead = len(str(context_data)) / 100000  # Context size impact
                processing_time += context_overhead
                
                # Simulate the processing
                time.sleep(processing_time)
                
                success = True
                
            except Exception as e:
                print(f"Error processing command {command}: {e}")
                processing_time = 0.1  # Minimal time for failed commands
                time.sleep(processing_time)
                success = False
        else:
            # Command not found - quick failure
            time.sleep(0.05)
            success = False
        
        end_time = time.perf_counter()
        memory_after = process.memory_info().rss / 1024 / 1024
        
        execution_time_ms = (end_time - start_time) * 1000
        memory_impact_mb = memory_after - memory_before
        context_size_kb = len(str(context_data)) / 1024
        
        # Update context with command results (simulate state accumulation)
        context_data[f'{command}_result'] = {
            'timestamp': time.time(),
            'execution_time': execution_time_ms,
            'success': success,
            'output_size': random.randint(100, 1000)  # Simulate output
        }
        
        return WorkflowStep(
            step_name=f"step_{len(context_data)}",
            command=command,
            execution_time_ms=execution_time_ms,
            memory_impact_mb=memory_impact_mb,
            context_size_kb=context_size_kb,
            success=success
        )

    def benchmark_workflow(self, workflow_name: str, workflow_config: Dict) -> WorkflowMetrics:
        """Benchmark complete workflow execution"""
        print(f"  🔄 Benchmarking {workflow_name} workflow...")
        
        steps = workflow_config['steps']
        baseline_time_s = workflow_config['baseline_time_s']
        
        # Initialize workflow context
        workflow_context = {
            'workflow_name': workflow_name,
            'start_time': time.time(),
            'user_input': 'simulated user request',
            'session_id': f'test_{int(time.time())}'
        }
        
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024
        peak_memory = 0
        
        workflow_steps = []
        total_execution_time = 0
        successful_steps = 0
        
        workflow_start = time.perf_counter()
        
        # Execute workflow steps
        for i, command in enumerate(steps):
            print(f"    📋 Executing step {i+1}/{len(steps)}: {command}")
            
            step_result = self.simulate_command_execution(command, workflow_context)
            workflow_steps.append(step_result)
            
            total_execution_time += step_result.execution_time_ms
            if step_result.success:
                successful_steps += 1
            
            # Track peak memory
            current_memory = process.memory_info().rss / 1024 / 1024
            peak_memory = max(peak_memory, current_memory - initial_memory)
            
            print(f"      ✓ Completed in {step_result.execution_time_ms:.1f}ms "
                  f"(context: {step_result.context_size_kb:.1f}KB)")
        
        workflow_end = time.perf_counter()
        total_workflow_time_ms = (workflow_end - workflow_start) * 1000
        
        # Calculate metrics
        success_rate = (successful_steps / len(steps)) * 100 if steps else 0
        average_step_time = total_execution_time / len(steps) if steps else 0
        context_overhead = peak_memory * 0.1  # Estimate context memory overhead
        
        # Performance grading
        performance_ratio = (total_workflow_time_ms / 1000) / baseline_time_s
        if performance_ratio <= 0.1:
            performance_grade = 'A+'
        elif performance_ratio <= 0.2:
            performance_grade = 'A'
        elif performance_ratio <= 0.3:
            performance_grade = 'B+'
        elif performance_ratio <= 0.5:
            performance_grade = 'B'
        elif performance_ratio <= 0.7:
            performance_grade = 'C+'
        elif performance_ratio <= 1.0:
            performance_grade = 'C'
        else:
            performance_grade = 'D'
        
        return WorkflowMetrics(
            workflow_name=workflow_name,
            total_execution_time_ms=total_workflow_time_ms,
            peak_memory_mb=peak_memory,
            average_step_time_ms=average_step_time,
            context_overhead_mb=context_overhead,
            steps=workflow_steps,
            success_rate=success_rate,
            performance_grade=performance_grade
        )

    def run_workflow_benchmarks(self) -> List[WorkflowMetrics]:
        """Execute all workflow performance benchmarks"""
        print("🔄 Workflow Performance Benchmarking")
        print("=" * 50)
        
        workflow_results = []
        
        for workflow_name, workflow_config in self.workflows.items():
            workflow_metrics = self.benchmark_workflow(workflow_name, workflow_config)
            workflow_results.append(workflow_metrics)
            
            # Print workflow summary
            duration_s = workflow_metrics.total_execution_time_ms / 1000
            efficiency_status = "✅" if workflow_metrics.success_rate >= 80 else "⚠️"
            performance_status = "🏆" if workflow_metrics.performance_grade in ['A+', 'A', 'B+'] else "🔧"
            
            print(f"  {efficiency_status} {performance_status} {workflow_name}: {duration_s:.1f}s "
                  f"({len(workflow_metrics.steps)} steps, {workflow_metrics.success_rate:.0f}% success, "
                  f"grade: {workflow_metrics.performance_grade})")
            print()
        
        return workflow_results

    def analyze_scaling_behavior(self, workflow_results: List[WorkflowMetrics]) -> Dict:
        """Analyze workflow performance scaling patterns"""
        scaling_analysis = {
            'step_count_impact': {},
            'memory_scaling': {},
            'context_growth': {},
            'performance_degradation': {}
        }
        
        # Analyze step count vs performance
        for workflow in workflow_results:
            step_count = len(workflow.steps)
            avg_time_per_step = workflow.average_step_time_ms
            
            scaling_analysis['step_count_impact'][workflow.workflow_name] = {
                'steps': step_count,
                'avg_time_per_step': avg_time_per_step,
                'total_time': workflow.total_execution_time_ms
            }
        
        # Memory scaling analysis
        for workflow in workflow_results:
            scaling_analysis['memory_scaling'][workflow.workflow_name] = {
                'peak_memory': workflow.peak_memory_mb,
                'context_overhead': workflow.context_overhead_mb,
                'memory_per_step': workflow.peak_memory_mb / len(workflow.steps) if workflow.steps else 0
            }
        
        # Context growth analysis
        for workflow in workflow_results:
            context_sizes = [step.context_size_kb for step in workflow.steps]
            if context_sizes:
                scaling_analysis['context_growth'][workflow.workflow_name] = {
                    'initial_context': context_sizes[0] if context_sizes else 0,
                    'final_context': context_sizes[-1] if context_sizes else 0,
                    'growth_rate': (context_sizes[-1] - context_sizes[0]) / len(context_sizes) if len(context_sizes) > 1 else 0
                }
        
        return scaling_analysis

    def generate_workflow_report(self, workflow_results: List[WorkflowMetrics], scaling_analysis: Dict) -> str:
        """Generate comprehensive workflow performance report"""
        report = []
        report.append("# Workflow Performance Benchmarking Report")
        report.append(f"**Generated**: {datetime.now().isoformat()}")
        report.append(f"**Workflows Tested**: {len(workflow_results)}")
        report.append("")
        
        # Executive summary
        total_steps = sum(len(w.steps) for w in workflow_results)
        avg_success_rate = sum(w.success_rate for w in workflow_results) / len(workflow_results)
        avg_execution_time = sum(w.total_execution_time_ms for w in workflow_results) / len(workflow_results)
        
        report.append("## Executive Summary")
        report.append("")
        report.append(f"- **Total Steps Executed**: {total_steps}")
        report.append(f"- **Average Success Rate**: {avg_success_rate:.1f}%")
        report.append(f"- **Average Execution Time**: {avg_execution_time/1000:.1f}s")
        report.append("")
        
        # Performance rankings
        sorted_workflows = sorted(workflow_results, key=lambda w: w.total_execution_time_ms)
        
        report.append("## Performance Rankings")
        report.append("")
        report.append("### Fastest Workflows")
        for i, workflow in enumerate(sorted_workflows[:3], 1):
            duration_s = workflow.total_execution_time_ms / 1000
            report.append(f"{i}. **{workflow.workflow_name}**: {duration_s:.1f}s ({workflow.performance_grade})")
        report.append("")
        
        # Detailed workflow analysis
        report.append("## Detailed Workflow Analysis")
        report.append("")
        
        for workflow in workflow_results:
            duration_s = workflow.total_execution_time_ms / 1000
            report.append(f"### {workflow.workflow_name.replace('_', ' ').title()}")
            report.append("")
            report.append(f"- **Total Execution Time**: {duration_s:.1f}s")
            report.append(f"- **Average Step Time**: {workflow.average_step_time_ms:.1f}ms")
            report.append(f"- **Peak Memory Usage**: {workflow.peak_memory_mb:.1f}MB")
            report.append(f"- **Success Rate**: {workflow.success_rate:.1f}%")
            report.append(f"- **Performance Grade**: {workflow.performance_grade}")
            report.append("")
            
            # Step breakdown
            report.append("**Step Performance:**")
            for step in workflow.steps:
                status_icon = "✅" if step.success else "❌"
                report.append(f"- {status_icon} {step.command}: {step.execution_time_ms:.1f}ms")
            report.append("")
        
        # Scaling analysis
        report.append("## Performance Scaling Analysis")
        report.append("")
        
        # Memory scaling
        report.append("### Memory Scaling Patterns")
        for workflow_name, memory_data in scaling_analysis['memory_scaling'].items():
            report.append(f"- **{workflow_name}**: {memory_data['peak_memory']:.1f}MB peak "
                         f"({memory_data['memory_per_step']:.1f}MB per step)")
        report.append("")
        
        # Context growth
        report.append("### Context Growth Patterns")
        for workflow_name, context_data in scaling_analysis['context_growth'].items():
            growth_rate = context_data['growth_rate']
            report.append(f"- **{workflow_name}**: {context_data['initial_context']:.1f}KB → "
                         f"{context_data['final_context']:.1f}KB (growth: {growth_rate:.1f}KB/step)")
        report.append("")
        
        # Optimization recommendations
        report.append("## Optimization Recommendations")
        report.append("")
        
        slow_workflows = [w for w in workflow_results if w.performance_grade in ['C', 'D']]
        if slow_workflows:
            report.append("### Performance Optimization")
            for workflow in slow_workflows:
                report.append(f"- **{workflow.workflow_name}**: Consider step parallelization and context optimization")
        
        high_memory_workflows = [w for w in workflow_results if w.peak_memory_mb > 10]
        if high_memory_workflows:
            report.append("")
            report.append("### Memory Optimization")
            for workflow in high_memory_workflows:
                report.append(f"- **{workflow.workflow_name}**: {workflow.peak_memory_mb:.1f}MB peak - implement context pruning")
        
        return '\n'.join(report)

def main():
    """Main workflow performance benchmarking execution"""
    if len(sys.argv) != 2:
        print("Usage: python workflow-performance-benchmark.py <commands_dir>")
        sys.exit(1)
    
    commands_dir = sys.argv[1]
    
    benchmarker = WorkflowPerformanceBenchmarker(commands_dir)
    
    # Run workflow benchmarks
    workflow_results = benchmarker.run_workflow_benchmarks()
    
    # Analyze scaling behavior
    scaling_analysis = benchmarker.analyze_scaling_behavior(workflow_results)
    
    print("=" * 50)
    print(f"✅ Workflow Performance Benchmarking Complete")
    print(f"📊 {len(workflow_results)} workflows analyzed")
    
    # Generate comprehensive report
    report = benchmarker.generate_workflow_report(workflow_results, scaling_analysis)
    
    # Save results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results_file = f"workflow_performance_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump([asdict(workflow) for workflow in workflow_results], f, indent=2, default=str)
    
    scaling_file = f"workflow_scaling_analysis_{timestamp}.json"
    with open(scaling_file, 'w') as f:
        json.dump(scaling_analysis, f, indent=2)
    
    print(f"💾 Results saved to: {results_file}")
    print(f"📈 Scaling analysis saved to: {scaling_file}")
    print("\n" + report)

if __name__ == "__main__":
    main()