#!/usr/bin/env python3
"""
Step 17: Cross-Reference Verification - Validate all XML references and dependencies
"""

import re
from pathlib import Path
from collections import defaultdict, Counter
import json

def find_all_files():
    """Find all markdown files in the project"""
    project_root = Path(".")
    all_files = {}
    
    for md_file in project_root.rglob("*.md"):
        try:
            relative_path = str(md_file.relative_to(project_root))
            all_files[relative_path] = md_file
            
            # Also store just the filename for easy lookup
            filename = md_file.name
            if filename not in all_files:
                all_files[filename] = []
            elif not isinstance(all_files[filename], list):
                all_files[filename] = [all_files[filename]]
                
            if isinstance(all_files[filename], list):
                all_files[filename].append(md_file)
            else:
                all_files[filename] = [all_files[filename], md_file]
        except (OSError, ValueError):
            continue
    
    return all_files

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

def categorize_file_type(file_path):
    """Categorize file type based on path"""
    path_str = str(file_path)
    
    if '.claude/commands/core' in path_str:
        return 'Core Command'
    elif '.claude/commands/meta' in path_str:
        return 'Meta Command'
    elif '.claude/commands/quality' in path_str:
        return 'Quality Command'
    elif '.claude/commands/' in path_str:
        return 'Other Command'
    elif '.claude/components/atomic' in path_str:
        return 'Atomic Component'
    elif '.claude/components/security' in path_str:
        return 'Security Component'
    elif '.claude/components/orchestration' in path_str:
        return 'Orchestration Component'
    elif '.claude/components/intelligence' in path_str:
        return 'Intelligence Component'
    elif '.claude/components/' in path_str:
        return 'Other Component'
    elif '.claude/context' in path_str:
        return 'Context File'
    elif 'docs/xml-schema' in path_str:
        return 'XML Schema Doc'
    else:
        return 'Root Documentation'

