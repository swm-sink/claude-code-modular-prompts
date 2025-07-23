"""
Test utilities and data factories for comprehensive testing.
"""

import tempfile
import json
import yaml
import secrets
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from unittest.mock import Mock, MagicMock, patch

class TestDataFactory:
    """Factory for generating test data."""
    
    @staticmethod
    def create_api_key(provider: str = "openai") -> str:
        """Generate a realistic looking API key."""
        prefixes = {
            "openai": "sk-",
            "anthropic": "ak-", 
            "google": "AIza",
            "azure": "az-"
        }
        prefix = prefixes.get(provider, "key-")
        return f"{prefix}{secrets.token_hex(16)}"
    
    @staticmethod
    def create_command_file(name: str = "test-command", include_metadata: bool = True) -> str:
        """Generate a command file content."""
        content = f"""
# {name.replace('-', ' ').title()}

**Usage**: `/{name} $ARGUMENTS`

## Key Arguments
- **$ARGUMENTS**: The arguments for the command

## Core Logic
"""
        
        if include_metadata:
            content = f"""<metadata>
<name>{name}</name>
<description>Test command for {name}</description>
</metadata>

{content}"""
        
        return content
    
    @staticmethod
    def create_component_file(name: str = "test-component", dependencies: List[str] = None) -> str:
        """Generate a component file content."""
        deps = dependencies or []
        dep_section = "\n".join([f"- {dep}" for dep in deps]) if deps else "- None"
        
        return f"""<metadata>
<name>{name}</name>
<description>Test component for {name}</description>
<dependencies>
{dep_section}
</dependencies>
</metadata>

# {name.replace('-', ' ').title()}

This is a test component that provides {name} functionality.

## Key Features
- Feature 1
- Feature 2

## Implementation
```python
def {name.replace('-', '_')}():
    pass
```
"""
    
    @staticmethod
    def create_security_issue(severity: str = "HIGH", category: str = "API Keys") -> Dict[str, Any]:
        """Create a security issue dict."""
        return {
            "severity": severity,
            "category": category,
            "description": f"Test {category} issue",
            "file": "test_file.py",
            "line": 42,
            "recommendation": f"Fix the {category} issue"
        }
    
    @staticmethod
    def create_performance_metric(metric_type: str = "cpu") -> Dict[str, Any]:
        """Create a performance metric."""
        return {
            "type": metric_type,
            "value": 75.5,
            "timestamp": datetime.now().isoformat(),
            "threshold": 80.0,
            "unit": "percent" if metric_type == "cpu" else "MB"
        }


class MockFactory:
    """Factory for creating common mock objects."""
    
    @staticmethod
    def create_mcp_server_mock() -> Mock:
        """Create a mock MCP server."""
        mock_server = Mock()
        mock_server.project_root = Path("/mock/project")
        mock_server.resources = []
        mock_server.commands = {}
        mock_server.components = {}
        mock_server.discover_resources = Mock(return_value=[
            {"name": "test-resource", "path": "/test/resource.md"}
        ])
        mock_server.execute_command = Mock(return_value={"status": "success"})
        return mock_server
    
    @staticmethod
    def create_security_auditor_mock() -> Mock:
        """Create a mock security auditor."""
        mock_auditor = Mock()
        mock_auditor.framework_root = Path("claude_prompt_factory")
        mock_auditor.security_issues = []
        mock_auditor.security_recommendations = []
        
        # Mock check methods
        mock_auditor.check_sensitive_data = Mock(return_value={
            "passed": True, "risk_level": "LOW", "issues": []
        })
        mock_auditor.check_input_validation = Mock(return_value={
            "passed": True, "risk_level": "LOW", "issues": []
        })
        
        return mock_auditor
    
    @staticmethod
    def create_api_key_manager_mock() -> Mock:
        """Create a mock API key manager."""
        mock_manager = Mock()
        mock_manager.key_store = {}
        mock_manager.master_key = b"test_master_key_32_bytes_long!!!"
        mock_manager.store_key = Mock()
        mock_manager.retrieve_key = Mock(return_value="test-api-key")
        mock_manager.rotate_key = Mock(return_value=True)
        return mock_manager


