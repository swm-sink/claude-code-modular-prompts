#!/usr/bin/env python3
"""
Step 14: Content-to-Metadata Ratio Analysis - Calculate actual content vs. XML overhead
"""

import re
from pathlib import Path
from collections import defaultdict
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

def separate_content_and_metadata(file_path):
    """Separate actual markdown content from XML metadata"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None, None, None
    
    # Count total lines
    total_lines = len(content.split('\n'))
    total_chars = len(content)
    
    # Remove YAML frontmatter (not XML metadata)
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    yaml_content = ""
    if yaml_match:
        yaml_content = yaml_match.group(0)
        content = content[len(yaml_content):]
    
    # Extract XML metadata blocks
    xml_content = ""
    remaining_content = content
    
    # XML metadata patterns to extract
    xml_patterns = [
        (r'<!-- AI_METADATA_START -->.*?<!-- AI_METADATA_END -->', re.DOTALL),
        (r'<ai_document_metadata>.*?</ai_document_metadata>', re.DOTALL),
        (r'<command_metadata>.*?</command_metadata>', re.DOTALL),
        (r'<component_metadata>.*?</component_metadata>', re.DOTALL),
        (r'<ai_navigation>.*?</ai_navigation>', re.DOTALL),
        (r'<context_engineering>.*?</context_engineering>', re.DOTALL),
        (r'<context[^>]*>.*?</context>', re.DOTALL),
        (r'<instructions>.*?</instructions>', re.DOTALL),
        (r'<examples>.*?</examples>', re.DOTALL),
        (r'<params>.*?</params>', re.DOTALL),
        (r'<arguments>.*?</arguments>', re.DOTALL),
        (r'<automation[^>]*>.*?</automation>', re.DOTALL),
        (r'<memory[^>]*>.*?</memory>', re.DOTALL),
        (r'<integration[^>]*>.*?</integration>', re.DOTALL),
        (r'<configuration[^>]*>.*?</configuration>', re.DOTALL)
    ]
    
    for pattern, flags in xml_patterns:
        matches = re.findall(pattern, remaining_content, flags)
        for match in matches:
            xml_content += match + "\n"
            remaining_content = remaining_content.replace(match, "")
    
    # Clean up remaining content (actual markdown content)
    remaining_content = re.sub(r'\n\n+', '\n\n', remaining_content)  # Multiple newlines
    remaining_content = remaining_content.strip()
    
    # Calculate statistics
    yaml_lines = len(yaml_content.split('\n')) if yaml_content else 0
    xml_lines = len(xml_content.split('\n')) if xml_content else 0
    content_lines = len(remaining_content.split('\n')) if remaining_content else 0
    
    yaml_chars = len(yaml_content)
    xml_chars = len(xml_content)
    content_chars = len(remaining_content)
    
    return {
        'total_lines': total_lines,
        'total_chars': total_chars,
        'yaml_lines': yaml_lines,
        'yaml_chars': yaml_chars,
        'xml_lines': xml_lines,
        'xml_chars': xml_chars,
        'content_lines': content_lines,
        'content_chars': content_chars,
        'yaml_content': yaml_content,
        'xml_content': xml_content,
        'markdown_content': remaining_content
    }

def analyze_content_ratios(xml_files):
    """Analyze content-to-metadata ratios across all files"""
    results = {
        'total_files': len(xml_files),
        'file_analysis': [],
        'category_stats': defaultdict(list),
        'overall_stats': {
            'total_lines': 0,
            'total_chars': 0,
            'total_yaml_lines': 0,
            'total_xml_lines': 0,
            'total_content_lines': 0,
            'worst_xml_overhead': [],
            'best_content_ratio': [],
            'content_inversion_files': []  # Files with >80% metadata
        }
    }
    
    print(f"Analyzing content-to-metadata ratios in {len(xml_files)} files...")
    
    for i, file_path in enumerate(xml_files):
        if i % 10 == 0:
            print(f"  Processing {i+1}/{len(xml_files)}")
        
        relative_path = str(file_path.relative_to(Path(".")))
        file_type = categorize_file_type(file_path)
        
        analysis = separate_content_and_metadata(file_path)
        if not analysis:
            continue
        
        # Calculate ratios
        total_lines = analysis['total_lines']
        yaml_ratio = (analysis['yaml_lines'] / total_lines) * 100 if total_lines > 0 else 0
        xml_ratio = (analysis['xml_lines'] / total_lines) * 100 if total_lines > 0 else 0
        content_ratio = (analysis['content_lines'] / total_lines) * 100 if total_lines > 0 else 0
        metadata_ratio = yaml_ratio + xml_ratio
        
        # Character-based ratios
        total_chars = analysis['total_chars']
        yaml_char_ratio = (analysis['yaml_chars'] / total_chars) * 100 if total_chars > 0 else 0
        xml_char_ratio = (analysis['xml_chars'] / total_chars) * 100 if total_chars > 0 else 0
        content_char_ratio = (analysis['content_chars'] / total_chars) * 100 if total_chars > 0 else 0
        
        file_result = {
            'file_path': relative_path,
            'file_type': file_type,
            'total_lines': total_lines,
            'yaml_lines': analysis['yaml_lines'],
            'xml_lines': analysis['xml_lines'],
            'content_lines': analysis['content_lines'],
            'yaml_ratio': yaml_ratio,
            'xml_ratio': xml_ratio,
            'content_ratio': content_ratio,
            'metadata_ratio': metadata_ratio,
            'total_chars': total_chars,
            'yaml_chars': analysis['yaml_chars'],
            'xml_chars': analysis['xml_chars'],
            'content_chars': analysis['content_chars'],
            'yaml_char_ratio': yaml_char_ratio,
            'xml_char_ratio': xml_char_ratio,
            'content_char_ratio': content_char_ratio
        }
        
        results['file_analysis'].append(file_result)
        results['category_stats'][file_type].append(file_result)
        
        # Update overall stats
        results['overall_stats']['total_lines'] += total_lines
        results['overall_stats']['total_chars'] += total_chars
        results['overall_stats']['total_yaml_lines'] += analysis['yaml_lines']
        results['overall_stats']['total_xml_lines'] += analysis['xml_lines']
        results['overall_stats']['total_content_lines'] += analysis['content_lines']
        
        # Track extreme cases
        if xml_ratio >= 80:  # Extreme XML overhead
            results['overall_stats']['worst_xml_overhead'].append({
                'file': relative_path,
                'xml_ratio': xml_ratio,
                'content_ratio': content_ratio,
                'type': file_type
            })
        
        if content_ratio >= 60:  # Good content ratio
            results['overall_stats']['best_content_ratio'].append({
                'file': relative_path,
                'content_ratio': content_ratio,
                'xml_ratio': xml_ratio,
                'type': file_type
            })
        
        if metadata_ratio >= 80:  # Content inversion (metadata dominates)
            results['overall_stats']['content_inversion_files'].append({
                'file': relative_path,
                'metadata_ratio': metadata_ratio,
                'content_ratio': content_ratio,
                'type': file_type
            })
    
    return results

def generate_ratio_report(results):
    """Generate comprehensive content-to-metadata ratio report"""
    print("\n" + "=" * 60)
    print("STEP 14: CONTENT-TO-METADATA RATIO ANALYSIS RESULTS")
    print("=" * 60)
    
    total_files = results['total_files']
    overall = results['overall_stats']
    
    # Overall statistics
    total_lines = overall['total_lines']
    total_yaml = overall['total_yaml_lines']
    total_xml = overall['total_xml_lines']
    total_content = overall['total_content_lines']
    
    yaml_ratio = (total_yaml / total_lines) * 100 if total_lines > 0 else 0
    xml_ratio = (total_xml / total_lines) * 100 if total_lines > 0 else 0
    content_ratio = (total_content / total_lines) * 100 if total_lines > 0 else 0
    metadata_ratio = yaml_ratio + xml_ratio
    
    print(f"Total Files Analyzed: {total_files}")
    print(f"Total Lines: {total_lines:,}")
    print(f"YAML Frontmatter: {total_yaml:,} lines ({yaml_ratio:.1f}%)")
    print(f"XML Metadata: {total_xml:,} lines ({xml_ratio:.1f}%)")
    print(f"Actual Content: {total_content:,} lines ({content_ratio:.1f}%)")
    print(f"Total Metadata: {total_yaml + total_xml:,} lines ({metadata_ratio:.1f}%)")
    
    # Ratio assessment
    if content_ratio >= 60:
        assessment = "GOOD"
    elif content_ratio >= 40:
        assessment = "ACCEPTABLE"  
    elif content_ratio >= 20:
        assessment = "POOR"
    else:
        assessment = "CRITICAL"
    
    print(f"\nContent-to-Metadata Balance: {assessment}")
    
    # Category analysis
    print(f"\nContent Ratio by File Category:")
    category_averages = []
    for category, files in results['category_stats'].items():
        if files:
            avg_content = sum(f['content_ratio'] for f in files) / len(files)
            avg_xml = sum(f['xml_ratio'] for f in files) / len(files)
            avg_yaml = sum(f['yaml_ratio'] for f in files) / len(files)
            category_averages.append((category, avg_content, avg_xml, avg_yaml, len(files)))
    
    category_averages.sort(key=lambda x: x[1], reverse=True)  # Sort by content ratio
    
    for category, avg_content, avg_xml, avg_yaml, count in category_averages:
        status = "✅" if avg_content >= 50 else "⚠️" if avg_content >= 30 else "🚨"
        print(f"  {status} {category:<25} Content: {avg_content:5.1f}%, XML: {avg_xml:5.1f}%, YAML: {avg_yaml:4.1f}% ({count} files)")
    
    # Worst XML overhead files
    worst_xml = results['overall_stats']['worst_xml_overhead']
    if worst_xml:
        print(f"\nWorst XML Overhead Files (≥80% XML):")
        worst_xml.sort(key=lambda x: x['xml_ratio'], reverse=True)
        for i, file_info in enumerate(worst_xml[:10], 1):
            print(f"  {i:2d}. {file_info['xml_ratio']:5.1f}% XML: {file_info['file']} ({file_info['type']})")
    
    # Content inversion files
    inversion_files = results['overall_stats']['content_inversion_files']
    if inversion_files:
        print(f"\nContent Inversion Files (≥80% Metadata):")
        inversion_files.sort(key=lambda x: x['metadata_ratio'], reverse=True)
        for i, file_info in enumerate(inversion_files[:10], 1):
            print(f"  {i:2d}. {file_info['metadata_ratio']:5.1f}% Metadata: {file_info['file']} ({file_info['type']})")
    
    # Best content ratio files
    best_content = results['overall_stats']['best_content_ratio']
    if best_content:
        print(f"\nBest Content Ratio Files (≥60% Content):")
        best_content.sort(key=lambda x: x['content_ratio'], reverse=True)
        for i, file_info in enumerate(best_content[:5], 1):
            print(f"  {i:2d}. {file_info['content_ratio']:5.1f}% Content: {file_info['file']} ({file_info['type']})")
    
    # Improvement targets
    print(f"\nImprovement Analysis:")
    target_content_ratio = 70  # Target content ratio
    current_avg_content = content_ratio
    improvement_needed = target_content_ratio - current_avg_content
    
    print(f"Current Average Content Ratio: {current_avg_content:.1f}%")
    print(f"Target Content Ratio: {target_content_ratio}%")
    print(f"Improvement Needed: +{improvement_needed:.1f} percentage points")
    
    # Files requiring attention
    files_needing_improvement = len([f for f in results['file_analysis'] if f['content_ratio'] < 50])
    percentage_needing_improvement = (files_needing_improvement / total_files) * 100
    
    print(f"Files with <50% Content: {files_needing_improvement}/{total_files} ({percentage_needing_improvement:.1f}%)")
    
    if percentage_needing_improvement > 60:
        print("RECOMMENDATION: System-wide content-metadata rebalancing required")
    elif percentage_needing_improvement > 30:
        print("RECOMMENDATION: Targeted content improvement needed")
    else:
        print("RECOMMENDATION: Minor adjustments sufficient")
    
    # Potential savings
    if xml_ratio > 20:  # Current XML overhead too high
        target_xml_ratio = 15  # Target max XML overhead
        xml_reduction_potential = xml_ratio - target_xml_ratio
        lines_savings = (xml_reduction_potential / 100) * total_lines
        print(f"\nPotential Savings from XML Reduction:")
        print(f"Target XML Ratio: {target_xml_ratio}%")
        print(f"Potential Line Savings: {lines_savings:,.0f} lines ({xml_reduction_potential:.1f} percentage points)")
    
    print("=" * 60)

def main():
    """Main content-to-metadata ratio analysis"""
    xml_files = find_xml_files()
    
    if not xml_files:
        print("No XML-tagged files found!")
        return
    
    results = analyze_content_ratios(xml_files)
    generate_ratio_report(results)
    
    # Save detailed results
    with open('content_metadata_ratio_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nDetailed results saved to: content_metadata_ratio_results.json")

if __name__ == "__main__":
    main()