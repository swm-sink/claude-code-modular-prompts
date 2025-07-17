"""
TDD RED: Tests for framework parser
These tests define the expected behavior of the .claude directory parser
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestFrameworkParser:
    """Test cases for framework parser functionality"""
    
    def test_framework_parser_module_exists(self):
        """Test that framework parser module exists"""
        from data.framework_parser import FrameworkParser
        assert FrameworkParser is not None
    
    def test_framework_parser_has_parse_method(self):
        """Test that FrameworkParser has a parse method"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        assert hasattr(parser, 'parse'), "FrameworkParser should have parse() method"
        assert callable(parser.parse), "parse should be callable"
    
    def test_framework_parser_has_get_commands_method(self):
        """Test that FrameworkParser has get_commands method"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        assert hasattr(parser, 'get_commands'), "FrameworkParser should have get_commands() method"
        assert callable(parser.get_commands), "get_commands should be callable"
    
    def test_framework_parser_has_get_modules_method(self):
        """Test that FrameworkParser has get_modules method"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        assert hasattr(parser, 'get_modules'), "FrameworkParser should have get_modules() method"
        assert callable(parser.get_modules), "get_modules should be callable"
    
    def test_framework_parser_has_get_directory_structure_method(self):
        """Test that FrameworkParser has get_directory_structure method"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        assert hasattr(parser, 'get_directory_structure'), "FrameworkParser should have get_directory_structure() method"
        assert callable(parser.get_directory_structure), "get_directory_structure should be callable"
    
    def test_framework_parser_has_validate_framework_method(self):
        """Test that FrameworkParser has validate_framework method"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        assert hasattr(parser, 'validate_framework'), "FrameworkParser should have validate_framework() method"
        assert callable(parser.validate_framework), "validate_framework should be callable"
    
    def test_framework_parser_initialization_with_path(self):
        """Test FrameworkParser initialization with custom path"""
        from data.framework_parser import FrameworkParser
        test_path = Path("/test/path")
        parser = FrameworkParser(framework_path=test_path)
        assert parser.framework_path == test_path
    
    def test_framework_parser_initialization_without_path(self):
        """Test FrameworkParser initialization with default path"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        assert parser.framework_path is not None
        assert isinstance(parser.framework_path, Path)
    
    def test_framework_parser_file_size_constraint(self):
        """Test that framework_parser.py is under 500 lines"""
        parser_path = Path(__file__).parent.parent / "data" / "framework_parser.py"
        assert parser_path.exists(), "framework_parser.py should exist"
        
        with open(parser_path, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines and comments for more accurate count
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        assert len(code_lines) < 500, f"framework_parser.py should be <500 lines of code, found {len(code_lines)}"


class TestFrameworkParserParsing:
    """Test cases for framework parsing functionality"""
    
    def test_parse_method_returns_framework_data(self):
        """Test that parse method returns structured framework data"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock the framework path to avoid dependency on actual .claude directory
        parser.framework_path = Path("/mock/path")
        
        with patch.object(parser, '_scan_directory') as mock_scan:
            mock_scan.return_value = {
                'commands': [],
                'modules': [],
                'structure': {}
            }
            
            result = parser.parse()
            
            assert isinstance(result, dict), "parse() should return a dictionary"
            assert 'commands' in result, "Result should contain 'commands' key"
            assert 'modules' in result, "Result should contain 'modules' key"
            assert 'structure' in result, "Result should contain 'structure' key"
            assert 'metadata' in result, "Result should contain 'metadata' key"
    
    def test_get_commands_returns_list(self):
        """Test that get_commands returns a list of command objects"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock parsed data
        parser._parsed_data = {
            'commands': [
                {'name': 'auto', 'path': '/commands/auto.md'},
                {'name': 'task', 'path': '/commands/task.md'}
            ]
        }
        
        commands = parser.get_commands()
        
        assert isinstance(commands, list), "get_commands() should return a list"
        assert len(commands) == 2, "Should return 2 commands"
        assert all('name' in cmd for cmd in commands), "All commands should have 'name' key"
        assert all('path' in cmd for cmd in commands), "All commands should have 'path' key"
    
    def test_get_modules_returns_list(self):
        """Test that get_modules returns a list of module objects"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock parsed data
        parser._parsed_data = {
            'modules': [
                {'name': 'tdd-cycle-pattern', 'category': 'patterns', 'path': '/modules/patterns/tdd-cycle-pattern.md'},
                {'name': 'intelligent-routing', 'category': 'patterns', 'path': '/modules/patterns/intelligent-routing.md'}
            ]
        }
        
        modules = parser.get_modules()
        
        assert isinstance(modules, list), "get_modules() should return a list"
        assert len(modules) == 2, "Should return 2 modules"
        assert all('name' in mod for mod in modules), "All modules should have 'name' key"
        assert all('category' in mod for mod in modules), "All modules should have 'category' key"
        assert all('path' in mod for mod in modules), "All modules should have 'path' key"
    
    def test_get_directory_structure_returns_dict(self):
        """Test that get_directory_structure returns structured data"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock parsed data
        parser._parsed_data = {
            'structure': {
                'commands': {'count': 21, 'files': []},
                'modules': {'count': 64, 'categories': {}},
                'total_files': 165
            }
        }
        
        structure = parser.get_directory_structure()
        
        assert isinstance(structure, dict), "get_directory_structure() should return a dictionary"
        assert 'commands' in structure, "Structure should contain 'commands' key"
        assert 'modules' in structure, "Structure should contain 'modules' key"
        assert 'total_files' in structure, "Structure should contain 'total_files' key"
    
    def test_validate_framework_returns_validation_result(self):
        """Test that validate_framework returns validation results"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock parsed data
        parser._parsed_data = {
            'commands': [{'name': 'auto'}, {'name': 'task'}],
            'modules': [{'name': 'tdd-cycle-pattern'}, {'name': 'intelligent-routing'}],
            'structure': {'total_files': 165}
        }
        
        result = parser.validate_framework()
        
        assert isinstance(result, dict), "validate_framework() should return a dictionary"
        assert 'is_valid' in result, "Result should contain 'is_valid' key"
        assert 'errors' in result, "Result should contain 'errors' key"
        assert 'warnings' in result, "Result should contain 'warnings' key"
        assert 'statistics' in result, "Result should contain 'statistics' key"
    
    def test_parse_method_handles_missing_directory(self):
        """Test that parse method handles missing .claude directory gracefully"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser(framework_path=Path("/nonexistent/path"))
        
        result = parser.parse()
        
        assert isinstance(result, dict), "parse() should return a dictionary even for missing directory"
        assert result['commands'] == [], "Commands should be empty list for missing directory"
        assert result['modules'] == [], "Modules should be empty list for missing directory"
        assert result['metadata']['is_valid'] is False, "Should indicate invalid framework"
    
    def test_parse_method_handles_empty_directory(self):
        """Test that parse method handles empty .claude directory"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        with patch('pathlib.Path.exists', return_value=True), \
             patch('pathlib.Path.is_dir', return_value=True), \
             patch('pathlib.Path.glob', return_value=[]):
            
            result = parser.parse()
            
            assert isinstance(result, dict), "parse() should return a dictionary for empty directory"
            assert result['commands'] == [], "Commands should be empty list for empty directory"
            assert result['modules'] == [], "Modules should be empty list for empty directory"


