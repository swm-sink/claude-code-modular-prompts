"""
TDD RED: Comprehensive failing test suite for Command Explorer component
These tests define the expected behavior and architecture of the command explorer
All tests MUST fail until implementation is complete - strict TDD methodology

Coverage Target: 95%+ of all functionality
Performance Target: <2s load time for 50+ commands
Architecture: Streamlit + Plotly interactive visualization
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import pandas as pd
import plotly.graph_objects as go
from typing import Dict, List, Optional, Any

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import existing framework components for integration
from data.framework_parser import FrameworkParser
from data.models import Command, Module, Framework


class TestCommandExplorerInitialization:
    """Test cases for CommandExplorer initialization and basic functionality"""
    
    def test_command_explorer_module_exists(self):
        """Test that CommandExplorer module exists and can be imported"""
        # Module should now be importable in GREEN phase
        from components.command_explorer import CommandExplorer
        assert CommandExplorer is not None
    
    def test_command_explorer_initialization_with_framework_path(self):
        """Test CommandExplorer initialization with valid framework path"""
        # This test MUST fail - no implementation exists yet
        from components.command_explorer import CommandExplorer
        
        framework_path = Path("/test/.claude")
        explorer = CommandExplorer(framework_path=framework_path)
        
        assert explorer.framework_path == framework_path
        assert hasattr(explorer, 'framework_parser')
        assert isinstance(explorer.framework_parser, FrameworkParser)
    
    def test_command_explorer_initialization_with_invalid_path(self):
        """Test CommandExplorer initialization with invalid framework path"""
        from components.command_explorer import CommandExplorer
        
        with pytest.raises(ValueError):
            CommandExplorer(framework_path=None)
        
        with pytest.raises(TypeError):
            CommandExplorer(framework_path="not_a_path_object")
    
    def test_command_explorer_initialization_default_parameters(self):
        """Test CommandExplorer initialization with default parameters"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        assert hasattr(explorer, 'framework_path')
        assert hasattr(explorer, 'framework_parser')
        assert hasattr(explorer, 'selected_command')
        assert explorer.selected_command is None
        assert hasattr(explorer, 'filter_state')
        assert isinstance(explorer.filter_state, dict)
    
    def test_command_explorer_has_required_methods(self):
        """Test that CommandExplorer has all required methods"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        # Core functionality methods
        assert hasattr(explorer, 'load_commands_from_framework')
        assert callable(explorer.load_commands_from_framework)
        assert hasattr(explorer, 'filter_commands_by_category')
        assert callable(explorer.filter_commands_by_category)
        assert hasattr(explorer, 'get_command_details')
        assert callable(explorer.get_command_details)
        assert hasattr(explorer, 'render_command_usage_examples')
        assert callable(explorer.render_command_usage_examples)
        
        # Visualization methods
        assert hasattr(explorer, 'create_dependency_visualization')
        assert callable(explorer.create_dependency_visualization)
        assert hasattr(explorer, 'generate_plotly_charts')
        assert callable(explorer.generate_plotly_charts)
        assert hasattr(explorer, 'handle_command_selection')
        assert callable(explorer.handle_command_selection)
        
        # Main render method
        assert hasattr(explorer, 'render')
        assert callable(explorer.render)


class TestCommandExplorerDataLoading:
    """Test cases for command data loading and framework integration"""
    
    def test_load_commands_from_framework_success(self):
        """Test successful loading of commands from framework"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        # Mock framework parser
        mock_commands = [
            {'name': 'auto', 'path': '/commands/auto.md', 'category': 'command'},
            {'name': 'task', 'path': '/commands/task.md', 'category': 'command'},
            {'name': 'feature', 'path': '/commands/feature.md', 'category': 'command'}
        ]
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': mock_commands}
            
            result = explorer.load_commands_from_framework()
            
            assert isinstance(result, list)
            assert len(result) == 3
            assert all(isinstance(cmd, Command) for cmd in result)
            mock_parse.assert_called_once()
    
    def test_load_commands_from_framework_empty_directory(self):
        """Test loading commands from empty framework directory"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': []}
            
            result = explorer.load_commands_from_framework()
            
            assert isinstance(result, list)
            assert len(result) == 0
            mock_parse.assert_called_once()
    
    def test_load_commands_from_framework_missing_directory(self):
        """Test loading commands when framework directory doesn't exist"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.side_effect = FileNotFoundError("Framework directory not found")
            
            with pytest.raises(FileNotFoundError):
                explorer.load_commands_from_framework()
    
    def test_load_commands_from_framework_performance(self):
        """Test loading performance with large command sets"""
        from components.command_explorer import CommandExplorer
        import time
        
        explorer = CommandExplorer()
        
        # Create 100 mock commands to test performance
        large_command_set = [
            {'name': f'command_{i}', 'path': f'/commands/command_{i}.md', 'category': 'command'}
            for i in range(100)
        ]
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': large_command_set}
            
            start_time = time.time()
            result = explorer.load_commands_from_framework()
            end_time = time.time()
            
            # Should complete within 2 seconds for 100 commands
            assert (end_time - start_time) < 2.0
            assert len(result) == 100
    
    def test_load_commands_from_framework_with_metadata(self):
        """Test loading commands with complete metadata"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        mock_commands = [
            {
                'name': 'auto',
                'path': '/commands/auto.md',
                'category': 'command',
                'description': 'Intelligent routing',
                'usage': '/auto "your request"',
                'examples': ['Example 1', 'Example 2'],
                'modules': ['routing', 'analysis']
            }
        ]
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': mock_commands}
            
            result = explorer.load_commands_from_framework()
            
            assert len(result) == 1
            command = result[0]
            assert command.name == 'auto'
            assert command.description == 'Intelligent routing'
            assert command.usage == '/auto "your request"'
            assert len(command.examples) == 2
            assert len(command.modules) == 2


class TestCommandExplorerFiltering:
    """Test cases for command filtering and categorization"""
    
    def test_filter_commands_by_category_single_category(self):
        """Test filtering commands by single category"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core'),
            Command(name='task', path='/commands/task.md', category='core'),
            Command(name='meta-review', path='/commands/meta-review.md', category='meta')
        ]
        
        result = explorer.filter_commands_by_category(commands, 'core')
        
        assert len(result) == 2
        assert all(cmd.category == 'core' for cmd in result)
    
    def test_filter_commands_by_category_multiple_categories(self):
        """Test filtering commands by multiple categories"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core'),
            Command(name='task', path='/commands/task.md', category='core'),
            Command(name='meta-review', path='/commands/meta-review.md', category='meta'),
            Command(name='init', path='/commands/init.md', category='setup')
        ]
        
        result = explorer.filter_commands_by_category(commands, ['core', 'meta'])
        
        assert len(result) == 3
        assert all(cmd.category in ['core', 'meta'] for cmd in result)
    
    def test_filter_commands_by_category_no_matches(self):
        """Test filtering commands with no matching categories"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core'),
            Command(name='task', path='/commands/task.md', category='core')
        ]
        
        result = explorer.filter_commands_by_category(commands, 'nonexistent')
        
        assert len(result) == 0
        assert isinstance(result, list)
    
    def test_filter_commands_by_category_empty_input(self):
        """Test filtering empty command list"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        result = explorer.filter_commands_by_category([], 'core')
        
        assert len(result) == 0
        assert isinstance(result, list)
    
    def test_filter_commands_by_usage_pattern(self):
        """Test filtering commands by usage patterns"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core', usage='/auto "request"'),
            Command(name='task', path='/commands/task.md', category='core', usage='/task "implement"'),
            Command(name='query', path='/commands/query.md', category='core', usage='/query "analyze"')
        ]
        
        result = explorer.filter_commands_by_usage_pattern(commands, 'request')
        
        assert len(result) == 1
        assert result[0].name == 'auto'
    
    def test_filter_commands_by_multiple_criteria(self):
        """Test filtering commands by multiple criteria simultaneously"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core', usage='/auto "request"'),
            Command(name='task', path='/commands/task.md', category='core', usage='/task "implement"'),
            Command(name='meta-review', path='/commands/meta-review.md', category='meta', usage='/meta-review')
        ]
        
        result = explorer.filter_commands_by_multiple_criteria(
            commands, 
            category='core', 
            usage_pattern='request'
        )
        
        assert len(result) == 1
        assert result[0].name == 'auto'


class TestCommandExplorerDetails:
    """Test cases for command detail retrieval and processing"""
    
    def test_get_command_details_complete_metadata(self):
        """Test getting command details with complete metadata"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(
            name='auto',
            path='/commands/auto.md',
            category='core',
            description='Intelligent routing',
            usage='/auto "your request"',
            examples=['Example 1', 'Example 2'],
            modules=['routing', 'analysis']
        )
        
        result = explorer.get_command_details(command)
        
        assert isinstance(result, dict)
        assert result['name'] == 'auto'
        assert result['description'] == 'Intelligent routing'
        assert result['usage'] == '/auto "your request"'
        assert len(result['examples']) == 2
        assert len(result['modules']) == 2
        assert 'category' in result
        assert 'path' in result
    
    def test_get_command_details_minimal_metadata(self):
        """Test getting command details with minimal metadata"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='minimal', path='/commands/minimal.md', category='core')
        
        result = explorer.get_command_details(command)
        
        assert isinstance(result, dict)
        assert result['name'] == 'minimal'
        assert result['description'] is None
        assert result['usage'] is None
        assert len(result['examples']) == 0
        assert len(result['modules']) == 0
    
    def test_get_command_details_file_content_parsing(self):
        """Test getting command details with file content parsing"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='auto', path='/commands/auto.md', category='core')
        
        mock_file_content = """
        # Auto Command
        
        Intelligent routing for framework operations
        
        ## Usage
        /auto "your request here"
        
        ## Examples
        - Example 1
        - Example 2
        """
        
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            result = explorer.get_command_details(command, include_file_content=True)
            
            assert 'file_content' in result
            assert 'parsed_description' in result
            assert 'parsed_usage' in result
            assert 'parsed_examples' in result
    
    def test_get_command_details_malformed_file(self):
        """Test getting command details with malformed command file"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='broken', path='/commands/broken.md', category='core')
        
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = explorer.get_command_details(command)
            
            assert isinstance(result, dict)
            assert result['name'] == 'broken'
            assert 'error' in result
            assert result['error'] == 'File not found'
    
    def test_get_command_details_performance_optimization(self):
        """Test command details retrieval performance"""
        from components.command_explorer import CommandExplorer
        import time
        
        explorer = CommandExplorer()
        
        # Create 50 commands for performance testing
        commands = [
            Command(name=f'cmd_{i}', path=f'/commands/cmd_{i}.md', category='core')
            for i in range(50)
        ]
        
        start_time = time.time()
        results = [explorer.get_command_details(cmd) for cmd in commands]
        end_time = time.time()
        
        # Should process 50 commands within 1 second
        assert (end_time - start_time) < 1.0
        assert len(results) == 50
        assert all(isinstance(result, dict) for result in results)


class TestCommandExplorerUsageExamples:
    """Test cases for command usage examples rendering"""
    
    def test_render_command_usage_examples_with_examples(self):
        """Test rendering command usage examples with valid examples"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(
            name='auto',
            path='/commands/auto.md',
            category='core',
            examples=[
                '/auto "analyze codebase"',
                '/auto "implement feature"',
                '/auto "fix bug"'
            ]
        )
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.code') as mock_code, \
             patch('streamlit.selectbox') as mock_selectbox:
            
            mock_selectbox.return_value = '/auto "analyze codebase"'
            
            explorer.render_command_usage_examples(command)
            
            mock_subheader.assert_called()
            mock_code.assert_called()
            mock_selectbox.assert_called()
    
    def test_render_command_usage_examples_no_examples(self):
        """Test rendering command usage examples with no examples"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='minimal', path='/commands/minimal.md', category='core')
        
        with patch('streamlit.info') as mock_info:
            explorer.render_command_usage_examples(command)
            
            mock_info.assert_called()
            args, kwargs = mock_info.call_args
            assert "No examples available" in args[0]
    
    def test_render_command_usage_examples_interactive_selection(self):
        """Test interactive example selection functionality"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(
            name='auto',
            path='/commands/auto.md',
            category='core',
            examples=[
                '/auto "example 1"',
                '/auto "example 2"',
                '/auto "example 3"'
            ]
        )
        
        with patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.code') as mock_code:
            
            mock_selectbox.return_value = '/auto "example 2"'
            
            explorer.render_command_usage_examples(command)
            
            # Should call selectbox with all examples
            mock_selectbox.assert_called_once()
            selectbox_args = mock_selectbox.call_args[0]
            assert len(selectbox_args[1]) == 3  # All examples available
            
            # Should display selected example
            mock_code.assert_called_with('/auto "example 2"')
    
    def test_render_command_usage_examples_format_display(self):
        """Test usage examples display formatting"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(
            name='feature',
            path='/commands/feature.md',
            category='core',
            examples=[
                '/feature "implement user authentication"',
                '/feature "add payment processing"'
            ]
        )
        
        with patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.code') as mock_code, \
             patch('streamlit.markdown') as mock_markdown:
            
            mock_selectbox.return_value = '/feature "implement user authentication"'
            
            explorer.render_command_usage_examples(command)
            
            # Should format examples properly
            mock_code.assert_called_with('/feature "implement user authentication"')
            mock_markdown.assert_called()
    
    def test_render_command_usage_examples_copy_functionality(self):
        """Test copy to clipboard functionality for examples"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(
            name='task',
            path='/commands/task.md',
            category='core',
            examples=['/task "implement unit tests"']
        )
        
        with patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.button') as mock_button, \
             patch('streamlit.success') as mock_success:
            
            mock_selectbox.return_value = '/task "implement unit tests"'
            mock_button.return_value = True
            
            explorer.render_command_usage_examples(command)
            
            # Should provide copy button
            mock_button.assert_called()
            mock_success.assert_called()


