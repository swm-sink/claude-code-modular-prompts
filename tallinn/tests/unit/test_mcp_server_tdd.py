#!/usr/bin/env python3
"""
Test-Driven Development (TDD) tests for MCP Server

This module implements comprehensive tests for the Claude Code MCP Server
following TDD principles: Red → Green → Refactor
"""

import asyncio
import json
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock
import pytest

# Import test utilities
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from test_utils import TestDataFactory, FileSystemHelper, create_temp_project

# Import the module under test
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from mcp_server import ClaudeCodeMCPServer


class TestMCPServerTDD:
    """TDD tests for Claude Code MCP Server."""
    
    @pytest.fixture
    def temp_project(self):
        """Create a temporary project structure."""
        temp_path = create_temp_project()
        
        # Create .claude/commands directory
        commands_dir = temp_path / ".claude" / "commands"
        commands_dir.mkdir(parents=True, exist_ok=True)
        
        # Create some test commands
        core_dir = commands_dir / "core"
        core_dir.mkdir(exist_ok=True)
        
        # Create a test command with frontmatter
        test_cmd = core_dir / "test-command.md"
        test_cmd.write_text("""---
name: /test-command
description: A test command for unit testing
usage: /test-command [args]
tools: Read, Write
---

# Test Command

This is a test command for unit testing.

## Examples

```bash
/test-command arg1 arg2
```
""")
        
        # Create a component
        comp_dir = temp_path / "claude_prompt_factory" / "components" / "test"
        comp_dir.mkdir(parents=True, exist_ok=True)
        
        test_comp = comp_dir / "test-component.md"
        test_comp.write_text("""<metadata>
<name>test-component</name>
<description>A test component</description>
</metadata>

# Test Component

This is a test component.
""")
        
        yield temp_path
        shutil.rmtree(temp_path)
    
    @pytest.fixture
    def server(self, temp_project):
        """Create an MCP server instance."""
        return ClaudeCodeMCPServer(str(temp_project))
    
    # Test 1: Server Initialization
    def test_server_initializes_with_project_root(self, temp_project):
        """Test that server initializes correctly with project root."""
        server = ClaudeCodeMCPServer(str(temp_project))
        
        assert server.project_root == temp_project
        assert server.commands_dir == temp_project / ".claude" / "commands"
        assert server.components_dir == temp_project / "claude_prompt_factory" / "components"
        assert server.server is not None
        assert server.resources_cache == {}
    
    # Test 2: Default Project Root
    def test_server_uses_cwd_as_default_project_root(self):
        """Test that server uses current directory if no project root provided."""
        original_cwd = Path.cwd()
        
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            import os
            os.chdir(temp_path)
            
            try:
                server = ClaudeCodeMCPServer()
                assert server.project_root == temp_path
            finally:
                os.chdir(original_cwd)
    
    # Test 3: Resource Discovery
    @pytest.mark.asyncio
    async def test_discover_resources_finds_commands_and_components(self, server, temp_project):
        """Test that resource discovery finds all commands and components."""
        resources = await server._discover_resources()
        
        assert len(resources) > 0
        
        # Check for command resources
        command_resources = [r for r in resources if "commands" in r.uri]
        assert len(command_resources) >= 1
        
        # Check for component resources
        component_resources = [r for r in resources if "components" in r.uri]
        assert len(component_resources) >= 1
        
        # Verify resource structure
        for resource in resources:
            assert hasattr(resource, 'uri')
            assert hasattr(resource, 'name')
            assert hasattr(resource, 'description')
    
    # Test 4: Command Discovery
    @pytest.mark.asyncio
    async def test_discover_commands_processes_markdown_files(self, server, temp_project):
        """Test that command discovery processes .md files correctly."""
        resources = []
        await server._discover_commands(resources)
        
        # Should find at least our test command
        assert len(resources) >= 1
        
        # Find our test command
        test_cmd_resource = None
        for resource in resources:
            if "test-command" in resource.uri:
                test_cmd_resource = resource
                break
        
        assert test_cmd_resource is not None
        assert test_cmd_resource.name == "/test-command"
        assert "test command" in test_cmd_resource.description.lower()
    
    # Test 5: Extract Command Metadata
    @pytest.mark.asyncio
    async def test_extract_command_metadata_from_frontmatter(self, server, temp_project):
        """Test extraction of command metadata from frontmatter."""
        test_file = temp_project / ".claude" / "commands" / "core" / "test-command.md"
        metadata = await server._extract_command_metadata(test_file)
        
        assert metadata['name'] == '/test-command'
        assert metadata['description'] == 'A test command for unit testing'
        assert metadata['usage'] == '/test-command [args]'
        assert metadata['tools'] == 'Read, Write'
        assert metadata['category'] == 'core'
    
    # Test 6: Extract XML Metadata
    def test_extract_xml_metadata_from_content(self, server):
        """Test extraction of metadata from XML format."""
        content = """<metadata>
<name>test-name</name>
<description>Test description</description>
</metadata>

Other content here
"""
        metadata = server._extract_xml_metadata(content)
        
        assert metadata['name'] == 'test-name'
        assert metadata['description'] == 'Test description'
    
    # Test 7: Component Discovery
    @pytest.mark.asyncio
    async def test_discover_components_processes_component_files(self, server, temp_project):
        """Test that component discovery finds and processes components."""
        resources = []
        await server._discover_components(resources)
        
        # Should find at least our test component
        assert len(resources) >= 1
        
        # Find our test component
        test_comp_resource = None
        for resource in resources:
            if "test-component" in resource.uri:
                test_comp_resource = resource
                break
        
        assert test_comp_resource is not None
        assert "test-component" in test_comp_resource.name
        assert "test component" in test_comp_resource.description.lower()
    
    # Test 8: Read Resource
    @pytest.mark.asyncio
    async def test_read_resource_returns_file_content(self, server, temp_project):
        """Test reading a resource returns its content."""
        # Create a simple resource
        test_file = temp_project / "test_resource.md"
        test_content = "# Test Resource\n\nThis is test content."
        test_file.write_text(test_content)
        
        # Read using relative URI
        uri = f"file://{test_file.relative_to(server.project_root)}"
        content = await server._read_resource(uri)
        
        assert content == test_content
    
    # Test 9: Execute Command
    @pytest.mark.asyncio
    async def test_execute_command_list_commands(self, server):
        """Test executing the list-commands tool."""
        result = await server._execute_command("list-commands", {})
        
        assert isinstance(result, str)
        assert "Available Commands" in result
        
        # Should contain our test command
        assert "/test-command" in result
    
    # Test 10: List Commands with Category Filter
    @pytest.mark.asyncio
    async def test_list_commands_with_category_filter(self, server):
        """Test listing commands filtered by category."""
        result = await server._list_commands(category="core")
        
        assert "/test-command" in result
        assert "core" in result.lower()
    
    # Test 11: Get Command Info
    @pytest.mark.asyncio
    async def test_get_command_info_returns_details(self, server):
        """Test getting detailed information about a command."""
        result = await server._get_command_info("/test-command")
        
        assert "/test-command" in result
        assert "test command for unit testing" in result.lower()
        assert "Usage:" in result
        assert "Examples:" in result
    
    # Test 12: Error Handling - Missing Command
    @pytest.mark.asyncio
    async def test_get_command_info_handles_missing_command(self, server):
        """Test error handling for non-existent command."""
        result = await server._get_command_info("/non-existent-command")
        
        assert "not found" in result.lower()
    
    # Test 13: Extract Examples from Content
    def test_extract_examples_from_content(self, server):
        """Test extraction of examples from markdown content."""
        content = """
# Command

## Examples

```bash
/command arg1 arg2
```

Another example:

```bash
/command --flag value
```
"""
        examples = server._extract_examples_from_content(content)
        
        assert len(examples) == 2
        assert examples[0]['code'] == '/command arg1 arg2'
        assert examples[1]['code'] == '/command --flag value'
    
    # Test 14: Caching Behavior
    @pytest.mark.asyncio
    async def test_resources_are_cached_after_discovery(self, server):
        """Test that resources are cached to improve performance."""
        # First discovery
        resources1 = await server._discover_resources()
        assert len(server.resources_cache) > 0
        
        # Second discovery should use cache
        with patch.object(server, '_discover_commands') as mock_discover:
            resources2 = await server._discover_resources()
            # Should not call discover methods if cache is fresh
            assert resources1 == resources2
    
    # Test 15: Handler Setup
    def test_server_handlers_are_setup(self, server):
        """Test that MCP handlers are properly setup."""
        # Verify handlers are registered
        assert hasattr(server.server, 'list_resources')
        assert hasattr(server.server, 'read_resource')
        assert hasattr(server.server, 'list_tools')
        assert hasattr(server.server, 'call_tool')


