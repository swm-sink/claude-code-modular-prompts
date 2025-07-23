#!/usr/bin/env python3
"""
Fix dependencies format to match validator expectations.
Converts <dependencies> to <includes_components> format.
"""

import os
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DependenciesFormatFixer:
    def __init__(self):
        self.root_path = Path("claude_prompt_factory")
        self.fixes_applied = 0
        
    def fix_dependencies_format(self, file_path: Path) -> bool:
        """Convert dependencies to includes_components format."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Find dependencies section
            deps_pattern = r'<dependencies>\s*(.*?)\s*</dependencies>'
            deps_match = re.search(deps_pattern, content, re.DOTALL)
            
            if deps_match:
                deps_content = deps_match.group(1)
                
                # Extract all include components
                includes = re.findall(r'<include component="([^"]+)" />', deps_content)
                
                if includes:
                    # Build includes_components section
                    components_list = '\n'.join(f'    <component>{comp}</component>' for comp in includes)
                    new_section = f"""<includes_components>
{components_list}
  </includes_components>"""
                    
                    # Replace dependencies with includes_components
                    content = content.replace(deps_match.group(0), new_section)
                    modified = True
                    logger.info(f"Converted dependencies to includes_components in {file_path}")
            
            # Also add includes_components if missing but has include directives
            elif '<include component=' in content and '<includes_components>' not in content:
                # Find all includes
                includes = re.findall(r'<include component="([^"]+)" />', content)
                
                if includes:
                    # Build includes_components section
                    components_list = '\n'.join(f'    <component>{comp}</component>' for comp in includes)
                    includes_section = f"""
  
  <includes_components>
{components_list}
  </includes_components>"""
                    
                    # Find insertion point (before closing tag)
                    if '<command_file>' in content:
                        closing_tag = '</command_file>'
                    else:
                        closing_tag = '</prompt_component>'
                    
                    insertion_point = content.rfind(closing_tag)
                    if insertion_point > -1:
                        content = content[:insertion_point] + includes_section + '\n' + content[insertion_point:]
                        modified = True
                        logger.info(f"Added includes_components section to {file_path}")
            
            if modified:
                # Create backup
                backup_path = file_path.with_suffix(file_path.suffix + '.backup')
                backup_path.write_text(original_content, encoding='utf-8')
                
                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes_applied += 1
                return True
                
        except Exception as e:
            logger.error(f"Error fixing dependencies format in {file_path}: {e}")
            
        return False
    
    def run_fixes(self):
        """Run fixes across all command files."""
        logger.info("Starting dependencies format fixes...")
        
        # Fix commands
        commands_dir = self.root_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.rglob("*.md"):
                if cmd_file.name not in ['README.md', 'CLAUDE.md']:
                    self.fix_dependencies_format(cmd_file)
        
        logger.info(f"Total dependencies format fixes applied: {self.fixes_applied}")

if __name__ == "__main__":
    fixer = DependenciesFormatFixer()
    fixer.run_fixes()