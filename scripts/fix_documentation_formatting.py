#!/usr/bin/env python3
"""
Documentation Formatting Fixer
Fixes common formatting issues in markdown documentation files.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

def fix_horizontal_lines(content: str) -> str:
    """Remove excessive horizontal lines."""
    # Replace long dashes with nothing
    content = re.sub(r'────+', '', content)
    return content

def fix_xml_formatting(content: str) -> str:
    """Improve XML block formatting in markdown."""
    lines = content.split('\n')
    fixed_lines = []
    in_xml_block = False
    
    for i, line in enumerate(lines):
        # Check if we're starting an XML block outside code fences
        if (line.strip().startswith('<') and 
            line.strip().endswith('>') and 
            not line.strip().startswith('```') and
            i > 0 and not lines[i-1].strip().startswith('```')):
            
            # Check if this is the start of an XML block
            if not in_xml_block:
                # Add code fence before XML
                fixed_lines.append('```xml')
                in_xml_block = True
        
        fixed_lines.append(line)
        
        # Check if we need to close XML block
        if (in_xml_block and 
            line.strip().startswith('</') and 
            (i == len(lines) - 1 or 
             lines[i+1].strip() == '' or 
             lines[i+1].strip().startswith('#'))):
            fixed_lines.append('```')
            in_xml_block = False
    
    return '\n'.join(fixed_lines)

def fix_spacing(content: str) -> str:
    """Fix excessive spacing issues."""
    # Remove multiple consecutive blank lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # Fix spacing around headers
    content = re.sub(r'\n#+\s+', '\n\n# ', content)
    
    return content

def fix_code_blocks(content: str) -> str:
    """Ensure proper spacing in code blocks."""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Fix cramped XML attributes
        if '<' in line and '=' in line and not line.strip().startswith('```'):
            # Add spaces around attributes for readability
            line = re.sub(r'(\w+)=("[^"]*")', r'\1 = \2', line)
            
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def process_file(file_path: Path) -> Tuple[bool, str]:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes
        content = fix_horizontal_lines(content)
        content = fix_spacing(content)
        content = fix_code_blocks(content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Fixed formatting issues"
        else:
            return False, "No changes needed"
            
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main execution function."""
    project_root = Path.cwd()
    docs_dir = project_root / "docs"
    
    # Find all markdown files
    md_files = list(docs_dir.rglob("*.md"))
    
    # Also include top-level markdown files
    top_level_md = [
        project_root / "CLAUDE.md",
        project_root / "README.md", 
        project_root / "CONTRIBUTING.md"
    ]
    
    all_files = md_files + [f for f in top_level_md if f.exists()]
    
    print(f"Processing {len(all_files)} markdown files...")
    
    fixed_count = 0
    error_count = 0
    
    for file_path in all_files:
        try:
            was_fixed, message = process_file(file_path)
            if was_fixed:
                fixed_count += 1
                print(f"✅ Fixed: {file_path.relative_to(project_root)}")
            else:
                print(f"ℹ️  Skipped: {file_path.relative_to(project_root)} - {message}")
        except Exception as e:
            error_count += 1
            print(f"❌ Error: {file_path.relative_to(project_root)} - {str(e)}")
    
    print(f"\nSummary:")
    print(f"- Files processed: {len(all_files)}")
    print(f"- Files fixed: {fixed_count}")
    print(f"- Errors: {error_count}")

if __name__ == "__main__":
    main()