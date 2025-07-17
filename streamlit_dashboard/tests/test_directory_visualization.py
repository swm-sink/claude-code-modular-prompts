"""
TDD RED: Tests for directory visualization component
These tests define the expected behavior of the interactive directory tree visualization
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import pandas as pd

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDirectoryVisualizationModule:
    """Test cases for directory visualization module structure and interface"""
    
    def test_directory_visualization_module_exists(self):
        """Test that directory visualization module exists"""
        from components.directory_visualization import DirectoryVisualization
        assert DirectoryVisualization is not None
    
    def test_directory_visualization_has_render_method(self):
        """Test that DirectoryVisualization has render method"""
        from components.directory_visualization import DirectoryVisualization
        viz = DirectoryVisualization()
        assert hasattr(viz, 'render'), "DirectoryVisualization should have render() method"
        assert callable(viz.render), "render should be callable"
    
    def test_directory_visualization_has_display_tree_method(self):
        """Test that DirectoryVisualization has display_tree method"""
        from components.directory_visualization import DirectoryVisualization
        viz = DirectoryVisualization()
        assert hasattr(viz, 'display_tree'), "DirectoryVisualization should have display_tree() method"
        assert callable(viz.display_tree), "display_tree should be callable"
    
    def test_directory_visualization_has_create_tree_data_method(self):
        """Test that DirectoryVisualization has create_tree_data method"""
        from components.directory_visualization import DirectoryVisualization
        viz = DirectoryVisualization()
        assert hasattr(viz, 'create_tree_data'), "DirectoryVisualization should have create_tree_data() method"
        assert callable(viz.create_tree_data), "create_tree_data should be callable"
    
    def test_directory_visualization_has_filter_tree_method(self):
        """Test that DirectoryVisualization has filter_tree method"""
        from components.directory_visualization import DirectoryVisualization
        viz = DirectoryVisualization()
        assert hasattr(viz, 'filter_tree'), "DirectoryVisualization should have filter_tree() method"
        assert callable(viz.filter_tree), "filter_tree should be callable"
    
    def test_directory_visualization_file_size_constraint(self):
        """Test that directory_visualization.py is under 500 lines"""
        viz_path = Path(__file__).parent.parent / "components" / "directory_visualization.py"
        assert viz_path.exists(), "directory_visualization.py should exist"
        
        with open(viz_path, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines and comments for more accurate count
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        assert len(code_lines) < 500, f"directory_visualization.py should be <500 lines of code, found {len(code_lines)}"


class TestDirectoryVisualizationRendering:
    """Test cases for directory visualization rendering functionality"""
    
    def test_render_displays_header(self):
        """Test that render method displays directory visualization header"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        with patch('streamlit.title') as mock_title:
            viz.render()
            
            # Should display a title
            mock_title.assert_called()
            args, kwargs = mock_title.call_args
            assert "Directory" in args[0] and "Visualization" in args[0]
    
    def test_render_displays_description(self):
        """Test that render method displays description"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        with patch('streamlit.markdown') as mock_markdown:
            viz.render()
            
            # Should display description
            mock_markdown.assert_called()
    
    def test_render_calls_display_tree(self):
        """Test that render method calls display_tree"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        with patch.object(viz, 'display_tree') as mock_display_tree:
            viz.render()
            
            # Should call display_tree
            mock_display_tree.assert_called_once()
    
    def test_render_includes_search_controls(self):
        """Test that render method includes search controls"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        with patch('streamlit.text_input') as mock_text_input:
            viz.render()
            
            # Should include search input
            mock_text_input.assert_called()
    
    def test_render_includes_filter_controls(self):
        """Test that render method includes filter controls"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        with patch('streamlit.selectbox') as mock_selectbox:
            viz.render()
            
            # Should include filter selectbox
            mock_selectbox.assert_called()


