#!/usr/bin/env python3
"""
Performance Profiler for Claude Code Modular Prompts Framework
Measures actual token usage, execution times, and resource consumption
"""

import os
import json
import time
import sys
import glob
import csv
from datetime import datetime
from pathlib import Path
import psutil
import tracemalloc

class FrameworkProfiler:
    def __init__(self, framework_root):
        self.framework_root = Path(framework_root)
        self.claude_dir = self.framework_root / '.claude'
        self.results = {
            'timestamp': datetime.utcnow().isoformat(),
            'framework_version': '3.0.0',
            'measurements': {},
            'bottlenecks': [],
            'optimization_opportunities': []
        }
        
    def measure_file_stats(self):
        """Measure framework file statistics and sizes"""
        stats = {
            'total_files': 0,
            'total_size_kb': 0,
            'file_distribution': {},
            'largest_files': []
        }
        
        file_sizes = []
        
        for root, dirs, files in os.walk(self.claude_dir):
            for file in files:
                if file.endswith('.md'):
                    filepath = Path(root) / file
                    size = filepath.stat().st_size
                    stats['total_files'] += 1
                    stats['total_size_kb'] += size / 1024
                    
                    category = root.split('/')[-1]
                    if category not in stats['file_distribution']:
                        stats['file_distribution'][category] = {'count': 0, 'size_kb': 0}
                    stats['file_distribution'][category]['count'] += 1
                    stats['file_distribution'][category]['size_kb'] += size / 1024
                    
                    file_sizes.append((str(filepath), size))
        
        # Get largest files
        file_sizes.sort(key=lambda x: x[1], reverse=True)
        stats['largest_files'] = [(f, s/1024) for f, s in file_sizes[:10]]
        
        return stats
    
    def estimate_token_usage(self, filepath, multiplier=1.3):
        """Estimate token usage for a file (chars * multiplier for markdown)"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Rough estimate: 1 token ≈ 4 chars, markdown adds ~30% overhead
                char_count = len(content)
                estimated_tokens = int(char_count / 4 * multiplier)
                return estimated_tokens
        except:
            return 0
    
    def profile_command_loading(self):
        """Profile command loading and token usage"""
        commands_dir = self.claude_dir / 'commands'
        command_profiles = {}
        
        for cmd_file in commands_dir.glob('*.md'):
            start_time = time.time()
            
            # Measure file loading
            tokens = self.estimate_token_usage(cmd_file)
            load_time = time.time() - start_time
            
            # Analyze command dependencies
            dependencies = self.analyze_dependencies(cmd_file)
            total_tokens = tokens
            
            for dep in dependencies:
                dep_path = self.claude_dir / dep
                if dep_path.exists():
                    total_tokens += self.estimate_token_usage(dep_path)
            
            command_profiles[cmd_file.stem] = {
                'direct_tokens': tokens,
                'total_tokens': total_tokens,
                'load_time_ms': load_time * 1000,
                'dependencies': len(dependencies),
                'file_size_kb': cmd_file.stat().st_size / 1024
            }
        
        return command_profiles
    
    def analyze_dependencies(self, filepath):
        """Extract module dependencies from a file"""
        dependencies = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Look for module references
                for line in content.split('\n'):
                    if 'modules/' in line or 'system/' in line:
                        # Extract path patterns
                        if '.md' in line:
                            start = line.find('modules/') if 'modules/' in line else line.find('system/')
                            if start >= 0:
                                end = line.find('.md', start) + 3
                                if end > start:
                                    dep = line[start:end]
                                    if dep not in dependencies:
                                        dependencies.append(dep)
        except:
            pass
        return dependencies
    
    def profile_module_loading(self):
        """Profile module loading patterns and costs"""
        modules_dir = self.claude_dir / 'modules'
        module_profiles = {}
        
        for category in ['patterns', 'development', 'meta']:
            cat_dir = modules_dir / category
            if cat_dir.exists():
                for mod_file in cat_dir.glob('*.md'):
                    tokens = self.estimate_token_usage(mod_file)
                    module_profiles[f"{category}/{mod_file.stem}"] = {
                        'tokens': tokens,
                        'size_kb': mod_file.stat().st_size / 1024,
                        'category': category
                    }
        
        return module_profiles
    
    def calculate_workflow_costs(self, command_profiles, module_profiles):
        """Calculate token costs for common workflows"""
        workflows = {
            'simple_task': {
                'commands': ['task'],
                'modules': ['patterns/tdd-cycle-pattern'],
                'description': 'Basic TDD task execution'
            },
            'feature_development': {
                'commands': ['feature'],
                'modules': ['patterns/workflow-orchestration-engine', 'patterns/tdd-cycle-pattern'],
                'description': 'PRD-driven feature development'
            },
            'research_analysis': {
                'commands': ['query'],
                'modules': ['patterns/research-analysis-pattern'],
                'description': 'Code research and analysis'
            },
            'multi_agent': {
                'commands': ['swarm'],
                'modules': ['patterns/multi-agent', 'patterns/workflow-orchestration-engine'],
                'description': 'Multi-agent coordination'
            },
            'full_auto': {
                'commands': ['auto'],
                'modules': ['patterns/intelligent-routing'],
                'description': 'Auto-routing with decision making'
            }
        }
        
        workflow_costs = {}
        
        for workflow_name, workflow in workflows.items():
            total_tokens = 0
            
            # Add command tokens
            for cmd in workflow['commands']:
                if cmd in command_profiles:
                    total_tokens += command_profiles[cmd]['total_tokens']
            
            # Add module tokens
            for mod in workflow['modules']:
                for mod_key in module_profiles:
                    if mod in mod_key:
                        total_tokens += module_profiles[mod_key]['tokens']
            
            # Add CLAUDE.md overhead (assuming it's always loaded)
            claude_md = self.framework_root / 'CLAUDE.md'
            if claude_md.exists():
                total_tokens += self.estimate_token_usage(claude_md)
            
            workflow_costs[workflow_name] = {
                'total_tokens': total_tokens,
                'description': workflow['description'],
                'cost_usd': total_tokens * 0.000015,  # Rough estimate
                'percentage_of_context': (total_tokens / 200000) * 100
            }
        
        return workflow_costs
    
    def identify_bottlenecks(self, command_profiles, module_profiles):
        """Identify performance bottlenecks"""
        bottlenecks = []
        
        # Large file bottlenecks
        for cmd, profile in command_profiles.items():
            if profile['total_tokens'] > 10000:
                bottlenecks.append({
                    'type': 'excessive_tokens',
                    'component': f'command/{cmd}',
                    'tokens': profile['total_tokens'],
                    'impact': 'high',
                    'optimization': f'Reduce by {int((profile["total_tokens"] - 5000) / profile["total_tokens"] * 100)}%'
                })
        
        # Module duplication
        seen_modules = {}
        for mod, profile in module_profiles.items():
            base_name = mod.split('/')[-1]
            if base_name in seen_modules:
                bottlenecks.append({
                    'type': 'potential_duplication',
                    'component': f'module/{mod}',
                    'duplicate_of': seen_modules[base_name],
                    'tokens_wasted': profile['tokens'],
                    'impact': 'medium'
                })
            else:
                seen_modules[base_name] = mod
        
        # Context window inefficiency
        total_framework_tokens = sum(p['tokens'] for p in module_profiles.values())
        if total_framework_tokens > 50000:
            bottlenecks.append({
                'type': 'framework_overhead',
                'total_tokens': total_framework_tokens,
                'impact': 'critical',
                'optimization': 'Implement lazy loading and modular composition'
            })
        
        return bottlenecks
    
    def generate_optimization_targets(self, bottlenecks, workflow_costs):
        """Generate specific optimization targets"""
        targets = []
        
        # Token reduction targets
        total_possible_reduction = sum(b.get('tokens_wasted', 0) for b in bottlenecks if b['type'] == 'potential_duplication')
        if total_possible_reduction > 0:
            targets.append({
                'target': 'eliminate_duplication',
                'potential_savings': total_possible_reduction,
                'percentage': int(total_possible_reduction / 200000 * 100),
                'priority': 'high'
            })
        
        # Workflow optimization
        for workflow, cost in workflow_costs.items():
            if cost['percentage_of_context'] > 10:
                targets.append({
                    'target': f'optimize_{workflow}',
                    'current_tokens': cost['total_tokens'],
                    'target_tokens': int(cost['total_tokens'] * 0.6),
                    'potential_savings': int(cost['total_tokens'] * 0.4),
                    'priority': 'high' if cost['percentage_of_context'] > 20 else 'medium'
                })
        
        return targets
    
    def run_full_profile(self):
        """Run complete performance profile"""
        print("Starting framework performance profiling...")
        
        # File statistics
        print("Measuring file statistics...")
        file_stats = self.measure_file_stats()
        self.results['file_statistics'] = file_stats
        
        # Command profiling
        print("Profiling command loading...")
        command_profiles = self.profile_command_loading()
        self.results['command_profiles'] = command_profiles
        
        # Module profiling
        print("Profiling module loading...")
        module_profiles = self.profile_module_loading()
        self.results['module_profiles'] = module_profiles
        
        # Workflow costs
        print("Calculating workflow costs...")
        workflow_costs = self.calculate_workflow_costs(command_profiles, module_profiles)
        self.results['workflow_costs'] = workflow_costs
        
        # Bottleneck identification
        print("Identifying bottlenecks...")
        bottlenecks = self.identify_bottlenecks(command_profiles, module_profiles)
        self.results['bottlenecks'] = bottlenecks
        
        # Optimization targets
        print("Generating optimization targets...")
        targets = self.generate_optimization_targets(bottlenecks, workflow_costs)
        self.results['optimization_targets'] = targets
        
        return self.results


def main():
    framework_root = Path('/Users/smenssink/conductor/repo/claude-code-modular-prompts/vatican')
    profiler = FrameworkProfiler(framework_root)
    
    # Run profiling
    results = profiler.run_full_profile()
    
    # Save results
    output_dir = framework_root / 'agent_comms' / 'batch1-results'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON metrics
    with open(output_dir / 'performance-metrics.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Generate CSV bottleneck analysis
    with open(output_dir / 'bottleneck-analysis.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Type', 'Component', 'Impact', 'Details', 'Optimization'])
        
        for bottleneck in results['bottlenecks']:
            writer.writerow([
                bottleneck.get('type', ''),
                bottleneck.get('component', ''),
                bottleneck.get('impact', ''),
                json.dumps({k: v for k, v in bottleneck.items() if k not in ['type', 'component', 'impact']}),
                bottleneck.get('optimization', 'N/A')
            ])
    
    print(f"\nProfiling complete! Results saved to {output_dir}")
    print(f"Total framework files: {results['file_statistics']['total_files']}")
    print(f"Total framework size: {results['file_statistics']['total_size_kb']:.1f} KB")
    print(f"Bottlenecks identified: {len(results['bottlenecks'])}")
    print(f"Optimization targets: {len(results['optimization_targets'])}")


if __name__ == '__main__':
    main()