#!/usr/bin/env python3
"""
PROJECT_CONFIG Validation Script

This script validates PROJECT_CONFIG.xml files and tests dynamic placeholder resolution.
It checks XML structure, required fields, and simulates runtime placeholder resolution.
"""

import xml.etree.ElementTree as ET
import os
import sys
import re
from typing import Dict, List, Tuple, Optional
import json

class ProjectConfigValidator:
    """Validates PROJECT_CONFIG.xml files and tests dynamic resolution."""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config_tree = None
        self.config_root = None
        self.errors = []
        self.warnings = []
        self.config_values = {}
        
    def validate(self) -> bool:
        """Run all validation checks."""
        print(f"\n=== Validating PROJECT_CONFIG: {self.config_path} ===\n")
        
        # Step 1: Check file exists
        if not self._check_file_exists():
            return False
            
        # Step 2: Parse XML
        if not self._parse_xml():
            return False
            
        # Step 3: Validate structure
        if not self._validate_structure():
            return False
            
        # Step 4: Load configuration values
        self._load_config_values()
        
        # Step 5: Test dynamic resolution
        self._test_dynamic_resolution()
        
        # Step 6: Validate against CLAUDE.md placeholders
        self._validate_claude_md_placeholders()
        
        # Report results
        self._report_results()
        
        return len(self.errors) == 0
    
    def _check_file_exists(self) -> bool:
        """Check if configuration file exists."""
        if not os.path.exists(self.config_path):
            self.errors.append(f"Configuration file not found: {self.config_path}")
            return False
        return True
    
    def _parse_xml(self) -> bool:
        """Parse XML configuration file."""
        try:
            self.config_tree = ET.parse(self.config_path)
            self.config_root = self.config_tree.getroot()
            print("✓ XML parsing successful")
            return True
        except ET.ParseError as e:
            self.errors.append(f"XML parsing error: {e}")
            return False
    
    def _validate_structure(self) -> bool:
        """Validate required XML structure."""
        required_sections = [
            'project_info',
            'project_structure',
            'quality_standards',
            'development_workflow'
        ]
        
        for section in required_sections:
            if self.config_root.find(section) is None:
                self.errors.append(f"Missing required section: {section}")
        
        # Check version attribute
        if 'version' not in self.config_root.attrib:
            self.errors.append("Missing version attribute in project_configuration")
        
        if self.errors:
            return False
            
        print("✓ XML structure validation passed")
        return True
    
    def _load_config_values(self):
        """Load all configuration values into a dictionary."""
        def extract_values(element, path=""):
            for child in element:
                child_path = f"{path}.{child.tag}" if path else child.tag
                if child.text and child.text.strip():
                    self.config_values[child_path] = child.text.strip()
                extract_values(child, child_path)
        
        extract_values(self.config_root)
        print(f"✓ Loaded {len(self.config_values)} configuration values")
    
    def _test_dynamic_resolution(self):
        """Test dynamic placeholder resolution."""
        print("\n--- Testing Dynamic Placeholder Resolution ---")
        
        # Test cases from CLAUDE.md
        test_cases = [
            ("source_directory", "project_structure.source_directory", "src"),
            ("test_directory", "project_structure.test_directory", "tests"),
            ("docs_directory", "project_structure.docs_directory", "docs"),
            ("scripts_directory", "project_structure.scripts_directory", "scripts"),
            ("test_coverage.threshold", "quality_standards.test_coverage.threshold", "90"),
            ("performance.response_time_p95", "quality_standards.performance.response_time_p95", "200ms"),
            ("commands.test", "development_workflow.commands.test", "language-specific"),
            ("ai_temperature.factual", "framework_behavior.ai_temperature.factual", "0.2"),
        ]
        
        for placeholder, config_path, default in test_cases:
            resolved = self._resolve_placeholder(placeholder, default)
            
            # Check if we got the configured value or the default
            if config_path in self.config_values:
                # Config has this value
                print(f"  ✓ {placeholder}: '{resolved}' (from config)")
            else:
                # Using default
                print(f"  ✓ {placeholder}: '{resolved}' (using default)")
                
            # Verify resolution logic works
            if resolved == self.config_values.get(config_path, default):
                pass  # Good
            else:
                self.errors.append(
                    f"Resolution logic error for {placeholder}: got '{resolved}', expected '{self.config_values.get(config_path, default)}'"
                )
    
    def _resolve_placeholder(self, path: str, default: str) -> str:
        """Simulate runtime placeholder resolution."""
        # Direct lookup first
        if path in self.config_values:
            return self.config_values[path]
        
        # Convert placeholder path formats
        # Handle paths like "test_coverage.threshold" -> need full path
        search_paths = [
            path,
            path.replace("_", "."),
            f"project_structure.{path}",
            f"quality_standards.{path}",
            f"development_workflow.{path}",
            f"framework_behavior.{path}",
            f"quality_standards.test_coverage.{path}",
            f"quality_standards.performance.{path}",
            f"development_workflow.commands.{path}",
            f"framework_behavior.ai_temperature.{path}"
        ]
        
        for search_path in search_paths:
            if search_path in self.config_values:
                return self.config_values[search_path]
        
        # Try to find by suffix match
        for key, value in self.config_values.items():
            if key.endswith(f".{path}") or key.endswith(f".{path.replace('_', '.')}"):
                return value
        
        return default
    
    def _validate_claude_md_placeholders(self):
        """Validate that all CLAUDE.md placeholders can be resolved."""
        print("\n--- Validating CLAUDE.md Placeholders ---")
        
        # Extract placeholders from CLAUDE.md
        # Try multiple potential locations
        potential_paths = [
            os.path.join(os.path.dirname(os.path.dirname(self.config_path)), "CLAUDE.md"),
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(self.config_path))), "CLAUDE.md"),
            "CLAUDE.md",
            os.path.join(os.getcwd(), "CLAUDE.md")
        ]
        
        claude_md_path = None
        for path in potential_paths:
            if os.path.exists(path):
                claude_md_path = path
                break
        
        if not claude_md_path:
            self.warnings.append("CLAUDE.md not found for placeholder validation")
            return
        
        with open(claude_md_path, 'r') as f:
            content = f.read()
        
        # Find all [PROJECT_CONFIG: path | DEFAULT: value] patterns
        pattern = r'\[PROJECT_CONFIG:\s*([^|]+)\s*\|\s*DEFAULT:\s*([^\]]+)\]'
        placeholders = re.findall(pattern, content)
        
        unique_placeholders = set(placeholders)
        print(f"  Found {len(unique_placeholders)} unique placeholders in CLAUDE.md")
        
        resolved_count = 0
        for placeholder, default in unique_placeholders:
            placeholder = placeholder.strip()
            default = default.strip()
            resolved = self._resolve_placeholder(placeholder, default)
            
            if resolved != default:
                resolved_count += 1
        
        print(f"  ✓ {resolved_count}/{len(unique_placeholders)} placeholders resolved from config")
        print(f"  ✓ {len(unique_placeholders) - resolved_count} using defaults")
    
    def _report_results(self):
        """Report validation results."""
        print("\n=== Validation Results ===")
        
        if self.errors:
            print(f"\n❌ Found {len(self.errors)} errors:")
            for error in self.errors:
                print(f"  - {error}")
        else:
            print("\n✅ All validation checks passed!")
        
        if self.warnings:
            print(f"\n⚠️  Found {len(self.warnings)} warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        # Print configuration summary
        print("\n--- Configuration Summary ---")
        print(f"Project Name: {self.config_values.get('project_info.name', 'N/A')}")
        print(f"Domain: {self.config_values.get('project_info.domain', 'N/A')}")
        print(f"Language: {self.config_values.get('project_info.primary_language', 'N/A')}")
        print(f"Test Coverage Threshold: {self.config_values.get('quality_standards.test_coverage.threshold', 'N/A')}%")
        print(f"Source Directory: {self.config_values.get('project_structure.source_directory', 'N/A')}")
        print(f"Test Directory: {self.config_values.get('project_structure.test_directory', 'N/A')}")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python validate-project-config.py <path_to_config.xml>")
        sys.exit(1)
    
    config_path = sys.argv[1]
    validator = ProjectConfigValidator(config_path)
    
    if validator.validate():
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()