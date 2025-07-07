| version | last_updated | status |
|---------|--------------|--------|
| 2.3.0   | 2025-07-07   | stable |

# Documentation Index

────────────────────────────────────────────────────────────────────────────────

> **Quick Navigation**: Find exactly what you need in seconds!

---

## 🚀 Start Here

### Essential Docs
- **[Getting Started](GETTING_STARTED.md)** - 3-minute quickstart guide
- **[CLAUDE.md](../CLAUDE.md)** - Core framework rules (reference only)
- **[README](../README.md)** - Project overview
- **[Templates](../.claude/templates/)** - Format templates for new files

### Quick References
- **[All Commands](#-commands)** - What each command does
- **[Common Tasks](#-common-tasks)** - Solutions to everyday needs
- **[Troubleshooting](#-troubleshooting)** - Fix common issues

---

## 📚 Commands

### Core Commands (Use These 90% of the Time)
| Command | Purpose | Example |
|---------|---------|---------|
| `/auto` | Smart routing - decides what you need | `/auto "add user login"` |
| `/task` | Single component work with TDD | `/task "fix login bug"` |
| `/feature` | Complete feature with PRD & MVP | `/feature "shopping cart"` |
| `/swarm` | Complex multi-component work | `/swarm "migrate to GraphQL"` |
| `/query` | Research without changes | `/query "how does auth work?"` |

### Specialized Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/session` | Manage GitHub issues | Complex project tracking |

---

## 🎯 Common Tasks

### "I want to..."

#### **Add a new feature**
```bash
/feature "user profile with avatar upload"
```
- Creates full PRD
- Plans MVP approach
- Implements with tests

#### **Fix a bug**
```bash
/task "fix: users can't reset password"
```
- Writes test for bug
- Fixes the issue
- Verifies solution

#### **Understand existing code**
```bash
/query "explain the authentication flow"
```
- Maps code structure
- Explains architecture
- No modifications

#### **Refactor complex system**
```bash
/swarm "convert REST API to GraphQL"
```
- Creates GitHub epic
- Coordinates agents
- Tracks progress

#### **Find documentation**
```bash
/query "show me TDD examples"
```
- Searches all docs
- Returns relevant info

---

## 📖 Documentation by Category

### 🏗️ Architecture & Design
- **[Framework Overview](framework/README.md)** - How it all fits together
- **[Project Structure](framework/PROJECT_STRUCTURE_ANALYSIS.md)** - Directory layout
- **[Module System](.claude/README.md)** - Modular architecture

### 🛠️ Development Guides
- **[TDD Standards](framework/tdd-standards.md)** - Test-driven development
- **[Production Standards](framework/production-standards.md)** - Quality requirements
- **[AWARE Framework](framework/aware-framework.md)** - Systematic thinking
- **[Feature Examples](framework/feature-development-examples.md)** - Real scenarios

### 🔧 Configuration
- **[Settings Configuration](.claude/settings.json)** - Main settings file
- **[Permission Guide](framework/PERMISSION_GUIDE.md)** - Fix permission issues
- **[Naming Conventions](framework/NAMING_CONVENTIONS.md)** - Consistent naming

### 🎓 Best Practices
- **[Critical Thinking](framework/critical-thinking-enforcement.md)** - Analysis patterns
- **[Native Patterns](framework/native-patterns.md)** - Claude Code patterns
- **[Pattern Integration Map](PATTERN_INTEGRATION_MAP.md)** - Pattern usage across framework
- **[Honesty Policy](framework/honesty-policy.md)** - Framework limitations

### 📊 Advanced Topics
- **[Claude 4 Guide](CLAUDE_4_PROMPT_GUIDE.md)** - Claude 4 optimizations
- **[Integration Guide](framework/claude-code-integration.md)** - Claude integration
- **[Template Format](framework/TEMPLATE_FORMAT.md)** - Doc templates

---

## 🔍 Finding Documentation

### Search by Topic
```bash
# Find specific topics
/query "permission errors"
/query "TDD examples"
/query "swarm command"
```

### Browse by Location
- **Commands**: `.claude/commands/`
- **Modules**: `.claude/modules/`
- **Guides**: `docs/framework/`
- **Settings**: `.claude/settings/`

---

## 🆘 Troubleshooting

### Common Issues & Quick Fixes

#### Permission Errors
```bash
# One-line fix:
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```
[Full Guide](framework/PERMISSION_GUIDE.md)

#### Command Not Working
1. Check syntax: `/command "request"`
2. Try `/auto` instead
3. Check [command list](#-commands)

#### Not Sure What to Use
```bash
# Always works:
/auto "what you want to do"
```

#### Need Examples
- Check [Common Tasks](#-common-tasks)
- See [Feature Examples](framework/feature-development-examples.md)
- Try `/query "show examples"`

---

## 📝 Quick Reference Card

### The 80/20 Commands
```bash
/auto "..."     # When unsure (routes intelligently)
/task "..."     # Single component work
/feature "..."  # Complete features
/query "..."    # Research only
/query "..."    # Find help
```

### Key Principles
- **Start with `/auto`** - It figures out what you need
- **Trust the framework** - It enforces best practices
- **Use GitHub tracking** - For complex work
- **Read before writing** - Framework handles research

### Workflow Pattern
```
1. Research:  /query "understand current state"
2. Plan:      /auto "describe what you need"
3. Execute:   (framework routes to right command)
4. Track:     (auto-creates GitHub issues if needed)
```

---

## 💡 Philosophy Snippets

> *"Let the framework think, so you can create."*

> *"The best tool is the one you don't have to think about."*

> *"Research deeply, implement wisely, track everything."*

> *"Commands delegate, modules implement."*

---

**Need help?** Start with `/query "your question"` or `/auto "what you need"`!