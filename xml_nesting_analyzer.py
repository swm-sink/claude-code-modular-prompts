#!/usr/bin/env python3
"""
Step 12: XML Nesting Depth Analysis - Document maximum and average XML nesting levels
"""

import re
from pathlib import Path
import xml.etree.ElementTree as ET
from collections import defaultdict, Counter

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

def extract_xml_blocks(file_path):
    """Extract XML blocks from markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return []
    
    xml_blocks = []
    
    # Find XML metadata blocks between comments
    xml_sections = re.findall(r'<!-- AI_METADATA_START -->(.*?)<!-- AI_METADATA_END -->', content, re.DOTALL)
    xml_blocks.extend(xml_sections)
    
    # Find standalone XML blocks
    xml_patterns = [
        r'<ai_document_metadata>.*?</ai_document_metadata>',
        r'<command_metadata>.*?</command_metadata>',
        r'<component_metadata>.*?</component_metadata>', 
        r'<ai_navigation>.*?</ai_navigation>',
        r'<context_engineering>.*?</context_engineering>'
    ]
    
    for pattern in xml_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        xml_blocks.extend(matches)
    
    return xml_blocks

def analyze_nesting_depth_manual(xml_content):
    """Analyze XML nesting depth using manual parsing (more reliable for mixed content)"""
    lines = xml_content.split('\n')
    max_depth = 0
    current_depth = 0
    depth_distribution = Counter()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Count opening tags
        opening_tags = re.findall(r'<([a-zA-Z_][a-zA-Z0-9_-]*)[^/>]*(?<!/)>', line)
        # Count closing tags
        closing_tags = re.findall(r'</([a-zA-Z_][a-zA-Z0-9_-]*)>', line)
        # Count self-closing tags
        self_closing = re.findall(r'<([a-zA-Z_][a-zA-Z0-9_-]*)[^>]*/>', line)
        
        # Adjust depth
        current_depth += len(opening_tags)
        if current_depth > max_depth:
            max_depth = current_depth
        
        depth_distribution[current_depth] += 1
        current_depth -= len(closing_tags)
        
        # Self-closing tags don't affect depth
        
    return max_depth, dict(depth_distribution)

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

def analyze_all_files():
    """Analyze nesting depth across all XML-tagged files"""
    xml_files = find_xml_files()
    
    results = {
        'total_files': len(xml_files),
        'file_analysis': [],
        'category_stats': defaultdict(list),
        'overall_stats': {
            'max_depth_found': 0,
            'total_depths': [],
            'problematic_files': []
        }
    }
    
    print(f"Analyzing XML nesting depth in {len(xml_files)} files...")
    
    for i, file_path in enumerate(xml_files):
        if i % 10 == 0:
            print(f"  Processing {i+1}/{len(xml_files)}")
        
        relative_path = str(file_path.relative_to(Path(".")))
        file_type = categorize_file_type(file_path)
        
        xml_blocks = extract_xml_blocks(file_path)
        if not xml_blocks:
            continue
        
        file_max_depth = 0
        file_depth_distribution = Counter()
        
        for block in xml_blocks:
            max_depth, depth_dist = analyze_nesting_depth_manual(block)
            file_max_depth = max(file_max_depth, max_depth)
            
            for depth, count in depth_dist.items():
                file_depth_distribution[depth] += count
        
        file_analysis = {
            'file_path': relative_path,
            'file_type': file_type,
            'max_depth': file_max_depth,
            'depth_distribution': dict(file_depth_distribution),
            'xml_blocks_count': len(xml_blocks)
        }
        
        results['file_analysis'].append(file_analysis)
        results['category_stats'][file_type].append(file_max_depth)
        results['overall_stats']['total_depths'].append(file_max_depth)
        
        if file_max_depth > results['overall_stats']['max_depth_found']:
            results['overall_stats']['max_depth_found'] = file_max_depth
        
        if file_max_depth >= 5:  # Problematic depth threshold
            results['overall_stats']['problematic_files'].append({
                'file': relative_path,
                'depth': file_max_depth,
                'type': file_type
            })
    
    return results

def generate_report(results):
    """Generate comprehensive nesting depth analysis report"""
    print("\n" + "=" * 60)
    print("STEP 12: XML NESTING DEPTH ANALYSIS RESULTS")
    print("=" * 60)
    
    # Overall statistics
    total_files = results['total_files']
    max_depth = results['overall_stats']['max_depth_found']
    all_depths = results['overall_stats']['total_depths']
    avg_depth = sum(all_depths) / len(all_depths) if all_depths else 0
    
    print(f"Total Files Analyzed: {total_files}")
    print(f"Maximum Nesting Depth Found: {max_depth}")
    print(f"Average Maximum Depth per File: {avg_depth:.1f}")
    
    # Depth distribution
    depth_counter = Counter(all_depths)
    print(f"\nDepth Distribution:")
    for depth in sorted(depth_counter.keys()):
        count = depth_counter[depth]
        percentage = (count / total_files) * 100
        print(f"  {depth} levels: {count} files ({percentage:.1f}%)")
    
    # Category analysis
    print(f"\nNesting Depth by File Category:")
    for category, depths in results['category_stats'].items():
        if depths:
            avg_cat_depth = sum(depths) / len(depths)
            max_cat_depth = max(depths)
            print(f"  {category}: avg {avg_cat_depth:.1f}, max {max_cat_depth} ({len(depths)} files)")
    
    # Problematic files
    problematic = results['overall_stats']['problematic_files']
    if problematic:
        print(f"\nProblematic Files (≥5 levels deep): {len(problematic)}")
        sorted_problematic = sorted(problematic, key=lambda x: x['depth'], reverse=True)
        for file_info in sorted_problematic[:10]:  # Top 10 worst
            print(f"  {file_info['depth']} levels: {file_info['file']} ({file_info['type']})")
    
    # Recommendations
    print(f"\nNesting Complexity Assessment:")
    if max_depth <= 3:
        rating = "EXCELLENT"
    elif max_depth <= 4:
        rating = "GOOD"
    elif max_depth <= 5:
        rating = "ACCEPTABLE"
    elif max_depth <= 6:
        rating = "POOR"
    else:
        rating = "CRITICAL"
    
    print(f"Overall Nesting Complexity: {rating}")
    
    # Improvement targets
    excessive_nesting = len([d for d in all_depths if d > 3])
    percentage_excessive = (excessive_nesting / total_files) * 100
    
    print(f"\nImprovement Targets:")
    print(f"Files with Excessive Nesting (>3 levels): {excessive_nesting}/{total_files} ({percentage_excessive:.1f}%)")
    print(f"Target Nesting Levels: Maximum 3 levels")
    print(f"Files Requiring Flattening: {excessive_nesting}")
    
    if percentage_excessive > 50:
        print("RECOMMENDATION: Systematic nesting reduction required")
    elif percentage_excessive > 25:
        print("RECOMMENDATION: Targeted nesting reduction recommended")
    else:
        print("RECOMMENDATION: Minor nesting cleanup sufficient")
    
    print("=" * 60)

def main():
    """Main nesting depth analysis"""
    results = analyze_all_files()
    generate_report(results)
    
    # Save detailed results
    import json
    with open('xml_nesting_analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nDetailed results saved to: xml_nesting_analysis_results.json")

if __name__ == "__main__":
    main()