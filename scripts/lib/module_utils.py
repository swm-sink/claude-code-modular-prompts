"""Shared module analysis utilities."""

import os
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional


class ModuleAnalyzer:
    """Unified module analyzer for framework modules."""
    
    def __init__(self, base_path: str = ".claude"):
        self.base_path = Path(base_path)
        self.modules = []
        self.module_data = {}
        
    def find_modules(self, patterns: List[str] = None) -> List[Path]:
        """Find all module files matching patterns."""
        if patterns is None:
            patterns = ["modules/**/*.md", "patterns/**/*.md", "prompt_eng/**/*.md", 
                       "system/**/*.md", "meta/**/*.md", "domain/**/*.md"]
        
        self.modules = []
        for pattern in patterns:
            for path in self.base_path.glob(pattern):
                if path.name != "README.md" and path.is_file():
                    self.modules.append(path)
        
        return self.modules
    
    def extract_references(self, content: str) -> Set[str]:
        """Extract all module references from content."""
        references = set()
        
        # Pattern 1: Direct module references
        pattern1 = r'(modules|patterns|quality|development|security|system|meta|prompt_eng)/([^/\s]+)/([^/\s]+)\.md'
        matches1 = re.findall(pattern1, content)
        for category, subcat, module in matches1:
            references.add(f"{category}/{subcat}/{module}.md")
        
        # Pattern 2: Two-level references
        pattern2 = r'(modules|patterns|quality|development|security|system|meta)/([^/\s]+)\.md'
        matches2 = re.findall(pattern2, content)
        for category, module in matches2:
            references.add(f"{category}/{module}.md")
        
        # Pattern 3: Canonical source tags
        pattern3 = r'<canonical_source>([^<]+)</canonical_source>'
        matches3 = re.findall(pattern3, content)
        for ref in matches3:
            ref = ref.strip()
            if any(prefix in ref for prefix in ['modules/', 'system/', 'prompt_eng/', 'patterns/', 'quality/', 'meta/']):
                references.add(ref)
        
        # Pattern 4: Module attribute references
        pattern4 = r'module\s*=\s*"([^"]+)"'
        matches4 = re.findall(pattern4, content)
        for ref in matches4:
            if not ref.startswith('.') and '.md' in ref:
                references.add(ref)
        
        # Pattern 5: Markdown links
        pattern5 = r'\[([^\]]+)\]\(([^)]+\.md)\)'
        matches5 = re.findall(pattern5, content)
        for _, ref in matches5:
            if any(prefix in ref for prefix in ['modules/', 'system/', 'prompt_eng/', 'patterns/', 'quality/', 'meta/']):
                references.add(ref.strip())
        
        return references
    
    def analyze_dependencies(self, module_path: Path) -> Dict[str, any]:
        """Analyze dependencies for a single module."""
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        references = self.extract_references(content)
        
        # Classify references
        internal_refs = []
        external_refs = []
        broken_refs = []
        
        for ref in references:
            ref_path = self.base_path / ref
            if ref_path.exists():
                if str(ref_path).startswith(str(self.base_path)):
                    internal_refs.append(ref)
                else:
                    external_refs.append(ref)
            else:
                broken_refs.append(ref)
        
        return {
            'path': str(module_path),
            'references': list(references),
            'internal_refs': internal_refs,
            'external_refs': external_refs,
            'broken_refs': broken_refs,
            'ref_count': len(references)
        }
    
    def analyze_documentation(self, module_path: Path) -> Dict[str, any]:
        """Analyze documentation quality of a module."""
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check various documentation aspects
        checks = {
            'has_version_table': bool(re.search(r'^\|\s*version\s*\|', content, re.MULTILINE)),
            'has_title': bool(re.search(r'^#\s+\w+', content, re.MULTILINE)),
            'has_purpose': bool(re.search(r'(?i)(purpose|overview|description):', content)),
            'has_usage': bool(re.search(r'(?i)(usage|example|how to use):', content)),
            'has_interface': bool(re.search(r'(?i)(interface|input|output|parameters):', content)),
            'has_dependencies': bool(re.search(r'(?i)(dependencies|requires|imports):', content)),
            'has_error_handling': bool(re.search(r'(?i)(error|exception|failure|recovery):', content)),
            'has_thinking_pattern': '<thinking_pattern>' in content,
            'has_implementation': '<implementation>' in content,
            'has_xml_structure': bool(re.search(r'<\w+[^>]*>', content)),
            'line_count': len(content.splitlines()),
            'word_count': len(content.split())
        }
        
        # Calculate documentation score
        score = sum(1 for check, value in checks.items() if value and check.startswith('has_')) * 10
        checks['doc_score'] = min(score, 100)
        
        return checks
    
    def check_compliance(self, module_path: Path) -> Dict[str, any]:
        """Check module compliance with framework standards."""
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()
        
        compliance = {
            'has_correct_version_table': False,
            'has_july_2025_date': False,
            'has_separator_after_header': False,
            'xml_properly_wrapped': True,
            'no_outdated_timestamps': True
        }
        
        # Check version table format
        if len(lines) >= 3:
            if (lines[0].startswith('| version') and 
                lines[1].startswith('|---') and 
                lines[2].startswith('|')):
                compliance['has_correct_version_table'] = True
                
                # Check for July 2025 date
                if re.search(r'2025-07-\d{2}', lines[2]):
                    compliance['has_july_2025_date'] = True
        
        # Check separator after header
        separator = '─' * 80
        for i, line in enumerate(lines):
            if line.startswith('# ') and i > 3:
                if i + 1 < len(lines) and lines[i + 1] == separator:
                    compliance['has_separator_after_header'] = True
                break
        
        # Check XML wrapping
        if '<' in content and '>' in content:
            xml_blocks = re.findall(r'<[^>]+>.*?</[^>]+>', content, re.DOTALL)
            for block in xml_blocks:
                if '```xml' not in content:
                    compliance['xml_properly_wrapped'] = False
                    break
        
        # Check for outdated timestamps
        old_dates = re.findall(r'20(1[0-9]|2[0-4])-\d{2}-\d{2}', content)
        if old_dates:
            compliance['no_outdated_timestamps'] = False
        
        compliance['compliance_score'] = sum(1 for v in compliance.values() if v) * 20
        
        return compliance
    
    def validate_interfaces(self, module_path: Path) -> Dict[str, any]:
        """Validate module interfaces and contracts."""
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        interface_data = {
            'has_input_spec': bool(re.search(r'(?i)(input|parameters|arguments):', content)),
            'has_output_spec': bool(re.search(r'(?i)(output|returns|result):', content)),
            'has_error_spec': bool(re.search(r'(?i)(errors|exceptions|failures):', content)),
            'has_preconditions': bool(re.search(r'(?i)(precondition|prerequisite|require)', content)),
            'has_postconditions': bool(re.search(r'(?i)(postcondition|ensure|guarantee)', content))
        }
        
        # Extract interface details if present
        interface_match = re.search(r'<interface>(.*?)</interface>', content, re.DOTALL)
        if interface_match:
            interface_data['has_formal_interface'] = True
            interface_data['interface_content'] = interface_match.group(1).strip()
        else:
            interface_data['has_formal_interface'] = False
        
        interface_data['interface_score'] = sum(1 for k, v in interface_data.items() 
                                               if k.startswith('has_') and v) * 15
        
        return interface_data
    
    def generate_dependency_graph(self) -> Dict[str, List[str]]:
        """Generate a complete dependency graph for all modules."""
        graph = {}
        
        for module in self.modules:
            deps = self.analyze_dependencies(module)
            relative_path = str(module.relative_to(self.base_path))
            graph[relative_path] = deps['internal_refs']
        
        return graph