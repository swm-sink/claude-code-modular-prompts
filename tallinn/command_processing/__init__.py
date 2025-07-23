#!/usr/bin/env python3
"""
Command Processing Module for Claude Code Framework

Provides modular command processing, parsing, and simplification capabilities
for converting XML-based commands to human-readable markdown format.
"""

from .xml_parser import XMLCommandParser
from .content_processor import ContentProcessor
from .markdown_generator import MarkdownGenerator
from .component_extractor import ComponentExtractor

__all__ = [
    'XMLCommandParser',
    'ContentProcessor', 
    'MarkdownGenerator',
    'ComponentExtractor',
]