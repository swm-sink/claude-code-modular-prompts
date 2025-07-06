#!/usr/bin/env python3
"""
XML Structure Validation Script for Claude Framework
Validates XML syntax, structure, and compliance with Claude 4 standards
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Set
import xml.etree.ElementTree as ET
from collections import defaultdict

class XMLValidator:
    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.errors = []
        self.warnings = []
        self.stats = defaultdict(int)
        
    def validate_all_files(self) -> Dict[str, List[str]]:
        """Validate all markdown files in the framework"""
        results = {}
        
        # Find all .md files
        md_files = list(self.framework_root.rglob("*.md"))
        print(f"Found {len(md_files)} markdown files to validate")
        
        for file_path in md_files:
            print(f"Validating: {file_path.relative_to(self.framework_root)}")
            file_results = self.validate_file(file_path)
            results[str(file_path)] = file_results
            
        return results
    
    def validate_file(self, file_path: Path) -> List[str]:
        """Validate XML structure in a single file"""
        errors = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Check for XML blocks
            xml_blocks = self.extract_xml_blocks(content)
            
            if not xml_blocks:
                self.stats['no_xml_files'] += 1
                return ["No XML blocks found"]
            
            self.stats['xml_files'] += 1
            
            for i, xml_block in enumerate(xml_blocks):
                block_errors = self.validate_xml_block(xml_block, i)
                errors.extend(block_errors)
                
        except Exception as e:
            errors.append(f"Error reading file: {str(e)}")
            
        return errors
    
    def extract_xml_blocks(self, content: str) -> List[str]:
        """Extract XML blocks from markdown content"""
        xml_blocks = []
        
        # Look for XML-like structures (tags with angle brackets)
        # This is more permissive than strict XML since we're in markdown
        lines = content.split('\n')
        current_block = []
        in_xml_block = False
        
        for line in lines:
            # Check if line contains XML tags
            if '<' in line and '>' in line:
                if not in_xml_block:
                    in_xml_block = True
                    current_block = [line]
                else:
                    current_block.append(line)
            elif in_xml_block:
                if line.strip() == '' or line.startswith('  ') or line.startswith('\t'):
                    # Continue the block for indented or empty lines
                    current_block.append(line)
                else:
                    # End of XML block
                    if current_block:
                        xml_blocks.append('\n'.join(current_block))
                    current_block = []
                    in_xml_block = False
                    
                    # Check if this line starts a new XML block
                    if '<' in line and '>' in line:
                        in_xml_block = True
                        current_block = [line]
        
        # Don't forget the last block
        if current_block:
            xml_blocks.append('\n'.join(current_block))
            
        return xml_blocks
    
    def validate_xml_block(self, xml_block: str, block_index: int) -> List[str]:
        """Validate a single XML block"""
        errors = []
        
        # Check for basic XML structure
        errors.extend(self.check_tag_matching(xml_block, block_index))
        errors.extend(self.check_nesting(xml_block, block_index))
        errors.extend(self.check_claude4_patterns(xml_block, block_index))
        
        return errors
    
    def check_tag_matching(self, xml_block: str, block_index: int) -> List[str]:
        """Check if opening and closing tags match"""
        errors = []
        
        # Find all opening tags (not self-closing)
        opening_tags = re.findall(r'<(\w+)(?:\s[^>]*)?(?<!/)>', xml_block)
        # Find self-closing tags
        self_closing_tags = re.findall(r'<(\w+)(?:\s[^>]*)?/>', xml_block)
        # Find closing tags
        closing_tags = re.findall(r'</(\w+)', xml_block)
        
        # Remove self-closing tags from opening tags (they don't need closing tags)
        actual_opening_tags = [tag for tag in opening_tags if tag not in self_closing_tags]
        
        # Check for unmatched tags
        for tag in actual_opening_tags:
            if tag not in closing_tags:
                errors.append(f"Block {block_index}: Opening tag '<{tag}>' has no matching closing tag")
        
        for tag in closing_tags:
            if tag not in actual_opening_tags:
                errors.append(f"Block {block_index}: Closing tag '</{tag}>' has no matching opening tag")
        
        return errors
    
    def check_nesting(self, xml_block: str, block_index: int) -> List[str]:
        """Check proper nesting of XML tags"""
        errors = []
        
        # Simple stack-based nesting check
        tag_stack = []
        lines = xml_block.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Find self-closing tags first and exclude them
            self_closing = re.findall(r'<(\w+)(?:\s[^>]*)?/>', line)
            
            # Find opening and closing tags (not self-closing)
            tags = re.findall(r'<(/?)(\w+)(?:\s[^>]*)?(?<!/)>', line)
            
            for is_closing, tag_name in tags:
                # Skip if this tag is self-closing
                if tag_name in self_closing:
                    continue
                    
                if is_closing:
                    # Closing tag
                    if not tag_stack:
                        errors.append(f"Block {block_index}, line {line_num}: Closing tag '</{tag_name}>' with no opening tag")
                    elif tag_stack[-1] != tag_name:
                        errors.append(f"Block {block_index}, line {line_num}: Mismatched closing tag '</{tag_name}>', expected '</{tag_stack[-1]}>'")
                    else:
                        tag_stack.pop()
                else:
                    # Opening tag
                    tag_stack.append(tag_name)
        
        # Check for unclosed tags
        for tag in tag_stack:
            errors.append(f"Block {block_index}: Unclosed tag '<{tag}>'")
        
        return errors
    
    def check_claude4_patterns(self, xml_block: str, block_index: int) -> List[str]:
        """Check for Claude 4 specific patterns"""
        errors = []
        
        # Check for enforcement attributes
        if 'enforcement=' in xml_block:
            self.stats['enforcement_patterns'] += 1
            
            # Validate enforcement values
            enforcement_values = re.findall(r'enforcement="([^"]*)"', xml_block)
            valid_enforcement = {'mandatory', 'strict', 'absolute', 'automatic'}
            
            for value in enforcement_values:
                if value not in valid_enforcement:
                    errors.append(f"Block {block_index}: Invalid enforcement value '{value}'. Valid values: {valid_enforcement}")
        
        # Check for priority attributes
        if 'priority=' in xml_block:
            self.stats['priority_patterns'] += 1
            
            priority_values = re.findall(r'priority="([^"]*)"', xml_block)
            valid_priority = {'highest', 'high', 'medium', 'low', 'mandatory'}
            
            for value in priority_values:
                if value not in valid_priority:
                    errors.append(f"Block {block_index}: Invalid priority value '{value}'. Valid values: {valid_priority}")
        
        # Check for common Claude 4 tags
        claude4_tags = ['framework_principles', 'strict_enforcement', 'execution_requirements', 
                       'cognitive_process', 'quality_gates', 'validation_checklist']
        
        for tag in claude4_tags:
            if f'<{tag}' in xml_block:
                self.stats[f'{tag}_usage'] += 1
        
        return errors
    
    def generate_report(self, results: Dict[str, List[str]]) -> str:
        """Generate a comprehensive validation report"""
        report = []
        report.append("=" * 80)
        report.append("CLAUDE FRAMEWORK XML VALIDATION REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Summary statistics
        total_files = len(results)
        files_with_errors = sum(1 for errors in results.values() if errors and errors != ["No XML blocks found"])
        files_with_xml = self.stats['xml_files']
        
        report.append("SUMMARY STATISTICS:")
        report.append(f"- Total files analyzed: {total_files}")
        report.append(f"- Files with XML blocks: {files_with_xml}")
        report.append(f"- Files with errors: {files_with_errors}")
        report.append(f"- Files without XML: {self.stats['no_xml_files']}")
        report.append("")
        
        # Claude 4 pattern usage
        report.append("CLAUDE 4 PATTERN USAGE:")
        report.append(f"- Enforcement patterns: {self.stats['enforcement_patterns']}")
        report.append(f"- Priority patterns: {self.stats['priority_patterns']}")
        
        for key, value in self.stats.items():
            if key.endswith('_usage'):
                tag_name = key.replace('_usage', '')
                report.append(f"- {tag_name} tags: {value}")
        report.append("")
        
        # Detailed errors
        if files_with_errors > 0:
            report.append("DETAILED ERRORS:")
            report.append("-" * 40)
            
            for file_path, errors in results.items():
                if errors and errors != ["No XML blocks found"]:
                    relative_path = Path(file_path).relative_to(self.framework_root)
                    report.append(f"\n{relative_path}:")
                    for error in errors:
                        report.append(f"  ❌ {error}")
        
        # Files without XML (informational)
        files_without_xml = [f for f, errors in results.items() if errors == ["No XML blocks found"]]
        if files_without_xml:
            report.append("\nFILES WITHOUT XML BLOCKS:")
            report.append("-" * 40)
            for file_path in files_without_xml:
                relative_path = Path(file_path).relative_to(self.framework_root)
                report.append(f"  ℹ️  {relative_path}")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)

def main():
    if len(sys.argv) > 1:
        framework_root = sys.argv[1]
    else:
        framework_root = "/Users/smenssink/Documents/Github personal projects/claude-code-modular-agents/.claude"
    
    validator = XMLValidator(framework_root)
    results = validator.validate_all_files()
    report = validator.generate_report(results)
    
    print(report)
    
    # Save report to file
    report_file = Path(framework_root) / "validation_report.txt"
    report_file.write_text(report)
    print(f"\nReport saved to: {report_file}")
    
    # Exit with error code if validation failed
    files_with_errors = sum(1 for errors in results.values() if errors and errors != ["No XML blocks found"])
    return 1 if files_with_errors > 0 else 0

if __name__ == "__main__":
    sys.exit(main())