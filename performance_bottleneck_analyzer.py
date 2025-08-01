#!/usr/bin/env python3
"""
Step 16: Performance Bottleneck Identification - Find heaviest XML processing points
"""

import time
import psutil
import os
import re
from pathlib import Path
from collections import defaultdict, Counter
import json
import xml.etree.ElementTree as ET
from xml.parsers.expat import ExpatError
import statistics

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

def measure_file_metrics(file_path):
    """Measure comprehensive file metrics"""
    try:
        # File size
        file_size = os.path.getsize(file_path)
        
        # Read time
        start_time = time.perf_counter()
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        read_time = time.perf_counter() - start_time
        
        # Basic metrics
        total_lines = len(content.split('\n'))
        total_chars = len(content)
        
        # XML extraction time
        start_time = time.perf_counter()
        xml_content = extract_xml_content(content)
        xml_extraction_time = time.perf_counter() - start_time
        
        # XML parsing time (if valid)
        xml_parse_time = 0
        xml_parse_success = False
        if xml_content:
            try:
                start_time = time.perf_counter()
                # Wrap in root element for parsing
                wrapped_xml = f"<root>{xml_content}</root>"
                ET.fromstring(wrapped_xml)
                xml_parse_time = time.perf_counter() - start_time
                xml_parse_success = True
            except (ET.ParseError, ExpatError):
                xml_parse_time = 0
                xml_parse_success = False
        
        # XML complexity metrics
        xml_lines = len(xml_content.split('\n')) if xml_content else 0
        xml_chars = len(xml_content) if xml_content else 0
        xml_elements = len(re.findall(r'<[a-zA-Z_][^/>]*>', xml_content)) if xml_content else 0
        xml_nesting_depth = calculate_max_nesting_depth(xml_content) if xml_content else 0
        
        return {
            'file_size': file_size,
            'read_time': read_time,
            'total_lines': total_lines,
            'total_chars': total_chars,
            'xml_extraction_time': xml_extraction_time,
            'xml_parse_time': xml_parse_time,
            'xml_parse_success': xml_parse_success,
            'xml_lines': xml_lines,
            'xml_chars': xml_chars,
            'xml_elements': xml_elements,
            'xml_nesting_depth': xml_nesting_depth,
            'xml_ratio': (xml_chars / total_chars * 100) if total_chars > 0 else 0,
            'total_processing_time': read_time + xml_extraction_time + xml_parse_time
        }
    except Exception as e:
        return None

def extract_xml_content(content):
    """Extract XML content from markdown"""
    xml_blocks = []
    
    # XML metadata patterns
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
    ]
    
    for pattern, flags in xml_patterns:
        matches = re.findall(pattern, content, flags)
        xml_blocks.extend(matches)
    
    return '\n'.join(xml_blocks)

def calculate_max_nesting_depth(xml_content):
    """Calculate maximum XML nesting depth"""
    max_depth = 0
    current_depth = 0
    
    # Find all opening and closing tags
    tags = re.findall(r'<(/?)([a-zA-Z_][a-zA-Z0-9_-]*)[^>]*/?>', xml_content)
    
    for is_closing, tag_name in tags:
        if is_closing:  # Closing tag
            current_depth -= 1
        else:  # Opening tag (not self-closing)
            current_depth += 1
            max_depth = max(max_depth, current_depth)
    
    return max_depth

