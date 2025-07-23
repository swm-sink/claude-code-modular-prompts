#!/usr/bin/env python3
"""
XML Repair and Migration Script for Claude Code Prompt Factory
Fixes XML parsing errors and standardizes template compliance.
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class XMLRepairMigrator:
    def __init__(self, root_path: str = "claude_prompt_factory"):
        self.root_path = Path(root_path)
        self.repairs_made = []
        self.failed_repairs = []
        
    def repair_xml_structure(self, file_path: Path) -> Dict[str, any]:
        """Repair XML structure issues in a single file."""
        result = {
            "file": str(file_path),
            "success": False,
            "repairs": [],
            "errors": []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Common XML repair patterns
            content = self._fix_mismatched_tags(content, result)
            content = self._fix_unclosed_tags(content, result)  
            content = self._fix_invalid_tokens(content, result)
            content = self._fix_malformed_cdata(content, result)
            content = self._standardize_output_sections(content, result)
            
            # Validate the repaired XML
            if self._validate_xml_structure(content, file_path):
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    result["success"] = True
                    logging.info(f"Successfully repaired {file_path}")
                else:
                    result["success"] = True  # No changes needed
                    
            else:
                result["errors"].append("XML still invalid after repairs")
                
        except Exception as e:
            result["errors"].append(f"Repair failed: {str(e)}")
            
        return result
        
    def _fix_mismatched_tags(self, content: str, result: Dict) -> str:
        """Fix common mismatched tag patterns."""
        fixes = [
            # Fix common tag mismatches
            (r'<o>', '<output>'),
            (r'</o>', '</output>'),
            (r'<output_format>', '<output>'),
            (r'</output_format>', '</output>'),
            
            # Fix incomplete closing tags
            (r'<([^/>]+)>\s*</\s*>', r'<\1></\1>'),
            
            # Fix self-closing tags that should be paired
            (r'<(step|description|output|metadata) ([^>]*)/>', r'<\1 \2></\1>'),
        ]
        
        for pattern, replacement in fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                result["repairs"].append(f"Fixed pattern: {pattern} -> {replacement}")
                
        return content
        
    def _fix_unclosed_tags(self, content: str, result: Dict) -> str:
        """Fix unclosed XML tags by analyzing structure."""
        lines = content.split('\n')
        stack = []
        
        for i, line in enumerate(lines):
            # Find opening tags
            opening_tags = re.findall(r'<(\w+)(?:\s[^>]*)?>', line)
            for tag in opening_tags:
                if tag not in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                    stack.append((tag, i))
            
            # Find closing tags  
            closing_tags = re.findall(r'</(\w+)>', line)
            for tag in closing_tags:
                if stack and stack[-1][0] == tag:
                    stack.pop()
                elif stack:
                    # Mismatched closing tag - try to fix
                    expected_tag = stack[-1][0]
                    lines[i] = line.replace(f'</{tag}>', f'</{expected_tag}>')
                    result["repairs"].append(f"Fixed mismatched closing tag at line {i+1}: {tag} -> {expected_tag}")
                    stack.pop()
        
        # Close any remaining unclosed tags
        while stack:
            tag, line_num = stack.pop()
            lines.append(f'</{tag}>')
            result["repairs"].append(f"Added missing closing tag: </{tag}>")
            
        return '\n'.join(lines)
        
    def _fix_invalid_tokens(self, content: str, result: Dict) -> str:
        """Fix invalid XML tokens and characters."""
        fixes = [
            # Fix unescaped ampersands
            (r'&(?!(?:amp|lt|gt|quot|apos);)', '&amp;'),
            
            # Fix unescaped less-than signs
            (r'<(?![/!?]?\w)', '&lt;'),
            
            # Fix invalid characters in XML
            (r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', ''),
            
            # Fix quotes in attributes
            (r'(\w+)=([^"\s>]+)(?=\s|>)', r'\1="\2"'),
        ]
        
        for pattern, replacement in fixes:
            original = content
            content = re.sub(pattern, replacement, content)
            if content != original:
                result["repairs"].append(f"Fixed invalid tokens: {pattern}")
                
        return content
        
    def _fix_malformed_cdata(self, content: str, result: Dict) -> str:
        """Fix malformed CDATA sections."""
        # Ensure CDATA sections are properly formed
        content = re.sub(r'<!\[CDATA\[(.*?)\]\]>', 
                        lambda m: f'<![CDATA[\n{m.group(1).strip()}\n]]>', 
                        content, flags=re.DOTALL)
                        
        return content
        
    def _standardize_output_sections(self, content: str, result: Dict) -> str:
        """Standardize output sections to use consistent format."""
        # Convert <o> tags to <output>
        if '<o>' in content and '</o>' in content:
            content = content.replace('<o>', '<output>')
            content = content.replace('</o>', '</output>')
            result["repairs"].append("Standardized <o> tags to <output>")
            
        # Convert <output_format> to <output>
        if '<output_format>' in content:
            content = content.replace('<output_format>', '<output>')
            content = content.replace('</output_format>', '</output>')
            result["repairs"].append("Standardized <output_format> to <output>")
            
        return content
        
    def _validate_xml_structure(self, content: str, file_path: Path) -> bool:
        """Validate if XML structure is well-formed."""
        try:
            if file_path.parts[-2] == 'commands':
                # For commands, extract just the XML portion
                xml_match = re.search(r'<command_file>.*?</command_file>', content, re.DOTALL)
                if xml_match:
                    ET.fromstring(xml_match.group(0))
                    return True
                return False
            else:
                # For components, validate the entire content
                ET.fromstring(content)
                return True
        except ET.ParseError:
            return False
            
    def migrate_all(self) -> Dict[str, any]:
        """Migrate all files with XML issues."""
        summary = {
            "total_files_processed": 0,
            "successful_repairs": 0,
            "failed_repairs": 0,
            "results": []
        }
        
        # Process components
        components_dir = self.root_path / "components"
        if components_dir.exists():
            for comp_file in components_dir.rglob("*.md"):
                if comp_file.name != "README.md":
                    result = self.repair_xml_structure(comp_file)
                    summary["results"].append(result)
                    summary["total_files_processed"] += 1
                    if result["success"]:
                        summary["successful_repairs"] += 1
                    else:
                        summary["failed_repairs"] += 1
                        
        # Process commands  
        commands_dir = self.root_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.rglob("*.md"):
                if cmd_file.name != "README.md":
                    result = self.repair_xml_structure(cmd_file)
                    summary["results"].append(result)
                    summary["total_files_processed"] += 1
                    if result["success"]:
                        summary["successful_repairs"] += 1
                    else:
                        summary["failed_repairs"] += 1
                        
        return summary
        
    def generate_migration_report(self, summary: Dict) -> str:
        """Generate migration report."""
        report = []
        report.append("# XML Repair Migration Report")
        report.append(f"**Generated**: {__import__('datetime').datetime.now().isoformat()}")
        report.append("")
        
        # Summary
        report.append("## Executive Summary")
        report.append(f"- **Files Processed**: {summary['total_files_processed']}")
        report.append(f"- **Successful Repairs**: {summary['successful_repairs']}")
        report.append(f"- **Failed Repairs**: {summary['failed_repairs']}")
        success_rate = (summary['successful_repairs'] / summary['total_files_processed'] * 100) if summary['total_files_processed'] > 0 else 0
        report.append(f"- **Success Rate**: {success_rate:.1f}%")
        report.append("")
        
        # Detailed results
        if summary['successful_repairs'] > 0:
            report.append("## ✅ Successful Repairs")
            for result in summary["results"]:
                if result["success"] and result["repairs"]:
                    report.append(f"### {result['file']}")
                    for repair in result["repairs"]:
                        report.append(f"- ✅ {repair}")
                    report.append("")
                    
        if summary['failed_repairs'] > 0:
            report.append("## ❌ Failed Repairs")
            for result in summary["results"]:
                if not result["success"]:
                    report.append(f"### {result['file']}")
                    for error in result["errors"]:
                        report.append(f"- ❌ {error}")
                    report.append("")
        
        return "\n".join(report)

def main():
    """Main migration function."""
    migrator = XMLRepairMigrator()
    summary = migrator.migrate_all()
    report = migrator.generate_migration_report(summary)
    
    # Save report
    with open("xml_repair_migration_report.md", "w") as f:
        f.write(report)
        
    print(f"XML repair migration complete. {summary['successful_repairs']}/{summary['total_files_processed']} files repaired successfully.")
    print("Report saved to xml_repair_migration_report.md")

if __name__ == "__main__":
    main()