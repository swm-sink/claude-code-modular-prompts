"""
TDD RED: Tests for overview dashboard component
These tests define the expected behavior of the framework overview dashboard
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import pandas as pd

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestOverviewDashboard:
    """Test cases for overview dashboard functionality"""
    
    def test_overview_dashboard_module_exists(self):
        """Test that overview dashboard module exists"""
        from components.overview_dashboard import OverviewDashboard
        assert OverviewDashboard is not None
    
    def test_overview_dashboard_has_render_method(self):
        """Test that OverviewDashboard has render method"""
        from components.overview_dashboard import OverviewDashboard
        dashboard = OverviewDashboard()
        assert hasattr(dashboard, 'render'), "OverviewDashboard should have render() method"
        assert callable(dashboard.render), "render should be callable"
    
    def test_overview_dashboard_has_display_stats_method(self):
        """Test that OverviewDashboard has display_stats method"""
        from components.overview_dashboard import OverviewDashboard
        dashboard = OverviewDashboard()
        assert hasattr(dashboard, 'display_stats'), "OverviewDashboard should have display_stats() method"
        assert callable(dashboard.display_stats), "display_stats should be callable"
    
    def test_overview_dashboard_has_show_commands_summary_method(self):
        """Test that OverviewDashboard has show_commands_summary method"""
        from components.overview_dashboard import OverviewDashboard
        dashboard = OverviewDashboard()
        assert hasattr(dashboard, 'show_commands_summary'), "OverviewDashboard should have show_commands_summary() method"
        assert callable(dashboard.show_commands_summary), "show_commands_summary should be callable"
    
    def test_overview_dashboard_has_show_modules_summary_method(self):
        """Test that OverviewDashboard has show_modules_summary method"""
        from components.overview_dashboard import OverviewDashboard
        dashboard = OverviewDashboard()
        assert hasattr(dashboard, 'show_modules_summary'), "OverviewDashboard should have show_modules_summary() method"
        assert callable(dashboard.show_modules_summary), "show_modules_summary should be callable"
    
    def test_overview_dashboard_file_size_constraint(self):
        """Test that overview_dashboard.py is under 500 lines"""
        dashboard_path = Path(__file__).parent.parent / "components" / "overview_dashboard.py"
        assert dashboard_path.exists(), "overview_dashboard.py should exist"
        
        with open(dashboard_path, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines and comments for more accurate count
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        assert len(code_lines) < 500, f"overview_dashboard.py should be <500 lines of code, found {len(code_lines)}"


class TestOverviewDashboardRendering:
    """Test cases for overview dashboard rendering functionality"""
    
    def test_render_method_displays_title(self):
        """Test that render method displays framework overview title"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch('streamlit.title') as mock_title:
            dashboard.render()
            
            # Should display a title
            mock_title.assert_called()
            args, kwargs = mock_title.call_args
            assert "Framework Overview" in args[0] or "Overview" in args[0]
    
    def test_render_method_displays_description(self):
        """Test that render method displays framework description"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch('streamlit.markdown') as mock_markdown:
            dashboard.render()
            
            # Should display description
            mock_markdown.assert_called()
    
    def test_render_method_calls_display_stats(self):
        """Test that render method calls display_stats"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch.object(dashboard, 'display_stats') as mock_display_stats:
            dashboard.render()
            
            # Should call display_stats
            mock_display_stats.assert_called_once()
    
    def test_render_method_calls_show_commands_summary(self):
        """Test that render method calls show_commands_summary"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch.object(dashboard, 'show_commands_summary') as mock_show_commands:
            dashboard.render()
            
            # Should call show_commands_summary
            mock_show_commands.assert_called_once()
    
    def test_render_method_calls_show_modules_summary(self):
        """Test that render method calls show_modules_summary"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch.object(dashboard, 'show_modules_summary') as mock_show_modules:
            dashboard.render()
            
            # Should call show_modules_summary
            mock_show_modules.assert_called_once()


