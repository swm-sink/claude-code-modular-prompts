#!/usr/bin/env python3
"""
Mock Tool Environment for Claude Code Functional Testing

This module provides a safe, controlled environment for testing Claude Code commands
without executing actual file system operations or external tool calls.
"""

import json
import os
import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union
from unittest.mock import Mock


@dataclass
class MockFile:
    """Represents a file in the mock file system."""
    content: str
    permissions: str = "rw-r--r--"
    size: int = 0
    last_modified: float = 0.0
    
    def __post_init__(self):
        if self.size == 0:
            self.size = len(self.content.encode('utf-8'))


@dataclass
class MockToolResult:
    """Standard result structure for mock tool operations."""
    success: bool
    output: str
    error: str = ""
    tool_used: str = ""
    execution_time_ms: float = 0.0
    resources_used: Dict[str, Any] = field(default_factory=dict)


class MockFileSystem:
    """
    Mock file system for testing Read, Write, Edit operations safely.
    
    Provides a controlled environment that simulates file operations
    without touching the actual file system.
    """
    
    def __init__(self):
        self.files: Dict[str, MockFile] = {}
        self.directories: Set[str] = {"/", "/tmp", "/home", "/usr"}
        self.current_directory = "/"
        self.permissions = {}
        self.operation_log: List[Dict[str, Any]] = []
    
    def _log_operation(self, operation: str, path: str, **kwargs):
        """Log all file system operations for testing validation."""
        self.operation_log.append({
            "operation": operation,
            "path": path,
            "timestamp": len(self.operation_log),
            **kwargs
        })
    
    def _normalize_path(self, path: str) -> str:
        """Normalize file paths for consistent handling."""
        if not path.startswith('/'):
            path = os.path.join(self.current_directory, path)
        return os.path.normpath(path)
    
    def _ensure_directory_exists(self, file_path: str):
        """Ensure parent directories exist for a file path."""
        dir_path = os.path.dirname(file_path)
        if dir_path and dir_path not in self.directories:
            self.directories.add(dir_path)
    
    def read_file(self, path: str, offset: int = 0, limit: Optional[int] = None) -> MockToolResult:
        """Simulate Read tool functionality."""
        normalized_path = self._normalize_path(path)
        self._log_operation("read", normalized_path, offset=offset, limit=limit)
        
        if normalized_path not in self.files:
            return MockToolResult(
                success=False,
                output="",
                error=f"File not found: {path}",
                tool_used="Read"
            )
        
        content = self.files[normalized_path].content
        lines = content.split('\n')
        
        if offset > 0:
            lines = lines[offset:]
        if limit is not None:
            lines = lines[:limit]
        
        result_content = '\n'.join(lines)
        
        return MockToolResult(
            success=True,
            output=result_content,
            tool_used="Read",
            resources_used={"bytes_read": len(result_content)}
        )
    
    def write_file(self, path: str, content: str) -> MockToolResult:
        """Simulate Write tool functionality."""
        normalized_path = self._normalize_path(path)
        self._log_operation("write", normalized_path, content_length=len(content))
        
        self._ensure_directory_exists(normalized_path)
        self.files[normalized_path] = MockFile(content=content)
        
        return MockToolResult(
            success=True,
            output=f"File written successfully: {path}",
            tool_used="Write",
            resources_used={"bytes_written": len(content)}
        )
    
    def edit_file(self, path: str, old_string: str, new_string: str, replace_all: bool = False) -> MockToolResult:
        """Simulate Edit tool functionality."""
        normalized_path = self._normalize_path(path)
        self._log_operation("edit", normalized_path, old_string=old_string, new_string=new_string, replace_all=replace_all)
        
        if normalized_path not in self.files:
            return MockToolResult(
                success=False,
                output="",
                error=f"File not found: {path}",
                tool_used="Edit"
            )
        
        current_content = self.files[normalized_path].content
        
        if replace_all:
            new_content = current_content.replace(old_string, new_string)
            replacements = current_content.count(old_string)
        else:
            if old_string not in current_content:
                return MockToolResult(
                    success=False,
                    output="",
                    error=f"String not found in file: {old_string}",
                    tool_used="Edit"
                )
            
            new_content = current_content.replace(old_string, new_string, 1)
            replacements = 1
        
        self.files[normalized_path].content = new_content
        
        return MockToolResult(
            success=True,
            output=f"File edited successfully. Made {replacements} replacement(s).",
            tool_used="Edit",
            resources_used={"replacements_made": replacements}
        )
    
    def list_directory(self, path: str) -> MockToolResult:
        """Simulate LS tool functionality."""
        normalized_path = self._normalize_path(path)
        self._log_operation("list", normalized_path)
        
        if normalized_path not in self.directories:
            return MockToolResult(
                success=False,
                output="",
                error=f"Directory not found: {path}",
                tool_used="LS"
            )
        
        # Find files and subdirectories in the specified path
        contents = []
        for file_path in self.files:
            if file_path.startswith(normalized_path + "/") and file_path != normalized_path:
                relative_path = file_path[len(normalized_path):].lstrip("/")
                if "/" not in relative_path:  # Direct child, not nested
                    contents.append(relative_path)
        
        for dir_path in self.directories:
            if dir_path.startswith(normalized_path + "/") and dir_path != normalized_path:
                relative_path = dir_path[len(normalized_path):].lstrip("/")
                if "/" not in relative_path:  # Direct child, not nested
                    contents.append(relative_path + "/")
        
        return MockToolResult(
            success=True,
            output="\n".join(sorted(contents)),
            tool_used="LS",
            resources_used={"items_listed": len(contents)}
        )


