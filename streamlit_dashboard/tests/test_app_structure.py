"""
TDD RED: Tests for Streamlit app structure
These tests define the expected behavior of the main application structure
"""

import pytest
import sys
import os
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestAppStructure:
    """Test cases for main application structure and initialization"""
    
    def test_app_module_exists(self):
        """Test that the main app module exists"""
        app_path = Path(__file__).parent.parent / "app.py"
        assert app_path.exists(), "app.py file should exist"
    
    def test_app_has_main_function(self):
        """Test that app.py has a main function"""
        import app
        assert hasattr(app, 'main'), "app.py should have a main() function"
        assert callable(app.main), "main should be a callable function"
    
    def test_app_has_config_class(self):
        """Test that app has a configuration class"""
        import app
        assert hasattr(app, 'AppConfig'), "app.py should have AppConfig class"
        assert hasattr(app.AppConfig, 'FRAMEWORK_PATH'), "AppConfig should have FRAMEWORK_PATH"
        assert hasattr(app.AppConfig, 'PAGE_TITLE'), "AppConfig should have PAGE_TITLE"
        assert hasattr(app.AppConfig, 'PAGE_ICON'), "AppConfig should have PAGE_ICON"
    
    def test_app_has_navigation_setup(self):
        """Test that app has navigation setup function"""
        import app
        assert hasattr(app, 'setup_navigation'), "app.py should have setup_navigation()"
        assert callable(app.setup_navigation), "setup_navigation should be callable"
    
    def test_app_has_page_routing(self):
        """Test that app has page routing function"""
        import app
        assert hasattr(app, 'route_to_page'), "app.py should have route_to_page()"
        assert callable(app.route_to_page), "route_to_page should be callable"
    
    def test_app_follows_separation_of_concerns(self):
        """Test that app.py follows single responsibility principle"""
        import app
        import inspect
        
        # Get all functions and classes in app module
        members = inspect.getmembers(app)
        functions = [name for name, obj in members if inspect.isfunction(obj)]
        classes = [name for name, obj in members if inspect.isclass(obj)]
        
        # App should have limited responsibility - configuration and routing only
        expected_functions = ['main', 'setup_navigation', 'route_to_page']
        expected_classes = ['AppConfig']
        
        # Check that we don't have excessive functions (separation of concerns)
        assert len(functions) <= 5, f"App should have ≤5 functions, found {len(functions)}: {functions}"
        assert len(classes) <= 2, f"App should have ≤2 classes, found {len(classes)}: {classes}"
        
        # Check that essential functions exist
        for func in expected_functions:
            assert func in functions, f"Missing required function: {func}"
        
        for cls in expected_classes:
            assert cls in classes, f"Missing required class: {cls}"
    
    def test_app_imports_are_minimal(self):
        """Test that app.py has minimal imports (no business logic dependencies)"""
        import app
        import inspect
        
        # Read the source file to check imports
        app_path = Path(__file__).parent.parent / "app.py"
        with open(app_path, 'r') as f:
            source = f.read()
        
        # Should import streamlit and navigation/routing utilities
        assert "import streamlit" in source, "Should import streamlit"
        
        # Should NOT import business logic modules directly
        forbidden_imports = [
            "from data.framework_parser import",
            "from data.command_analyzer import", 
            "from data.module_inspector import",
            "from components.framework_overview import",
            "from components.command_explorer import"
        ]
        
        for forbidden in forbidden_imports:
            assert forbidden not in source, f"App should not directly import: {forbidden}"
    
    def test_app_file_size_constraint(self):
        """Test that app.py is under 500 lines (no god objects)"""
        app_path = Path(__file__).parent.parent / "app.py"
        with open(app_path, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines and comments for more accurate count
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        assert len(code_lines) < 500, f"app.py should be <500 lines of code, found {len(code_lines)}"


class TestComponentStructure:
    """Test cases for component directory structure"""
    
    def test_components_directory_exists(self):
        """Test that components directory exists with proper structure"""
        components_path = Path(__file__).parent.parent / "components"
        assert components_path.exists(), "components directory should exist"
        assert components_path.is_dir(), "components should be a directory"
    
    def test_components_init_file_exists(self):
        """Test that components has __init__.py file"""
        init_path = Path(__file__).parent.parent / "components" / "__init__.py"
        assert init_path.exists(), "components/__init__.py should exist"
    
    def test_data_directory_exists(self):
        """Test that data directory exists with proper structure"""
        data_path = Path(__file__).parent.parent / "data"
        assert data_path.exists(), "data directory should exist"
        assert data_path.is_dir(), "data should be a directory"
    
    def test_data_init_file_exists(self):
        """Test that data has __init__.py file"""
        init_path = Path(__file__).parent.parent / "data" / "__init__.py"
        assert init_path.exists(), "data/__init__.py should exist"
    
    def test_utils_directory_exists(self):
        """Test that utils directory exists with proper structure"""
        utils_path = Path(__file__).parent.parent / "utils"
        assert utils_path.exists(), "utils directory should exist"
        assert utils_path.is_dir(), "utils should be a directory"
    
    def test_utils_init_file_exists(self):
        """Test that utils has __init__.py file"""
        init_path = Path(__file__).parent.parent / "utils" / "__init__.py"
        assert init_path.exists(), "utils/__init__.py should exist"


class TestProjectConfiguration:
    """Test cases for project configuration and setup"""
    
    def test_requirements_file_exists(self):
        """Test that requirements.txt exists with necessary dependencies"""
        req_path = Path(__file__).parent.parent / "requirements.txt"
        assert req_path.exists(), "requirements.txt should exist"
        
        with open(req_path, 'r') as f:
            requirements = f.read()
        
        essential_deps = [
            "streamlit>=1.28.0",
            "plotly>=5.15.0", 
            "networkx>=3.1",
            "pandas>=2.0.0",
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0"
        ]
        
        for dep in essential_deps:
            assert dep in requirements, f"Missing dependency: {dep}"
    
    def test_tests_directory_exists(self):
        """Test that tests directory exists with proper structure"""
        tests_path = Path(__file__).parent
        assert tests_path.exists(), "tests directory should exist"
        assert tests_path.is_dir(), "tests should be a directory"
    
    def test_assets_directory_exists(self):
        """Test that assets directory exists"""
        assets_path = Path(__file__).parent.parent / "assets"
        assert assets_path.exists(), "assets directory should exist"
        assert assets_path.is_dir(), "assets should be a directory"