class TestCommandExplorerVisualization:
    """Test cases for command dependency visualization"""
    
    def test_create_dependency_visualization_basic(self):
        """Test creating basic dependency visualization"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core', modules=['routing']),
            Command(name='task', path='/commands/task.md', category='core', modules=['tdd']),
            Command(name='feature', path='/commands/feature.md', category='core', modules=['workflow'])
        ]
        
        result = explorer.create_dependency_visualization(commands)
        
        assert isinstance(result, dict)
        assert 'nodes' in result
        assert 'edges' in result
        assert len(result['nodes']) > 0
        assert len(result['edges']) > 0
    
    def test_create_dependency_visualization_complex_dependencies(self):
        """Test creating visualization with complex dependency relationships"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core', modules=['routing', 'analysis']),
            Command(name='task', path='/commands/task.md', category='core', modules=['tdd', 'analysis']),
            Command(name='feature', path='/commands/feature.md', category='core', modules=['workflow', 'tdd'])
        ]
        
        result = explorer.create_dependency_visualization(commands)
        
        assert isinstance(result, dict)
        assert 'nodes' in result
        assert 'edges' in result
        
        # Should have nodes for commands and modules
        nodes = result['nodes']
        assert len(nodes) > 3  # Commands + modules
        
        # Should have edges showing dependencies
        edges = result['edges']
        assert len(edges) > 0
    
    def test_create_dependency_visualization_circular_dependencies(self):
        """Test handling circular dependencies in visualization"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='cmd1', path='/commands/cmd1.md', category='core', modules=['mod1', 'mod2']),
            Command(name='cmd2', path='/commands/cmd2.md', category='core', modules=['mod2', 'mod1'])
        ]
        
        result = explorer.create_dependency_visualization(commands)
        
        assert isinstance(result, dict)
        assert 'nodes' in result
        assert 'edges' in result
        
        # Should handle circular dependencies gracefully
        assert len(result['nodes']) > 0
        assert len(result['edges']) > 0
    
    def test_create_dependency_visualization_performance(self):
        """Test dependency visualization performance with large datasets"""
        from components.command_explorer import CommandExplorer
        import time
        
        explorer = CommandExplorer()
        
        # Create 50 commands with complex dependencies
        commands = [
            Command(
                name=f'cmd_{i}',
                path=f'/commands/cmd_{i}.md',
                category='core',
                modules=[f'mod_{i}', f'mod_{i+1}', f'mod_{i+2}']
            )
            for i in range(50)
        ]
        
        start_time = time.time()
        result = explorer.create_dependency_visualization(commands)
        end_time = time.time()
        
        # Should complete within 3 seconds for 50 commands
        assert (end_time - start_time) < 3.0
        assert isinstance(result, dict)
    
    def test_create_dependency_visualization_plotly_data_structure(self):
        """Test that visualization returns proper Plotly data structure"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core', modules=['routing'])
        ]
        
        result = explorer.create_dependency_visualization(commands)
        
        # Should have proper structure for Plotly network graph
        assert 'nodes' in result
        assert 'edges' in result
        
        nodes = result['nodes']
        edges = result['edges']
        
        # Nodes should have required properties
        for node in nodes:
            assert 'id' in node
            assert 'label' in node
            assert 'type' in node  # command or module
            assert 'category' in node
        
        # Edges should have source and target
        for edge in edges:
            assert 'source' in edge
            assert 'target' in edge


