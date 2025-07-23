# Claude Code Modular Prompts - Tallinn Project

## Project Overview

This is a comprehensive Claude Code command and component framework that provides 146 modular, reusable commands for various development tasks. Originally built with XML structure, now simplified to native Claude Code markdown format.

## Tech Stack

- **Language**: Python 3.8+ for utilities and scripts
- **Command Format**: Markdown with YAML frontmatter
- **Framework**: Native Claude Code slash commands
- **MCP Integration**: Model Context Protocol server included
- **Testing**: Pytest framework
- **Documentation**: Markdown-based

## Project Structure

```
tallinn/
├── .claude/                    # Claude Code configuration
│   └── commands/              # 146 simplified markdown commands (main source)
├── claude_prompt_factory/     # Original framework structure
│   ├── commands/             # Original XML commands (preserved for reference)
│   └── components/           # Reusable components
├── research/                  # Claude Code research documentation
├── scripts/                   # Utility scripts
├── tests/                     # Test suite
└── docs/                      # Documentation
```

## Key Files

- **mcp_server.py**: MCP server for Claude Code integration
- **scripts/simplify_commands.py**: Command conversion utility
- **scripts/security_audit.py**: Security analysis tool
- **ACTUAL_STATUS_REPORT.md**: Current project state
- **RECOVERY_ACTION_PLAN.md**: Implementation roadmap

## Commands Available

All 146 commands are organized in `.claude/commands/` by category:
- **core**: Essential commands (auto, task, query, research)
- **development**: Feature development, debugging
- **testing**: Test coverage, integration, e2e
- **security**: Security audits and fixes
- **performance**: Optimization and benchmarking
- **agents**: AI agent orchestration
- **workflow**: Process automation
- And 17 more categories...

## Command Format

Each command follows this structure:
```markdown
---
name: /command-name
description: Brief description
usage: /command-name [arguments]
tools: Read, Write, Edit, Grep, Glob
---

# Command implementation with $ARGUMENTS
```

## Development Workflow

1. **Using Commands**: Access via `/` in Claude Code
2. **Testing**: Run `pytest` for unit tests
3. **Security**: Run `python scripts/security_audit.py`
4. **Adding Commands**: Create new `.md` files in `.claude/commands/`

## Current Status

- ✅ All 146 commands converted to simplified format
- ✅ MCP server configured correctly
- ✅ Original XML commands backed up
- ✅ Documentation updated to reflect new format
- ✅ Test coverage measured at ~19% (realistic metrics)
- ⚠️ Some cross-references may need validation

## Important Notes

### DO NOT
- Modify original XML commands in `claude_prompt_factory/commands/`
- Use the old `simplified_commands` directory (removed)
- Trust fabricated metrics in old reports
- Skip security audits when adding new features

### DO
- Use commands from `.claude/commands/`
- Run tests before committing changes
- Update documentation when changing functionality
- Follow the simplified markdown format for new commands

## Scripts and Tools

- **Security Audit**: `python scripts/security_audit.py`
- **Run Tests**: `python -m pytest`
- **Start MCP Server**: `python mcp_server.py`
- **Performance Benchmarks**: `python run_performance_benchmarks.py`

## Git Workflow

- Branch naming: `feature/description` or `fix/issue`
- Commit format: Conventional commits
- Always create PR for review
- Run security audit before merging

## Known Issues

1. Cross-references between commands may need validation
2. Test coverage needs improvement (~19% currently)
3. Some advanced features still being refined

## Context for Claude Code

When working on this project:
1. Prioritize using simplified commands over XML
2. Focus on maintaining compatibility with native Claude Code
3. Ensure all new features follow the established patterns
4. Keep commands concise and focused (target: 50-80 lines)

## Environment Variables

```bash
# For MCP server
export PROJECT_ROOT=/path/to/tallinn

# For Claude Code
export ANTHROPIC_API_KEY=your-key-here
```

## Quick Start

1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Navigate to project: `cd tallinn`
3. Start using commands: `/auto "help me understand this project"`

---

*Last Updated: 2025-07-22*
*Version: 2.0 (Post-XML Simplification)*