"""
Framework Parser for .claude directory structure
Parses and analyzes the modular prompt framework components
"""

from pathlib import Path
import re
from typing import Dict, List, Optional, Any


# Sentinel value to distinguish between no argument and explicit None
_UNSET = object()

# Constants for directory and file structure
class FrameworkConstants:
    """Constants for framework structure"""
    COMMANDS_DIR = "commands"
    MODULES_DIR = "modules"
    FILE_EXTENSION = "*.md"
    DEFAULT_CATEGORY = "general"
    COMMAND_CATEGORY = "command"
    
    # Error messages
    ERROR_NOT_FOUND = "Framework directory not found"
    ERROR_NOT_DIR = "Framework path is not a directory"
    ERROR_NO_COMMANDS = "No commands found in framework"
    ERROR_NO_MODULES = "No modules found in framework"


class FrameworkParser:
    """Parser for .claude directory structure and framework components"""
    
    def __init__(self, framework_path=_UNSET):
        """Initialize the framework parser"""
        if framework_path is _UNSET:
            # Default to .claude directory in parent of parent directory
            self.framework_path = Path(__file__).parent.parent.parent / ".claude"
        elif framework_path is None:
            raise ValueError("framework_path cannot be None")
        else:
            if not isinstance(framework_path, Path):
                raise TypeError("framework_path must be a Path object")
            self.framework_path = framework_path
        
        self._parsed_data: Optional[Dict[str, Any]] = None
    
    def parse(self) -> Dict[str, Any]:
        """Parse the framework directory and return structured data"""
        if not self.framework_path.exists():
            return self._create_empty_result(is_valid=False, error=FrameworkConstants.ERROR_NOT_FOUND)
        
        if not self.framework_path.is_dir():
            return self._create_empty_result(is_valid=False, error=FrameworkConstants.ERROR_NOT_DIR)
        
        # Scan the directory structure
        scan_result = self._scan_directory()
        
        # Create structured result
        result = {
            'commands': scan_result.get('commands', []),
            'modules': scan_result.get('modules', []),
            'structure': scan_result.get('structure', {}),
            'metadata': {
                'framework_path': str(self.framework_path),
                'is_valid': True,
                'total_files': len(list(self.framework_path.glob('**/*.md'))),
                'parsed_at': self._get_current_timestamp()
            }
        }
        
        # Store parsed data for later access
        self._parsed_data = result
        return result
    
    def get_commands(self) -> List[Dict[str, Any]]:
        """Get list of parsed commands"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before accessing commands")
        return self._parsed_data['commands']
    
    def get_modules(self) -> List[Dict[str, Any]]:
        """Get list of parsed modules"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before accessing modules")
        return self._parsed_data['modules']
    
    def get_directory_structure(self) -> Dict[str, Any]:
        """Get directory structure information"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before accessing structure")
        return self._parsed_data['structure']
    
    def validate_framework(self) -> Dict[str, Any]:
        """Validate the parsed framework data"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before validation")
        
        errors = []
        warnings = []
        
        # Validate commands
        commands = self._parsed_data['commands']
        if len(commands) == 0:
            errors.append(FrameworkConstants.ERROR_NO_COMMANDS)
        
        # Validate modules
        modules = self._parsed_data['modules']
        if len(modules) == 0:
            errors.append(FrameworkConstants.ERROR_NO_MODULES)
        
        # Create validation result
        is_valid = len(errors) == 0
        
        # Get total files from metadata if available, otherwise calculate from structure
        total_files = 0
        if 'metadata' in self._parsed_data:
            total_files = self._parsed_data['metadata']['total_files']
        elif 'structure' in self._parsed_data:
            total_files = self._parsed_data['structure'].get('total_files', 0)
        
        return {
            'is_valid': is_valid,
            'errors': errors,
            'warnings': warnings,
            'statistics': {
                'commands_count': len(commands),
                'modules_count': len(modules),
                'total_files': total_files
            }
        }
    
    def _scan_directory(self) -> Dict[str, Any]:
        """Scan the .claude directory and extract components"""
        commands = []
        modules = []
        structure = {}
        
        # Scan commands directory
        commands_dir = self.framework_path / FrameworkConstants.COMMANDS_DIR
        if commands_dir.exists():
            for command_file in commands_dir.glob(FrameworkConstants.FILE_EXTENSION):
                commands.append(self._create_command_entry(command_file))
        
        # Scan modules directory
        modules_dir = self.framework_path / FrameworkConstants.MODULES_DIR
        if modules_dir.exists():
            for module_file in modules_dir.glob("**/" + FrameworkConstants.FILE_EXTENSION):
                modules.append(self._create_module_entry(module_file, modules_dir))
        
        # Build structure information
        structure = self._build_structure_info(commands, modules)
        
        return {
            'commands': commands,
            'modules': modules,
            'structure': structure
        }
    
    def _group_modules_by_category(self, modules: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Group modules by category"""
        categories = {}
        for module in modules:
            category = module['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(module)
        return categories
    
    def _build_structure_info(self, commands: List[Dict[str, Any]], modules: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Build structure information from commands and modules"""
        return {
            'commands': {
                'count': len(commands),
                'files': commands
            },
            'modules': {
                'count': len(modules),
                'categories': self._group_modules_by_category(modules)
            },
            'total_files': len(commands) + len(modules)
        }
    
    def _create_command_entry(self, command_file: Path) -> Dict[str, Any]:
        """Create a command entry from a file path"""
        return {
            'name': command_file.stem,
            'path': str(command_file),
            'category': FrameworkConstants.COMMAND_CATEGORY
        }
    
    def _create_module_entry(self, module_file: Path, modules_dir: Path) -> Dict[str, Any]:
        """Create a module entry from a file path"""
        # Determine category from path
        parts = module_file.relative_to(modules_dir).parts
        category = parts[0] if len(parts) > 1 else FrameworkConstants.DEFAULT_CATEGORY
        
        return {
            'name': module_file.stem,
            'path': str(module_file),
            'category': category
        }
    
    def _create_empty_result(self, is_valid: bool = True, error: str = None) -> Dict[str, Any]:
        """Create an empty result structure"""
        return {
            'commands': [],
            'modules': [],
            'structure': {
                'commands': {'count': 0, 'files': []},
                'modules': {'count': 0, 'categories': {}},
                'total_files': 0
            },
            'metadata': {
                'framework_path': str(self.framework_path),
                'is_valid': is_valid,
                'total_files': 0,
                'parsed_at': self._get_current_timestamp(),
                'error': error
            }
        }
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp for metadata"""
        from datetime import datetime
        return datetime.now().isoformat()