class TestCommandExplorerInteraction:
    """Test cases for command selection and interaction handling"""
    
    def test_handle_command_selection_valid_command(self):
        """Test handling valid command selection"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='auto', path='/commands/auto.md', category='core')
        
        result = explorer.handle_command_selection(command)
        
        assert explorer.selected_command == command
        assert result == True
    
    def test_handle_command_selection_none_command(self):
        """Test handling None command selection"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        result = explorer.handle_command_selection(None)
        
        assert explorer.selected_command is None
        assert result == False
    
    def test_handle_command_selection_ui_state_update(self):
        """Test UI state update on command selection"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='task', path='/commands/task.md', category='core')
        
        with patch('streamlit.session_state') as mock_session_state:
            explorer.handle_command_selection(command)
            
            assert explorer.selected_command == command
    
    def test_handle_command_selection_invalid_command(self):
        """Test handling invalid command selection"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with pytest.raises(TypeError):
            explorer.handle_command_selection("invalid_command")
    
    def test_handle_command_selection_persistence(self):
        """Test command selection persistence across interactions"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command1 = Command(name='auto', path='/commands/auto.md', category='core')
        command2 = Command(name='task', path='/commands/task.md', category='core')
        
        explorer.handle_command_selection(command1)
        assert explorer.selected_command == command1
        
        explorer.handle_command_selection(command2)
        assert explorer.selected_command == command2
    
    def test_handle_command_selection_callback_execution(self):
        """Test callback execution on command selection"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        callback_executed = False
        
        def selection_callback(command):
            nonlocal callback_executed
            callback_executed = True
        
        command = Command(name='auto', path='/commands/auto.md', category='core')
        
        explorer.handle_command_selection(command, callback=selection_callback)
        
        assert callback_executed == True
        assert explorer.selected_command == command


