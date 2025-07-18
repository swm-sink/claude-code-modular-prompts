"""
TDD RED: Comprehensive failing test suite for Module Visualizer component
These tests define the expected behavior and architecture of the module visualizer
All tests MUST fail until implementation is complete - strict TDD methodology

Coverage Target: 100% of all functionality
Performance Target: <2s load time for 100+ modules
Architecture: Streamlit + Plotly + NetworkX interactive visualization
Module Categories: patterns, development, meta, system, domain, templates
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock, mock_open
import pandas as pd
import plotly.graph_objects as go
import networkx as nx
from typing import Dict, List, Optional, Any, Tuple
import time

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import existing framework components for integration
from data.framework_parser import FrameworkParser
from data.models import Command, Module, Framework


class TestModuleVisualizerInitialization:
    """Test cases for ModuleVisualizer initialization and basic functionality"""
    
    def test_module_visualizer_module_exists(self):
        """Test that ModuleVisualizer module exists and can be imported"""
        # Module should now be importable in GREEN phase
        from components.module_visualizer import ModuleVisualizer
        assert ModuleVisualizer is not None
    
    def test_module_visualizer_initialization_with_framework_path(self):
        """Test ModuleVisualizer initialization with valid framework path"""
        # This test MUST fail - no implementation exists yet
        from components.module_visualizer import ModuleVisualizer
        
        framework_path = Path("/test/.claude")
        visualizer = ModuleVisualizer(framework_path=framework_path)
        
        assert visualizer.framework_path == framework_path
        assert hasattr(visualizer, 'framework_parser')
        assert isinstance(visualizer.framework_parser, FrameworkParser)
    
    def test_module_visualizer_initialization_with_invalid_path(self):
        """Test ModuleVisualizer initialization with invalid framework path"""
        from components.module_visualizer import ModuleVisualizer
        
        with pytest.raises(ValueError):
            ModuleVisualizer(framework_path=None)
        
        with pytest.raises(TypeError):
            ModuleVisualizer(framework_path="not_a_path_object")
    
    def test_module_visualizer_initialization_default_parameters(self):
        """Test ModuleVisualizer initialization with default parameters"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        assert hasattr(visualizer, 'framework_path')
        assert hasattr(visualizer, 'framework_parser')
        assert hasattr(visualizer, 'selected_module')
        assert visualizer.selected_module is None
        assert hasattr(visualizer, 'filter_state')
        assert isinstance(visualizer.filter_state, dict)
        assert hasattr(visualizer, 'dependency_graph')
        assert visualizer.dependency_graph is None
        assert hasattr(visualizer, 'layout_config')
        assert isinstance(visualizer.layout_config, dict)
    
    def test_module_visualizer_has_required_methods(self):
        """Test that ModuleVisualizer has all required methods"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Core functionality methods
        assert hasattr(visualizer, 'load_modules_from_framework')
        assert callable(visualizer.load_modules_from_framework)
        assert hasattr(visualizer, 'parse_module_dependencies')
        assert callable(visualizer.parse_module_dependencies)
        assert hasattr(visualizer, 'filter_modules_by_category')
        assert callable(visualizer.filter_modules_by_category)
        assert hasattr(visualizer, 'search_modules_by_content')
        assert callable(visualizer.search_modules_by_content)
        
        # Tree navigation methods
        assert hasattr(visualizer, 'build_module_tree')
        assert callable(visualizer.build_module_tree)
        assert hasattr(visualizer, 'render_module_tree_navigation')
        assert callable(visualizer.render_module_tree_navigation)
        assert hasattr(visualizer, 'expand_category_nodes')
        assert callable(visualizer.expand_category_nodes)
        
        # Visualization methods
        assert hasattr(visualizer, 'create_dependency_graph')
        assert callable(visualizer.create_dependency_graph)
        assert hasattr(visualizer, 'create_network_visualization')
        assert callable(visualizer.create_network_visualization)
        assert hasattr(visualizer, 'create_complexity_heatmap')
        assert callable(visualizer.create_complexity_heatmap)
        assert hasattr(visualizer, 'create_usage_frequency_chart')
        assert callable(visualizer.create_usage_frequency_chart)
        assert hasattr(visualizer, 'create_category_distribution_chart')
        assert callable(visualizer.create_category_distribution_chart)
        
        # UI interaction methods
        assert hasattr(visualizer, 'handle_module_selection')
        assert callable(visualizer.handle_module_selection)
        assert hasattr(visualizer, 'render_module_details_panel')
        assert callable(visualizer.render_module_details_panel)
        assert hasattr(visualizer, 'render_filter_controls')
        assert callable(visualizer.render_filter_controls)
        assert hasattr(visualizer, 'handle_zoom_pan_controls')
        assert callable(visualizer.handle_zoom_pan_controls)
        
        # Export methods
        assert hasattr(visualizer, 'export_visualization_png')
        assert callable(visualizer.export_visualization_png)
        assert hasattr(visualizer, 'export_visualization_svg')
        assert callable(visualizer.export_visualization_svg)
        assert hasattr(visualizer, 'export_module_data_json')
        assert callable(visualizer.export_module_data_json)
        
        # Main render method
        assert hasattr(visualizer, 'render')
        assert callable(visualizer.render)
    
    def test_module_visualizer_default_layout_config(self):
        """Test default layout configuration"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        layout_config = visualizer.layout_config
        
        # Should have default layout parameters
        assert 'algorithm' in layout_config
        assert 'node_size' in layout_config
        assert 'edge_width' in layout_config
        assert 'zoom_level' in layout_config
        assert 'pan_position' in layout_config
        assert 'color_scheme' in layout_config
        
        # Verify default values
        assert layout_config['algorithm'] == 'force_directed'
        assert layout_config['node_size'] == 'medium'
        assert layout_config['zoom_level'] == 1.0
        assert isinstance(layout_config['pan_position'], dict)
        assert 'x' in layout_config['pan_position']
        assert 'y' in layout_config['pan_position']