class TestMCPServerEdgeCases:
    """Edge case tests for MCP Server."""
    
    @pytest.fixture
    def empty_project(self):
        """Create an empty project structure."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield Path(temp_dir)
    
    @pytest.fixture
    def server_empty(self, empty_project):
        """Create server with empty project."""
        return ClaudeCodeMCPServer(str(empty_project))
    
    # Test 1: Empty Project
    @pytest.mark.asyncio
    async def test_discover_resources_handles_empty_project(self, server_empty):
        """Test resource discovery with no commands or components."""
        resources = await server_empty._discover_resources()
        
        # Should return empty list, not error
        assert isinstance(resources, list)
        assert len(resources) == 0
    
    # Test 2: Malformed Frontmatter
    @pytest.mark.asyncio
    async def test_extract_metadata_handles_malformed_frontmatter(self, server_empty, empty_project):
        """Test handling of malformed frontmatter."""
        bad_file = empty_project / "bad.md"
        bad_file.write_text("""---
name: /bad-command
description: Missing closing
tools: Read

# Command
""")
        
        metadata = await server_empty._extract_command_metadata(bad_file)
        
        # Should handle gracefully
        assert isinstance(metadata, dict)
        assert 'name' in metadata
    
    # Test 3: Unicode in Files
    @pytest.mark.asyncio
    async def test_handles_unicode_in_command_files(self, server_empty, empty_project):
        """Test handling of Unicode characters in command files."""
        unicode_file = empty_project / "unicode.md"
        unicode_file.write_text("""---