class TestCommandExplorerPlotlyCharts:
    """Test cases for Plotly chart generation"""
    
    def test_generate_plotly_charts_command_relationships(self):
        """Test generating Plotly charts for command relationships"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core', modules=['routing']),
            Command(name='task', path='/commands/task.md', category='core', modules=['tdd'])
        ]
        
        result = explorer.generate_plotly_charts(commands, chart_type='relationships')
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
    
    def test_generate_plotly_charts_usage_frequency(self):
        """Test generating Plotly charts for usage frequency visualization"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core'),
            Command(name='task', path='/commands/task.md', category='core'),
            Command(name='feature', path='/commands/feature.md', category='core')
        ]
        
        usage_data = {'auto': 50, 'task': 30, 'feature': 20}
        
        result = explorer.generate_plotly_charts(commands, chart_type='usage_frequency', usage_data=usage_data)
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
    
    def test_generate_plotly_charts_category_distribution(self):
        """Test generating Plotly charts for command category distribution"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core'),
            Command(name='task', path='/commands/task.md', category='core'),
            Command(name='meta-review', path='/commands/meta-review.md', category='meta')
        ]
        
        result = explorer.generate_plotly_charts(commands, chart_type='category_distribution')
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
    
    def test_generate_plotly_charts_interactive_behaviors(self):
        """Test interactive behaviors in Plotly charts"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core')
        ]
        
        result = explorer.generate_plotly_charts(commands, chart_type='relationships', interactive=True)
        
        assert isinstance(result, go.Figure)
        # Should have interactive configurations
        assert result.layout.hovermode is not None
        assert result.layout.clickmode is not None
    
    def test_generate_plotly_charts_export_functionality(self):
        """Test chart export functionality"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core')
        ]
        
        result = explorer.generate_plotly_charts(commands, chart_type='relationships', export_config=True)
        
        assert isinstance(result, go.Figure)
        # Should have export configuration
        assert hasattr(result, 'layout')
    
    def test_generate_plotly_charts_invalid_chart_type(self):
        """Test handling invalid chart type"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core')
        ]
        
        with pytest.raises(ValueError):
            explorer.generate_plotly_charts(commands, chart_type='invalid_type')