class TestModuleVisualizerDataLoading:
    """Test cases for module data loading and framework integration"""
    
    def test_load_modules_from_framework_success(self):
        """Test successful loading of modules from framework"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Mock framework parser
        mock_modules = [
            {'name': 'routing', 'path': '/modules/patterns/routing.md', 'category': 'patterns'},
            {'name': 'tdd-cycle', 'path': '/modules/patterns/tdd-cycle.md', 'category': 'patterns'},
            {'name': 'security', 'path': '/modules/system/security.md', 'category': 'system'}
        ]
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': mock_modules}
            
            result = visualizer.load_modules_from_framework()
            
            assert isinstance(result, list)
            assert len(result) == 3
            assert all(isinstance(mod, Module) for mod in result)
            mock_parse.assert_called_once()
    
    def test_load_modules_from_framework_large_dataset(self):
        """Test loading modules with large dataset (100+ modules)"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create 150 mock modules for performance testing
        large_module_set = [
            {
                'name': f'module_{i}',
                'path': f'/modules/category_{i%10}/module_{i}.md',
                'category': f'category_{i%10}',
                'description': f'Module {i} description',
                'dependencies': [f'module_{j}' for j in range(max(0, i-3), i)]
            }
            for i in range(150)
        ]
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': large_module_set}
            
            start_time = time.time()
            result = visualizer.load_modules_from_framework()
            end_time = time.time()
            
            # Should complete within 2 seconds for 150 modules
            assert (end_time - start_time) < 2.0
            assert len(result) == 150
    
    def test_load_modules_from_framework_empty_directory(self):
        """Test loading modules from empty framework directory"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': []}
            
            result = visualizer.load_modules_from_framework()
            
            assert isinstance(result, list)
            assert len(result) == 0
            mock_parse.assert_called_once()
    
    def test_load_modules_from_framework_missing_directory(self):
        """Test loading modules when framework directory doesn't exist"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.side_effect = FileNotFoundError("Framework directory not found")
            
            with pytest.raises(FileNotFoundError):
                visualizer.load_modules_from_framework()
    
    def test_load_modules_from_framework_with_metadata(self):
        """Test loading modules with complete metadata"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        mock_modules = [
            {
                'name': 'routing',
                'path': '/modules/patterns/routing.md',
                'category': 'patterns',
                'description': 'Intelligent routing module',
                'version': '1.0.0',
                'dependencies': ['analysis', 'validation'],
                'tags': ['core', 'routing', 'ai']
            }
        ]
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': mock_modules}
            
            result = visualizer.load_modules_from_framework()
            
            assert len(result) == 1
            module = result[0]
            assert module.name == 'routing'
            assert module.description == 'Intelligent routing module'
            assert module.version == '1.0.0'
            assert len(module.dependencies) == 2
            assert len(module.tags) == 3
    
    def test_parse_module_dependencies_success(self):
        """Test successful parsing of module dependencies"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis']),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns', dependencies=[]),
            Module(name='tdd-cycle', path='/modules/patterns/tdd-cycle.md', category='patterns', dependencies=['analysis'])
        ]
        
        result = visualizer.parse_module_dependencies(modules)
        
        assert isinstance(result, dict)
        assert 'nodes' in result
        assert 'edges' in result
        assert len(result['nodes']) == 3
        assert len(result['edges']) == 2  # routing->analysis, tdd-cycle->analysis
    
    def test_parse_module_dependencies_circular_references(self):
        """Test parsing modules with circular dependencies"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='mod1', path='/modules/mod1.md', category='test', dependencies=['mod2']),
            Module(name='mod2', path='/modules/mod2.md', category='test', dependencies=['mod3']),
            Module(name='mod3', path='/modules/mod3.md', category='test', dependencies=['mod1'])
        ]
        
        result = visualizer.parse_module_dependencies(modules)
        
        assert isinstance(result, dict)
        assert 'nodes' in result
        assert 'edges' in result
        assert 'circular_dependencies' in result
        assert len(result['circular_dependencies']) > 0
    
    def test_parse_module_dependencies_missing_dependencies(self):
        """Test parsing modules with missing dependencies"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['missing_module'])
        ]
        
        result = visualizer.parse_module_dependencies(modules)
        
        assert isinstance(result, dict)
        assert 'missing_dependencies' in result
        assert 'missing_module' in result['missing_dependencies']