def extract_cross_references(file_path, all_files):
    """Extract all cross-references from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return {}
    
    references = {
        'file_references': [],
        'component_references': [],
        'command_references': [],
        'xml_refs': [],
        'markdown_links': [],
        'broken_references': [],
        'valid_references': []
    }
    
    # XML-based references
    xml_ref_patterns = [
        (r'<file[^>]*ref="([^"]+)"', 'file_references'),
        (r'<context_file[^>]*ref="([^"]+)"', 'file_references'),
        (r'<component[^>]*ref="([^"]+)"', 'component_references'),
        (r'<command[^>]*ref="([^"]+)"', 'command_references'),
        (r'<file[^>]*>(.*?)</file>', 'xml_refs'),
        (r'<requires>(.*?)</requires>', 'xml_refs'),
        (r'<incompatible>(.*?)</incompatible>', 'xml_refs'),
        (r'ref="([^"]+)"', 'xml_refs'),  # Generic ref attributes
    ]
    
    for pattern, ref_type in xml_ref_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            if ',' in match:  # Handle comma-separated lists
                refs = [r.strip() for r in match.split(',')]
                references[ref_type].extend(refs)
            else:
                references[ref_type].append(match.strip())
    
    # Markdown link references
    markdown_patterns = [
        r'\[([^\]]+)\]\(([^)]+\.md)\)',  # [text](file.md)
        r'\]\(([^)]+\.md)\)',  # Just the file part
    ]
    
    for pattern in markdown_patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            if isinstance(match, tuple):
                ref = match[1] if len(match) > 1 else match[0]
            else:
                ref = match
            if ref.endswith('.md'):
                references['markdown_links'].append(ref)
    
    # Validate references
    all_refs = (references['file_references'] + 
                references['component_references'] + 
                references['command_references'] + 
                references['xml_refs'] + 
                references['markdown_links'])
    
    for ref in all_refs:
        if not ref or ref.isspace():
            continue
            
        ref = ref.strip()
        is_valid = validate_reference(ref, all_files)
        
        if is_valid:
            references['valid_references'].append(ref)
        else:
            references['broken_references'].append(ref)
    
    return references

def validate_reference(ref, all_files):
    """Validate if a reference points to an existing file"""
    if not ref:
        return False
    
    # Clean up the reference
    ref = ref.strip()
    
    # Handle different reference formats
    possible_refs = [
        ref,
        f"{ref}.md",
        ref.replace('.md', '') + '.md',
        f"/.claude/commands/{ref}",
        f"/.claude/commands/{ref}.md",
        f"/.claude/components/{ref}",
        f"/.claude/components/{ref}.md",
    ]
    
    # Check if any variation exists
    for possible_ref in possible_refs:
        # Direct path match
        if possible_ref in all_files:
            return True
        
        # Filename match
        filename = Path(possible_ref).name
        if filename in all_files:
            return True
        
        # Partial path match
        for existing_path in all_files:
            if isinstance(existing_path, str) and possible_ref in existing_path:
                return True
    
    return False

def analyze_cross_references(xml_files, all_files):
    """Analyze cross-references across all XML files"""
    results = {
        'total_files': len(xml_files),
        'file_analysis': [],
        'reference_summary': {
            'total_references': 0,
            'valid_references': 0,
            'broken_references': 0,
            'reference_types': Counter(),
            'most_referenced_files': Counter(),
            'files_with_broken_refs': []
        },
        'dependency_graph': defaultdict(list),
        'circular_dependencies': [],
        'orphaned_files': [],
        'reference_quality': {}
    }
    
    print(f"Analyzing cross-references in {len(xml_files)} files...")
    
    for i, file_path in enumerate(xml_files):
        if i % 10 == 0:
            print(f"  Processing {i+1}/{len(xml_files)}")
        
        relative_path = str(file_path.relative_to(Path(".")))
        file_type = categorize_file_type(file_path)
        
        references = extract_cross_references(file_path, all_files)
        
        # Count references by type
        ref_counts = {}
        total_file_refs = 0
        for ref_type, refs in references.items():
            if ref_type not in ['valid_references', 'broken_references']:
                ref_counts[ref_type] = len(refs)
                total_file_refs += len(refs)
                results['reference_summary']['reference_types'][ref_type] += len(refs)
        
        file_result = {
            'file_path': relative_path,
            'file_type': file_type,
            'total_references': total_file_refs,
            'valid_references': len(references['valid_references']),
            'broken_references': len(references['broken_references']),
            'reference_counts': ref_counts,
            'broken_refs_list': references['broken_references']
        }
        
        results['file_analysis'].append(file_result)
        
        # Update summary statistics
        results['reference_summary']['total_references'] += total_file_refs
        results['reference_summary']['valid_references'] += len(references['valid_references'])
        results['reference_summary']['broken_references'] += len(references['broken_references'])
        
        if references['broken_references']:
            results['reference_summary']['files_with_broken_refs'].append({
                'file': relative_path,
                'broken_count': len(references['broken_references']),
                'broken_refs': references['broken_references']
            })
        
        # Track most referenced files
        for ref in references['valid_references']:
            results['reference_summary']['most_referenced_files'][ref] += 1
        
        # Build dependency graph
        results['dependency_graph'][relative_path] = references['valid_references']
    
    # Detect circular dependencies
    results['circular_dependencies'] = detect_circular_dependencies(results['dependency_graph'])
    
    # Find orphaned files (files not referenced by others)
    referenced_files = set()
    for refs in results['dependency_graph'].values():
        referenced_files.update(refs)
    
    all_analyzed_files = set(r['file_path'] for r in results['file_analysis'])
    results['orphaned_files'] = list(all_analyzed_files - referenced_files)
    
    # Calculate reference quality metrics
    results['reference_quality'] = calculate_reference_quality(results)
    
    return results

def detect_circular_dependencies(dependency_graph):
    """Detect circular dependencies in the reference graph"""
    circular_deps = []
    visited = set()
    rec_stack = set()
    
    def dfs(node, path):
        if node in rec_stack:
            # Found a cycle - find where the cycle starts
            if node in path:
                cycle_start = path.index(node)
                cycle = path[cycle_start:] + [node]
                circular_deps.append(cycle)
            return True
        
        if node in visited:
            return False
        
        visited.add(node)
        rec_stack.add(node)
        current_path = path + [node]
        
        for neighbor in dependency_graph.get(node, []):
            # Try to resolve neighbor to actual file path
            neighbor_resolved = resolve_reference_to_file(neighbor, dependency_graph.keys())
            if neighbor_resolved and dfs(neighbor_resolved, current_path):
                return True
        
        rec_stack.remove(node)
        return False
    
    for node in dependency_graph:
        if node not in visited:
            dfs(node, [])
    
    return circular_deps

def resolve_reference_to_file(ref, all_file_paths):
    """Resolve a reference to an actual file path"""
    for file_path in all_file_paths:
        if ref in file_path or Path(ref).name == Path(file_path).name:
            return file_path
    return ref

def calculate_reference_quality(results):
    """Calculate reference quality metrics"""
    total_refs = results['reference_summary']['total_references']
    valid_refs = results['reference_summary']['valid_references']
    broken_refs = results['reference_summary']['broken_references']
    
    quality = {
        'overall_validity_rate': (valid_refs / total_refs * 100) if total_refs > 0 else 0,
        'broken_reference_rate': (broken_refs / total_refs * 100) if total_refs > 0 else 0,
        'files_with_issues': len(results['reference_summary']['files_with_broken_refs']),
        'issue_rate': (len(results['reference_summary']['files_with_broken_refs']) / 
                      results['total_files'] * 100) if results['total_files'] > 0 else 0,
        'average_refs_per_file': total_refs / results['total_files'] if results['total_files'] > 0 else 0,
        'circular_dependency_count': len(results['circular_dependencies']),
        'orphaned_file_count': len(results['orphaned_files'])
    }
    
    return quality

def generate_cross_reference_report(results):
    """Generate comprehensive cross-reference validation report"""
    print("\n" + "=" * 60)
    print("STEP 17: CROSS-REFERENCE VERIFICATION RESULTS")
    print("=" * 60)
    
    total_files = results['total_files']
    summary = results['reference_summary']
    quality = results['reference_quality']
    
    print(f"Total Files Analyzed: {total_files}")
    print(f"Total References Found: {summary['total_references']:,}")
    print(f"Valid References: {summary['valid_references']:,} ({quality['overall_validity_rate']:.1f}%)")
    print(f"Broken References: {summary['broken_references']:,} ({quality['broken_reference_rate']:.1f}%)")
    print(f"Average References per File: {quality['average_refs_per_file']:.1f}")
    
    # Reference quality assessment
    if quality['overall_validity_rate'] >= 95:
        validity_status = "✅ EXCELLENT"
    elif quality['overall_validity_rate'] >= 85:
        validity_status = "⚠️ GOOD"
    elif quality['overall_validity_rate'] >= 70:
        validity_status = "🚨 POOR"
    else:
        validity_status = "🚨 CRITICAL"
    
    print(f"\nReference Quality: {validity_status}")
    
    # Reference types breakdown
    print(f"\nReference Types Breakdown:")
    for ref_type, count in summary['reference_types'].most_common():
        percentage = (count / summary['total_references'] * 100) if summary['total_references'] > 0 else 0
        print(f"  {ref_type.replace('_', ' ').title()}: {count:,} ({percentage:.1f}%)")
    
    # Files with broken references
    broken_files = summary['files_with_broken_refs']
    if broken_files:
        print(f"\nFiles with Broken References ({len(broken_files)} files):")
        broken_files_sorted = sorted(broken_files, key=lambda x: x['broken_count'], reverse=True)
        for i, file_info in enumerate(broken_files_sorted[:10], 1):
            print(f"  {i:2d}. {file_info['broken_count']:2d} broken refs - {file_info['file']}")
            if i <= 3:  # Show specific broken refs for top 3
                for ref in file_info['broken_refs'][:3]:
                    print(f"      - {ref}")
                if len(file_info['broken_refs']) > 3:
                    print(f"      ... and {len(file_info['broken_refs']) - 3} more")
    
    # Most referenced files
    most_referenced = summary['most_referenced_files'].most_common(10)
    if most_referenced:
        print(f"\nMost Referenced Files:")
        for i, (ref, count) in enumerate(most_referenced, 1):
            print(f"  {i:2d}. {count:2d} references - {ref}")
    
    # Circular dependencies
    circular_deps = results['circular_dependencies']
    if circular_deps:
        print(f"\nCircular Dependencies Found ({len(circular_deps)}):")
        for i, cycle in enumerate(circular_deps[:5], 1):
            cycle_str = " → ".join(cycle)
            print(f"  {i}. {cycle_str}")
    else:
        print(f"\nCircular Dependencies: ✅ None found")
    
    # Orphaned files
    orphaned = results['orphaned_files']
    if orphaned:
        print(f"\nOrphaned Files (Not Referenced by Others) - {len(orphaned)} files:")
        for i, orphan in enumerate(orphaned[:10], 1):
            print(f"  {i:2d}. {orphan}")
    else:
        print(f"\nOrphaned Files: ✅ All files are referenced")
    
    # Category analysis
    print(f"\nReference Quality by Category:")
    category_stats = defaultdict(lambda: {'total': 0, 'valid': 0, 'broken': 0, 'files': 0})
    
    for file_data in results['file_analysis']:
        category = file_data['file_type']
        category_stats[category]['total'] += file_data['total_references']
        category_stats[category]['valid'] += file_data['valid_references']
        category_stats[category]['broken'] += file_data['broken_references']
        category_stats[category]['files'] += 1
    
    for category, stats in sorted(category_stats.items()):
        if stats['total'] > 0:
            validity = (stats['valid'] / stats['total'] * 100)
            status = "✅" if validity >= 95 else "⚠️" if validity >= 85 else "🚨"
            print(f"  {status} {category:<25} {validity:5.1f}% valid ({stats['valid']:3d}/{stats['total']:3d} refs, {stats['files']} files)")
    
    # Critical issues summary
    print(f"\nCritical Issues Summary:")
    if quality['broken_reference_rate'] > 10:
        print(f"  🚨 High broken reference rate: {quality['broken_reference_rate']:.1f}%")
    if quality['issue_rate'] > 20:
        print(f"  🚨 Many files with issues: {quality['issue_rate']:.1f}% of files")
    if quality['circular_dependency_count'] > 0:
        print(f"  🚨 Circular dependencies found: {quality['circular_dependency_count']}")
    if quality['orphaned_file_count'] > total_files * 0.3:
        print(f"  ⚠️ Many orphaned files: {quality['orphaned_file_count']} files")
    
    if (quality['broken_reference_rate'] <= 5 and 
        quality['circular_dependency_count'] == 0 and
        quality['overall_validity_rate'] >= 95):
        print(f"  ✅ Reference integrity is excellent")
    
    # Recommendations
    print(f"\nRecommendations:")
    if quality['broken_reference_rate'] > 5:
        print(f"  1. Fix broken references before XML optimization")
    if quality['circular_dependency_count'] > 0:
        print(f"  2. Resolve circular dependencies to prevent infinite loops")
    if quality['orphaned_file_count'] > 10:
        print(f"  3. Review orphaned files - consider removal or add references")
    if quality['average_refs_per_file'] > 20:
        print(f"  4. High reference density may indicate over-coupling")
    
    print("=" * 60)

def main():
    """Main cross-reference verification analysis"""
    all_files = find_all_files()
    xml_files = find_xml_files()
    
    if not xml_files:
        print("No XML-tagged files found!")
        return
    
    print(f"Found {len(all_files)} total files and {len(xml_files)} XML-tagged files")
    
    results = analyze_cross_references(xml_files, all_files)
    generate_cross_reference_report(results)
    
    # Save detailed results
    with open('cross_reference_validation_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\nDetailed results saved to: cross_reference_validation_results.json")

if __name__ == "__main__":
    main()