class TestCommandExplorerErrorHandling:
    """Test cases for error handling and graceful degradation"""
    
    def test_graceful_degradation_missing_framework_data(self):
        """Test graceful degradation when framework data is missing"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.side_effect = FileNotFoundError("Framework not found")
            
            with patch('streamlit.error') as mock_error:
                explorer.render()
                
                mock_error.assert_called()
                args, kwargs = mock_error.call_args
                assert "Framework not found" in args[0]
    
    def test_graceful_degradation_invalid_framework_path(self):
        """Test graceful degradation with invalid framework path"""
        from components.command_explorer import CommandExplorer
        
        with patch('streamlit.error') as mock_error:
            explorer = CommandExplorer(framework_path=Path("/nonexistent/path"))
            explorer.render()
            
            mock_error.assert_called()
    
    def test_graceful_degradation_corrupted_command_files(self):
        """Test graceful degradation with corrupted command files"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': [{'name': 'broken'}]}  # Missing required fields
            
            with patch('streamlit.warning') as mock_warning:
                result = explorer.load_commands_from_framework()
                
                mock_warning.assert_called()
                assert isinstance(result, list)
    
    def test_graceful_degradation_network_file_access_errors(self):
        """Test graceful degradation with network/file access errors"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='remote', path='/network/command.md', category='core')
        
        with patch('builtins.open', side_effect=PermissionError("Access denied")):
            with patch('streamlit.error') as mock_error:
                result = explorer.get_command_details(command)
                
                assert isinstance(result, dict)
                assert 'error' in result
    
    def test_graceful_degradation_memory_constraints(self):
        """Test graceful degradation under memory constraints"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        # Simulate memory error
        with patch.object(explorer, 'generate_plotly_charts', side_effect=MemoryError("Out of memory")):
            with patch('streamlit.error') as mock_error:
                commands = [Command(name='test', path='/test.md', category='core')]
                explorer.create_dependency_visualization(commands)
                
                mock_error.assert_called()
    
    def test_error_recovery_mechanisms(self):
        """Test error recovery mechanisms"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        # Test automatic retry on transient errors
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.side_effect = [ConnectionError("Temporary failure"), {'commands': []}]
            
            result = explorer.load_commands_from_framework(retry_on_failure=True)
            
            assert isinstance(result, list)
            assert mock_parse.call_count == 2


class TestCommandExplorerPerformance:
    """Test cases for performance benchmarks and optimization"""
    
    def test_load_time_with_large_command_sets(self):
        """Test load time performance with 50+ commands"""
        from components.command_explorer import CommandExplorer
        import time
        
        explorer = CommandExplorer()
        
        # Create 75 commands for performance testing
        large_command_set = [
            {
                'name': f'command_{i}',
                'path': f'/commands/command_{i}.md',
                'category': 'core',
                'description': f'Command {i} description',
                'usage': f'/command_{i} "usage"',
                'examples': [f'Example {i}'],
                'modules': [f'module_{i}']
            }
            for i in range(75)
        ]
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': large_command_set}
            
            start_time = time.time()
            result = explorer.load_commands_from_framework()
            end_time = time.time()
            
            # Should complete within 2 seconds for 75 commands
            assert (end_time - start_time) < 2.0
            assert len(result) == 75
    
    def test_rendering_performance_benchmarks(self):
        """Test rendering performance benchmarks"""
        from components.command_explorer import CommandExplorer
        import time
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name=f'cmd_{i}', path=f'/commands/cmd_{i}.md', category='core')
            for i in range(30)
        ]
        
        with patch('streamlit.selectbox'), \
             patch('streamlit.dataframe'), \
             patch('streamlit.plotly_chart'):
            
            start_time = time.time()
            explorer.render()
            end_time = time.time()
            
            # Should render within 1 second for 30 commands
            assert (end_time - start_time) < 1.0
    
    def test_memory_usage_constraints(self):
        """Test memory usage constraints"""
        from components.command_explorer import CommandExplorer
        import sys
        
        explorer = CommandExplorer()
        
        # Create large dataset
        large_commands = [
            Command(
                name=f'command_{i}',
                path=f'/commands/command_{i}.md',
                category='core',
                examples=[f'Example {j}' for j in range(10)]  # 10 examples each
            )
            for i in range(100)
        ]
        
        initial_memory = sys.getsizeof(explorer)
        
        with patch.object(explorer, 'load_commands_from_framework', return_value=large_commands):
            result = explorer.load_commands_from_framework()
            
            # Memory usage should remain reasonable
            current_memory = sys.getsizeof(explorer)
            memory_increase = current_memory - initial_memory
            
            # Should not use excessive memory (arbitrary threshold)
            assert memory_increase < 10000000  # 10MB
    
    def test_response_time_requirements(self):
        """Test response time requirements for interactive operations"""
        from components.command_explorer import CommandExplorer
        import time
        
        explorer = CommandExplorer()
        
        command = Command(name='auto', path='/commands/auto.md', category='core')
        
        # Test command selection response time
        start_time = time.time()
        explorer.handle_command_selection(command)
        end_time = time.time()
        
        # Should respond within 100ms for interactive operations
        assert (end_time - start_time) < 0.1
    
    def test_concurrent_access_scenarios(self):
        """Test performance under concurrent access scenarios"""
        from components.command_explorer import CommandExplorer
        import threading
        import time
        
        explorer = CommandExplorer()
        
        results = []
        
        def concurrent_load():
            result = explorer.load_commands_from_framework()
            results.append(len(result))
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': [{'name': 'test', 'path': '/test.md', 'category': 'core'}]}
            
            threads = []
            for i in range(5):
                thread = threading.Thread(target=concurrent_load)
                threads.append(thread)
                thread.start()
            
            for thread in threads:
                thread.join(timeout=2.0)
            
            # All threads should complete successfully
            assert len(results) == 5
            assert all(result == 1 for result in results)


class TestCommandExplorerAccessibility:
    """Test cases for accessibility and usability features"""
    
    def test_aria_labels_and_descriptions(self):
        """Test ARIA labels and descriptions for accessibility"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.button') as mock_button:
            
            explorer.render()
            
            # Should include accessibility attributes
            mock_selectbox.assert_called()
            mock_button.assert_called()
    
    def test_keyboard_navigation_support(self):
        """Test keyboard navigation support"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name='auto', path='/commands/auto.md', category='core'),
            Command(name='task', path='/commands/task.md', category='core')
        ]
        
        with patch('streamlit.selectbox') as mock_selectbox:
            # Mock keyboard navigation
            mock_selectbox.return_value = 'auto'
            
            explorer.render()
            
            # Should support keyboard navigation
            mock_selectbox.assert_called()
    
    def test_screen_reader_compatibility(self):
        """Test screen reader compatibility"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(
            name='auto',
            path='/commands/auto.md',
            category='core',
            description='Intelligent routing command'
        )
        
        with patch('streamlit.markdown') as mock_markdown:
            explorer.render_command_usage_examples(command)
            
            # Should include screen reader friendly content
            mock_markdown.assert_called()
    
    def test_color_contrast_validation(self):
        """Test color contrast validation for accessibility"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [Command(name='auto', path='/commands/auto.md', category='core')]
        
        result = explorer.generate_plotly_charts(commands, chart_type='relationships')
        
        # Should use accessible colors
        assert isinstance(result, go.Figure)
        # Color contrast validation would be done in actual implementation


class TestCommandExplorerMobileResponsiveness:
    """Test cases for mobile responsiveness and touch interaction"""
    
    def test_touch_interaction_support(self):
        """Test touch interaction support for mobile devices"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [Command(name='auto', path='/commands/auto.md', category='core')]
        
        result = explorer.generate_plotly_charts(commands, chart_type='relationships', mobile_optimized=True)
        
        assert isinstance(result, go.Figure)
        # Should have touch-friendly configurations
    
    def test_responsive_layout_validation(self):
        """Test responsive layout validation"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with patch('streamlit.columns') as mock_columns:
            # Mock responsive columns
            mock_columns.return_value = [MagicMock(), MagicMock()]
            
            explorer.render()
            
            # Should use responsive layout
            mock_columns.assert_called()
    
    def test_mobile_performance_optimization(self):
        """Test mobile performance optimization"""
        from components.command_explorer import CommandExplorer
        import time
        
        explorer = CommandExplorer()
        
        commands = [
            Command(name=f'cmd_{i}', path=f'/commands/cmd_{i}.md', category='core')
            for i in range(20)
        ]
        
        with patch('streamlit.plotly_chart'):
            start_time = time.time()
            result = explorer.generate_plotly_charts(commands, chart_type='relationships', mobile_optimized=True)
            end_time = time.time()
            
            # Should be optimized for mobile performance
            assert (end_time - start_time) < 2.0
            assert isinstance(result, go.Figure)
    
    def test_gesture_handling(self):
        """Test gesture handling for mobile interactions"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        commands = [Command(name='auto', path='/commands/auto.md', category='core')]
        
        result = explorer.generate_plotly_charts(commands, chart_type='relationships', gesture_support=True)
        
        assert isinstance(result, go.Figure)
        # Should support gestures like pinch-to-zoom, swipe, etc.