def analyze_performance_bottlenecks(xml_files):
    """Analyze performance bottlenecks across all XML files"""
    results = {
        'total_files': len(xml_files),
        'file_metrics': [],
        'category_performance': defaultdict(list),
        'bottleneck_analysis': {
            'slowest_files': [],
            'largest_files': [],
            'most_complex_files': [],
            'xml_heavy_files': [],
            'parse_failures': []
        },
        'performance_correlations': {},
        'system_impact': {}
    }
    
    print(f"Analyzing performance bottlenecks in {len(xml_files)} files...")
    
    # Get initial memory usage
    process = psutil.Process()
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    total_processing_time = 0
    
    for i, file_path in enumerate(xml_files):
        if i % 10 == 0:
            print(f"  Processing {i+1}/{len(xml_files)}")
        
        relative_path = str(file_path.relative_to(Path(".")))
        file_type = categorize_file_type(file_path)
        
        metrics = measure_file_metrics(file_path)
        if not metrics:
            continue
        
        file_result = {
            'file_path': relative_path,
            'file_type': file_type,
            **metrics
        }
        
        results['file_metrics'].append(file_result)
        results['category_performance'][file_type].append(file_result)
        
        total_processing_time += metrics['total_processing_time']
        
        # Track bottlenecks
        if metrics['total_processing_time'] > 0.001:  # > 1ms
            results['bottleneck_analysis']['slowest_files'].append(file_result)
        
        if metrics['file_size'] > 50000:  # > 50KB
            results['bottleneck_analysis']['largest_files'].append(file_result)
        
        if metrics['xml_elements'] > 100:
            results['bottleneck_analysis']['most_complex_files'].append(file_result)
        
        if metrics['xml_ratio'] > 80:
            results['bottleneck_analysis']['xml_heavy_files'].append(file_result)
        
        if not metrics['xml_parse_success'] and metrics['xml_chars'] > 0:
            results['bottleneck_analysis']['parse_failures'].append(file_result)
    
    # Get final memory usage
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    memory_usage = final_memory - initial_memory
    
    results['system_impact'] = {
        'total_processing_time': total_processing_time,
        'memory_usage_mb': memory_usage,
        'average_file_time': total_processing_time / len(xml_files) if xml_files else 0,
        'files_per_second': len(xml_files) / total_processing_time if total_processing_time > 0 else 0
    }
    
    # Calculate performance correlations
    results['performance_correlations'] = calculate_performance_correlations(results['file_metrics'])
    
    return results

def calculate_performance_correlations(file_metrics):
    """Calculate correlations between file characteristics and performance"""
    if len(file_metrics) < 2:
        return {}
    
    # Extract metrics for correlation analysis
    processing_times = [f['total_processing_time'] for f in file_metrics]
    file_sizes = [f['file_size'] for f in file_metrics]
    xml_ratios = [f['xml_ratio'] for f in file_metrics]
    xml_elements = [f['xml_elements'] for f in file_metrics]
    nesting_depths = [f['xml_nesting_depth'] for f in file_metrics]
    
    correlations = {}
    
    # Simple correlation calculation (Pearson correlation coefficient approximation)
    def simple_correlation(x, y):
        if len(x) != len(y) or len(x) < 2:
            return 0
        
        mean_x = statistics.mean(x)
        mean_y = statistics.mean(y)
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
        
        sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(len(x)))
        sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(len(y)))
        
        denominator = (sum_sq_x * sum_sq_y) ** 0.5
        
        return numerator / denominator if denominator != 0 else 0
    
    correlations['size_vs_time'] = simple_correlation(file_sizes, processing_times)
    correlations['xml_ratio_vs_time'] = simple_correlation(xml_ratios, processing_times)
    correlations['xml_elements_vs_time'] = simple_correlation(xml_elements, processing_times)
    correlations['nesting_vs_time'] = simple_correlation(nesting_depths, processing_times)
    
    return correlations

