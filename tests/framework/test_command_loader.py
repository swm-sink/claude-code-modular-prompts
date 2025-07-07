"""Test command loading and validation."""

import os
import pytest
from pathlib import Path


class TestCommandLoader:
    """Test suite for command loading functionality."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands"
    
    def test_commands_directory_exists(self, commands_dir):
        """Test that commands directory exists."""
        assert commands_dir.exists(), f"Commands directory not found at {commands_dir}"
        assert commands_dir.is_dir(), f"{commands_dir} is not a directory"
    
    def test_all_core_commands_present(self, commands_dir):
        """Test that all core commands are present."""
        required_commands = [
            "auto.md",
            "task.md", 
            "feature.md",
            "swarm.md",
            "query.md",
            "session.md"
        ]
        
        for command in required_commands:
            command_path = commands_dir / command
            assert command_path.exists(), f"Required command {command} not found"
            assert command_path.stat().st_size > 0, f"Command {command} is empty"
    
    def test_command_structure_validation(self, commands_dir):
        """Test that commands follow delegation pattern."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            
            # Commands should have delegation target
            assert "<delegation target=" in content or "delegates_to=" in content, \
                f"Command {command_file.name} missing delegation pattern"
            
            # Commands should reference modules
            assert "modules/" in content, \
                f"Command {command_file.name} doesn't reference any modules"
    
    def test_no_implementation_in_commands(self, commands_dir):
        """Test that commands only delegate, not implement."""
        implementation_keywords = [
            "def ", "class ", "function ", "```python", "```javascript",
            "implementation:", "algorithm:", "step 1:", "step 2:"
        ]
        
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text().lower()
            
            for keyword in implementation_keywords:
                assert keyword not in content, \
                    f"Command {command_file.name} contains implementation keyword '{keyword}'"
    
    def test_command_token_budget(self, commands_dir):
        """Test that commands stay within 4k token budget."""
        # Rough approximation: 1 token ≈ 4 characters
        max_chars = 4000 * 4  # 16k characters for 4k tokens
        
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            char_count = len(content)
            
            assert char_count <= max_chars, \
                f"Command {command_file.name} exceeds token budget ({char_count} chars)"


class TestCommandMetadata:
    """Test command metadata and documentation."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands"
    
    def test_command_has_purpose(self, commands_dir):
        """Test that each command has a clear purpose statement."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            
            assert "purpose=" in content or "## Purpose" in content, \
                f"Command {command_file.name} missing purpose statement"
    
    def test_command_has_usage_examples(self, commands_dir):
        """Test that each command has usage examples."""
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            
            assert "<example" in content or "## Example" in content or "### Usage" in content, \
                f"Command {command_file.name} missing usage examples"