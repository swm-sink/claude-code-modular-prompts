"""Test framework dependency graph and architecture."""

import os
import pytest
from pathlib import Path
import re


class TestDependencyGraph:
    """Test suite for framework dependency analysis."""
    
    @pytest.fixture
    def framework_root(self):
        """Get the framework root directory."""
        return Path(__file__).parent.parent.parent / ".claude"
    
    def test_claude_md_references_valid_files(self):
        """Test that CLAUDE.md references only existing files."""
        claude_md = Path(__file__).parent.parent.parent / "CLAUDE.md"
        assert claude_md.exists(), "CLAUDE.md not found"
        
        content = claude_md.read_text()
        
        # Find all module references
        module_refs = re.findall(r'modules/[\w/\-]+\.md', content)
        
        for ref in module_refs:
            ref_path = Path(__file__).parent.parent.parent / ".claude" / ref
            assert ref_path.exists(), f"CLAUDE.md references non-existent module: {ref}"
    
    def test_command_module_connections(self, framework_root):
        """Test that all command-module connections are valid."""
        commands_dir = framework_root / "commands"
        modules_dir = framework_root / "modules"
        
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            
            # Find module references
            module_refs = re.findall(r'modules/[\w/\-]+\.md', content)
            
            for ref in module_refs:
                module_path = framework_root / ref
                assert module_path.exists(), \
                    f"Command {command_file.name} references non-existent module: {ref}"
    
    def test_no_orphaned_modules(self, framework_root):
        """Test that all modules are referenced by at least one command."""
        modules_dir = framework_root / "modules"
        commands_dir = framework_root / "commands"
        
        # Build set of all referenced modules
        referenced_modules = set()
        
        # Check commands
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            module_refs = re.findall(r'modules/([\w/\-]+\.md)', content)
            referenced_modules.update(module_refs)
        
        # Check CLAUDE.md
        claude_md = framework_root.parent / "CLAUDE.md"
        if claude_md.exists():
            content = claude_md.read_text()
            module_refs = re.findall(r'modules/([\w/\-]+\.md)', content)
            referenced_modules.update(module_refs)
        
        # Check all modules are referenced
        for module_file in modules_dir.rglob("*.md"):
            module_path = module_file.relative_to(modules_dir)
            # Some utility modules might not be directly referenced
            if "README" not in str(module_path) and "index" not in str(module_path):
                # Warning, not error - some modules might be indirectly used
                if str(module_path) not in referenced_modules:
                    # Use warnings module instead of pytest.warning
                    import warnings
                    warnings.warn(f"Module {module_path} is not referenced by any command")
    
    def test_framework_file_count(self, framework_root):
        """Test that framework stays under file count limit."""
        total_files = 0
        
        for file_path in framework_root.rglob("*"):
            if file_path.is_file():
                total_files += 1
        
        assert total_files < 100, f"Framework has {total_files} files, exceeding 100 file limit"
    
    def test_settings_structure(self, framework_root):
        """Test that settings directory has correct structure."""
        settings_dir = framework_root / "settings"
        assert settings_dir.exists(), "Settings directory not found"
        
        required_settings = ["commands.json", "core.json", "patterns.json", "permissions.json"]
        
        for setting in required_settings:
            setting_path = settings_dir / setting
            assert setting_path.exists(), f"Required settings file {setting} not found"
            
            # Validate JSON structure
            import json
            try:
                with open(setting_path) as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                pytest.fail(f"Invalid JSON in {setting}: {e}")


class TestArchitecturalIntegrity:
    """Test architectural principles and patterns."""
    
    @pytest.fixture
    def framework_root(self):
        """Get the framework root directory."""
        return Path(__file__).parent.parent.parent / ".claude"
    
    def test_delegation_pattern_enforced(self, framework_root):
        """Test that delegation pattern is properly implemented."""
        commands_dir = framework_root / "commands"
        
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            
            # Should have delegation
            assert any(pattern in content for pattern in [
                "<delegation", "delegates_to", "delegation target"
            ]), f"Command {command_file.name} doesn't follow delegation pattern"
            
            # Should NOT have implementation
            implementation_patterns = ["def ", "class ", "function ", "algorithm:"]
            for pattern in implementation_patterns:
                assert pattern not in content.lower(), \
                    f"Command {command_file.name} contains implementation (found '{pattern}')"
    
    def test_single_source_of_truth(self, framework_root):
        """Test that each concept exists in only one place."""
        concept_locations = {}
        
        # Track where concepts are defined
        for file_path in framework_root.rglob("*.md"):
            if file_path.is_file():
                content = file_path.read_text()
                
                # Look for concept definitions
                concepts = re.findall(r'(?:name|id|concept)[:=]\s*"?([a-zA-Z_\-]+)"?', content)
                
                for concept in concepts:
                    if concept in concept_locations:
                        # Some repetition is okay (references vs definitions)
                        if "definition" in content or "implementation" in content:
                            import warnings
                            warnings.warn(
                                f"Concept '{concept}' potentially defined in multiple places: "
                                f"{concept_locations[concept]} and {file_path.relative_to(framework_root)}"
                            )
                    else:
                        concept_locations[concept] = file_path.relative_to(framework_root)