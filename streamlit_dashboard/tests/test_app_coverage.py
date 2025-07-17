"""
Additional tests to achieve 90% coverage for app.py
Tests the route_to_page function and various edge cases
"""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestAppCoverage:
    """Test cases to improve coverage for app.py"""
    
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_route_to_framework_overview(self, mock_info, mock_title):
        """Test routing to Framework Overview page"""
        import app
        
        app.route_to_page("Framework Overview")
        
        mock_title.assert_called_once_with("🏗️ Framework Overview")
        mock_info.assert_called_once_with("Framework overview component will be implemented here")
    
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_route_to_command_explorer(self, mock_info, mock_title):
        """Test routing to Command Explorer page"""
        import app
        
        app.route_to_page("Command Explorer")
        
        mock_title.assert_called_once_with("🔍 Command Explorer")
        mock_info.assert_called_once_with("Command explorer component will be implemented here")
    
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_route_to_module_visualizer(self, mock_info, mock_title):
        """Test routing to Module Visualizer page"""
        import app
        
        app.route_to_page("Module Visualizer")
        
        mock_title.assert_called_once_with("🧩 Module Visualizer")
        mock_info.assert_called_once_with("Module visualizer component will be implemented here")
    
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_route_to_prompt_constructor(self, mock_info, mock_title):
        """Test routing to Prompt Constructor page"""
        import app
        
        app.route_to_page("Prompt Constructor")
        
        mock_title.assert_called_once_with("🔨 Prompt Constructor")
        mock_info.assert_called_once_with("Prompt constructor component will be implemented here")
    
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_route_to_quality_gates(self, mock_info, mock_title):
        """Test routing to Quality Gates page"""
        import app
        
        app.route_to_page("Quality Gates")
        
        mock_title.assert_called_once_with("🛡️ Quality Gates")
        mock_info.assert_called_once_with("Quality gates component will be implemented here")
    
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_route_to_routing_simulator(self, mock_info, mock_title):
        """Test routing to Routing Simulator page"""
        import app
        
        app.route_to_page("Routing Simulator")
        
        mock_title.assert_called_once_with("🎯 Routing Simulator")
        mock_info.assert_called_once_with("Routing simulator component will be implemented here")
    
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_route_to_meta_framework(self, mock_info, mock_title):
        """Test routing to Meta Framework page"""
        import app
        
        app.route_to_page("Meta Framework")
        
        mock_title.assert_called_once_with("🌟 Meta Framework")
        mock_info.assert_called_once_with("Meta framework component will be implemented here")
    
    @patch('streamlit.error')
    def test_route_to_unknown_page(self, mock_error):
        """Test routing to unknown page shows error"""
        import app
        
        app.route_to_page("Unknown Page")
        
        mock_error.assert_called_once_with("Unknown page: Unknown Page")
    
    @patch('streamlit.set_page_config')
    @patch('streamlit.sidebar')
    @patch('streamlit.title')
    @patch('streamlit.radio')
    def test_setup_navigation_function(self, mock_radio, mock_title, mock_sidebar, mock_set_page_config):
        """Test setup_navigation function"""
        import app
        
        # Mock the return value of radio
        mock_radio.return_value = "Framework Overview"
        
        # Mock the sidebar context manager
        mock_sidebar.return_value.__enter__ = MagicMock()
        mock_sidebar.return_value.__exit__ = MagicMock()
        
        result = app.setup_navigation()
        
        # Verify set_page_config was called with correct parameters
        mock_set_page_config.assert_called_once_with(
            page_title=app.AppConfig.PAGE_TITLE,
            page_icon=app.AppConfig.PAGE_ICON,
            layout=app.AppConfig.LAYOUT,
            initial_sidebar_state=app.AppConfig.INITIAL_SIDEBAR_STATE
        )
        
        # Verify navigation was set up
        assert result == "Framework Overview"
    
    @patch('streamlit.set_page_config')
    @patch('streamlit.sidebar')
    @patch('streamlit.title')
    @patch('streamlit.radio')
    @patch('streamlit.info')
    def test_main_function_integration(self, mock_info, mock_radio, mock_title, mock_sidebar, mock_set_page_config):
        """Test main function integration"""
        import app
        
        # Mock the return value of radio
        mock_radio.return_value = "Framework Overview"
        
        # Mock the sidebar context manager
        mock_sidebar.return_value.__enter__ = MagicMock()
        mock_sidebar.return_value.__exit__ = MagicMock()
        
        # Call main function
        app.main()
        
        # Verify the workflow: setup_navigation was called, then route_to_page
        mock_set_page_config.assert_called_once()
        mock_info.assert_called_once()


class TestAppConfigCoverage:
    """Test cases to improve coverage for AppConfig class"""
    
    def test_app_config_attributes(self):
        """Test that AppConfig has all required attributes"""
        import app
        
        # Test all attributes are accessible
        assert hasattr(app.AppConfig, 'FRAMEWORK_PATH')
        assert hasattr(app.AppConfig, 'PAGE_TITLE')
        assert hasattr(app.AppConfig, 'PAGE_ICON')
        assert hasattr(app.AppConfig, 'LAYOUT')
        assert hasattr(app.AppConfig, 'INITIAL_SIDEBAR_STATE')
        assert hasattr(app.AppConfig, 'NAVIGATION_PAGES')
        
        # Test attribute values are correct
        assert app.AppConfig.PAGE_TITLE == "Claude Code Framework Dashboard"
        assert app.AppConfig.PAGE_ICON == "🧠"
        assert app.AppConfig.LAYOUT == "wide"
        assert app.AppConfig.INITIAL_SIDEBAR_STATE == "expanded"
        assert len(app.AppConfig.NAVIGATION_PAGES) == 7
        
        # Test FRAMEWORK_PATH is a Path object
        assert isinstance(app.AppConfig.FRAMEWORK_PATH, Path)
    
    def test_navigation_pages_content(self):
        """Test navigation pages list content"""
        import app
        
        expected_pages = [
            "Framework Overview",
            "Command Explorer", 
            "Module Visualizer",
            "Prompt Constructor",
            "Quality Gates",
            "Routing Simulator",
            "Meta Framework"
        ]
        
        assert app.AppConfig.NAVIGATION_PAGES == expected_pages