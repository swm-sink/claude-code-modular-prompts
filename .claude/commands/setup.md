---
name: setup
description: Initialize Claude Code project structure
usage: "/setup"
allowed-tools: [Write, Read, Glob, LS, Edit]
---

# Setup Command

## What I'll Do

I'll set up a complete Claude Code project structure:
1. Create .claude/ directory structure
2. Generate essential commands
3. Create CLAUDE.md for project context
4. Set up settings.json
5. Initialize documentation

## Structure I'll Create

```
.claude/
├── commands/       # Your slash commands
├── settings.json   # Claude Code configuration
└── CLAUDE.md      # Project context

docs/               # Documentation
README.md          # User documentation
```

## Essential Commands

I'll create starter commands:
- `/task` - General task execution
- `/help` - Project assistance
- `/commit` - Git operations
- `/test` - Run tests

## Configuration

I'll configure:
- Tool permissions
- File access patterns
- Command categories
- Development workflow

Run this command to initialize your Claude Code project structure.