class MockBashEnvironment:
    """
    Mock bash environment for testing Bash tool operations safely.
    
    Provides controlled command execution without affecting the host system.
    """
    
    def __init__(self, file_system: MockFileSystem):
        self.file_system = file_system
        self.environment_vars = {"HOME": "/home", "USER": "testuser", "PATH": "/usr/bin:/bin"}
        self.command_history: List[Dict[str, Any]] = []
        self.exit_code = 0
    
    def _log_command(self, command: str, result: MockToolResult):
        """Log executed commands for testing validation."""
        self.command_history.append({
            "command": command,
            "result": result,
            "timestamp": len(self.command_history)
        })
    
    def execute_command(self, command: str, timeout: int = 120000) -> MockToolResult:
        """Simulate Bash tool functionality with safe command execution."""
        # Basic command parsing and simulation
        command = command.strip()
        
        # Simulate common commands safely
        if command.startswith("echo "):
            output = command[5:].strip('"\'')
            result = MockToolResult(
                success=True,
                output=output,
                tool_used="Bash",
                execution_time_ms=1.0
            )
        
        elif command.startswith("ls "):
            path = command[3:].strip()
            result = self.file_system.list_directory(path)
            result.tool_used = "Bash"
        
        elif command.startswith("pwd"):
            result = MockToolResult(
                success=True,
                output=self.file_system.current_directory,
                tool_used="Bash",
                execution_time_ms=0.5
            )
        
        elif command.startswith("cd "):
            path = command[3:].strip()
            normalized_path = self.file_system._normalize_path(path)
            if normalized_path in self.file_system.directories:
                self.file_system.current_directory = normalized_path
                result = MockToolResult(
                    success=True,
                    output="",
                    tool_used="Bash",
                    execution_time_ms=0.5
                )
            else:
                result = MockToolResult(
                    success=False,
                    output="",
                    error=f"Directory not found: {path}",
                    tool_used="Bash"
                )
        
        elif command.startswith("cat "):
            path = command[4:].strip()
            result = self.file_system.read_file(path)
            result.tool_used = "Bash"
        
        else:
            # For unimplemented commands, return a safe default
            result = MockToolResult(
                success=True,
                output=f"Simulated output for: {command}",
                tool_used="Bash",
                execution_time_ms=10.0
            )
        
        self._log_command(command, result)
        return result


