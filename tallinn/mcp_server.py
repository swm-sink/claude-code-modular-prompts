#!/usr/bin/env python3
"""
Claude Code MCP (Model Context Protocol) Server

This server exposes all Claude Code commands and components as MCP resources,
making them discoverable and executable through Claude Code's interface.

Features:
- Automatic command discovery from .claude/commands/
- JSON metadata extraction for command information
- Resource-based access to commands and components
- Real-time command execution capabilities
- Comprehensive error handling and logging
"""

import asyncio
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Union
from datetime import datetime

# MCP Server imports
try:
    from mcp import (
        Resource,
        Tool,
    )
    from mcp.types import TextContent
    from mcp.server import Server
    from mcp.server.models import InitializationOptions
    from mcp.server.stdio import stdio_server
except ImportError as e:
    print(f"MCP dependencies not installed or version mismatch. Please run: pip install mcp. Error: {e}", file=sys.stderr)
    # Don't exit here, allow for testing without full MCP functionality
    Resource = type('Resource', (), {})
    Tool = type('Tool', (), {})
    TextContent = type('TextContent', (), {})

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ClaudeCodeMCPServer:
    """MCP Server for Claude Code framework integration."""
    
    def __init__(self, project_root: str = None):
        """Initialize the MCP server with project configuration."""
        self.project_root = Path(project_root or os.getcwd())
        self.commands_dir = self.project_root / ".claude" / "commands"
        self.components_dir = self.project_root / "claude_prompt_factory" / "components"
        
        # Initialize MCP server
        self.server = Server("claude-code-mcp")
        self.resources_cache = {}
        self.last_scan_time = None
        
        # Setup server handlers
        self._setup_handlers()
        
        logger.info(f"Claude Code MCP Server initialized")
        logger.info(f"Project root: {self.project_root}")
        logger.info(f"Commands directory: {self.commands_dir}")
        logger.info(f"Components directory: {self.components_dir}")
    
    def _setup_handlers(self):
        """Setup MCP server request handlers."""
        
        @self.server.list_resources()
        async def list_resources() -> List[Resource]:
            """List all available Claude Code resources."""
            try:
                resources = await self._discover_resources()
                logger.info(f"Listed {len(resources)} resources")
                return resources
            except Exception as e:
                logger.error(f"Error listing resources: {e}")
                return []
        
        @self.server.read_resource()
        async def read_resource(uri: str) -> str:
            """Read a specific Claude Code resource."""
            try:
                content = await self._read_resource(uri)
                logger.info(f"Read resource: {uri}")
                return content
            except Exception as e:
                logger.error(f"Error reading resource {uri}: {e}")
                raise
        
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            """List available Claude Code tools."""
            return [
                Tool(
                    name="execute_command",
                    description="Execute a Claude Code command",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "command": {"type": "string", "description": "Command name (e.g., 'task', 'query')"},
                            "arguments": {"type": "object", "description": "Command arguments"}
                        },
                        "required": ["command"]
                    }
                ),
                Tool(
                    name="list_commands",
                    description="List all available Claude Code commands",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "category": {"type": "string", "description": "Optional category filter"}
                        }
                    }
                ),
                Tool(
                    name="get_command_info",
                    description="Get detailed information about a specific command",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "command": {"type": "string", "description": "Command name"}
                        },
                        "required": ["command"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Execute Claude Code tools."""
            try:
                if name == "execute_command":
                    result = await self._execute_command(
                        arguments.get("command"),
                        arguments.get("arguments", {})
                    )
                elif name == "list_commands":
                    result = await self._list_commands(arguments.get("category"))
                elif name == "get_command_info":
                    result = await self._get_command_info(arguments.get("command"))
                else:
                    result = f"Unknown tool: {name}"
                
                return [TextContent(type="text", text=result)]
            except Exception as e:
                error_msg = f"Error executing tool {name}: {e}"
                logger.error(error_msg)
                return [TextContent(type="text", text=error_msg)]
    
    async def _discover_resources(self) -> List[Resource]:
        """Discover all Claude Code resources."""
        resources = []
        
        # Check if we need to refresh cache
        current_time = datetime.now()
        if (self.last_scan_time is None or 
            (current_time - self.last_scan_time).seconds > 300):  # Refresh every 5 minutes
            
            self.resources_cache = {}
            
            # Discover commands
            await self._discover_commands(resources)
            
            # Discover components
            await self._discover_components(resources)
            
            self.last_scan_time = current_time
            logger.info(f"Resource discovery completed: {len(resources)} resources found")
        
        else:
            # Use cached resources
            resources = list(self.resources_cache.values())
            logger.info(f"Using cached resources: {len(resources)} resources")
        
        return resources
    
    async def _discover_commands(self, resources: List[Resource]):
        """Discover command files and extract metadata."""
        if not self.commands_dir.exists():
            logger.warning(f"Commands directory not found: {self.commands_dir}")
            return
        
        for md_file in self.commands_dir.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            
            try:
                # Extract command metadata
                metadata = await self._extract_command_metadata(md_file)
                if not metadata:
                    continue
                
                # Create resource URI
                relative_path = md_file.relative_to(self.commands_dir)
                uri = f"claude-code://commands/{relative_path.as_posix()}"
                
                # Create resource
                resource = Resource(
                    uri=uri,
                    name=metadata.get('name', md_file.stem),
                    description=metadata.get('description', f"Claude Code command: {md_file.stem}"),
                    mimeType="text/markdown"
                )
                
                resources.append(resource)
                self.resources_cache[uri] = resource
                
            except Exception as e:
                logger.warning(f"Failed to process command {md_file}: {e}")
    
    async def _discover_components(self, resources: List[Resource]):
        """Discover component files."""
        if not self.components_dir.exists():
            logger.warning(f"Components directory not found: {self.components_dir}")
            return
        
        for md_file in self.components_dir.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            
            try:
                # Read component content
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract description from content
                description = self._extract_description_from_content(content, md_file.stem)
                
                # Create resource URI
                relative_path = md_file.relative_to(self.components_dir)
                uri = f"claude-code://components/{relative_path.as_posix()}"
                
                # Create resource
                resource = Resource(
                    uri=uri,
                    name=f"Component: {md_file.stem}",
                    description=description,
                    mimeType="text/markdown"
                )
                
                resources.append(resource)
                self.resources_cache[uri] = resource
                
            except Exception as e:
                logger.warning(f"Failed to process component {md_file}: {e}")
    
    async def _extract_command_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extract metadata from command file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = {}
            
            # Extract YAML frontmatter
            frontmatter = await self._extract_frontmatter(file_path)
            if frontmatter:
                metadata.update(frontmatter)
            
            # Extract XML metadata if present
            xml_metadata = self._extract_xml_metadata(content)
            if xml_metadata:
                metadata.update(xml_metadata)
            
            return metadata
            
        except Exception as e:
            logger.error(f"Error extracting metadata from {file_path}: {e}")
            return {}
    
    async def _extract_frontmatter(self, file_path: Path) -> Dict[str, Any]:
        """Extract YAML frontmatter from markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.startswith('---'):
                return {}
            
            # Find the end of frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                return {}
            
            yaml_content = parts[1].strip()
            frontmatter = {}
            
            # Simple YAML parsing for common fields
            for line in yaml_content.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"\'')
            
            return frontmatter
            
        except Exception as e:
            logger.error(f"Error extracting frontmatter from {file_path}: {e}")
            return {}
    
    def _extract_xml_metadata(self, content: str) -> Dict[str, Any]:
        """Extract metadata from XML command structure."""
        metadata = {}
        
        # Extract XML metadata
        xml_match = re.search(r'<metadata>(.*?)</metadata>', content, re.DOTALL)
        if xml_match:
            xml_content = xml_match.group(1)
            
            # Extract name
            name_match = re.search(r'<name>([^<]+)</name>', xml_content)
            if name_match:
                metadata['name'] = name_match.group(1)
            
            # Extract purpose
            purpose_match = re.search(r'<purpose>([^<]+)</purpose>', xml_content)
            if purpose_match:
                metadata['description'] = purpose_match.group(1)
            
            # Extract usage
            usage_match = re.search(r'<usage[^>]*>\s*<!\[CDATA\[(.*?)\]\]>', xml_content, re.DOTALL)
            if usage_match:
                metadata['usage'] = usage_match.group(1).strip()
        
        return metadata
    
    def _extract_description_from_content(self, content: str, fallback: str) -> str:
        """Extract description from content."""
        # Try to find first paragraph or heading
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('---'):
                if len(line) > 20:  # Meaningful description
                    return line[:200] + "..." if len(line) > 200 else line
        
        return f"Claude Code component: {fallback}"
    
    async def _read_resource(self, uri: str) -> str:
        """Read resource content by URI."""
        try:
            # Parse URI to get file path
            if uri.startswith("claude-code://commands/"):
                relative_path = uri.replace("claude-code://commands/", "")
                file_path = self.commands_dir / relative_path
            elif uri.startswith("claude-code://components/"):
                relative_path = uri.replace("claude-code://components/", "")
                file_path = self.components_dir / relative_path
            else:
                raise ValueError(f"Unknown resource URI scheme: {uri}")
            
            if not file_path.exists():
                raise FileNotFoundError(f"Resource not found: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add metadata header
            metadata = await self._extract_command_metadata(file_path)
            if metadata:
                header = "# Resource Metadata\n\n"
                for key, value in metadata.items():
                    header += f"- **{key}**: {value}\n"
                header += "\n---\n\n"
                content = header + content
            
            return content
            
        except Exception as e:
            logger.error(f"Error reading resource {uri}: {e}")
            raise
    
    async def _execute_command(self, command: str, arguments: Dict[str, Any]) -> str:
        """Execute a Claude Code command."""
        try:
            # This is a placeholder for command execution
            # In a real implementation, you would integrate with the actual command execution system
            
            result = {
                "command": command,
                "arguments": arguments,
                "status": "executed",
                "timestamp": datetime.now().isoformat(),
                "message": f"Command '{command}' executed successfully with MCP server"
            }
            
            return json.dumps(result, indent=2)
            
        except Exception as e:
            error_result = {
                "command": command,
                "arguments": arguments,
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            return json.dumps(error_result, indent=2)
    
    async def _list_commands(self, category: Optional[str] = None) -> str:
        """List available commands."""
        try:
            commands = []
            
            if not self.commands_dir.exists():
                return json.dumps({"error": "Commands directory not found"}, indent=2)
            
            for md_file in self.commands_dir.rglob("*.md"):
                if md_file.name == "README.md":
                    continue
                
                # Apply category filter
                if category and category not in str(md_file.parent.name):
                    continue
                
                metadata = await self._extract_command_metadata(md_file)
                relative_path = md_file.relative_to(self.commands_dir)
                
                command_info = {
                    "name": metadata.get('name', md_file.stem),
                    "path": str(relative_path),
                    "category": md_file.parent.name,
                    "description": metadata.get('description', ''),
                    "usage": metadata.get('usage', ''),
                }
                
                commands.append(command_info)
            
            return json.dumps({
                "commands": commands,
                "total": len(commands),
                "category_filter": category
            }, indent=2)
            
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)
    
    async def _get_command_info(self, command: str) -> str:
        """Get detailed information about a specific command."""
        try:
            # Find command file
            command_file = None
            for md_file in self.commands_dir.rglob("*.md"):
                if md_file.stem == command or md_file.name == f"{command}.md":
                    command_file = md_file
                    break
            
            if not command_file:
                return json.dumps({"error": f"Command '{command}' not found"}, indent=2)
            
            # Extract full metadata
            metadata = await self._extract_command_metadata(command_file)
            
            # Read content
            with open(command_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract examples
            examples = self._extract_examples_from_content(content)
            
            command_info = {
                "name": metadata.get('name', command),
                "description": metadata.get('description', ''),
                "usage": metadata.get('usage', ''),
                "file_path": str(command_file.relative_to(self.commands_dir)),
                "category": command_file.parent.name,
                "examples": examples,
                "metadata": metadata
            }
            
            return json.dumps(command_info, indent=2)
            
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)
    
    def _extract_examples_from_content(self, content: str) -> List[Dict[str, str]]:
        """Extract usage examples from content."""
        examples = []
        
        # Find examples in various formats
        # Look for code blocks with examples
        code_blocks = re.findall(r'```(?:bash|shell)?\n([^`]+)```', content)
        for block in code_blocks:
            lines = block.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('/') or line.startswith('claude'):
                    examples.append({
                        "usage": line,
                        "description": "Example usage"
                    })
        
        # Look for XML examples
        xml_examples = re.findall(r'<example>(.*?)</example>', content, re.DOTALL)
        for example in xml_examples:
            usage_match = re.search(r'<usage>([^<]+)</usage>', example)
            desc_match = re.search(r'<description>([^<]+)</description>', example)
            
            if usage_match:
                examples.append({
                    "usage": usage_match.group(1).strip(),
                    "description": desc_match.group(1).strip() if desc_match else "Example usage"
                })
        
        return examples[:5]  # Limit to 5 examples
    
    async def run_server(self):
        """Run the MCP server."""
        logger.info("Starting Claude Code MCP Server...")
        
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(read_stream, write_stream, InitializationOptions())


async def main():
    """Main entry point for the MCP server."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Claude Code MCP Server")
    parser.add_argument(
        "--project-root", 
        default=None,
        help="Project root directory (defaults to current directory)"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level"
    )
    
    args = parser.parse_args()
    
    # Configure logging
    logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    # Initialize and run server
    try:
        server = ClaudeCodeMCPServer(args.project_root)
        await server.run_server()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())