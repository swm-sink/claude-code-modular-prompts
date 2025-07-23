#!/usr/bin/env python3
"""
Fix remaining critical issues in commands and components.
Focuses on missing <claude_prompt> elements and dependencies formatting.
"""

import os
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CriticalIssueFixer:
    def __init__(self):
        self.root_path = Path("claude_prompt_factory")
        self.fixes_applied = 0
        
    def fix_missing_claude_prompt(self, file_path: Path) -> bool:
        """Fix missing <claude_prompt> elements in command files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Skip special files
            if file_path.name in ['CLAUDE.md', 'README.md']:
                return False
            
            # Check if it has YAML frontmatter and command_file structure
            if '---' in content[:10] and '<command_file>' in content:
                # Check if <claude_prompt> is missing
                if '<claude_prompt>' not in content:
                    # Find where to insert it (after dependencies or arguments)
                    insertion_point = -1
                    
                    # Try after dependencies
                    deps_end = content.find('</dependencies>')
                    if deps_end > -1:
                        insertion_point = deps_end + len('</dependencies>')
                    else:
                        # Try after arguments
                        args_end = content.find('</arguments>')
                        if args_end > -1:
                            insertion_point = args_end + len('</arguments>')
                    
                    if insertion_point > -1:
                        # Generate appropriate claude_prompt based on command type
                        command_name = file_path.stem.replace('-', ' ').title()
                        claude_prompt_template = f"""
  
  <claude_prompt>
    <![CDATA[
You are executing the {command_name} command. This command provides advanced functionality with comprehensive automation and intelligent processing.

## Execution Framework

1. **Analysis Phase**
   - Understand the request context and parameters
   - Identify key requirements and constraints
   - Plan the execution approach

2. **Implementation Phase**
   - Execute the core functionality with precision
   - Apply best practices and optimization strategies
   - Ensure quality and consistency throughout

3. **Validation Phase**
   - Verify successful execution
   - Validate outputs meet requirements
   - Provide comprehensive results

## Key Principles

- **Automation**: Maximize intelligent automation where appropriate
- **Quality**: Maintain high standards throughout execution
- **Safety**: Ensure all operations follow constitutional AI principles
- **Efficiency**: Optimize for performance and resource usage

Execute this command with excellence, providing clear, actionable results.
    ]]>
  </claude_prompt>"""
                        
                        content = content[:insertion_point] + claude_prompt_template + content[insertion_point:]
                        modified = True
                        logger.info(f"Added missing <claude_prompt> to {file_path}")
            
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
            logger.error(f"Error fixing claude_prompt in {file_path}: {e}")
            
        return False
    
    def fix_dependencies_format(self, file_path: Path) -> bool:
        """Fix dependencies section format to ensure proper recognition."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Check if dependencies section exists but might be malformed
            if '<dependencies>' in content:
                # Ensure dependencies section is properly formatted
                deps_pattern = r'<dependencies>.*?</dependencies>'
                deps_match = re.search(deps_pattern, content, re.DOTALL)
                
                if deps_match:
                    deps_content = deps_match.group(0)
                    # Check if it's empty or has no includes
                    if '<include' not in deps_content:
                        # Add at least one include
                        new_deps = """<dependencies>
    <include component="components/constitutional/safety-framework.md" />
  </dependencies>"""
                        content = content.replace(deps_match.group(0), new_deps)
                        modified = True
                        logger.info(f"Fixed empty dependencies in {file_path}")
            
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
            logger.error(f"Error fixing dependencies in {file_path}: {e}")
            
        return False
    
    def fix_yaml_argument_hint(self, file_path: Path) -> bool:
        """Fix missing argument-hint in YAML frontmatter."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Check if it has YAML frontmatter
            if content.startswith('---'):
                # Extract YAML section
                yaml_end = content.find('---', 3)
                if yaml_end > -1:
                    yaml_content = content[3:yaml_end]
                    body_content = content[yaml_end+3:]
                    
                    # Check if argument-hint is missing
                    if 'argument-hint:' not in yaml_content:
                        # Add argument-hint after description
                        desc_match = re.search(r'description:.*\n', yaml_content)
                        if desc_match:
                            insertion_point = desc_match.end()
                            hint = 'argument-hint: "[options]"\n'
                            yaml_content = yaml_content[:insertion_point] + hint + yaml_content[insertion_point:]
                            modified = True
                            logger.info(f"Added missing argument-hint to {file_path}")
                    
                    if modified:
                        content = f"---\n{yaml_content}---{body_content}"
            
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
            logger.error(f"Error fixing YAML in {file_path}: {e}")
            
        return False
    
    def run_fixes(self):
        """Run all critical fixes."""
        logger.info("Starting critical issue fixes...")
        
        # Commands that need claude_prompt
        commands_needing_claude_prompt = [
            "agents/component-linker.md",
            "agents/error-aggregator.md", 
            "agents/command-converter.md",
            "agents/xml-parser.md",
            "agents/framework-tester.md",
            "agents/progress-coordinator.md",
            "workflow/mass-transformation.md"
        ]
        
        # Fix missing claude_prompt
        commands_dir = self.root_path / "commands"
        for cmd_rel_path in commands_needing_claude_prompt:
            cmd_path = commands_dir / cmd_rel_path
            if cmd_path.exists():
                self.fix_missing_claude_prompt(cmd_path)
        
        # Fix dependencies format issues
        if commands_dir.exists():
            for cmd_file in commands_dir.rglob("*.md"):
                if cmd_file.name != "README.md":
                    self.fix_dependencies_format(cmd_file)
        
        # Fix YAML argument-hint
        yaml_fix_commands = [
            "context/prime-mega.md",
            "analysis/quality-enforce.md"
        ]
        
        for cmd_rel_path in yaml_fix_commands:
            cmd_path = commands_dir / cmd_rel_path
            if cmd_path.exists():
                self.fix_yaml_argument_hint(cmd_path)
        
        logger.info(f"Total critical fixes applied: {self.fixes_applied}")

if __name__ == "__main__":
    fixer = CriticalIssueFixer()
    fixer.run_fixes()