class MockSearchTools:
    """
    Mock search tools for testing Grep and Glob operations safely.
    
    Provides pattern matching and search functionality without file system access.
    """
    
    def __init__(self, file_system: MockFileSystem):
        self.file_system = file_system
        self.search_history: List[Dict[str, Any]] = []
    
    def _log_search(self, operation: str, pattern: str, result: MockToolResult):
        """Log search operations for testing validation."""
        self.search_history.append({
            "operation": operation,
            "pattern": pattern,
            "result": result,
            "timestamp": len(self.search_history)
        })
    
    def grep_search(self, pattern: str, path: str = ".", case_insensitive: bool = False, 
                   line_numbers: bool = False, context_before: int = 0, 
                   context_after: int = 0) -> MockToolResult:
        """Simulate Grep tool functionality."""
        search_files = []
        
        if path in self.file_system.files:
            search_files = [path]
        else:
            # Search in all files if directory specified
            for file_path in self.file_system.files:
                if file_path.startswith(path):
                    search_files.append(file_path)
        
        matches = []
        flags = re.IGNORECASE if case_insensitive else 0
        
        for file_path in search_files:
            content = self.file_system.files[file_path].content
            lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                if re.search(pattern, line, flags):
                    if line_numbers:
                        match_text = f"{file_path}:{line_num}:{line}"
                    else:
                        match_text = f"{file_path}:{line}"
                    matches.append(match_text)
        
        result = MockToolResult(
            success=True,
            output="\n".join(matches) if matches else "",
            tool_used="Grep",
            resources_used={"files_searched": len(search_files), "matches_found": len(matches)}
        )
        
        self._log_search("grep", pattern, result)
        return result
    
    def glob_search(self, pattern: str, path: str = ".") -> MockToolResult:
        """Simulate Glob tool functionality."""
        import fnmatch
        
        matching_files = []
        
        for file_path in self.file_system.files:
            if file_path.startswith(path):
                relative_path = file_path[len(path):].lstrip("/")
                if fnmatch.fnmatch(relative_path, pattern) or fnmatch.fnmatch(file_path, pattern):
                    matching_files.append(file_path)
        
        result = MockToolResult(
            success=True,
            output="\n".join(sorted(matching_files)),
            tool_used="Glob",
            resources_used={"files_matched": len(matching_files)}
        )
        
        self._log_search("glob", pattern, result)
        return result


