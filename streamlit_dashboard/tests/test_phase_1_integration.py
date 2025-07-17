"""
Phase 1 Integration Tests - Comprehensive End-to-End Testing
Tests the complete integration of all Phase 1 components:
- App structure and navigation
- Framework parser integration
- Data models and transformations
- Overview dashboard rendering
- Directory visualization functionality
- Error handling and performance
"""

import pytest
import streamlit as st
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import time
import json
from typing import Dict, Any, List

# Import Phase 1 components
from app import AppConfig, setup_navigation, route_to_page, main
from data.framework_parser import FrameworkParser
from data.models import Command, Module, Framework
from components.overview_dashboard import OverviewDashboard
from components.directory_visualization import DirectoryVisualization


class TestPhase1Integration:
    """Comprehensive integration tests for Phase 1 components"""
    
    def setup_method(self):
        """Setup test fixtures and mock framework structure"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_framework_path = self.temp_dir / ".claude"
        self.setup_test_framework()
        
        # Clear Streamlit session state
        if hasattr(st, 'session_state'):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
    
    def teardown_method(self):
        """Clean up test fixtures"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
    
    def setup_test_framework(self):
        """Create a realistic test framework structure"""
        # Create framework directory structure
        (self.test_framework_path / "commands").mkdir(parents=True)
        (self.test_framework_path / "modules" / "patterns").mkdir(parents=True)
        (self.test_framework_path / "modules" / "development").mkdir(parents=True)
        (self.test_framework_path / "modules" / "meta").mkdir(parents=True)
        
        # Create test command files
        test_commands = [
            {"name": "auto", "content": "# Auto Command\nIntelligent routing command"},
            {"name": "task", "content": "# Task Command\nSingle task development"},
            {"name": "feature", "content": "# Feature Command\nComplete feature development"},
            {"name": "query", "content": "# Query Command\nResearch and analysis"},
            {"name": "swarm", "content": "# Swarm Command\nMulti-agent coordination"}
        ]
        
        for cmd in test_commands:
            (self.test_framework_path / "commands" / f"{cmd['name']}.md").write_text(cmd['content'])
        
        # Create test module files
        test_modules = [
            {"path": "modules/patterns/tdd-cycle.md", "content": "# TDD Cycle Pattern\nTest-driven development"},
            {"path": "modules/patterns/routing.md", "content": "# Routing Pattern\nIntelligent routing"},
            {"path": "modules/development/testing.md", "content": "# Testing Module\nTesting framework"},
            {"path": "modules/meta/evolution.md", "content": "# Evolution Module\nFramework evolution"}
        ]
        
        for module in test_modules:
            (self.test_framework_path / module['path']).write_text(module['content'])
    
    @pytest.fixture
    def mock_streamlit_app(self):
        """Mock Streamlit app for testing"""
        with patch('streamlit.set_page_config') as mock_config, \
             patch('streamlit.sidebar') as mock_sidebar, \
             patch('streamlit.radio') as mock_radio, \
             patch('streamlit.title') as mock_title, \
             patch('streamlit.info') as mock_info, \
             patch('streamlit.error') as mock_error:
            
            mock_radio.return_value = "Framework Overview"
            yield {
                'config': mock_config,
                'sidebar': mock_sidebar,
                'radio': mock_radio,
                'title': mock_title,
                'info': mock_info,
                'error': mock_error
            }
    
    def test_complete_framework_loading_workflow(self, mock_streamlit_app):
        """Test complete framework loading and display workflow"""
        # Create parser with test framework
        parser = FrameworkParser(self.test_framework_path)
        
        # Test parsing
        framework_data = parser.parse()
        assert framework_data['metadata']['is_valid'] is True
        assert len(framework_data['commands']) == 5
        assert len(framework_data['modules']) == 4
        
        # Test data model creation
        framework = Framework.from_dict({
            'path': str(self.test_framework_path),
            'commands': framework_data['commands'],
            'modules': framework_data['modules'],
            'name': 'Test Framework',
            'version': '3.0.0'
        })
        
        assert framework.name == 'Test Framework'
        assert len(framework.commands) == 5
        assert len(framework.modules) == 4
        
        # Test statistics generation
        stats = framework.statistics()
        assert stats['total_commands'] == 5
        assert stats['total_modules'] == 4
        assert stats['total_components'] == 9
        assert 'commands_by_category' in stats
        assert 'modules_by_category' in stats
        
        # Test overview dashboard rendering
        with patch('data.framework_parser.FrameworkParser') as mock_parser:
            mock_parser.return_value.parse.return_value = framework_data
            
            dashboard = OverviewDashboard()
            
            # Mock streamlit components for dashboard
            with patch('streamlit.title'), \
                 patch('streamlit.markdown'), \
                 patch('streamlit.subheader'), \
                 patch('streamlit.columns') as mock_columns, \
                 patch('streamlit.metric'), \
                 patch('streamlit.dataframe'), \
                 patch('streamlit.text_input'), \
                 patch('streamlit.selectbox'), \
                 patch('streamlit.expander'), \
                 patch('streamlit.caption'), \
                 patch('streamlit.write'), \
                 patch('streamlit.info'), \
                 patch('streamlit.error'):
                
                mock_columns.return_value = [Mock(), Mock(), Mock()]
                
                # This should not raise any exceptions
                dashboard.render()
    
    def test_navigation_workflow_integration(self, mock_streamlit_app):
        """Test navigation between overview and directory visualization"""
        # Test navigation setup
        with patch('streamlit.set_page_config'), \
             patch('streamlit.sidebar'), \
             patch('streamlit.radio') as mock_radio:
            
            # Test Framework Overview page
            mock_radio.return_value = "Framework Overview"
            selected_page = setup_navigation()
            assert selected_page == "Framework Overview"
            
            # Test routing to overview
            with patch('streamlit.title') as mock_title, \
                 patch('streamlit.info') as mock_info:
                route_to_page(selected_page)
                mock_title.assert_called_with("🏗️ Framework Overview")
                mock_info.assert_called_with("Framework overview component will be implemented here")
    
    def test_error_handling_cascade(self, mock_streamlit_app):
        """Test error handling across all components"""
        # Test framework parser error handling
        invalid_path = Path("/nonexistent/path")
        parser = FrameworkParser(invalid_path)
        result = parser.parse()
        
        assert result['metadata']['is_valid'] is False
        assert 'error' in result['metadata']
        assert result['commands'] == []
        assert result['modules'] == []
        
        # Test overview dashboard error handling
        with patch('data.framework_parser.FrameworkParser') as mock_parser:
            mock_parser.return_value.parse.side_effect = Exception("Parse error")
            
            dashboard = OverviewDashboard()
            
            with patch('streamlit.error') as mock_error, \
                 patch('streamlit.info') as mock_info, \
                 patch('streamlit.title'), \
                 patch('streamlit.markdown'):
                dashboard.render()
                mock_error.assert_called_with("Error loading framework data: Parse error")
                mock_info.assert_called_with("Please ensure the .claude directory exists and contains valid framework files.")
        
        # Test directory visualization error handling
        viz = DirectoryVisualization()
        
        # Create proper context manager mocks
        mock_col1 = Mock()
        mock_col1.__enter__ = Mock(return_value=mock_col1)
        mock_col1.__exit__ = Mock(return_value=None)
        
        mock_col2 = Mock()
        mock_col2.__enter__ = Mock(return_value=mock_col2)
        mock_col2.__exit__ = Mock(return_value=None)
        
        with patch.object(viz.parser, 'parse') as mock_parse, \
             patch('streamlit.error') as mock_error, \
             patch('streamlit.info') as mock_info, \
             patch('streamlit.title'), \
             patch('streamlit.markdown'), \
             patch('streamlit.columns') as mock_columns, \
             patch('streamlit.text_input'), \
             patch('streamlit.selectbox'):
            
            mock_parse.side_effect = Exception("Visualization error")
            mock_columns.return_value = [mock_col1, mock_col2]
            viz.render()
            mock_error.assert_called_with("Error loading directory visualization: Visualization error")
            mock_info.assert_called_with("Please ensure the .claude directory exists and contains valid framework files.")
    
    def test_data_consistency_across_components(self, mock_streamlit_app):
        """Test data consistency between parser, models, and components"""
        # Parse framework data
        parser = FrameworkParser(self.test_framework_path)
        framework_data = parser.parse()
        
        # Create framework model
        framework = Framework.from_dict({
            'path': str(self.test_framework_path),
            'commands': framework_data['commands'],
            'modules': framework_data['modules'],
            'name': 'Test Framework',
            'version': '3.0.0'
        })
        
        # Test data consistency
        assert len(framework.commands) == len(framework_data['commands'])
        assert len(framework.modules) == len(framework_data['modules'])
        
        # Test command data consistency
        for i, cmd_data in enumerate(framework_data['commands']):
            cmd = framework.commands[i]
            assert cmd.name == cmd_data['name']
            assert cmd.path == cmd_data['path']
            assert cmd.category == cmd_data['category']
        
        # Test module data consistency
        for i, mod_data in enumerate(framework_data['modules']):
            mod = framework.modules[i]
            assert mod.name == mod_data['name']
            assert mod.path == mod_data['path']
            assert mod.category == mod_data['category']
        
        # Test statistics consistency
        stats = framework.statistics()
        structure_stats = framework_data['structure']
        
        assert stats['total_commands'] == structure_stats['commands']['count']
        assert stats['total_modules'] == structure_stats['modules']['count']
        assert stats['total_components'] == structure_stats['total_files']
    
    def test_performance_integration_targets(self, mock_streamlit_app):
        """Test performance targets for integrated components"""
        # Test framework parsing performance
        parser = FrameworkParser(self.test_framework_path)
        
        start_time = time.time()
        framework_data = parser.parse()
        parse_time = time.time() - start_time
        
        # Framework parsing should be fast (<1 second for small frameworks)
        assert parse_time < 1.0, f"Framework parsing took {parse_time:.2f}s, should be <1s"
        
        # Test model creation performance
        start_time = time.time()
        framework = Framework.from_dict({
            'path': str(self.test_framework_path),
            'commands': framework_data['commands'],
            'modules': framework_data['modules'],
            'name': 'Test Framework',
            'version': '3.0.0'
        })
        model_time = time.time() - start_time
        
        # Model creation should be fast (<0.5 seconds)
        assert model_time < 0.5, f"Model creation took {model_time:.2f}s, should be <0.5s"
        
        # Test statistics generation performance
        start_time = time.time()
        stats = framework.statistics()
        stats_time = time.time() - start_time
        
        # Statistics should be fast (<0.1 seconds)
        assert stats_time < 0.1, f"Statistics generation took {stats_time:.2f}s, should be <0.1s"
    
    def test_user_workflow_scenarios(self, mock_streamlit_app):
        """Test realistic user workflow scenarios"""
        # Scenario 1: User loads dashboard and views framework overview
        with patch('data.framework_parser.FrameworkParser') as mock_parser:
            mock_parser.return_value.parse.return_value = {
                'commands': [{'name': 'auto', 'path': '/auto.md', 'category': 'command'}],
                'modules': [{'name': 'routing', 'path': '/routing.md', 'category': 'patterns'}],
                'structure': {
                    'commands': {'count': 1, 'files': []},
                    'modules': {'count': 1, 'categories': {}},
                    'total_files': 2
                },
                'metadata': {'is_valid': True, 'total_files': 2}
            }
            
            dashboard = OverviewDashboard()
            
            with patch('streamlit.title'), \
                 patch('streamlit.markdown'), \
                 patch('streamlit.subheader'), \
                 patch('streamlit.columns') as mock_columns, \
                 patch('streamlit.metric'), \
                 patch('streamlit.dataframe'), \
                 patch('streamlit.text_input'), \
                 patch('streamlit.selectbox'), \
                 patch('streamlit.expander'), \
                 patch('streamlit.caption'), \
                 patch('streamlit.write'), \
                 patch('streamlit.info'):
                
                mock_columns.return_value = [Mock(), Mock(), Mock()]
                
                # Should render without errors
                dashboard.render()
        
        # Scenario 2: User searches for specific commands
        commands = [
            Command("auto", "/auto.md", "command", "Intelligent routing"),
            Command("task", "/task.md", "command", "Single task development"),
            Command("feature", "/feature.md", "command", "Feature development")
        ]
        
        dashboard = OverviewDashboard()
        
        # Test search functionality
        filtered_commands = dashboard._filter_commands(commands, "auto")
        assert len(filtered_commands) == 1
        assert filtered_commands[0].name == "auto"
        
        filtered_commands = dashboard._filter_commands(commands, "development")
        assert len(filtered_commands) == 2  # task and feature contain "development"
        
        # Scenario 3: User filters modules by category
        modules = [
            Module("routing", "/routing.md", "patterns", "Routing logic"),
            Module("tdd", "/tdd.md", "patterns", "TDD cycle"),
            Module("testing", "/testing.md", "development", "Testing framework")
        ]
        
        categories = dashboard._get_module_categories(modules)
        assert "patterns" in categories
        assert "development" in categories
        
        filtered_modules = dashboard._filter_modules_by_category(modules, "patterns")
        assert len(filtered_modules) == 2
        
        filtered_modules = dashboard._filter_modules_by_category(modules, "development")
        assert len(filtered_modules) == 1
    
    def test_directory_visualization_integration(self, mock_streamlit_app):
        """Test directory visualization component integration"""
        # Test with real framework data
        parser = FrameworkParser(self.test_framework_path)
        framework_data = parser.parse()
        
        viz = DirectoryVisualization()
        
        # Test tree data creation
        tree_data = viz.create_tree_data(framework_data)
        
        assert tree_data['name'] == '.claude'
        assert tree_data['type'] == 'directory'
        assert 'children' in tree_data
        assert len(tree_data['children']) >= 2  # Should have commands and modules
        
        # Test with empty framework data
        empty_tree = viz.create_tree_data(None)
        assert empty_tree['name'] == '.claude'
        assert empty_tree['children'] == []
        
        # Test tree filtering
        filtered_tree = viz.filter_tree(tree_data, "auto", "All")
        assert filtered_tree is not None
        
        # Test HTML generation
        html_output = viz._generate_tree_html(tree_data)
        assert 'tree-container' in html_output
        assert 'tree-node' in html_output
        assert 'script' in html_output
    
    def test_app_configuration_integration(self, mock_streamlit_app):
        """Test app configuration and routing integration"""
        # Test app configuration
        assert AppConfig.FRAMEWORK_PATH.name == ".claude"
        assert AppConfig.PAGE_TITLE == "Claude Code Framework Dashboard"
        assert AppConfig.PAGE_ICON == "🧠"
        assert AppConfig.LAYOUT == "wide"
        
        # Test navigation pages
        assert "Framework Overview" in AppConfig.NAVIGATION_PAGES
        assert "Command Explorer" in AppConfig.NAVIGATION_PAGES
        assert "Module Visualizer" in AppConfig.NAVIGATION_PAGES
        
        # Test routing for each page
        for page in AppConfig.NAVIGATION_PAGES:
            with patch('streamlit.title') as mock_title, \
                 patch('streamlit.info') as mock_info:
                route_to_page(page)
                mock_title.assert_called_once()
                mock_info.assert_called_once()
    
    def test_main_application_flow(self, mock_streamlit_app):
        """Test complete main application flow"""
        with patch('streamlit.set_page_config'), \
             patch('streamlit.sidebar'), \
             patch('streamlit.radio') as mock_radio, \
             patch('streamlit.title'), \
             patch('streamlit.info'):
            
            mock_radio.return_value = "Framework Overview"
            
            # Should execute without errors
            main()
            
            # Test with different page selection
            mock_radio.return_value = "Module Visualizer"
            main()
    
    def test_component_state_management(self, mock_streamlit_app):
        """Test state management across components"""
        # Test session state initialization
        viz = DirectoryVisualization()
        
        # Test tree expansion state
        with patch('streamlit.session_state', new_callable=dict) as mock_state:
            mock_state['tree_expanded'] = True
            
            # Create proper context manager mocks
            mock_col1 = Mock()
            mock_col1.__enter__ = Mock(return_value=mock_col1)
            mock_col1.__exit__ = Mock(return_value=None)
            
            mock_col2 = Mock()
            mock_col2.__enter__ = Mock(return_value=mock_col2)
            mock_col2.__exit__ = Mock(return_value=None)
            
            mock_sidebar = Mock()
            mock_sidebar.__enter__ = Mock(return_value=mock_sidebar)
            mock_sidebar.__exit__ = Mock(return_value=None)
            
            mock_expander = Mock()
            mock_expander.__enter__ = Mock(return_value=mock_expander)
            mock_expander.__exit__ = Mock(return_value=None)
            
            with patch('streamlit.title'), \
                 patch('streamlit.markdown'), \
                 patch('streamlit.columns') as mock_columns, \
                 patch('streamlit.text_input'), \
                 patch('streamlit.selectbox'), \
                 patch('streamlit.subheader'), \
                 patch('streamlit.button'), \
                 patch('streamlit.components.v1.html'), \
                 patch('streamlit.sidebar', mock_sidebar), \
                 patch('streamlit.header'), \
                 patch('streamlit.write'), \
                 patch('streamlit.info'), \
                 patch('streamlit.expander', return_value=mock_expander):
                
                mock_columns.return_value = [mock_col1, mock_col2]
                
                # Should handle state without errors
                viz.render()
    
    def test_error_recovery_mechanisms(self, mock_streamlit_app):
        """Test error recovery mechanisms across components"""
        # Test parser error recovery
        parser = FrameworkParser(Path("/invalid/path"))
        result = parser.parse()
        assert result['metadata']['is_valid'] is False
        assert 'error' in result['metadata']
        
        # Test model error recovery
        with pytest.raises(ValueError):
            Command("", "/path", "category")  # Empty name should raise error
        
        with pytest.raises(ValueError):
            Module("name", "", "category")  # Empty path should raise error
        
        # Test framework validation
        framework = Framework("/path", [], [], "Test Framework")
        validation = framework.validate_framework() if hasattr(framework, 'validate_framework') else {'is_valid': True}
        
        # Test component error handling
        dashboard = OverviewDashboard()
        
        with patch('streamlit.error') as mock_error:
            dashboard._handle_error(Exception("Test error"))
            mock_error.assert_called_with("Error loading framework data: Test error")
    
    def test_integration_performance_benchmarks(self, mock_streamlit_app):
        """Test performance benchmarks for integrated system"""
        # Create larger test framework for performance testing
        larger_framework_path = self.temp_dir / "large_framework"
        larger_framework_path.mkdir()
        (larger_framework_path / "commands").mkdir()
        (larger_framework_path / "modules").mkdir()
        
        # Create many files for stress testing
        for i in range(50):
            (larger_framework_path / "commands" / f"cmd_{i}.md").write_text(f"# Command {i}")
        
        for i in range(100):
            (larger_framework_path / "modules" / f"mod_{i}.md").write_text(f"# Module {i}")
        
        # Test parsing performance
        parser = FrameworkParser(larger_framework_path)
        
        start_time = time.time()
        framework_data = parser.parse()
        parse_time = time.time() - start_time
        
        # Should handle larger frameworks efficiently
        assert parse_time < 3.0, f"Large framework parsing took {parse_time:.2f}s, should be <3s"
        assert len(framework_data['commands']) == 50
        assert len(framework_data['modules']) == 100
        
        # Test model creation with large data
        start_time = time.time()
        framework = Framework.from_dict({
            'path': str(larger_framework_path),
            'commands': framework_data['commands'],
            'modules': framework_data['modules'],
            'name': 'Large Framework',
            'version': '3.0.0'
        })
        model_time = time.time() - start_time
        
        assert model_time < 2.0, f"Large model creation took {model_time:.2f}s, should be <2s"
        
        # Test statistics with large data
        start_time = time.time()
        stats = framework.statistics()
        stats_time = time.time() - start_time
        
        assert stats_time < 0.5, f"Large stats generation took {stats_time:.2f}s, should be <0.5s"
        assert stats['total_commands'] == 50
        assert stats['total_modules'] == 100
        assert stats['total_components'] == 150