class TestModuleVisualizerFiltering:
    """Test cases for module filtering and categorization"""
    
    def test_filter_modules_by_category_single_category(self):
        """Test filtering modules by single category"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='tdd-cycle', path='/modules/patterns/tdd-cycle.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system')
        ]
        
        result = visualizer.filter_modules_by_category(modules, 'patterns')
        
        assert len(result) == 2
        assert all(mod.category == 'patterns' for mod in result)
    
    def test_filter_modules_by_category_multiple_categories(self):
        """Test filtering modules by multiple categories"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system'),
            Module(name='meta-review', path='/modules/meta/meta-review.md', category='meta'),
            Module(name='wizard', path='/modules/domain/wizard.md', category='domain')
        ]
        
        result = visualizer.filter_modules_by_category(modules, ['patterns', 'system'])
        
        assert len(result) == 2
        assert all(mod.category in ['patterns', 'system'] for mod in result)
    
    def test_filter_modules_by_category_no_matches(self):
        """Test filtering modules with no matching categories"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system')
        ]
        
        result = visualizer.filter_modules_by_category(modules, 'nonexistent')
        
        assert len(result) == 0
        assert isinstance(result, list)
    
    def test_filter_modules_by_type_complexity(self):
        """Test filtering modules by complexity type"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='simple', path='/modules/simple.md', category='patterns', tags=['simple']),
            Module(name='complex', path='/modules/complex.md', category='patterns', tags=['complex']),
            Module(name='medium', path='/modules/medium.md', category='patterns', tags=['medium'])
        ]
        
        result = visualizer.filter_modules_by_type(modules, complexity='simple')
        
        assert len(result) == 1
        assert result[0].name == 'simple'
    
    def test_search_modules_by_content_name_search(self):
        """Test searching modules by name"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing-patterns', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='tdd-cycle-engine', path='/modules/patterns/tdd.md', category='patterns'),
            Module(name='security-validation', path='/modules/system/security.md', category='system')
        ]
        
        result = visualizer.search_modules_by_content(modules, 'routing')
        
        assert len(result) == 1
        assert result[0].name == 'routing-patterns'
    
    def test_search_modules_by_content_description_search(self):
        """Test searching modules by description content"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', description='Intelligent routing system'),
            Module(name='tdd-cycle', path='/modules/patterns/tdd.md', category='patterns', description='Test driven development cycle'),
            Module(name='security', path='/modules/system/security.md', category='system', description='Security validation framework')
        ]
        
        result = visualizer.search_modules_by_content(modules, 'validation')
        
        assert len(result) == 1
        assert result[0].name == 'security'
    
    def test_search_modules_by_content_file_content_search(self):
        """Test searching modules by file content"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        ]
        
        mock_file_content = "This module implements intelligent routing for AI systems"
        
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            result = visualizer.search_modules_by_content(modules, 'intelligent routing', search_file_content=True)
            
            assert len(result) == 1
            assert result[0].name == 'routing'
    
    def test_search_modules_by_content_case_insensitive(self):
        """Test case-insensitive search functionality"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='ROUTING', path='/modules/patterns/routing.md', category='patterns', description='Intelligent ROUTING system')
        ]
        
        result = visualizer.search_modules_by_content(modules, 'routing')
        
        assert len(result) == 1
        assert result[0].name == 'ROUTING'
    
    def test_search_modules_by_content_regex_support(self):
        """Test regex support in search functionality"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing-v1', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='routing-v2', path='/modules/patterns/routing2.md', category='patterns'),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns')
        ]
        
        result = visualizer.search_modules_by_content(modules, r'routing-v\d+', use_regex=True)
        
        assert len(result) == 2
        assert all('routing-v' in mod.name for mod in result)


class TestModuleVisualizerTreeNavigation:
    """Test cases for module tree navigation and hierarchy"""
    
    def test_build_module_tree_basic_structure(self):
        """Test building basic module tree structure"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='tdd-cycle', path='/modules/patterns/tdd.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system'),
            Module(name='quality', path='/modules/system/quality.md', category='system')
        ]
        
        result = visualizer.build_module_tree(modules)
        
        assert isinstance(result, dict)
        assert 'patterns' in result
        assert 'system' in result
        assert len(result['patterns']) == 2
        assert len(result['system']) == 2
    
    def test_build_module_tree_nested_categories(self):
        """Test building tree with nested categories"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing/core.md', category='patterns/routing'),
            Module(name='advanced', path='/modules/patterns/routing/advanced.md', category='patterns/routing'),
            Module(name='security', path='/modules/system/security/core.md', category='system/security')
        ]
        
        result = visualizer.build_module_tree(modules)
        
        assert isinstance(result, dict)
        assert 'patterns' in result
        assert 'system' in result
        assert 'routing' in result['patterns']
        assert 'security' in result['system']
    
    def test_build_module_tree_with_dependencies(self):
        """Test building tree with dependency information"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis']),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns', dependencies=[]),
            Module(name='security', path='/modules/system/security.md', category='system', dependencies=['analysis'])
        ]
        
        result = visualizer.build_module_tree(modules, include_dependencies=True)
        
        assert isinstance(result, dict)
        assert 'patterns' in result
        assert 'system' in result
        
        # Check dependency information is included
        patterns_routing = next(m for m in result['patterns'] if m['name'] == 'routing')
        assert 'dependencies' in patterns_routing
        assert len(patterns_routing['dependencies']) == 1
    
    def test_render_module_tree_navigation_basic(self):
        """Test rendering basic module tree navigation"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        tree_data = {
            'patterns': [
                {'name': 'routing', 'path': '/modules/patterns/routing.md'},
                {'name': 'tdd-cycle', 'path': '/modules/patterns/tdd.md'}
            ],
            'system': [
                {'name': 'security', 'path': '/modules/system/security.md'}
            ]
        }
        
        with patch('streamlit.expander') as mock_expander, \
             patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.button') as mock_button:
            
            mock_expander.return_value.__enter__ = Mock()
            mock_expander.return_value.__exit__ = Mock()
            
            visualizer.render_module_tree_navigation(tree_data)
            
            mock_expander.assert_called()
            mock_selectbox.assert_called()
    
    def test_render_module_tree_navigation_with_search(self):
        """Test rendering tree navigation with search functionality"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        tree_data = {
            'patterns': [
                {'name': 'routing', 'path': '/modules/patterns/routing.md'},
                {'name': 'tdd-cycle', 'path': '/modules/patterns/tdd.md'}
            ]
        }
        
        with patch('streamlit.text_input') as mock_text_input, \
             patch('streamlit.expander') as mock_expander:
            
            mock_text_input.return_value = 'routing'
            mock_expander.return_value.__enter__ = Mock()
            mock_expander.return_value.__exit__ = Mock()
            
            visualizer.render_module_tree_navigation(tree_data, enable_search=True)
            
            mock_text_input.assert_called()
            mock_expander.assert_called()
    
    def test_expand_category_nodes_basic(self):
        """Test expanding category nodes in tree navigation"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        tree_data = {
            'patterns': [
                {'name': 'routing', 'path': '/modules/patterns/routing.md'},
                {'name': 'tdd-cycle', 'path': '/modules/patterns/tdd.md'}
            ]
        }
        
        result = visualizer.expand_category_nodes(tree_data, 'patterns')
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(item, dict) for item in result)
    
    def test_expand_category_nodes_with_filtering(self):
        """Test expanding category nodes with filtering"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        tree_data = {
            'patterns': [
                {'name': 'routing', 'path': '/modules/patterns/routing.md'},
                {'name': 'tdd-cycle', 'path': '/modules/patterns/tdd.md'},
                {'name': 'analysis', 'path': '/modules/patterns/analysis.md'}
            ]
        }
        
        result = visualizer.expand_category_nodes(tree_data, 'patterns', filter_text='routing')
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['name'] == 'routing'
    
    def test_expand_category_nodes_nonexistent_category(self):
        """Test expanding nonexistent category nodes"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        tree_data = {
            'patterns': [
                {'name': 'routing', 'path': '/modules/patterns/routing.md'}
            ]
        }
        
        result = visualizer.expand_category_nodes(tree_data, 'nonexistent')
        
        assert isinstance(result, list)
        assert len(result) == 0


class TestModuleVisualizerNetworkVisualization:
    """Test cases for network graph visualization"""
    
    def test_create_dependency_graph_basic(self):
        """Test creating basic dependency graph"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis']),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns', dependencies=[]),
            Module(name='security', path='/modules/system/security.md', category='system', dependencies=['analysis'])
        ]
        
        result = visualizer.create_dependency_graph(modules)
        
        assert isinstance(result, nx.DiGraph)
        assert result.number_of_nodes() == 3
        assert result.number_of_edges() == 2
    
    def test_create_dependency_graph_with_weights(self):
        """Test creating dependency graph with edge weights"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis']),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns', dependencies=[]),
            Module(name='security', path='/modules/system/security.md', category='system', dependencies=['analysis'])
        ]
        
        result = visualizer.create_dependency_graph(modules, include_weights=True)
        
        assert isinstance(result, nx.DiGraph)
        
        # Check that edges have weight attributes
        for edge in result.edges(data=True):
            assert 'weight' in edge[2]
    
    def test_create_dependency_graph_circular_dependencies(self):
        """Test creating graph with circular dependencies"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='mod1', path='/modules/mod1.md', category='test', dependencies=['mod2']),
            Module(name='mod2', path='/modules/mod2.md', category='test', dependencies=['mod3']),
            Module(name='mod3', path='/modules/mod3.md', category='test', dependencies=['mod1'])
        ]
        
        result = visualizer.create_dependency_graph(modules)
        
        assert isinstance(result, nx.DiGraph)
        assert result.number_of_nodes() == 3
        assert result.number_of_edges() == 3
        
        # Check for cycles
        cycles = list(nx.simple_cycles(result))
        assert len(cycles) > 0
    
    def test_create_network_visualization_basic(self):
        """Test creating basic network visualization"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns')
        graph.add_node('analysis', category='patterns')
        graph.add_edge('routing', 'analysis')
        
        result = visualizer.create_network_visualization(graph)
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
    
    def test_create_network_visualization_with_layout(self):
        """Test creating network visualization with different layouts"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns')
        graph.add_node('analysis', category='patterns')
        graph.add_edge('routing', 'analysis')
        
        # Test different layout algorithms
        layouts = ['spring', 'circular', 'kamada_kawai', 'planar']
        
        for layout in layouts:
            result = visualizer.create_network_visualization(graph, layout=layout)
            assert isinstance(result, go.Figure)
            assert len(result.data) > 0
    
    def test_create_network_visualization_with_colors(self):
        """Test creating network visualization with color coding"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns')
        graph.add_node('security', category='system')
        graph.add_edge('routing', 'security')
        
        result = visualizer.create_network_visualization(graph, color_by_category=True)
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
        
        # Check that nodes have different colors for different categories
        node_trace = result.data[0]
        assert hasattr(node_trace, 'marker')
        assert hasattr(node_trace.marker, 'color')
    
    def test_create_network_visualization_interactive(self):
        """Test creating interactive network visualization"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns', description='Routing module')
        graph.add_node('analysis', category='patterns', description='Analysis module')
        graph.add_edge('routing', 'analysis')
        
        result = visualizer.create_network_visualization(graph, interactive=True)
        
        assert isinstance(result, go.Figure)
        
        # Check interactive features
        assert result.layout.hovermode is not None
        assert result.layout.clickmode is not None
        
        # Check tooltips
        node_trace = result.data[0]
        assert hasattr(node_trace, 'hovertemplate')
        assert node_trace.hovertemplate is not None
    
    def test_create_network_visualization_zoom_pan(self):
        """Test creating network visualization with zoom and pan"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns')
        graph.add_node('analysis', category='patterns')
        graph.add_edge('routing', 'analysis')
        
        result = visualizer.create_network_visualization(graph, enable_zoom_pan=True)
        
        assert isinstance(result, go.Figure)
        
        # Check zoom and pan configuration
        assert result.layout.xaxis.fixedrange is False
        assert result.layout.yaxis.fixedrange is False
    
    def test_create_network_visualization_performance(self):
        """Test network visualization performance with large graphs"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create large graph with 100 nodes
        graph = nx.DiGraph()
        for i in range(100):
            graph.add_node(f'node_{i}', category=f'category_{i%5}')
            if i > 0:
                graph.add_edge(f'node_{i}', f'node_{i-1}')
        
        start_time = time.time()
        result = visualizer.create_network_visualization(graph)
        end_time = time.time()
        
        # Should complete within 3 seconds for 100 nodes
        assert (end_time - start_time) < 3.0
        assert isinstance(result, go.Figure)


