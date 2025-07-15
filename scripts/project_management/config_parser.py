#!/usr/bin/env python3
"""
PROJECT_CONFIG Parser Demonstration

This script demonstrates how the framework would parse PROJECT_CONFIG.xml
and resolve placeholders at runtime.
"""

import xml.etree.ElementTree as ET
import os
import re
from typing import Dict, Optional, Any
import json

class ProjectConfigParser:
    """Parser for PROJECT_CONFIG.xml with placeholder resolution."""
    
    def __init__(self, config_path: str = "PROJECT_CONFIG.xml"):
        self.config_path = config_path
        self.config_data = {}
        self.loaded = False
        
    def load(self) -> bool:
        """Load and parse PROJECT_CONFIG.xml."""
        if not os.path.exists(self.config_path):
            print(f"Configuration file not found: {self.config_path}")
            return False
            
        try:
            tree = ET.parse(self.config_path)
            root = tree.getroot()
            self._parse_element(root, "")
            self.loaded = True
            print(f"Loaded configuration from: {self.config_path}")
            return True
        except Exception as e:
            print(f"Error loading configuration: {e}")
            return False
    
    def _parse_element(self, element, path_prefix: str):
        """Recursively parse XML elements into dot-notation paths."""
        for child in element:
            # Build the path
            path = f"{path_prefix}.{child.tag}" if path_prefix else child.tag
            
            # If element has text content, store it
            if child.text and child.text.strip():
                self.config_data[path] = child.text.strip()
            
            # Recursively parse children
            self._parse_element(child, path)
    
    def resolve(self, placeholder: str) -> str:
        """Resolve a PROJECT_CONFIG placeholder.
        
        Args:
            placeholder: String like "[PROJECT_CONFIG: path | DEFAULT: value]"
            
        Returns:
            Resolved value from config or default
        """
        # Parse placeholder format
        match = re.match(r'\[PROJECT_CONFIG:\s*([^|]+)\s*\|\s*DEFAULT:\s*([^\]]+)\]', placeholder)
        if not match:
            return placeholder  # Not a valid placeholder
        
        path = match.group(1).strip()
        default = match.group(2).strip()
        
        # Try to resolve from loaded config
        value = self.get(path)
        return value if value is not None else default
    
    def get(self, path: str) -> Optional[str]:
        """Get a configuration value by path."""
        if not self.loaded:
            return None
        
        # Direct lookup
        if path in self.config_data:
            return self.config_data[path]
        
        # Try with common prefixes
        prefixes = [
            "project_structure.",
            "quality_standards.",
            "development_workflow.",
            "framework_behavior.",
            "quality_standards.test_coverage.",
            "quality_standards.performance.",
            "development_workflow.commands.",
            "framework_behavior.ai_temperature."
        ]
        
        for prefix in prefixes:
            full_path = prefix + path
            if full_path in self.config_data:
                return self.config_data[full_path]
        
        # Try suffix matching
        for key, value in self.config_data.items():
            if key.endswith(f".{path}"):
                return value
        
        return None
    
    def resolve_in_text(self, text: str) -> str:
        """Resolve all placeholders in a text string."""
        # Find all placeholders
        pattern = r'\[PROJECT_CONFIG:[^]]+\]'
        
        def replacer(match):
            return self.resolve(match.group(0))
        
        return re.sub(pattern, replacer, text)
    
    def print_config(self):
        """Print the loaded configuration."""
        print("\n=== Loaded Configuration ===")
        for path, value in sorted(self.config_data.items()):
            print(f"  {path}: {value}")


def demonstrate_resolution():
    """Demonstrate PROJECT_CONFIG resolution with examples."""
    print("=== PROJECT_CONFIG Parser Demonstration ===\n")
    
    # Try to load actual PROJECT_CONFIG.xml
    parser = ProjectConfigParser()
    
    # If no PROJECT_CONFIG.xml, try test config
    if not parser.load():
        test_config = "internal/artifacts/test-PROJECT_CONFIG.xml"
        if os.path.exists(test_config):
            print(f"\nTrying test configuration: {test_config}")
            parser = ProjectConfigParser(test_config)
            parser.load()
    
    # Test resolution of individual placeholders
    print("\n=== Testing Placeholder Resolution ===")
    test_placeholders = [
        "[PROJECT_CONFIG: source_directory | DEFAULT: src]",
        "[PROJECT_CONFIG: test_directory | DEFAULT: tests]",
        "[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]",
        "[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]",
        "[PROJECT_CONFIG: commands.test | DEFAULT: npm test]",
        "[PROJECT_CONFIG: ai_temperature.factual | DEFAULT: 0.2]",
        "[PROJECT_CONFIG: non_existent_path | DEFAULT: fallback_value]"
    ]
    
    for placeholder in test_placeholders:
        resolved = parser.resolve(placeholder)
        print(f"  {placeholder}")
        print(f"    → {resolved}")
    
    # Test resolution in text
    print("\n=== Testing Text Resolution ===")
    sample_text = """
    Project Structure:
    - Source files: [PROJECT_CONFIG: source_directory | DEFAULT: src]
    - Tests: [PROJECT_CONFIG: test_directory | DEFAULT: tests]
    - Documentation: [PROJECT_CONFIG: docs_directory | DEFAULT: docs]
    
    Quality Standards:
    - Test coverage must be at least [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%
    - Response time P95: [PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]
    
    Commands:
    - Run tests: [PROJECT_CONFIG: commands.test | DEFAULT: npm test]
    - Build: [PROJECT_CONFIG: commands.build | DEFAULT: npm run build]
    """
    
    resolved_text = parser.resolve_in_text(sample_text)
    print("Original text with placeholders:")
    print(sample_text)
    print("\nResolved text:")
    print(resolved_text)


if __name__ == "__main__":
    demonstrate_resolution()