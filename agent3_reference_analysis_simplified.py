#!/usr/bin/env python3
"""
Agent 3: Reference Pattern Analyst (Simplified)
Quick analysis of reference patterns using Agent 1 and Agent 2 foundation data
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

class ReferencePatternAnalyst:
    def __init__(self, base_path=".claude"):
        self.base_path = Path(base_path)
        self.broken_references = defaultdict(list)
        self.reference_patterns = defaultdict(int)
        self.fix_strategies = []
        
        # Load foundation data from previous agents
        self.agent1_data = self.load_agent1_data()
        self.agent2_data = self.load_agent2_data()
        
    def load_agent1_data(self):
        """Load Agent 1's inventory data"""
        try:
            with open("agent1_inventory_results.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Agent 1 data not found")
            return {}
    
    def load_agent2_data(self):
        """Load Agent 2's directory audit data"""
        try:
            with open("agent2_directory_audit_results.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Agent 2 data not found")
            return {}
    
    def quick_reference_analysis(self):
        """Quick analysis of reference patterns"""
        print("🔍 Agent 3: Quick reference pattern analysis...")
        
        results = {
            'files_analyzed': 0,
            'total_references': 0,
            'broken_references': 0,
            'reference_types': defaultdict(int),
            'broken_patterns': defaultdict(int),
            'structural_impact': {}
        }
        
        # Get files with dependencies from Agent 1 if available
        if self.agent1_data and 'handoff_data' in self.agent1_data:
            files_with_deps = self.agent1_data['handoff_data']['agent_3_reference_analysis']['files_with_dependencies']
            
            for file_path, dependencies in files_with_deps.items():
                results['files_analyzed'] += 1
                results['total_references'] += len(dependencies)
                
                for dep in dependencies:
                    # Classify reference type
                    ref_type = self.classify_reference_type(dep)
                    results['reference_types'][ref_type] += 1
                    
                    # Check if reference is broken
                    if self.is_reference_broken(file_path, dep):
                        results['broken_references'] += 1
                        break_reason = self.get_break_reason(dep)
                        results['broken_patterns'][break_reason] += 1
                        
                        self.broken_references[file_path].append({
                            'reference': dep,
                            'break_reason': break_reason,
                            'structural_cause': self.get_structural_cause(dep)
                        })
        
        # Calculate percentages
        if results['total_references'] > 0:
            results['broken_percentage'] = (results['broken_references'] / results['total_references']) * 100
        else:
            results['broken_percentage'] = 0
        
        # Analyze structural impact using Agent 2 data
        if self.agent2_data:
            results['structural_impact'] = self.analyze_structural_impact()
        
        print(f"📊 Quick analysis: {results['broken_references']}/{results['total_references']} broken ({results['broken_percentage']:.1f}%)")
        return results
    
    def classify_reference_type(self, reference):
        """Classify the type of reference"""
        if reference.startswith('../'):
            return 'relative_parent'
        elif reference.startswith('./'):
            return 'relative_current'
        elif reference.startswith('system/'):
            return 'system_module'
        elif reference.startswith('patterns/'):
            return 'pattern_module'
        elif reference.startswith('modules/'):
            return 'module_reference'
        elif '/' in reference:
            return 'path_reference'
        else:
            return 'direct_reference'
    
    def is_reference_broken(self, source_file, reference):
        """Quick check if a reference is broken"""
        # Try to resolve relative to .claude
        claude_path = self.base_path / reference
        if claude_path.exists():
            return False
        
        # Try relative to source file
        source_path = Path(source_file)
        if source_path.exists():
            relative_path = source_path.parent / reference
            if relative_path.exists():
                return False
        
        # Try simple search by filename
        filename = Path(reference).name
        for found in self.base_path.rglob(filename):
            return False
        
        return True  # Couldn't find it anywhere
    
    def get_break_reason(self, reference):
        """Determine why a reference is broken"""
        if reference.startswith('../'):
            return 'RELATIVE_PATH_ISSUE'
        elif reference.startswith('system/') or reference.startswith('patterns/'):
            return 'STRUCTURAL_REORGANIZATION'
        elif '/' not in reference:
            return 'MISSING_FILE'
        else:
            return 'PATH_RESOLUTION_FAILURE'
    
    def get_structural_cause(self, reference):
        """Get structural cause from Agent 2 data"""
        if not self.agent2_data:
            return 'NO_STRUCTURAL_CONTEXT'
        
        # Check if affected by pattern duplication
        if 'patterns/' in reference:
            overlaps = self.agent2_data.get('overlaps', [])
            for overlap in overlaps:
                if overlap.get('type') == 'PATTERN_DUPLICATION':
                    return 'PATTERN_DUPLICATION_CONFLICT'
        
        return 'STRUCTURAL_REORGANIZATION_NEEDED'
    
    def analyze_structural_impact(self):
        """Analyze how Agent 2's findings impact references"""
        impact = {
            'directory_complexity': len(self.agent2_data.get('actual_structure', {})),
            'structural_overlaps': len(self.agent2_data.get('overlaps', [])),
            'documentation_inconsistencies': len(self.agent2_data.get('inconsistencies', [])),
            'consolidation_needed': 'YES' if len(self.agent2_data.get('overlaps', [])) > 2 else 'NO'
        }
        
        # Assess severity
        if impact['structural_overlaps'] > 3:
            impact['severity'] = 'CRITICAL'
        elif impact['structural_overlaps'] > 1:
            impact['severity'] = 'HIGH'
        else:
            impact['severity'] = 'MEDIUM'
        
        return impact
    
    def generate_fix_strategies(self, analysis_results):
        """Generate prioritized fix strategies"""
        print("💡 Agent 3: Generating fix strategies...")
        
        strategies = []
        
        # Strategy based on most common break pattern
        broken_patterns = analysis_results['broken_patterns']
        most_common = max(broken_patterns.items(), key=lambda x: x[1]) if broken_patterns else None
        
        if most_common and most_common[1] > 10:
            pattern, count = most_common
            strategies.append({
                'priority': 'HIGH',
                'strategy': f'FIX_{pattern}',
                'description': f'Address {count} broken references of type {pattern}',
                'affected_count': count,
                'effort': 'HIGH' if count > 20 else 'MEDIUM'
            })
        
        # Strategy based on structural impact
        structural_impact = analysis_results.get('structural_impact', {})
        if structural_impact.get('severity') == 'CRITICAL':
            strategies.append({
                'priority': 'CRITICAL',
                'strategy': 'STRUCTURAL_CONSOLIDATION_FIRST',
                'description': 'Consolidate structure before fixing references',
                'affected_count': analysis_results['broken_references'],
                'effort': 'HIGH',
                'prerequisites': ['Agent 5 architecture design', 'Agent 6 migration plan']
            })
        
        # General reference cleanup strategy
        if analysis_results['broken_percentage'] > 30:
            strategies.append({
                'priority': 'HIGH',
                'strategy': 'COMPREHENSIVE_REFERENCE_CLEANUP',
                'description': f"Fix {analysis_results['broken_references']} broken references",
                'affected_count': analysis_results['broken_references'],
                'effort': 'HIGH'
            })
        
        self.fix_strategies = strategies
        print(f"📋 Generated {len(strategies)} fix strategies")
        return strategies
    
    def run_analysis(self):
        """Run complete simplified analysis"""
        print("🔗 Agent 3: Starting simplified reference analysis...")
        
        # Quick reference analysis
        analysis_results = self.quick_reference_analysis()
        
        # Generate fix strategies
        fix_strategies = self.generate_fix_strategies(analysis_results)
        
        # Generate report
        report = {
            'analysis_timestamp': datetime.now().isoformat(),
            'agent': 'Agent 3 - Reference Pattern Analyst (Simplified)',
            'analysis_results': analysis_results,
            'broken_reference_details': dict(self.broken_references),
            'fix_strategies': fix_strategies,
            'handoff_data': {
                'agent_4_testing_guidance': {
                    'broken_reference_count': analysis_results['broken_references'],
                    'broken_percentage': analysis_results['broken_percentage'],
                    'critical_issues': [s for s in fix_strategies if s['priority'] == 'CRITICAL']
                },
                'agent_5_architecture_input': {
                    'reference_complexity_score': analysis_results['broken_references'],
                    'structural_consolidation_required': analysis_results.get('structural_impact', {}).get('consolidation_needed') == 'YES'
                },
                'agent_8_reference_reconciliation': {
                    'broken_reference_catalog': dict(self.broken_references),
                    'fix_priority_order': sorted(fix_strategies, key=lambda x: {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2}.get(x['priority'], 3))
                }
            }
        }
        
        print("✅ Agent 3: Simplified reference analysis complete")
        return report
    
    def save_results(self, output_file="agent3_reference_analysis_results.json"):
        """Save analysis results"""
        report = self.run_analysis()
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"💾 Agent 3: Results saved to {output_file}")
        return report

