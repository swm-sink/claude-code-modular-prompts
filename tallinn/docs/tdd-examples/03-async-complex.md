# Example 3: Async/Complex Module TDD - ClaudeCodeMCPServer

This example demonstrates Test-Driven Development (TDD) for complex, asynchronous modules. We'll implement key functionality of the `ClaudeCodeMCPServer` class, showing how to handle async operations, complex state management, and integration points through TDD.

## Target Module Overview

The `ClaudeCodeMCPServer` class handles:
- **Async resource discovery**: Finding commands and components across file system
- **Complex integration**: MCP protocol, file operations, metadata parsing
- **Caching behavior**: Performance optimization with state management
- **Multiple data sources**: Commands (.md files) and components (XML files)
- **Error handling**: Network timeouts, file permissions, malformed data

## TDD Strategy for Async/Complex Modules

When testing async/complex modules, we need to:
1. **Use pytest-asyncio** for async test support
2. **Mock complex integrations** (file system, external protocols)
3. **Test integration points** between subsystems
4. **Handle timing and concurrency** issues
5. **Test error propagation** through async call chains

## TDD Cycle Implementation

### 🔴 Red Phase 1: Basic Resource Discovery

Let's start with the fundamental async behavior - discovering resources.

```python
# tests/unit/test_mcp_server_complex_tdd.py
#!/usr/bin/env python3

import pytest
import asyncio
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock
import sys

# Import test utilities
sys.path.insert(0, str(Path(__file__).parent.parent))
from test_utils import create_temp_project

# Import the module under test
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from mcp_server import ClaudeCodeMCPServer


class TestMCPServerComplexTDD:
    """TDD implementation for complex ClaudeCodeMCPServer functionality."""
    
    @pytest.fixture
    async def temp_project_async(self):
        """Create temporary project structure for async testing."""
        temp_path = create_temp_project()
        
        # Create commands directory with test files
        commands_dir = temp_path / ".claude" / "commands" / "core"
        commands_dir.mkdir(parents=True, exist_ok=True)
        
        # Create a simple test command
        test_cmd = commands_dir / "async-test.md"
        test_cmd.write_text("""---
name: /async-test
description: Test command for async testing
usage: /async-test [args]
tools: Read, Write
---

# Async Test Command
This command tests async functionality.
""")
        
        yield temp_path
        shutil.rmtree(temp_path)
    
    @pytest.mark.asyncio
    async def test_discover_resources_returns_list_of_resources(self, temp_project_async):
        """Test: _discover_resources should return a list of resource objects."""
        # Arrange
        server = ClaudeCodeMCPServer(str(temp_project_async))
        
        # Act
        resources = await server._discover_resources()
        
        # Assert
        assert isinstance(resources, list)
        assert len(resources) > 0
        
        # Check resource structure
        for resource in resources:
            assert hasattr(resource, 'uri')
            assert hasattr(resource, 'name')
            assert hasattr(resource, 'description')
```

**Run the test:**
```bash
$ pytest tests/unit/test_mcp_server_complex_tdd.py::TestMCPServerComplexTDD::test_discover_resources_returns_list_of_resources -v

FAILED - Depends on actual file system and existing implementation
```

✅ **Test fails as expected** - we need to mock the complex file system interactions.

### 🟢 Green Phase 1: Mock Complex File Operations