class TestDirectoryVisualizationTreeData:
    """Test cases for directory tree data creation"""
    
    def test_create_tree_data_returns_hierarchical_structure(self):
        """Test that create_tree_data returns proper hierarchical structure"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock framework parser data
        mock_framework_data = {
            'structure': {
                'commands': {
                    'count': 2,
                    'files': [
                        {'name': 'auto', 'path': '/commands/auto.md', 'category': 'command'},
                        {'name': 'task', 'path': '/commands/task.md', 'category': 'command'}
                    ]
                },
                'modules': {
                    'count': 3,
                    'categories': {
                        'patterns': [
                            {'name': 'tdd-cycle-pattern', 'path': '/modules/patterns/tdd-cycle-pattern.md', 'category': 'patterns'},
                            {'name': 'intelligent-routing', 'path': '/modules/patterns/intelligent-routing.md', 'category': 'patterns'}
                        ],
                        'security': [
                            {'name': 'security-validator', 'path': '/modules/security/security-validator.md', 'category': 'security'}
                        ]
                    }
                }
            }
        }
        
        tree_data = viz.create_tree_data(mock_framework_data)
        
        # Should return hierarchical structure
        assert isinstance(tree_data, dict), "Tree data should be a dictionary"
        assert 'name' in tree_data, "Tree data should have name"
        assert 'children' in tree_data, "Tree data should have children"
        assert 'type' in tree_data, "Tree data should have type"
    
    def test_create_tree_data_includes_file_metadata(self):
        """Test that create_tree_data includes file metadata"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock framework parser data with file metadata
        mock_framework_data = {
            'structure': {
                'commands': {
                    'count': 1,
                    'files': [
                        {'name': 'auto', 'path': '/commands/auto.md', 'category': 'command', 'size': 1024}
                    ]
                },
                'modules': {
                    'count': 0,
                    'categories': {}
                }
            }
        }
        
        tree_data = viz.create_tree_data(mock_framework_data)
        
        # Should include metadata for files
        commands_node = next((child for child in tree_data['children'] if child['name'] == 'commands'), None)
        assert commands_node is not None, "Should have commands node"
        assert len(commands_node['children']) > 0, "Commands node should have children"
        
        file_node = commands_node['children'][0]
        assert 'metadata' in file_node, "File nodes should have metadata"
        assert 'category' in file_node['metadata'], "File metadata should include category"
    
    def test_create_tree_data_handles_empty_framework(self):
        """Test that create_tree_data handles empty framework gracefully"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock empty framework data
        mock_framework_data = {
            'structure': {
                'commands': {
                    'count': 0,
                    'files': []
                },
                'modules': {
                    'count': 0,
                    'categories': {}
                }
            }
        }
        
        tree_data = viz.create_tree_data(mock_framework_data)
        
        # Should still return valid structure
        assert isinstance(tree_data, dict), "Tree data should be a dictionary"
        assert tree_data['name'] == '.claude', "Root should be .claude"
        assert len(tree_data['children']) >= 0, "Should have children list"
    
    def test_create_tree_data_color_codes_by_type(self):
        """Test that create_tree_data color codes nodes by type"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock framework data with different types
        mock_framework_data = {
            'structure': {
                'commands': {
                    'count': 1,
                    'files': [
                        {'name': 'auto', 'path': '/commands/auto.md', 'category': 'command'}
                    ]
                },
                'modules': {
                    'count': 1,
                    'categories': {
                        'patterns': [
                            {'name': 'tdd-pattern', 'path': '/modules/patterns/tdd-pattern.md', 'category': 'patterns'}
                        ]
                    }
                }
            }
        }
        
        tree_data = viz.create_tree_data(mock_framework_data)
        
        # Should have color coding for different types
        commands_node = next((child for child in tree_data['children'] if child['name'] == 'commands'), None)
        modules_node = next((child for child in tree_data['children'] if child['name'] == 'modules'), None)
        
        assert commands_node is not None, "Should have commands node"
        assert modules_node is not None, "Should have modules node"
        assert 'color' in commands_node, "Commands node should have color"
        assert 'color' in modules_node, "Modules node should have color"


