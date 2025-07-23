#!/usr/bin/env python3
"""
XML Command Parser Module

Handles parsing of XML command structures and extraction of metadata,
arguments, examples, and other command data.
"""

import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple, Any, Optional
from pathlib import Path


class XMLCommandParser:
    """Parser for XML-based command files."""
    
    def __init__(self):
        self.component_cache = {}
    
    def extract_yaml_frontmatter(self, content: str) -> Tuple[Dict[str, str], str]:
        """Extract YAML frontmatter from markdown content."""
        frontmatter = {}
        body = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1].strip()
                body = parts[2].lstrip()
                
                # Simple YAML parsing for common fields
                for line in yaml_content.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        frontmatter[key.strip()] = value.strip().strip('"\'')
        
        return frontmatter, body
    
    def extract_xml_data(self, content: str) -> Dict[str, Any]:
        """Extract data from XML command structure.
        
        Refactored for improved testability and maintainability.
        """
        data = self._create_default_data_structure()
        
        xml_root = self._parse_xml_content(content)
        if xml_root is None:
            return data
        
        # Extract all sections using specialized helper methods
        data['metadata'] = self._extract_metadata_from_root(xml_root)
        data['arguments'] = self._extract_arguments_from_root(xml_root)
        data['examples'] = self._extract_examples_from_root(xml_root)
        data['prompt'] = self._extract_prompt_from_root(xml_root)
        data['components'] = self._extract_components_from_root(xml_root)
        self._extract_dependencies(xml_root, data)
        
        return data
    
    def _create_default_data_structure(self) -> Dict[str, Any]:
        """Create the default data structure for XML parsing results."""
        return {
            'metadata': {},
            'arguments': [],
            'examples': [],
            'prompt': '',
            'components': [],
            'dependencies': {}
        }
    
    def _parse_xml_content(self, content: str) -> Optional[ET.Element]:
        """Parse XML content and return the root element."""
        # Find the XML block
        xml_match = re.search(r'<command_file>(.*?)</command_file>', content, re.DOTALL)
        if not xml_match:
            return None
        
        xml_content = xml_match.group(1)
        
        try:
            return ET.fromstring(f"<root>{xml_content}</root>")
        except ET.ParseError as e:
            print(f"Warning: Failed to parse XML content: {e}")
            return None
    
    def _extract_metadata_from_root(self, root: ET.Element) -> Dict[str, str]:
        """Extract metadata from XML root element."""
        metadata = {}
        metadata_element = root.find('metadata')
        
        if metadata_element is not None:
            for child in metadata_element:
                text_value = child.text.strip() if child.text else ''
                metadata[child.tag] = text_value
        
        return metadata
    
    def _extract_arguments_from_root(self, root: ET.Element) -> List[Dict[str, Any]]:
        """Extract arguments from XML root element."""
        arguments = []
        arguments_element = root.find('arguments')
        
        if arguments_element is not None:
            for arg in arguments_element.findall('argument'):
                arg_data = self._parse_single_argument(arg)
                arguments.append(arg_data)
        
        return arguments
    
    def _parse_single_argument(self, arg_element: ET.Element) -> Dict[str, Any]:
        """Parse a single argument element."""
        arg_data = {
            'name': arg_element.get('name', ''),
            'type': arg_element.get('type', 'string'),
            'required': arg_element.get('required', 'false').lower() == 'true',
            'description': ''
        }
        
        desc_element = arg_element.find('description')
        if desc_element is not None and desc_element.text:
            arg_data['description'] = desc_element.text.strip()
        
        return arg_data
    
    def _extract_examples_from_root(self, root: ET.Element) -> List[Dict[str, str]]:
        """Extract examples from XML root element."""
        examples = []
        examples_element = root.find('examples')
        
        if examples_element is not None:
            for example in examples_element.findall('example'):
                example_data = self._parse_single_example(example)
                examples.append(example_data)
        
        return examples
    
    def _parse_single_example(self, example_element: ET.Element) -> Dict[str, str]:
        """Parse a single example element."""
        example_data = {'description': '', 'usage': ''}
        
        desc_element = example_element.find('description')
        if desc_element is not None and desc_element.text:
            example_data['description'] = desc_element.text.strip()
        
        usage_element = example_element.find('usage')
        if usage_element is not None and usage_element.text:
            example_data['usage'] = usage_element.text.strip()
        
        return example_data
    
    def _extract_prompt_from_root(self, root: ET.Element) -> str:
        """Extract prompt from XML root element."""
        claude_prompt = root.find('claude_prompt/prompt')
        
        if claude_prompt is not None:
            return ET.tostring(claude_prompt, encoding='unicode', method='text')
        
        return ''
    
    def _extract_components_from_root(self, root: ET.Element) -> List[str]:
        """Extract component includes from XML root element."""
        components = []
        includes = root.findall('.//include')
        
        for include in includes:
            if include.text:
                components.append(include.text.strip())
        
        return components
    
    def _extract_dependencies(self, root: ET.Element, data: Dict[str, Any]) -> None:
        """Extract dependency information from XML root."""
        deps = root.find('dependencies')
        if deps is not None:
            # Component dependencies
            comp_deps = deps.find('includes_components')
            if comp_deps is not None:
                data['dependencies']['components'] = [
                    comp.text.strip() for comp in comp_deps.findall('component') 
                    if comp.text
                ]
            
            # Command dependencies
            cmd_deps = deps.find('invokes_commands')
            if cmd_deps is not None:
                data['dependencies']['commands'] = [
                    cmd.text.strip() for cmd in cmd_deps.findall('command')
                    if cmd.text
                ]
            
            # Config dependencies
            cfg_deps = deps.find('uses_config_values')
            if cfg_deps is not None:
                data['dependencies']['config'] = [
                    cfg.text.strip() for cfg in cfg_deps.findall('config')
                    if cfg.text
                ]
    
    def parse_command_file(self, file_path: Path) -> Tuple[Dict[str, str], Dict[str, Any]]:
        """Parse a complete command file and return frontmatter and XML data."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, body = self.extract_yaml_frontmatter(content)
        xml_data = self.extract_xml_data(content)
        
        return frontmatter, xml_data