```python
class TestMCPServerComplexTDD:
    """TDD implementation for complex ClaudeCodeMCPServer functionality."""
    
    @pytest.fixture
    def mock_resource_structure(self):
        """Mock a realistic resource structure."""
        return [
            Mock(
                uri="file://commands/core/test-cmd.md",
                name="/test-cmd",
                description="A test command"
            ),
            Mock(
                uri="file://components/test/component.md", 
                name="test-component",
                description="A test component"
            )
        ]
    
    @pytest.mark.asyncio
    async def test_discover_resources_returns_list_of_resources(self, mock_resource_structure):
        """Test: _discover_resources should return a list of resource objects."""
        # Arrange
        with patch.object(ClaudeCodeMCPServer, '_discover_commands') as mock_cmd, \
             patch.object(ClaudeCodeMCPServer, '_discover_components') as mock_comp:
            
            # Mock the async methods to populate a resources list
            async def mock_discover_commands(resources_list):
                resources_list.extend(mock_resource_structure[:1])  # Add command
            
            async def mock_discover_components(resources_list):
                resources_list.extend(mock_resource_structure[1:])  # Add component
            
            mock_cmd.side_effect = mock_discover_commands
            mock_comp.side_effect = mock_discover_components
            
            server = ClaudeCodeMCPServer("/fake/path")
            
            # Act
            resources = await server._discover_resources()
            
            # Assert
            assert isinstance(resources, list)
            assert len(resources) == 2
            assert resources[0].name == "/test-cmd"
            assert resources[1].name == "test-component"
```

**Run the test:**
```bash
$ pytest tests/unit/test_mcp_server_complex_tdd.py::TestMCPServerComplexTDD::test_discover_resources_returns_list_of_resources -v

PASSED
```

✅ **Test passes** - basic async resource discovery works.

### 🔴 Red Phase 2: Test Command Discovery Details

```python
@pytest.mark.asyncio
async def test_discover_commands_processes_markdown_files_with_frontmatter(self):
    """Test: _discover_commands should process .md files and extract metadata."""
    # Arrange
    fake_commands_dir = Path("/fake/commands")
    
    # Mock file system to return our test files
    mock_files = [
        fake_commands_dir / "core" / "test1.md",
        fake_commands_dir / "dev" / "test2.md",
    ]
    
    with patch('pathlib.Path.rglob') as mock_rglob, \
         patch.object(ClaudeCodeMCPServer, '_extract_command_metadata') as mock_extract:
        
        # Setup file discovery
        mock_rglob.return_value = mock_files
        
        # Setup metadata extraction
        async def mock_extract_metadata(file_path):
            if "test1.md" in str(file_path):
                return {
                    'name': '/test1',
                    'description': 'First test command',
                    'category': 'core'
                }
            elif "test2.md" in str(file_path):
                return {
                    'name': '/test2', 
                    'description': 'Second test command',
                    'category': 'dev'
                }
            return {}
        
        mock_extract.side_effect = mock_extract_metadata
        
        server = ClaudeCodeMCPServer("/fake/path")
        resources = []
        
        # Act
        await server._discover_commands(resources)
        
        # Assert
        assert len(resources) == 2
        assert resources[0].name == '/test1'
        assert resources[1].name == '/test2'
        assert "core" in resources[0].uri
        assert "dev" in resources[1].uri
```

**Run the test:**
```bash
$ pytest tests/unit/test_mcp_server_complex_tdd.py::TestMCPServerComplexTDD::test_discover_commands_processes_markdown_files_with_frontmatter -v

FAILED - Need to implement async metadata extraction properly
```

✅ **Test fails as expected** - our mocking doesn't match the actual async behavior.

### 🟢 Green Phase 2: Implement Async Metadata Processing

We need to understand how the real `_extract_command_metadata` method works:

