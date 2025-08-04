# Installation Guide

## Quick Install (30 seconds)

```bash
# Install 7 essential commands
git clone https://github.com/swm-sink/claude-context-architect
cd claude-context-architect
./setup-minimal.sh /path/to/your/project

# Test it works
cd /path/to/your/project
# Open Claude Code and try: /help
```

**That's it. No configuration, no customization, no manual work.**

## What Gets Installed

```
your-project/
├── .claude/
│   ├── commands/
│   │   ├── help.md      # /help - Command guide
│   │   ├── task.md      # /task - Execute any development task
│   │   ├── analyze.md   # /analyze - Analyze code and problems
│   │   ├── review.md    # /review - Code review with suggestions  
│   │   ├── debug.md     # /debug - Debug issues and errors
│   │   ├── test.md      # /test - Generate and run tests
│   │   └── docs.md      # /docs - Create documentation
│   └── settings.json    # Claude Code configuration
└── CLAUDE.md            # Project memory (optional)
```

**Total: 8 files, ~50KB**

## Alternative: Git Submodule

```bash
# For easier updates
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-templates
cd .claude-templates && ./setup-minimal.sh ../
```

## Requirements

- Claude Code desktop application
- Git (for cloning)

## Troubleshooting

**Commands don't show up in Claude Code?**
1. Make sure you're in the right project directory
2. Restart Claude Code completely
3. Try `/help` to see if commands loaded

**Permission denied error?**
```bash
chmod +x setup-minimal.sh
./setup-minimal.sh /path/to/your/project
```

**Need more commands?** 
This repo also contains 64+ additional commands that require manual customization. Run `./setup.sh` instead of `./setup-minimal.sh` if you want to try the complex system.