# Claude Context Architect - Pure Claude Native

A **100% Claude Code native** system for deep project discovery and custom command generation.

## What This Is

This is a pure Claude Code native implementation that:
- **Analyzes** your project deeply (30-60 minutes)
- **Extracts** your project's DNA (patterns, conventions, architecture)
- **Generates** custom commands specific to YOUR project
- **Zero dependencies** - Everything runs in Claude conversation

## Quick Start (10-15 minutes)

```bash
# 1. Setup Claude structure
/setup

# 2. Deep discovery (30-60 min interactive)
/discover

# 3. Generate custom commands
/generate
```

That's it. Three commands. Pure Claude native.

## What Makes This Different

### ❌ What This Is NOT
- Not shell scripts pretending to be smart
- Not YAML configs that don't execute
- Not templates you have to customize
- Not instruction manuals for Claude

### ✅ What This IS
- **Executable commands** that run immediately
- **XML semantic tagging** for Claude understanding
- **Direct tool usage** (Read, Write, Glob, Grep)
- **Project-specific** generation, not generic templates

## Project Structure

```
.claude/
├── commands/           # Your executable commands
│   ├── setup.md       # Initialize structure
│   ├── discover.md    # Deep analysis
│   └── generate.md    # Create custom commands
├── context/           # Project understanding
└── settings.json      # Minimal config

outputs/               # Generated artifacts
├── PROJECT-DNA.md    # Your project's extracted patterns
└── generated/        # Your custom commands
```

## Core Principles

1. **Everything in conversation** - No external scripts
2. **Commands execute** - Not instruction manuals
3. **XML for semantics** - Claude understands structure
4. **Zero dependencies** - Only Claude's native tools
5. **Project-specific** - Generated for YOUR codebase

## The Three Commands

### `/setup`
- Creates `.claude/` structure
- Detects your technology stack
- Initializes context
- **Time**: 1-2 minutes

### `/discover`
- Deep 30-60 minute consultation
- Analyzes architecture, domain, patterns
- Creates PROJECT-DNA.md
- **Time**: 30-60 minutes interactive

### `/generate`
- Reads your PROJECT-DNA
- Generates custom commands
- Creates executable, not templates
- **Time**: 5-10 minutes

## Requirements

- Claude Code CLI
- A project to analyze
- 30-60 minutes for discovery

## No Installation Needed

This IS the installation. Just run `/setup`.

## Philosophy

> "If it doesn't execute, delete it."  
> "If it needs a script, rewrite as a command."  
> "If it's YAML config, convert to XML tags."  
> "If it's documentation, make it functional."

## Anti-Patterns We Avoid

Based on extensive research and validation:
- ❌ Hallucinated metrics (87.3% improvement!)
- ❌ Theatrical success claims
- ❌ Over-engineering
- ❌ Template pollution
- ❌ Context bloat

## License

MIT

---

*Pure Claude Code native. Zero scripts. Zero configs. Just commands that work.*