class TestDirectoryVisualizationTreeDisplay:
    """Test cases for directory tree display functionality"""
    
    def test_display_tree_renders_interactive_tree(self):
        """Test that display_tree renders an interactive tree component"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'commands',
                    'type': 'directory',
                    'children': [
                        {'name': 'auto.md', 'type': 'file', 'metadata': {'category': 'command'}}
                    ]
                }
            ]
        }
        
        with patch('streamlit.components.v1.html') as mock_html:
            viz.display_tree(mock_tree_data)
            
            # Should render HTML component for interactive tree
            mock_html.assert_called()
    
    def test_display_tree_includes_expansion_controls(self):
        """Test that display_tree includes expansion controls"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'commands',
                    'type': 'directory',
                    'children': [
                        {'name': 'auto.md', 'type': 'file', 'metadata': {'category': 'command'}}
                    ]
                }
            ]
        }
        
        with patch('streamlit.columns') as mock_columns:
            # Mock columns for controls
            mock_col1, mock_col2 = MagicMock(), MagicMock()
            mock_col1.__enter__ = MagicMock(return_value=mock_col1)
            mock_col1.__exit__ = MagicMock(return_value=None)
            mock_col2.__enter__ = MagicMock(return_value=mock_col2)
            mock_col2.__exit__ = MagicMock(return_value=None)
            mock_columns.return_value = [mock_col1, mock_col2]
            
            viz.display_tree(mock_tree_data)
            
            # Should include expansion controls
            mock_columns.assert_called()
    
    def test_display_tree_shows_file_metadata(self):
        """Test that display_tree shows file metadata when available"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data with file metadata
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'auto.md',
                    'type': 'file',
                    'metadata': {
                        'category': 'command',
                        'size': 1024,
                        'modified': '2025-01-15T10:30:00Z'
                    }
                }
            ]
        }
        
        with patch('streamlit.expander') as mock_expander:
            # Mock expander for file details
            mock_expander_instance = MagicMock()
            mock_expander_instance.__enter__ = MagicMock(return_value=mock_expander_instance)
            mock_expander_instance.__exit__ = MagicMock(return_value=None)
            mock_expander.return_value = mock_expander_instance
            
            viz.display_tree(mock_tree_data)
            
            # Should show file metadata
            mock_expander.assert_called()
    
    def test_display_tree_supports_zoom_and_pan(self):
        """Test that display_tree supports zoom and pan functionality"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': []
        }
        
        with patch('streamlit.components.v1.html') as mock_html:
            viz.display_tree(mock_tree_data)
            
            # Should render HTML with zoom/pan capabilities
            mock_html.assert_called()
            
            # Check that the HTML includes zoom/pan functionality
            call_args = mock_html.call_args
            html_content = call_args[1]['html'] if 'html' in call_args[1] else call_args[0][0]
            
            # Should include zoom/pan controls
            assert 'zoom' in html_content.lower() or 'pan' in html_content.lower()