class MockToolEnvironment:
    """
    Comprehensive mock environment for all Claude Code tools.
    
    Coordinates between different mock tools and provides a unified interface
    for functional testing of Claude Code commands.
    """
    
    def __init__(self):
        self.file_system = MockFileSystem()
        self.bash_environment = MockBashEnvironment(self.file_system)
        self.search_tools = MockSearchTools(self.file_system)
        self.tool_call_log: List[Dict[str, Any]] = []
        
        # Initialize with some default files for testing
        self._setup_default_environment()
    
    def _setup_default_environment(self):
        """Set up a basic file system structure for testing."""
        # Create some default directories and files
        self.file_system.directories.update([
            "/project",
            "/project/src",
            "/project/tests",
            "/project/docs"
        ])
        
        # Add some sample files
        sample_files = {
            "/project/README.md": "# Sample Project\n\nThis is a test project for Claude Code testing.",
            "/project/src/main.py": "def hello():\n    print('Hello, World!')\n\nif __name__ == '__main__':\n    hello()",
            "/project/tests/test_main.py": "import unittest\nfrom src.main import hello\n\nclass TestMain(unittest.TestCase):\n    pass",
            "/project/.gitignore": "*.pyc\n__pycache__/\n.venv/",
        }
        
        for path, content in sample_files.items():
            self.file_system.files[path] = MockFile(content=content)
    
    def route_tool_call(self, tool_name: str, **kwargs) -> MockToolResult:
        """
        Route tool calls to appropriate mock implementations.
        
        This method intercepts Claude Code tool calls and routes them to
        the corresponding mock tool implementations.
        """
        tool_call = {
            "tool": tool_name,
            "args": kwargs,
            "timestamp": len(self.tool_call_log)
        }
        
        try:
            if tool_name == "Read":
                result = self.file_system.read_file(
                    kwargs.get("file_path", ""),
                    kwargs.get("offset", 0),
                    kwargs.get("limit")
                )
            
            elif tool_name == "Write":
                result = self.file_system.write_file(
                    kwargs.get("file_path", ""),
                    kwargs.get("content", "")
                )
            
            elif tool_name == "Edit":
                result = self.file_system.edit_file(
                    kwargs.get("file_path", ""),
                    kwargs.get("old_string", ""),
                    kwargs.get("new_string", ""),
                    kwargs.get("replace_all", False)
                )
            
            elif tool_name == "LS":
                result = self.file_system.list_directory(
                    kwargs.get("path", ".")
                )
            
            elif tool_name == "Bash":
                result = self.bash_environment.execute_command(
                    kwargs.get("command", ""),
                    kwargs.get("timeout", 120000)
                )
            
            elif tool_name == "Grep":
                result = self.search_tools.grep_search(
                    kwargs.get("pattern", ""),
                    kwargs.get("path", "."),
                    kwargs.get("case_insensitive", False),
                    kwargs.get("line_numbers", False),
                    kwargs.get("context_before", 0),
                    kwargs.get("context_after", 0)
                )
            
            elif tool_name == "Glob":
                result = self.search_tools.glob_search(
                    kwargs.get("pattern", ""),
                    kwargs.get("path", ".")
                )
            
            else:
                result = MockToolResult(
                    success=False,
                    output="",
                    error=f"Unknown tool: {tool_name}",
                    tool_used=tool_name
                )
            
            tool_call["result"] = result
            
        except Exception as e:
            result = MockToolResult(
                success=False,
                output="",
                error=f"Tool execution error: {str(e)}",
                tool_used=tool_name
            )
            tool_call["result"] = result
        
        self.tool_call_log.append(tool_call)
        return result
    
    def get_execution_summary(self) -> Dict[str, Any]:
        """Get a summary of all tool executions for analysis."""
        return {
            "total_tool_calls": len(self.tool_call_log),
            "tools_used": list(set(call["tool"] for call in self.tool_call_log)),
            "successful_calls": len([call for call in self.tool_call_log if call["result"].success]),
            "failed_calls": len([call for call in self.tool_call_log if not call["result"].success]),
            "file_operations": len(self.file_system.operation_log),
            "commands_executed": len(self.bash_environment.command_history),
            "searches_performed": len(self.search_tools.search_history),
        }
    
    def reset_environment(self):
        """Reset the mock environment to its initial state."""
        self.__init__()
    
    def export_state(self) -> Dict[str, Any]:
        """Export the current state for debugging and analysis."""
        return {
            "files": {path: file.content for path, file in self.file_system.files.items()},
            "directories": list(self.file_system.directories),
            "tool_calls": self.tool_call_log,
            "execution_summary": self.get_execution_summary()
        }


# Test utility functions

def create_test_environment() -> MockToolEnvironment:
    """Create a fresh mock environment for testing."""
    return MockToolEnvironment()


def validate_tool_usage(environment: MockToolEnvironment, expected_tools: List[str]) -> bool:
    """Validate that the expected tools were used during command execution."""
    actual_tools = environment.get_execution_summary()["tools_used"]
    return all(tool in actual_tools for tool in expected_tools)


def assert_file_operations(environment: MockToolEnvironment, expected_operations: List[str]) -> bool:
    """Assert that specific file operations were performed."""
    operations = [op["operation"] for op in environment.file_system.operation_log]
    return all(op in operations for op in expected_operations)


if __name__ == "__main__":
    # Example usage and basic testing
    env = create_test_environment()
    
    # Test file operations
    print("Testing file operations...")
    result = env.route_tool_call("Read", file_path="/project/README.md")
    print(f"Read result: {result.success}, Output length: {len(result.output)}")
    
    result = env.route_tool_call("Write", file_path="/project/test.txt", content="Test content")
    print(f"Write result: {result.success}")
    
    result = env.route_tool_call("Edit", file_path="/project/test.txt", old_string="Test", new_string="Modified")
    print(f"Edit result: {result.success}")
    
    # Test search operations
    result = env.route_tool_call("Grep", pattern="Hello", path="/project")
    print(f"Grep result: {result.success}, Matches: {len(result.output.split('\n')) if result.output else 0}")
    
    # Print execution summary
    summary = env.get_execution_summary()
    print(f"\nExecution Summary: {summary}")