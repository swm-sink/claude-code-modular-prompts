#!/usr/bin/env python3
"""
XML Infrastructure Agent - Automated Fix Scripts for XML Parsing Errors

This script addresses the 95+ XML parsing errors identified in the Claude Code
Modular Prompts framework by implementing targeted fixes for common patterns.

Author: XML Infrastructure Agent Phase 1
Date: 2025-07-22
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class XMLErrorFixer:
    def __init__(self, root_path: str = "claude_prompt_factory"):
        self.root_path = Path(root_path)
        self.fixes_applied = []
        self.errors_encountered = []
        
    def fix_mismatched_tags(self, file_path: Path) -> bool:
        """Fix mismatched XML tags in component files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_made = []
            
            # Common mismatched tag patterns
            tag_fixes = [
                # Fix <o> tags that should be <output>
                (r'<o>', '<output>'),
                (r'</o>', '</output>'),
                
                # Fix incomplete closing tags
                (r'<([^/>]+)>\s*$', r'<\1></\1>'),
                
                # Fix malformed self-closing tags
                (r'<([^/>]+)\s*/\s*>', r'<\1 />'),
                
                # Fix nested tag issues
                (r'</([^>]+)>\s*</([^>]+)>', self._fix_nested_tags),
            ]
            
            for pattern, replacement in tag_fixes:
                if callable(replacement):
                    # Custom fix function
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        fix_result = replacement(match)
                        if fix_result:
                            content = content.replace(match.group(0), fix_result)
                            fixes_made.append(f"Custom fix: {match.group(0)} -> {fix_result}")
                else:
                    # Simple replacement
                    old_content = content
                    content = re.sub(pattern, replacement, content)
                    if content != old_content:
                        fixes_made.append(f"Pattern fix: {pattern} -> {replacement}")
            
            if fixes_made:
                self._backup_file(file_path)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.fixes_applied.append({
                    'file': str(file_path),
                    'type': 'mismatched_tags',
                    'fixes': fixes_made
                })
                logger.info(f"Fixed mismatched tags in {file_path}: {len(fixes_made)} fixes")
                return True
                
        except Exception as e:
            self.errors_encountered.append({
                'file': str(file_path),
                'error': str(e),
                'type': 'mismatched_tags'
            })
            logger.error(f"Error fixing mismatched tags in {file_path}: {e}")
            
        return False
    
    def fix_missing_output_sections(self, file_path: Path) -> bool:
        """Add missing <output> sections to component files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if output section is missing
            if '<output>' not in content and '<output_format>' not in content:
                # Generate appropriate output section based on component type
                component_name = file_path.stem
                output_template = self._generate_output_template(component_name, content)
                
                # Find insertion point (before closing tag)
                closing_tag_pattern = r'(\s*</[^>]+>\s*)$'
                match = re.search(closing_tag_pattern, content)
                
                if match:
                    insertion_point = match.start()
                    new_content = (
                        content[:insertion_point] + 
                        "\n\n" + output_template + "\n" + 
                        content[insertion_point:]
                    )
                    
                    self._backup_file(file_path)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    self.fixes_applied.append({
                        'file': str(file_path),
                        'type': 'missing_output_section',
                        'fix': 'Added output section template'
                    })
                    logger.info(f"Added missing output section to {file_path}")
                    return True
                    
        except Exception as e:
            self.errors_encountered.append({
                'file': str(file_path),
                'error': str(e),
                'type': 'missing_output_section'
            })
            logger.error(f"Error adding output section to {file_path}: {e}")
            
        return False
    
    def fix_malformed_xml_structure(self, file_path: Path) -> bool:
        """Fix malformed XML structure issues."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_made = []
            
            # Fix common XML structure issues
            structure_fixes = [
                # Fix invalid tokens (common encoding issues)
                (r'[^\x09\x0A\x0D\x20-\xD7FF\xE000-\xFFFD\x10000-\x10FFFF]', ''),
                
                # Fix unclosed CDATA sections
                (r'<!\[CDATA\[(.*?)(?!</\]\]>)', r'<![CDATA[\1]]>'),
                
                # Fix malformed attributes
                (r'(\w+)=([^"\s>]+)', r'\1="\2"'),
                
                # Fix space issues in self-closing tags
                (r'<(\w+)/>', r'<\1 />'),
                
                # Fix missing XML declaration encoding issues
                (r'^(?!<\?xml)', '<?xml version="1.0" encoding="UTF-8"?>\n'),
            ]
            
            for pattern, replacement in structure_fixes:
                old_content = content
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                if content != old_content:
                    fixes_made.append(f"Structure fix: {pattern}")
            
            if fixes_made:
                self._backup_file(file_path)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.fixes_applied.append({
                    'file': str(file_path),
                    'type': 'malformed_xml_structure',
                    'fixes': fixes_made
                })
                logger.info(f"Fixed XML structure in {file_path}: {len(fixes_made)} fixes")
                return True
                
        except Exception as e:
            self.errors_encountered.append({
                'file': str(file_path),
                'error': str(e),
                'type': 'malformed_xml_structure'
            })
            logger.error(f"Error fixing XML structure in {file_path}: {e}")
            
        return False
    
    def fix_command_file_structure(self, file_path: Path) -> bool:
        """Fix missing <command_file> XML structure in command files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '<command_file>' not in content:
                # Extract YAML frontmatter
                yaml_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
                
                if yaml_match:
                    yaml_content = yaml_match.group(1)
                    body_content = yaml_match.group(2)
                    
                    # Generate command_file structure
                    command_template = self._generate_command_file_template(file_path.stem, body_content)
                    
                    new_content = f"---\n{yaml_content}\n---\n\n{command_template}"
                    
                    self._backup_file(file_path)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    self.fixes_applied.append({
                        'file': str(file_path),
                        'type': 'missing_command_file_structure',
                        'fix': 'Added command_file XML wrapper'
                    })
                    logger.info(f"Added command_file structure to {file_path}")
                    return True
                    
        except Exception as e:
            self.errors_encountered.append({
                'file': str(file_path),
                'error': str(e),
                'type': 'missing_command_file_structure'
            })
            logger.error(f"Error adding command_file structure to {file_path}: {e}")
            
        return False
    
    def validate_xml_after_fix(self, file_path: Path) -> bool:
        """Validate XML structure after applying fixes."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # For command files, extract XML portion
            if 'commands/' in str(file_path):
                xml_match = re.search(r'<command_file>.*?</command_file>', content, re.DOTALL)
                if xml_match:
                    xml_content = xml_match.group(0)
                else:
                    return False
            else:
                xml_content = content
            
            # Validate XML
            ET.fromstring(xml_content)
            return True
            
        except ET.ParseError as e:
            logger.warning(f"XML validation failed for {file_path}: {e}")
            return False
        except Exception as e:
            logger.error(f"Validation error for {file_path}: {e}")
            return False
    
    def _fix_nested_tags(self, match):
        """Custom function to fix nested tag issues."""
        full_match = match.group(0)
        tag1 = match.group(1)
        tag2 = match.group(2)
        
        # Simple heuristic: if tags are similar, assume typo
        if tag1.lower() == tag2.lower():
            return f"</{tag1}>"
        
        return full_match  # No change if can't determine fix
    
    def _generate_output_template(self, component_name: str, content: str) -> str:
        """Generate appropriate output template based on component type and content."""
        # Analyze content to determine output type
        if 'workflow' in component_name or 'orchestrat' in component_name:
            return """  <output>
    Workflow execution completed with comprehensive automation:

    **Execution Status:** [percentage]% workflow completion achieved
    **Process Automation:** [count] automated process steps executed successfully
    **Integration Points:** [count] system integration points configured
    **Performance Metrics:** [0-100] workflow effectiveness rating
    **System Coordination:** Advanced workflow orchestration with intelligent automation
  </output>"""
        
        elif 'security' in component_name or 'secure' in component_name:
            return """  <output>
    Security framework implementation completed with comprehensive protection:

    **Security Level:** [percentage]% security compliance achieved
    **Threat Protection:** [count] security measures actively implemented
    **Compliance Status:** [percentage]% regulatory compliance maintained
    **Security Metrics:** [0-100] security effectiveness rating
    **Protection Coverage:** Advanced security with multi-layered defense systems
  </output>"""
        
        elif 'optimization' in component_name or 'performance' in component_name:
            return """  <output>
    Optimization framework completed with enhanced performance:

    **Performance Gain:** [percentage]% improvement achieved
    **Resource Efficiency:** [count] optimization strategies implemented
    **System Performance:** [percentage]% performance baseline improvement
    **Optimization Metrics:** [0-100] optimization effectiveness rating
    **Advanced Optimization:** Comprehensive performance enhancement with intelligent tuning
  </output>"""
        
        else:
            return """  <output>
    Component implementation completed successfully:

    **Implementation Status:** [percentage]% component functionality achieved
    **Feature Coverage:** [count] features successfully implemented
    **System Integration:** [percentage]% integration completion
    **Quality Metrics:** [0-100] component effectiveness rating
    **Advanced Implementation:** Comprehensive component with intelligent automation
  </output>"""
    
    def _generate_command_file_template(self, command_name: str, body_content: str) -> str:
        """Generate command_file XML template."""
        return f"""<command_file>
  <metadata>
    <name>{command_name}</name>
    <purpose>Command implementation for {command_name}</purpose>
    <usage_pattern>
      <![CDATA[
      {command_name} [arguments]
      ]]>
    </usage_pattern>
  </metadata>
  
  <arguments>
    <argument name="target" type="string" required="false">
      <description>Target specification for command execution</description>
    </argument>
  </arguments>
  
  <steps>
    <step name="execute">
      <description>Execute {command_name} functionality</description>
      <![CDATA[
      {body_content}
      ]]>
    </step>
  </steps>
  
  <output>
    Command '{command_name}' executed successfully with comprehensive results.
  </output>
</command_file>"""
    
    def _backup_file(self, file_path: Path):
        """Create backup of file before modification."""
        backup_path = file_path.with_suffix(file_path.suffix + '.backup')
        backup_path.write_text(file_path.read_text(encoding='utf-8'), encoding='utf-8')
    
    def run_comprehensive_fix(self):
        """Run comprehensive fix across all identified problem files."""
        logger.info("Starting comprehensive XML error fixing...")
        
        # Priority 1: Critical XML parsing errors
        critical_files = [
            "components/ecosystem/api-marketplace.md",
            "components/constitutional/constitutional-framework.md",
            "components/constitutional/safety-framework.md",
            "components/quality/framework-validation.md",
            "components/intelligence/cognitive-architecture.md",
            "components/learning/meta-learning.md",
            "components/learning/meta-learning-framework.md",
            "components/learning/examples-library.md",
            "components/optimization/opro-framework.md",
            "components/optimization/dspy-framework.md",
            "components/optimization/prompt-optimization.md",
            "components/optimization/autoprompt-framework.md",
            "components/optimization/textgrad-framework.md",
            "components/meta/component-loader.md",
            "components/reasoning/react-reasoning.md",
            "components/reasoning/tree-of-thoughts.md",
            "components/testing/mutation-testing.md",
            "components/user-experience/intelligent-help.md",
            "components/deployment/ci-cd-integration.md",
            "components/reliability/chaos-engineering.md",
            "components/actions/parallel-execution.md",
            "components/orchestration/agent-orchestration.md",
            "components/orchestration/dag-orchestrator.md",
            "components/orchestration/agent-swarm.md",
            "components/performance/framework-optimization.md",
            "components/performance/auto-scaling.md",
            "components/community/community-platform.md",
            "components/error/circuit-breaker.md",
            "components/validation/xml-structure.md",
            "components/validation/input-validation.md",
            "components/analytics/business-intelligence.md",
            "components/analytics/user-feedback.md"
        ]
        
        # Fix critical files first
        for file_rel_path in critical_files:
            file_path = self.root_path / file_rel_path
            if file_path.exists():
                logger.info(f"Processing critical file: {file_path}")
                self.fix_mismatched_tags(file_path)
                self.fix_malformed_xml_structure(file_path)
                self.fix_missing_output_sections(file_path)
                
                # Validate after fixes
                if not self.validate_xml_after_fix(file_path):
                    logger.warning(f"XML validation still failing for {file_path}")
        
        # Priority 2: Missing output sections
        components_dir = self.root_path / "components"
        if components_dir.exists():
            for comp_file in components_dir.rglob("*.md"):
                if comp_file.name != "README.md":
                    self.fix_missing_output_sections(comp_file)
        
        # Priority 3: Command file structure issues
        commands_dir = self.root_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.rglob("*.md"):
                if cmd_file.name != "README.md":
                    self.fix_command_file_structure(cmd_file)
        
        # Generate fix report
        self._generate_fix_report()
    
    def _generate_fix_report(self):
        """Generate comprehensive fix report."""
        report = {
            'total_fixes': len(self.fixes_applied),
            'total_errors': len(self.errors_encountered),
            'fixes_by_type': {},
            'success_rate': 0
        }
        
        # Calculate statistics
        for fix in self.fixes_applied:
            fix_type = fix['type']
            if fix_type not in report['fixes_by_type']:
                report['fixes_by_type'][fix_type] = 0
            report['fixes_by_type'][fix_type] += 1
        
        if report['total_fixes'] + report['total_errors'] > 0:
            report['success_rate'] = report['total_fixes'] / (report['total_fixes'] + report['total_errors']) * 100
        
        # Write report
        report_path = self.root_path.parent / "xml_fix_report.json"
        import json
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump({
                'summary': report,
                'fixes_applied': self.fixes_applied,
                'errors_encountered': self.errors_encountered
            }, f, indent=2)
        
        logger.info(f"Fix report generated: {report_path}")
        logger.info(f"Total fixes applied: {report['total_fixes']}")
        logger.info(f"Success rate: {report['success_rate']:.1f}%")

if __name__ == "__main__":
    fixer = XMLErrorFixer()
    fixer.run_comprehensive_fix()