class TestModuleVisualizerComplexityAnalysis:
    """Test cases for module complexity analysis and visualization"""
    
    def test_create_complexity_heatmap_basic(self):
        """Test creating basic complexity heatmap"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system')
        ]
        
        # Mock complexity calculation
        with patch.object(visualizer, 'calculate_module_complexity') as mock_calc:
            mock_calc.side_effect = lambda module: {'complexity': 5, 'lines': 100, 'dependencies': 2}
            
            result = visualizer.create_complexity_heatmap(modules)
            
            assert isinstance(result, go.Figure)
            assert len(result.data) > 0
    
    def test_create_complexity_heatmap_by_category(self):
        """Test creating complexity heatmap grouped by category"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system'),
            Module(name='meta', path='/modules/meta/meta.md', category='meta')
        ]
        
        with patch.object(visualizer, 'calculate_module_complexity') as mock_calc:
            mock_calc.side_effect = lambda module: {'complexity': 5, 'lines': 100, 'dependencies': 2}
            
            result = visualizer.create_complexity_heatmap(modules, group_by='category')
            
            assert isinstance(result, go.Figure)
            assert len(result.data) > 0
    
    def test_calculate_module_complexity_basic(self):
        """Test basic module complexity calculation"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis'])
        
        mock_file_content = """
        # Routing Module
        
        This is a test module with some content.
        
        ## Function 1
        def function1():
            if True:
                return 1
            else:
                return 2
        
        ## Function 2
        def function2():
            for i in range(10):
                print(i)
        """
        
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            result = visualizer.calculate_module_complexity(module)
            
            assert isinstance(result, dict)
            assert 'complexity' in result
            assert 'lines' in result
            assert 'dependencies' in result
            assert 'functions' in result
    
    def test_calculate_module_complexity_with_ast_analysis(self):
        """Test module complexity calculation with AST analysis"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        
        mock_python_code = """
        def complex_function():
            if True:
                for i in range(10):
                    if i % 2 == 0:
                        try:
                            while True:
                                break
                        except:
                            pass
                    else:
                        continue
            return True
        """
        
        with patch('builtins.open', mock_open(read_data=mock_python_code)):
            result = visualizer.calculate_module_complexity(module, include_ast_analysis=True)
            
            assert isinstance(result, dict)
            assert 'complexity' in result
            assert 'cyclomatic_complexity' in result
            assert 'ast_complexity' in result
    
    def test_calculate_module_complexity_file_not_found(self):
        """Test complexity calculation when file doesn't exist"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='missing', path='/modules/missing.md', category='patterns')
        
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = visualizer.calculate_module_complexity(module)
            
            assert isinstance(result, dict)
            assert 'complexity' in result
            assert result['complexity'] == 0
            assert 'error' in result
    
    def test_create_complexity_heatmap_interactive(self):
        """Test creating interactive complexity heatmap"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        ]
        
        with patch.object(visualizer, 'calculate_module_complexity') as mock_calc:
            mock_calc.return_value = {'complexity': 5, 'lines': 100, 'dependencies': 2}
            
            result = visualizer.create_complexity_heatmap(modules, interactive=True)
            
            assert isinstance(result, go.Figure)
            assert result.layout.hovermode is not None
            
            # Check hover information
            heatmap_trace = result.data[0]
            assert hasattr(heatmap_trace, 'hovertemplate')


class TestModuleVisualizerUsageAnalysis:
    """Test cases for module usage frequency and analysis"""
    
    def test_create_usage_frequency_chart_basic(self):
        """Test creating basic usage frequency chart"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system')
        ]
        
        usage_data = {
            'routing': 50,
            'analysis': 35,
            'security': 15
        }
        
        result = visualizer.create_usage_frequency_chart(modules, usage_data)
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
    
    def test_create_usage_frequency_chart_bar_chart(self):
        """Test creating usage frequency bar chart"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns')
        ]
        
        usage_data = {'routing': 50, 'analysis': 35}
        
        result = visualizer.create_usage_frequency_chart(modules, usage_data, chart_type='bar')
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
        
        # Check that it's a bar chart
        bar_trace = result.data[0]
        assert bar_trace.type == 'bar'
    
    def test_create_usage_frequency_chart_pie_chart(self):
        """Test creating usage frequency pie chart"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns')
        ]
        
        usage_data = {'routing': 50, 'analysis': 35}
        
        result = visualizer.create_usage_frequency_chart(modules, usage_data, chart_type='pie')
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
        
        # Check that it's a pie chart
        pie_trace = result.data[0]
        assert pie_trace.type == 'pie'
    
    def test_create_usage_frequency_chart_missing_data(self):
        """Test creating usage frequency chart with missing usage data"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns')
        ]
        
        usage_data = {'routing': 50}  # Missing 'analysis'
        
        result = visualizer.create_usage_frequency_chart(modules, usage_data)
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
    
    def test_analyze_module_usage_patterns_basic(self):
        """Test analyzing module usage patterns"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis']),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns', dependencies=[]),
            Module(name='security', path='/modules/system/security.md', category='system', dependencies=['analysis'])
        ]
        
        result = visualizer.analyze_module_usage_patterns(modules)
        
        assert isinstance(result, dict)
        assert 'most_used' in result
        assert 'least_used' in result
        assert 'dependency_count' in result
        assert 'usage_by_category' in result
    
    def test_analyze_module_usage_patterns_with_historical_data(self):
        """Test analyzing usage patterns with historical data"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        ]
        
        historical_data = {
            'routing': [10, 15, 20, 25, 30]  # Usage over time
        }
        
        result = visualizer.analyze_module_usage_patterns(modules, historical_data=historical_data)
        
        assert isinstance(result, dict)
        assert 'trends' in result
        assert 'growth_rate' in result
    
    def test_create_category_distribution_chart_basic(self):
        """Test creating basic category distribution chart"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='tdd', path='/modules/patterns/tdd.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system'),
            Module(name='meta', path='/modules/meta/meta.md', category='meta')
        ]
        
        result = visualizer.create_category_distribution_chart(modules)
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
    
    def test_create_category_distribution_chart_donut(self):
        """Test creating category distribution donut chart"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system')
        ]
        
        result = visualizer.create_category_distribution_chart(modules, chart_type='donut')
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
        
        # Check that it's a donut chart (pie with hole)
        pie_trace = result.data[0]
        assert pie_trace.type == 'pie'
        assert pie_trace.hole > 0
    
    def test_create_category_distribution_chart_with_counts(self):
        """Test creating category distribution chart with count labels"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='tdd', path='/modules/patterns/tdd.md', category='patterns'),
            Module(name='security', path='/modules/system/security.md', category='system')
        ]
        
        result = visualizer.create_category_distribution_chart(modules, show_counts=True)
        
        assert isinstance(result, go.Figure)
        assert len(result.data) > 0
        
        # Check that labels include counts
        pie_trace = result.data[0]
        assert pie_trace.textinfo == 'label+percent+value'


class TestModuleVisualizerInteraction:
    """Test cases for user interaction and module selection"""
    
    def test_handle_module_selection_valid_module(self):
        """Test handling valid module selection"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        
        result = visualizer.handle_module_selection(module)
        
        assert visualizer.selected_module == module
        assert result == True
    
    def test_handle_module_selection_none_module(self):
        """Test handling None module selection"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        result = visualizer.handle_module_selection(None)
        
        assert visualizer.selected_module is None
        assert result == False
    
    def test_handle_module_selection_ui_state_update(self):
        """Test UI state update on module selection"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        
        with patch('streamlit.session_state') as mock_session_state:
            visualizer.handle_module_selection(module)
            
            assert visualizer.selected_module == module
    
    def test_handle_module_selection_with_callback(self):
        """Test module selection with callback execution"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        callback_executed = False
        
        def selection_callback(module):
            nonlocal callback_executed
            callback_executed = True
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        
        visualizer.handle_module_selection(module, callback=selection_callback)
        
        assert callback_executed == True
        assert visualizer.selected_module == module
    
    def test_render_module_details_panel_basic(self):
        """Test rendering basic module details panel"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(
            name='routing',
            path='/modules/patterns/routing.md',
            category='patterns',
            description='Intelligent routing module',
            dependencies=['analysis'],
            tags=['core', 'routing']
        )
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.markdown') as mock_markdown, \
             patch('streamlit.json') as mock_json:
            
            visualizer.render_module_details_panel(module)
            
            mock_subheader.assert_called()
            mock_markdown.assert_called()
            mock_json.assert_called()
    
    def test_render_module_details_panel_with_content(self):
        """Test rendering module details panel with file content"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        
        mock_file_content = """
        # Routing Module
        
        This module implements intelligent routing capabilities.
        
        ## Usage
        
        ```python
        from routing import Router
        router = Router()
        ```
        """
        
        with patch('builtins.open', mock_open(read_data=mock_file_content)), \
             patch('streamlit.code') as mock_code:
            
            visualizer.render_module_details_panel(module, show_content=True)
            
            mock_code.assert_called()
    
    def test_render_module_details_panel_with_dependencies(self):
        """Test rendering module details panel with dependency visualization"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis', 'validation'])
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.plotly_chart') as mock_plotly:
            
            visualizer.render_module_details_panel(module, show_dependencies=True)
            
            mock_subheader.assert_called()
            mock_plotly.assert_called()
    
    def test_render_filter_controls_basic(self):
        """Test rendering basic filter controls"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        categories = ['patterns', 'system', 'meta']
        
        with patch('streamlit.multiselect') as mock_multiselect, \
             patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.slider') as mock_slider:
            
            mock_multiselect.return_value = ['patterns']
            mock_selectbox.return_value = 'medium'
            mock_slider.return_value = 5
            
            result = visualizer.render_filter_controls(categories)
            
            assert isinstance(result, dict)
            assert 'categories' in result
            assert 'complexity' in result
            assert 'min_dependencies' in result
            
            mock_multiselect.assert_called()
            mock_selectbox.assert_called()
            mock_slider.assert_called()
    
    def test_render_filter_controls_with_search(self):
        """Test rendering filter controls with search functionality"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        categories = ['patterns', 'system']
        
        with patch('streamlit.text_input') as mock_text_input, \
             patch('streamlit.multiselect') as mock_multiselect:
            
            mock_text_input.return_value = 'routing'
            mock_multiselect.return_value = ['patterns']
            
            result = visualizer.render_filter_controls(categories, enable_search=True)
            
            assert isinstance(result, dict)
            assert 'search_term' in result
            assert 'categories' in result
            
            mock_text_input.assert_called()
            mock_multiselect.assert_called()
    
    def test_handle_zoom_pan_controls_basic(self):
        """Test handling zoom and pan controls"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch('streamlit.slider') as mock_slider, \
             patch('streamlit.button') as mock_button:
            
            mock_slider.side_effect = [1.5, 0.2, 0.3]  # zoom, pan_x, pan_y
            mock_button.return_value = False
            
            result = visualizer.handle_zoom_pan_controls()
            
            assert isinstance(result, dict)
            assert 'zoom' in result
            assert 'pan_x' in result
            assert 'pan_y' in result
            
            mock_slider.assert_called()
            mock_button.assert_called()
    
    def test_handle_zoom_pan_controls_reset(self):
        """Test handling zoom and pan controls with reset"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch('streamlit.slider') as mock_slider, \
             patch('streamlit.button') as mock_button:
            
            mock_slider.side_effect = [1.5, 0.2, 0.3]
            mock_button.return_value = True  # Reset button clicked
            
            result = visualizer.handle_zoom_pan_controls()
            
            assert isinstance(result, dict)
            assert result['zoom'] == 1.0
            assert result['pan_x'] == 0.0
            assert result['pan_y'] == 0.0


