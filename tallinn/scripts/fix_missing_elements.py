#!/usr/bin/env python3
"""
Fix missing required XML elements in components and commands.
This script adds missing <step>, <description>, <arguments>, and <dependencies> elements.
"""

import os
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MissingElementFixer:
    def __init__(self):
        self.root_path = Path("claude_prompt_factory")
        self.fixes_applied = 0
        
    def fix_component_missing_elements(self, file_path: Path) -> bool:
        """Fix missing <step> and <description> elements in component files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Check if it's a component file and needs step/description
            if '<prompt_component>' in content:
                # Check for missing <step> elements
                if '<step' not in content and '</prompt_component>' in content:
                    # Insert a basic step structure before closing tag
                    insertion_point = content.rfind('</prompt_component>')
                    if insertion_point > -1:
                        step_template = """  <step name="execute">
    <description>Execute the component functionality with comprehensive automation.</description>
    <execution>
      Component implementation executes with intelligent automation and validation.
    </execution>
  </step>
  
"""
                        content = content[:insertion_point] + step_template + content[insertion_point:]
                        modified = True
                        logger.info(f"Added missing <step> to {file_path}")
                
                # Check if description is missing at component level
                if '<description>' not in content[:200]:  # Check in the beginning
                    # Add description after prompt_component opening
                    match = re.search(r'<prompt_component[^>]*>', content)
                    if match:
                        insertion_point = match.end()
                        desc_template = f"\n  <description>Advanced component implementation for {file_path.stem}</description>\n"
                        content = content[:insertion_point] + desc_template + content[insertion_point:]
                        modified = True
                        logger.info(f"Added missing top-level <description> to {file_path}")
            
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
            logger.error(f"Error fixing component {file_path}: {e}")
            
        return False
    
    def fix_command_missing_elements(self, file_path: Path) -> bool:
        """Fix missing elements in command files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Skip special files
            if file_path.name in ['CLAUDE.md', 'README.md']:
                return False
            
            # Check if it's a command file
            if '---' in content[:10]:  # Has YAML frontmatter
                # Extract YAML and body
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    yaml_content = parts[1]
                    body_content = parts[2]
                    
                    # Check for missing <arguments> in body
                    if '<arguments>' not in body_content and '<command_file>' in body_content:
                        # Find insertion point after metadata
                        metadata_end = body_content.find('</metadata>')
                        if metadata_end > -1:
                            args_template = """
  
  <arguments>
    <argument name="target" type="string" required="false">
      <description>Target specification for command execution</description>
    </argument>
    <argument name="options" type="object" required="false">
      <description>Additional options for command configuration</description>
    </argument>
  </arguments>"""
                            insertion_point = metadata_end + len('</metadata>')
                            body_content = body_content[:insertion_point] + args_template + body_content[insertion_point:]
                            modified = True
                            logger.info(f"Added missing <arguments> to {file_path}")
                    
                    # Check for missing <dependencies>
                    if '<dependencies>' not in body_content and '<command_file>' in body_content:
                        # Find insertion point before steps or output
                        steps_start = body_content.find('<steps>')
                        if steps_start == -1:
                            steps_start = body_content.find('<claude_prompt>')
                        if steps_start == -1:
                            steps_start = body_content.find('<output>')
                        
                        if steps_start > -1:
                            deps_template = """
  
  <dependencies>
    <include component="components/constitutional/safety-framework.md" />
  </dependencies>"""
                            body_content = body_content[:steps_start] + deps_template + '\n  \n  ' + body_content[steps_start:]
                            modified = True
                            logger.info(f"Added missing <dependencies> to {file_path}")
                    
                    if modified:
                        content = f"---{yaml_content}---{body_content}"
            
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
            logger.error(f"Error fixing command {file_path}: {e}")
            
        return False
    
    def run_fixes(self):
        """Run all fixes across the codebase."""
        logger.info("Starting missing element fixes...")
        
        # Fix components
        components_dir = self.root_path / "components"
        if components_dir.exists():
            for comp_file in components_dir.rglob("*.md"):
                if comp_file.name != "README.md":
                    self.fix_component_missing_elements(comp_file)
        
        # Fix commands
        commands_dir = self.root_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.rglob("*.md"):
                if cmd_file.name != "README.md":
                    self.fix_command_missing_elements(cmd_file)
        
        logger.info(f"Total fixes applied: {self.fixes_applied}")

if __name__ == "__main__":
    fixer = MissingElementFixer()
    fixer.run_fixes()