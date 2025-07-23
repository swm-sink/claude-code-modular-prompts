# Model Context Protocol (MCP) Documentation

## Overview

Model Context Protocol (MCP) is an open protocol that enables LLMs to access external tools and data sources in a secure, standardized way. It's designed specifically for LLM interactions, similar to web APIs but optimized for AI use cases.

## Official Resources

- **MCP Website**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Official Quickstart**: [modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server)
- **Python SDK**: [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
- **Server Collection**: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Core Concepts

### What MCP Provides

1. **Standardized Communication**: Protocol for LLM-to-tool interaction
2. **Security**: Built-in approval mechanisms for tool usage
3. **Flexibility**: Support for various transport mechanisms
4. **Extensibility**: Easy to create custom servers

### Architecture

```
┌─────────────┐     MCP Protocol     ┌─────────────┐
│ Claude Code │ ◄──────────────────► │ MCP Server  │
│   (Client)  │                       │   (Tools)   │
└─────────────┘                       └─────────────┘
```

## Configuration in Claude Code

### Project-Scoped Configuration (.mcp.json)

Create `.mcp.json` in your project root:

```json
{
  "servers": {
    "github": {
      "command": "mcp-server-github",
      "args": ["--token", "${GITHUB_TOKEN}"]
    },
    "puppeteer": {
      "command": "mcp-server-puppeteer",
      "args": ["--headless"]
    },
    "postgres": {
      "command": "mcp-server-postgres",
      "args": ["${DATABASE_URL}"]
    },
    "slack": {
      "command": "mcp-server-slack",
      "args": ["--token", "${SLACK_TOKEN}"]
    }
  }
}
```

### User-Scoped Configuration

Add servers via CLI:

```bash
# Add local server
claude mcp add github mcp-server-github --token ${GITHUB_TOKEN}

# Add SSE server
claude mcp add --transport sse myserver https://my-server.com

# List configured servers
claude mcp list

# Remove server
claude mcp remove github
```

### Configuration Hierarchy

1. **Project-level** (.mcp.json) - Shared with team
2. **User-level** (~/.claude/mcp.json) - Personal servers
3. **Session-level** - Temporary additions

## Available MCP Servers

### Official Servers

1. **GitHub** (`mcp-server-github`)
   - Repository management
   - Issue and PR operations
   - Code search
   - CI/CD status

2. **Slack** (`mcp-server-slack`)
   - Channel operations
   - Message sending
   - User lookups
   - Workspace info

3. **Google Drive** (`mcp-server-googledrive`)
   - File operations
   - Document search
   - Sharing management
   - Folder navigation

4. **Puppeteer** (`mcp-server-puppeteer`)
   - Web automation
   - Screenshot capture
   - Form filling
   - Browser control

5. **PostgreSQL** (`mcp-server-postgres`)
   - Query execution
   - Schema inspection
   - Data manipulation
   - Transaction support

6. **Git** (`mcp-server-git`)
   - Local repository operations
   - Commit history
   - Branch management
   - Diff generation

### Community Servers

- **Sentry**: Error tracking integration
- **Figma**: Design file access
- **Notion**: Database and page management
- **Jira**: Issue tracking
- **Discord**: Bot operations

## Creating Custom MCP Servers

### Python Example

```python
from mcp import Server, Tool, Resource
import asyncio

# Create server instance
server = Server("my-custom-server")

# Define a tool
@server.tool()
async def search_database(query: str, limit: int = 10) -> list:
    """Search the database for matching records."""
    # Implementation here
    results = await db.search(query, limit=limit)
    return results

# Define a resource
@server.resource()
async def get_config() -> dict:
    """Get current configuration."""
    return {
        "version": "1.0.0",
        "features": ["search", "update"]
    }

# Run the server
if __name__ == "__main__":
    server.run()
```

### JavaScript/TypeScript Example

```typescript
import { Server, Tool } from '@modelcontextprotocol/sdk';

const server = new Server({
  name: 'my-server',
  version: '1.0.0'
});

// Define tools
server.addTool({
  name: 'calculate',
  description: 'Perform calculations',
  inputSchema: {
    type: 'object',
    properties: {
      expression: { type: 'string' }
    }
  },
  handler: async ({ expression }) => {
    // Secure alternative to eval() - use a safe parser or predefined operations
    try {
      // Only allow basic math operations as an example
      const sanitized = expression.replace(/[^0-9+\-*/\(\)\s]/g, '');
      const result = Function('"use strict"; return (' + sanitized + ')')();
      return { result };
    } catch (error) {
      return { error: 'Invalid expression' };
    }
  }
});

// Start server
server.start();
```

## MCP Prompts as Slash Commands

MCP servers can expose prompts that become slash commands:

```python
@server.prompt()
async def review_code():
    """Review code for best practices."""
    return """
    Please review the selected code for:
    1. Security vulnerabilities
    2. Performance issues
    3. Code style violations
    4. Best practice adherence
    """
```

This becomes available as `/mcp__servername__review_code` in Claude Code.

## Advanced MCP Features

### 1. Transport Mechanisms

**Standard I/O** (Default)
```json
{
  "command": "mcp-server-name",
  "args": ["--flag", "value"]
}
```

**Server-Sent Events (SSE)**
```json
{
  "transport": "sse",
  "url": "https://my-mcp-server.com/sse"
}
```

### 2. Environment Variables

```json
{
  "servers": {
    "myserver": {
      "command": "mcp-server",
      "args": ["${API_KEY}"],
      "env": {
        "DEBUG": "true",
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

### 3. Debugging MCP

```bash
# Enable debug mode
claude --mcp-debug

# Verbose logging
claude --verbose

# Test specific server
claude mcp test github
```

## Enterprise MCP Patterns

### 1. Centralized Configuration

```json
{
  "servers": {
    "company-data": {
      "command": "mcp-company-server",
      "args": ["--config", "/etc/company/mcp.conf"]
    }
  }
}
```

### 2. Security Considerations

- Use environment variables for secrets
- Implement proper authentication
- Validate all inputs
- Log access for auditing
- Use least-privilege principles

### 3. Performance Optimization

```python
# Implement caching
@server.tool()
@cache(ttl=300)  # 5-minute cache
async def expensive_operation(param: str):
    # Cached operation
    pass

# Batch operations
@server.tool()
async def batch_process(items: list):
    # Process multiple items efficiently
    pass
```

## Troubleshooting MCP

### Common Issues

1. **Server Not Found**
   ```bash
   # Check installation
   which mcp-server-name
   
   # Verify configuration
   claude mcp list
   ```

2. **Permission Errors**
   ```bash
   # Fix permissions
   chmod +x /path/to/mcp-server
   ```

3. **Connection Failures**
   - Check firewall rules
   - Verify server is running
   - Test with `--mcp-debug`

### Debug Commands

```bash
# Test server connection
claude mcp test servername

# View server logs
claude mcp logs servername

# Restart server
claude mcp restart servername
```

## Best Practices

### 1. Server Design
- Keep tools focused and single-purpose
- Provide clear descriptions
- Validate inputs thoroughly
- Handle errors gracefully

### 2. Configuration Management
- Use version control for .mcp.json
- Document server requirements
- Provide setup scripts
- Test configurations regularly

### 3. Security
- Never hardcode credentials
- Use secure transport (HTTPS/SSE)
- Implement rate limiting
- Audit tool usage

### 4. Team Collaboration
- Share MCP configs via git
- Document custom servers
- Provide installation guides
- Create server templates

## Future of MCP

### Upcoming Features
- WebSocket transport support
- Enhanced security models
- Performance improvements
- Better debugging tools

### Community Growth
- Growing ecosystem of servers
- Standardization efforts
- Integration with more tools
- Enhanced documentation