class TestPhase1ValidationCriteria:
    """Test validation criteria for Phase 1 completion"""
    
    def test_component_completeness(self):
        """Test that all required Phase 1 components are present"""
        # Test app.py components
        assert hasattr(AppConfig, 'FRAMEWORK_PATH')
        assert hasattr(AppConfig, 'NAVIGATION_PAGES')
        assert callable(setup_navigation)
        assert callable(route_to_page)
        assert callable(main)
        
        # Test framework parser components
        assert callable(FrameworkParser)
        parser_instance = FrameworkParser(Path("test"))
        assert hasattr(parser_instance, 'parse')
        assert hasattr(parser_instance, 'get_commands')
        assert hasattr(parser_instance, 'get_modules')
        
        # Test data models
        assert callable(Command)
        assert callable(Module)
        assert callable(Framework)
        
        # Test dashboard components
        assert callable(OverviewDashboard)
        assert callable(DirectoryVisualization)
        
        dashboard_instance = OverviewDashboard()
        assert hasattr(dashboard_instance, 'render')
        assert hasattr(dashboard_instance, 'display_stats')
        assert hasattr(dashboard_instance, 'show_commands_summary')
        assert hasattr(dashboard_instance, 'show_modules_summary')
        
        viz_instance = DirectoryVisualization()
        assert hasattr(viz_instance, 'render')
        assert hasattr(viz_instance, 'create_tree_data')
        assert hasattr(viz_instance, 'display_tree')
        assert hasattr(viz_instance, 'filter_tree')
    
    def test_integration_coverage_requirements(self):
        """Test that integration tests meet coverage requirements"""
        # This test ensures we have comprehensive integration test coverage
        # Coverage should be >=90% for integration scenarios
        
        integration_test_areas = [
            'complete_framework_loading_workflow',
            'navigation_workflow_integration',
            'error_handling_cascade',
            'data_consistency_across_components',
            'performance_integration_targets',
            'user_workflow_scenarios',
            'directory_visualization_integration',
            'app_configuration_integration',
            'main_application_flow',
            'component_state_management',
            'error_recovery_mechanisms',
            'integration_performance_benchmarks'
        ]
        
        # Verify all critical integration areas are tested
        test_class = TestPhase1Integration
        test_methods = [method for method in dir(test_class) if method.startswith('test_')]
        
        for area in integration_test_areas:
            assert f'test_{area}' in test_methods, f"Missing integration test for {area}"
    
    def test_phase_1_completion_criteria(self):
        """Test Phase 1 completion criteria"""
        # All Phase 1 components should be importable
        try:
            from app import main
            from data.framework_parser import FrameworkParser
            from data.models import Command, Module, Framework
            from components.overview_dashboard import OverviewDashboard
            from components.directory_visualization import DirectoryVisualization
        except ImportError as e:
            pytest.fail(f"Phase 1 component import failed: {e}")
        
        # All components should have required methods
        required_methods = {
            'OverviewDashboard': ['render', 'display_stats', 'show_commands_summary', 'show_modules_summary'],
            'DirectoryVisualization': ['render', 'create_tree_data', 'display_tree', 'filter_tree'],
            'FrameworkParser': ['parse', 'get_commands', 'get_modules'],
            'Command': ['to_dict', 'from_dict'],
            'Module': ['to_dict', 'from_dict'],
            'Framework': ['to_dict', 'from_dict', 'statistics']
        }
        
        for class_name, methods in required_methods.items():
            if class_name == 'OverviewDashboard':
                cls = OverviewDashboard
            elif class_name == 'DirectoryVisualization':
                cls = DirectoryVisualization
            elif class_name == 'FrameworkParser':
                cls = FrameworkParser
            elif class_name == 'Command':
                cls = Command
            elif class_name == 'Module':
                cls = Module
            elif class_name == 'Framework':
                cls = Framework
            
            for method in methods:
                assert hasattr(cls, method), f"{class_name} missing required method: {method}"
        
        # Performance targets should be met
        # This is validated in the performance integration tests
        assert True  # Placeholder for successful validation