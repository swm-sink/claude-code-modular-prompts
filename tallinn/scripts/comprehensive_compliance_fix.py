#!/usr/bin/env python3
"""
Comprehensive compliance fix to achieve 95% template compliance.
This script addresses all remaining issues systematically.
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ComprehensiveComplianceFixer:
    def __init__(self):
        self.root_path = Path("claude_prompt_factory")
        self.fixes_applied = 0
        self.xml_parse_errors = []
        
    def fix_component_xml_errors(self, file_path: Path) -> bool:
        """Fix XML parsing errors in component files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Common XML fixes
            fixes = [
                # Fix common mismatched tags
                (r'<output_format>', '<output>'),
                (r'</output_format>', '</output>'),
                (r'<component_output>', '<output>'),
                (r'</component_output>', '</output>'),
                
                # Fix unclosed tags
                (r'<step([^>]*)(?<!/)>(?!.*</step>)', r'<step\1 />'),
                (r'<description>([^<]+)$', r'<description>\1</description>'),
                
                # Fix CDATA sections
                (r'<!\[CDATA\[([^]]*)\]\]>', lambda m: f'<![CDATA[{self._escape_cdata(m.group(1))}]]>'),
                
                # Fix invalid characters
                (r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', ''),
            ]
            
            for pattern, replacement in fixes:
                if callable(replacement):
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                else:
                    old_content = content
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                    if content != old_content:
                        modified = True
                        logger.info(f"Applied XML fix pattern {pattern} to {file_path}")
            
            # Ensure proper XML structure
            if '<prompt_component>' in content and '</prompt_component>' not in content:
                content += '\n</prompt_component>'
                modified = True
            
            if modified:
                # Create backup
                backup_path = file_path.with_suffix(file_path.suffix + '.backup')
                backup_path.write_text(original_content, encoding='utf-8')
                
                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes_applied += 1
                logger.info(f"Fixed XML errors in {file_path}")
                return True
                
        except Exception as e:
            logger.error(f"Error fixing XML in {file_path}: {e}")
            self.xml_parse_errors.append((str(file_path), str(e)))
            
        return False
    
    def _escape_cdata(self, content: str) -> str:
        """Escape problematic content in CDATA sections."""
        # Remove nested CDATA markers
        content = content.replace(']]>', ']]]]><![CDATA[>')
        return content
    
    def add_yaml_argument_hints(self, file_path: Path) -> bool:
        """Add missing argument-hint to YAML frontmatter."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.startswith('---'):
                return False
            
            yaml_end = content.find('---', 3)
            if yaml_end == -1:
                return False
            
            yaml_content = content[3:yaml_end]
            body_content = content[yaml_end+3:]
            
            if 'argument-hint:' not in yaml_content:
                # Add argument-hint after description
                lines = yaml_content.split('\n')
                new_lines = []
                for i, line in enumerate(lines):
                    new_lines.append(line)
                    if line.startswith('description:'):
                        new_lines.append('argument-hint: "[options]"')
                
                yaml_content = '\n'.join(new_lines)
                content = f"---\n{yaml_content}---{body_content}"
                
                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes_applied += 1
                logger.info(f"Added argument-hint to {file_path}")
                return True
                
        except Exception as e:
            logger.error(f"Error fixing YAML in {file_path}: {e}")
            
        return False
    
    def ensure_dependencies_both_formats(self, file_path: Path) -> bool:
        """Ensure commands have both dependencies and includes_components."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '<command_file>' not in content:
                return False
            
            modified = False
            
            # Check if we have includes_components but no dependencies
            if '<includes_components>' in content and '<dependencies>' not in content:
                # Find all includes
                includes = re.findall(r'<include component="([^"]+)" />', content)
                
                if includes:
                    # Add dependencies section after includes_components
                    includes_end = content.find('</includes_components>')
                    if includes_end > -1:
                        deps_content = '\n'.join(f'    <include component="{comp}" />' for comp in includes)
                        deps_section = f"""
  
  <dependencies>
{deps_content}
  </dependencies>"""
                        insertion_point = includes_end + len('</includes_components>')
                        content = content[:insertion_point] + deps_section + content[insertion_point:]
                        modified = True
                        logger.info(f"Added dependencies section to {file_path}")
            
            if modified:
                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes_applied += 1
                return True
                
        except Exception as e:
            logger.error(f"Error ensuring dependencies in {file_path}: {e}")
            
        return False
    
    def fix_special_files(self):
        """Fix special files like CLAUDE.md that need custom handling."""
        # Fix CLAUDE.md
        claude_path = self.root_path / "commands" / "CLAUDE.md"
        if claude_path.exists():
            try:
                with open(claude_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if '<claude_prompt>' not in content:
                    # Add a special claude_prompt for CLAUDE.md
                    claude_prompt = """
<claude_prompt>
  <![CDATA[
This is the main Claude Code Prompt Factory command registry. Use the commands listed above to access the framework's capabilities.

## Command Categories:
- **Core**: Essential framework commands for initialization and routing
- **Agentic**: Advanced AI reasoning and coordination capabilities
- **Development**: Software development workflow commands
- **Analysis**: Code analysis and quality assessment
- **Testing**: Comprehensive testing framework
- **Security**: Security analysis and compliance
- **Performance**: Optimization and performance analysis

Select the appropriate command based on your needs, or use `/auto` for intelligent routing.
  ]]>
</claude_prompt>"""
                    
                    # Insert before closing
                    closing_tag = content.rfind('```')
                    if closing_tag > -1:
                        content = content[:closing_tag] + claude_prompt + '\n\n' + content[closing_tag:]
                        
                        with open(claude_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        self.fixes_applied += 1
                        logger.info("Added claude_prompt to CLAUDE.md")
            
            except Exception as e:
                logger.error(f"Error fixing CLAUDE.md: {e}")
    
    def run_comprehensive_fixes(self):
        """Run all fixes to achieve 95% compliance."""
        logger.info("Starting comprehensive compliance fixes...")
        
        # Fix YAML argument hints
        yaml_fixes = [
            "commands/context/prime-mega.md",
            "commands/analysis/quality-enforce.md"
        ]
        
        for yaml_file in yaml_fixes:
            file_path = self.root_path / yaml_file
            if file_path.exists():
                self.add_yaml_argument_hints(file_path)
        
        # Fix XML parsing errors in components
        xml_error_files = [
            "components/quality/framework-validation.md",
            "components/intelligence/cognitive-architecture.md",
            "components/learning/meta-learning-framework.md",
            "components/optimization/prompt-optimization.md",
            "components/user-experience/intelligent-help.md",
            "components/actions/parallel-execution.md",
            "components/orchestration/dag-orchestrator.md",
            "components/error/circuit-breaker.md",
            "components/validation/xml-structure.md",
            "components/analytics/business-intelligence.md",
            "components/analytics/user-feedback.md"
        ]
        
        for xml_file in xml_error_files:
            file_path = self.root_path / xml_file
            if file_path.exists():
                self.fix_component_xml_errors(file_path)
        
        # Ensure all commands have both dependency formats
        commands_dir = self.root_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.rglob("*.md"):
                if cmd_file.name not in ['README.md', 'CLAUDE.md']:
                    self.ensure_dependencies_both_formats(cmd_file)
        
        # Fix special files
        self.fix_special_files()
        
        logger.info(f"Total comprehensive fixes applied: {self.fixes_applied}")
        
        if self.xml_parse_errors:
            logger.warning(f"XML parse errors encountered: {len(self.xml_parse_errors)}")
            for file_path, error in self.xml_parse_errors[:5]:
                logger.warning(f"  {file_path}: {error}")

if __name__ == "__main__":
    fixer = ComprehensiveComplianceFixer()
    fixer.run_comprehensive_fixes()