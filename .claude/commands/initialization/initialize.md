---
name: initialize
description: Minimal Claude Code initialization - creates essential structure only
usage: "/initialize [--minimal]"
allowed-tools: [Write, LS]
---

# Initialize Claude Code

I'll create the minimal structure needed for Claude Code to work.

## Minimal Setup (Default)

Creates only the essentials:
1. `.claude/` directory structure
2. Basic `settings.json` with safe defaults
3. Empty `CLAUDE.md` template

## What Gets Created

```
.claude/
├── commands/       # Your custom commands go here
├── agents/         # Specialized agents (optional)
└── settings.json   # Claude Code configuration
```

## Settings Defaults

- Safe tool permissions (Read, Write, Edit)
- Command auto-discovery enabled
- Context management configured
- No dangerous operations allowed

## Next Steps

After initialization:
- Run `/quick-setup` for project detection
- Run `/orchestrate` for comprehensive setup
- Add your first command with `/generate`

Creating minimal structure now...