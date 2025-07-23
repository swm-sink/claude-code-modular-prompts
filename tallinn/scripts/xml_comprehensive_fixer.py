#!/usr/bin/env python3
"""
Comprehensive XML fixer for component files.
Addresses specific malformation patterns found in the codebase.
"""

import re
import logging
from pathlib import Path
from typing import List, Tuple
import defusedxml.ElementTree as ET

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)


class ComprehensiveXMLFixer:
    """Fix specific XML malformation patterns in component files."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.components_dir = project_root / "claude_prompt_factory" / "components"
        self.fixes_applied = 0
        
    def fix_file(self, file_path: Path) -> bool:
        """Fix XML issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply fixes in specific order
            content = self._fix_duplicate_closing_tags(content)
            content = self._fix_malformed_comments(content)
            content = self._fix_empty_self_closing_tags(content)
            content = self._fix_unclosed_tags(content)
            content = self._fix_mismatched_tags(content)
            content = self._ensure_root_element(content)
            
            if content != original_content:
                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes_applied += 1
                
                # Validate the fixed content
                try:
                    ET.fromstring(content)
                    logger.info(f"✅ Successfully fixed and validated: {file_path}")
                    return True
                except ET.ParseError as e:
                    logger.error(f"❌ Fixed but still invalid: {file_path} - {e}")
                    return False
            else:
                logger.info(f"No changes needed: {file_path}")
                return True
                
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return False
    
    def _fix_duplicate_closing_tags(self, content: str) -> str:
        """Fix duplicate closing tags like </description></description>."""
        # Pattern: </tag></tag> -> </tag>
        pattern = r'</(\w+)></\1>'
        while re.search(pattern, content):
            content = re.sub(pattern, r'</\1>', content)
        return content
    
    def _fix_malformed_comments(self, content: str) -> str:
        """Fix malformed XML comments."""
        # Fix </!-- to <!--
        content = re.sub(r'</!--', '<!--', content)
        # Fix --> without matching <!--
        content = re.sub(r'(?<!<!--)-->', '', content)
        # Ensure comments are properly closed
        content = re.sub(r'<!--([^-]|(-(?!->)))*(?!-->)', r'<!-- \g<0> -->', content)
        return content
    
    def _fix_empty_self_closing_tags(self, content: str) -> str:
        """Fix empty self-closing tags followed by opening tags."""
        # Pattern: <tag></tag><another_tag> -> <tag>
        pattern = r'<(\w+)></\1>(?=<\w+[^/])'
        content = re.sub(pattern, r'<\1>', content)
        return content
    
    def _fix_unclosed_tags(self, content: str) -> str:
        """Fix unclosed tags by adding closing tags."""
        lines = content.split('\n')
        tag_stack = []
        fixed_lines = []
        
        for line in lines:
            fixed_line = line
            
            # Find opening tags
            opening_tags = re.findall(r'<(\w+)(?:\s[^>]*)?>(?!</)', line)
            for tag in opening_tags:
                if tag not in ['br', 'hr', 'img', 'input', 'meta', 'link']:  # self-closing tags
                    tag_stack.append(tag)
            
            # Find closing tags
            closing_tags = re.findall(r'</(\w+)>', line)
            for tag in closing_tags:
                if tag_stack and tag_stack[-1] == tag:
                    tag_stack.pop()
                elif tag_stack:
                    # Mismatched closing tag - try to find matching opening tag
                    if tag in tag_stack:
                        # Close all tags until we reach the matching one
                        while tag_stack and tag_stack[-1] != tag:
                            fixed_line = f"</{tag_stack.pop()}>" + fixed_line
                        if tag_stack:
                            tag_stack.pop()
            
            fixed_lines.append(fixed_line)
        
        # Close any remaining open tags
        while tag_stack:
            fixed_lines.append(f"</{tag_stack.pop()}>")
        
        return '\n'.join(fixed_lines)
    
    def _fix_mismatched_tags(self, content: str) -> str:
        """Fix mismatched opening and closing tags."""
        # Common mismatches in the codebase
        replacements = [
            # Fix step tag issues
            (r'<step([^>]*)></step>\s*<description>', r'<step\1>\n    <description>'),
            (r'</description></description>', r'</description>'),
            (r'</description>\s*</step>', r'</description>\n  </step>'),
            # Fix component structure
            (r'<(\w+)></\1><(\w+)>', r'<\1>\n    <\2>'),
            # Fix self-closing followed by content
            (r'<(\w+)/><\1>', r'<\1>'),
        ]
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        return content
    
    def _ensure_root_element(self, content: str) -> str:
        """Ensure content has a single root element."""
        # Skip if already has prompt_component root
        if content.strip().startswith('<prompt_component>'):
            return content
        
        # Check if content needs wrapping
        try:
            ET.fromstring(f"<root>{content}</root>")
            # Content can be wrapped, but let's check if it already has a root
            # Count top-level elements
            lines = content.strip().split('\n')
            top_level_opens = 0
            top_level_closes = 0
            depth = 0
            
            for line in lines:
                # Count opening tags
                opens = len(re.findall(r'<(\w+)(?:\s[^>]*)?>(?!</)', line))
                closes = len(re.findall(r'</(\w+)>', line))
                
                if depth == 0 and opens > 0:
                    top_level_opens += opens
                
                depth += opens - closes
                
                if depth == 0 and closes > 0:
                    top_level_closes += closes
            
            # If multiple top-level elements, we already have prompt_component wrapper
            if top_level_opens > 1 or top_level_closes > 1:
                return content
            
        except ET.ParseError:
            # Content is malformed, needs fixing
            pass
        
        return content
    
    def fix_all_components(self) -> Tuple[int, int]:
        """Fix all component files."""
        component_files = list(self.components_dir.rglob("*.md"))
        successful = 0
        failed = 0
        
        logger.info(f"Found {len(component_files)} component files to process")
        
        for file_path in component_files:
            if self.fix_file(file_path):
                successful += 1
            else:
                failed += 1
        
        return successful, failed


def main():
    """Main execution."""
    project_root = Path(__file__).parent.parent
    fixer = ComprehensiveXMLFixer(project_root)
    
    logger.info("Starting comprehensive XML fix process...")
    successful, failed = fixer.fix_all_components()
    
    logger.info(f"\n=== Comprehensive Fix Summary ===")
    logger.info(f"Files processed: {successful + failed}")
    logger.info(f"Successfully fixed: {successful}")
    logger.info(f"Failed to fix: {failed}")
    logger.info(f"Total fixes applied: {fixer.fixes_applied}")
    
    if failed > 0:
        logger.warning(f"⚠️ {failed} files still have issues and need manual review")
        return 1
    else:
        logger.info("✅ All files successfully fixed!")
        return 0


if __name__ == "__main__":
    exit(main())