def generate_bottleneck_report(results):
    """Generate comprehensive performance bottleneck report"""
    print("\n" + "=" * 60)
    print("STEP 16: PERFORMANCE BOTTLENECK IDENTIFICATION RESULTS")
    print("=" * 60)
    
    total_files = results['total_files']
    system_impact = results['system_impact']
    
    print(f"Total Files Analyzed: {total_files}")
    print(f"Total Processing Time: {system_impact['total_processing_time']:.3f} seconds")
    print(f"Memory Usage: {system_impact['memory_usage_mb']:.1f} MB")
    print(f"Average Time per File: {system_impact['average_file_time']*1000:.2f} ms")
    print(f"Processing Rate: {system_impact['files_per_second']:.1f} files/second")
    
    # Performance correlations
    correlations = results['performance_correlations']
    print(f"\nPerformance Correlations:")
    print(f"  File Size vs Processing Time: {correlations.get('size_vs_time', 0):.3f}")
    print(f"  XML Ratio vs Processing Time: {correlations.get('xml_ratio_vs_time', 0):.3f}")
    print(f"  XML Elements vs Processing Time: {correlations.get('xml_elements_vs_time', 0):.3f}")
    print(f"  XML Nesting vs Processing Time: {correlations.get('nesting_vs_time', 0):.3f}")
    
    # Category performance analysis
    print(f"\nPerformance by Category:")
    category_stats = []
    for category, files in results['category_performance'].items():
        if files:
            avg_time = statistics.mean(f['total_processing_time'] for f in files) * 1000  # ms
            avg_size = statistics.mean(f['file_size'] for f in files) / 1024  # KB
            avg_xml_ratio = statistics.mean(f['xml_ratio'] for f in files)
            category_stats.append((category, avg_time, avg_size, avg_xml_ratio, len(files)))
    
    category_stats.sort(key=lambda x: x[1], reverse=True)  # Sort by avg time
    
    for category, avg_time, avg_size, avg_xml_ratio, count in category_stats:
        status = "🚨" if avg_time > 2.0 else "⚠️" if avg_time > 1.0 else "✅"
        print(f"  {status} {category:<25} {avg_time:5.2f}ms, {avg_size:5.1f}KB, {avg_xml_ratio:4.1f}% XML ({count} files)")
    
    # Bottleneck analysis
    bottlenecks = results['bottleneck_analysis']
    
    # Slowest files
    slowest = sorted(bottlenecks['slowest_files'], key=lambda x: x['total_processing_time'], reverse=True)[:10]
    if slowest:
        print(f"\nSlowest Processing Files (>1ms):")
        for i, file_info in enumerate(slowest, 1):
            time_ms = file_info['total_processing_time'] * 1000
            print(f"  {i:2d}. {time_ms:6.2f}ms - {file_info['file_path']} ({file_info['file_type']})")
    
    # Largest files
    largest = sorted(bottlenecks['largest_files'], key=lambda x: x['file_size'], reverse=True)[:10]
    if largest:
        print(f"\nLargest Files (>50KB):")
        for i, file_info in enumerate(largest, 1):
            size_kb = file_info['file_size'] / 1024
            print(f"  {i:2d}. {size_kb:6.1f}KB - {file_info['file_path']} ({file_info['file_type']})")
    
    # Most complex files
    complex_files = sorted(bottlenecks['most_complex_files'], key=lambda x: x['xml_elements'], reverse=True)[:10]
    if complex_files:
        print(f"\nMost XML Complex Files (>100 elements):")
        for i, file_info in enumerate(complex_files, 1):
            elements = file_info['xml_elements']
            nesting = file_info['xml_nesting_depth']
            print(f"  {i:2d}. {elements:3d} elements, {nesting} levels - {file_info['file_path']} ({file_info['file_type']})")
    
    # XML-heavy files
    xml_heavy = sorted(bottlenecks['xml_heavy_files'], key=lambda x: x['xml_ratio'], reverse=True)[:10]
    if xml_heavy:
        print(f"\nXML-Heavy Files (>80% XML):")
        for i, file_info in enumerate(xml_heavy, 1):
            xml_ratio = file_info['xml_ratio']
            print(f"  {i:2d}. {xml_ratio:5.1f}% XML - {file_info['file_path']} ({file_info['file_type']})")
    
    # Parse failures
    parse_failures = bottlenecks['parse_failures']
    if parse_failures:
        print(f"\nXML Parse Failures ({len(parse_failures)} files):")
        for i, file_info in enumerate(parse_failures[:5], 1):
            print(f"  {i:2d}. {file_info['file_path']} ({file_info['file_type']})")
    
    # Performance impact analysis
    print(f"\nPerformance Impact Analysis:")
    
    # Calculate potential savings
    xml_heavy_count = len(xml_heavy)
    slow_files_count = len(slowest)
    complex_files_count = len(complex_files)
    
    print(f"  XML-Heavy Files: {xml_heavy_count} files ({xml_heavy_count/total_files*100:.1f}%)")
    print(f"  Slow Processing Files: {slow_files_count} files ({slow_files_count/total_files*100:.1f}%)")
    print(f"  Complex XML Files: {complex_files_count} files ({complex_files_count/total_files*100:.1f}%)")
    
    # Estimated improvement potential
    if xml_heavy_count > 0:
        current_avg_time = system_impact['average_file_time'] * 1000  # ms
        potential_improvement = min(50, xml_heavy_count / total_files * 100)  # Max 50% improvement
        print(f"  Potential Speed Improvement: {potential_improvement:.1f}% by optimizing XML-heavy files")
    
    print("=" * 60)

def main():
    """Main performance bottleneck analysis"""
    xml_files = find_xml_files()
    
    if not xml_files:
        print("No XML-tagged files found!")
        return
    
    results = analyze_performance_bottlenecks(xml_files)
    generate_bottleneck_report(results)
    
    # Save detailed results
    with open('performance_bottleneck_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\nDetailed results saved to: performance_bottleneck_results.json")

if __name__ == "__main__":
    main()