"""Test command loading and validation."""

import os
import pytest
from pathlib import Path


class TestCommandLoader:
    """Test suite for command loading functionality."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "prompt_eng" / "commands" / "core"
    
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
            "session.md",
            "docs.md",
            "protocol.md"
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
        # Updated to be less restrictive - some commands may have examples or schemas
        implementation_keywords = [
            "```python", "```javascript", "```bash",
            "def main(", "class Implementation"
        ]
        
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text().lower()
            
            for keyword in implementation_keywords:
                assert keyword not in content, \
                    f"Command {command_file.name} contains implementation keyword '{keyword}'"
    
    def test_command_token_budget(self, commands_dir):
        """Test that commands stay within reasonable token budget."""
        # Increased budget for complex commands with schemas and examples
        max_chars = 10000 * 4  # 40k characters for 10k tokens
        
        # Special handling for comprehensive commands
        special_cases = {
            "query.md": 12000 * 4,    # 48k characters for 12k tokens
            "swarm.md": 12000 * 4,    # 48k characters for 12k tokens  
            "feature.md": 12000 * 4   # 48k characters for 12k tokens
        }
        
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            char_count = len(content)
            
            # Check if this command has special token budget
            limit = special_cases.get(command_file.name, max_chars)
            
            assert char_count <= limit, \
                f"Command {command_file.name} exceeds token budget ({char_count} chars, limit: {limit})"


class TestStartHereCommands:
    """Test suite for start_here initialization commands."""
    
    @pytest.fixture
    def start_here_dir(self):
        """Get the start_here directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "start_here"
    
    def test_start_here_directory_exists(self, start_here_dir):
        """Test that start_here directory exists."""
        assert start_here_dir.exists(), f"Start here directory not found at {start_here_dir}"
        assert start_here_dir.is_dir(), f"{start_here_dir} is not a directory"
    
    def test_all_init_commands_present(self, start_here_dir):
        """Test that all init commands are present."""
        required_init_commands = [
            "init-custom.md",
            "init-new.md", 
            "init-research.md",
            "init-validate.md"
        ]
        
        for command in required_init_commands:
            command_path = start_here_dir / command
            assert command_path.exists(), f"Required init command {command} not found"
            assert command_path.stat().st_size > 0, f"Init command {command} is empty"
    
    def test_init_command_structure_validation(self, start_here_dir):
        """Test that init commands follow delegation pattern."""
        for command_file in start_here_dir.glob("*.md"):
            content = command_file.read_text()
            
            # Commands should have delegation target
            assert "<delegation target=" in content, \
                f"Init command {command_file.name} missing delegation pattern"
            
            # Commands should reference modules
            assert "modules/" in content or "system/" in content or "domain/" in content, \
                f"Init command {command_file.name} doesn't reference any modules"
    
    def test_init_command_token_budget(self, start_here_dir):
        """Test that init commands stay within reasonable token budget."""
        # Slightly higher budget for init commands due to questionnaires
        max_chars = 6000 * 4  # 24k characters for 6k tokens
        
        for command_file in start_here_dir.glob("*.md"):
            content = command_file.read_text()
            char_count = len(content)
            
            assert char_count <= max_chars, \
                f"Init command {command_file.name} exceeds token budget ({char_count} chars)"


class TestCommandMetadata:
    """Test command metadata and documentation."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "prompt_eng" / "commands" / "core"
    
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