name: /unicode-test
description: 测试命令 🚀 тест
usage: /unicode-test [参数]
---

# Unicode Test 中文测试

Examples with emojis 🎉🎊
""", encoding='utf-8')
        
        metadata = await server_empty._extract_command_metadata(unicode_file)
        
        assert metadata['description'] == '测试命令 🚀 тест'
        assert '参数' in metadata['usage']
    
    # Test 4: Large Files
    @pytest.mark.asyncio
    async def test_handles_large_command_files(self, server_empty, empty_project):
        """Test handling of very large command files."""
        large_file = empty_project / "large.md"
        
        # Create a 1MB file
        large_content = "---\nname: /large\ndescription: Large file\n---\n\n"
        large_content += "# Large Command\n\n" + ("x" * 1024 + "\n") * 1024
        
        large_file.write_text(large_content)
        
        metadata = await server_empty._extract_command_metadata(large_file)
        
        assert metadata['name'] == '/large'
        assert metadata['description'] == 'Large file'
    
    # Test 5: Concurrent Access
    @pytest.mark.asyncio
    async def test_concurrent_resource_discovery(self, server_empty):
        """Test concurrent access to resource discovery."""
        # Run multiple discoveries concurrently
        tasks = [
            server_empty._discover_resources()
            for _ in range(10)
        ]
        
        results = await asyncio.gather(*tasks)
        
        # All should return the same result
        for result in results:
            assert result == results[0]
    
    # Test 6: Invalid URI
    @pytest.mark.asyncio
    async def test_read_resource_handles_invalid_uri(self, server_empty):
        """Test reading resource with invalid URI."""
        with pytest.raises(Exception):
            await server_empty._read_resource("invalid://uri/format")
    
    # Test 7: Permission Errors
    @pytest.mark.asyncio
    async def test_handles_permission_errors(self, server_empty, empty_project):
        """Test handling of files with permission errors."""
        protected_file = empty_project / "protected.md"
        protected_file.write_text("content")
        
        # Make file unreadable
        import os
        os.chmod(protected_file, 0o000)
        
        try:
            # Should handle gracefully
            resources = await server_empty._discover_resources()
            assert isinstance(resources, list)
        finally:
            # Restore permissions for cleanup
            os.chmod(protected_file, 0o644)


class TestMCPServerIntegration:
    """Integration tests for MCP Server."""
    
    @pytest.fixture
    def full_project(self):
        """Create a full project structure with multiple commands and components."""
        temp_path = create_temp_project()
        
        # Create multiple command categories
        categories = ['core', 'development', 'testing', 'security']
        commands_dir = temp_path / ".claude" / "commands"
        
        for category in categories:
            cat_dir = commands_dir / category
            cat_dir.mkdir(parents=True, exist_ok=True)
            
            # Create 2 commands per category
            for i in range(2):
                cmd_file = cat_dir / f"{category}-command-{i}.md"
                cmd_file.write_text(f"""---
name: /{category}-command-{i}
description: Command {i} in {category} category
usage: /{category}-command-{i} [args]
tools: Read, Write, Grep
---

# {category.title()} Command {i}

This is a test command in the {category} category.

## Examples

```bash
/{category}-command-{i} example
```
""")
        
        yield temp_path
        shutil.rmtree(temp_path)
    
    @pytest.fixture
    def server_full(self, full_project):
        """Create server with full project."""
        return ClaudeCodeMCPServer(str(full_project))
    
    # Test 1: Full Discovery
    @pytest.mark.asyncio
    async def test_full_resource_discovery(self, server_full):
        """Test discovery of all resources in a full project."""
        resources = await server_full._discover_resources()
        
        # Should find at least 8 commands (2 per category × 4 categories)
        command_resources = [r for r in resources if "commands" in r.uri]
        assert len(command_resources) >= 8
        
        # Check all categories are represented
        categories_found = set()
        for resource in command_resources:
            for category in ['core', 'development', 'testing', 'security']:
                if category in resource.uri:
                    categories_found.add(category)
        
        assert len(categories_found) == 4
    
    # Test 2: Category Filtering
    @pytest.mark.asyncio
    async def test_list_commands_by_all_categories(self, server_full):
        """Test listing commands for each category."""
        categories = ['core', 'development', 'testing', 'security']
        
        for category in categories:
            result = await server_full._list_commands(category=category)
            
            # Should contain commands from this category
            assert f"/{category}-command-0" in result
            assert f"/{category}-command-1" in result
            
            # Should not contain commands from other categories
            other_categories = [c for c in categories if c != category]
            for other in other_categories:
                assert f"/{other}-command-0" not in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])