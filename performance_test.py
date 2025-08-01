#!/usr/bin/env python3
"""
Step 6: Performance Impact Assessment - XML Parsing Overhead Analysis
"""

import time
import os
import xml.etree.ElementTree as ET
from pathlib import Path
import re
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

def extract_xml_content(file_path):
    """Extract XML content from markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find XML blocks
        xml_blocks = []
        
        # Look for XML metadata blocks
        xml_patterns = [
            r'<!-- AI_METADATA_START -->(.*?)<!-- AI_METADATA_END -->',
            r'<ai_document_metadata>.*?</ai_document_metadata>',
            r'<command_metadata>.*?</command_metadata>',
            r'<component_metadata>.*?</component_metadata>',
            r'<ai_navigation>.*?</ai_navigation>',
            r'<context_engineering>.*?</context_engineering>'
        ]
        
        for pattern in xml_patterns:
            matches = re.findall(pattern, content, re.DOTALL | re.MULTILINE)
            xml_blocks.extend(matches)
        
        return '\n'.join(xml_blocks)
    
    except Exception as e:
        return ""

def measure_parsing_performance(xml_files):
    """Measure XML parsing performance"""
    results = {
        'total_files': len(xml_files),
        'successful_parses': 0,
        'failed_parses': 0,
        'parse_times': [],
        'file_sizes': [],
        'xml_sizes': [],
        'errors': []
    }
    
    print(f"Testing XML parsing performance on {len(xml_files)} files...")
    
    for i, file_path in enumerate(xml_files):
        if i % 10 == 0:
            print(f"  Processing file {i+1}/{len(xml_files)}")
        
        try:
            # Measure file size
            file_size = os.path.getsize(file_path)
            results['file_sizes'].append(file_size)
            
            # Extract XML content
            xml_content = extract_xml_content(file_path)
            xml_size = len(xml_content.encode('utf-8'))
            results['xml_sizes'].append(xml_size)
            
            if xml_content.strip():
                # Measure parsing time
                start_time = time.perf_counter()
                
                # Attempt to parse XML
                # Note: This is a simplified test - real XML in markdown is mixed with other content
                try:
                    # Create a minimal XML wrapper for parsing test
                    wrapped_xml = f"<root>{xml_content}</root>"
                    ET.fromstring(wrapped_xml)
                    results['successful_parses'] += 1
                except ET.ParseError:
                    # Try parsing individual blocks
                    results['failed_parses'] += 1
                    results['errors'].append(f"Parse error in {file_path}")
                
                end_time = time.perf_counter()
                parse_time = (end_time - start_time) * 1000  # Convert to milliseconds
                results['parse_times'].append(parse_time)
            
        except Exception as e:
            results['failed_parses'] += 1
            results['errors'].append(f"Error processing {file_path}: {str(e)}")
    
    return results

def analyze_performance_impact(results):
    """Analyze performance impact"""
    if not results['parse_times']:
        return "No successful parses to analyze"
    
    analysis = {
        'total_files': results['total_files'],
        'success_rate': (results['successful_parses'] / results['total_files']) * 100,
        'avg_parse_time_ms': statistics.mean(results['parse_times']),
        'max_parse_time_ms': max(results['parse_times']),
        'min_parse_time_ms': min(results['parse_times']),
        'total_parse_time_ms': sum(results['parse_times']),
        'avg_file_size_kb': statistics.mean(results['file_sizes']) / 1024,
        'avg_xml_size_kb': statistics.mean(results['xml_sizes']) / 1024,
        'xml_overhead_ratio': statistics.mean(results['xml_sizes']) / statistics.mean(results['file_sizes']),
        'projected_full_library_load_time_ms': sum(results['parse_times']),
        'errors_count': len(results['errors'])
    }
    
    return analysis

def main():
    """Main performance assessment"""
    print("=" * 60)
    print("STEP 6: XML PARSING PERFORMANCE IMPACT ASSESSMENT")
    print("=" * 60)
    
    # Find XML files
    xml_files = find_xml_files()
    print(f"Found {len(xml_files)} XML-tagged files")
    
    if not xml_files:
        print("No XML-tagged files found!")
        return
    
    # Measure performance
    results = measure_parsing_performance(xml_files)
    analysis = analyze_performance_impact(results)
    
    # Report results
    print("\n" + "=" * 40)
    print("PERFORMANCE ANALYSIS RESULTS")
    print("=" * 40)
    
    if isinstance(analysis, dict):
        print(f"Total Files Analyzed: {analysis['total_files']}")
        print(f"Parse Success Rate: {analysis['success_rate']:.1f}%")
        print(f"Average Parse Time: {analysis['avg_parse_time_ms']:.2f} ms")
        print(f"Maximum Parse Time: {analysis['max_parse_time_ms']:.2f} ms")
        print(f"Total Parse Time: {analysis['total_parse_time_ms']:.2f} ms")
        print(f"Average File Size: {analysis['avg_file_size_kb']:.1f} KB")
        print(f"Average XML Size: {analysis['avg_xml_size_kb']:.1f} KB")
        print(f"XML Overhead Ratio: {analysis['xml_overhead_ratio']:.1%}")
        print(f"Projected Full Library Load Time: {analysis['projected_full_library_load_time_ms']:.2f} ms")
        print(f"Parse Errors: {analysis['errors_count']}")
        
        # Performance rating
        total_time = analysis['projected_full_library_load_time_ms']
        if total_time < 100:
            rating = "EXCELLENT"
        elif total_time < 500:
            rating = "GOOD"
        elif total_time < 1000:
            rating = "ACCEPTABLE"
        elif total_time < 2000:
            rating = "POOR"
        else:
            rating = "CRITICAL"
        
        print(f"\nPerformance Rating: {rating}")
        
        # Show errors if any
        if results['errors']:
            print("\nERRORS ENCOUNTERED:")
            for error in results['errors'][:5]:  # Show first 5 errors
                print(f"  - {error}")
            if len(results['errors']) > 5:
                print(f"  ... and {len(results['errors']) - 5} more errors")
    
    else:
        print(analysis)
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()