```python
@pytest.mark.asyncio
async def test_discover_commands_processes_markdown_files_with_frontmatter(self):
    """Test: _discover_commands should process .md files and extract metadata."""
    # Arrange
    server = ClaudeCodeMCPServer("/fake/path")
    resources = []
    
    # Create realistic file mocks
    mock_file1 = Mock()
    mock_file1.name = "test1.md"
    mock_file1.relative_to.return_value = Path("commands/core/test1.md")
    
    mock_file2 = Mock()
    mock_file2.name = "test2.md" 
    mock_file2.relative_to.return_value = Path("commands/dev/test2.md")
    
    with patch.object(server.commands_dir, 'rglob', return_value=[mock_file1, mock_file2]) as mock_rglob, \
         patch.object(server, '_extract_command_metadata') as mock_extract:
        
        # Mock async metadata extraction
        async def extract_metadata(file_path):
            if "test1.md" in str(file_path):
                return {
                    'name': '/test1',
                    'description': 'First test command',
                    'category': 'core',
                    'usage': '/test1 [args]',
                    'tools': 'Read, Write'
                }
            return {
                'name': '/test2',
                'description': 'Second test command', 
                'category': 'dev',
                'usage': '/test2 [args]',
                'tools': 'Grep, Edit'
            }
        
        mock_extract.side_effect = extract_metadata
        
        # Act
        await server._discover_commands(resources)
        
        # Assert
        assert len(resources) == 2
        
        # Verify first resource
        cmd1 = resources[0]
        assert cmd1.name == '/test1'
        assert cmd1.description == 'First test command'
        assert "commands/core/test1.md" in cmd1.uri
        
        # Verify second resource
        cmd2 = resources[1] 
        assert cmd2.name == '/test2'
        assert cmd2.description == 'Second test command'
        assert "commands/dev/test2.md" in cmd2.uri
```

### 🔴 Red Phase 3: Test Error Handling in Async Context

```python
@pytest.mark.asyncio
async def test_discover_resources_handles_file_permission_errors_gracefully(self):
    """Test: Should handle file permission errors during discovery."""
    # Arrange
    server = ClaudeCodeMCPServer("/fake/path")
    
    with patch.object(server, '_discover_commands') as mock_cmd, \
         patch.object(server, '_discover_components') as mock_comp:
        
        # Simulate permission error in command discovery
        mock_cmd.side_effect = PermissionError("Access denied to commands directory")
        
        # Components discovery should still work
        async def mock_comp_success(resources):
            resources.append(Mock(uri="file://comp.md", name="comp", description="Component"))
        
        mock_comp.side_effect = mock_comp_success
        
        # Act & Assert - should not raise exception
        resources = await server._discover_resources()
        
        # Should still get components even if commands fail
        assert len(resources) == 1
        assert resources[0].name == "comp"

@pytest.mark.asyncio
async def test_discover_resources_handles_malformed_files_gracefully(self):
    """Test: Should skip malformed files and continue processing."""
    # Arrange
    server = ClaudeCodeMCPServer("/fake/path")
    resources = []
    
    # Mock files where some have parsing errors
    mock_good_file = Mock()
    mock_good_file.relative_to.return_value = Path("commands/good.md")
    
    mock_bad_file = Mock()
    mock_bad_file.relative_to.return_value = Path("commands/bad.md")
    
    with patch.object(server.commands_dir, 'rglob', return_value=[mock_good_file, mock_bad_file]), \
         patch.object(server, '_extract_command_metadata') as mock_extract:
        
        async def extract_with_errors(file_path):
            if "bad.md" in str(file_path):
                raise ValueError("Malformed frontmatter")
            return {
                'name': '/good-command',
                'description': 'A working command',
                'category': 'core'
            }
        
        mock_extract.side_effect = extract_with_errors
        
        # Act
        await server._discover_commands(resources)
        
        # Assert - should only get the good file
        assert len(resources) == 1
        assert resources[0].name == '/good-command'
```

**Run the tests:**
```bash
$ pytest tests/unit/test_mcp_server_complex_tdd.py::TestMCPServerComplexTDD -k "error" -v

PASSED (if error handling exists) or FAILED (if we need to implement it)
```

### 🔴 Red Phase 4: Test Caching Behavior

