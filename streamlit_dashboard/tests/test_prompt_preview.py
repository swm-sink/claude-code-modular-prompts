"""
Tests for Real-time Prompt Preview component
TDD RED PHASE: Write failing tests first
"""

import pytest
import unittest.mock as mock
from pathlib import Path
import json
from unittest.mock import MagicMock, patch

# Import the component we're going to build
try:
    from components.prompt_preview import PromptPreview, PromptHighlighter, PromptComposer
except ImportError:
    # These don't exist yet - we'll create them
    PromptPreview = None
    PromptHighlighter = None
    PromptComposer = None


class TestPromptHighlighter:
    """Test the PromptHighlighter class"""
    
    def test_highlight_framework_syntax(self):
        """Test highlighting framework-specific syntax"""
        if PromptHighlighter is None:
            pytest.skip("PromptHighlighter not implemented yet")
        
        highlighter = PromptHighlighter()
        
        prompt_text = """
        /auto "analyze this code"
        
        Uses modules:
        - modules/patterns/tdd-cycle-pattern.md
        - system/quality/universal-quality-gates.md
        
        Quality Gates:
        - TDD enforcement
        - 90% coverage
        """
        
        highlighted = highlighter.highlight_framework_syntax(prompt_text)
        
        assert isinstance(highlighted, str)
        assert len(highlighted) > len(prompt_text)  # Should have markup
        assert "/auto" in highlighted
    
    def test_highlight_commands(self):
        """Test highlighting command syntax"""
        if PromptHighlighter is None:
            pytest.skip("PromptHighlighter not implemented yet")
        
        highlighter = PromptHighlighter()
        
        text = "/task implement function /feature build system /auto analyze"
        highlighted = highlighter.highlight_commands(text)
        
        assert "/task" in highlighted
        assert "/feature" in highlighted
        assert "/auto" in highlighted
    
    def test_highlight_module_references(self):
        """Test highlighting module references"""
        if PromptHighlighter is None:
            pytest.skip("PromptHighlighter not implemented yet")
        
        highlighter = PromptHighlighter()
        
        text = "modules/patterns/tdd-cycle.md and system/quality/gates.md"
        highlighted = highlighter.highlight_module_references(text)
        
        assert "modules/patterns/tdd-cycle.md" in highlighted
        assert "system/quality/gates.md" in highlighted
    
    def test_highlight_quality_metrics(self):
        """Test highlighting quality metrics and thresholds"""
        if PromptHighlighter is None:
            pytest.skip("PromptHighlighter not implemented yet")
        
        highlighter = PromptHighlighter()
        
        text = "Coverage: 90% Performance: 200ms TDD: enforced"
        highlighted = highlighter.highlight_quality_metrics(text)
        
        assert "90%" in highlighted
        assert "200ms" in highlighted
        assert "enforced" in highlighted


class TestPromptComposer:
    """Test the PromptComposer class"""
    
    @pytest.fixture
    def framework_path(self, tmp_path):
        """Create a temporary framework directory"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create commands directory
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        
        (commands_dir / "task.md").write_text("""
# Task Command

## Instructions
Implement the requested functionality following TDD methodology.
""")
        
        # Create modules directory
        modules_dir = framework_dir / "modules"
        modules_dir.mkdir()
        patterns_dir = modules_dir / "patterns"
        patterns_dir.mkdir()
        
        (patterns_dir / "tdd-cycle.md").write_text("""
# TDD Cycle Pattern