if __name__ == "__main__":
    analyst = ReferencePatternAnalyst()
    report = analyst.save_results()
    
    # Print summary
    print("\n" + "="*80)
    print("AGENT 3 REFERENCE ANALYSIS SUMMARY")
    print("="*80)
    results = report['analysis_results']
    print(f"📁 Files Analyzed: {results['files_analyzed']}")
    print(f"🔗 Total References: {results['total_references']}")
    print(f"💔 Broken References: {results['broken_references']} ({results['broken_percentage']:.1f}%)")
    print(f"🛠️  Fix Strategies: {len(report['fix_strategies'])}")
    
    if report['fix_strategies']:
        print("\n🚨 Priority Fix Strategies:")
        for strategy in report['fix_strategies']:
            print(f"  {strategy['priority']}: {strategy['strategy']} - {strategy['description']}")
    
    structural_impact = results.get('structural_impact', {})
    if structural_impact:
        print(f"\n🏗️  Structural Impact: {structural_impact.get('severity', 'UNKNOWN')} severity")
        print(f"   Directory Complexity: {structural_impact.get('directory_complexity', 0)}")
        print(f"   Overlaps: {structural_impact.get('structural_overlaps', 0)}")
        print(f"   Consolidation Needed: {structural_impact.get('consolidation_needed', 'UNKNOWN')}")
    
    print(f"\n✅ Agent 3 Complete - Reference analysis data ready for Agent 4, 5, and 8")