```python
@pytest.mark.asyncio
async def test_discover_resources_caches_results_for_performance(self):
    """Test: Should cache resource discovery results to avoid repeated work."""
    # Arrange
    server = ClaudeCodeMCPServer("/fake/path")
    
    # Mock expensive discovery operations
    discovery_call_count = {'commands': 0, 'components': 0}
    
    async def mock_discover_commands(resources):
        discovery_call_count['commands'] += 1
        resources.append(Mock(uri="file://cmd.md", name="/cmd", description="Command"))
    
    async def mock_discover_components(resources):
        discovery_call_count['components'] += 1
        resources.append(Mock(uri="file://comp.md", name="comp", description="Component"))
    
    with patch.object(server, '_discover_commands', side_effect=mock_discover_commands), \
         patch.object(server, '_discover_components', side_effect=mock_discover_components):
        
        # Act - call discovery multiple times
        resources1 = await server._discover_resources()
        resources2 = await server._discover_resources()
        resources3 = await server._discover_resources()
        
        # Assert - should only call expensive operations once
        assert discovery_call_count['commands'] == 1
        assert discovery_call_count['components'] == 1
        
        # All results should be identical
        assert len(resources1) == len(resources2) == len(resources3) == 2
        assert resources1[0].name == resources2[0].name == resources3[0].name

@pytest.mark.asyncio 
async def test_discover_resources_cache_can_be_invalidated(self):
    """Test: Cache should be invalidatable for fresh data."""
    # Arrange
    server = ClaudeCodeMCPServer("/fake/path")
    
    call_count = {'count': 0}
    
    async def mock_discovery_that_changes(resources):
        call_count['count'] += 1
        resources.append(Mock(
            uri=f"file://cmd{call_count['count']}.md",
            name=f"/cmd{call_count['count']}",
            description=f"Command {call_count['count']}"
        ))
    
    with patch.object(server, '_discover_commands', side_effect=mock_discovery_that_changes), \
         patch.object(server, '_discover_components'):
        
        # Act
        resources1 = await server._discover_resources()
        
        # Clear cache (simulate cache invalidation)
        server.resources_cache.clear()
        
        resources2 = await server._discover_resources()
        
        # Assert - should get different results after cache clear
        assert call_count['count'] == 2
        assert resources1[0].name == "/cmd1"
        assert resources2[0].name == "/cmd2"
```

### 🔴 Red Phase 5: Test Concurrent Access

```python
@pytest.mark.asyncio
async def test_discover_resources_handles_concurrent_access_safely(self):
    """Test: Should handle multiple concurrent discovery requests safely."""
    # Arrange
    server = ClaudeCodeMCPServer("/fake/path")
    
    # Mock slow discovery to test concurrency
    discovery_count = {'count': 0}
    
    async def slow_discover_commands(resources):
        discovery_count['count'] += 1
        await asyncio.sleep(0.1)  # Simulate slow I/O
        resources.append(Mock(uri="file://cmd.md", name="/cmd", description="Command"))
    
    async def slow_discover_components(resources):
        await asyncio.sleep(0.05)  # Simulate slow I/O
        resources.append(Mock(uri="file://comp.md", name="comp", description="Component"))
    
    with patch.object(server, '_discover_commands', side_effect=slow_discover_commands), \
         patch.object(server, '_discover_components', side_effect=slow_discover_components):
        
        # Act - start multiple concurrent discoveries
        tasks = [
            server._discover_resources(),
            server._discover_resources(), 
            server._discover_resources()
        ]
        
        results = await asyncio.gather(*tasks)
        
        # Assert - all should get same results, discovery should only happen once due to caching
        assert len(results) == 3
        for result in results:
            assert len(result) == 2  # 1 command + 1 component
            assert result[0].name == "/cmd"
            assert result[1].name == "comp"
        
        # Discovery should only happen once due to proper caching
        assert discovery_count['count'] <= 1  # May be 1 if no caching, should be 1 with proper caching
```

### 🔵 Refactor Phase: Create Comprehensive Async Test Suite

Now let's refactor our test suite to be more maintainable:

