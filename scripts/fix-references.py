#!/usr/bin/env python3
"""
Fix broken references in markdown files based on validation report
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class ReferenceFixer:
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path).resolve()
        self.fixes_applied = 0
        self.files_modified = set()
        
        # Define reference mappings based on file moves
        self.reference_mappings = {
            # Quality modules moved to system/quality
            '.claude/modules/quality/universal-quality-gates.md': '.claude/system/quality/universal-quality-gates.md',
            '.claude/modules/quality/tdd.md': '.claude/system/quality/tdd.md',
            '.claude/modules/quality/test-coverage.md': '.claude/system/quality/test-coverage.md',
            '.claude/modules/quality/security-gate-verification.md': '.claude/system/quality/security-gate-verification.md',
            '.claude/modules/quality/tdd-verification.md': '.claude/system/quality/tdd-verification.md',
            
            # Security modules moved to system/security
            '.claude/modules/security/threat-modeling.md': '.claude/system/security/threat-modeling.md',
            
            # Pattern moved from prompt_eng to modules
            '.claude/prompt_eng/patterns/': '.claude/modules/patterns/',
            
            # Add more mappings as needed
        }
        
    def fix_reference(self, file_path: Path, old_ref: str, line_num: int) -> str:
        """Fix a single reference based on context"""
        # Remove anchor if present
        ref_without_anchor = old_ref.split('#')[0]
        
        # Handle relative paths
        if ref_without_anchor.startswith(('../', './')):
            # Convert to absolute from file location
            abs_ref = (file_path.parent / ref_without_anchor).resolve()
            try:
                rel_to_root = abs_ref.relative_to(self.root_path)
                check_ref = str(rel_to_root)
            except ValueError:
                check_ref = ref_without_anchor
        else:
            check_ref = ref_without_anchor
            
        # Check mappings
        for old_path, new_path in self.reference_mappings.items():
            if old_path in check_ref:
                return old_ref.replace(old_path, new_path)
            # Handle partial matches
            if old_path.replace('.claude/', '') in check_ref and '.claude/' not in check_ref:
                # Add .claude/ prefix if missing
                partial = old_path.replace('.claude/', '')
                if partial in check_ref:
                    return old_ref.replace(partial, new_path)
                    
        # Special cases for quality and security modules
        if 'modules/quality/' in old_ref and not old_ref.startswith('.claude/'):
            # Check if file exists in system/quality
            basename = os.path.basename(old_ref)
            if (self.root_path / '.claude' / 'system' / 'quality' / basename).exists():
                return old_ref.replace('modules/quality/', '.claude/system/quality/')
                
        if 'modules/security/' in old_ref and not old_ref.startswith('.claude/'):
            # Check if file exists in system/security
            basename = os.path.basename(old_ref)
            if (self.root_path / '.claude' / 'system' / 'security' / basename).exists():
                return old_ref.replace('modules/security/', '.claude/system/security/')
                
        # Fix references that are missing .claude prefix
        if old_ref.startswith('modules/') and not old_ref.startswith('.claude/'):
            # Don't add .claude if the path already has ../.claude
            if '../.claude' in str(file_path.parent / old_ref):
                return old_ref
            return '.claude/' + old_ref
            
        # Fix CLAUDE.md canonical sources
        if old_ref == 'quality/universal-quality-gates.md':
            return '.claude/system/quality/universal-quality-gates.md'
        if old_ref == 'quality/tdd.md':
            return '.claude/system/quality/tdd.md'
        if old_ref == 'patterns/module-composition-framework.md':
            return '.claude/modules/patterns/module-composition-framework.md'
        if old_ref == 'patterns/duplication-prevention.md':
            return '.claude/modules/patterns/duplication-prevention.md'
            
        return None
        
    def fix_file(self, file_path: Path, broken_refs: List[Tuple[str, int, str]]) -> int:
        """Fix all broken references in a file"""
        fixes = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            modified = False
            for ref_url, line_num, ref_text in broken_refs:
                fixed_ref = self.fix_reference(file_path, ref_url, line_num)
                if fixed_ref and fixed_ref != ref_url:
                    # Find and replace in the specific line
                    line_idx = line_num - 1
                    if line_idx < len(lines):
                        old_line = lines[line_idx]
                        new_line = old_line.replace(ref_url, fixed_ref)
                        if new_line != old_line:
                            lines[line_idx] = new_line
                            modified = True
                            fixes += 1
                            print(f"  Fixed: {ref_url} → {fixed_ref}")
                            
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                self.files_modified.add(file_path)
                
        except Exception as e:
            print(f"Error fixing {file_path}: {e}")
            
        return fixes
        
    def run(self):
        """Run the reference fixing process"""
        print("Starting reference fixing...")
        
        # Parse the validation report
        report_path = self.root_path / "internal/reports/reference_validation_report.md"
        if not report_path.exists():
            print("Error: Validation report not found. Run validate-references.py first.")
            return False
            
        broken_refs = self.parse_report(report_path)
        
        # Fix references
        for file_path, refs in broken_refs.items():
            print(f"\nFixing {file_path}...")
            fixes = self.fix_file(self.root_path / file_path, refs)
            self.fixes_applied += fixes
            
        print(f"\n Summary:")
        print(f"  Files modified: {len(self.files_modified)}")
        print(f"  References fixed: {self.fixes_applied}")
        
        return True
        
    def parse_report(self, report_path: Path) -> Dict[str, List[Tuple[str, int, str]]]:
        """Parse the validation report to extract broken references"""
        broken_refs = {}
        current_file = None
        
        with open(report_path, 'r') as f:
            lines = f.readlines()
            
        in_broken_section = False
        for line in lines:
            if line.strip() == "## Broken References by File":
                in_broken_section = True
                continue
            elif line.startswith("## ") and in_broken_section:
                break
                
            if in_broken_section:
                if line.startswith("### "):
                    current_file = line[4:].strip()
                    broken_refs[current_file] = []
                elif line.startswith("- Line ") and current_file:
                    # Parse: - Line 289: `[Full Threat Model](evidence/security/{task_id}/threat-model.json)` → `evidence/security/{task_id}/threat-model.json`
                    match = re.match(r'- Line (\d+): `([^`]+)` → `([^`]+)`', line)
                    if match:
                        line_num = int(match.group(1))
                        ref_text = match.group(2)
                        ref_url = match.group(3)
                        broken_refs[current_file].append((ref_url, line_num, ref_text))
                        
        return broken_refs

if __name__ == "__main__":
    fixer = ReferenceFixer()
    success = fixer.run()
    sys.exit(0 if success else 1)