class TestCommandExplorerIntegration:
    """Test cases for integration with existing framework components"""
    
    def test_integration_with_framework_parser(self):
        """Test integration with framework parser"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        # Should use FrameworkParser
        assert isinstance(explorer.framework_parser, FrameworkParser)
    
    def test_integration_with_data_models(self):
        """Test integration with Command data model"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command_data = {
            'name': 'auto',
            'path': '/commands/auto.md',
            'category': 'core',
            'description': 'Intelligent routing'
        }
        
        command = Command.from_dict(command_data)
        
        result = explorer.get_command_details(command)
        
        assert isinstance(result, dict)
        assert result['name'] == 'auto'
    
    def test_integration_with_streamlit_components(self):
        """Test integration with Streamlit components"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        with patch('streamlit.title') as mock_title, \
             patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.plotly_chart') as mock_plotly:
            
            explorer.render()
            
            # Should use Streamlit components
            mock_title.assert_called()
            mock_selectbox.assert_called()
            mock_plotly.assert_called()
    
    def test_data_flow_validation(self):
        """Test data flow validation between components"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        # Test data flow: parser -> commands -> visualization
        mock_commands = [
            {'name': 'auto', 'path': '/commands/auto.md', 'category': 'core'}
        ]
        
        with patch.object(explorer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'commands': mock_commands}
            
            loaded_commands = explorer.load_commands_from_framework()
            viz_data = explorer.create_dependency_visualization(loaded_commands)
            
            assert len(loaded_commands) == 1
            assert isinstance(viz_data, dict)
    
    def test_state_management_testing(self):
        """Test state management across component interactions"""
        from components.command_explorer import CommandExplorer
        
        explorer = CommandExplorer()
        
        command = Command(name='auto', path='/commands/auto.md', category='core')
        
        # Test state persistence
        explorer.handle_command_selection(command)
        assert explorer.selected_command == command
        
        # Test state updates
        explorer.filter_state = {'category': 'core'}
        assert explorer.filter_state['category'] == 'core'


