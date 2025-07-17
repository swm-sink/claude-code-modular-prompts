"""
Additional tests to achieve 90% coverage for framework parser
These tests cover the missing lines and edge cases
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestFrameworkParserCoverage:
    """Test cases to improve coverage for framework parser"""
    
    def test_parse_method_handles_file_instead_of_directory(self):
        """Test that parse method handles file instead of directory"""
        from data.framework_parser import FrameworkParser
        
        # Create a mock file path
        mock_file_path = Mock(spec=Path)
        mock_file_path.exists.return_value = True
        mock_file_path.is_dir.return_value = False  # This is a file, not directory
        
        parser = FrameworkParser(framework_path=mock_file_path)
        result = parser.parse()
        
        assert result['commands'] == []
        assert result['modules'] == []
        assert result['metadata']['is_valid'] is False
        assert result['metadata']['error'] == "Framework path is not a directory"
    
    def test_validate_framework_with_no_commands(self):
        """Test validation when no commands are found"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock parsed data with no commands
        parser._parsed_data = {
            'commands': [],  # No commands
            'modules': [{'name': 'test-module'}],
            'metadata': {'total_files': 1}
        }
        
        result = parser.validate_framework()
        
        assert result['is_valid'] is False
        assert "No commands found in framework" in result['errors']
        assert result['statistics']['commands_count'] == 0
        assert result['statistics']['modules_count'] == 1
    
    def test_validate_framework_with_no_modules(self):
        """Test validation when no modules are found"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock parsed data with no modules
        parser._parsed_data = {
            'commands': [{'name': 'test-command'}],
            'modules': [],  # No modules
            'metadata': {'total_files': 1}
        }
        
        result = parser.validate_framework()
        
        assert result['is_valid'] is False
        assert "No modules found in framework" in result['errors']
        assert result['statistics']['commands_count'] == 1
        assert result['statistics']['modules_count'] == 0
    
    def test_validate_framework_with_structure_but_no_metadata(self):
        """Test validation when structure exists but no metadata"""
        from data.framework_parser import FrameworkParser
        parser = FrameworkParser()
        
        # Mock parsed data with structure but no metadata
        parser._parsed_data = {
            'commands': [{'name': 'test-command'}],
            'modules': [{'name': 'test-module'}],
            'structure': {'total_files': 42}
            # No metadata key
        }
        
        result = parser.validate_framework()
        
        assert result['is_valid'] is True
        assert result['statistics']['total_files'] == 42
        assert result['statistics']['commands_count'] == 1
        assert result['statistics']['modules_count'] == 1
    
    def test_scan_directory_with_actual_commands(self):
        """Test directory scanning with actual command files"""
        from data.framework_parser import FrameworkParser
        
        # Create a mock parser with framework path
        parser = FrameworkParser()
        
        # Mock the framework path and commands directory
        mock_framework_path = Mock(spec=Path)
        mock_commands_dir = Mock(spec=Path)
        mock_modules_dir = Mock(spec=Path)
        
        # Mock command files
        mock_command_file = Mock(spec=Path)
        mock_command_file.stem = "auto"
        mock_command_file.__str__ = Mock(return_value="/commands/auto.md")
        
        # Setup the mocks
        mock_framework_path.__truediv__.side_effect = lambda x: mock_commands_dir if x == "commands" else mock_modules_dir
        mock_commands_dir.exists.return_value = True
        mock_commands_dir.glob.return_value = [mock_command_file]
        mock_modules_dir.exists.return_value = False
        
        parser.framework_path = mock_framework_path
        
        # Test the scan directory method
        result = parser._scan_directory()
        
        assert len(result['commands']) == 1
        assert result['commands'][0]['name'] == "auto"
        assert result['commands'][0]['category'] == 'command'
        assert result['structure']['commands']['count'] == 1
    
    def test_scan_directory_with_actual_modules(self):
        """Test directory scanning with actual module files"""
        from data.framework_parser import FrameworkParser
        
        # Create a mock parser with framework path
        parser = FrameworkParser()
        
        # Mock the framework path and directories
        mock_framework_path = Mock(spec=Path)
        mock_commands_dir = Mock(spec=Path)
        mock_modules_dir = Mock(spec=Path)
        
        # Mock module files with different categories
        mock_module_file1 = Mock(spec=Path)
        mock_module_file1.stem = "tdd-cycle-pattern"
        mock_module_file1.__str__ = Mock(return_value="/modules/patterns/tdd-cycle-pattern.md")
        mock_module_file1.relative_to.return_value = Path("patterns/tdd-cycle-pattern.md")
        
        mock_module_file2 = Mock(spec=Path)
        mock_module_file2.stem = "intelligent-routing"
        mock_module_file2.__str__ = Mock(return_value="/modules/patterns/intelligent-routing.md")
        mock_module_file2.relative_to.return_value = Path("patterns/intelligent-routing.md")
        
        # Setup the mocks
        mock_framework_path.__truediv__.side_effect = lambda x: mock_commands_dir if x == "commands" else mock_modules_dir
        mock_commands_dir.exists.return_value = False
        mock_modules_dir.exists.return_value = True
        mock_modules_dir.glob.return_value = [mock_module_file1, mock_module_file2]
        
        parser.framework_path = mock_framework_path
        
        # Test the scan directory method
        result = parser._scan_directory()
        
        assert len(result['modules']) == 2
        assert result['modules'][0]['name'] == "tdd-cycle-pattern"
        assert result['modules'][0]['category'] == 'patterns'
        assert result['modules'][1]['name'] == "intelligent-routing"
        assert result['modules'][1]['category'] == 'patterns'
        assert result['structure']['modules']['count'] == 2
    
    def test_group_modules_by_category(self):
        """Test module grouping by category"""
        from data.framework_parser import FrameworkParser
        
        parser = FrameworkParser()
        
        # Test modules with different categories
        modules = [
            {'name': 'tdd-cycle-pattern', 'category': 'patterns'},
            {'name': 'intelligent-routing', 'category': 'patterns'},
            {'name': 'security-validator', 'category': 'security'},
            {'name': 'context-manager', 'category': 'context'}
        ]
        
        result = parser._group_modules_by_category(modules)
        
        assert 'patterns' in result
        assert 'security' in result
        assert 'context' in result
        assert len(result['patterns']) == 2
        assert len(result['security']) == 1
        assert len(result['context']) == 1
        assert result['patterns'][0]['name'] == 'tdd-cycle-pattern'
        assert result['security'][0]['name'] == 'security-validator'
    
    def test_scan_directory_with_single_level_modules(self):
        """Test module scanning with single level modules (no subdirectory)"""
        from data.framework_parser import FrameworkParser
        
        parser = FrameworkParser()
        
        # Mock the framework path and directories
        mock_framework_path = Mock(spec=Path)
        mock_commands_dir = Mock(spec=Path)
        mock_modules_dir = Mock(spec=Path)
        
        # Mock module file with no subdirectory (single level)
        mock_module_file = Mock(spec=Path)
        mock_module_file.stem = "single-module"
        mock_module_file.__str__ = Mock(return_value="/modules/single-module.md")
        mock_module_file.relative_to.return_value = Path("single-module.md")
        
        # Setup the mocks
        mock_framework_path.__truediv__.side_effect = lambda x: mock_commands_dir if x == "commands" else mock_modules_dir
        mock_commands_dir.exists.return_value = False
        mock_modules_dir.exists.return_value = True
        mock_modules_dir.glob.return_value = [mock_module_file]
        
        parser.framework_path = mock_framework_path
        
        # Test the scan directory method
        result = parser._scan_directory()
        
        assert len(result['modules']) == 1
        assert result['modules'][0]['name'] == "single-module"
        assert result['modules'][0]['category'] == 'general'  # Should default to 'general'
    
    def test_full_integration_with_real_directory_structure(self):
        """Test full integration with simulated real directory structure"""
        from data.framework_parser import FrameworkParser
        
        parser = FrameworkParser()
        
        # Mock the actual .claude directory scanning
        with patch('pathlib.Path.exists', return_value=True), \
             patch('pathlib.Path.is_dir', return_value=True), \
             patch('pathlib.Path.glob') as mock_glob:
            
            # Mock the glob calls for total file count
            mock_glob.return_value = ['file1.md', 'file2.md', 'file3.md']
            
            # Mock the directory scanning
            with patch.object(parser, '_scan_directory') as mock_scan:
                mock_scan.return_value = {
                    'commands': [
                        {'name': 'auto', 'path': '/commands/auto.md', 'category': 'command'},
                        {'name': 'task', 'path': '/commands/task.md', 'category': 'command'}
                    ],
                    'modules': [
                        {'name': 'tdd-cycle-pattern', 'path': '/modules/patterns/tdd-cycle-pattern.md', 'category': 'patterns'},
                        {'name': 'intelligent-routing', 'path': '/modules/patterns/intelligent-routing.md', 'category': 'patterns'}
                    ],
                    'structure': {
                        'commands': {'count': 2, 'files': []},
                        'modules': {'count': 2, 'categories': {}},
                        'total_files': 4
                    }
                }
                
                result = parser.parse()
                
                # Verify full structure
                assert len(result['commands']) == 2
                assert len(result['modules']) == 2
                assert result['metadata']['is_valid'] is True
                assert result['metadata']['total_files'] == 3  # From glob mock
                
                # Test validation
                validation = parser.validate_framework()
                assert validation['is_valid'] is True
                assert validation['statistics']['commands_count'] == 2
                assert validation['statistics']['modules_count'] == 2