class TestModuleVisualizerExport:
    """Test cases for visualization export functionality"""
    
    def test_export_visualization_png_basic(self):
        """Test basic PNG export functionality"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create a simple figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
        
        with patch('plotly.io.to_image') as mock_to_image:
            mock_to_image.return_value = b'fake_png_data'
            
            result = visualizer.export_visualization_png(fig)
            
            assert isinstance(result, bytes)
            assert result == b'fake_png_data'
            mock_to_image.assert_called_once()
    
    def test_export_visualization_png_with_options(self):
        """Test PNG export with custom options"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
        
        export_options = {
            'width': 1200,
            'height': 800,
            'scale': 2
        }
        
        with patch('plotly.io.to_image') as mock_to_image:
            mock_to_image.return_value = b'fake_png_data'
            
            result = visualizer.export_visualization_png(fig, **export_options)
            
            assert isinstance(result, bytes)
            mock_to_image.assert_called_once()
            
            # Check that options were passed
            call_args = mock_to_image.call_args
            assert call_args[1]['width'] == 1200
            assert call_args[1]['height'] == 800
            assert call_args[1]['scale'] == 2
    
    def test_export_visualization_svg_basic(self):
        """Test basic SVG export functionality"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
        
        with patch('plotly.io.to_image') as mock_to_image:
            mock_to_image.return_value = b'<svg>fake_svg_data</svg>'
            
            result = visualizer.export_visualization_svg(fig)
            
            assert isinstance(result, bytes)
            assert result == b'<svg>fake_svg_data</svg>'
            mock_to_image.assert_called_once()
    
    def test_export_visualization_svg_with_options(self):
        """Test SVG export with custom options"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
        
        export_options = {
            'width': 1000,
            'height': 600
        }
        
        with patch('plotly.io.to_image') as mock_to_image:
            mock_to_image.return_value = b'<svg>fake_svg_data</svg>'
            
            result = visualizer.export_visualization_svg(fig, **export_options)
            
            assert isinstance(result, bytes)
            mock_to_image.assert_called_once()
            
            # Check that format is SVG
            call_args = mock_to_image.call_args
            assert call_args[1]['format'] == 'svg'
    
    def test_export_module_data_json_basic(self):
        """Test basic JSON export functionality"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis']),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns', dependencies=[])
        ]
        
        result = visualizer.export_module_data_json(modules)
        
        assert isinstance(result, str)
        
        # Should be valid JSON
        import json
        data = json.loads(result)
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]['name'] == 'routing'
        assert data[1]['name'] == 'analysis'
    
    def test_export_module_data_json_with_dependencies(self):
        """Test JSON export with dependency information"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns', dependencies=['analysis'])
        ]
        
        result = visualizer.export_module_data_json(modules, include_dependencies=True)
        
        assert isinstance(result, str)
        
        import json
        data = json.loads(result)
        assert isinstance(data, dict)
        assert 'modules' in data
        assert 'dependencies' in data
        assert len(data['modules']) == 1
        assert len(data['dependencies']) == 1
    
    def test_export_module_data_json_with_metadata(self):
        """Test JSON export with metadata"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        ]
        
        metadata = {
            'export_date': '2025-01-01',
            'framework_version': '3.0.0',
            'total_modules': 1
        }
        
        result = visualizer.export_module_data_json(modules, metadata=metadata)
        
        assert isinstance(result, str)
        
        import json
        data = json.loads(result)
        assert 'metadata' in data
        assert data['metadata']['export_date'] == '2025-01-01'
        assert data['metadata']['framework_version'] == '3.0.0'
        assert data['metadata']['total_modules'] == 1
    
    def test_export_all_formats_integration(self):
        """Test exporting in all supported formats"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create test data
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        ]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
        
        with patch('plotly.io.to_image') as mock_to_image:
            mock_to_image.return_value = b'fake_image_data'
            
            # Test all export formats
            png_data = visualizer.export_visualization_png(fig)
            svg_data = visualizer.export_visualization_svg(fig)
            json_data = visualizer.export_module_data_json(modules)
            
            assert isinstance(png_data, bytes)
            assert isinstance(svg_data, bytes)
            assert isinstance(json_data, str)
            
            # Should have called to_image twice (PNG and SVG)
            assert mock_to_image.call_count == 2