class TestDirectoryVisualizationFiltering:
    """Test cases for directory tree filtering functionality"""
    
    def test_filter_tree_by_search_term(self):
        """Test that filter_tree filters nodes by search term"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'commands',
                    'type': 'directory',
                    'children': [
                        {'name': 'auto.md', 'type': 'file', 'metadata': {'category': 'command'}},
                        {'name': 'task.md', 'type': 'file', 'metadata': {'category': 'command'}}
                    ]
                },
                {
                    'name': 'modules',
                    'type': 'directory',
                    'children': [
                        {'name': 'patterns', 'type': 'directory', 'children': [
                            {'name': 'tdd-pattern.md', 'type': 'file', 'metadata': {'category': 'patterns'}}
                        ]}
                    ]
                }
            ]
        }
        
        filtered_tree = viz.filter_tree(mock_tree_data, search_term='auto')
        
        # Should filter to only nodes containing 'auto'
        assert filtered_tree is not None, "Should return filtered tree"
        assert 'children' in filtered_tree, "Filtered tree should have children"
        
        # Should preserve structure but filter contents
        commands_node = next((child for child in filtered_tree['children'] 
                             if child['name'] == 'commands'), None)
        assert commands_node is not None, "Should preserve commands directory"
        
        # Should only include files matching search term
        auto_file = next((child for child in commands_node['children'] 
                         if 'auto' in child['name']), None)
        assert auto_file is not None, "Should include auto.md file"
    
    def test_filter_tree_by_file_type(self):
        """Test that filter_tree filters nodes by file type"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data with different file types
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'commands',
                    'type': 'directory',
                    'children': [
                        {'name': 'auto.md', 'type': 'file', 'metadata': {'category': 'command'}},
                        {'name': 'task.md', 'type': 'file', 'metadata': {'category': 'command'}}
                    ]
                },
                {
                    'name': 'modules',
                    'type': 'directory',
                    'children': [
                        {'name': 'patterns', 'type': 'directory', 'children': [
                            {'name': 'tdd-pattern.md', 'type': 'file', 'metadata': {'category': 'patterns'}}
                        ]}
                    ]
                }
            ]
        }
        
        filtered_tree = viz.filter_tree(mock_tree_data, file_type='command')
        
        # Should filter to only command files
        assert filtered_tree is not None, "Should return filtered tree"
        
        # Should preserve structure but filter by category
        commands_node = next((child for child in filtered_tree['children'] 
                             if child['name'] == 'commands'), None)
        assert commands_node is not None, "Should preserve commands directory"
        
        # Should only include command files
        for child in commands_node['children']:
            if child['type'] == 'file':
                assert child['metadata']['category'] == 'command', "Should only include command files"
    
    def test_filter_tree_preserves_directory_structure(self):
        """Test that filter_tree preserves directory structure"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'commands',
                    'type': 'directory',
                    'children': [
                        {'name': 'auto.md', 'type': 'file', 'metadata': {'category': 'command'}}
                    ]
                },
                {
                    'name': 'modules',
                    'type': 'directory',
                    'children': [
                        {'name': 'patterns', 'type': 'directory', 'children': [
                            {'name': 'other-pattern.md', 'type': 'file', 'metadata': {'category': 'patterns'}}
                        ]}
                    ]
                }
            ]
        }
        
        filtered_tree = viz.filter_tree(mock_tree_data, search_term='auto')
        
        # Should preserve directory structure
        assert filtered_tree['name'] == '.claude', "Should preserve root name"
        assert filtered_tree['type'] == 'directory', "Should preserve root type"
        
        # Should include parent directories of matching files
        commands_node = next((child for child in filtered_tree['children'] 
                             if child['name'] == 'commands'), None)
        assert commands_node is not None, "Should preserve parent directories"
        assert commands_node['type'] == 'directory', "Parent should remain directory"
    
    def test_filter_tree_handles_empty_results(self):
        """Test that filter_tree handles empty filter results"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'commands',
                    'type': 'directory',
                    'children': [
                        {'name': 'auto.md', 'type': 'file', 'metadata': {'category': 'command'}}
                    ]
                }
            ]
        }
        
        filtered_tree = viz.filter_tree(mock_tree_data, search_term='nonexistent')
        
        # Should return empty structure when no matches
        assert filtered_tree is not None, "Should return tree structure"
        assert filtered_tree['name'] == '.claude', "Should preserve root"
        assert len(filtered_tree['children']) == 0, "Should have empty children for no matches"


