#!/usr/bin/env python3
"""
Reference Validation Script
Validates all cross-references and links in markdown files
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Set

class ReferenceValidator:
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path).resolve()
        self.markdown_files: List[Path] = []
        self.broken_references: Dict[str, List[Tuple[str, int, str]]] = defaultdict(list)
        self.valid_references: Dict[str, int] = defaultdict(int)
        self.external_references: Dict[str, int] = defaultdict(int)
        
        # Patterns for different types of references
        self.patterns = {
            'markdown_link': re.compile(r'\[([^\]]+)\]\(([^)]+)\)'),
            'reference_link': re.compile(r'\[([^\]]+)\]\[([^\]]+)\]'),
            'reference_def': re.compile(r'^\[([^\]]+)\]:\s*(.+)$', re.MULTILINE),
            'module_ref': re.compile(r'modules?/[a-zA-Z0-9/_-]+\.md'),
            'command_ref': re.compile(r'commands?/[a-zA-Z0-9/_-]+\.md'),
            'claude_ref': re.compile(r'\.claude/[a-zA-Z0-9/_-]+'),
            'script_ref': re.compile(r'scripts?/[a-zA-Z0-9/_-]+\.(py|sh|js)'),
        }
        
    def find_markdown_files(self):
        """Find all markdown files in the project"""
        for root, dirs, files in os.walk(self.root_path):
            # Skip .git and other hidden directories, and internal reports
            dirs[:] = [d for d in dirs if not d.startswith('.') or d == '.claude']
            if 'internal/reports' in root:
                continue
            
            for file in files:
                if file.endswith('.md'):
                    self.markdown_files.append(Path(root) / file)
        
        print(f"Found {len(self.markdown_files)} markdown files")
        
    def extract_references(self, file_path: Path) -> List[Tuple[int, str, str]]:
        """Extract all references from a markdown file"""
        references = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
            # Extract markdown links
            for i, line in enumerate(lines, 1):
                for match in self.patterns['markdown_link'].finditer(line):
                    link_text, link_url = match.groups()
                    if not link_url.startswith(('http://', 'https://', 'mailto:', '#')):
                        references.append((i, link_url, f"[{link_text}]({link_url})"))
                        
            # Extract reference-style links
            ref_definitions = {}
            for match in self.patterns['reference_def'].finditer(content):
                ref_name, ref_url = match.groups()
                ref_definitions[ref_name.lower()] = ref_url
                
            for i, line in enumerate(lines, 1):
                for match in self.patterns['reference_link'].finditer(line):
                    link_text, ref_name = match.groups()
                    ref_url = ref_definitions.get(ref_name.lower())
                    if ref_url and not ref_url.startswith(('http://', 'https://', 'mailto:', '#')):
                        references.append((i, ref_url, f"[{link_text}][{ref_name}]"))
                        
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
        return references
        
    def validate_reference(self, base_path: Path, reference: str) -> bool:
        """Validate if a reference exists"""
        # Handle different reference formats
        ref = reference.strip()
        
        # Remove anchor links
        if '#' in ref:
            ref = ref.split('#')[0]
            
        if not ref:
            return True  # Anchor-only links are valid
            
        # Handle absolute paths from project root
        if ref.startswith('/'):
            target_path = self.root_path / ref[1:]
        else:
            # Handle relative paths
            target_path = (base_path.parent / ref).resolve()
            
        # Check if file exists
        return target_path.exists()
        
    def analyze_references(self):
        """Analyze all references in markdown files"""
        total_refs = 0
        
        for md_file in self.markdown_files:
            relative_path = md_file.relative_to(self.root_path)
            references = self.extract_references(md_file)
            
            for line_num, ref_url, ref_text in references:
                total_refs += 1
                
                if ref_url.startswith(('http://', 'https://', 'mailto:')):
                    self.external_references[ref_url] += 1
                elif self.validate_reference(md_file, ref_url):
                    self.valid_references[ref_url] += 1
                else:
                    self.broken_references[str(relative_path)].append((ref_url, line_num, ref_text))
                    
        print(f"\nAnalyzed {total_refs} references:")
        print(f"  - Valid internal: {sum(self.valid_references.values())}")
        print(f"  - External: {sum(self.external_references.values())}")
        print(f"  - Broken: {sum(len(refs) for refs in self.broken_references.values())}")
        
    def generate_report(self, output_file: str = "reference_validation_report.md"):
        """Generate a detailed report of findings"""
        with open(output_file, 'w') as f:
            f.write("# Reference Validation Report\n\n")
            f.write(f"Generated: {Path(output_file).stem}\n\n")
            
            # Summary
            f.write("## Summary\n\n")
            f.write(f"- Total markdown files: {len(self.markdown_files)}\n")
            f.write(f"- Valid internal references: {sum(self.valid_references.values())}\n")
            f.write(f"- External references: {sum(self.external_references.values())}\n")
            f.write(f"- Broken references: {sum(len(refs) for refs in self.broken_references.values())}\n")
            f.write(f"- Files with broken references: {len(self.broken_references)}\n\n")
            
            # Broken references by file
            if self.broken_references:
                f.write("## Broken References by File\n\n")
                for file_path, refs in sorted(self.broken_references.items()):
                    f.write(f"### {file_path}\n\n")
                    for ref_url, line_num, ref_text in refs:
                        f.write(f"- Line {line_num}: `{ref_text}` → `{ref_url}`\n")
                    f.write("\n")
                    
            # Most referenced files
            f.write("## Most Referenced Files\n\n")
            ref_counts = defaultdict(int)
            for ref, count in self.valid_references.items():
                ref_counts[ref] += count
            
            for ref, count in sorted(ref_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
                f.write(f"- `{ref}`: {count} references\n")
                
            # Pattern analysis
            f.write("\n## Pattern Analysis\n\n")
            patterns_found = defaultdict(list)
            for file_path, refs in self.broken_references.items():
                for ref_url, _, _ in refs:
                    if 'modules/' in ref_url:
                        patterns_found['module_references'].append((file_path, ref_url))
                    elif 'commands/' in ref_url:
                        patterns_found['command_references'].append((file_path, ref_url))
                    elif '.claude/' in ref_url:
                        patterns_found['claude_references'].append((file_path, ref_url))
                    elif 'scripts/' in ref_url:
                        patterns_found['script_references'].append((file_path, ref_url))
                        
            for pattern, occurrences in patterns_found.items():
                if occurrences:
                    f.write(f"### {pattern.replace('_', ' ').title()}\n\n")
                    for file_path, ref in occurrences[:10]:  # Show first 10
                        f.write(f"- {file_path}: `{ref}`\n")
                    if len(occurrences) > 10:
                        f.write(f"- ... and {len(occurrences) - 10} more\n")
                    f.write("\n")
                    
    def suggest_fixes(self) -> Dict[str, str]:
        """Suggest fixes for common broken reference patterns"""
        fixes = {}
        
        # Analyze broken references for patterns
        for file_path, refs in self.broken_references.items():
            for ref_url, _, _ in refs:
                # Check for common patterns
                if 'prompt_eng/patterns' in ref_url and 'modules/patterns' not in ref_url:
                    # Old pattern location
                    suggested = ref_url.replace('prompt_eng/patterns', 'modules/patterns')
                    fixes[ref_url] = suggested
                elif 'modules/quality/' in ref_url and ref_url.endswith('.md'):
                    # Check if it's in system/quality now
                    basename = os.path.basename(ref_url)
                    if (self.root_path / '.claude' / 'system' / 'quality' / basename).exists():
                        fixes[ref_url] = ref_url.replace('modules/quality/', 'system/quality/')
                elif 'modules/security/' in ref_url and ref_url.endswith('.md'):
                    # Check if it's in system/security now
                    basename = os.path.basename(ref_url)
                    if (self.root_path / '.claude' / 'system' / 'security' / basename).exists():
                        fixes[ref_url] = ref_url.replace('modules/security/', 'system/security/')
                        
        return fixes
        
    def run(self):
        """Run the complete validation process"""
        print("Starting reference validation...")
        self.find_markdown_files()
        self.analyze_references()
        
        # Generate main report
        report_path = "internal/reports/reference_validation_report.md"
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        self.generate_report(report_path)
        print(f"\nReport generated: {report_path}")
        
        # Get fix suggestions
        fixes = self.suggest_fixes()
        if fixes:
            print("\nSuggested fixes:")
            for broken, fixed in list(fixes.items())[:10]:
                print(f"  {broken} → {fixed}")
            if len(fixes) > 10:
                print(f"  ... and {len(fixes) - 10} more")
                
        return len(self.broken_references) == 0

if __name__ == "__main__":
    validator = ReferenceValidator()
    success = validator.run()
    sys.exit(0 if success else 1)