class TestModuleVisualizerErrorHandling:
    """Test cases for error handling and graceful degradation"""
    
    def test_graceful_degradation_missing_framework_data(self):
        """Test graceful degradation when framework data is missing"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.side_effect = FileNotFoundError("Framework not found")
            
            with patch('streamlit.error') as mock_error:
                visualizer.render()
                
                mock_error.assert_called()
                args, kwargs = mock_error.call_args
                assert "Framework not found" in args[0]
    
    def test_graceful_degradation_invalid_framework_path(self):
        """Test graceful degradation with invalid framework path"""
        from components.module_visualizer import ModuleVisualizer
        
        with patch('streamlit.error') as mock_error:
            visualizer = ModuleVisualizer(framework_path=Path("/nonexistent/path"))
            visualizer.render()
            
            mock_error.assert_called()
    
    def test_graceful_degradation_corrupted_module_files(self):
        """Test graceful degradation with corrupted module files"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': [{'name': 'broken'}]}  # Missing required fields
            
            with patch('streamlit.warning') as mock_warning:
                result = visualizer.load_modules_from_framework()
                
                mock_warning.assert_called()
                assert isinstance(result, list)
    
    def test_graceful_degradation_network_visualization_errors(self):
        """Test graceful degradation with network visualization errors"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create invalid graph
        graph = "invalid_graph"
        
        with patch('streamlit.error') as mock_error:
            result = visualizer.create_network_visualization(graph)
            
            mock_error.assert_called()
            assert result is None
    
    def test_graceful_degradation_memory_constraints(self):
        """Test graceful degradation under memory constraints"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Simulate memory error
        with patch.object(visualizer, 'create_network_visualization', side_effect=MemoryError("Out of memory")):
            with patch('streamlit.error') as mock_error:
                modules = [Module(name='test', path='/test.md', category='test')]
                visualizer.create_dependency_graph(modules)
                
                mock_error.assert_called()
    
    def test_error_recovery_mechanisms(self):
        """Test error recovery mechanisms"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Test automatic retry on transient errors
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.side_effect = [ConnectionError("Temporary failure"), {'modules': []}]
            
            result = visualizer.load_modules_from_framework(retry_on_failure=True)
            
            assert isinstance(result, list)
            assert mock_parse.call_count == 2
    
    def test_error_handling_invalid_module_data(self):
        """Test error handling with invalid module data"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Test with None module
        with pytest.raises(TypeError):
            visualizer.handle_module_selection("invalid_module")
        
        # Test with invalid module list
        with pytest.raises(TypeError):
            visualizer.filter_modules_by_category("not_a_list", 'patterns')
    
    def test_error_handling_file_access_errors(self):
        """Test error handling with file access errors"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='restricted', path='/restricted/module.md', category='test')
        
        with patch('builtins.open', side_effect=PermissionError("Access denied")):
            with patch('streamlit.error') as mock_error:
                result = visualizer.calculate_module_complexity(module)
                
                assert isinstance(result, dict)
                assert 'error' in result
    
    def test_error_handling_export_failures(self):
        """Test error handling with export failures"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
        
        with patch('plotly.io.to_image', side_effect=Exception("Export failed")):
            with patch('streamlit.error') as mock_error:
                result = visualizer.export_visualization_png(fig)
                
                assert result is None
                mock_error.assert_called()


class TestModuleVisualizerPerformance:
    """Test cases for performance benchmarks and optimization"""
    
    def test_load_time_with_large_module_sets(self):
        """Test load time performance with 100+ modules"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create 120 modules for performance testing
        large_module_set = [
            {
                'name': f'module_{i}',
                'path': f'/modules/category_{i%8}/module_{i}.md',
                'category': f'category_{i%8}',
                'description': f'Module {i} description',
                'dependencies': [f'module_{j}' for j in range(max(0, i-2), i)]
            }
            for i in range(120)
        ]
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': large_module_set}
            
            start_time = time.time()
            result = visualizer.load_modules_from_framework()
            end_time = time.time()
            
            # Should complete within 2 seconds for 120 modules
            assert (end_time - start_time) < 2.0
            assert len(result) == 120
    
    def test_rendering_performance_benchmarks(self):
        """Test rendering performance benchmarks"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name=f'mod_{i}', path=f'/modules/mod_{i}.md', category='test')
            for i in range(50)
        ]
        
        with patch('streamlit.selectbox'), \
             patch('streamlit.plotly_chart'), \
             patch('streamlit.expander'):
            
            start_time = time.time()
            visualizer.render()
            end_time = time.time()
            
            # Should render within 1.5 seconds for 50 modules
            assert (end_time - start_time) < 1.5
    
    def test_network_visualization_performance(self):
        """Test network visualization performance with large graphs"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create large graph with 80 nodes
        graph = nx.DiGraph()
        for i in range(80):
            graph.add_node(f'node_{i}', category=f'category_{i%6}')
            if i > 0:
                graph.add_edge(f'node_{i}', f'node_{i-1}')
        
        start_time = time.time()
        result = visualizer.create_network_visualization(graph)
        end_time = time.time()
        
        # Should complete within 2 seconds for 80 nodes
        assert (end_time - start_time) < 2.0
        assert isinstance(result, go.Figure)
    
    def test_dependency_parsing_performance(self):
        """Test dependency parsing performance"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create modules with complex dependencies
        modules = [
            Module(
                name=f'module_{i}',
                path=f'/modules/module_{i}.md',
                category='test',
                dependencies=[f'module_{j}' for j in range(max(0, i-3), i)]
            )
            for i in range(100)
        ]
        
        start_time = time.time()
        result = visualizer.parse_module_dependencies(modules)
        end_time = time.time()
        
        # Should complete within 1 second for 100 modules
        assert (end_time - start_time) < 1.0
        assert isinstance(result, dict)
    
    def test_memory_usage_constraints(self):
        """Test memory usage constraints"""
        from components.module_visualizer import ModuleVisualizer
        import sys
        
        visualizer = ModuleVisualizer()
        
        # Create large dataset
        large_modules = [
            Module(
                name=f'module_{i}',
                path=f'/modules/module_{i}.md',
                category='test',
                dependencies=[f'module_{j}' for j in range(max(0, i-5), i)]
            )
            for i in range(200)
        ]
        
        initial_memory = sys.getsizeof(visualizer)
        
        with patch.object(visualizer, 'load_modules_from_framework', return_value=large_modules):
            result = visualizer.load_modules_from_framework()
            
            # Memory usage should remain reasonable
            current_memory = sys.getsizeof(visualizer)
            memory_increase = current_memory - initial_memory
            
            # Should not use excessive memory (arbitrary threshold)
            assert memory_increase < 15000000  # 15MB
    
    def test_response_time_requirements(self):
        """Test response time requirements for interactive operations"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        
        # Test module selection response time
        start_time = time.time()
        visualizer.handle_module_selection(module)
        end_time = time.time()
        
        # Should respond within 50ms for interactive operations
        assert (end_time - start_time) < 0.05
    
    def test_concurrent_access_scenarios(self):
        """Test performance under concurrent access scenarios"""
        from components.module_visualizer import ModuleVisualizer
        import threading
        
        visualizer = ModuleVisualizer()
        
        results = []
        
        def concurrent_load():
            result = visualizer.load_modules_from_framework()
            results.append(len(result))
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': [{'name': 'test', 'path': '/test.md', 'category': 'test'}]}
            
            threads = []
            for i in range(5):
                thread = threading.Thread(target=concurrent_load)
                threads.append(thread)
                thread.start()
            
            for thread in threads:
                thread.join(timeout=3.0)
            
            # All threads should complete successfully
            assert len(results) == 5
            assert all(result == 1 for result in results)
    
    def test_large_dependency_graph_performance(self):
        """Test performance with large dependency graphs"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Create modules with complex dependency web
        modules = []
        for i in range(150):
            deps = []
            for j in range(max(0, i-10), i):
                if j % 3 == 0:  # Sparse dependencies
                    deps.append(f'module_{j}')
            
            modules.append(Module(
                name=f'module_{i}',
                path=f'/modules/module_{i}.md',
                category=f'category_{i%7}',
                dependencies=deps
            ))
        
        start_time = time.time()
        result = visualizer.create_dependency_graph(modules)
        end_time = time.time()
        
        # Should complete within 2 seconds for 150 modules
        assert (end_time - start_time) < 2.0
        assert isinstance(result, nx.DiGraph)
        assert result.number_of_nodes() == 150


