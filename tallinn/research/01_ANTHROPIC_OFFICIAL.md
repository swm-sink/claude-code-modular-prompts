# Official Anthropic Claude Code Documentation

## Overview
Claude Code is Anthropic's official agentic terminal tool that embeds Claude Opus 4 directly in your terminal, providing deep codebase awareness and the ability to edit files and run commands directly in your environment.

## Core Features

### 1. Project Awareness
- Claude Code maintains awareness of your entire project structure
- Can find up-to-date information from the web
- With MCP can pull from external datasources like Google Drive, Figma, and Slack

### 2. Direct Environment Interaction
- Can directly edit files
- Run commands
- Create commits
- Handle git workflows through natural language commands

### 3. Model Support
- **Claude Opus 4**: The most powerful model for coding (72.5% on SWE-bench, 43.2% on Terminal-bench)
- **Claude Sonnet 4**: Balanced performance and speed
- **Claude Haiku 3.5**: Fast, lightweight option

## 2025 Updates & General Availability

Claude Code is now generally available with:
- Background tasks via GitHub Actions
- Native integrations with VS Code and JetBrains
- Extensions display edits directly in your files for seamless pair programming

## IDE Integrations

### VS Code
- Beta extension available
- Inline edit display
- Quick launch with Cmd+Esc (Mac) or Ctrl+Esc (Windows/Linux)
- Works with VS Code, Cursor, and Windsurf

### JetBrains
- Plugin available for IntelliJ, PyCharm, Android Studio, WebStorm, PhpStorm, GoLand
- Automatic IDE detection
- Integrated diff viewer

## Key Capabilities

### Automation
- Fix lint issues
- Resolve merge conflicts
- Write release notes
- Handle 90%+ of git interactions

### Unix Philosophy
Claude Code is composable and scriptable:
```bash
tail -f app.log | claude -p "Slack me if you see any anomalies"
```

### SDK and Extensions
- Extensible Claude Code SDK for building custom agents
- Claude Code on GitHub (beta) - tag Claude on PRs for automated responses

## Enterprise Features

### Deployment Options
- Anthropic's API
- Amazon Bedrock (FedRAMP High, DoD IL4/5 approved)
- Google Cloud Vertex AI

### Security
- Enterprise-grade security, privacy, and compliance
- Managed permissions configuration
- Corporate proxy support
- LLM gateway integration

## Installation

```bash
npm install -g @anthropic-ai/claude-code
```

Requirements: Node 18+ on macOS/Linux/WSL

## Best Practices (Official)

### Custom Commands
Store prompt templates in `.claude/commands/` folder:
```bash
echo "Analyze performance and suggest optimizations:" > .claude/commands/optimize.md
```

### CLAUDE.md Files
Create a `CLAUDE.md` file in your repository root to define:
- Code style guidelines
- Review criteria
- Project-specific rules
- Preferred patterns

### MCP Configuration
Use `.mcp.json` for project-scoped MCP servers:
```json
{
  "servers": {
    "puppeteer": {
      "command": "mcp-server-puppeteer"
    }
  }
}
```

## Documentation Links

1. [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
2. [Setup Guide](https://docs.anthropic.com/en/docs/claude-code/setup)
3. [Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
4. [SDK Documentation](https://docs.anthropic.com/en/docs/claude-code/sdk)
5. [GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
6. [MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)
7. [IDE Integrations](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
8. [Slash Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
9. [Tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials)
10. [Enterprise Deployment](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations)

## Key Announcements

- [Introducing Claude 4](https://www.anthropic.com/news/claude-4)
- [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Claude Code Launch](https://www.anthropic.com/claude-code)
- [Code with Claude 2025 Event](https://www.anthropic.com/events/code-with-claude-2025)