#!/usr/bin/env python3
"""Unified module analysis tool - replaces multiple module analysis scripts.

This tool consolidates functionality from:
- analyze-module-dependencies.py
- audit-module-docs.py
- find-compliant-modules.py
- validate-module-interfaces.py
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Add the parent directory to the path so we can import from lib
sys.path.insert(0, str(Path(__file__).parent))

from lib.module_utils import ModuleAnalyzer


def analyze_dependencies(analyzer, output_format='summary'):
    """Analyze and report module dependencies."""
    print("\n🔗 Module Dependency Analysis")
    print("=" * 60)
    
    all_deps = {}
    broken_refs = []
    
    for module in analyzer.modules:
        deps = analyzer.analyze_dependencies(module)
        relative_path = str(module.relative_to(analyzer.base_path))
        all_deps[relative_path] = deps
        
        if deps['broken_refs']:
            broken_refs.append((relative_path, deps['broken_refs']))
    
    # Summary statistics
    total_refs = sum(d['ref_count'] for d in all_deps.values())
    modules_with_deps = sum(1 for d in all_deps.values() if d['ref_count'] > 0)
    
    print(f"Total modules analyzed: {len(analyzer.modules)}")
    print(f"Modules with dependencies: {modules_with_deps}")
    print(f"Total references found: {total_refs}")
    print(f"Modules with broken references: {len(broken_refs)}")
    
    if output_format == 'detailed':
        # Most connected modules
        print("\n📊 Most Connected Modules:")
        sorted_modules = sorted(all_deps.items(), key=lambda x: x[1]['ref_count'], reverse=True)[:10]
        for module, deps in sorted_modules:
            print(f"  {module}: {deps['ref_count']} references")
    
    if broken_refs:
        print("\n❌ Broken References Found:")
        for module, refs in broken_refs:
            print(f"\n  {module}:")
            for ref in refs:
                print(f"    - {ref}")
    
    return all_deps


def audit_documentation(analyzer):
    """Audit module documentation quality."""
    print("\n📚 Module Documentation Audit")
    print("=" * 60)
    
    doc_stats = []
    
    for module in analyzer.modules:
        stats = analyzer.analyze_documentation(module)
        stats['module'] = str(module.relative_to(analyzer.base_path))
        doc_stats.append(stats)
    
    # Calculate averages
    avg_score = sum(s['doc_score'] for s in doc_stats) / len(doc_stats)
    avg_lines = sum(s['line_count'] for s in doc_stats) / len(doc_stats)
    
    print(f"Total modules audited: {len(doc_stats)}")
    print(f"Average documentation score: {avg_score:.1f}/100")
    print(f"Average module size: {avg_lines:.0f} lines")
    
    # Find poorly documented modules
    poor_docs = [s for s in doc_stats if s['doc_score'] < 50]
    if poor_docs:
        print(f"\n⚠️  Poorly Documented Modules ({len(poor_docs)}):")
        for stats in sorted(poor_docs, key=lambda x: x['doc_score'])[:10]:
            print(f"  {stats['module']}: {stats['doc_score']}/100")
    
    # Documentation coverage
    print("\n📊 Documentation Coverage:")
    coverage = defaultdict(int)
    for key in ['has_purpose', 'has_usage', 'has_interface', 'has_dependencies', 
                'has_error_handling', 'has_thinking_pattern']:
        coverage[key] = sum(1 for s in doc_stats if s.get(key, False))
        percentage = (coverage[key] / len(doc_stats)) * 100
        print(f"  {key.replace('has_', '').replace('_', ' ').title()}: {percentage:.1f}%")
    
    return doc_stats


def check_compliance(analyzer):
    """Check modules for framework compliance."""
    print("\n✅ Module Compliance Check")
    print("=" * 60)
    
    compliance_results = []
    non_compliant = []
    
    for module in analyzer.modules:
        result = analyzer.check_compliance(module)
        result['module'] = str(module.relative_to(analyzer.base_path))
        compliance_results.append(result)
        
        if result['compliance_score'] < 100:
            non_compliant.append(result)
    
    # Summary
    avg_compliance = sum(r['compliance_score'] for r in compliance_results) / len(compliance_results)
    fully_compliant = sum(1 for r in compliance_results if r['compliance_score'] == 100)
    
    print(f"Total modules checked: {len(compliance_results)}")
    print(f"Fully compliant modules: {fully_compliant}/{len(compliance_results)}")
    print(f"Average compliance score: {avg_compliance:.1f}/100")
    
    if non_compliant:
        print(f"\n❌ Non-Compliant Modules ({len(non_compliant)}):")
        for result in sorted(non_compliant, key=lambda x: x['compliance_score'])[:15]:
            issues = []
            if not result['has_correct_version_table']:
                issues.append("version table")
            if not result['has_july_2025_date']:
                issues.append("July 2025 date")
            if not result['has_separator_after_header']:
                issues.append("separator")
            if not result['xml_properly_wrapped']:
                issues.append("XML wrapping")
            if not result['no_outdated_timestamps']:
                issues.append("outdated timestamps")
            
            print(f"  {result['module']}: {result['compliance_score']}/100 - Issues: {', '.join(issues)}")
    
    return compliance_results


def validate_interfaces(analyzer):
    """Validate module interfaces."""
    print("\n🔌 Module Interface Validation")
    print("=" * 60)
    
    interface_results = []
    
    for module in analyzer.modules:
        result = analyzer.validate_interfaces(module)
        result['module'] = str(module.relative_to(analyzer.base_path))
        interface_results.append(result)
    
    # Statistics
    avg_score = sum(r['interface_score'] for r in interface_results) / len(interface_results)
    formal_interfaces = sum(1 for r in interface_results if r.get('has_formal_interface', False))
    
    print(f"Total modules analyzed: {len(interface_results)}")
    print(f"Modules with formal interfaces: {formal_interfaces}")
    print(f"Average interface score: {avg_score:.1f}/100")
    
    # Interface coverage
    print("\n📊 Interface Specification Coverage:")
    for key in ['has_input_spec', 'has_output_spec', 'has_error_spec', 
                'has_preconditions', 'has_postconditions']:
        count = sum(1 for r in interface_results if r.get(key, False))
        percentage = (count / len(interface_results)) * 100
        print(f"  {key.replace('has_', '').replace('_', ' ').title()}: {percentage:.1f}%")
    
    # Poor interfaces
    poor_interfaces = [r for r in interface_results if r['interface_score'] < 50]
    if poor_interfaces:
        print(f"\n⚠️  Modules with Poor Interface Definitions ({len(poor_interfaces)}):")
        for result in sorted(poor_interfaces, key=lambda x: x['interface_score'])[:10]:
            print(f"  {result['module']}: {result['interface_score']}/100")
    
    return interface_results


def generate_report(analyzer, report_type='all'):
    """Generate comprehensive module analysis report."""
    results = {}
    
    if report_type in ['all', 'dependencies']:
        results['dependencies'] = analyze_dependencies(analyzer, 'detailed')
    
    if report_type in ['all', 'documentation']:
        results['documentation'] = audit_documentation(analyzer)
    
    if report_type in ['all', 'compliance']:
        results['compliance'] = check_compliance(analyzer)
    
    if report_type in ['all', 'interfaces']:
        results['interfaces'] = validate_interfaces(analyzer)
    
    if report_type == 'all':
        # Generate dependency graph
        print("\n🗺️  Generating Dependency Graph...")
        results['dependency_graph'] = analyzer.generate_dependency_graph()
        print(f"Graph generated with {len(results['dependency_graph'])} nodes")
    
    return results


def main():
    """Main entry point for the unified module analyzer."""
    parser = argparse.ArgumentParser(
        description="Unified module analysis tool for framework modules"
    )
    parser.add_argument(
        '--analysis',
        choices=['all', 'dependencies', 'documentation', 'compliance', 'interfaces'],
        default='all',
        help='Type of analysis to perform'
    )
    parser.add_argument(
        '--base-path',
        default='.claude',
        help='Base path for module search'
    )
    parser.add_argument(
        '--output',
        help='Output file for results (JSON format)'
    )
    parser.add_argument(
        '--patterns',
        nargs='+',
        help='Custom glob patterns for finding modules'
    )
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = ModuleAnalyzer(args.base_path)
    
    # Find modules
    print(f"🔍 Searching for modules in {args.base_path}...")
    modules = analyzer.find_modules(args.patterns)
    print(f"Found {len(modules)} modules")
    
    if not modules:
        print("No modules found!")
        sys.exit(1)
    
    # Perform analysis
    results = generate_report(analyzer, args.analysis)
    
    # Save results if requested
    if args.output:
        # Convert Path objects to strings for JSON serialization
        def convert_paths(obj):
            if isinstance(obj, Path):
                return str(obj)
            elif isinstance(obj, dict):
                return {k: convert_paths(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_paths(item) for item in obj]
            return obj
        
        with open(args.output, 'w') as f:
            json.dump(convert_paths(results), f, indent=2)
        print(f"\n📊 Detailed results saved to {args.output}")
    
    # Determine exit code based on issues found
    exit_code = 0
    if 'dependencies' in results:
        broken_count = sum(1 for d in results['dependencies'].values() if d['broken_refs'])
        if broken_count > 0:
            exit_code = 1
    
    if 'compliance' in results:
        non_compliant = sum(1 for r in results['compliance'] if r['compliance_score'] < 100)
        if non_compliant > 10:  # Allow some non-compliance
            exit_code = 1
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()