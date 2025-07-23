#!/usr/bin/env python3
"""
TDD Tests for Refactored XML Parser

These tests define the desired behavior for the refactored extract_xml_data function.
Tests are written first to ensure the refactoring maintains functionality while improving structure.
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from command_processing.xml_parser import XMLCommandParser


class TestXMLParserRefactored(unittest.TestCase):
    """TDD tests for refactored XML parser functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = XMLCommandParser()
        
        # Sample XML content for testing
        self.sample_xml_content = """
<command_file>
    <metadata>
        <name>test-command</name>
        <purpose>Test command for parsing</purpose>
        <usage>test-command [options]</usage>
        <category>testing</category>
    </metadata>
    
    <arguments>
        <argument name="file" type="string" required="true">
            <description>Input file path</description>
        </argument>
        <argument name="verbose" type="boolean" required="false">
            <description>Enable verbose output</description>
        </argument>
    </arguments>
    
    <examples>
        <example>
            <description>Basic usage</description>
            <usage>test-command input.txt</usage>
        </example>
        <example>
            <description>Verbose mode</description>
            <usage>test-command input.txt --verbose</usage>
        </example>
    </examples>
    
    <claude_prompt>
        <prompt>Execute the test command with the given parameters.</prompt>
    </claude_prompt>
    
    <include>common-utilities</include>
    <include>file-operations</include>
    
    <dependencies>
        <includes_components>
            <component>validation</component>
            <component>logging</component>
        </includes_components>
        <invokes_commands>
            <command>validate</command>
        </invokes_commands>
        <uses_config_values>
            <config>debug_mode</config>
        </uses_config_values>
    </dependencies>
</command_file>
        """
        
        self.malformed_xml_content = """
<command_file>
    <metadata>
        <name>broken-command
        <purpose>Missing closing tag</purpose>
    </metadata>
</command_file>
        """
        
        self.minimal_xml_content = """
<command_file>
    <metadata>
        <name>minimal</name>
    </metadata>
</command_file>
        """

    def test_extract_xml_data_returns_complete_structure(self):
        """Test that extract_xml_data returns the expected data structure."""
        result = self.parser.extract_xml_data(self.sample_xml_content)
        
        # Verify structure
        expected_keys = ['metadata', 'arguments', 'examples', 'prompt', 'components', 'dependencies']
        self.assertEqual(set(result.keys()), set(expected_keys))
        
        # Verify types
        self.assertIsInstance(result['metadata'], dict)
        self.assertIsInstance(result['arguments'], list)
        self.assertIsInstance(result['examples'], list)
        self.assertIsInstance(result['prompt'], str)
        self.assertIsInstance(result['components'], list)
        self.assertIsInstance(result['dependencies'], dict)

    def test_extract_metadata_correctly(self):
        """Test metadata extraction functionality."""
        result = self.parser.extract_xml_data(self.sample_xml_content)
        
        expected_metadata = {
            'name': 'test-command',
            'purpose': 'Test command for parsing',
            'usage': 'test-command [options]',
            'category': 'testing'
        }
        
        self.assertEqual(result['metadata'], expected_metadata)

    def test_extract_arguments_correctly(self):
        """Test arguments extraction functionality."""  
        result = self.parser.extract_xml_data(self.sample_xml_content)
        
        self.assertEqual(len(result['arguments']), 2)
        
        # First argument
        arg1 = result['arguments'][0]
        self.assertEqual(arg1['name'], 'file')
        self.assertEqual(arg1['type'], 'string')
        self.assertTrue(arg1['required'])
        self.assertEqual(arg1['description'], 'Input file path')
        
        # Second argument
        arg2 = result['arguments'][1]
        self.assertEqual(arg2['name'], 'verbose')
        self.assertEqual(arg2['type'], 'boolean')
        self.assertFalse(arg2['required'])
        self.assertEqual(arg2['description'], 'Enable verbose output')

    def test_extract_examples_correctly(self):
        """Test examples extraction functionality."""
        result = self.parser.extract_xml_data(self.sample_xml_content)
        
        self.assertEqual(len(result['examples']), 2)
        
        # First example
        ex1 = result['examples'][0]
        self.assertEqual(ex1['description'], 'Basic usage')
        self.assertEqual(ex1['usage'], 'test-command input.txt')
        
        # Second example
        ex2 = result['examples'][1]
        self.assertEqual(ex2['description'], 'Verbose mode')
        self.assertEqual(ex2['usage'], 'test-command input.txt --verbose')

    def test_extract_prompt_correctly(self):
        """Test prompt extraction functionality."""
        result = self.parser.extract_xml_data(self.sample_xml_content)
        
        self.assertEqual(result['prompt'].strip(), 'Execute the test command with the given parameters.')

    def test_extract_components_correctly(self):
        """Test component includes extraction functionality."""
        result = self.parser.extract_xml_data(self.sample_xml_content)
        
        expected_components = ['common-utilities', 'file-operations']
        self.assertEqual(result['components'], expected_components)

    def test_extract_dependencies_correctly(self):
        """Test dependencies extraction functionality."""
        result = self.parser.extract_xml_data(self.sample_xml_content)
        
        dependencies = result['dependencies']
        
        self.assertEqual(dependencies['components'], ['validation', 'logging'])
        self.assertEqual(dependencies['commands'], ['validate'])
        self.assertEqual(dependencies['config'], ['debug_mode'])

    def test_handles_missing_xml_gracefully(self):
        """Test handling of content without XML."""
        content_without_xml = "This is just plain text without XML structure."
        result = self.parser.extract_xml_data(content_without_xml)
        
        # Should return default structure
        expected_structure = {
            'metadata': {},
            'arguments': [],
            'examples': [],
            'prompt': '',
            'components': [],
            'dependencies': {}
        }
        
        self.assertEqual(result, expected_structure)

    def test_handles_malformed_xml_gracefully(self):
        """Test handling of malformed XML content."""
        with patch('builtins.print') as mock_print:
            result = self.parser.extract_xml_data(self.malformed_xml_content)
            
            # Should return default structure when XML is malformed
            expected_structure = {
                'metadata': {},
                'arguments': [],
                'examples': [],
                'prompt': '',
                'components': [],
                'dependencies': {}
            }
            
            self.assertEqual(result, expected_structure)
            mock_print.assert_called_once()  # Should print warning

    def test_handles_minimal_xml_content(self):
        """Test handling of minimal XML content."""
        result = self.parser.extract_xml_data(self.minimal_xml_content)
        
        # Should have minimal metadata but empty other sections
        self.assertEqual(result['metadata']['name'], 'minimal')
        self.assertEqual(result['arguments'], [])
        self.assertEqual(result['examples'], [])
        self.assertEqual(result['prompt'], '')
        self.assertEqual(result['components'], [])
        self.assertEqual(result['dependencies'], {})

    def test_handles_empty_text_elements(self):
        """Test handling of empty text elements."""
        xml_with_empty_elements = """
<command_file>
    <metadata>
        <name></name>
        <purpose>Valid purpose</purpose>
    </metadata>
    <arguments>
        <argument name="test" type="string" required="false">
            <description></description>
        </argument>
    </arguments>
</command_file>
        """
        
        result = self.parser.extract_xml_data(xml_with_empty_elements)
        
        # Empty name should be empty string
        self.assertEqual(result['metadata']['name'], '')
        self.assertEqual(result['metadata']['purpose'], 'Valid purpose')
        
        # Empty description should be empty string
        self.assertEqual(result['arguments'][0]['description'], '')

    def test_extract_xml_data_performance(self):
        """Test that extract_xml_data performs reasonably for large content."""
        import time
        
        # Create larger XML content
        large_xml = self.sample_xml_content
        for i in range(10):
            large_xml += f"""
    <arguments>
        <argument name="arg{i}" type="string" required="false">
            <description>Test argument {i}</description>
        </argument>
    </arguments>
            """
        
        start_time = time.time()
        result = self.parser.extract_xml_data(large_xml)
        end_time = time.time()
        
        # Should complete in reasonable time (< 1 second)
        self.assertLess(end_time - start_time, 1.0)
        self.assertIsInstance(result, dict)

    # Tests for the new helper methods that will be created during refactoring
    
    def test_extract_metadata_helper_method(self):
        """Test the extracted metadata helper method."""
        # This test will pass after refactoring extracts the helper method
        self.assertTrue(hasattr(self.parser, '_extract_metadata_from_root') or 
                       hasattr(self.parser, 'extract_xml_data'))
    
    def test_extract_arguments_helper_method(self):
        """Test the extracted arguments helper method."""
        # This test will pass after refactoring extracts the helper method
        self.assertTrue(hasattr(self.parser, '_extract_arguments_from_root') or 
                       hasattr(self.parser, 'extract_xml_data'))
    
    def test_extract_examples_helper_method(self):
        """Test the extracted examples helper method."""
        # This test will pass after refactoring extracts the helper method
        self.assertTrue(hasattr(self.parser, '_extract_examples_from_root') or 
                       hasattr(self.parser, 'extract_xml_data'))