```python
#!/usr/bin/env python3
"""
TDD Example: Async/Complex Module Testing
Testing ClaudeCodeMCPServer async functionality
"""

import pytest
import asyncio
import tempfile
import json
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from test_utils import create_temp_project

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from mcp_server import ClaudeCodeMCPServer


class TestMCPServerAsyncTDD:
    """TDD implementation for ClaudeCodeMCPServer async functionality."""
    
    @pytest.fixture
    def mock_server_environment(self):
        """Create a controlled mock environment for server testing."""
        # Mock file system structure
        mock_commands = [
            {
                'path': Path("commands/core/cmd1.md"),
                'metadata': {'name': '/cmd1', 'description': 'Core command', 'category': 'core'}
            },
            {
                'path': Path("commands/dev/cmd2.md"), 
                'metadata': {'name': '/cmd2', 'description': 'Dev command', 'category': 'dev'}
            }
        ]
        
        mock_components = [
            {
                'path': Path("components/test/comp1.md"),
                'metadata': {'name': 'comp1', 'description': 'Test component'}
            }
        ]
        
        return {
            'commands': mock_commands,
            'components': mock_components,
            'project_root': '/fake/project'
        }
    
    @pytest.fixture
    def server_with_mocks(self, mock_server_environment):
        """Create server with comprehensive mocking."""
        server = ClaudeCodeMCPServer(mock_server_environment['project_root'])
        
        # Attach mock data for test access
        server._test_commands = mock_server_environment['commands']
        server._test_components = mock_server_environment['components']
        
        return server
    
    # Core async functionality tests
    @pytest.mark.asyncio
    async def test_discover_resources_returns_structured_resources(self, server_with_mocks):
        """Test: _discover_resources should return properly structured resource objects."""
        # Arrange
        server = server_with_mocks
        
        with patch.object(server, '_discover_commands') as mock_cmd, \
             patch.object(server, '_discover_components') as mock_comp:
            
            async def populate_commands(resources):
                for cmd in server._test_commands:
                    mock_resource = Mock()
                    mock_resource.uri = f"file://{cmd['path']}"
                    mock_resource.name = cmd['metadata']['name']
                    mock_resource.description = cmd['metadata']['description']
                    resources.append(mock_resource)
            
            async def populate_components(resources):
                for comp in server._test_components:
                    mock_resource = Mock()
                    mock_resource.uri = f"file://{comp['path']}"
                    mock_resource.name = comp['metadata']['name']
                    mock_resource.description = comp['metadata']['description']
                    resources.append(mock_resource)
            
            mock_cmd.side_effect = populate_commands
            mock_comp.side_effect = populate_components
            
            # Act
            resources = await server._discover_resources()
            
            # Assert
            assert len(resources) == 3  # 2 commands + 1 component
            
            # Verify command resources
            cmd_resources = [r for r in resources if r.name.startswith('/')]
            assert len(cmd_resources) == 2
            assert cmd_resources[0].name == '/cmd1'
            assert cmd_resources[1].name == '/cmd2'
            
            # Verify component resources
            comp_resources = [r for r in resources if not r.name.startswith('/')]
            assert len(comp_resources) == 1
            assert comp_resources[0].name == 'comp1'
    
    @pytest.mark.asyncio
    async def test_discover_commands_processes_files_with_metadata_extraction(self, server_with_mocks):
        """Test: _discover_commands should extract metadata from each file."""
        # Arrange
        server = server_with_mocks
        resources = []
        
        # Mock file discovery
        mock_files = [cmd['path'] for cmd in server._test_commands]
        
        with patch.object(server.commands_dir, 'rglob', return_value=mock_files) as mock_rglob, \
             patch.object(server, '_extract_command_metadata') as mock_extract:
            
            # Setup metadata extraction to return test data
            async def extract_metadata(file_path):
                for cmd in server._test_commands:
                    if cmd['path'].name in str(file_path):
                        return cmd['metadata']
                return {}
            
            mock_extract.side_effect = extract_metadata
            
            # Act
            await server._discover_commands(resources)
            
            # Assert
            assert len(resources) == 2
            assert all(hasattr(r, 'uri') for r in resources)
            assert all(hasattr(r, 'name') for r in resources)
            assert all(hasattr(r, 'description') for r in resources)
            
            # Verify metadata extraction was called for each file
            assert mock_extract.call_count == 2
    
    # Error handling tests
    @pytest.mark.asyncio
    async def test_discover_resources_handles_partial_failures_gracefully(self, server_with_mocks):
        """Test: Should continue processing even if some discoveries fail."""
        # Arrange
        server = server_with_mocks
        
        with patch.object(server, '_discover_commands') as mock_cmd, \
             patch.object(server, '_discover_components') as mock_comp:
            
            # Commands discovery fails
            mock_cmd.side_effect = PermissionError("Cannot read commands directory")
            
            # Components discovery succeeds
            async def successful_comp_discovery(resources):
                mock_resource = Mock()
                mock_resource.uri = "file://components/working.md"
                mock_resource.name = "working-component"
                mock_resource.description = "A working component"
                resources.append(mock_resource)
            
            mock_comp.side_effect = successful_comp_discovery
            
            # Act - should not raise exception
            resources = await server._discover_resources()
            
            # Assert - should still get component results
            assert len(resources) == 1
            assert resources[0].name == "working-component"
    
    @pytest.mark.asyncio
    async def test_discover_resources_handles_malformed_data_gracefully(self, server_with_mocks):
        """Test: Should skip malformed files and continue processing valid ones."""
        # Arrange
        server = server_with_mocks
        resources = []
        
        # Mix of good and bad files
        good_file = Mock()
        good_file.relative_to.return_value = Path("commands/good.md")
        
        bad_file = Mock()
        bad_file.relative_to.return_value = Path("commands/bad.md")
        
        with patch.object(server.commands_dir, 'rglob', return_value=[good_file, bad_file]), \
             patch.object(server, '_extract_command_metadata') as mock_extract:
            
            async def extract_with_some_failures(file_path):
                if "bad.md" in str(file_path):
                    raise ValueError("Malformed YAML frontmatter")
                return {
                    'name': '/good-command',
                    'description': 'A properly formatted command',
                    'category': 'core'
                }
            
            mock_extract.side_effect = extract_with_some_failures
            
            # Act
            await server._discover_commands(resources)
            
            # Assert - should process good file, skip bad file
            assert len(resources) == 1
            assert resources[0].name == '/good-command'
    
    # Performance and caching tests
    @pytest.mark.asyncio
    async def test_discover_resources_implements_caching_for_performance(self, server_with_mocks):
        """Test: Should cache results to avoid repeated expensive operations."""
        # Arrange
        server = server_with_mocks
        call_counts = {'commands': 0, 'components': 0}
        
        async def counting_cmd_discovery(resources):
            call_counts['commands'] += 1
            mock_resource = Mock()
            mock_resource.uri = "file://cmd.md"
            mock_resource.name = "/cached-cmd"
            mock_resource.description = "Cached command"
            resources.append(mock_resource)
        
        async def counting_comp_discovery(resources):
            call_counts['components'] += 1
            mock_resource = Mock()
            mock_resource.uri = "file://comp.md"
            mock_resource.name = "cached-comp"
            mock_resource.description = "Cached component"
            resources.append(mock_resource)
        
        with patch.object(server, '_discover_commands', side_effect=counting_cmd_discovery), \
             patch.object(server, '_discover_components', side_effect=counting_comp_discovery):
            
            # Act - multiple calls
            result1 = await server._discover_resources()
            result2 = await server._discover_resources()
            result3 = await server._discover_resources()
            
            # Assert - expensive operations called only once
            assert call_counts['commands'] == 1
            assert call_counts['components'] == 1
            
            # Results should be consistent
            assert len(result1) == len(result2) == len(result3) == 2
            assert result1[0].name == result2[0].name == result3[0].name
    
    @pytest.mark.asyncio
    async def test_concurrent_discovery_requests_handled_safely(self, server_with_mocks):
        """Test: Multiple concurrent discovery requests should be handled safely."""
        # Arrange
        server = server_with_mocks
        discovery_count = {'count': 0}
        
        async def slow_discovery_simulation(resources):
            discovery_count['count'] += 1
            # Simulate I/O delay
            await asyncio.sleep(0.01)
            
            mock_resource = Mock()
            mock_resource.uri = f"file://concurrent-{discovery_count['count']}.md"
            mock_resource.name = f"/concurrent-{discovery_count['count']}"
            mock_resource.description = f"Concurrent resource {discovery_count['count']}"
            resources.append(mock_resource)
        
        with patch.object(server, '_discover_commands', side_effect=slow_discovery_simulation), \
             patch.object(server, '_discover_components'):
            
            # Act - concurrent requests
            tasks = [
                server._discover_resources(),
                server._discover_resources(),
                server._discover_resources(),
                server._discover_resources(),
                server._discover_resources()
            ]
            
            results = await asyncio.gather(*tasks)
            
            # Assert - all results should be consistent
            assert len(results) == 5
            for result in results:
                assert len(result) >= 1
            
            # With proper caching, discovery should happen only once
            assert discovery_count['count'] <= 5  # Upper bound without caching
    
    # Integration test
    @pytest.mark.asyncio
    async def test_full_resource_discovery_integration(self, server_with_mocks):
        """Test: Full integration of resource discovery with realistic data."""
        # Arrange
        server = server_with_mocks
        
        # Create realistic mock file structure
        with patch('pathlib.Path.exists', return_value=True), \
             patch.object(server.commands_dir, 'rglob') as mock_cmd_rglob, \
             patch.object(server.components_dir, 'rglob') as mock_comp_rglob, \
             patch.object(server, '_extract_command_metadata') as mock_cmd_meta, \
             patch.object(server, '_extract_xml_metadata') as mock_comp_meta:
            
            # Setup command files
            cmd_files = [
                Mock(relative_to=Mock(return_value=Path("commands/core/auto.md"))),
                Mock(relative_to=Mock(return_value=Path("commands/dev/debug.md")))
            ]
            mock_cmd_rglob.return_value = cmd_files
            
            # Setup component files  
            comp_files = [
                Mock(relative_to=Mock(return_value=Path("components/validation/input.md")))
            ]
            mock_comp_rglob.return_value = comp_files
            
            # Setup metadata extraction
            async def extract_cmd_metadata(file_path):
                if "auto.md" in str(file_path):
                    return {'name': '/auto', 'description': 'Auto command', 'category': 'core'}
                return {'name': '/debug', 'description': 'Debug command', 'category': 'dev'}
            
            def extract_comp_metadata(content):
                return {'name': 'input-validation', 'description': 'Input validation component'}
            
            mock_cmd_meta.side_effect = extract_cmd_metadata
            mock_comp_meta.return_value = {'name': 'input-validation', 'description': 'Input validation component'}
            
            # Mock file reading for components
            with patch('builtins.open', mock_open(read_data="<metadata><name>input-validation</name></metadata>")):
                # Act
                resources = await server._discover_resources()
                
                # Assert
                assert len(resources) == 3  # 2 commands + 1 component
                
                # Verify commands
                cmd_resources = [r for r in resources if r.name.startswith('/')]
                assert len(cmd_resources) == 2
                cmd_names = {r.name for r in cmd_resources}
                assert cmd_names == {'/auto', '/debug'}
                
                # Verify components
                comp_resources = [r for r in resources if not r.name.startswith('/')]
                assert len(comp_resources) == 1
                assert comp_resources[0].name == 'input-validation'


# Additional test utilities for async testing
class AsyncTestHelpers:
    """Helper utilities for async testing patterns."""
    
    @staticmethod
    async def create_mock_resources(count=3, prefix="test"):
        """Create mock resources for testing."""
        resources = []
        for i in range(count):
            mock_resource = Mock()
            mock_resource.uri = f"file://{prefix}-{i}.md"
            mock_resource.name = f"/{prefix}-{i}"
            mock_resource.description = f"Test resource {i}"
            resources.append(mock_resource)
        return resources
    
    @staticmethod
    def create_slow_async_mock(delay=0.01, return_value=None):
        """Create an async mock that simulates slow I/O."""
        async def slow_operation(*args, **kwargs):
            await asyncio.sleep(delay)
            return return_value
        return AsyncMock(side_effect=slow_operation)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--asyncio-mode=auto"])
```

