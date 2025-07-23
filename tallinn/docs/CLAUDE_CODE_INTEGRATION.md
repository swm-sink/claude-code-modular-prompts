# Claude Code Integration Guide

## Overview

The Claude Code Modular Prompts Framework provides native integration with Claude Code through the Model Context Protocol (MCP). This guide covers setup, configuration, and usage of the framework within Claude Code.

## Prerequisites

- Claude Code desktop application installed
- Python 3.8+ for MCP server
- Framework cloned and dependencies installed

## Setup Instructions

### 1. Install Dependencies

```bash
cd claude-code-modular-prompts/tallinn
pip install -r requirements.txt
```

### 2. Configure MCP Server

```bash
# Make setup script executable
chmod +x setup_mcp.sh

# Run setup (creates MCP configuration)
./setup_mcp.sh
```

### 3. Start MCP Server

```bash
# Start the MCP server
python start_mcp_server.py

# Or start manually
python mcp_server.py
```

## Command Usage

### Available Commands

All 146+ commands are available as slash commands in Claude Code:

#### Core Commands
- `/auto` - Intelligent command routing
- `/query` - Codebase analysis and understanding
- `/task` - Focused development tasks
- `/feature` - Complete feature development

#### Development Commands
- `/debug` - Debugging and troubleshooting
- `/dev-test` - Development testing workflows
- `/dev-refactor` - Code refactoring tasks

#### Security Commands
- `/secure-audit` - Security auditing
- `/secure-scan` - Security scanning
- `/secure-fix` - Security issue fixing

#### Performance Commands
- `/perf-optimize` - Performance optimization
- `/perf-monitor` - Performance monitoring
- `/perf-benchmark` - Performance benchmarking

### Command Structure

All commands follow this structure:

```markdown
---
name: /command-name
description: Brief description
usage: /command-name [arguments]
tools: Read, Write, Edit, Grep, Glob, Bash
---

# Command implementation
```

### Usage Examples

```bash
# Intelligent routing
/auto "analyze the authentication system"

# Code analysis
/query "how does user authentication work?"

# Focused task
/task "fix password validation bug"

# Feature development
/feature "user profile management system"

# Security audit
/secure-audit "analyze security vulnerabilities"

# Performance optimization
/perf-optimize "optimize database queries"
```

## MCP Configuration

### Configuration Files

- `mcp_config.json` - MCP server configuration
- `claude_desktop_config.json` - Claude Code integration settings
- `settings.local.json` - Local development settings

### Server Configuration

The MCP server runs on localhost with configurable port (default 8000):

```json
{
  "server": {
    "host": "localhost",
    "port": 8000
  },
  "commands_path": ".claude/commands/",
  "max_concurrent": 10
}
```

## Directory Structure

```
tallinn/
├── .claude/
│   └── commands/          # 146+ markdown commands
├── mcp_server.py          # MCP server implementation
├── start_mcp_server.py    # Server startup script
├── setup_mcp.sh          # Setup script
├── mcp_config.json       # MCP configuration
└── docs/                 # Documentation
```

## Troubleshooting

### Common Issues

**Commands Not Available**
- Ensure MCP server is running
- Check `.claude/commands/` directory exists
- Verify YAML frontmatter in command files

**Connection Errors**
- Check MCP server port (default 8000)
- Verify firewall settings
- Ensure Python dependencies installed

**Permission Errors**
- Run `chmod +x setup_mcp.sh`
- Check file permissions in `.claude/commands/`
- Verify Python environment

### Debugging

```bash
# Check MCP server status
curl http://localhost:8000/health

# View server logs
python start_mcp_server.py --debug

# Test command availability
python -c "import mcp_server; print(mcp_server.list_commands())"
```

## Development

### Adding New Commands

1. Create command file in `.claude/commands/{category}/`
2. Use YAML frontmatter format
3. Test with MCP server
4. Restart server to reload commands

### Command Template

```markdown
---
name: /your-command
description: Your command description
usage: /your-command [arguments]
tools: Read, Write, Edit, Grep, Glob
---

# Your Command

**Usage**: `/your-command $ARGUMENTS`

## Key Arguments
- **$ARGUMENT1** (required): Description

## Examples
```bash
/your-command "example usage"
```

## Core Logic
[Your command implementation]
```

### Best Practices

- Keep commands focused and concise
- Use clear argument descriptions
- Provide usage examples
- Follow naming conventions
- Test thoroughly before deployment

## Security Considerations

- MCP server runs locally only
- No external network access required
- Commands have access to local filesystem
- Review command implementations before use
- Use security auditing tools regularly

## Performance

- Current test coverage: ~19%
- 146+ commands available
- MCP server handles up to 10 concurrent requests
- Command execution depends on individual implementations

---

*For more information, see the [Complete User Guide](COMPLETE_USER_GUIDE.md) and [Getting Started Guide](GETTING_STARTED.md).*