class TestOverviewDashboardStats:
    """Test cases for overview dashboard statistics functionality"""
    
    def test_display_stats_shows_metrics(self):
        """Test that display_stats shows key framework metrics"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        # Mock framework data
        mock_framework = Mock()
        mock_framework.statistics.return_value = {
            'total_commands': 21,
            'total_modules': 64,
            'total_components': 85,
            'commands_by_category': {'command': 21},
            'modules_by_category': {'patterns': 25, 'security': 15, 'context': 24}
        }
        
        with patch('streamlit.columns') as mock_columns, \
             patch('streamlit.metric') as mock_metric:
            
            # Mock columns return with context manager support
            mock_col1, mock_col2, mock_col3 = MagicMock(), MagicMock(), MagicMock()
            mock_col1.__enter__ = MagicMock(return_value=mock_col1)
            mock_col1.__exit__ = MagicMock(return_value=None)
            mock_col2.__enter__ = MagicMock(return_value=mock_col2)
            mock_col2.__exit__ = MagicMock(return_value=None)
            mock_col3.__enter__ = MagicMock(return_value=mock_col3)
            mock_col3.__exit__ = MagicMock(return_value=None)
            mock_columns.return_value = [mock_col1, mock_col2, mock_col3]
            
            dashboard.display_stats(mock_framework)
            
            # Should create columns for metrics
            mock_columns.assert_called_once_with(3)
            
            # Should display metrics
            assert mock_metric.call_count >= 3
    
    def test_display_stats_handles_empty_framework(self):
        """Test that display_stats handles empty framework gracefully"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        # Mock empty framework
        mock_framework = Mock()
        mock_framework.statistics.return_value = {
            'total_commands': 0,
            'total_modules': 0,
            'total_components': 0,
            'commands_by_category': {},
            'modules_by_category': {}
        }
        
        with patch('streamlit.columns') as mock_columns, \
             patch('streamlit.metric') as mock_metric:
            
            # Mock columns return with context manager support
            mock_col1, mock_col2, mock_col3 = MagicMock(), MagicMock(), MagicMock()
            mock_col1.__enter__ = MagicMock(return_value=mock_col1)
            mock_col1.__exit__ = MagicMock(return_value=None)
            mock_col2.__enter__ = MagicMock(return_value=mock_col2)
            mock_col2.__exit__ = MagicMock(return_value=None)
            mock_col3.__enter__ = MagicMock(return_value=mock_col3)
            mock_col3.__exit__ = MagicMock(return_value=None)
            mock_columns.return_value = [mock_col1, mock_col2, mock_col3]
            
            dashboard.display_stats(mock_framework)
            
            # Should still create columns and display metrics
            mock_columns.assert_called_once_with(3)
            assert mock_metric.call_count >= 3
    
    def test_display_stats_shows_category_breakdown(self):
        """Test that display_stats shows category breakdown"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        # Mock framework data
        mock_framework = Mock()
        mock_framework.statistics.return_value = {
            'total_commands': 21,
            'total_modules': 64,
            'total_components': 85,
            'commands_by_category': {'command': 21},
            'modules_by_category': {'patterns': 25, 'security': 15, 'context': 24}
        }
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.columns') as mock_columns, \
             patch('streamlit.dataframe') as mock_dataframe:
            
            # Mock columns return with context manager support
            mock_col1, mock_col2, mock_col3 = MagicMock(), MagicMock(), MagicMock()
            mock_col1.__enter__ = MagicMock(return_value=mock_col1)
            mock_col1.__exit__ = MagicMock(return_value=None)
            mock_col2.__enter__ = MagicMock(return_value=mock_col2)
            mock_col2.__exit__ = MagicMock(return_value=None)
            mock_col3.__enter__ = MagicMock(return_value=mock_col3)
            mock_col3.__exit__ = MagicMock(return_value=None)
            mock_columns.return_value = [mock_col1, mock_col2, mock_col3]
            
            dashboard.display_stats(mock_framework)
            
            # Should display category breakdown
            mock_subheader.assert_called()
            mock_dataframe.assert_called()


class TestOverviewDashboardCommandsSummary:
    """Test cases for commands summary functionality"""
    
    def test_show_commands_summary_displays_commands(self):
        """Test that show_commands_summary displays commands information"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Command
        
        dashboard = OverviewDashboard()
        
        # Mock commands
        commands = [
            Command(name="auto", path="/commands/auto.md", category="command"),
            Command(name="task", path="/commands/task.md", category="command"),
            Command(name="feature", path="/commands/feature.md", category="command")
        ]
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.dataframe') as mock_dataframe, \
             patch('pandas.DataFrame') as mock_df_constructor:
            
            dashboard.show_commands_summary(commands)
            
            # Should display commands section
            mock_subheader.assert_called()
            mock_dataframe.assert_called()
            mock_df_constructor.assert_called()
    
    def test_show_commands_summary_handles_empty_commands(self):
        """Test that show_commands_summary handles empty commands list"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.info') as mock_info:
            
            dashboard.show_commands_summary([])
            
            # Should display info about no commands
            mock_subheader.assert_called()
            mock_info.assert_called()
    
    def test_show_commands_summary_creates_dataframe(self):
        """Test that show_commands_summary creates proper DataFrame"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Command
        
        dashboard = OverviewDashboard()
        
        # Mock commands
        commands = [
            Command(name="auto", path="/commands/auto.md", category="command", description="Intelligent routing"),
            Command(name="task", path="/commands/task.md", category="command", description="Single task development")
        ]
        
        with patch('streamlit.subheader'), \
             patch('streamlit.dataframe') as mock_dataframe, \
             patch('pandas.DataFrame') as mock_df_constructor:
            
            dashboard.show_commands_summary(commands)
            
            # Should create DataFrame with command data
            mock_df_constructor.assert_called_once()
            call_args = mock_df_constructor.call_args[0][0]
            
            # Should have proper columns
            assert len(call_args) == 2  # 2 commands
            assert all('name' in cmd for cmd in call_args)
            assert all('category' in cmd for cmd in call_args)
    
    def test_show_commands_summary_includes_search_functionality(self):
        """Test that show_commands_summary includes search functionality"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Command
        
        dashboard = OverviewDashboard()
        
        # Mock commands
        commands = [
            Command(name="auto", path="/commands/auto.md", category="command"),
            Command(name="task", path="/commands/task.md", category="command")
        ]
        
        with patch('streamlit.text_input') as mock_text_input, \
             patch('streamlit.subheader'), \
             patch('streamlit.dataframe'):
            
            # Mock text_input to return empty string
            mock_text_input.return_value = ""
            
            dashboard.show_commands_summary(commands)
            
            # Should include search input
            mock_text_input.assert_called()


class TestOverviewDashboardModulesSummary:
    """Test cases for modules summary functionality"""
    
    def test_show_modules_summary_displays_modules(self):
        """Test that show_modules_summary displays modules information"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Module
        
        dashboard = OverviewDashboard()
        
        # Mock modules
        modules = [
            Module(name="tdd-cycle-pattern", path="/modules/patterns/tdd-cycle-pattern.md", category="patterns"),
            Module(name="intelligent-routing", path="/modules/patterns/intelligent-routing.md", category="patterns"),
            Module(name="security-validator", path="/modules/security/security-validator.md", category="security")
        ]
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.dataframe') as mock_dataframe, \
             patch('pandas.DataFrame') as mock_df_constructor:
            
            dashboard.show_modules_summary(modules)
            
            # Should display modules section
            mock_subheader.assert_called()
            mock_dataframe.assert_called()
            mock_df_constructor.assert_called()
    
    def test_show_modules_summary_handles_empty_modules(self):
        """Test that show_modules_summary handles empty modules list"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.info') as mock_info:
            
            dashboard.show_modules_summary([])
            
            # Should display info about no modules
            mock_subheader.assert_called()
            mock_info.assert_called()
    
    def test_show_modules_summary_creates_dataframe(self):
        """Test that show_modules_summary creates proper DataFrame"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Module
        
        dashboard = OverviewDashboard()
        
        # Mock modules
        modules = [
            Module(name="tdd-cycle-pattern", path="/modules/patterns/tdd-cycle-pattern.md", category="patterns"),
            Module(name="security-validator", path="/modules/security/security-validator.md", category="security")
        ]
        
        with patch('streamlit.subheader'), \
             patch('streamlit.dataframe') as mock_dataframe, \
             patch('pandas.DataFrame') as mock_df_constructor:
            
            dashboard.show_modules_summary(modules)
            
            # Should create DataFrame with module data
            assert mock_df_constructor.call_count > 0  # Should be called at least once
            
            # Get the last call to verify structure
            call_args = mock_df_constructor.call_args[0][0]
            
            # Should have proper columns
            assert len(call_args) >= 1  # At least one module per call
            assert all('name' in mod for mod in call_args)
            assert all('category' in mod for mod in call_args)
    
    def test_show_modules_summary_includes_category_filter(self):
        """Test that show_modules_summary includes category filter"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Module
        
        dashboard = OverviewDashboard()
        
        # Mock modules
        modules = [
            Module(name="tdd-cycle-pattern", path="/modules/patterns/tdd-cycle-pattern.md", category="patterns"),
            Module(name="security-validator", path="/modules/security/security-validator.md", category="security")
        ]
        
        with patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.subheader'), \
             patch('streamlit.dataframe'):
            
            # Mock selectbox to return "All Categories"
            mock_selectbox.return_value = "All Categories"
            
            dashboard.show_modules_summary(modules)
            
            # Should include category filter
            mock_selectbox.assert_called()
    
    def test_show_modules_summary_groups_by_category(self):
        """Test that show_modules_summary can group modules by category"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Module
        
        dashboard = OverviewDashboard()
        
        # Mock modules with different categories
        modules = [
            Module(name="pattern1", path="/modules/patterns/pattern1.md", category="patterns"),
            Module(name="pattern2", path="/modules/patterns/pattern2.md", category="patterns"),
            Module(name="security1", path="/modules/security/security1.md", category="security")
        ]
        
        with patch('streamlit.subheader') as mock_subheader, \
             patch('streamlit.dataframe') as mock_dataframe, \
             patch('streamlit.expander') as mock_expander:
            
            # Mock expander with context manager support
            mock_expander_instance = MagicMock()
            mock_expander_instance.__enter__ = MagicMock(return_value=mock_expander_instance)
            mock_expander_instance.__exit__ = MagicMock(return_value=None)
            mock_expander.return_value = mock_expander_instance
            
            dashboard.show_modules_summary(modules)
            
            # Should group by category
            mock_expander.assert_called()