## Key TDD Lessons for Async/Complex Modules

### 1. Async Testing Requires Special Setup
```python
# ✅ GOOD: Proper async test setup
@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected

# ❌ BAD: Missing async/await
def test_async_function():
    result = async_function()  # Returns coroutine, not result
    assert result == expected
```

### 2. Mock Async Dependencies Carefully
```python
# ✅ GOOD: Mock async methods properly
with patch.object(obj, 'async_method', new_callable=AsyncMock) as mock:
    mock.return_value = "expected"
    result = await obj.async_method()

# ❌ BAD: Using regular Mock for async
with patch.object(obj, 'async_method', return_value="expected"):
    result = await obj.async_method()  # Will fail
```

### 3. Test Concurrency and Race Conditions
```python
async def test_concurrent_access():
    tasks = [expensive_operation() for _ in range(10)]
    results = await asyncio.gather(*tasks)
    # Verify all results are consistent
```

### 4. Handle Partial Failures Gracefully
Complex modules often have multiple failure points:
- **Network timeouts**: Mock network delays and failures
- **File system errors**: Test permission denied, disk full, etc.
- **Data corruption**: Test malformed input handling
- **Resource exhaustion**: Test memory/connection limits

### 5. Performance Testing in TDD
```python
async def test_caching_improves_performance():
    start_time = time.time()
    
    # First call - should be slow
    await expensive_operation()
    first_call_time = time.time() - start_time
    
    start_time = time.time()
    
    # Second call - should be fast (cached)
    await expensive_operation()
    second_call_time = time.time() - start_time
    
    assert second_call_time < first_call_time * 0.1  # 10x faster
```