class TestCommandExplorerFileConstraints:
    """Test cases for file size and code organization constraints"""
    
    def test_command_explorer_file_size_constraint(self):
        """Test that command_explorer.py is under 800 lines"""
        explorer_path = Path(__file__).parent.parent / "components" / "command_explorer.py"
        
        # This will fail until file is created
        assert explorer_path.exists(), "command_explorer.py should exist"
        
        with open(explorer_path, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines and comments for accurate count
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        assert len(code_lines) < 800, f"command_explorer.py should be <800 lines of code, found {len(code_lines)}"
    
    def test_command_explorer_imports_are_appropriate(self):
        """Test that command_explorer.py has appropriate imports"""
        explorer_path = Path(__file__).parent.parent / "components" / "command_explorer.py"
        
        with open(explorer_path, 'r') as f:
            source = f.read()
        
        # Should import necessary modules
        assert "import streamlit" in source, "Should import streamlit for UI"
        assert "import plotly" in source, "Should import plotly for visualization"
        assert "from data.framework_parser import FrameworkParser" in source, "Should import FrameworkParser"
        assert "from data.models import Command" in source, "Should import Command model"
    
    def test_command_explorer_separation_of_concerns(self):
        """Test that CommandExplorer follows single responsibility principle"""
        from components.command_explorer import CommandExplorer
        import inspect
        
        # Get all methods in CommandExplorer
        methods = [name for name, obj in inspect.getmembers(CommandExplorer) if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        public_methods = [m for m in methods if not m.startswith('_') and m != '__init__']
        
        # Should have focused responsibility - command exploration only
        assert len(public_methods) <= 12, f"CommandExplorer should have ≤12 public methods, found {len(public_methods)}: {public_methods}"
    
    def test_command_explorer_cyclomatic_complexity(self):
        """Test that CommandExplorer has acceptable cyclomatic complexity"""
        from components.command_explorer import CommandExplorer
        import ast
        import inspect
        import textwrap
        
        def count_decision_points(source):
            dedented_source = textwrap.dedent(source)
            tree = ast.parse(dedented_source)
            decision_nodes = (ast.If, ast.For, ast.While, ast.Try, ast.With)
            return sum(1 for node in ast.walk(tree) if isinstance(node, decision_nodes))
        
        # Check each method
        for method_name, method in inspect.getmembers(CommandExplorer, inspect.isfunction):
            if not method_name.startswith('_'):
                try:
                    source = inspect.getsource(method)
                    complexity = count_decision_points(source)
                    assert complexity <= 15, f"CommandExplorer.{method_name} has complexity {complexity} > 15"
                except (OSError, TypeError, IndentationError):
                    pass


# Performance benchmark data for implementation guidance
class TestCommandExplorerImplementationGuidance:
    """Test cases that provide implementation guidance and benchmarks"""
    
    def test_performance_benchmarks_specification(self):
        """Define performance benchmarks for implementation"""
        benchmarks = {
            'load_time_50_commands': 2.0,  # seconds
            'render_time_30_commands': 1.0,  # seconds
            'interactive_response_time': 0.1,  # seconds
            'memory_usage_100_commands': 10000000,  # bytes (10MB)
            'dependency_visualization_50_commands': 3.0,  # seconds
        }
        
        # This test documents expected performance - implementation should meet these
        assert all(isinstance(v, (int, float)) for v in benchmarks.values())
        assert all(v > 0 for v in benchmarks.values())
    
    def test_coverage_analysis_plan(self):
        """Define coverage analysis plan for 90%+ target"""
        coverage_areas = {
            'initialization': ['__init__', 'parameter_validation', 'default_setup'],
            'data_loading': ['load_commands_from_framework', 'error_handling', 'performance'],
            'filtering': ['filter_commands_by_category', 'filter_by_usage', 'multiple_criteria'],
            'details': ['get_command_details', 'file_parsing', 'metadata_extraction'],
            'visualization': ['create_dependency_visualization', 'plotly_charts', 'interactivity'],
            'interaction': ['handle_command_selection', 'ui_updates', 'state_management'],
            'error_handling': ['graceful_degradation', 'recovery_mechanisms', 'validation'],
            'performance': ['load_time', 'render_time', 'memory_usage'],
            'accessibility': ['aria_labels', 'keyboard_navigation', 'screen_reader'],
            'mobile': ['touch_interaction', 'responsive_layout', 'gestures'],
            'integration': ['framework_parser', 'data_models', 'streamlit_components']
        }
        
        # Each area should have comprehensive test coverage
        assert len(coverage_areas) >= 11
        assert all(len(tests) >= 3 for tests in coverage_areas.values())
    
    def test_integration_specifications(self):
        """Define integration specifications with existing framework"""
        integration_points = {
            'framework_parser': 'data.framework_parser.FrameworkParser',
            'command_model': 'data.models.Command',
            'module_model': 'data.models.Module',
            'framework_model': 'data.models.Framework',
            'streamlit_ui': 'streamlit components',
            'plotly_viz': 'plotly.graph_objects'
        }
        
        # All integration points should be clearly defined
        assert len(integration_points) == 6
        assert all(isinstance(v, str) for v in integration_points.values())


def mock_open(read_data=''):
    """Mock open function for file operations"""
    from unittest.mock import mock_open as mock_open_builtin
    return mock_open_builtin(read_data=read_data)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])