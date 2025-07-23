# Claude Code Comprehensive Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [Installation & Setup](#installation--setup)
4. [CLAUDE.md Configuration](#claudemd-configuration)
5. [Slash Commands](#slash-commands)
6. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
7. [IDE Integration](#ide-integration)
8. [Automation & CI/CD](#automation--cicd)
9. [Context Engineering](#context-engineering)
10. [Enterprise Deployment](#enterprise-deployment)
11. [Performance Optimization](#performance-optimization)
12. [Best Practices](#best-practices)
13. [Troubleshooting](#troubleshooting)
14. [Community Resources](#community-resources)

## Introduction

Claude Code is Anthropic's official agentic terminal tool that embeds Claude models directly in your development environment. It provides deep codebase awareness, file editing capabilities, and command execution through natural language.

### Key Features
- **Agentic Capabilities**: Understands context, makes decisions, executes tasks
- **Deep Codebase Understanding**: Maps and comprehends entire project structures
- **Direct Environment Interaction**: Edits files, runs commands, manages git
- **Extensible Architecture**: MCP support, custom commands, SDK availability

### Available Models
- **Claude Opus 4**: Most powerful (72.5% SWE-bench, 43.2% Terminal-bench)
- **Claude Sonnet 4**: Balanced performance and speed
- **Claude Haiku 3.5**: Fast, lightweight option

## Core Concepts

### 1. Agentic AI
Claude Code acts as an intelligent agent that:
- Analyzes your entire codebase
- Makes informed decisions
- Executes multi-step tasks
- Learns from your project context

### 2. Natural Language Interface
Interact using plain English:
```bash
claude "fix the authentication bug in the login system"
claude "add dark mode to the application"
claude "refactor the database connection logic"
```

### 3. Unix Philosophy
Composable and scriptable:
```bash
# Pipe operations
cat error.log | claude -p "identify critical issues"

# Command chaining
git diff | claude -p "review changes" | mail -s "Review" team@company.com
```

## Installation & Setup

### Requirements
- Node.js 18+ (LTS recommended)
- macOS, Linux, or WSL on Windows
- Active internet connection

### Basic Installation
```bash
# Install globally
npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version

# Initial setup
claude login
```

### Configuration
```bash
# Set API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Configure model preference
claude config set model claude-opus-4

# Set default options
claude config set auto-approve false
```

## CLAUDE.md Configuration

CLAUDE.md is the cornerstone of effective Claude Code usage. It provides project-specific context that transforms Claude from a generic assistant to your specialized team member.

### File Hierarchy
1. **Global**: `~/.claude/CLAUDE.md` - Personal preferences
2. **Project**: `/project/CLAUDE.md` - Team conventions
3. **Local**: `/project/CLAUDE.local.md` - Personal overrides
4. **Subdirectory**: `/project/module/CLAUDE.md` - Module-specific

### Essential Sections

```markdown
# Project Name

## Tech Stack
- Framework: Next.js 14
- Language: TypeScript 5.2
- Database: PostgreSQL with Prisma
- Testing: Jest + React Testing Library

## Project Structure
- `src/app/`: Next.js App Router
- `src/components/`: Reusable components
- `src/lib/`: Business logic
- `tests/`: Test files

## Commands
- `npm run dev`: Start development
- `npm run build`: Production build
- `npm test`: Run tests

## Code Style
- Use ES modules (import/export)
- Prefer arrow functions
- Sort imports: react → next → third-party → local

## Git Workflow
- Branch: feature/TICKET-description
- Commits: conventional format
- PR requires 2 approvals

## DO NOT
- Edit src/legacy/
- Commit .env files
- Use console.log
- Skip tests
```

### Best Practices
- Keep under 500 lines
- Update regularly
- Be specific and concrete
- Include the "why"
- Version control it

## Slash Commands

### Built-in Commands
- `/clear` - Clear conversation context
- `/config` - Configure settings
- `/cost` - Show token usage
- `/help` - Display help
- `/login` - Authenticate
- `/logout` - Sign out
- `/model` - Switch models
- `/install-github-app` - Set up GitHub integration

### Custom Commands

Create in `.claude/commands/`:

```markdown
# .claude/commands/review.md
---
description: Comprehensive code review
allowed-tools: Read, Grep
---

Review the code for:
1. Security vulnerabilities
2. Performance issues
3. Code style violations
4. Best practices

Focus on: $ARGUMENTS
```

Usage:
```bash
/project:review "authentication module"
```

### Advanced Features

**Variable Arguments:**
```markdown
Fix issue #$ARGUMENTS following our coding standards
```

**Bash Integration:**
```markdown
---
allowed-tools: Bash(git status:*), Bash(git diff:*)
---
Current status: !`git status`
Changes: !`git diff`
```

**File References:**
```markdown
Review @src/api/auth.ts against @docs/api-spec.md
```

## Model Context Protocol (MCP)

MCP enables Claude Code to connect with external tools and data sources.

### Configuration

**Project-scoped** (`.mcp.json`):
```json
{
  "servers": {
    "github": {
      "command": "mcp-server-github",
      "args": ["--token", "${GITHUB_TOKEN}"]
    },
    "postgres": {
      "command": "mcp-server-postgres",
      "args": ["${DATABASE_URL}"]
    }
  }
}
```

**User-scoped**:
```bash
claude mcp add puppeteer mcp-server-puppeteer --headless
claude mcp list
claude mcp remove puppeteer
```

### Available Servers
- GitHub - Repository management
- Slack - Team communication
- Google Drive - Document access
- Puppeteer - Web automation
- PostgreSQL - Database queries
- Git - Local repository operations

### Creating Custom Servers

**Python Example:**
```python
from mcp import Server, Tool

server = Server("my-server")

@server.tool()
async def search_docs(query: str) -> list:
    """Search documentation."""
    results = await search_engine.query(query)
    return results

server.run()
```

## IDE Integration

### VS Code
1. Install extension from marketplace
2. Run `claude` in integrated terminal
3. Quick launch: `Cmd+Esc` (Mac) / `Ctrl+Esc` (Windows/Linux)

Features:
- Inline diff viewing
- Selection context sharing
- Direct file editing

### JetBrains
1. Install plugin from JetBrains Marketplace
2. Restart IDE
3. Run `/config` and set diff tool to auto

Supports:
- IntelliJ IDEA
- PyCharm
- WebStorm
- PhpStorm
- GoLand

## Automation & CI/CD

### Headless Mode
```bash
# Basic usage
claude -p "Your prompt" --output-format json

# With tool restrictions
claude -p "Analyze code" --allowed-tools Read,Grep

# Streaming output
claude -p "Long task" --output-format stream-json
```

### GitHub Actions
```yaml
name: Claude Analysis
on: [push]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: anthropics/claude-code-action@v1
        with:
          prompt: "Review PR for security issues"
          github-token: ${{ secrets.GITHUB_TOKEN }}
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

claude -p "Check for security vulnerabilities" \
  --allowed-tools Read,Grep \
  --output-format json | \
  jq -e '.vulnerabilities | length == 0'
```

## Context Engineering

### Token Management
- 200k token context window (≈500 pages)
- Enterprise: 500k with Sonnet 4

### Optimization Strategies

1. **File Structure**
   - Keep files under 300 lines
   - Modular architecture
   - Clear separation of concerns

2. **Context Loading**
   ```markdown
   # Read files in order:
   1. Specifications: /docs/
   2. Implementation: /src/
   3. Tests: /tests/
   ```

3. **Memory Management**
   ```bash
   # Clear between tasks
   /clear
   
   # Specific references
   @src/specific-file.ts
   ```

### Extended Thinking
- `"think"` - Basic analysis
- `"think hard"` - Complex problems
- `"think harder"` - Critical decisions
- `"ultrathink"` - Architecture design

## Enterprise Deployment

### Deployment Options

1. **Anthropic API**
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```

2. **Amazon Bedrock**
   ```bash
   export CLAUDE_CODE_USE_BEDROCK=1
   export AWS_REGION=us-east-1
   ```
   - FedRAMP High certified
   - DoD IL4/5 approved

3. **Google Vertex AI**
   ```bash
   export CLAUDE_CODE_USE_VERTEX=1
   export CLOUD_ML_REGION=us-central1
   ```

### Security Features
- Managed permissions
- Audit logging
- VPC deployment
- SOC 2 compliance
- HIPAA support

### Cost Management
```json
{
  "budgets": {
    "monthly_limit": 10000,
    "per_user_limit": 100,
    "alert_thresholds": [0.5, 0.75, 0.9]
  }
}
```

## Performance Optimization

### Speed Improvements
1. **Model Selection**
   - Haiku for simple tasks
   - Sonnet for balanced work
   - Opus for complex analysis

2. **Caching**
   - Prompt caching: 90% cost reduction
   - Context caching for repeated queries

3. **Batch Operations**
   ```bash
   find . -name "*.js" | \
     xargs -n 10 claude -p "Add JSDoc comments"
   ```

### Token Optimization
1. **Compact Files**
   - Single responsibility
   - Clear boundaries
   - Minimal dependencies

2. **Direct Instructions**
   ```markdown
   # Focus on:
   - src/api/auth.ts
   - src/middleware/auth.ts
   # Ignore: tests/, docs/
   ```

3. **Selective Inclusion**
   ```python
   # Include only relevant sections
   lines 45-120 of UserService.ts
   ```

## Best Practices

### Development Workflow
1. **Start with /init**
   - Analyzes codebase
   - Generates initial CLAUDE.md
   - Creates project understanding

2. **Use Planning Mode**
   - Complex tasks benefit from planning
   - Prevents jumping to implementation
   - Improves accuracy

3. **Incremental Development**
   - Start with minimal prompt
   - Build on responses
   - Refine as needed

### Team Collaboration
1. **Shared Configuration**
   - CLAUDE.md in version control
   - Team-wide slash commands
   - Consistent MCP setup

2. **Code Review Integration**
   ```bash
   /install-github-app
   # Automatic PR reviews
   # Bug detection
   # Security analysis
   ```

3. **Documentation**
   - Update CLAUDE.md regularly
   - Document custom commands
   - Share best practices

### Security
1. **Never hardcode secrets**
2. **Use environment variables**
3. **Implement least privilege**
4. **Regular security audits**
5. **Monitor usage patterns**

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   ```bash
   # Check API key
   echo $ANTHROPIC_API_KEY
   
   # Re-login
   claude logout
   claude login
   ```

2. **Context Window Exceeded**
   - Use `/clear` regularly
   - Reduce file inclusion
   - Select specific sections

3. **Tool Permission Issues**
   ```bash
   # Explicitly allow tools
   claude --allowed-tools Read,Write,Edit
   ```

### Debug Mode
```bash
# Enable verbose logging
claude --verbose

# MCP debugging
claude --mcp-debug

# Check configuration
claude config list
```

## Community Resources

### Essential Repositories
1. **anthropics/claude-code** - Official repository
2. **awesome-claude-code** - Curated resources
3. **claude-code-guide** - Comprehensive guide
4. **Model Context Protocol** - MCP servers

### Learning Resources
- Official documentation
- Community tutorials
- Video guides
- Example projects

### Getting Help
- GitHub issues
- Community Discord
- Stack Overflow
- Official support

## Conclusion

Claude Code represents a paradigm shift in how developers interact with AI assistants. By following this guide and continuously refining your approach, you can achieve:

- 10x productivity improvements
- Higher code quality
- Reduced cognitive load
- Better team collaboration

Remember: Claude Code is a tool that amplifies your capabilities. The key to success is thoughtful integration into your workflow and continuous optimization of your context engineering.

---

*This guide synthesizes research from 50+ sources including official Anthropic documentation, community resources, and developer experiences. For detailed information on specific topics, refer to the individual research documents in this folder.*