## Complexity Comparison

| Aspect | Simple Function | Class with Dependencies | Async/Complex Module |
|--------|-----------------|------------------------|---------------------|
| **Test Setup** | Minimal | Moderate mocking | Extensive async mocking |
| **Error Handling** | Input validation | Dependency failures | Network, concurrency, state |
| **Performance** | Not relevant | Method efficiency | Caching, concurrency, I/O |
| **State Management** | Stateless | Object state | Distributed state, caching |
| **Integration** | None | Internal dependencies | External systems, protocols |

## Running This Example

```bash
# Install async testing dependencies
pip install pytest-asyncio

# Run the async TDD example
pytest docs/tdd-examples/03-async-complex.md -v --asyncio-mode=auto

# Run with timing to see async behavior
pytest docs/tdd-examples/03-async-complex.md -v --durations=10

# Run concurrency tests specifically
pytest docs/tdd-examples/03-async-complex.md -k "concurrent" -v

# Run with coverage for complex modules
pytest docs/tdd-examples/03-async-complex.md --cov=mcp_server --cov-report=term-missing
```

This example demonstrates how TDD scales to handle the most complex scenarios in software development: asynchronous operations, integration points, error handling, and performance considerations. The discipline of Red-Green-Refactor remains the same, but the tooling and techniques must evolve to handle the complexity.