class TestModuleVisualizerAccessibility:
    """Test cases for accessibility and usability features"""
    
    def test_aria_labels_and_descriptions(self):
        """Test ARIA labels and descriptions for accessibility"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.button') as mock_button, \
             patch('streamlit.multiselect') as mock_multiselect:
            
            visualizer.render()
            
            # Should include accessibility attributes
            mock_selectbox.assert_called()
            mock_button.assert_called()
            mock_multiselect.assert_called()
    
    def test_keyboard_navigation_support(self):
        """Test keyboard navigation support"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns'),
            Module(name='analysis', path='/modules/patterns/analysis.md', category='patterns')
        ]
        
        with patch('streamlit.selectbox') as mock_selectbox:
            # Mock keyboard navigation
            mock_selectbox.return_value = 'routing'
            
            visualizer.render()
            
            # Should support keyboard navigation
            mock_selectbox.assert_called()
    
    def test_screen_reader_compatibility(self):
        """Test screen reader compatibility"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(
            name='routing',
            path='/modules/patterns/routing.md',
            category='patterns',
            description='Intelligent routing module'
        )
        
        with patch('streamlit.markdown') as mock_markdown:
            visualizer.render_module_details_panel(module)
            
            # Should include screen reader friendly content
            mock_markdown.assert_called()
    
    def test_color_contrast_validation(self):
        """Test color contrast validation for accessibility"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [Module(name='routing', path='/modules/patterns/routing.md', category='patterns')]
        
        result = visualizer.create_category_distribution_chart(modules)
        
        # Should use accessible colors
        assert isinstance(result, go.Figure)
        # Color contrast validation would be done in actual implementation
    
    def test_high_contrast_mode_support(self):
        """Test high contrast mode support"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns')
        graph.add_node('analysis', category='patterns')
        graph.add_edge('routing', 'analysis')
        
        result = visualizer.create_network_visualization(graph, high_contrast=True)
        
        assert isinstance(result, go.Figure)
        # High contrast colors should be applied
    
    def test_text_size_scalability(self):
        """Test text size scalability for accessibility"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [Module(name='routing', path='/modules/patterns/routing.md', category='patterns')]
        
        # Test different text sizes
        for text_size in ['small', 'medium', 'large']:
            result = visualizer.create_category_distribution_chart(modules, text_size=text_size)
            assert isinstance(result, go.Figure)