class FileSystemHelper:
    """Helper for file system operations in tests."""
    
    @staticmethod
    def create_project_structure(root_dir: Path) -> Dict[str, Path]:
        """Create a standard project structure for testing."""
        dirs = {
            "root": root_dir,
            "framework": root_dir / "claude_prompt_factory",
            "commands": root_dir / "claude_prompt_factory" / "commands",
            "components": root_dir / "claude_prompt_factory" / "components",
            "scripts": root_dir / "scripts",
            "tests": root_dir / "tests",
            "security": root_dir / "security",
            "performance": root_dir / "performance"
        }
        
        # Create all directories
        for dir_path in dirs.values():
            dir_path.mkdir(parents=True, exist_ok=True)
            
        return dirs
    
    @staticmethod
    def create_test_files(dirs: Dict[str, Path]) -> Dict[str, Path]:
        """Create test files in the project structure."""
        files = {}
        
        # Create command files
        cmd_file = dirs["commands"] / "test-command.md"
        cmd_file.write_text(TestDataFactory.create_command_file())
        files["test_command"] = cmd_file
        
        # Create component files
        comp_file = dirs["components"] / "test-component.md"
        comp_file.write_text(TestDataFactory.create_component_file())
        files["test_component"] = comp_file
        
        # Create config files
        config_file = dirs["root"] / "config.json"
        config_file.write_text(json.dumps({
            "project_name": "test_project",
            "version": "1.0.0"
        }))
        files["config"] = config_file
        
        return files


class AssertionHelpers:
    """Helper methods for common test assertions."""
    
    @staticmethod
    def assert_valid_api_key(key: str, provider: str = None):
        """Assert that an API key has valid format."""
        assert isinstance(key, str)
        assert len(key) > 10
        
        if provider == "openai":
            assert key.startswith("sk-")
        elif provider == "anthropic":
            assert key.startswith("ak-")
    
    @staticmethod
    def assert_security_issue_format(issue: Dict[str, Any]):
        """Assert that a security issue has the correct format."""
        required_fields = ["severity", "category", "description"]
        for field in required_fields:
            assert field in issue
        
        assert issue["severity"] in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    
    @staticmethod
    def assert_performance_metric_format(metric: Dict[str, Any]):
        """Assert that a performance metric has the correct format."""
        required_fields = ["type", "value", "timestamp"]
        for field in required_fields:
            assert field in metric
        
        assert isinstance(metric["value"], (int, float))
        assert metric["value"] >= 0


def mock_file_operations():
    """Context manager for mocking file operations."""
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('pathlib.Path.exists', return_value=True):
            with patch('pathlib.Path.is_file', return_value=True):
                with patch('pathlib.Path.is_dir', return_value=False):
                    yield mock_file


def create_temp_project() -> Path:
    """Create a temporary project structure for testing."""
    temp_dir = tempfile.mkdtemp()
    temp_path = Path(temp_dir)
    
    dirs = FileSystemHelper.create_project_structure(temp_path)
    files = FileSystemHelper.create_test_files(dirs)
    
    return temp_path


# Pytest fixtures that can be imported
import pytest

@pytest.fixture
def test_data_factory():
    """Provide test data factory."""
    return TestDataFactory()

@pytest.fixture
def mock_factory():
    """Provide mock factory."""
    return MockFactory()

@pytest.fixture
def file_system_helper():
    """Provide file system helper."""
    return FileSystemHelper()

@pytest.fixture
def assertion_helpers():
    """Provide assertion helpers."""
    return AssertionHelpers()

@pytest.fixture
def temp_project():
    """Create a temporary project structure."""
    temp_path = create_temp_project()
    yield temp_path
    # Cleanup
    import shutil
    shutil.rmtree(temp_path)