class TestFrameworkParserEdgeCases:
    """Test cases for edge cases and error conditions"""
    
    def test_framework_parser_with_none_path(self):
        """Test FrameworkParser handles None path gracefully"""
        from data.framework_parser import FrameworkParser
        
        with pytest.raises(ValueError, match="framework_path cannot be None"):
            FrameworkParser(framework_path=None)
    
    def test_framework_parser_with_invalid_path_type(self):
        """Test FrameworkParser handles invalid path type"""
        from data.framework_parser import FrameworkParser
        
        with pytest.raises(TypeError, match="framework_path must be a Path object"):
            FrameworkParser(framework_path="string_path")
    
    def test_get_commands_without_parsing(self):
        """Test get_commands raises error when called before parsing"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        with pytest.raises(RuntimeError, match="Must call parse\\(\\) before accessing commands"):
            parser.get_commands()
    
    def test_get_modules_without_parsing(self):
        """Test get_modules raises error when called before parsing"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        with pytest.raises(RuntimeError, match="Must call parse\\(\\) before accessing modules"):
            parser.get_modules()
    
    def test_get_directory_structure_without_parsing(self):
        """Test get_directory_structure raises error when called before parsing"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        with pytest.raises(RuntimeError, match="Must call parse\\(\\) before accessing structure"):
            parser.get_directory_structure()
    
    def test_validate_framework_without_parsing(self):
        """Test validate_framework raises error when called before parsing"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        with pytest.raises(RuntimeError, match="Must call parse\\(\\) before validation"):
            parser.validate_framework()
    
    def test_framework_parser_follows_separation_of_concerns(self):
        """Test that framework parser follows single responsibility principle"""
        from data.framework_parser import FrameworkParser
        import inspect
        
        # Get all methods in FrameworkParser
        methods = [name for name, obj in inspect.getmembers(FrameworkParser) if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        # Should have focused responsibility - parsing .claude directory only
        expected_methods = ['parse', 'get_commands', 'get_modules', 'get_directory_structure', 'validate_framework']
        
        public_methods = [m for m in methods if not m.startswith('_') and m != '__init__']
        
        # Check that we don't have excessive methods (separation of concerns)
        assert len(public_methods) <= 7, f"Parser should have ≤7 public methods, found {len(public_methods)}: {public_methods}"
        
        # Check that essential methods exist
        for method in expected_methods:
            assert method in public_methods, f"Missing required method: {method}"
    
    def test_framework_parser_imports_are_minimal(self):
        """Test that framework_parser.py has minimal imports"""
        parser_path = Path(__file__).parent.parent / "data" / "framework_parser.py"
        with open(parser_path, 'r') as f:
            source = f.read()
        
        # Should import only necessary modules
        assert "from pathlib import Path" in source, "Should import Path for file operations"
        
        # Should NOT import UI or business logic modules
        forbidden_imports = [
            "import streamlit",
            "from components.",
            "from app import",
            "import plotly",
            "import pandas"
        ]
        
        for forbidden in forbidden_imports:
            assert forbidden not in source, f"Parser should not import UI/business logic: {forbidden}"