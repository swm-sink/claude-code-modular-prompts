#!/usr/bin/env python3
"""
Step 8: Dependency Mapping - XML Cross-References and Relationships Analysis
"""

import re
import json
from pathlib import Path
from collections import defaultdict, Counter
import networkx as nx

def find_xml_files():
    """Find all XML-tagged markdown files"""
    project_root = Path(".")
    xml_files = []
    
    for md_file in project_root.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if '<ai_document_metadata>' in content:
                    xml_files.append(md_file)
        except (UnicodeDecodeError, PermissionError):
            continue
    
    return xml_files

def extract_dependencies(file_path):
    """Extract all XML cross-references from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return {}
    
    dependencies = {
        'file_references': [],
        'component_references': [],
        'command_references': [],
        'context_references': [],
        'hardcoded_counts': [],
        'hardcoded_paths': []
    }
    
    # File references pattern
    file_ref_patterns = [
        r'<file[^>]*ref="([^"]*)"[^>]*>',
        r'ref="([^"]*\.md)"',
        r'<context_file[^>]*ref="([^"]*)"',
        r'<upstream_dependencies>.*?<file[^>]*ref="([^"]*)"',
        r'<downstream_consumers>.*?<file[^>]*ref="([^"]*)"'
    ]
    
    for pattern in file_ref_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        dependencies['file_references'].extend(matches)
    
    # Component references
    component_patterns = [
        r'<component[^>]*ref="([^"]*)"',
        r'<required_components>.*?<component[^>]*ref="([^"]*)"',
        r'<compatible_components>.*?<component[^>]*ref="([^"]*)"',
        r'<incompatible_components>.*?<component[^>]*ref="([^"]*)"'
    ]
    
    for pattern in component_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        dependencies['component_references'].extend(matches)
    
    # Command references
    command_patterns = [
        r'<command[^>]*ref="([^"]*)"',
        r'<invokable_commands>.*?<command[^>]*ref="([^"]*)"',
        r'/([a-zA-Z-]+)', # Slash commands
    ]
    
    for pattern in command_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        dependencies['command_references'].extend(matches)
    
    # Context file references
    context_patterns = [
        r'<context_file[^>]*ref="([^"]*)"',
        r'<required_context>.*?<context_file[^>]*ref="([^"]*)"',
        r'<helpful_context>.*?<context_file[^>]*ref="([^"]*)"'
    ]
    
    for pattern in context_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        dependencies['context_references'].extend(matches)
    
    # Hardcoded counts
    count_patterns = [
        r'<command_count>(\d+)</command_count>',
        r'<component_count>(\d+)</component_count>',
        r'<total_commands>(\d+)</total_commands>',
        r'<total_components>(\d+)</total_components>',
        r'<progressive_disclosure_layers>(\d+)</progressive_disclosure_layers>'
    ]
    
    for pattern in count_patterns:
        matches = re.findall(pattern, content)
        dependencies['hardcoded_counts'].extend(matches)
    
    # Hardcoded paths
    path_patterns = [
        r'<file_path>([^<]*)</file_path>',
        r'/Users/[^<\s]*',
        r'/claude-code-modular-prompts/[^<\s]*'
    ]
    
    for pattern in path_patterns:
        matches = re.findall(pattern, content)
        dependencies['hardcoded_paths'].extend(matches)
    
    # Clean up and deduplicate
    for key in dependencies:
        dependencies[key] = list(set(dependencies[key]))  # Remove duplicates
        dependencies[key] = [item for item in dependencies[key] if item.strip()]  # Remove empty
    
    return dependencies

def analyze_dependency_complexity(xml_files):
    """Analyze the overall dependency complexity"""
    all_dependencies = {}
    dependency_stats = {
        'total_files': len(xml_files),
        'total_file_references': 0,
        'total_component_references': 0,
        'total_command_references': 0,
        'total_context_references': 0,
        'total_hardcoded_counts': 0,
        'total_hardcoded_paths': 0,
        'files_with_dependencies': 0,
        'high_dependency_files': [],
        'broken_references': [],
        'circular_references': [],
        'most_referenced_files': Counter(),
        'most_referenced_components': Counter(),
        'hardcoded_count_distribution': Counter()
    }
    
    print("Analyzing dependencies across files...")
    
    for i, file_path in enumerate(xml_files):
        if i % 10 == 0:
            print(f"  Processing {i+1}/{len(xml_files)}")
        
        relative_path = str(file_path.relative_to(Path(".")))
        dependencies = extract_dependencies(file_path)
        all_dependencies[relative_path] = dependencies
        
        # Update statistics
        file_ref_count = len(dependencies['file_references'])
        component_ref_count = len(dependencies['component_references'])
        command_ref_count = len(dependencies['command_references'])
        context_ref_count = len(dependencies['context_references'])
        count_ref_count = len(dependencies['hardcoded_counts'])
        path_ref_count = len(dependencies['hardcoded_paths'])
        
        dependency_stats['total_file_references'] += file_ref_count
        dependency_stats['total_component_references'] += component_ref_count
        dependency_stats['total_command_references'] += command_ref_count
        dependency_stats['total_context_references'] += context_ref_count
        dependency_stats['total_hardcoded_counts'] += count_ref_count
        dependency_stats['total_hardcoded_paths'] += path_ref_count
        
        total_refs = file_ref_count + component_ref_count + command_ref_count + context_ref_count
        if total_refs > 0:
            dependency_stats['files_with_dependencies'] += 1
            
        if total_refs > 10:  # High dependency threshold
            dependency_stats['high_dependency_files'].append({
                'file': relative_path,
                'total_references': total_refs,
                'breakdown': {
                    'files': file_ref_count,
                    'components': component_ref_count,
                    'commands': command_ref_count,
                    'contexts': context_ref_count
                }
            })
        
        # Track most referenced items
        for ref in dependencies['file_references']:
            dependency_stats['most_referenced_files'][ref] += 1
        for ref in dependencies['component_references']:
            dependency_stats['most_referenced_components'][ref] += 1
        for count in dependencies['hardcoded_counts']:
            dependency_stats['hardcoded_count_distribution'][count] += 1
    
    return all_dependencies, dependency_stats

def detect_circular_dependencies(all_dependencies):
    """Detect circular reference patterns"""
    # Build directed graph
    G = nx.DiGraph()
    
    for source_file, deps in all_dependencies.items():
        for ref in deps['file_references']:
            # Normalize reference to match file paths
            if ref.endswith('.md'):
                G.add_edge(source_file, ref)
    
    # Find cycles
    try:
        cycles = list(nx.simple_cycles(G))
        return cycles
    except:
        return []

def generate_dependency_report(dependency_stats, all_dependencies, circular_deps):
    """Generate comprehensive dependency analysis report"""
    
    print("\n")
    print("=" * 60)
    print("STEP 8: XML DEPENDENCY MAPPING ANALYSIS RESULTS")
    print("=" * 60)
    
    # Overall statistics
    print(f"Total Files Analyzed: {dependency_stats['total_files']}")
    print(f"Files with Dependencies: {dependency_stats['files_with_dependencies']}")
    print(f"Dependency Rate: {(dependency_stats['files_with_dependencies']/dependency_stats['total_files']*100):.1f}%")
    
    print(f"\nTotal Cross-References Found:")
    print(f"  File References: {dependency_stats['total_file_references']}")
    print(f"  Component References: {dependency_stats['total_component_references']}")
    print(f"  Command References: {dependency_stats['total_command_references']}")
    print(f"  Context References: {dependency_stats['total_context_references']}")
    total_refs = (dependency_stats['total_file_references'] + 
                  dependency_stats['total_component_references'] + 
                  dependency_stats['total_command_references'] + 
                  dependency_stats['total_context_references'])
    print(f"  TOTAL REFERENCES: {total_refs}")
    
    print(f"\nMaintenance Burden Indicators:")
    print(f"  Hardcoded Counts: {dependency_stats['total_hardcoded_counts']}")
    print(f"  Hardcoded Paths: {dependency_stats['total_hardcoded_paths']}")
    
    # Average references per file
    avg_refs = total_refs / dependency_stats['total_files']
    print(f"\nAverage References per File: {avg_refs:.1f}")
    
    # High dependency files
    if dependency_stats['high_dependency_files']:
        print(f"\nHigh Dependency Files (>10 references): {len(dependency_stats['high_dependency_files'])}")
        sorted_high_deps = sorted(dependency_stats['high_dependency_files'], 
                                key=lambda x: x['total_references'], reverse=True)
        for file_info in sorted_high_deps[:5]:  # Top 5
            print(f"  {file_info['file']}: {file_info['total_references']} refs")
            print(f"    Files: {file_info['breakdown']['files']}, Components: {file_info['breakdown']['components']}")
    
    # Most referenced items
    print(f"\nMost Referenced Files:")
    for ref, count in dependency_stats['most_referenced_files'].most_common(5):
        print(f"  {ref}: {count} references")
    
    print(f"\nMost Referenced Components:")
    for ref, count in dependency_stats['most_referenced_components'].most_common(5):
        print(f"  {ref}: {count} references")
    
    # Hardcoded count patterns
    print(f"\nHardcoded Count Distribution:")
    for count, frequency in dependency_stats['hardcoded_count_distribution'].most_common(5):
        print(f"  {count}: appears {frequency} times")
    
    # Circular dependencies
    if circular_deps:
        print(f"\nCircular Dependencies Found: {len(circular_deps)}")
        for i, cycle in enumerate(circular_deps[:3]):  # Show first 3
            print(f"  Cycle {i+1}: {' -> '.join(cycle)} -> {cycle[0]}")
    else:
        print(f"\nCircular Dependencies: None detected")
    
    # Risk assessment
    risk_level = "LOW"
    if total_refs > 300:
        risk_level = "CRITICAL"
    elif total_refs > 200:
        risk_level = "HIGH"
    elif total_refs > 100:
        risk_level = "MEDIUM"
    
    print(f"\nDependency Complexity Risk Level: {risk_level}")
    
    # Maintenance cost estimate
    maintenance_hours = (total_refs * 0.1) + (dependency_stats['total_hardcoded_counts'] * 0.05)
    print(f"Estimated Annual Maintenance Hours: {maintenance_hours:.1f}")
    
    print("=" * 60)

def main():
    """Main dependency mapping analysis"""
    # Find XML files
    xml_files = find_xml_files()
    
    if not xml_files:
        print("No XML-tagged files found!")
        return
    
    print(f"Found {len(xml_files)} XML-tagged files for dependency analysis")
    
    # Analyze dependencies
    all_dependencies, dependency_stats = analyze_dependency_complexity(xml_files)
    
    # Detect circular dependencies
    circular_deps = detect_circular_dependencies(all_dependencies)
    
    # Generate report
    generate_dependency_report(dependency_stats, all_dependencies, circular_deps)
    
    # Save detailed results to JSON for further analysis
    results = {
        'dependency_stats': dependency_stats,
        'circular_dependencies': circular_deps,
        'file_count': len(xml_files)
    }
    
    # Convert Counter objects to regular dicts for JSON serialization
    results['dependency_stats']['most_referenced_files'] = dict(dependency_stats['most_referenced_files'])
    results['dependency_stats']['most_referenced_components'] = dict(dependency_stats['most_referenced_components'])
    results['dependency_stats']['hardcoded_count_distribution'] = dict(dependency_stats['hardcoded_count_distribution'])
    
    with open('dependency_analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nDetailed results saved to: dependency_analysis_results.json")

if __name__ == "__main__":
    main()