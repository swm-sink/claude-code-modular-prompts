#!/usr/bin/env python3
"""
Configuration Validator for Claude Code Modular Prompts Framework

Validates PROJECT_CONFIG.xml files to ensure they contain all required sections
and values for proper framework operation.

Author: Claude Code Framework
Version: 1.0.0
Date: 2025-07-11
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
import logging
import re
import sys
import os

# Add current directory to path for local imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xml_utils import xml_to_dict, parse_xml_file, navigate_xml_path


class ConfigValidator:
    """
    Validates PROJECT_CONFIG.xml files for completeness and correctness.
    """
    
    def __init__(self, project_root: Optional[str] = None):
        """
        Initialize configuration validator.
        
        Args:
            project_root: Path to project root directory (default: current directory)
        """
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.config_file = self.project_root / "PROJECT_CONFIG.xml"
        self.logger = logging.getLogger(__name__)
        
        # Define required and optional sections
        self.required_sections = {
            'project_info': {
                'required_fields': ['name', 'domain', 'primary_language'],
                'optional_fields': ['description', 'framework_stack']
            },
            'project_structure': {
                'required_fields': ['source_directory', 'test_directory'],
                'optional_fields': ['docs_directory', 'scripts_directory', 'config_directory', 'build_directory']
            },
            'quality_standards': {
                'required_fields': ['test_coverage', 'code_quality'],
                'optional_fields': ['performance', 'security_requirements']
            },
            'development_workflow': {
                'required_fields': ['commands'],
                'optional_fields': ['git_workflow']
            }
        }
        
        self.optional_sections = {
            'domain_specific_rules': {
                'description': 'Project-specific rules and requirements'
            },
            'custom_personas': {
                'description': 'Custom personas for the project'
            },
            'security_requirements': {
                'description': 'Security and compliance requirements'
            },
            'deployment': {
                'description': 'Deployment configuration'
            },
            'framework_behavior': {
                'description': 'Framework behavior customization'
            }
        }
        
        # Define valid values for specific fields
        self.valid_values = {
            'domain': [
                'web-development', 'mobile-engineering', 'data-analytics', 
                'data-engineering', 'devops-platform', 'enterprise-tools',
                'financial-technology', 'machine-learning', 'platform-engineering'
            ],
            'primary_language': [
                'javascript', 'typescript', 'python', 'java', 'go', 'rust',
                'cpp', 'csharp', 'swift', 'kotlin', 'php', 'ruby'
            ],
            'test_coverage.enforcement': ['BLOCKING', 'CONDITIONAL', 'ADVISORY'],
            'file_creation_policy': ['conservative', 'moderate', 'permissive'],
            'test_first_enforcement': ['strict', 'flexible', 'advisory'],
            'documentation_generation': ['automatic', 'on-request', 'manual']
        }
    
    def validate(self) -> Dict[str, Any]:
        """
        Validate the PROJECT_CONFIG.xml file.
        
        Returns:
            Dictionary containing validation results
        """
        result = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'suggestions': [],
            'config_found': False,
            'sections_found': [],
            'missing_required': [],
            'missing_optional': []
        }
        
        # Check if config file exists
        if not self.config_file.exists():
            result['valid'] = False
            result['errors'].append(f"PROJECT_CONFIG.xml not found at {self.config_file}")
            result['suggestions'].append("Create PROJECT_CONFIG.xml using PROJECT_CONFIG_TEMPLATE.md")
            return result
        
        result['config_found'] = True
        
        try:
            # Parse XML
            tree = ET.parse(self.config_file)
            root = tree.getroot()
            
            # Validate root element
            if root.tag != 'project_configuration':
                result['errors'].append(f"Root element should be 'project_configuration', found '{root.tag}'")
                result['valid'] = False
            
            # Validate version attribute
            version = root.get('version')
            if not version:
                result['warnings'].append("Missing 'version' attribute on root element")
            elif version != '1.0.0':
                result['warnings'].append(f"Version '{version}' may not be compatible with framework")
            
            # Convert XML to dict for easier validation
            config = xml_to_dict(root)
            
            # Validate required sections
            self._validate_required_sections(config, result)
            
            # Validate specific field values
            self._validate_field_values(config, result)
            
            # Check for common issues
            self._check_common_issues(config, result)
            
            # Suggest missing optional sections
            self._suggest_optional_sections(config, result)
            
        except ET.ParseError as e:
            result['valid'] = False
            result['errors'].append(f"XML parsing error: {e}")
        except Exception as e:
            result['valid'] = False
            result['errors'].append(f"Validation error: {e}")
        
        return result
    
    def _validate_required_sections(self, config: Dict[str, Any], result: Dict[str, Any]) -> None:
        """Validate that all required sections are present."""
        for section_name, section_config in self.required_sections.items():
            if section_name not in config:
                result['missing_required'].append(section_name)
                result['errors'].append(f"Missing required section: {section_name}")
                result['valid'] = False
                continue
            
            result['sections_found'].append(section_name)
            section_data = config[section_name]
            
            # Validate required fields within section
            for field in section_config['required_fields']:
                if not self._has_field(section_data, field):
                    result['missing_required'].append(f"{section_name}.{field}")
                    result['errors'].append(f"Missing required field: {section_name}.{field}")
                    result['valid'] = False
    
    def _has_field(self, data: Any, field_path: str) -> bool:
        """Check if a field exists using dot notation."""
        if not isinstance(data, dict):
            return False
        
        parts = field_path.split('.')
        current = data
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return False
        
        return True
    
    def _validate_field_values(self, config: Dict[str, Any], result: Dict[str, Any]) -> None:
        """Validate specific field values against allowed values."""
        for field_path, valid_values in self.valid_values.items():
            value = self._get_field_value(config, field_path)
            
            if value is not None and value not in valid_values:
                result['warnings'].append(
                    f"Field '{field_path}' has value '{value}' which is not in recommended values: {valid_values}"
                )
    
    def _get_field_value(self, data: Dict[str, Any], field_path: str) -> Any:
        """Get field value using dot notation."""
        parts = field_path.split('.')
        current = data
        
        try:
            for part in parts:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    return None
            return current
        except (KeyError, TypeError):
            return None
    
    def _check_common_issues(self, config: Dict[str, Any], result: Dict[str, Any]) -> None:
        """Check for common configuration issues."""
        
        # Check test coverage threshold
        threshold = self._get_field_value(config, 'quality_standards.test_coverage.threshold')
        if threshold is not None:
            try:
                threshold_val = int(threshold)
                if threshold_val < 50:
                    result['warnings'].append(f"Test coverage threshold {threshold_val}% is very low")
                elif threshold_val > 100:
                    result['errors'].append(f"Test coverage threshold {threshold_val}% cannot exceed 100%")
                    result['valid'] = False
            except ValueError:
                result['errors'].append(f"Test coverage threshold '{threshold}' should be a number")
                result['valid'] = False
        
        # Check source directory exists
        source_dir = self._get_field_value(config, 'project_structure.source_directory')
        if source_dir:
            source_path = self.project_root / source_dir
            if not source_path.exists():
                result['warnings'].append(f"Source directory '{source_dir}' does not exist")
        
        # Check test directory exists
        test_dir = self._get_field_value(config, 'project_structure.test_directory')
        if test_dir:
            test_path = self.project_root / test_dir
            if not test_path.exists():
                result['warnings'].append(f"Test directory '{test_dir}' does not exist")
        
        # Validate performance thresholds
        response_time = self._get_field_value(config, 'quality_standards.performance.response_time_p95')
        if response_time:
            if not re.match(r'^\d+ms$', str(response_time)):
                result['warnings'].append(f"Performance threshold '{response_time}' should be in format 'NNNms'")
    
    def _suggest_optional_sections(self, config: Dict[str, Any], result: Dict[str, Any]) -> None:
        """Suggest missing optional sections that might be useful."""
        for section_name, section_info in self.optional_sections.items():
            if section_name not in config:
                result['missing_optional'].append(section_name)
                result['suggestions'].append(
                    f"Consider adding optional section '{section_name}': {section_info['description']}"
                )
    
    def generate_minimal_config(self, project_name: str, domain: str, language: str) -> str:
        """
        Generate a minimal valid PROJECT_CONFIG.xml.
        
        Args:
            project_name: Name of the project
            domain: Project domain 
            language: Primary programming language
            
        Returns:
            XML content as string
        """
        template = f"""<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0">
  <project_info>
    <name>{project_name}</name>
    <domain>{domain}</domain>
    <description>Generated minimal configuration</description>
    <primary_language>{language}</primary_language>
  </project_info>

  <project_structure>
    <root_directory>.</root_directory>
    <source_directory>src</source_directory>
    <test_directory>tests</test_directory>
    <docs_directory>docs</docs_directory>
    <scripts_directory>scripts</scripts_directory>
  </project_structure>

  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>BLOCKING</enforcement>
      <tool>auto-detect</tool>
    </test_coverage>
    <performance>
      <response_time_p95>200ms</response_time_p95>
    </performance>
    <code_quality>
      <linter>auto-detect</linter>
      <formatter>auto-detect</formatter>
    </code_quality>
  </quality_standards>

  <development_workflow>
    <commands>
      <install>auto-detect</install>
      <test>auto-detect</test>
      <lint>auto-detect</lint>
      <build>auto-detect</build>
    </commands>
    <git_workflow>
      <branch_pattern>feature/*</branch_pattern>
      <commit_style>conventional</commit_style>
    </git_workflow>
  </development_workflow>

  <framework_behavior>
    <file_creation_policy>conservative</file_creation_policy>
    <test_first_enforcement>strict</test_first_enforcement>
    <ai_temperature>
      <factual>0.2</factual>
      <analysis>0.3</analysis>
      <creative>0.7</creative>
    </ai_temperature>
  </framework_behavior>
</project_configuration>"""
        return template


def main():
    """CLI interface for configuration validator."""
    import argparse
    
    parser = argparse.ArgumentParser(description="PROJECT_CONFIG.xml Validator")
    parser.add_argument('--project-root', help="Project root directory")
    parser.add_argument('--generate', help="Generate minimal config with project name")
    parser.add_argument('--domain', help="Project domain for generation")
    parser.add_argument('--language', help="Primary language for generation")
    parser.add_argument('--output', help="Output file for generation")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    validator = ConfigValidator(project_root=args.project_root)
    
    try:
        if args.generate:
            if not args.domain or not args.language:
                print("ERROR: --domain and --language required for generation")
                return 1
            
            config_content = validator.generate_minimal_config(
                args.generate, args.domain, args.language
            )
            
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(config_content)
                print(f"Generated configuration saved to {args.output}")
            else:
                print(config_content)
        
        else:
            result = validator.validate()
            
            print(f"Configuration validation: {'PASS' if result['valid'] else 'FAIL'}")
            print(f"Configuration file found: {result['config_found']}")
            
            if result['errors']:
                print("\nERRORS:")
                for error in result['errors']:
                    print(f"  ❌ {error}")
            
            if result['warnings']:
                print("\nWARNINGS:")
                for warning in result['warnings']:
                    print(f"  ⚠️  {warning}")
            
            if result['suggestions']:
                print("\nSUGGESTIONS:")
                for suggestion in result['suggestions']:
                    print(f"  💡 {suggestion}")
            
            if result['sections_found']:
                print(f"\nSections found: {', '.join(result['sections_found'])}")
            
            if not result['valid']:
                return 1
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())