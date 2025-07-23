"""
Common test fixtures and utilities for all tests.
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, MagicMock

@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)

@pytest.fixture
def mock_project_root(temp_dir):
    """Create a mock project structure."""
    project_root = temp_dir / "project"
    project_root.mkdir()
    
    # Create basic structure
    (project_root / "claude_prompt_factory").mkdir()
    (project_root / "scripts").mkdir()
    (project_root / "tests").mkdir()
    
    return project_root

@pytest.fixture
def mock_security_auditor():
    """Create a mock SecurityAuditor instance."""
    mock_auditor = Mock()
    mock_auditor.framework_root = Path("claude_prompt_factory")
    mock_auditor.rotation_manager = Mock()
    mock_auditor.validator = Mock()
    mock_auditor.report_generator = Mock()
    
    return mock_auditor

@pytest.fixture
def temp_config_dir():
    """Create temporary directory for configuration files."""
    import tempfile
    import os
    with tempfile.TemporaryDirectory() as temp_dir:
        old_cwd = os.getcwd()
        os.chdir(temp_dir)
        try:
            yield Path(temp_dir)
        finally:
            os.chdir(old_cwd)

@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory structure for testing."""
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        project_root = Path(temp_dir)
        
        # Create .claude/commands directory structure
        commands_dir = project_root / ".claude" / "commands"
        commands_dir.mkdir(parents=True)
        
        # Create some test command files
        test_commands = {
            "core/task.md": {
                "name": "/task",
                "description": "Execute a task",
                "content": "---\nname: /task\ndescription: Execute a task\n---\n# Task Command\nExecute tasks."
            },
            "development/debug.md": {
                "name": "/debug",
                "description": "Debug code",
                "content": "---\nname: /debug\ndescription: Debug code\n---\n# Debug Command\nDebug your code."
            }
        }
        
        for cmd_path, cmd_data in test_commands.items():
            cmd_file = commands_dir / cmd_path
            cmd_file.parent.mkdir(parents=True, exist_ok=True)
            cmd_file.write_text(cmd_data["content"])
        
        # Create components directory
        components_dir = project_root / "claude_prompt_factory" / "components"
        components_dir.mkdir(parents=True)
        
        # Create a test component
        test_component = components_dir / "test-component.md"
        test_component.write_text("# Test Component\nThis is a test component.")
        
        yield project_root

@pytest.fixture
def mock_mcp_server():
    """Mock MCP server for testing."""
    from unittest.mock import patch
    with patch('mcp_server.Server') as mock_server:
        mock_instance = Mock()
        mock_server.return_value = mock_instance
        
        # Mock the decorators
        mock_instance.list_resources.return_value = lambda func: func
        mock_instance.read_resource.return_value = lambda func: func
        mock_instance.list_tools.return_value = lambda func: func
        mock_instance.call_tool.return_value = lambda func: func
        
        yield mock_instance

@pytest.fixture
def sample_config():
    """Sample configuration for testing."""
    return {
        "keys": {
            "openai": {
                "current": "old-key-123",
                "backup": "backup-key-456",
                "rotation_days": 30
            },
            "anthropic": {
                "current": "claude-key-789",
                "backup": "claude-backup-012",
                "rotation_days": 45
            }
        },
        "notifications": {
            "email": "admin@example.com",
            "webhook": "https://example.com/webhook"
        },
        "rotation_schedule": {
            "enabled": True,
            "check_interval_hours": 24
        }
    }
