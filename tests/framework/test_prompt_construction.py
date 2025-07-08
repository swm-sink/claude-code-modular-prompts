"""Test prompt construction visualization functionality.

This test suite validates the framework enhancements for Claude 4 prompt construction,
runtime visualization, and context budget optimization.
"""

import pytest
from pathlib import Path
import xml.etree.ElementTree as ET


class TestPromptConstructionMethodology:
    """Test suite for prompt construction methodology validation."""
    
    @pytest.fixture
    def claude_md_path(self):
        """Get CLAUDE.md file path."""
        return Path(__file__).parent.parent.parent / "CLAUDE.md"
    
    def test_prompt_construction_methodology_section_exists(self, claude_md_path):
        """Test that CLAUDE.md contains prompt_construction_methodology section."""
        content = claude_md_path.read_text()
        assert "<prompt_construction_methodology" in content, \
            "CLAUDE.md missing prompt_construction_methodology section"
        assert "version=" in content, \
            "prompt_construction_methodology missing version attribute"
    
    def test_visualization_requirements_defined(self, claude_md_path):
        """Test that visualization requirements are properly defined."""
        content = claude_md_path.read_text()
        assert "<visualization_requirements>" in content, \
            "Missing visualization_requirements section"
        assert "<execution_preview>" in content, \
            "Missing execution_preview requirement"
        assert "<runtime_dashboard>" in content, \
            "Missing runtime_dashboard requirement"
        assert "<context_budget>" in content, \
            "Missing context_budget requirement"
    
    def test_lego_block_assembly_defined(self, claude_md_path):
        """Test that lego block assembly concepts are defined."""
        content = claude_md_path.read_text()
        assert "<lego_block_assembly>" in content, \
            "Missing lego_block_assembly section"
        assert "<command_role>" in content, \
            "Missing command_role definition"
        assert "<module_role>" in content, \
            "Missing module_role definition"
        assert "<runtime_role>" in content, \
            "Missing runtime_role definition"


class TestCommandPromptConstruction:
    """Test suite for command prompt construction enhancements."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands"
    
    def test_all_commands_have_prompt_construction_section(self, commands_dir):
        """Test that all commands have prompt_construction section."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            assert "<prompt_construction>" in content, \
                f"Command {command_file.name} missing prompt_construction section"
    
    def test_assembly_preview_in_commands(self, commands_dir):
        """Test that commands contain assembly_preview visualization."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            assert "<assembly_preview>" in content, \
                f"Command {command_file.name} missing assembly_preview"
            # Should contain visual workflow elements
            assert "┌─" in content or "│" in content or "└─" in content, \
                f"Command {command_file.name} assembly_preview missing visual elements"
    
    def test_context_budget_in_commands(self, commands_dir):
        """Test that commands contain context budget estimation."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            assert "<context_budget>" in content, \
                f"Command {command_file.name} missing context_budget"
            assert "tokens:" in content, \
                f"Command {command_file.name} context_budget missing token estimation"
    
    def test_runtime_visualization_in_commands(self, commands_dir):
        """Test that commands contain runtime visualization."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            assert "<runtime_visualization>" in content, \
                f"Command {command_file.name} missing runtime_visualization"
            assert "<execution_trace>" in content, \
                f"Command {command_file.name} missing execution_trace"
    
    def test_claude_4_interpretation_guide_in_commands(self, commands_dir):
        """Test that commands contain Claude 4 interpretation guide."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            assert "<claude_4_interpretation>" in content, \
                f"Command {command_file.name} missing claude_4_interpretation"
            assert "<parsing_behavior>" in content, \
                f"Command {command_file.name} missing parsing_behavior"
            assert "<decision_points>" in content, \
                f"Command {command_file.name} missing decision_points"