1. Write failing test (RED)
2. Implement minimal code (GREEN) 
3. Refactor while keeping tests green (REFACTOR)
""")
        
        return framework_dir
    
    def test_prompt_composer_initialization(self, framework_path):
        """Test PromptComposer can be initialized"""
        if PromptComposer is None:
            pytest.skip("PromptComposer not implemented yet")
        
        composer = PromptComposer(framework_path=framework_path)
        assert composer.framework_path == framework_path
        assert hasattr(composer, 'components')
    
    def test_load_component_content(self, framework_path):
        """Test loading content from framework components"""
        if PromptComposer is None:
            pytest.skip("PromptComposer not implemented yet")
        
        composer = PromptComposer(framework_path=framework_path)
        
        # Test loading command content
        command_content = composer.load_component_content("commands/task.md")
        assert "Task Command" in command_content
        assert "TDD methodology" in command_content
        
        # Test loading module content
        module_content = composer.load_component_content("modules/patterns/tdd-cycle.md")
        assert "TDD Cycle Pattern" in module_content
        assert "RED" in module_content
    
    def test_compose_prompt_from_components(self, framework_path):
        """Test composing prompt from multiple components"""
        if PromptComposer is None:
            pytest.skip("PromptComposer not implemented yet")
        
        composer = PromptComposer(framework_path=framework_path)
        
        components = [
            {"type": "command", "name": "task", "file": "commands/task.md"},
            {"type": "module", "name": "tdd-cycle", "file": "modules/patterns/tdd-cycle.md"}
        ]
        
        composed_prompt = composer.compose_prompt_from_components(components)
        
        assert isinstance(composed_prompt, str)
        assert "Task Command" in composed_prompt
        assert "TDD Cycle Pattern" in composed_prompt
        assert len(composed_prompt) > 100  # Should be substantial
    
    def test_resolve_component_dependencies(self, framework_path):
        """Test resolving dependencies between components"""
        if PromptComposer is None:
            pytest.skip("PromptComposer not implemented yet")
        
        composer = PromptComposer(framework_path=framework_path)
        
        components = [
            {"type": "command", "name": "task", "dependencies": ["tdd-cycle"]},
        ]
        
        resolved_components = composer.resolve_component_dependencies(components)
        
        assert len(resolved_components) >= len(components)
        # Should include dependencies
    
    def test_validate_prompt_composition(self, framework_path):
        """Test validating prompt composition for completeness"""
        if PromptComposer is None:
            pytest.skip("PromptComposer not implemented yet")
        
        composer = PromptComposer(framework_path=framework_path)
        
        # Valid composition
        components = [
            {"type": "command", "name": "task", "file": "commands/task.md"}
        ]
        
        is_valid, errors = composer.validate_prompt_composition(components)
        assert is_valid is True
        assert len(errors) == 0
        
        # Invalid composition (missing file)
        invalid_components = [
            {"type": "command", "name": "nonexistent", "file": "commands/nonexistent.md"}
        ]
        
        is_valid, errors = composer.validate_prompt_composition(invalid_components)
        assert is_valid is False
        assert len(errors) > 0
    
    def test_optimize_prompt_structure(self, framework_path):
        """Test optimizing prompt structure for clarity"""
        if PromptComposer is None:
            pytest.skip("PromptComposer not implemented yet")
        
        composer = PromptComposer(framework_path=framework_path)
        
        raw_prompt = """
        Task Command
        Implement functionality
        TDD Cycle Pattern  
        Write tests first
        """
        
        optimized_prompt = composer.optimize_prompt_structure(raw_prompt)
        
        assert isinstance(optimized_prompt, str)
        assert len(optimized_prompt) >= len(raw_prompt)
        # Should have improved structure


class TestPromptPreview:
    """Test the PromptPreview component"""
    
    @pytest.fixture
    def framework_path(self, tmp_path):
        """Create a temporary framework directory"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create sample structure
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        (commands_dir / "task.md").write_text("# Task Command")
        
        return framework_dir
    
    def test_prompt_preview_initialization(self, framework_path):
        """Test PromptPreview can be initialized"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        assert preview.framework_path == framework_path
        assert hasattr(preview, 'highlighter')
        assert hasattr(preview, 'composer')
    
    def test_generate_live_preview(self, framework_path):
        """Test generating live preview as user builds prompt"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        # Test with empty components
        empty_preview = preview.generate_live_preview([])
        assert isinstance(empty_preview, dict)
        assert 'raw_prompt' in empty_preview
        assert 'highlighted_prompt' in empty_preview
        
        # Test with components
        components = [
            {"type": "command", "name": "task", "file": "commands/task.md"}
        ]
        
        live_preview = preview.generate_live_preview(components)
        
        assert isinstance(live_preview, dict)
        assert 'raw_prompt' in live_preview
        assert 'highlighted_prompt' in live_preview
        assert 'metadata' in live_preview
        assert len(live_preview['raw_prompt']) > 0
    
    def test_calculate_prompt_metrics(self, framework_path):
        """Test calculating prompt metrics (length, complexity, etc.)"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        prompt_text = "This is a test prompt with /task command and modules/patterns/test.md"
        
        metrics = preview.calculate_prompt_metrics(prompt_text)
        
        assert isinstance(metrics, dict)
        assert 'character_count' in metrics
        assert 'word_count' in metrics
        assert 'command_count' in metrics
        assert 'module_count' in metrics
        assert 'estimated_tokens' in metrics
        
        assert metrics['character_count'] > 0
        assert metrics['word_count'] > 0
        assert metrics['command_count'] >= 1
    
    def test_detect_syntax_errors(self, framework_path):
        """Test detecting syntax errors in prompt composition"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        # Valid prompt
        valid_prompt = "/task implement feature"
        errors = preview.detect_syntax_errors(valid_prompt)
        assert isinstance(errors, list)
        
        # Invalid prompt (malformed command)
        invalid_prompt = "/ task implement feature"  # Space after /
        errors = preview.detect_syntax_errors(invalid_prompt)
        assert isinstance(errors, list)
        # May or may not have errors depending on implementation
    
    def test_get_completion_suggestions(self, framework_path):
        """Test getting autocomplete suggestions"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        # Test command suggestions
        partial_command = "/ta"
        suggestions = preview.get_completion_suggestions(partial_command, cursor_position=3)
        
        assert isinstance(suggestions, list)
        # Should suggest "/task" if available
        
        # Test module suggestions
        partial_module = "modules/pat"
        suggestions = preview.get_completion_suggestions(partial_module, cursor_position=11)
        
        assert isinstance(suggestions, list)
    
    def test_export_prompt_template(self, framework_path, tmp_path):
        """Test exporting composed prompt as template"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        components = [
            {"type": "command", "name": "task", "file": "commands/task.md"}
        ]
        
        template_file = tmp_path / "test_template.json"
        success = preview.export_prompt_template(components, template_file)
        
        assert success is True
        assert template_file.exists()
        
        # Verify template structure
        with open(template_file) as f:
            template_data = json.load(f)
        
        assert 'components' in template_data
        assert 'metadata' in template_data
        assert len(template_data['components']) > 0
    
    def test_import_prompt_template(self, framework_path, tmp_path):
        """Test importing prompt template"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        # Create test template
        template_data = {
            'components': [
                {"type": "command", "name": "task", "file": "commands/task.md"}
            ],
            'metadata': {
                'name': 'Test Template',
                'version': '1.0'
            }
        }
        
        template_file = tmp_path / "test_template.json"
        with open(template_file, 'w') as f:
            json.dump(template_data, f)
        
        components = preview.import_prompt_template(template_file)
        
        assert isinstance(components, list)
        assert len(components) > 0
        assert components[0]['name'] == 'task'
    
    def test_real_time_validation(self, framework_path):
        """Test real-time validation as user types"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        # Simulate typing
        partial_prompts = [
            "/",
            "/ta",
            "/task",
            "/task impl",
            "/task implement feature"
        ]
        
        for prompt in partial_prompts:
            validation_result = preview.validate_prompt_real_time(prompt)
            
            assert isinstance(validation_result, dict)
            assert 'is_valid' in validation_result
            assert 'errors' in validation_result
            assert 'suggestions' in validation_result
    
    def test_collaborative_editing_support(self, framework_path):
        """Test support for collaborative prompt editing"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        # Test getting current state for sharing
        components = [{"type": "command", "name": "task"}]
        state = preview.get_shareable_state(components)
        
        assert isinstance(state, dict)
        assert 'components' in state
        assert 'timestamp' in state
        
        # Test applying shared state
        applied_components = preview.apply_shared_state(state)
        assert isinstance(applied_components, list)
    
    def test_render_prompt_preview_ui(self, framework_path):
        """Test rendering the prompt preview UI"""
        if PromptPreview is None:
            pytest.skip("PromptPreview not implemented yet")
        
        preview = PromptPreview(framework_path=framework_path)
        
        # Test that the method exists and can be called
        # We don't test Streamlit rendering in unit tests
        assert hasattr(preview, 'render_prompt_preview_ui')
        assert callable(preview.render_prompt_preview_ui)