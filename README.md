# Claude Code Modular Agents Framework

> 🚀 **A prompt engineering framework that improves Claude Code workflow efficiency through organized prompts and GitHub integration**

[![Version](https://img.shields.io/badge/version-2.2.0-blue.svg)](https://github.com/swm-sink/claude-code-modular-agents)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude 4](https://img.shields.io/badge/Claude-4%20Optimized-purple.svg)](CLAUDE.md)

## What is This?

Claude Code Modular Agents is a personal development tool that enhances your Claude Code workflow through:

- **🎯 Smart Commands**: Intelligent routing that understands context
- **🧩 Modular Prompts**: Reusable components that reduce repetition  
- **✅ Quality Reminders**: Built-in TDD and best practice prompts
- **📊 GitHub Integration**: Issue-based tracking for complex work
- **🔧 Organized Structure**: 29 specialized prompt modules across 7 categories

**Reality Check**: This is a sophisticated prompt engineering system, NOT autonomous AI agents or enterprise software. It's a personal productivity tool.

## Quick Start (30 seconds!)

### Installation

```bash
# Clone the framework
git clone https://github.com/swm-sink/claude-code-modular-agents.git

# Copy framework to your project
cp -r claude-code-modular-agents/.claude your-project/
cp claude-code-modular-agents/CLAUDE.md your-project/
```

### Start Using Immediately

```bash
# Not sure what command to use? Start here:
/auto "Add user authentication to my app"

# Quick focused task:
/task "Fix the login bug"

# Just researching:
/query "How does our caching work?"
```

📚 **[Full Getting Started Guide](docs/GETTING_STARTED.md)** - 3 minute read, working in 30 seconds!

## Key Commands

### The 5 Essential Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `/auto` | Smart routing - decides what you need | `/auto "add user login"` |
| `/task` | Single component work with TDD | `/task "fix password reset"` |
| `/feature` | Complete feature with PRD | `/feature "shopping cart"` |
| `/swarm` | Complex multi-component work | `/swarm "migrate to GraphQL"` |
| `/query` | Research without changes | `/query "explain auth flow"` |

### Visual Command Flow

```
Your Request → /auto → Intelligent Routing → Right Command → Quality Output
```

## What This Actually Does

### ✅ What It Does Well

- **Organizes complex prompts** into reusable modules
- **Routes requests intelligently** to the right approach
- **Enforces best practices** like TDD automatically
- **Tracks complex work** with GitHub integration
- **Provides helpful reminders** for quality code

### ❌ What It Doesn't Do

- **Not autonomous agents** - it's organized prompts
- **Not enterprise software** - it's a personal tool
- **Not magic** - it enhances Claude Code, doesn't replace thinking
- **Not a platform** - it's workflow automation

## Real-World Examples

### Building a Feature
```bash
/feature "User profile with avatar upload"
# → Creates requirements doc (PRD)
# → Plans minimal viable approach
# → Implements with tests
# → Validates everything works
```

### Fixing a Bug
```bash
/task "Fix: Users can't reset password"
# → Writes test for the bug first
# → Implements the fix
# → Verifies test passes
# → No regressions
```

### Complex Project
```bash
/swarm "Convert REST API to GraphQL"
# → Creates GitHub tracking issue
# → Breaks into manageable phases
# → Coordinates the work
# → Tracks progress
```

## Framework Structure

```
.claude/
├── commands/        # Smart command routers (delegation only)
├── modules/         # Actual implementation prompts
│   ├── security/    # Security reminder prompts
│   ├── quality/     # TDD and quality prompts
│   ├── development/ # Development workflow prompts
│   └── patterns/    # Reusable pattern prompts
├── templates/       # Format templates for new files
└── settings/        # Your preferences
```

**Philosophy**: *"Commands delegate, modules implement"*

## File Format Standard (Framework 3.0)

All framework files follow a standardized table-based format:

### Version Table Header
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 2.0.0   | 2025-07-07   | stable |
```

### Document Structure
```markdown
# Document Title

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Clear purpose statement">
  <!-- XML-structured content -->
</command>
```

────────────────────────────────────────────────────────────────────────────────
```

### Key Format Elements
- **Version table**: Tracks versions, updates, and status
- **Horizontal separators**: 80-character lines using `────`
- **XML configuration blocks**: Structured, semantic content
- **Clear section organization**: Logical flow with proper spacing

### Templates Available
- **Command template**: `.claude/templates/command-template.md`
- **Module template**: `.claude/templates/module-template.md`

## Documentation

- **[Getting Started](docs/GETTING_STARTED.md)** - 3-minute quickstart
- **[Documentation Index](docs/DOCUMENTATION_INDEX.md)** - Find anything quickly
- **[CLAUDE.md](CLAUDE.md)** - Core framework rules (reference)
- **[Templates](.claude/templates/)** - Format templates for new files
- **[Framework Guides](docs/framework/)** - Deep dives on specific topics
- **[Examples](projects-test/)** - See it in action

## Requirements

- Claude Code (Claude Desktop App)
- Git for version control
- GitHub CLI (`gh`) for issue tracking
- Basic terminal knowledge

## Contributing

We welcome contributions! The framework is designed to be extended:
1. Commands go in `.claude/commands/`
2. Implementation modules go in `.claude/modules/`
3. Follow the delegation pattern
4. Keep modules under 2k tokens

## Support

- **Issues**: [GitHub Issues](https://github.com/swm-sink/claude-code-modular-agents/issues)
- **Discussions**: [GitHub Discussions](https://github.com/swm-sink/claude-code-modular-agents/discussions)
- **Quick Help**: Use `/docs "your question"`

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>🚀 Start with <code>/auto</code> and let the framework handle the complexity!</strong>
</p>

<p align="center">
  <em>"Let the framework think, so you can create."</em>
</p>