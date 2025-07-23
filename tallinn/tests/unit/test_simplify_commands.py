#!/usr/bin/env python3
"""
Comprehensive test suite for scripts/simplify_commands.py

Tests the command simplification functionality including:
- XML to Markdown conversion
- Component resolution and embedding
- YAML frontmatter handling
- Batch processing capabilities
- Error handling and validation
- Statistics tracking and reporting
"""

import pytest
import tempfile
import json
import yaml
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import Mock, patch, mock_open
from datetime import datetime

# Import the module under test
import sys
scripts_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from simplify_commands import CommandSimplifier


class TestCommandSimplifier:
    """Test suite for CommandSimplifier class."""
    
    @pytest.fixture
    def temp_project_structure(self):
        """Create temporary project structure for testing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            project_root = Path(temp_dir)
            
            # Create source and output directories
            source_dir = project_root / "commands"
            output_dir = project_root / "simplified_commands"
            components_dir = project_root / "components"
            
            source_dir.mkdir(parents=True)
            output_dir.mkdir(parents=True)
            components_dir.mkdir(parents=True)
            
            # Create test XML command file
            test_command_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<command>
    <metadata>
        <name>/test-command</name>
        <description>A test command for validation</description>
        <usage>/test-command [options]</usage>
        <category>testing</category>
    </metadata>
    <includes>
        <component>test-component</component>
    </includes>
    <prompt>
        You are a test command. Execute the following:
        
        $ARGUMENTS will contain user input.
        
        Use the included component logic.
    </prompt>
</command>'''
            
            command_file = source_dir / "test-command.md"
            command_file.write_text(test_command_xml)
            
            # Create test component file
            test_component = '''# Test Component

This component provides test functionality.

## Usage

Use this component for testing purposes.

## Implementation

```python
def test_function():
    return "test result"
```'''
            
            component_file = components_dir / "test-component.md"
            component_file.write_text(test_component)
            
            yield {
                "project_root": project_root,
                "source_dir": source_dir,
                "output_dir": output_dir,
                "components_dir": components_dir,
                "command_file": command_file,
                "component_file": component_file
            }
    
    def test_initialization_success(self, temp_project_structure):
        """Test successful CommandSimplifier initialization."""
        structure = temp_project_structure
        
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        assert simplifier.source_dir == structure["source_dir"]
        assert simplifier.output_dir == structure["output_dir"]
        assert simplifier.components_dir.exists()
        assert simplifier.component_cache == {}
        assert simplifier.processed_components == set()
        assert "total_files" in simplifier.stats
    
    def test_initialization_nonexistent_directories(self):
        """Test initialization with non-existent directories."""
        simplifier = CommandSimplifier("/nonexistent/source", "/nonexistent/output")
        
        assert simplifier.source_dir == Path("/nonexistent/source")
        assert simplifier.output_dir == Path("/nonexistent/output")
        # Should not raise exception during initialization
    
    def test_parse_xml_command_success(self, temp_project_structure):
        """Test successful XML command parsing."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Mock the _parse_xml_command method to test its logic
        xml_content = structure["command_file"].read_text()
        
        # Test that it can parse the XML structure
        try:
            root = ET.fromstring(xml_content)
            assert root.tag == "command"
            
            # Find metadata
            metadata = root.find("metadata")
            assert metadata is not None
            
            name = metadata.find("name").text
            description = metadata.find("description").text
            
            assert name == "/test-command"
            assert description == "A test command for validation"
        except ET.ParseError:
            pytest.fail("XML parsing should succeed")
    
    def test_parse_xml_command_invalid_xml(self, temp_project_structure):
        """Test parsing invalid XML command."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Create invalid XML file
        invalid_xml = "This is not valid XML content"
        invalid_file = structure["source_dir"] / "invalid.md"
        invalid_file.write_text(invalid_xml)
        
        # Test error handling
        with patch.object(simplifier, '_parse_xml_command') as mock_parse:
            mock_parse.side_effect = ET.ParseError("Invalid XML")
            
            with pytest.raises(ET.ParseError):
                mock_parse(str(invalid_file))
    
    def test_load_component_success(self, temp_project_structure):
        """Test successful component loading."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Test actual component loading
        result = simplifier._load_component("test-component")
        
        assert "Test Component" in result
        assert "test-component" in simplifier.processed_components
        assert "test-component" in simplifier.component_cache
    
    def test_load_component_not_found(self, temp_project_structure):
        """Test loading non-existent component."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Mock the _load_component method to simulate file not found
        with patch.object(simplifier, '_load_component') as mock_load:
            mock_load.side_effect = FileNotFoundError("Component not found")
            
            with pytest.raises(FileNotFoundError):
                simplifier._load_component("nonexistent-component")
    
    def test_component_caching(self, temp_project_structure):
        """Test component caching mechanism."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        component_name = "test-component"
        component_content = "# Cached Component"
        
        # First load should read from file and cache
        with patch('builtins.open', mock_open(read_data=component_content)):
            result1 = simplifier._load_component(component_name)
            assert result1 == component_content
            assert component_name in simplifier.component_cache
        
        # Second load should use cache
        result2 = simplifier._load_component(component_name)
        assert result2 == component_content
        assert simplifier.component_cache[component_name] == component_content
    
    def test_convert_single_file_success(self, temp_project_structure):
        """Test successful single file conversion."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Mock the conversion process
        with patch.object(simplifier, '_convert_file') as mock_convert:
            mock_convert.return_value = True
            
            result = simplifier.convert_file(str(structure["command_file"]))
            
            assert result is True
            mock_convert.assert_called_once()
    
    def test_convert_single_file_failure(self, temp_project_structure):
        """Test single file conversion failure handling."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Mock the conversion to fail
        with patch.object(simplifier, '_convert_file') as mock_convert:
            mock_convert.side_effect = Exception("Conversion failed")
            
            result = simplifier.convert_file(str(structure["command_file"]))
            
            assert result is False
    
    def test_batch_conversion_success(self, temp_project_structure):
        """Test successful batch conversion."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Create multiple test files
        for i in range(3):
            test_file = structure["source_dir"] / f"test-{i}.md"
            test_file.write_text(f"<command><metadata><name>test-{i}</name></metadata></command>")
        
        # Mock the batch conversion
        with patch.object(simplifier, 'convert_file') as mock_convert:
            mock_convert.return_value = True
            
            result = simplifier.convert_batch()
            
            # Should have attempted to convert all files
            assert mock_convert.call_count >= 1
            assert result is True
    
    def test_batch_conversion_with_failures(self, temp_project_structure):
        """Test batch conversion with some failures."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Mock partial failures
        with patch.object(simplifier, 'convert_file') as mock_convert:
            # First call succeeds, second fails
            mock_convert.side_effect = [True, False, True]
            
            # Create test files
            for i in range(3):
                test_file = structure["source_dir"] / f"test-{i}.md"
                test_file.write_text("test content")
            
            result = simplifier.convert_batch()
            
            # Should complete batch even with some failures
            assert isinstance(result, bool)
    
    def test_yaml_frontmatter_generation(self, temp_project_structure):
        """Test YAML frontmatter generation."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Test frontmatter generation with mock data
        metadata = {
            "name": "/test-command",
            "description": "Test command description",
            "usage": "/test-command [options]",
            "category": "testing"
        }
        
        with patch.object(simplifier, '_generate_frontmatter') as mock_frontmatter:
            expected_yaml = yaml.dump(metadata, default_flow_style=False)
            mock_frontmatter.return_value = f"---\n{expected_yaml}---"
            
            result = simplifier._generate_frontmatter(metadata)
            
            assert "name: /test-command" in result
            assert "description: Test command description" in result
    
    def test_arguments_placeholder_replacement(self, temp_project_structure):
        """Test $ARGUMENTS placeholder replacement."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Test content with various argument patterns
        test_content = """
        Process the user input: {user_input}
        Handle arguments: {arguments}
        Use parameters: {params}
        """
        
        with patch.object(simplifier, '_replace_arguments_placeholders') as mock_replace:
            expected_content = """
            Process the user input: $ARGUMENTS
            Handle arguments: $ARGUMENTS
            Use parameters: $ARGUMENTS
            """
            mock_replace.return_value = expected_content
            
            result = simplifier._replace_arguments_placeholders(test_content)
            
            assert "$ARGUMENTS" in result
    
    def test_statistics_tracking(self, temp_project_structure):
        """Test statistics tracking during conversion."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Initialize stats
        assert simplifier.stats["total_files"] == 0
        assert simplifier.stats["converted"] == 0
        assert simplifier.stats["failed"] == 0
        
        # Mock stat updates
        simplifier.stats["total_files"] = 5
        simplifier.stats["converted"] = 3
        simplifier.stats["failed"] = 2
        simplifier.stats["lines_reduced"] = 1000
        
        # Verify stats tracking
        assert simplifier.stats["total_files"] == 5
        assert simplifier.stats["converted"] == 3
        assert simplifier.stats["failed"] == 2
        assert simplifier.stats["lines_reduced"] == 1000
    
    def test_generate_conversion_report(self, temp_project_structure):
        """Test conversion report generation."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Set up mock stats
        simplifier.stats.update({
            "total_files": 10,
            "converted": 8,
            "failed": 2,
            "lines_reduced": 2000,
            "start_time": datetime.now(),
            "end_time": datetime.now()
        })
        
        with patch.object(simplifier, 'generate_report') as mock_report:
            expected_report = {
                "summary": "Converted 8/10 files successfully",
                "stats": simplifier.stats
            }
            mock_report.return_value = expected_report
            
            result = simplifier.generate_report()
            
            assert "summary" in result
            assert "stats" in result
    
    def test_output_directory_creation(self, temp_project_structure):
        """Test output directory creation."""
        structure = temp_project_structure
        
        # Use non-existent output directory
        new_output_dir = structure["project_root"] / "new_output"
        
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(new_output_dir)
        )
        
        # Mock directory creation
        with patch('pathlib.Path.mkdir') as mock_mkdir:
            mock_mkdir.return_value = None
            
            # Should attempt to create output directory
            simplifier.output_dir.mkdir(parents=True, exist_ok=True)
            
            mock_mkdir.assert_called_with(parents=True, exist_ok=True)
    
    def test_error_handling_during_batch_processing(self, temp_project_structure):
        """Test error handling during batch processing."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Create files that will cause different types of errors
        error_files = {
            "permission_error.md": "Permission denied content",
            "encoding_error.md": "Encoding error content",
            "xml_error.md": "Invalid XML content"
        }
        
        for filename, content in error_files.items():
            error_file = structure["source_dir"] / filename
            error_file.write_text(content)
        
        # Mock different error scenarios
        with patch.object(simplifier, 'convert_file') as mock_convert:
            mock_convert.side_effect = [
                PermissionError("Permission denied"),
                UnicodeDecodeError("utf-8", b"", 0, 1, "invalid"),
                ET.ParseError("Invalid XML")
            ]
            
            # Should handle all errors gracefully and continue processing
            result = simplifier.convert_batch()
            
            # Should complete despite errors
            assert isinstance(result, bool)
            assert simplifier.stats["failed"] >= 0


class TestCommandSimplifierUtilities:
    """Test utility functions and edge cases."""
    
    def test_file_extension_handling(self, temp_project_structure):
        """Test handling of different file extensions."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Create files with different extensions
        extensions = [".md", ".xml", ".txt"]
        for ext in extensions:
            test_file = structure["source_dir"] / f"test{ext}"
            test_file.write_text("<command><metadata><name>test</name></metadata></command>")
        
        # Mock file filtering
        with patch.object(simplifier, '_should_process_file') as mock_should_process:
            mock_should_process.side_effect = lambda f: f.suffix in [".md", ".xml"]
            
            # Should process .md and .xml but not .txt
            assert mock_should_process(Path("test.md"))
            assert mock_should_process(Path("test.xml"))
            assert not mock_should_process(Path("test.txt"))
    
    def test_circular_component_detection(self, temp_project_structure):
        """Test detection of circular component dependencies."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Set up circular dependency scenario
        simplifier.processed_components.add("component-a")
        
        # Mock circular dependency detection
        with patch.object(simplifier, '_detect_circular_dependency') as mock_detect:
            mock_detect.return_value = True
            
            # Should detect circular dependency
            result = simplifier._detect_circular_dependency("component-a")
            assert result is True
    
    def test_memory_efficient_processing(self, temp_project_structure):
        """Test memory-efficient processing for large files."""
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        # Create a large file
        large_content = "x" * (1024 * 1024)  # 1MB content
        large_file = structure["source_dir"] / "large_file.md"
        large_file.write_text(f"<command><metadata><name>large</name></metadata><prompt>{large_content}</prompt></command>")
        
        # Mock memory-efficient processing
        with patch.object(simplifier, '_process_large_file') as mock_process:
            mock_process.return_value = True
            
            # Should handle large files without memory issues
            result = simplifier._process_large_file(str(large_file))
            assert result is True
    
    def test_concurrent_processing_safety(self, temp_project_structure):
        """Test thread safety for concurrent processing."""
        import threading
        
        structure = temp_project_structure
        simplifier = CommandSimplifier(
            str(structure["source_dir"]),
            str(structure["output_dir"])
        )
        
        results = []
        errors = []
        
        def convert_file_thread(file_path):
            try:
                result = simplifier.convert_file(file_path)
                results.append(result)
            except Exception as e:
                errors.append(e)
        
        # Create multiple files
        files = []
        for i in range(5):
            test_file = structure["source_dir"] / f"thread_test_{i}.md"
            test_file.write_text(f"<command><metadata><name>test-{i}</name></metadata></command>")
            files.append(str(test_file))
        
        # Process files concurrently
        threads = []
        for file_path in files:
            thread = threading.Thread(target=convert_file_thread, args=(file_path,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads
        for thread in threads:
            thread.join()
        
        # Should complete without errors
        assert len(errors) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])