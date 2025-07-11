#!/usr/bin/env python3
"""
Template Resolution Engine for Claude Code Modular Prompts Framework

Implements dynamic resolution of [PROJECT_CONFIG: path | DEFAULT: value] placeholders
throughout the framework, enabling project-specific customization without modifying
core framework files.

Author: Claude Code Framework
Version: 1.0.0
Date: 2025-07-11
"""

import xml.etree.ElementTree as ET
import re
import os
import time
from typing import Dict, Any, Optional, Union
from pathlib import Path
import logging
import sys

# Add current directory to path for local imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xml_utils import xml_to_dict, parse_xml_file, navigate_xml_path


class TemplateResolver:
    """
    Dynamic template resolution engine for project configuration placeholders.
    
    Resolves [PROJECT_CONFIG: path.to.value | DEFAULT: fallback_value] patterns
    by loading PROJECT_CONFIG.xml and navigating XML structure using dot notation.
    """
    
    def __init__(self, project_root: Optional[str] = None, cache_ttl: int = 300):
        """
        Initialize template resolver.
        
        Args:
            project_root: Path to project root directory (default: current directory)
            cache_ttl: Cache time-to-live in seconds (default: 5 minutes)
        """
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.config_file = self.project_root / "PROJECT_CONFIG.xml"
        self.cache_ttl = cache_ttl
        
        # Cache for resolved values and parsed configuration
        self._config_cache: Dict[str, Any] = {}
        self._value_cache: Dict[str, Any] = {}
        self._last_load_time: float = 0
        self._config_mtime: float = 0
        
        # Regex pattern for placeholder matching
        self.placeholder_pattern = re.compile(
            r'\[PROJECT_CONFIG:\s*([^|]+?)\s*\|\s*DEFAULT:\s*([^]]+?)\s*\]'
        )
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
    def _should_reload_config(self) -> bool:
        """Check if configuration should be reloaded."""
        if not self.config_file.exists():
            return False
            
        current_mtime = self.config_file.stat().st_mtime
        current_time = time.time()
        
        # Reload if file modified or cache expired
        return (current_mtime != self._config_mtime or 
                current_time - self._last_load_time > self.cache_ttl)
    
    def _load_configuration(self) -> Dict[str, Any]:
        """Load and parse PROJECT_CONFIG.xml file."""
        if not self.config_file.exists():
            self.logger.info(f"No PROJECT_CONFIG.xml found at {self.config_file}")
            return {}
        
        try:
            self.logger.debug(f"Loading configuration from {self.config_file}")
            
            # Use shared XML utility
            config = parse_xml_file(self.config_file)
            
            # Update cache metadata
            self._config_mtime = self.config_file.stat().st_mtime
            self._last_load_time = time.time()
            
            self.logger.info(f"Configuration loaded successfully from {self.config_file}")
            return config
            
        except ET.ParseError as e:
            self.logger.error(f"Failed to parse PROJECT_CONFIG.xml: {e}")
            return {}
        except Exception as e:
            self.logger.error(f"Error loading configuration: {e}")
            return {}
    
    def _navigate_path(self, config: Dict[str, Any], path: str) -> Optional[Any]:
        """Navigate configuration using dot notation path."""
        return navigate_xml_path(config, path)
    
    def _resolve_single_placeholder(self, match: re.Match) -> str:
        """Resolve a single placeholder match."""
        config_path = match.group(1).strip()
        default_value = match.group(2).strip()
        
        # Check value cache first
        cache_key = f"{config_path}|{default_value}"
        if cache_key in self._value_cache:
            return str(self._value_cache[cache_key])
        
        # Load configuration if needed
        if self._should_reload_config():
            self._config_cache = self._load_configuration()
            self._value_cache.clear()  # Clear value cache on config reload
        
        # Navigate configuration
        if self._config_cache:
            resolved_value = self._navigate_path(self._config_cache, config_path)
            if resolved_value is not None:
                self._value_cache[cache_key] = resolved_value
                self.logger.debug(f"Resolved {config_path} = {resolved_value}")
                return str(resolved_value)
        
        # Use default value if not found
        self._value_cache[cache_key] = default_value
        self.logger.debug(f"Using default for {config_path} = {default_value}")
        return default_value
    
    def resolve_template(self, text: str) -> str:
        """
        Resolve all placeholders in the given text.
        
        Args:
            text: Text containing [PROJECT_CONFIG: path | DEFAULT: value] placeholders
            
        Returns:
            Text with all placeholders resolved to configured or default values
        """
        if not text or not isinstance(text, str):
            return text
        
        def replace_placeholder(match: re.Match) -> str:
            try:
                return self._resolve_single_placeholder(match)
            except Exception as e:
                self.logger.error(f"Error resolving placeholder {match.group(0)}: {e}")
                return match.group(0)  # Return original placeholder on error
        
        # Replace all placeholders
        resolved_text = self.placeholder_pattern.sub(replace_placeholder, text)
        
        # Log if any replacements were made
        if resolved_text != text:
            placeholder_count = len(self.placeholder_pattern.findall(text))
            self.logger.debug(f"Resolved {placeholder_count} placeholder(s)")
        
        return resolved_text
    
    def resolve_file(self, file_path: Union[str, Path]) -> str:
        """
        Resolve all placeholders in a file.
        
        Args:
            file_path: Path to file containing placeholders
            
        Returns:
            File content with all placeholders resolved
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            self.logger.error(f"File not found: {file_path}")
            return ""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            resolved_content = self.resolve_template(content)
            self.logger.info(f"Resolved placeholders in {file_path}")
            return resolved_content
            
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return ""
    
    def get_config_value(self, path: str, default: Any = None) -> Any:
        """
        Get a specific configuration value by path.
        
        Args:
            path: Dot-notation path to configuration value
            default: Default value if path not found
            
        Returns:
            Configuration value or default
        """
        if self._should_reload_config():
            self._config_cache = self._load_configuration()
        
        if self._config_cache:
            value = self._navigate_path(self._config_cache, path)
            if value is not None:
                return value
        
        return default
    
    def validate_configuration(self) -> Dict[str, Any]:
        """
        Validate the current configuration.
        
        Returns:
            Dictionary with validation results
        """
        result = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'config_found': False,
            'required_paths': []
        }
        
        # Check if config file exists
        if not self.config_file.exists():
            result['warnings'].append(f"No PROJECT_CONFIG.xml found at {self.config_file}")
            return result
        
        result['config_found'] = True
        
        # Try to load configuration
        try:
            config = self._load_configuration()
            if not config:
                result['valid'] = False
                result['errors'].append("Configuration file is empty or invalid")
                return result
            
            # Validate required sections
            required_sections = [
                'project_info',
                'project_structure', 
                'quality_standards',
                'development_workflow'
            ]
            
            for section in required_sections:
                if section not in config:
                    result['warnings'].append(f"Missing recommended section: {section}")
            
            self.logger.info("Configuration validation completed")
            
        except Exception as e:
            result['valid'] = False
            result['errors'].append(f"Configuration validation error: {e}")
        
        return result
    
    def clear_cache(self) -> None:
        """Clear all cached configuration and values."""
        self._config_cache.clear()
        self._value_cache.clear()
        self._last_load_time = 0
        self._config_mtime = 0
        self.logger.debug("Configuration cache cleared")


def main():
    """CLI interface for template resolver."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Template Resolution Engine")
    parser.add_argument('--project-root', help="Project root directory")
    parser.add_argument('--file', help="Resolve placeholders in specific file")
    parser.add_argument('--text', help="Resolve placeholders in text")
    parser.add_argument('--validate', action='store_true', help="Validate configuration")
    parser.add_argument('--get', help="Get specific configuration value by path")
    parser.add_argument('--default', help="Default value for --get")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose logging")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    # Initialize resolver
    resolver = TemplateResolver(project_root=args.project_root)
    
    try:
        if args.validate:
            result = resolver.validate_configuration()
            print(f"Configuration valid: {result['valid']}")
            if result['errors']:
                print("Errors:")
                for error in result['errors']:
                    print(f"  - {error}")
            if result['warnings']:
                print("Warnings:")
                for warning in result['warnings']:
                    print(f"  - {warning}")
        
        elif args.get:
            value = resolver.get_config_value(args.get, args.default)
            print(value)
        
        elif args.file:
            resolved = resolver.resolve_file(args.file)
            print(resolved)
        
        elif args.text:
            resolved = resolver.resolve_template(args.text)
            print(resolved)
        
        else:
            parser.print_help()
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())