#!/usr/bin/env python3
"""
Fix documentation references that point to non-existent files
"""

import os
import re
from pathlib import Path

def fix_missing_doc_references():
    """Fix references to documentation that doesn't exist"""
    
    # These are references to files that should be removed or updated
    doc_fixes = {
        # Files that don't exist and should be removed
        'docs/CONTRIBUTING.md': {
            'CLAUDE.md': '../CLAUDE.md'  # Fix relative path
        },
        'docs/getting-started/first-commands.md': {
            '../user-guide/workflows/advanced-patterns.md': None,  # Remove - doesn't exist
            '../advanced/performance-optimization.md': None  # Remove - doesn't exist
        },
        'docs/getting-started/installation.md': {
            '../user-guide/customization/team-setup.md': None,  # Remove - doesn't exist
            '../advanced/performance-optimization.md': None  # Remove - doesn't exist
        },
        'docs/getting-started/quick-start.md': {
            '../user-guide/workflows/advanced-patterns.md': None,  # Remove - doesn't exist
            '../user-guide/customization/team-setup.md': None  # Remove - doesn't exist
        },
        'docs/guides/USER_GUIDE.md': {
            'docs/GETTING_STARTED.md': '../getting-started/quick-start.md',  # Fix path
            'docs/DOCUMENTATION_INDEX.md': '../README.md'  # Fix path
        },
        'docs/user-guide/workflows/common-patterns.md': {
            'advanced-patterns.md': None,  # Remove - doesn't exist
            'team-patterns.md': None,  # Remove - doesn't exist
            'production-patterns.md': None  # Remove - doesn't exist
        },
        'docs/user-guide/customization/advanced-config.md': {
            '../../advanced/performance-optimization.md': None  # Remove - doesn't exist
        }
    }
    
    # Files that reference things that should be fixed
    reference_fixes = {
        # Evidence directories are placeholders
        '.claude/system/quality/security-gate-verification.md': {
            'evidence/': '# Evidence directory (created at runtime): evidence/'
        },
        '.claude/system/quality/tdd-verification.md': {
            'evidence/': '# Evidence directory (created at runtime): evidence/'
        },
        # Modules that moved
        'examples/workflows/long-running-session/README.md': {
            '../../../.claude/modules/development/project-management.md': None,
            '../../../.claude/modules/development/progress-tracking.md': None,
            '../../../.claude/modules/development/team-coordination.md': None,
            '../../../.claude/modules/development/validation/': None,
        },
        'examples/workflows/multi-agent-development/README.md': {
            '../../../.claude/modules/development/testing/': None,
            '../../../.claude/modules/development/validation/': None,
        }
    }
    
    fixes_applied = 0
    
    # Apply documentation fixes
    for file_path, fixes in doc_fixes.items():
        if not Path(file_path).exists():
            continue
            
        with open(file_path, 'r') as f:
            content = f.read()
            
        original_content = content
        for old_ref, new_ref in fixes.items():
            if new_ref is None:
                # Remove the reference
                pattern = r'\[([^\]]+)\]\(' + re.escape(old_ref) + r'\)'
                content = re.sub(pattern, r'\1', content)
            else:
                # Replace with new reference
                content = content.replace(f']({old_ref})', f']({new_ref})')
                
        if content != original_content:
            with open(file_path, 'w') as f:
                f.write(content)
            fixes_applied += 1
            print(f"Fixed {file_path}")
            
    # Apply reference pattern fixes
    for file_path, fixes in reference_fixes.items():
        if not Path(file_path).exists():
            continue
            
        with open(file_path, 'r') as f:
            content = f.read()
            
        original_content = content
        for old_ref, new_ref in fixes.items():
            if 'evidence/' in old_ref and new_ref and new_ref.startswith('#'):
                # Replace evidence links with comments
                pattern = r'\[([^\]]+)\]\(' + re.escape(old_ref) + r'[^)]*\)'
                content = re.sub(pattern, new_ref, content)
            elif new_ref is None:
                # Remove the reference line entirely
                lines = content.split('\n')
                new_lines = []
                for line in lines:
                    if old_ref not in line:
                        new_lines.append(line)
                content = '\n'.join(new_lines)
                
        if content != original_content:
            with open(file_path, 'w') as f:
                f.write(content)
            fixes_applied += 1
            print(f"Fixed {file_path}")
            
    print(f"\nTotal files fixed: {fixes_applied}")
    
if __name__ == "__main__":
    fix_missing_doc_references()