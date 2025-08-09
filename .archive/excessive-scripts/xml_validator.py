#!/usr/bin/env python3
"""
XML Validation Framework for Claude Code Template Library

This script provides comprehensive XML validation for all XML-tagged markdown files
to prevent the anti-patterns we've identified and fixed during Phase 2.

Based on learnings from:
- 8 circular dependency fixes
- 40+ broken reference fixes  
- Template placeholder anti-pattern elimination
- Missing context files anti-pattern fixes
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass, asdict

@dataclass
class ValidationResult:
    """Results from XML validation"""
    file_path: str
    is_valid: bool
    errors: List[str] = None
    warnings: List[str] = None
    metadata: Dict = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []
        if self.warnings is None:
            self.warnings = []
        if self.metadata is None:
            self.metadata = {}

class XMLValidator:
    """Comprehensive XML validator for Claude Code template library"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.results: List[ValidationResult] = []
        
        # Anti-pattern prevention patterns from Phase 2 learnings
        self.placeholder_patterns = [
            r'\[FILE_REFERENCE\]',
            r'\[COMPONENT_NAME\]', 
            r'\[COMMAND_NAME\]',
            r'\[.*_REFERENCE.*\]'
        ]
        
        # Required XML sections for different file types
        self.required_sections = {
            'command': ['ai_document_metadata', 'command_metadata', 'ai_navigation'],
            'component': ['ai_document_metadata', 'component_metadata', 'ai_navigation'],
            'context': ['ai_document_metadata', 'context_metadata', 'ai_navigation'],
            'documentation': ['ai_document_metadata', 'document_metadata', 'ai_navigation']
        }
        
        # Known valid file types to prevent orphaned references
        self.valid_command_files: Set[str] = set()
        self.valid_component_files: Set[str] = set()
        self.valid_context_files: Set[str] = set()
        
    def scan_files(self) -> List[Path]:
        """Find all XML-tagged markdown files"""
        xml_files = []
        
        # Core locations for XML-tagged files
        search_paths = [
            '.claude/commands',
            '.claude/components', 
            '.claude/context',
            'docs/xml-schema',
            '.'  # Root level analysis files
        ]
        
        for search_path in search_paths:
            full_path = self.base_path / search_path
            if full_path.exists():
                for md_file in full_path.rglob('*.md'):
                    if self.has_xml_metadata(md_file):
                        xml_files.append(md_file)
                        
        return xml_files
    
    def has_xml_metadata(self, file_path: Path) -> bool:
        """Check if file contains XML metadata blocks"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(1000)  # Check first 1000 chars
                return '<!-- AI_METADATA_START -->' in content
        except Exception:
            return False
    
    def validate_file(self, file_path: Path) -> ValidationResult:
        """Validate a single XML-tagged markdown file"""
        result = ValidationResult(file_path=str(file_path), is_valid=True)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract XML blocks
            xml_blocks = self.extract_xml_blocks(content)
            
            if not xml_blocks:
                result.is_valid = False
                result.errors.append("No XML metadata blocks found")
                return result
                
            # Validate each XML block
            for block_name, xml_content in xml_blocks.items():
                self.validate_xml_block(block_name, xml_content, result)
                
            # Anti-pattern checks from Phase 2 learnings
            self.check_template_placeholders(content, result)
            self.check_circular_references(content, result)
            self.check_broken_references(content, result)
            self.validate_required_sections(xml_blocks, result)
            
        except Exception as e:
            result.is_valid = False
            result.errors.append(f"Validation failed: {str(e)}")
            
        return result
    
    def extract_xml_blocks(self, content: str) -> Dict[str, str]:
        """Extract XML metadata blocks from markdown content"""
        xml_blocks = {}
        
        # Find AI_METADATA blocks
        start_pattern = r'<!-- AI_METADATA_START -->'
        end_pattern = r'<!-- AI_METADATA_END -->'
        
        start_match = re.search(start_pattern, content)
        end_match = re.search(end_pattern, content)
        
        if start_match and end_match:
            xml_content = content[start_match.end():end_match.start()].strip()
            
            # Parse individual XML sections
            sections = ['ai_document_metadata', 'command_metadata', 'component_metadata', 
                       'context_metadata', 'document_metadata', 'ai_navigation', 
                       'context_engineering']
            
            for section in sections:
                section_match = re.search(f'<{section}.*?</{section}>', xml_content, re.DOTALL)
                if section_match:
                    xml_blocks[section] = section_match.group(0)
                    
        return xml_blocks
    
    def validate_xml_block(self, block_name: str, xml_content: str, result: ValidationResult):
        """Validate individual XML block for well-formedness"""
        try:
            # Attempt to parse as XML
            ET.fromstring(xml_content)
            
            # Extract metadata for analysis
            self.extract_metadata(block_name, xml_content, result)
            
        except ET.ParseError as e:
            result.is_valid = False
            result.errors.append(f"Invalid XML in {block_name}: {str(e)}")
    
    def extract_metadata(self, block_name: str, xml_content: str, result: ValidationResult):
        """Extract useful metadata from XML blocks"""
        if block_name == 'ai_document_metadata':
            # Extract document type
            doc_type_match = re.search(r'<document_type>(.*?)</document_type>', xml_content)
            if doc_type_match:
                result.metadata['document_type'] = doc_type_match.group(1)
                
        elif block_name == 'command_metadata':
            # Extract command info
            cmd_id_match = re.search(r'<command_id>(.*?)</command_id>', xml_content)
            if cmd_id_match:
                result.metadata['command_id'] = cmd_id_match.group(1)
                
    def check_template_placeholders(self, content: str, result: ValidationResult):
        """Check for template placeholder anti-pattern from Phase 2"""
        for pattern in self.placeholder_patterns:
            matches = re.findall(pattern, content)
            if matches:
                result.warnings.append(f"Template placeholder detected: {pattern} (should use {{{{PLACEHOLDER}}}} syntax)")
    
    def check_circular_references(self, content: str, result: ValidationResult):
        """Check for potential circular reference patterns from Phase 2"""
        # Extract ref attributes
        ref_matches = re.findall(r'ref="([^"]*)"', content)
        file_name = Path(result.file_path).stem
        
        # Simple circular reference detection
        if file_name in ref_matches:
            result.warnings.append(f"Potential circular reference: file references itself")
    
    def check_broken_references(self, content: str, result: ValidationResult):
        """Check for broken reference patterns from Phase 2"""
        # Extract all references
        ref_matches = re.findall(r'ref="([^"]*)"', content)
        
        for ref in ref_matches:
            # Skip template placeholders (now using {{}})
            if ref.startswith('{{') and ref.endswith('}}'):
                continue
                
            # Check for obviously broken references
            if not ref or ref.startswith('[') or ref.startswith('PLACEHOLDER'):
                result.errors.append(f"Broken reference detected: {ref}")
    
    def validate_required_sections(self, xml_blocks: Dict[str, str], result: ValidationResult):
        """Validate that required XML sections exist based on document type"""
        doc_type = result.metadata.get('document_type', 'unknown')
        
        if doc_type in self.required_sections:
            required = self.required_sections[doc_type]
            missing = [section for section in required if section not in xml_blocks]
            
            if missing:
                result.errors.append(f"Missing required XML sections for {doc_type}: {missing}")
    
    def validate_all(self) -> Dict:
        """Validate all XML-tagged files and return comprehensive results"""
        files = self.scan_files()
        
        print(f"🔍 Found {len(files)} XML-tagged markdown files to validate")
        
        self.results = []
        for file_path in files:
            print(f"Validating: {file_path}")
            result = self.validate_file(file_path)
            self.results.append(result)
            
        return self.generate_report()
    
    def generate_report(self) -> Dict:
        """Generate comprehensive validation report"""
        total_files = len(self.results)
        valid_files = sum(1 for r in self.results if r.is_valid)
        
        report = {
            'summary': {
                'total_files': total_files,
                'valid_files': valid_files,
                'invalid_files': total_files - valid_files,
                'success_rate': (valid_files / total_files * 100) if total_files > 0 else 0
            },
            'errors': [],
            'warnings': [],
            'file_results': [asdict(r) for r in self.results]
        }
        
        # Collect all errors and warnings
        for result in self.results:
            for error in result.errors:
                report['errors'].append({'file': result.file_path, 'error': error})
            for warning in result.warnings:
                report['warnings'].append({'file': result.file_path, 'warning': warning})
        
        return report

def main():
    """Main validation entry point"""
    print("🚀 XML Validation Framework - Phase 2 Prevention System")
    print("Based on learnings from 8 circular dependency fixes + 40+ broken reference fixes")
    print()
    
    validator = XMLValidator()
    report = validator.validate_all()
    
    print(f"\n📊 VALIDATION RESULTS:")
    print(f"Total files: {report['summary']['total_files']}")
    print(f"Valid files: {report['summary']['valid_files']}")
    print(f"Invalid files: {report['summary']['invalid_files']}")
    print(f"Success rate: {report['summary']['success_rate']:.1f}%")
    
    if report['errors']:
        print(f"\n🚨 ERRORS ({len(report['errors'])}):")
        for error in report['errors'][:10]:  # Show first 10
            print(f"  {error['file']}: {error['error']}")
        if len(report['errors']) > 10:
            print(f"  ... and {len(report['errors']) - 10} more errors")
    
    if report['warnings']:
        print(f"\n⚠️  WARNINGS ({len(report['warnings'])}):")
        for warning in report['warnings'][:10]:  # Show first 10
            print(f"  {warning['file']}: {warning['warning']}")
        if len(report['warnings']) > 10:
            print(f"  ... and {len(report['warnings']) - 10} more warnings")
    
    # Save detailed report
    with open('xml_validation_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Detailed report saved to: xml_validation_report.json")
    
    return 0 if report['summary']['success_rate'] >= 95 else 1

if __name__ == '__main__':
    exit(main())