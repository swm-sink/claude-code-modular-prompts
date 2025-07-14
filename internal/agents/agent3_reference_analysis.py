#!/usr/bin/env python3
"""
Agent 3: Reference Pattern Analyst
Analyze actual vs. claimed reference patterns using Agent 1 and Agent 2 foundation data
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import networkx as nx

class ReferencePatternAnalyst:
    def __init__(self, base_path=".claude"):
        self.base_path = Path(base_path)
        self.reference_network = nx.DiGraph()
        self.broken_references = defaultdict(list)
        self.reference_patterns = defaultdict(int)
        self.circular_dependencies = []
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
            print("⚠️  Agent 1 data not found - operating without inventory context")
            return {}
    
    def load_agent2_data(self):
        """Load Agent 2's directory audit data"""
        try:
            with open("agent2_directory_audit_results.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Agent 2 data not found - operating without structure context")
            return {}
    
    def extract_all_references(self):
        """Extract all references from all markdown files"""
        print("🔍 Agent 3: Extracting reference patterns from all files...")
        
        references = {}
        
        # Get files with dependencies from Agent 1 data
        if self.agent1_data and 'handoff_data' in self.agent1_data:
            files_with_deps = self.agent1_data['handoff_data']['agent_3_reference_analysis']['files_with_dependencies']
            
            for file_path, dependencies in files_with_deps.items():
                references[file_path] = {
                    'dependencies': dependencies,
                    'exists': Path(file_path).exists(),
                    'file_category': self.get_file_category(file_path),
                    'reference_types': self.classify_reference_types(dependencies)
                }
        else:
            # Fallback: scan all files directly
            print("📂 Fallback: Scanning all files for references...")
            for md_file in self.base_path.rglob("*.md"):
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                deps = self.extract_md_references(content)
                if deps:
                    references[str(md_file)] = {
                        'dependencies': deps,
                        'exists': True,
                        'file_category': self.get_file_category(str(md_file)),
                        'reference_types': self.classify_reference_types(deps)
                    }
        
        print(f"📊 Found {len(references)} files with references")
        return references
    
    def extract_md_references(self, content):
        """Extract markdown file references from content"""
        # Find all .md references
        patterns = [
            r'([a-zA-Z0-9_/./-]+\.md)',  # Direct .md references
            r'\[.*?\]\(([^)]+\.md)\)',    # Markdown links
            r'<[^>]+>([^<]+\.md)',       # XML references
        ]
        
        references = []
        for pattern in patterns:
            matches = re.findall(pattern, content)
            references.extend(matches)
        
        # Clean and deduplicate
        clean_refs = []
        for ref in references:
            # Skip web URLs
            if ref.startswith('http'):
                continue
            # Normalize path separators
            ref = ref.replace('\\', '/')
            if ref not in clean_refs:
                clean_refs.append(ref)
        
        return clean_refs
    
    def get_file_category(self, file_path):
        """Get file category from Agent 1 data"""
        if self.agent1_data and 'inventory' in self.agent1_data:
            return self.agent1_data['inventory'].get(file_path, {}).get('category', 'UNKNOWN')
        return 'UNKNOWN'
    
    def classify_reference_types(self, dependencies):
        """Classify types of references"""
        types = defaultdict(int)
        
        for dep in dependencies:
            if dep.startswith('../'):
                types['relative_parent'] += 1
            elif dep.startswith('./'):
                types['relative_current'] += 1
            elif dep.startswith('/'):
                types['absolute'] += 1
            elif dep.startswith('system/'):
                types['system_module'] += 1
            elif dep.startswith('patterns/'):
                types['pattern_module'] += 1
            elif dep.startswith('modules/'):
                types['module_reference'] += 1
            elif '/' in dep:
                types['path_reference'] += 1
            else:
                types['direct_reference'] += 1
        
        return dict(types)
    
    def analyze_reference_validity(self, references):
        """Analyze which references are valid vs broken"""
        print("🔍 Agent 3: Analyzing reference validity...")
        
        broken_count = 0
        valid_count = 0
        
        for source_file, ref_data in references.items():
            source_path = Path(source_file)
            
            for dependency in ref_data['dependencies']:
                # Try to resolve the reference
                resolved_path = self.resolve_reference_path(source_path, dependency)
                
                if resolved_path and resolved_path.exists():
                    valid_count += 1
                    # Add to network graph
                    self.reference_network.add_edge(source_file, str(resolved_path))
                else:
                    broken_count += 1
                    self.broken_references[source_file].append({
                        'reference': dependency,
                        'attempted_resolution': str(resolved_path) if resolved_path else None,
                        'break_type': self.classify_break_type(dependency),
                        'structural_cause': self.identify_structural_cause(dependency)
                    })
        
        total_refs = broken_count + valid_count
        broken_percentage = (broken_count / total_refs * 100) if total_refs > 0 else 0
        
        print(f"📊 Reference Analysis: {broken_count} broken, {valid_count} valid ({broken_percentage:.1f}% broken)")
        
        return {
            'total_references': total_refs,
            'broken_count': broken_count,
            'valid_count': valid_count,
            'broken_percentage': broken_percentage
        }
    
    def resolve_reference_path(self, source_path, reference):
        """Attempt to resolve a reference to an actual file path"""
        # Try different resolution strategies
        
        # Strategy 1: Relative to source file
        if reference.startswith('./') or reference.startswith('../'):
            resolved = (source_path.parent / reference).resolve()
            if resolved.exists():
                return resolved
        
        # Strategy 2: Relative to .claude root
        claude_relative = self.base_path / reference
        if claude_relative.exists():
            return claude_relative
        
        # Strategy 3: Absolute from project root
        if reference.startswith('/'):
            project_relative = Path('.') / reference.lstrip('/')
            if project_relative.exists():
                return project_relative
        
        # Strategy 4: Search for file by name (last resort)
        filename = Path(reference).name
        for found_file in self.base_path.rglob(filename):
            return found_file
        
        return None
    
    def classify_break_type(self, reference):
        """Classify why a reference is broken"""
        if reference.startswith('../'):
            return 'RELATIVE_PATH_ISSUE'
        elif reference.startswith('system/') or reference.startswith('patterns/'):
            return 'STRUCTURAL_REORGANIZATION'
        elif '/' not in reference:
            return 'MISSING_FILE'
        else:
            return 'PATH_RESOLUTION_FAILURE'
    
    def identify_structural_cause(self, reference):
        """Identify if Agent 2's structural findings explain the broken reference"""
        if not self.agent2_data:
            return 'NO_STRUCTURAL_CONTEXT'
        
        overlaps = self.agent2_data.get('overlaps', [])
        
        # Check if this reference is affected by structural overlaps
        for overlap in overlaps:
            if overlap['type'] == 'PATTERN_DUPLICATION' and 'patterns/' in reference:
                return 'PATTERN_DUPLICATION_CONFLICT'
            elif overlap['type'] == 'FUNCTIONAL_OVERLAP':
                for directory in overlap['directories']:
                    if any(dir_part in reference for dir_part in directory.split('/')):
                        return f"FUNCTIONAL_OVERLAP_{overlap['category'].upper()}"
        
        # Check inconsistencies
        inconsistencies = self.agent2_data.get('inconsistencies', [])
        for inconsistency in inconsistencies:
            if inconsistency['type'] == 'MISSING_CLAIMED_DIRECTORY':
                claimed = inconsistency['claimed']
                if claimed in reference:
                    return 'MISSING_CLAIMED_DIRECTORY'
        
        return 'STRUCTURAL_UNKNOWN'
    
    def detect_circular_dependencies(self):
        """Detect circular dependencies in the reference network"""
        print("🔍 Agent 3: Detecting circular dependencies...")
        
        try:
            cycles = list(nx.simple_cycles(self.reference_network))
            
            circular_deps = []
            for cycle in cycles:
                if len(cycle) > 1:  # Ignore self-references
                    circular_deps.append({
                        'cycle': cycle,
                        'length': len(cycle),
                        'severity': 'HIGH' if len(cycle) > 3 else 'MEDIUM',
                        'files_involved': cycle,
                        'impact_analysis': self.analyze_cycle_impact(cycle)
                    })
            
            self.circular_dependencies = circular_deps
            print(f"🔄 Found {len(circular_deps)} circular dependency cycles")
            
            return circular_deps
        
        except Exception as e:
            print(f"⚠️  Error detecting cycles: {e}")
            return []
    
    def analyze_cycle_impact(self, cycle):
        """Analyze the impact of a circular dependency cycle"""
        categories = []
        for file_path in cycle:
            category = self.get_file_category(file_path)
            categories.append(category)
        
        # Determine impact based on categories involved
        if 'COMMAND' in categories:
            return 'HIGH - Commands involved in cycle'
        elif 'QUALITY_MODULE' in categories:
            return 'HIGH - Quality infrastructure affected'
        elif len(set(categories)) > 2:
            return 'MEDIUM - Multiple categories involved'
        else:
            return 'LOW - Single category cycle'
    
    def analyze_reference_patterns(self, references):
        """Analyze patterns in how files reference each other"""
        print("🔍 Agent 3: Analyzing reference patterns...")
        
        patterns = {
            'cross_category_references': defaultdict(int),
            'reference_depth_distribution': defaultdict(int),
            'most_referenced_files': defaultdict(int),
            'reference_type_distribution': defaultdict(int),
            'structural_impact_analysis': {}
        }
        
        # Analyze cross-category references
        for source_file, ref_data in references.items():
            source_category = ref_data['file_category']
            
            for dep in ref_data['dependencies']:
                target_path = self.resolve_reference_path(Path(source_file), dep)
                if target_path:
                    target_category = self.get_file_category(str(target_path))
                    patterns['cross_category_references'][f"{source_category}→{target_category}"] += 1
                    patterns['most_referenced_files'][str(target_path)] += 1
            
            # Analyze reference depth
            ref_count = len(ref_data['dependencies'])
            if ref_count == 0:
                patterns['reference_depth_distribution']['isolated'] += 1
            elif ref_count <= 3:
                patterns['reference_depth_distribution']['low_coupling'] += 1
            elif ref_count <= 7:
                patterns['reference_depth_distribution']['medium_coupling'] += 1
            else:
                patterns['reference_depth_distribution']['high_coupling'] += 1
            
            # Analyze reference types
            for ref_type, count in ref_data['reference_types'].items():
                patterns['reference_type_distribution'][ref_type] += count
        
        # Analyze structural impact using Agent 2 data
        if self.agent2_data:
            patterns['structural_impact_analysis'] = {
                'directories_with_references': len(set(
                    str(Path(f).parent) for f in references.keys()
                )),
                'structural_overlap_impact': self.calculate_overlap_impact(references),
                'documentation_mismatch_impact': self.calculate_documentation_impact(references)
            }
        
        self.reference_patterns = patterns
        print("📊 Reference pattern analysis complete")
        return patterns
    
    def calculate_overlap_impact(self, references):
        """Calculate how structural overlaps impact references"""
        if not self.agent2_data or 'overlaps' not in self.agent2_data:
            return {}
        
        impact = {}
        overlaps = self.agent2_data['overlaps']
        
        for overlap in overlaps:
            overlap_type = overlap['type']
            affected_dirs = overlap.get('directories', [])
            
            # Count references affected by this overlap
            affected_refs = 0
            for source_file, ref_data in references.items():
                for dep in ref_data['dependencies']:
                    if any(affected_dir in dep for affected_dir in affected_dirs):
                        affected_refs += 1
            
            if affected_refs > 0:
                impact[overlap_type] = {
                    'affected_references': affected_refs,
                    'affected_directories': affected_dirs,
                    'severity': overlap.get('severity', 'UNKNOWN')
                }
        
        return impact
    
    def calculate_documentation_impact(self, references):
        """Calculate how documentation mismatches impact references"""
        if not self.agent2_data or 'inconsistencies' not in self.agent2_data:
            return {}
        
        inconsistencies = self.agent2_data['inconsistencies']
        doc_impact = {
            'missing_claimed_directories': 0,
            'undocumented_directory_references': 0,
            'total_affected_references': 0
        }
        
        for inconsistency in inconsistencies:
            if inconsistency['type'] == 'MISSING_CLAIMED_DIRECTORY':
                claimed = inconsistency['claimed']
                # Count references to missing claimed directories
                for source_file, ref_data in references.items():
                    for dep in ref_data['dependencies']:
                        if claimed in dep:
                            doc_impact['missing_claimed_directories'] += 1
                            doc_impact['total_affected_references'] += 1
        
        return doc_impact
    
    def generate_fix_strategies(self):
        """Generate strategies for fixing broken references"""
        print("💡 Agent 3: Generating reference fix strategies...")
        
        strategies = []
        
        # Analyze broken reference patterns
        break_type_counts = defaultdict(int)
        structural_cause_counts = defaultdict(int)
        
        for source_file, broken_refs in self.broken_references.items():
            for broken_ref in broken_refs:
                break_type_counts[broken_ref['break_type']] += 1
                structural_cause_counts[broken_ref['structural_cause']] += 1
        
        # Generate strategies based on break patterns
        if break_type_counts['STRUCTURAL_REORGANIZATION'] > 10:
            strategies.append({
                'priority': 'HIGH',
                'strategy': 'STRUCTURAL_CONSOLIDATION',
                'description': 'Consolidate duplicate directory structures before fixing references',
                'affected_references': break_type_counts['STRUCTURAL_REORGANIZATION'],
                'prerequisites': ['Agent 5 architecture design', 'Agent 6 migration plan'],
                'estimated_effort': 'HIGH'
            })
        
        if break_type_counts['RELATIVE_PATH_ISSUE'] > 5:
            strategies.append({
                'priority': 'MEDIUM',
                'strategy': 'STANDARDIZE_PATHS',
                'description': 'Convert relative paths to standardized absolute paths',
                'affected_references': break_type_counts['RELATIVE_PATH_ISSUE'],
                'prerequisites': ['Directory structure finalized'],
                'estimated_effort': 'MEDIUM'
            })
        
        if structural_cause_counts['PATTERN_DUPLICATION_CONFLICT'] > 0:
            strategies.append({
                'priority': 'CRITICAL',
                'strategy': 'RESOLVE_PATTERN_CONFLICTS',
                'description': 'Eliminate pattern duplication before reference updates',
                'affected_references': structural_cause_counts['PATTERN_DUPLICATION_CONFLICT'],
                'prerequisites': ['Agent 2 pattern consolidation recommendations'],
                'estimated_effort': 'HIGH'
            })
        
        # Strategy for circular dependencies
        if self.circular_dependencies:
            strategies.append({
                'priority': 'HIGH',
                'strategy': 'BREAK_CIRCULAR_DEPENDENCIES',
                'description': f'Resolve {len(self.circular_dependencies)} circular dependency cycles',
                'affected_references': sum(len(cycle['cycle']) for cycle in self.circular_dependencies),
                'prerequisites': ['Dependency analysis complete'],
                'estimated_effort': 'MEDIUM'
            })
        
        self.fix_strategies = strategies
        print(f"📋 Generated {len(strategies)} fix strategies")
        return strategies
    
    def run_complete_analysis(self):
        """Run complete reference pattern analysis"""
        print("🔗 Agent 3: Starting complete reference pattern analysis...")
        
        # Step 1: Extract all references
        references = self.extract_all_references()
        
        # Step 2: Analyze reference validity
        validity_analysis = self.analyze_reference_validity(references)
        
        # Step 3: Detect circular dependencies
        circular_deps = self.detect_circular_dependencies()
        
        # Step 4: Analyze reference patterns
        pattern_analysis = self.analyze_reference_patterns(references)
        
        # Step 5: Generate fix strategies
        fix_strategies = self.generate_fix_strategies()
        
        # Generate comprehensive report
        report = self.generate_reference_report(references, validity_analysis, pattern_analysis)
        
        print("✅ Agent 3: Reference pattern analysis complete")
        return report
    
    def generate_reference_report(self, references, validity_analysis, pattern_analysis):
        """Generate comprehensive reference analysis report"""
        return {
            'analysis_timestamp': datetime.now().isoformat(),
            'agent': 'Agent 3 - Reference Pattern Analyst',
            'analysis_summary': {
                'files_with_references': len(references),
                'total_references': validity_analysis['total_references'],
                'broken_references': validity_analysis['broken_count'],
                'broken_percentage': validity_analysis['broken_percentage'],
                'circular_dependencies': len(self.circular_dependencies),
                'fix_strategies_generated': len(self.fix_strategies)
            },
            'reference_validity': validity_analysis,
            'broken_reference_details': dict(self.broken_references),
            'circular_dependencies': self.circular_dependencies,
            'reference_patterns': pattern_analysis,
            'fix_strategies': self.fix_strategies,
            'structural_impact_assessment': self.assess_structural_impact(),
            'handoff_data': self.prepare_reference_handoff_data()
        }
    
    def assess_structural_impact(self):
        """Assess how Agent 2's structural findings impact references"""
        if not self.agent2_data:
            return {'status': 'NO_STRUCTURAL_DATA'}
        
        return {
            'directory_complexity_multiplier': len(self.agent2_data.get('actual_structure', {})) / 25,  # Baseline 25 dirs
            'overlap_reference_conflicts': len([
                overlap for overlap in self.agent2_data.get('overlaps', [])
                if overlap.get('severity') == 'CRITICAL'
            ]),
            'documentation_mismatch_impact': len([
                inconsist for inconsist in self.agent2_data.get('inconsistencies', [])
                if inconsist.get('severity') == 'HIGH'
            ]),
            'consolidation_requirement': 'CRITICAL' if len(self.agent2_data.get('overlaps', [])) > 2 else 'MEDIUM'
        }
    
    def prepare_reference_handoff_data(self):
        """Prepare handoff data for subsequent agents"""
        return {
            'agent_4_testing_guidance': {
                'broken_reference_hotspots': [
                    source for source, refs in self.broken_references.items()
                    if len(refs) > 3
                ],
                'circular_dependency_files': [
                    file for cycle in self.circular_dependencies
                    for file in cycle['files_involved']
                ],
                'critical_reference_paths': [
                    strategy for strategy in self.fix_strategies
                    if strategy['priority'] == 'CRITICAL'
                ]
            },
            'agent_5_architecture_input': {
                'reference_complexity_score': len(self.broken_references),
                'consolidation_impact_assessment': self.assess_structural_impact(),
                'required_path_standardization': len(self.fix_strategies)
            },
            'agent_8_reference_reconciliation': {
                'broken_reference_catalog': dict(self.broken_references),
                'fix_strategy_priority_order': sorted(
                    self.fix_strategies, 
                    key=lambda x: {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2}.get(x['priority'], 3)
                ),
                'circular_dependency_resolution_plan': self.circular_dependencies
            }
        }
    
    def save_analysis_results(self, output_file="agent3_reference_analysis_results.json"):
        """Save reference analysis results to file"""
        references = self.extract_all_references()
        validity_analysis = self.analyze_reference_validity(references)
        pattern_analysis = self.analyze_reference_patterns(references)
        report = self.generate_reference_report(references, validity_analysis, pattern_analysis)
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"💾 Agent 3: Reference analysis results saved to {output_file}")
        return report

if __name__ == "__main__":
    analyst = ReferencePatternAnalyst()
    report = analyst.run_complete_analysis()
    analyst.save_analysis_results()
    
    # Print summary for immediate visibility
    print("\n" + "="*80)
    print("AGENT 3 REFERENCE PATTERN ANALYSIS SUMMARY")
    print("="*80)
    print(f"🔗 Files with References: {report['analysis_summary']['files_with_references']}")
    print(f"📊 Total References: {report['analysis_summary']['total_references']}")
    print(f"💔 Broken References: {report['analysis_summary']['broken_references']} ({report['analysis_summary']['broken_percentage']:.1f}%)")
    print(f"🔄 Circular Dependencies: {report['analysis_summary']['circular_dependencies']}")
    print(f"🛠️  Fix Strategies: {report['analysis_summary']['fix_strategies_generated']}")
    
    if report['fix_strategies']:
        print("\n🚨 Priority Fix Strategies:")
        for strategy in sorted(report['fix_strategies'], key=lambda x: {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2}.get(x['priority'], 3)):
            print(f"  {strategy['priority']}: {strategy['strategy']} - {strategy['description']}")
    
    print(f"\n✅ Agent 3 Complete - Reference analysis data ready for Agent 4, 5, and 8")