class TestOverviewDashboardIntegration:
    """Test cases for overview dashboard integration"""
    
    def test_overview_dashboard_works_with_framework_data(self):
        """Test that overview dashboard integrates with framework data"""
        from components.overview_dashboard import OverviewDashboard
        from data.models import Framework, Command, Module
        
        dashboard = OverviewDashboard()
        
        # Create mock framework with data
        framework = Framework(
            path="/test/.claude",
            commands=[
                Command(name="auto", path="/commands/auto.md", category="command"),
                Command(name="task", path="/commands/task.md", category="command")
            ],
            modules=[
                Module(name="tdd-cycle-pattern", path="/modules/patterns/tdd-cycle-pattern.md", category="patterns"),
                Module(name="security-validator", path="/modules/security/security-validator.md", category="security")
            ]
        )
        
        with patch('streamlit.title'), \
             patch('streamlit.markdown'), \
             patch('streamlit.columns') as mock_columns, \
             patch('streamlit.metric'), \
             patch('streamlit.subheader'), \
             patch('streamlit.dataframe'), \
             patch('streamlit.text_input') as mock_text_input, \
             patch('streamlit.selectbox') as mock_selectbox, \
             patch('streamlit.expander') as mock_expander:
            
            # Mock returns for streamlit components
            mock_col1, mock_col2, mock_col3 = MagicMock(), MagicMock(), MagicMock()
            mock_col1.__enter__ = MagicMock(return_value=mock_col1)
            mock_col1.__exit__ = MagicMock(return_value=None)
            mock_col2.__enter__ = MagicMock(return_value=mock_col2)
            mock_col2.__exit__ = MagicMock(return_value=None)
            mock_col3.__enter__ = MagicMock(return_value=mock_col3)
            mock_col3.__exit__ = MagicMock(return_value=None)
            mock_columns.return_value = [mock_col1, mock_col2, mock_col3]
            
            mock_text_input.return_value = ""
            mock_selectbox.return_value = "All Categories"
            
            mock_expander_instance = MagicMock()
            mock_expander_instance.__enter__ = MagicMock(return_value=mock_expander_instance)
            mock_expander_instance.__exit__ = MagicMock(return_value=None)
            mock_expander.return_value = mock_expander_instance
            
            # Should render without errors
            dashboard.render()
            dashboard.display_stats(framework)
            dashboard.show_commands_summary(framework.commands)
            dashboard.show_modules_summary(framework.modules)
    
    def test_overview_dashboard_follows_separation_of_concerns(self):
        """Test that overview dashboard follows single responsibility principle"""
        from components.overview_dashboard import OverviewDashboard
        import inspect
        
        # Get all methods in OverviewDashboard
        methods = [name for name, obj in inspect.getmembers(OverviewDashboard) if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        # Should have focused responsibility - displaying overview only
        expected_methods = ['render', 'display_stats', 'show_commands_summary', 'show_modules_summary']
        
        public_methods = [m for m in methods if not m.startswith('_') and m != '__init__']
        
        # Check that we don't have excessive methods (separation of concerns)
        assert len(public_methods) <= 6, f"OverviewDashboard should have ≤6 public methods, found {len(public_methods)}: {public_methods}"
        
        # Check that essential methods exist
        for method in expected_methods:
            assert method in public_methods, f"Missing required method: {method}"
    
    def test_overview_dashboard_imports_are_minimal(self):
        """Test that overview_dashboard.py has minimal imports"""
        dashboard_path = Path(__file__).parent.parent / "components" / "overview_dashboard.py"
        with open(dashboard_path, 'r') as f:
            source = f.read()
        
        # Should import only necessary modules
        assert "import streamlit" in source, "Should import streamlit for UI"
        assert "import pandas" in source, "Should import pandas for data handling"
        
        # Should NOT import complex unrelated modules
        forbidden_imports = [
            "import plotly.graph_objects",
            "from utils.complex_operations import",
            "from advanced_visualization import",
            "from machine_learning import"
        ]
        
        for forbidden in forbidden_imports:
            assert forbidden not in source, f"OverviewDashboard should not import unrelated modules: {forbidden}"


class TestOverviewDashboardEdgeCases:
    """Test cases for edge cases and error conditions"""
    
    def test_overview_dashboard_handles_none_framework(self):
        """Test that overview dashboard handles None framework gracefully"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        with patch('streamlit.error') as mock_error:
            dashboard.display_stats(None)
            
            # Should display error message
            mock_error.assert_called()
    
    def test_overview_dashboard_handles_malformed_data(self):
        """Test that overview dashboard handles malformed data"""
        from components.overview_dashboard import OverviewDashboard
        
        dashboard = OverviewDashboard()
        
        # Mock framework with malformed statistics
        mock_framework = Mock()
        mock_framework.statistics.return_value = None
        
        with patch('streamlit.error') as mock_error:
            dashboard.display_stats(mock_framework)
            
            # Should handle gracefully
            mock_error.assert_called()
    
    def test_overview_dashboard_cyclomatic_complexity(self):
        """Test that overview dashboard has acceptable cyclomatic complexity"""
        from components.overview_dashboard import OverviewDashboard
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
        for method_name, method in inspect.getmembers(OverviewDashboard, inspect.isfunction):
            if not method_name.startswith('_'):  # Only check public methods
                try:
                    source = inspect.getsource(method)
                    complexity = count_decision_points(source)
                    assert complexity <= 10, f"OverviewDashboard.{method_name} has complexity {complexity} > 10"
                except (OSError, TypeError, IndentationError):
                    # Skip methods we can't get source for or parse
                    pass