class TestDirectoryVisualizationIntegration:
    """Test cases for directory visualization integration"""
    
    def test_directory_visualization_works_with_framework_parser(self):
        """Test that directory visualization integrates with framework parser"""
        from components.directory_visualization import DirectoryVisualization
        from data.framework_parser import FrameworkParser
        
        viz = DirectoryVisualization()
        
        # Mock framework parser
        with patch.object(FrameworkParser, 'parse') as mock_parse:
            mock_parse.return_value = {
                'structure': {
                    'commands': {
                        'count': 1,
                        'files': [
                            {'name': 'auto', 'path': '/commands/auto.md', 'category': 'command'}
                        ]
                    },
                    'modules': {
                        'count': 1,
                        'categories': {
                            'patterns': [
                                {'name': 'tdd-pattern', 'path': '/modules/patterns/tdd-pattern.md', 'category': 'patterns'}
                            ]
                        }
                    }
                }
            }
            
            # Should work with framework parser data
            viz.render()
            
            # Should call framework parser
            mock_parse.assert_called()
    
    def test_directory_visualization_works_with_framework_models(self):
        """Test that directory visualization integrates with framework models"""
        from components.directory_visualization import DirectoryVisualization
        from data.models import Framework, Command, Module
        
        viz = DirectoryVisualization()
        
        # Create framework with models
        framework = Framework(
            path="/test/.claude",
            commands=[
                Command(name="auto", path="/commands/auto.md", category="command"),
                Command(name="task", path="/commands/task.md", category="command")
            ],
            modules=[
                Module(name="tdd-pattern", path="/modules/patterns/tdd-pattern.md", category="patterns"),
                Module(name="security-validator", path="/modules/security/security-validator.md", category="security")
            ]
        )
        
        # Should work with framework models
        tree_data = viz.create_tree_data({
            'structure': {
                'commands': {
                    'count': len(framework.commands),
                    'files': [cmd.to_dict() for cmd in framework.commands]
                },
                'modules': {
                    'count': len(framework.modules),
                    'categories': {
                        'patterns': [mod.to_dict() for mod in framework.modules if mod.category == 'patterns'],
                        'security': [mod.to_dict() for mod in framework.modules if mod.category == 'security']
                    }
                }
            }
        })
        
        # Should create valid tree structure
        assert tree_data is not None, "Should create tree data from framework models"
        assert 'children' in tree_data, "Should have children structure"
    
    def test_directory_visualization_follows_separation_of_concerns(self):
        """Test that directory visualization follows single responsibility principle"""
        from components.directory_visualization import DirectoryVisualization
        import inspect
        
        # Get all methods in DirectoryVisualization
        methods = [name for name, obj in inspect.getmembers(DirectoryVisualization) 
                  if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        # Should have focused responsibility - directory visualization only
        expected_methods = ['render', 'display_tree', 'create_tree_data', 'filter_tree']
        
        public_methods = [m for m in methods if not m.startswith('_') and m != '__init__']
        
        # Check that we don't have excessive methods (separation of concerns)
        assert len(public_methods) <= 8, f"DirectoryVisualization should have ≤8 public methods, found {len(public_methods)}: {public_methods}"
        
        # Check that essential methods exist
        for method in expected_methods:
            assert method in public_methods, f"Missing required method: {method}"
    
    def test_directory_visualization_imports_are_minimal(self):
        """Test that directory_visualization.py has minimal imports"""
        viz_path = Path(__file__).parent.parent / "components" / "directory_visualization.py"
        with open(viz_path, 'r') as f:
            source = f.read()
        
        # Should import only necessary modules
        assert "import streamlit" in source, "Should import streamlit for UI"
        assert "import json" in source, "Should import json for data handling"
        
        # Should NOT import complex unrelated modules
        forbidden_imports = [
            "import plotly.graph_objects",
            "from utils.complex_operations import",
            "from advanced_visualization import",
            "from machine_learning import"
        ]
        
        for forbidden in forbidden_imports:
            assert forbidden not in source, f"DirectoryVisualization should not import unrelated modules: {forbidden}"


class TestDirectoryVisualizationEdgeCases:
    """Test cases for edge cases and error conditions"""
    
    def test_directory_visualization_handles_malformed_data(self):
        """Test that directory visualization handles malformed data gracefully"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock malformed framework data
        mock_malformed_data = {
            'structure': {
                'commands': None,  # Malformed - should be dict
                'modules': {
                    'count': 'not_a_number',  # Malformed - should be int
                    'categories': 'not_a_dict'  # Malformed - should be dict
                }
            }
        }
        
        # Should handle malformed data gracefully
        tree_data = viz.create_tree_data(mock_malformed_data)
        
        # Should return valid structure even with malformed input
        assert tree_data is not None, "Should return tree data even with malformed input"
        assert 'name' in tree_data, "Should have name field"
        assert 'children' in tree_data, "Should have children field"
    
    def test_directory_visualization_handles_render_exception(self):
        """Test that directory visualization handles render exceptions gracefully"""
        from components.directory_visualization import DirectoryVisualization
        from unittest.mock import patch
        
        viz = DirectoryVisualization()
        
        # Mock framework parser to raise exception
        with patch.object(viz.parser, 'parse') as mock_parse, \
             patch('streamlit.error') as mock_error, \
             patch('streamlit.info') as mock_info:
            
            mock_parse.side_effect = Exception("Parser error")
            
            # Should handle exception gracefully
            viz.render()
            
            # Should show error message
            mock_error.assert_called_once()
            mock_info.assert_called_once()
    
    def test_directory_visualization_handles_non_dict_structure(self):
        """Test that directory visualization handles non-dict structure"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock data with non-dict structure
        mock_data = {
            'structure': 'not_a_dict'  # Should be dict
        }
        
        # Should handle gracefully
        tree_data = viz.create_tree_data(mock_data)
        
        # Should return empty tree
        assert tree_data is not None, "Should return tree data"
        assert tree_data['name'] == '.claude', "Should have default name"
        assert len(tree_data['children']) == 0, "Should have empty children"
    
    def test_directory_visualization_handles_type_error(self):
        """Test that directory visualization handles TypeError in create_tree_data"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock data that causes TypeError
        mock_data = object()  # Not a dict
        
        # Should handle gracefully
        tree_data = viz.create_tree_data(mock_data)
        
        # Should return empty tree
        assert tree_data is not None, "Should return tree data"
        assert tree_data['name'] == '.claude', "Should have default name"
        assert len(tree_data['children']) == 0, "Should have empty children"
    
    def test_directory_visualization_handles_empty_tree_display(self):
        """Test that directory visualization handles empty tree display"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock empty tree data
        with patch('streamlit.info') as mock_info:
            viz.display_tree(None)
            
            # Should display info message
            mock_info.assert_called_once()
    
    def test_directory_visualization_handles_empty_filter_tree(self):
        """Test that directory visualization handles empty tree in filter"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Should handle None tree data
        filtered_tree = viz.filter_tree(None)
        
        # Should return empty tree
        assert filtered_tree is not None, "Should return tree data"
        assert filtered_tree['name'] == '.claude', "Should have default name"
        assert len(filtered_tree['children']) == 0, "Should have empty children"
    
    def test_directory_visualization_handles_none_node_filter(self):
        """Test that directory visualization handles None node in filter"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Should handle None node
        result = viz._filter_node(None, 'search', 'All')
        
        # Should return None
        assert result is None, "Should return None for None node"
    
    def test_directory_visualization_handles_selected_file_in_session(self):
        """Test that directory visualization handles selected file in session state"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock session state with selected file
        with patch('streamlit.session_state', {'selected_file': {'name': 'test.md', 'path': '/test.md', 'category': 'test', 'type': 'file'}}) as mock_session, \
             patch('streamlit.sidebar') as mock_sidebar, \
             patch('streamlit.header') as mock_header, \
             patch('streamlit.write') as mock_write, \
             patch('streamlit.button') as mock_button, \
             patch('streamlit.info') as mock_info, \
             patch('streamlit.expander') as mock_expander:
            
            # Mock sidebar context manager
            mock_sidebar_instance = MagicMock()
            mock_sidebar_instance.__enter__ = MagicMock(return_value=mock_sidebar_instance)
            mock_sidebar_instance.__exit__ = MagicMock(return_value=None)
            mock_sidebar.return_value = mock_sidebar_instance
            
            # Mock expander context manager
            mock_expander_instance = MagicMock()
            mock_expander_instance.__enter__ = MagicMock(return_value=mock_expander_instance)
            mock_expander_instance.__exit__ = MagicMock(return_value=None)
            mock_expander.return_value = mock_expander_instance
            
            mock_button.return_value = False
            
            # Should handle selected file
            viz._render_file_details()
            
            # Should write file details
            assert mock_write.call_count >= 4, "Should write file details"
    
    def test_directory_visualization_handles_none_input(self):
        """Test that directory visualization handles None input"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Should handle None input gracefully
        tree_data = viz.create_tree_data(None)
        
        # Should return empty but valid structure
        assert tree_data is not None, "Should return tree data even with None input"
        assert tree_data['name'] == '.claude', "Should have default root name"
        assert len(tree_data['children']) == 0, "Should have empty children"
    
    def test_directory_visualization_cyclomatic_complexity(self):
        """Test that directory visualization has acceptable cyclomatic complexity"""
        from components.directory_visualization import DirectoryVisualization
        import ast
        import inspect
        import textwrap
        
        # Simple complexity check - count decision points (if, for, while, etc.)
        def count_decision_points(source):
            dedented_source = textwrap.dedent(source)
            tree = ast.parse(dedented_source)
            decision_nodes = (ast.If, ast.For, ast.While, ast.Try, ast.With)
            return sum(1 for node in ast.walk(tree) if isinstance(node, decision_nodes))
        
        # Check each method
        for method_name, method in inspect.getmembers(DirectoryVisualization, inspect.isfunction):
            if not method_name.startswith('_'):  # Only check public methods
                try:
                    source = inspect.getsource(method)
                    complexity = count_decision_points(source)
                    assert complexity <= 10, f"DirectoryVisualization.{method_name} has complexity {complexity} > 10"
                except (OSError, TypeError, IndentationError):
                    # Skip methods we can't get source for or parse
                    pass
    
    def test_directory_visualization_performance_with_large_tree(self):
        """Test that directory visualization handles large trees efficiently"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Create large mock tree data
        large_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': []
        }
        
        # Add many files to test performance
        for i in range(100):
            large_tree_data['children'].append({
                'name': f'file_{i}.md',
                'type': 'file',
                'metadata': {'category': f'category_{i % 10}'}
            })
        
        # Should handle large trees without issues
        filtered_tree = viz.filter_tree(large_tree_data, search_term='file_5')
        
        # Should still work correctly
        assert filtered_tree is not None, "Should handle large trees"
        assert len(filtered_tree['children']) > 0, "Should find matches in large tree"


class TestDirectoryVisualizationInteractivity:
    """Test cases for interactive features"""
    
    def test_directory_visualization_supports_node_selection(self):
        """Test that directory visualization supports node selection"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'commands',
                    'type': 'directory',
                    'children': [
                        {'name': 'auto.md', 'type': 'file', 'metadata': {'category': 'command'}}
                    ]
                }
            ]
        }
        
        with patch('streamlit.components.v1.html') as mock_html:
            viz.display_tree(mock_tree_data)
            
            # Should include selection functionality
            mock_html.assert_called()
            
            # Check that HTML includes click handlers
            call_args = mock_html.call_args
            html_content = call_args[1]['html'] if 'html' in call_args[1] else call_args[0][0]
            
            # Should include click event handling
            assert 'onclick' in html_content.lower() or 'click' in html_content.lower()
    
    def test_directory_visualization_shows_file_details_on_click(self):
        """Test that directory visualization shows file details on click"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data with file metadata
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'auto.md',
                    'type': 'file',
                    'metadata': {
                        'category': 'command',
                        'path': '/commands/auto.md',
                        'size': 1024,
                        'modified': '2025-01-15T10:30:00Z'
                    }
                }
            ]
        }
        
        with patch('streamlit.sidebar') as mock_sidebar:
            viz.display_tree(mock_tree_data)
            
            # Should provide file details display
            mock_sidebar.assert_called()
    
    def test_directory_visualization_supports_navigation(self):
        """Test that directory visualization supports navigation to files"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock tree data
        mock_tree_data = {
            'name': '.claude',
            'type': 'directory',
            'children': [
                {
                    'name': 'auto.md',
                    'type': 'file',
                    'metadata': {
                        'category': 'command',
                        'path': '/commands/auto.md'
                    }
                }
            ]
        }
        
        with patch('streamlit.button') as mock_button:
            viz.display_tree(mock_tree_data)
            
            # Should include navigation buttons
            mock_button.assert_called()
    
    def test_directory_visualization_handles_button_click(self):
        """Test that directory visualization handles button clicks"""
        from components.directory_visualization import DirectoryVisualization
        
        viz = DirectoryVisualization()
        
        # Mock session state with selected file
        with patch('streamlit.session_state', {'selected_file': {'name': 'test.md', 'path': '/test.md', 'category': 'test', 'type': 'file'}}) as mock_session, \
             patch('streamlit.sidebar') as mock_sidebar, \
             patch('streamlit.header') as mock_header, \
             patch('streamlit.write') as mock_write, \
             patch('streamlit.button') as mock_button, \
             patch('streamlit.info') as mock_info, \
             patch('streamlit.expander') as mock_expander:
            
            # Mock sidebar context manager
            mock_sidebar_instance = MagicMock()
            mock_sidebar_instance.__enter__ = MagicMock(return_value=mock_sidebar_instance)
            mock_sidebar_instance.__exit__ = MagicMock(return_value=None)
            mock_sidebar.return_value = mock_sidebar_instance
            
            # Mock expander context manager
            mock_expander_instance = MagicMock()
            mock_expander_instance.__enter__ = MagicMock(return_value=mock_expander_instance)
            mock_expander_instance.__exit__ = MagicMock(return_value=None)
            mock_expander.return_value = mock_expander_instance
            
            # Mock button to return True (clicked)
            mock_button.return_value = True
            
            # Should handle button click
            viz._render_file_details()
            
            # Should call info when button is clicked
            mock_info.assert_called()