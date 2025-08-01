#!/usr/bin/env python3
"""
Step 13: XML Tag Frequency Analysis - Count usage of each XML tag type
"""

import re
from pathlib import Path
from collections import Counter, defaultdict
import json

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

def extract_xml_content(file_path):
    """Extract XML content from markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return ""
    
    # Find XML blocks
    xml_blocks = []
    
    # Look for XML metadata blocks
    xml_sections = re.findall(r'<!-- AI_METADATA_START -->(.*?)<!-- AI_METADATA_END -->', content, re.DOTALL)
    xml_blocks.extend(xml_sections)
    
    # Find individual XML elements
    xml_patterns = [
        r'<ai_document_metadata>.*?</ai_document_metadata>',
        r'<command_metadata>.*?</command_metadata>',
        r'<component_metadata>.*?</component_metadata>',
        r'<ai_navigation>.*?</ai_navigation>',
        r'<context_engineering>.*?</context_engineering>',
        r'<context[^>]*>.*?</context>',
        r'<instructions>.*?</instructions>',
        r'<examples>.*?</examples>',
        r'<params>.*?</params>',
        r'<arguments>.*?</arguments>'
    ]
    
    for pattern in xml_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        xml_blocks.extend(matches)
    
    return '\n'.join(xml_blocks)

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

def analyze_xml_tags(xml_files):
    """Analyze XML tag frequency across all files"""
    results = {
        'total_files': len(xml_files),
        'tag_frequency': Counter(),
        'tag_by_category': defaultdict(lambda: Counter()),
        'file_tag_counts': {},
        'unique_tags_per_file': {},
        'tag_file_spread': defaultdict(set),
        'container_tags': Counter(),
        'leaf_tags': Counter(),
        'attribute_frequency': Counter()
    }
    
    print(f"Analyzing XML tag frequency in {len(xml_files)} files...")
    
    for i, file_path in enumerate(xml_files):
        if i % 10 == 0:
            print(f"  Processing {i+1}/{len(xml_files)}")
        
        relative_path = str(file_path.relative_to(Path(".")))
        file_type = categorize_file_type(file_path)
        
        xml_content = extract_xml_content(file_path)
        if not xml_content:
            continue
        
        # Extract all XML tags (opening tags only)
        opening_tags = re.findall(r'<([a-zA-Z_][a-zA-Z0-9_-]*)[^/>]*(?<!/)>', xml_content)
        self_closing_tags = re.findall(r'<([a-zA-Z_][a-zA-Z0-9_-]*)[^>]*/>', xml_content)
        
        all_tags = opening_tags + self_closing_tags
        
        # Count tags
        file_tag_counter = Counter(all_tags)
        results['file_tag_counts'][relative_path] = dict(file_tag_counter)
        results['unique_tags_per_file'][relative_path] = len(file_tag_counter)
        
        # Update overall frequencies
        for tag, count in file_tag_counter.items():
            results['tag_frequency'][tag] += count
            results['tag_by_category'][file_type][tag] += count
            results['tag_file_spread'][tag].add(relative_path)
        
        # Identify container vs leaf tags
        for tag in set(all_tags):
            # Check if tag typically contains other tags (simplified heuristic)
            tag_content = re.findall(f'<{tag}[^>]*>(.*?)</{tag}>', xml_content, re.DOTALL)
            if tag_content:
                content = tag_content[0]
                if re.search(r'<[a-zA-Z_]', content):  # Contains other tags
                    results['container_tags'][tag] += 1
                else:
                    results['leaf_tags'][tag] += 1
        
        # Extract attributes
        attributes = re.findall(r'<[a-zA-Z_][a-zA-Z0-9_-]*[^>]*\s+([a-zA-Z_][a-zA-Z0-9_-]*)=', xml_content)
        for attr in attributes:
            results['attribute_frequency'][attr] += 1
    
    # Convert sets to lists for JSON serialization
    for tag in results['tag_file_spread']:
        results['tag_file_spread'][tag] = list(results['tag_file_spread'][tag])
    
    return results

def generate_frequency_report(results):
    """Generate comprehensive tag frequency analysis report"""
    print("\n" + "=" * 60)
    print("STEP 13: XML TAG FREQUENCY ANALYSIS RESULTS")
    print("=" * 60)
    
    total_files = results['total_files']
    total_tags = sum(results['tag_frequency'].values())
    unique_tags = len(results['tag_frequency'])
    
    print(f"Total Files Analyzed: {total_files}")
    print(f"Total XML Tags Found: {total_tags:,}")
    print(f"Unique Tag Types: {unique_tags}")
    print(f"Average Tags per File: {total_tags/total_files:.1f}")
    
    # Most frequent tags
    print(f"\nTop 20 Most Frequent XML Tags:")
    for i, (tag, count) in enumerate(results['tag_frequency'].most_common(20), 1):
        files_using = len(results['tag_file_spread'][tag])
        percentage = (count / total_tags) * 100
        file_spread = (files_using / total_files) * 100
        print(f"  {i:2d}. {tag:<30} {count:4d} uses ({percentage:4.1f}%) in {files_using:2d} files ({file_spread:4.1f}%)")
    
    # Tags with widest file spread (high maintenance burden)
    print(f"\nTags with Widest File Spread (High Maintenance Risk):")
    spread_ranking = sorted(results['tag_file_spread'].items(), 
                           key=lambda x: len(x[1]), reverse=True)
    for i, (tag, files) in enumerate(spread_ranking[:15], 1):
        file_count = len(files)
        usage_count = results['tag_frequency'][tag]
        percentage = (file_count / total_files) * 100
        print(f"  {i:2d}. {tag:<30} in {file_count:2d} files ({percentage:4.1f}%) - {usage_count:4d} total uses")
    
    # Rare tags (candidates for elimination)
    print(f"\nRare Tags (Potential Elimination Candidates):")
    rare_tags = [(tag, count) for tag, count in results['tag_frequency'].items() if count <= 5]
    rare_tags.sort(key=lambda x: x[1])
    for tag, count in rare_tags[:15]:
        files_using = len(results['tag_file_spread'][tag])
        print(f"  {tag:<30} {count:2d} uses in {files_using:2d} files")
    
    # Category analysis
    print(f"\nTag Usage by File Category:")
    for category, tag_counter in results['tag_by_category'].items():
        total_category_tags = sum(tag_counter.values())
        unique_category_tags = len(tag_counter)
        print(f"  {category:<25} {total_category_tags:4d} tags, {unique_category_tags:3d} unique")
    
    # Container vs leaf analysis
    print(f"\nContainer vs Leaf Tag Analysis:")
    container_count = sum(results['container_tags'].values())
    leaf_count = sum(results['leaf_tags'].values())
    print(f"  Container Tags: {len(results['container_tags'])} types, {container_count} instances")
    print(f"  Leaf Tags: {len(results['leaf_tags'])} types, {leaf_count} instances")
    
    # Most common attributes
    print(f"\nMost Common XML Attributes:")
    for i, (attr, count) in enumerate(results['attribute_frequency'].most_common(10), 1):
        print(f"  {i:2d}. {attr:<20} {count:4d} uses")
    
    # Complexity indicators
    avg_unique_tags = sum(results['unique_tags_per_file'].values()) / len(results['unique_tags_per_file'])
    print(f"\nComplexity Indicators:")
    print(f"  Average Unique Tags per File: {avg_unique_tags:.1f}")
    print(f"  Tag Diversity (unique/total): {unique_tags/total_tags:.3f}")
    
    # High-maintenance tags (appear in many files with high frequency)
    maintenance_burden = []
    for tag, count in results['tag_frequency'].items():
        file_spread = len(results['tag_file_spread'][tag])
        maintenance_score = count * file_spread  # High usage × wide spread = high maintenance
        maintenance_burden.append((tag, count, file_spread, maintenance_score))
    
    maintenance_burden.sort(key=lambda x: x[3], reverse=True)
    
    print(f"\nHighest Maintenance Burden Tags:")
    for i, (tag, count, file_spread, score) in enumerate(maintenance_burden[:10], 1):
        print(f"  {i:2d}. {tag:<30} Score: {score:5d} ({count:3d} uses × {file_spread:2d} files)")
    
    # Recommendations
    print(f"\nRecommendations:")
    
    # High-frequency, low-spread tags (good candidates to keep)
    efficient_tags = [(tag, count, len(results['tag_file_spread'][tag])) 
                     for tag, count in results['tag_frequency'].most_common(20)
                     if len(results['tag_file_spread'][tag]) <= 10]
    
    if efficient_tags:
        print(f"  Keep (High value, low maintenance): {len(efficient_tags)} tags")
    
    # Low-frequency tags (elimination candidates)
    elimination_candidates = len([tag for tag, count in results['tag_frequency'].items() if count <= 3])
    print(f"  Consider eliminating: {elimination_candidates} rare tags (≤3 uses)")
    
    # High maintenance tags (consolidation candidates)
    high_maintenance = len([tag for tag, files in results['tag_file_spread'].items() 
                           if len(files) > total_files * 0.5])
    print(f"  High maintenance burden: {high_maintenance} tags in >50% of files")
    
    print("=" * 60)

def main():
    """Main tag frequency analysis"""
    xml_files = find_xml_files()
    
    if not xml_files:
        print("No XML-tagged files found!")
        return
    
    results = analyze_xml_tags(xml_files)
    generate_frequency_report(results)
    
    # Save detailed results
    with open('xml_tag_frequency_results.json', 'w') as f:
        # Convert Counters to regular dicts for JSON serialization
        json_results = {
            'total_files': results['total_files'],
            'tag_frequency': dict(results['tag_frequency']),
            'file_tag_counts': results['file_tag_counts'],
            'unique_tags_per_file': results['unique_tags_per_file'],
            'tag_file_spread': results['tag_file_spread'],
            'container_tags': dict(results['container_tags']),
            'leaf_tags': dict(results['leaf_tags']),
            'attribute_frequency': dict(results['attribute_frequency']),
            'tag_by_category': {k: dict(v) for k, v in results['tag_by_category'].items()}
        }
        json.dump(json_results, f, indent=2)
    
    print(f"\nDetailed results saved to: xml_tag_frequency_results.json")

if __name__ == "__main__":
    main()