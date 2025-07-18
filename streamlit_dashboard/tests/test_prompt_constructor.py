"""
Tests for Prompt Constructor Component
Following TDD approach - writing tests first
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import sys
import streamlit as st
import json

# Add the streamlit_dashboard directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the component we're going to build
from components.prompt_constructor import PromptConstructor


class TestPromptConstructor:
    """Test suite for Prompt Constructor component"""
    
    @pytest.fixture
    def mock_framework_path(self, tmp_path):
        """Create a mock framework directory structure with sample modules"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create mock directory structure
        modules_dir = framework_dir / "modules"
        modules_dir.mkdir()
        patterns_dir = modules_dir / "patterns"
        patterns_dir.mkdir()
        
        # Create some mock module files
        tdd_content = """
# TDD Cycle Pattern

## Purpose
Enforce Test-Driven Development

## Steps
1. Write failing test
2. Write minimal code
3. Refactor

## Validation
- Tests must exist
- Coverage > 90%
"""
        (patterns_dir / "tdd-cycle-pattern.md").write_text(tdd_content)
        
        routing_content = """
# Intelligent Routing

## Purpose
Route requests to appropriate commands

## Decision Tree
- Simple task -> /task
- Complex -> /feature
- Unknown -> /auto
"""
        (patterns_dir / "intelligent-routing.md").write_text(routing_content)
        
        return framework_dir
    
    @pytest.fixture
    def prompt_constructor(self, mock_framework_path):
        """Create PromptConstructor instance with mock path"""
        return PromptConstructor(framework_path=mock_framework_path)
    
    def test_initialization(self, prompt_constructor, mock_framework_path):
        """Test that PromptConstructor initializes correctly"""
        assert prompt_constructor.framework_path == mock_framework_path
        assert hasattr(prompt_constructor, 'available_modules')
        assert hasattr(prompt_constructor, 'selected_modules')
        assert hasattr(prompt_constructor, 'constructed_prompt')
    
    def test_load_available_modules(self, prompt_constructor):
        """Test loading available modules from framework"""
        modules = prompt_constructor.load_available_modules()
        
        assert isinstance(modules, dict)
        assert 'patterns' in modules
        assert len(modules['patterns']) >= 2
        assert any('tdd-cycle-pattern' in m for m in modules['patterns'])
        assert any('intelligent-routing' in m for m in modules['patterns'])
    
    def test_parse_module_content(self, prompt_constructor):
        """Test parsing module content"""
        module_path = prompt_constructor.framework_path / "modules" / "patterns" / "tdd-cycle-pattern.md"
        content = prompt_constructor.parse_module_content(module_path)
        
        assert isinstance(content, dict)
        assert 'name' in content
        assert 'purpose' in content
        assert 'content' in content
        assert 'sections' in content
        assert content['name'] == 'tdd-cycle-pattern'
        assert 'TDD' in content['purpose'] or 'Test' in content['purpose']
    
    def test_add_module_to_prompt(self, prompt_constructor):
        """Test adding module to prompt construction"""
        modules = prompt_constructor.load_available_modules()
        first_module = modules['patterns'][0]
        
        success = prompt_constructor.add_module_to_prompt('patterns', first_module)
        
        assert success is True
        assert len(prompt_constructor.selected_modules) == 1
        assert prompt_constructor.selected_modules[0]['category'] == 'patterns'
    
    def test_remove_module_from_prompt(self, prompt_constructor):
        """Test removing module from prompt"""
        # First add a module
        modules = prompt_constructor.load_available_modules()
        first_module = modules['patterns'][0]
        prompt_constructor.add_module_to_prompt('patterns', first_module)
        
        # Then remove it
        success = prompt_constructor.remove_module_from_prompt(0)
        
        assert success is True
        assert len(prompt_constructor.selected_modules) == 0
    
    def test_reorder_modules(self, prompt_constructor):
        """Test reordering modules in prompt"""
        # Add two modules
        modules = prompt_constructor.load_available_modules()
        prompt_constructor.add_module_to_prompt('patterns', modules['patterns'][0])
        prompt_constructor.add_module_to_prompt('patterns', modules['patterns'][1])
        
        # Reorder them
        success = prompt_constructor.reorder_modules(0, 1)
        
        assert success is True
        assert prompt_constructor.selected_modules[0]['name'] == modules['patterns'][1]
        assert prompt_constructor.selected_modules[1]['name'] == modules['patterns'][0]
    
    def test_construct_prompt(self, prompt_constructor):
        """Test constructing the final prompt"""
        # Add modules
        modules = prompt_constructor.load_available_modules()
        prompt_constructor.add_module_to_prompt('patterns', modules['patterns'][0])
        
        # Add custom instructions
        custom_instructions = "Focus on code quality and testing"
        
        prompt = prompt_constructor.construct_prompt(
            custom_instructions=custom_instructions,
            include_metadata=True
        )
        
        assert isinstance(prompt, str)
        assert custom_instructions in prompt
        assert 'tdd-cycle-pattern' in prompt.lower() or 'TDD' in prompt
        assert len(prompt) > 100  # Should be substantial
    
    def test_validate_prompt(self, prompt_constructor):
        """Test prompt validation"""
        # Create a valid prompt
        modules = prompt_constructor.load_available_modules()
        prompt_constructor.add_module_to_prompt('patterns', modules['patterns'][0])
        prompt = prompt_constructor.construct_prompt()
        
        validation = prompt_constructor.validate_prompt(prompt)
        
        assert isinstance(validation, dict)
        assert 'is_valid' in validation
        assert 'token_count' in validation
        assert 'warnings' in validation
        assert 'errors' in validation
        assert validation['is_valid'] is True
    
    def test_export_prompt_template(self, prompt_constructor, tmp_path):
        """Test exporting prompt as template"""
        # Build a prompt
        modules = prompt_constructor.load_available_modules()
        prompt_constructor.add_module_to_prompt('patterns', modules['patterns'][0])
        
        template_path = tmp_path / "my_template.json"
        success = prompt_constructor.export_prompt_template(
            template_path,
            name="Test Template",
            description="A test template"
        )
        
        assert success is True
        assert template_path.exists()
        
        # Verify template content
        with open(template_path) as f:
            template = json.load(f)
        
        assert template['name'] == "Test Template"
        assert template['description'] == "A test template"
        assert 'modules' in template
        assert len(template['modules']) == 1
    
    def test_import_prompt_template(self, prompt_constructor, tmp_path):
        """Test importing prompt template"""
        # Create a template file
        template = {
            "name": "Import Test",
            "description": "Testing import",
            "modules": [
                {"category": "patterns", "name": "tdd-cycle-pattern.md"}
            ],
            "custom_instructions": "Test instructions"
        }
        
        template_path = tmp_path / "import_test.json"
        with open(template_path, 'w') as f:
            json.dump(template, f)
        
        # Import it
        success = prompt_constructor.import_prompt_template(template_path)
        
        assert success is True
        assert len(prompt_constructor.selected_modules) == 1
        assert prompt_constructor.selected_modules[0]['category'] == 'patterns'
    
    @patch('streamlit.columns')
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    def test_render_module_selector(self, mock_button, mock_selectbox, mock_columns, prompt_constructor):
        """Test rendering module selector UI"""
        mock_col1, mock_col2 = Mock(), Mock()
        mock_columns.return_value = [mock_col1, mock_col2]
        
        # Setup column context managers
        for col in [mock_col1, mock_col2]:
            col.__enter__ = Mock(return_value=None)
            col.__exit__ = Mock(return_value=None)
        
        mock_selectbox.side_effect = ['patterns', 'tdd-cycle-pattern.md']
        mock_button.return_value = True
        
        prompt_constructor.render_module_selector()
        
        # Verify UI elements were created
        assert mock_columns.called
        assert mock_selectbox.call_count >= 2
        assert mock_button.called
    
    @patch('streamlit.text_area')
    @patch('streamlit.code')
    def test_render_prompt_preview(self, mock_code, mock_text_area, prompt_constructor):
        """Test rendering prompt preview"""
        # Add a module first
        modules = prompt_constructor.load_available_modules()
        prompt_constructor.add_module_to_prompt('patterns', modules['patterns'][0])
        
        prompt_constructor.render_prompt_preview()
        
        # Verify preview was rendered
        mock_code.assert_called_once()
        assert len(mock_code.call_args[0][0]) > 0  # Should have content
    
    def test_estimate_token_count(self, prompt_constructor):
        """Test token count estimation"""
        text = "This is a test prompt with some content."
        count = prompt_constructor.estimate_token_count(text)
        
        assert isinstance(count, int)
        assert count > 0
        assert count < 50  # Reasonable for short text
    
    def test_get_module_dependencies(self, prompt_constructor):
        """Test getting module dependencies"""
        module_path = prompt_constructor.framework_path / "modules" / "patterns" / "tdd-cycle-pattern.md"
        deps = prompt_constructor.get_module_dependencies(module_path)
        
        assert isinstance(deps, list)
        # May or may not have dependencies, but should return a list
    
    @patch('streamlit.tabs')
    def test_render_method(self, mock_tabs, prompt_constructor):
        """Test main render method"""
        # Mock tabs
        mock_tab1, mock_tab2, mock_tab3 = Mock(), Mock(), Mock()
        mock_tabs.return_value = [mock_tab1, mock_tab2, mock_tab3]
        
        # Setup tab context managers
        for tab in [mock_tab1, mock_tab2, mock_tab3]:
            tab.__enter__ = Mock(return_value=None)
            tab.__exit__ = Mock(return_value=None)
        
        prompt_constructor.render()
        
        # Verify tabs were created
        mock_tabs.assert_called_once_with(["🔨 Constructor", "📚 Templates", "🔍 Preview"])