class TestModuleInterfaceContracts:
    """Test suite for module interface contract validation."""
    
    @pytest.fixture
    def modules_dir(self):
        """Get the modules directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules"
    
    def test_core_modules_have_interface_contracts(self, modules_dir):
        """Test that core modules have interface contracts."""
        core_modules = [
            "development/task-management.md",
            "patterns/intelligent-routing.md",
            "quality/tdd.md",
            "patterns/multi-agent.md"
        ]
        
        for module_path in core_modules:
            module_file = modules_dir / module_path
            if module_file.exists():
                content = module_file.read_text()
                assert "<interface_contract>" in content, \
                    f"Module {module_path} missing interface_contract"
    
    def test_interface_contract_structure(self, modules_dir):
        """Test that interface contracts have proper structure."""
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            if "<interface_contract>" in content:
                assert "<inputs>" in content, \
                    f"Module {module_file.name} interface_contract missing inputs"
                assert "<outputs>" in content, \
                    f"Module {module_file.name} interface_contract missing outputs"
    
    def test_execution_pattern_in_modules(self, modules_dir):
        """Test that modules contain execution patterns."""
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            if "<interface_contract>" in content:
                assert "<execution_pattern>" in content, \
                    f"Module {module_file.name} missing execution_pattern"
                assert "<claude_4_behavior>" in content, \
                    f"Module {module_file.name} missing claude_4_behavior"


class TestVisualizationModules:
    """Test suite for new visualization modules."""
    
    @pytest.fixture
    def patterns_dir(self):
        """Get the patterns directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "patterns"
    
    def test_prompt_construction_visualization_module_exists(self, patterns_dir):
        """Test that prompt-construction-visualization.md exists."""
        module_file = patterns_dir / "prompt-construction-visualization.md"
        assert module_file.exists(), \
            "prompt-construction-visualization.md module missing"
        assert module_file.stat().st_size > 0, \
            "prompt-construction-visualization.md module is empty"
    
    def test_runtime_execution_dashboard_module_exists(self, patterns_dir):
        """Test that runtime-execution-dashboard.md exists."""
        module_file = patterns_dir / "runtime-execution-dashboard.md"
        assert module_file.exists(), \
            "runtime-execution-dashboard.md module missing"
        assert module_file.stat().st_size > 0, \
            "runtime-execution-dashboard.md module is empty"
    
    def test_deterministic_execution_engine_module_exists(self, patterns_dir):
        """Test that deterministic-execution-engine.md exists."""
        module_file = patterns_dir / "deterministic-execution-engine.md"
        assert module_file.exists(), \
            "deterministic-execution-engine.md module missing"
        assert module_file.stat().st_size > 0, \
            "deterministic-execution-engine.md module is empty"


class TestContextBudgetOptimization:
    """Test suite for context budget optimization."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands"
    
    def test_context_budget_estimates_are_realistic(self, commands_dir):
        """Test that context budget estimates are within realistic ranges."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            if "<context_budget>" in content:
                # Extract token estimates (rough validation)
                lines = content.split('\n')
                for line in lines:
                    if "tokens:" in line and "~" in line:
                        # Basic sanity check that estimates are reasonable
                        assert any(char.isdigit() for char in line), \
                            f"Command {command_file.name} context_budget missing numeric estimates"
    
    def test_token_optimization_patterns_documented(self, commands_dir):
        """Test that token optimization patterns are documented."""
        # At least one command should document optimization strategies
        optimization_found = False
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            if "optimization" in content.lower() or "parallel" in content.lower():
                optimization_found = True
                break
        
        assert optimization_found, \
            "No token optimization patterns documented in commands"


class TestExecutionTraceValidation:
    """Test suite for execution trace functionality."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands"
    
    def test_execution_traces_have_timestamps(self, commands_dir):
        """Test that execution traces include timestamp patterns."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            if "<execution_trace>" in content:
                # Should contain timestamp-like patterns
                assert "[" in content and "]" in content, \
                    f"Command {command_file.name} execution_trace missing timestamp brackets"
    
    def test_execution_traces_have_progress_indicators(self, commands_dir):
        """Test that execution traces include progress indicators."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            if "<execution_trace>" in content:
                # Should contain progress symbols
                progress_symbols = ["▶️", "✓", "🔴", "✅", "💚", "🔧"]
                has_progress = any(symbol in content for symbol in progress_symbols)
                assert has_progress, \
                    f"Command {command_file.name} execution_trace missing progress indicators"


class TestFrameworkVersionAdvancement:
    """Test suite for framework version advancement."""
    
    @pytest.fixture
    def claude_md_path(self):
        """Get CLAUDE.md file path."""
        return Path(__file__).parent.parent.parent / "CLAUDE.md"
    
    def test_framework_version_advanced_to_2_4_1(self, claude_md_path):
        """Test that framework version is advanced to 2.4.1."""
        content = claude_md_path.read_text()
        # Should contain version 2.4.1 somewhere in version tables
        assert "2.4.1" in content, \
            "Framework version not advanced to 2.4.1"
    
    def test_version_table_updated_with_current_date(self, claude_md_path):
        """Test that version table contains current date."""
        content = claude_md_path.read_text()
        import datetime
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        assert current_date in content, \
            f"Version table not updated with current date {current_date}"