#!/usr/bin/env python3
"""
XML Utilities for Claude Code Modular Prompts Framework

Shared XML parsing and manipulation utilities to avoid code duplication
across framework scripts.

Author: Claude Code Framework
Version: 1.0.0
Date: 2025-07-11
"""

import xml.etree.ElementTree as ET
from typing import Dict, Any, Union, List
from pathlib import Path


def xml_to_dict(element: ET.Element) -> Union[Dict[str, Any], str]:
    """
    Convert XML element to nested dictionary.
    
    Args:
        element: XML element to convert
        
    Returns:
        Dictionary representation of XML element
    """
    result = {}
    
    # Handle element text content
    if element.text and element.text.strip():
        if len(element) == 0:  # Leaf node
            return element.text.strip()
    
    # Handle child elements
    for child in element:
        key = child.tag
        value = xml_to_dict(child)
        
        # Handle multiple elements with same tag
        if key in result:
            if not isinstance(result[key], list):
                result[key] = [result[key]]
            result[key].append(value)
        else:
            result[key] = value
    
    # Handle attributes
    if element.attrib:
        result.update({f"@{k}": v for k, v in element.attrib.items()})
    
    return result


def parse_xml_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Parse XML file and return as dictionary.
    
    Args:
        file_path: Path to XML file
        
    Returns:
        Dictionary representation of XML file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ET.ParseError: If XML is malformed
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"XML file not found: {file_path}")
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    return xml_to_dict(root)


def navigate_xml_path(data: Dict[str, Any], path: str) -> Any:
    """
    Navigate XML data using dot notation path.
    
    Args:
        data: Dictionary representation of XML
        path: Dot-notation path (e.g., "project_info.name")
        
    Returns:
        Value at path or None if not found
    """
    parts = path.strip().split('.')
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


def create_xml_element(tag: str, text: str = None, attrib: Dict[str, str] = None) -> ET.Element:
    """
    Create XML element with optional text and attributes.
    
    Args:
        tag: Element tag name
        text: Element text content
        attrib: Element attributes
        
    Returns:
        XML element
    """
    element = ET.Element(tag, attrib or {})
    if text:
        element.text = text
    return element


def dict_to_xml(data: Dict[str, Any], root_tag: str = "root") -> ET.Element:
    """
    Convert dictionary to XML element.
    
    Args:
        data: Dictionary to convert
        root_tag: Tag name for root element
        
    Returns:
        XML element
    """
    root = ET.Element(root_tag)
    _dict_to_xml_recursive(data, root)
    return root


def _dict_to_xml_recursive(data: Any, parent: ET.Element) -> None:
    """Recursively convert dictionary to XML elements."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key.startswith('@'):
                # Handle attributes
                parent.set(key[1:], str(value))
            else:
                child = ET.SubElement(parent, key)
                _dict_to_xml_recursive(value, child)
    elif isinstance(data, list):
        for item in data:
            _dict_to_xml_recursive(item, parent)
    else:
        parent.text = str(data)


def validate_xml_structure(file_path: Union[str, Path], required_elements: List[str] = None) -> Dict[str, Any]:
    """
    Validate XML file structure.
    
    Args:
        file_path: Path to XML file
        required_elements: List of required element paths
        
    Returns:
        Validation results dictionary
    """
    result = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'missing_elements': []
    }
    
    try:
        data = parse_xml_file(file_path)
        
        if required_elements:
            for element_path in required_elements:
                if navigate_xml_path(data, element_path) is None:
                    result['missing_elements'].append(element_path)
                    result['warnings'].append(f"Missing element: {element_path}")
        
    except FileNotFoundError:
        result['valid'] = False
        result['errors'].append(f"File not found: {file_path}")
    except ET.ParseError as e:
        result['valid'] = False
        result['errors'].append(f"XML parsing error: {e}")
    except Exception as e:
        result['valid'] = False
        result['errors'].append(f"Validation error: {e}")
    
    return result