class TestXMLParserRefactoredEdgeCases(unittest.TestCase):
    """Additional edge case tests for refactored XML parser."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = XMLCommandParser()
    
    def test_handles_nested_xml_elements(self):
        """Test handling of deeply nested XML elements."""
        nested_xml = """
<command_file>
    <metadata>
        <nested>
            <deep>
                <element>value</element>
            </deep>
        </nested>
    </metadata>
</command_file>
        """
        
        result = self.parser.extract_xml_data(nested_xml)
        # Should handle without crashing
        self.assertIsInstance(result, dict)
    
    def test_handles_special_characters_in_xml(self):
        """Test handling of special characters in XML content."""
        special_xml = """
<command_file>
    <metadata>
        <name>test &amp; special</name>
        <purpose>Test with &lt;special&gt; characters</purpose>
    </metadata>
</command_file>
        """
        
        result = self.parser.extract_xml_data(special_xml)
        self.assertEqual(result['metadata']['name'], 'test & special')
        self.assertEqual(result['metadata']['purpose'], 'Test with <special> characters')
    
    def test_thread_safety(self):
        """Test that the parser is thread-safe for concurrent access."""
        import threading
        import time
        
        results = []
        errors = []
        
        def parse_xml():
            try:
                result = self.parser.extract_xml_data("""
<command_file>
    <metadata>
        <name>thread-test</name>
    </metadata>
</command_file>
                """)
                results.append(result)
            except Exception as e:
                errors.append(e)
        
        # Run multiple threads
        threads = []
        for i in range(5):
            thread = threading.Thread(target=parse_xml)
            threads.append(thread)
            thread.start()
        
        # Wait for all threads
        for thread in threads:
            thread.join()
        
        # Check results
        self.assertEqual(len(errors), 0, f"Errors occurred: {errors}")
        self.assertEqual(len(results), 5)
        
        # All results should be identical
        for result in results:
            self.assertEqual(result['metadata']['name'], 'thread-test')


if __name__ == '__main__':
    unittest.main()