#!/usr/bin/env python3
"""
Deep structural XML fixer that addresses root causes of persistent XML errors.
"""

import re
import logging
from pathlib import Path
from typing import List, Tuple, Dict
import defusedxml.ElementTree as ET

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)


class DeepStructuralXMLFixer:
    """Fix deep structural XML issues in component files."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.components_dir = project_root / "claude_prompt_factory" / "components"
        self.fixes_applied = 0
        
    def fix_file(self, file_path: Path) -> bool:
        """Fix XML issues in a single file with deep structural fixes."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply fixes in specific order (order matters!)
            content = self._fix_double_comment_openings(content)
            content = self._fix_unclosed_comments(content)
            content = self._fix_unescaped_ampersands(content)
            content = self._fix_orphaned_tags(content)
            content = self._ensure_proper_structure(content)
            
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
                    # Log more details for debugging
                    self._log_error_context(content, e)
                    return False
            else:
                # Still try to validate
                try:
                    ET.fromstring(content)
                    logger.info(f"✅ Already valid: {file_path}")
                    return True
                except ET.ParseError as e:
                    logger.error(f"❌ No changes made but invalid: {file_path} - {e}")
                    return False
                
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return False
    
    def _fix_double_comment_openings(self, content: str) -> str:
        """Fix double comment openings like <!-- <!--."""
        # Fix patterns like: <!-- <!-- text <!-- text
        pattern = r'<!-- <!-- ([^<]+)<!-- \1'
        content = re.sub(pattern, r'<!-- \1', content)
        
        # Fix simpler double openings
        content = re.sub(r'<!-- <!--', '<!--', content)
        
        # Fix triple or more openings
        while '<!-- <!-- <!--' in content:
            content = content.replace('<!-- <!-- <!--', '<!--')
        
        return content
    
    def _fix_unclosed_comments(self, content: str) -> str:
        """Fix unclosed XML comments."""
        lines = content.split('\n')
        fixed_lines = []
        in_comment = False
        comment_start_line = -1
        
        for i, line in enumerate(lines):
            # Check for comment starts
            if '<!--' in line and '-->' not in line:
                in_comment = True
                comment_start_line = i
            elif '-->' in line and in_comment:
                in_comment = False
                comment_start_line = -1
            
            # If we're at the end of a logical section and still in a comment, close it
            if in_comment and (
                line.strip() == '' or 
                line.strip().startswith('<') and not line.strip().startswith('<!--') or
                i == len(lines) - 1
            ):
                # Check if this line should close the comment
                if i > comment_start_line + 1:  # Don't close immediately
                    if line.strip() == '':
                        # Add closing before empty line
                        if fixed_lines and not fixed_lines[-1].strip().endswith('-->'):
                            fixed_lines[-1] = fixed_lines[-1].rstrip() + ' -->'
                            in_comment = False
                    elif i == len(lines) - 1:
                        # Last line, must close
                        line = line.rstrip() + ' -->'
                        in_comment = False
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines)
    
    def _fix_unescaped_ampersands(self, content: str) -> str:
        """Fix unescaped ampersands, especially in 'W&B'."""
        # Fix W&B specifically
        content = re.sub(r'W&B(?![a-zA-Z])', r'W&amp;B', content)
        
        # Fix other common ampersands (but not in URLs or already escaped)
        # This regex looks for & not followed by amp; or in URLs
        content = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)(?![a-zA-Z]+://)', r'&amp;', content)
        
        return content
    
    def _fix_orphaned_tags(self, content: str) -> str:
        """Fix orphaned closing tags."""
        # Track tag stack to find orphaned tags
        lines = content.split('\n')
        fixed_lines = []
        tag_stack = []
        
        for line in lines:
            # Find all tags in the line
            opening_tags = re.findall(r'<(\w+)(?:\s[^>]*)?>(?!</)', line)
            closing_tags = re.findall(r'</(\w+)>', line)
            
            # Process opening tags
            for tag in opening_tags:
                if tag not in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                    tag_stack.append(tag)
            
            # Check closing tags
            new_line = line
            for tag in closing_tags:
                if tag_stack and tag == tag_stack[-1]:
                    # Matching tag, pop it
                    tag_stack.pop()
                elif tag in tag_stack:
                    # Tag exists but not at top - we have nesting issues
                    # Pop until we find it
                    while tag_stack and tag_stack[-1] != tag:
                        tag_stack.pop()
                    if tag_stack:
                        tag_stack.pop()
                else:
                    # Orphaned closing tag - remove it
                    logger.warning(f"Removing orphaned closing tag: </{tag}>")
                    new_line = new_line.replace(f'</{tag}>', '')
            
            fixed_lines.append(new_line)
        
        return '\n'.join(fixed_lines)
    
    def _ensure_proper_structure(self, content: str) -> str:
        """Ensure the content has proper XML structure."""
        # Remove any duplicate </prompt_component> tags at the end
        content = re.sub(r'(</prompt_component>\s*)+$', '</prompt_component>', content.strip())
        
        # Ensure we have opening and closing prompt_component tags
        if not content.strip().startswith('<prompt_component>'):
            logger.warning("Missing opening <prompt_component> tag")
        
        if not content.strip().endswith('</prompt_component>'):
            logger.warning("Missing closing </prompt_component> tag")
            # Don't add it automatically as it might already exist somewhere
        
        return content
    
    def _log_error_context(self, content: str, error: ET.ParseError):
        """Log context around the error for debugging."""
        if hasattr(error, 'position'):
            line, column = error.position
            lines = content.split('\n')
            if 0 <= line - 1 < len(lines):
                logger.debug(f"Error at line {line}, column {column}")
                logger.debug(f"Line content: {lines[line-1]}")
                if line - 2 >= 0:
                    logger.debug(f"Previous line: {lines[line-2]}")
                if line < len(lines):
                    logger.debug(f"Next line: {lines[line]}")
    
    def fix_all_components(self) -> Tuple[int, int]:
        """Fix all component files with deep structural fixes."""
        component_files = list(self.components_dir.rglob("*.md"))
        # Skip README files
        component_files = [f for f in component_files if f.name != "README.md"]
        
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
    fixer = DeepStructuralXMLFixer(project_root)
    
    logger.info("Starting deep structural XML fix process...")
    successful, failed = fixer.fix_all_components()
    
    logger.info(f"\n=== Deep Structural Fix Summary ===")
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