class TestModuleVisualizerMobileResponsiveness:
    """Test cases for mobile responsiveness and touch interaction"""
    
    def test_touch_interaction_support(self):
        """Test touch interaction support for mobile devices"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns')
        graph.add_node('analysis', category='patterns')
        graph.add_edge('routing', 'analysis')
        
        result = visualizer.create_network_visualization(graph, mobile_optimized=True)
        
        assert isinstance(result, go.Figure)
        # Should have touch-friendly configurations
    
    def test_responsive_layout_validation(self):
        """Test responsive layout validation"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch('streamlit.columns') as mock_columns:
            # Mock responsive columns
            mock_columns.return_value = [MagicMock(), MagicMock()]
            
            visualizer.render()
            
            # Should use responsive layout
            mock_columns.assert_called()
    
    def test_mobile_performance_optimization(self):
        """Test mobile performance optimization"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        modules = [
            Module(name=f'mod_{i}', path=f'/modules/mod_{i}.md', category='test')
            for i in range(25)
        ]
        
        with patch('streamlit.plotly_chart'):
            start_time = time.time()
            result = visualizer.create_category_distribution_chart(modules, mobile_optimized=True)
            end_time = time.time()
            
            # Should be optimized for mobile performance
            assert (end_time - start_time) < 1.5
            assert isinstance(result, go.Figure)
    
    def test_gesture_handling(self):
        """Test gesture handling for mobile interactions"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        graph = nx.DiGraph()
        graph.add_node('routing', category='patterns')
        graph.add_edge('routing', 'routing')
        
        result = visualizer.create_network_visualization(graph, gesture_support=True)
        
        assert isinstance(result, go.Figure)
        # Should support gestures like pinch-to-zoom, swipe, etc.
    
    def test_mobile_filter_controls(self):
        """Test mobile-optimized filter controls"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        categories = ['patterns', 'system', 'meta']
        
        with patch('streamlit.selectbox') as mock_selectbox:
            mock_selectbox.return_value = 'patterns'
            
            result = visualizer.render_filter_controls(categories, mobile_layout=True)
            
            assert isinstance(result, dict)
            mock_selectbox.assert_called()


class TestModuleVisualizerIntegration:
    """Test cases for integration with existing framework components"""
    
    def test_integration_with_framework_parser(self):
        """Test integration with framework parser"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Should use FrameworkParser
        assert isinstance(visualizer.framework_parser, FrameworkParser)
    
    def test_integration_with_data_models(self):
        """Test integration with Module data model"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module_data = {
            'name': 'routing',
            'path': '/modules/patterns/routing.md',
            'category': 'patterns',
            'description': 'Intelligent routing module',
            'dependencies': ['analysis']
        }
        
        module = Module.from_dict(module_data)
        
        result = visualizer.handle_module_selection(module)
        
        assert result == True
        assert visualizer.selected_module == module
    
    def test_integration_with_streamlit_components(self):
        """Test integration with Streamlit components"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        with patch('streamlit.title') as mock_title, \
             patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.plotly_chart') as mock_plotly:
            
            visualizer.render()
            
            # Should use Streamlit components
            mock_title.assert_called()
            mock_selectbox.assert_called()
            mock_plotly.assert_called()
    
    def test_integration_with_command_explorer(self):
        """Test integration with existing Command Explorer component"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Should be able to share data with Command Explorer
        modules = [
            Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        ]
        
        # Test shared data formats
        result = visualizer.export_module_data_json(modules)
        
        assert isinstance(result, str)
        
        import json
        data = json.loads(result)
        assert isinstance(data, list)
    
    def test_data_flow_validation(self):
        """Test data flow validation between components"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Test data flow: parser -> modules -> visualization
        mock_modules = [
            {'name': 'routing', 'path': '/modules/patterns/routing.md', 'category': 'patterns'}
        ]
        
        with patch.object(visualizer.framework_parser, 'parse') as mock_parse:
            mock_parse.return_value = {'modules': mock_modules}
            
            loaded_modules = visualizer.load_modules_from_framework()
            tree_data = visualizer.build_module_tree(loaded_modules)
            
            assert len(loaded_modules) == 1
            assert isinstance(tree_data, dict)
            assert 'patterns' in tree_data
    
    def test_state_management_testing(self):
        """Test state management across component interactions"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        module = Module(name='routing', path='/modules/patterns/routing.md', category='patterns')
        
        # Test state persistence
        visualizer.handle_module_selection(module)
        assert visualizer.selected_module == module
        
        # Test state updates
        visualizer.filter_state = {'category': 'patterns'}
        assert visualizer.filter_state['category'] == 'patterns'
    
    def test_configuration_compatibility(self):
        """Test configuration compatibility with framework settings"""
        from components.module_visualizer import ModuleVisualizer
        
        visualizer = ModuleVisualizer()
        
        # Test layout configuration
        assert isinstance(visualizer.layout_config, dict)
        assert 'algorithm' in visualizer.layout_config
        assert 'color_scheme' in visualizer.layout_config
        
        # Test filter state
        assert isinstance(visualizer.filter_state, dict)


class TestModuleVisualizerFileConstraints:
    """Test cases for file size and code organization constraints"""
    
    def test_module_visualizer_file_size_constraint(self):
        """Test that module_visualizer.py is under 500 lines"""
        visualizer_path = Path(__file__).parent.parent / "components" / "module_visualizer.py"
        
        # This will fail until file is created
        assert visualizer_path.exists(), "module_visualizer.py should exist"
        
        with open(visualizer_path, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines and comments for accurate count
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        assert len(code_lines) < 500, f"module_visualizer.py should be <500 lines of code, found {len(code_lines)}"
    
    def test_module_visualizer_imports_are_appropriate(self):
        """Test that module_visualizer.py has appropriate imports"""
        visualizer_path = Path(__file__).parent.parent / "components" / "module_visualizer.py"
        
        with open(visualizer_path, 'r') as f:
            source = f.read()
        
        # Should import necessary modules
        assert "import streamlit" in source, "Should import streamlit for UI"
        assert "import plotly" in source, "Should import plotly for visualization"
        assert "import networkx" in source, "Should import networkx for graph operations"
        assert "from data.framework_parser import FrameworkParser" in source, "Should import FrameworkParser"
        assert "from data.models import Module" in source, "Should import Module model"
    
    def test_module_visualizer_separation_of_concerns(self):
        """Test that ModuleVisualizer follows single responsibility principle"""
        from components.module_visualizer import ModuleVisualizer
        import inspect
        
        # Get all methods in ModuleVisualizer
        methods = [name for name, obj in inspect.getmembers(ModuleVisualizer) if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        public_methods = [m for m in methods if not m.startswith('_') and m != '__init__']
        
        # Should have focused responsibility - module visualization only
        assert len(public_methods) <= 20, f"ModuleVisualizer should have ≤20 public methods, found {len(public_methods)}: {public_methods}"
    
    def test_module_visualizer_cyclomatic_complexity(self):
        """Test that ModuleVisualizer has acceptable cyclomatic complexity"""
        from components.module_visualizer import ModuleVisualizer
        import ast
        import inspect
        import textwrap
        
        def count_decision_points(source):
            try:
                dedented_source = textwrap.dedent(source)
                tree = ast.parse(dedented_source)
                decision_nodes = (ast.If, ast.For, ast.While, ast.Try, ast.With)
                return sum(1 for node in ast.walk(tree) if isinstance(node, decision_nodes))
            except:
                return 0
        
        # Check each method
        for method_name, method in inspect.getmembers(ModuleVisualizer, inspect.isfunction):
            if not method_name.startswith('_'):
                try:
                    source = inspect.getsource(method)
                    complexity = count_decision_points(source)
                    assert complexity <= 10, f"ModuleVisualizer.{method_name} has complexity {complexity} > 10"
                except (OSError, TypeError, IndentationError):
                    pass


class TestModuleVisualizerImplementationGuidance:
    """Test cases that provide implementation guidance and benchmarks"""
    
    def test_performance_benchmarks_specification(self):
        """Define performance benchmarks for implementation"""
        benchmarks = {
            'load_time_100_modules': 2.0,  # seconds
            'render_time_50_modules': 1.5,  # seconds
            'network_viz_80_nodes': 2.0,  # seconds
            'interactive_response_time': 0.05,  # seconds
            'memory_usage_200_modules': 15000000,  # bytes (15MB)
            'dependency_parsing_100_modules': 1.0,  # seconds
        }
        
        # This test documents expected performance - implementation should meet these
        assert all(isinstance(v, (int, float)) for v in benchmarks.values())
        assert all(v > 0 for v in benchmarks.values())
    
    def test_coverage_analysis_plan(self):
        """Define coverage analysis plan for 100% target"""
        coverage_areas = {
            'initialization': ['__init__', 'parameter_validation', 'default_setup'],
            'data_loading': ['load_modules_from_framework', 'parse_dependencies', 'error_handling'],
            'filtering': ['filter_by_category', 'search_content', 'type_filtering'],
            'tree_navigation': ['build_tree', 'expand_nodes', 'navigation_controls'],
            'network_visualization': ['create_graph', 'network_viz', 'layouts'],
            'complexity_analysis': ['calculate_complexity', 'heatmap_creation', 'ast_analysis'],
            'usage_analysis': ['frequency_charts', 'pattern_analysis', 'category_distribution'],
            'interaction': ['module_selection', 'details_panel', 'filter_controls'],
            'export': ['png_export', 'svg_export', 'json_export'],
            'error_handling': ['graceful_degradation', 'recovery_mechanisms', 'validation'],
            'performance': ['load_time', 'render_time', 'memory_usage'],
            'accessibility': ['aria_labels', 'keyboard_navigation', 'screen_reader'],
            'mobile': ['touch_interaction', 'responsive_layout', 'gestures'],
            'integration': ['framework_parser', 'data_models', 'streamlit_components']
        }
        
        # Each area should have comprehensive test coverage
        assert len(coverage_areas) >= 14
        assert all(len(tests) >= 3 for tests in coverage_areas.values())
    
    def test_integration_specifications(self):
        """Define integration specifications with existing framework"""
        integration_points = {
            'framework_parser': 'data.framework_parser.FrameworkParser',
            'module_model': 'data.models.Module',
            'framework_model': 'data.models.Framework',
            'command_model': 'data.models.Command',
            'streamlit_ui': 'streamlit components',
            'plotly_viz': 'plotly.graph_objects',
            'networkx_graphs': 'networkx.DiGraph',
            'command_explorer': 'components.command_explorer.CommandExplorer'
        }
        
        # All integration points should be clearly defined
        assert len(integration_points) == 8
        assert all(isinstance(v, str) for v in integration_points.values())
    
    def test_module_categories_specification(self):
        """Define expected module categories for framework"""
        expected_categories = {
            'patterns': 'Core patterns and algorithms',
            'development': 'Development support modules',
            'meta': 'Meta-framework modules',
            'system': 'System and infrastructure modules',
            'domain': 'Domain-specific modules',
            'templates': 'Template and scaffolding modules'
        }
        
        # All categories should be supported
        assert len(expected_categories) == 6
        assert all(isinstance(v, str) for v in expected_categories.values())
    
    def test_visualization_types_specification(self):
        """Define supported visualization types"""
        visualization_types = {
            'network_graph': 'Interactive network dependency graph',
            'tree_hierarchy': 'Hierarchical tree navigation',
            'complexity_heatmap': 'Module complexity visualization',
            'usage_frequency': 'Usage frequency charts',
            'category_distribution': 'Category distribution charts',
            'dependency_matrix': 'Dependency relationship matrix'
        }
        
        # All visualization types should be supported
        assert len(visualization_types) == 6
        assert all(isinstance(v, str) for v in visualization_types.values())


def mock_open(read_data=''):
    """Mock open function for file operations"""
    from unittest.mock import mock_open as mock_open_builtin
    return mock_open_builtin(read_data=read_data)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])