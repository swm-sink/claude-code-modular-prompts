# Claude Code MCP Server Integration Guide

This guide explains how to set up and use the Model Context Protocol (MCP) server for Claude Code, making all commands and components discoverable and executable through Claude's interface.

## Overview

The Claude Code MCP server exposes the entire Claude Code framework through the Model Context Protocol, allowing you to:

- **Discover Commands**: Browse all 200+ available commands with descriptions and usage examples
- **Access Components**: View and understand the modular components that power commands
- **Execute Commands**: Run Claude Code commands with proper argument handling
- **Resource Management**: Efficiently access and cache command metadata and content

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

The MCP dependencies included are:
- `mcp>=1.0.0` - Core MCP protocol implementation
- `anyio>=4.0.0` - Async I/O support
- `pydantic>=2.0.0` - Data validation and settings

### 2. Configure Claude Desktop

The MCP server is already configured in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "claude-code-mcp": {
      "command": "python3",
      "args": ["start_mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/claude-code-modular-prompts/tallinn"
      }
    }
  }
}
```

### 3. Generate Simplified Commands (Optional)

The server automatically creates simplified commands on startup, but you can manually generate them:

```bash
python3 scripts/simplify_commands.py --priority-only
```

## Server Architecture

### Core Components

1. **`mcp_server.py`** - Main MCP server implementation
2. **`start_mcp_server.py`** - Server startup script with configuration
3. **`mcp_config.json`** - Server configuration and settings
4. **`.claude/commands/`** - Human-readable command versions

### Resource Discovery

The server automatically discovers resources from:

- **Commands**: `claude_prompt_factory/commands/` - All XML-based commands
- **Components**: `claude_prompt_factory/components/` - Reusable components
- **Simplified**: `.claude/commands/` - Human-readable versions

### URI Scheme

Resources are exposed using a custom URI scheme:

- `claude-code://commands/core/task.md` - Original XML commands
- `claude-code://components/validation/input-validation.md` - Components
- `claude-code://simplified/core/task.md` - Simplified versions

## Usage

### Starting the Server

#### Basic Usage
```bash
python3 start_mcp_server.py
```

#### Development Mode
```bash
python3 start_mcp_server.py --dev --log-level DEBUG
```

#### Custom Configuration
```bash
python3 start_mcp_server.py --project-root /path/to/project --no-simplify
```

### Available Tools

The MCP server provides three main tools:

#### 1. Execute Command
Execute any Claude Code command with arguments:
```json
{
  "tool": "execute_command",
  "arguments": {
    "command": "task",
    "arguments": {
      "task_description": "Create a user authentication system"
    }
  }
}
```

#### 2. List Commands  
Get a list of available commands:
```json
{
  "tool": "list_commands",
  "arguments": {
    "category": "core"  // Optional filter
  }
}
```

#### 3. Get Command Info
Get detailed information about a specific command:
```json
{
  "tool": "get_command_info", 
  "arguments": {
    "command": "task"
  }
}
```

## Resource Categories

The server organizes resources into logical categories:

### Core Commands
- **task** - TDD development workflow
- **query** - Information querying and analysis  
- **auto** - Automated workflow execution
- **research** - Research and analysis framework

### Development Commands
- **feature** - Feature development workflow
- **debug** - Debugging and troubleshooting
- **dev-test** - Development testing

### Git Commands  
- **git-commit** - Smart git commit with analysis
- **git-merge** - Automated merge conflict resolution
- **git-pr** - Pull request creation and management

### Testing Commands
- **test-coverage** - Test coverage analysis
- **test-unit** - Unit testing framework
- **test-integration** - Integration testing

### Security Commands
- **secure-audit** - Security auditing
- **secure-scan** - Vulnerability scanning
- **secure-fix** - Security issue remediation

### Performance Commands
- **perf-optimize** - Performance optimization
- **perf-benchmark** - Performance benchmarking
- **perf-monitor** - Performance monitoring

## Configuration

### Server Configuration (`mcp_config.json`)

Key configuration options:

```json
{
  "resources": {
    "cache_refresh_interval": 300,  // 5 minutes
    "max_resources_per_category": 1000
  },
  "logging": {
    "level": "INFO",
    "file": "mcp_server.log"
  },
  "features": {
    "auto_create_simplified_commands": true,
    "command_execution": true,
    "resource_caching": true
  }
}
```

### Environment Variables

- `PYTHONPATH` - Set to project root directory
- `MCP_LOG_LEVEL` - Override logging level
- `MCP_PROJECT_ROOT` - Override project root path

## Monitoring and Logs

### Log Files
- `mcp_server.log` - Main server log file
- Logs are rotated when they exceed 10MB
- 5 backup files are maintained

### Server Status
The server provides detailed startup information:
```
🚀 Claude Code MCP Server
==========================================
📁 Project Root: /path/to/project
📊 Log Level: INFO
📋 Commands Available: 150
🧩 Components Available: 75
⚡ Simplified Commands: 10
==========================================
```

## Troubleshooting

### Common Issues

#### 1. MCP Dependencies Not Found
```bash
pip install mcp anyio pydantic
```

#### 2. Project Structure Invalid
Ensure these directories exist:
- `claude_prompt_factory/commands/`
- `claude_prompt_factory/components/`

#### 3. Permission Issues
Make sure the server script is executable:
```bash
chmod +x start_mcp_server.py
```

#### 4. Resource Discovery Issues
Check the log file for detailed error messages:
```bash
tail -f mcp_server.log
```

### Debug Mode
Start in debug mode for detailed logging:
```bash
python3 start_mcp_server.py --dev
```

## Integration with Claude

Once the server is running and configured:

1. **Restart Claude Desktop** to load the new MCP server
2. **Browse Resources** using Claude's resource browser
3. **Execute Commands** through Claude's tool interface
4. **View Documentation** by accessing resource URIs

## Advanced Usage

### Custom Resource Filters
The server supports filtering resources by category, type, and other metadata.

### Command Execution
Commands can be executed with full argument validation and error handling.

### Metadata Extraction
The server automatically extracts and presents command metadata including:
- Usage examples
- Argument descriptions
- Dependencies
- Component relationships

## Performance Considerations

- **Resource Caching**: Resources are cached for 5 minutes to improve performance
- **Lazy Loading**: Components are loaded only when accessed
- **Memory Management**: Server manages memory usage for large command sets

## Security

- **Input Validation**: All inputs are validated before processing
- **Safe Execution**: Command execution includes proper error handling
- **Resource Access**: Only project resources are exposed through the server

## Contributing

To extend the MCP server:

1. Add new tools in the `_setup_handlers()` method
2. Implement resource discovery for new resource types
3. Update the configuration schema as needed
4. Add comprehensive logging for new features

## Support

For issues with the MCP server:

1. Check the server logs: `mcp_server.log`
2. Run in debug mode: `--dev --log-level DEBUG`
3. Validate project structure and dependencies
4. Review the configuration file: `mcp_config.json`

---

The Claude Code MCP Server provides a powerful interface to the entire Claude Code framework, making it easy to discover, understand, and execute commands through Claude's native interface.