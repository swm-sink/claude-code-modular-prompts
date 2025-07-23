#!/usr/bin/env python3
"""
Unit tests for command execution in the Claude Code Modular Prompts framework.
"""

import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
import json
import re

class TestCommandExecution(unittest.TestCase):
    """Test command parsing and execution capabilities."""
    
    def setUp(self):
        """Set up test environment."""
        self.framework_root = Path("claude_prompt_factory")
        self.test_commands = []
        
    def test_xml_parsing_valid_structure(self):
        """Test that valid XML command structures parse correctly."""
        valid_xml = """<command_file>
  <metadata>
    <name>/test-command</name>
    <purpose>Test command for validation</purpose>
  </metadata>
  <arguments>
    <argument name="test" type="string" required="true">
      <description>Test argument</description>
    </argument>
  </arguments>
  <claude_prompt>
    <![CDATA[Test prompt content]]>
  </claude_prompt>
</command_file>"""
        
        try:
            root = ET.fromstring(valid_xml)
            self.assertEqual(root.tag, "command_file")
            self.assertIsNotNone(root.find(".//metadata/name"))
            self.assertIsNotNone(root.find(".//claude_prompt"))
            self.assertTrue(True, "Valid XML parsed successfully")
        except ET.ParseError as e:
            self.fail(f"Valid XML failed to parse: {e}")
    
    def test_xml_parsing_invalid_structure(self):
        """Test that invalid XML structures fail gracefully."""
        invalid_xml = """<command_file>
  <metadata>
    <name>/test-command</name>
    <!-- Missing closing tag -->
  <arguments>
</command_file>"""
        
        with self.assertRaises(ET.ParseError):
            ET.fromstring(invalid_xml)
    
    def test_command_metadata_extraction(self):
        """Test extraction of command metadata."""
        command_path = self.framework_root / "commands" / "development" / "task.md"
        
        if command_path.exists():
            with open(command_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract YAML frontmatter
            yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if yaml_match:
                yaml_content = yaml_match.group(1)
                self.assertIn('description:', yaml_content)
                self.assertIn('allowed-tools:', yaml_content)
            else:
                self.skipTest(f"No YAML frontmatter found in {command_path}")
        else:
            self.skipTest(f"Command file not found: {command_path}")
    
    def test_component_inclusion_validation(self):
        """Test that component includes are valid."""
        command_path = self.framework_root / "commands" / "core" / "existing.md"
        
        if command_path.exists():
            with open(command_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all component includes
            includes = re.findall(r'<include component="([^"]+)" />', content)
            
            # Verify each included component exists
            for component_ref in includes:
                component_path = self.framework_root.parent / component_ref
                if not component_path.exists():
                    # Check if it's a relative path from components dir
                    component_path = self.framework_root / component_ref
                
                self.assertTrue(
                    component_path.exists() or 
                    (self.framework_root / "components" / component_ref.split('/')[-1]).exists(),
                    f"Component not found: {component_ref}"
                )
        else:
            self.skipTest(f"Command file not found: {command_path}")
    
    def test_argument_validation(self):
        """Test command argument structure and validation."""
        test_args_xml = """<arguments>
  <argument name="path" type="string" required="true">
    <description>File path to process</description>
  </argument>
  <argument name="options" type="object" required="false">
    <description>Additional options</description>
  </argument>
</arguments>"""
        
        root = ET.fromstring(test_args_xml)
        args = root.findall('argument')
        
        self.assertEqual(len(args), 2)
        
        # Validate first argument
        arg1 = args[0]
        self.assertEqual(arg1.get('name'), 'path')
        self.assertEqual(arg1.get('type'), 'string')
        self.assertEqual(arg1.get('required'), 'true')
        
        # Validate second argument
        arg2 = args[1]
        self.assertEqual(arg2.get('name'), 'options')
        self.assertEqual(arg2.get('type'), 'object')
        self.assertEqual(arg2.get('required'), 'false')

if __name__ == '__main__':
    unittest.main()