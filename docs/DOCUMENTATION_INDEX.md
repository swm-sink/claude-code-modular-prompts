| version | last_updated | status |
|---------|--------------|--------|
| 2.4.0   | 2025-07-08   | stable |

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
- **[Command Overview](commands/overview.md)** - Complete command reference with 2.4.0 runtime engine features
- **[Command Selection Guide](COMMAND_SELECTION_GUIDE.md)** - Stop confusion between `/docs` and `/query`!
- **[All Commands](#-commands)** - What each command does
- **[Common Tasks](#-common-tasks)** - Solutions to everyday needs
- **[Troubleshooting](#-troubleshooting)** - Fix common issues

---

## 📚 Commands

> **📖 Complete Reference**: See **[Command Overview](commands/overview.md)** for detailed command documentation with 2.4.0 runtime engine features!

### Core Commands (Use These 90% of the Time)
| Command | Purpose | 2.4.0 Enhancement | Example |
|---------|---------|-------------------|---------|
| `/auto` | Smart routing - decides what you need | TDD-aware intelligent routing | `/auto "add user login"` |
| `/task` | Single component work with TDD | Standard TDD enforcement | `/task "fix login bug"` |
| `/feature` | Complete feature with PRD & MVP | Feature-level TDD integration | `/feature "shopping cart"` |
| `/swarm` | Complex multi-component work | Multi-agent TDD coordination | `/swarm "migrate to GraphQL"` |
| `/query` | **Research ONLY** - understand code, no file changes | Test-aware research patterns | `/query "how does auth work?"` |
| `/docs` | **Documentation ONLY** - create/update docs | TDD methodology integration | `/docs generate "API Guide"` |

### Specialized Commands
| Command | Purpose | 2.4.0 Enhancement | When to Use |
|---------|---------|-------------------|-------------|
| `/session` | Manage GitHub issues | TDD progress tracking | Complex project tracking |
| `/protocol` | Production standards enforcement | Strictest TDD + all quality gates | Production-critical development |

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

### ⚙️ Module Runtime Engine (Framework 2.4.0)
- **[Command Overview](commands/overview.md)** - Complete command reference with runtime engine integration
- **[Module Runtime Engine User Guide](framework/module-runtime-engine.md)** - Comprehensive guide for practical usage and troubleshooting
- **[Runtime Engine Overview](.claude/modules/patterns/module-composition-framework.md)** - Deterministic module composition and execution
- **[Universal Quality Gates](.claude/modules/quality/universal-quality-gates.md)** - Comprehensive validation framework
- **[TDD Enforcement](.claude/modules/quality/tdd.md)** - Strict test-driven development
- **[Thinking Pattern Template](.claude/modules/patterns/thinking-pattern-template.md)** - Standardized command checkpoints
- **[Command Runtime Specifications](../CLAUDE.md#module_runtime_engine)** - Command-specific runtime behaviors
- **[Error Handling & Recovery](.claude/modules/patterns/module-composition-framework.md#error_handling)** - Recovery protocols and escalation
- **[Performance Optimization](.claude/modules/patterns/module-composition-framework.md#execution_optimization)** - Parallel execution and batching
- **[Module Integration Points](.claude/modules/patterns/module-composition-framework.md#integration_points)** - Framework integration specifications

#### Command Runtime Behaviors
| Command | Runtime Pattern | Quality Gates | TDD Enforcement |
|---------|----------------|---------------|-----------------|
| `/task` | Single-component TDD | Foundational + Development | Standard cycle |
| `/swarm` | Multi-agent coordination | All gates + Coordination | Isolated worktrees |
| `/auto` | TDD-aware routing | Analysis + Routing | Routes to TDD commands |
| `/query` | Read-only analysis | Analysis only | Test-aware research |
| `/session` | Session with TDD tracking | Foundational + Progress | Progress tracking |
| `/protocol` | Strictest enforcement | ALL gates | Production compliance |
| `/docs` | Documentation gateway | Foundational + Standards | Methodology docs |

#### Quality Gate Categories
- **Foundational Gates**: Critical thinking, requirement clarity, module integration, error handling
- **Development Gates**: TDD compliance, code quality, security requirements, performance validation
- **Coordination Gates**: Multi-agent synchronization, session tracking, integration validation
- **Documentation Gates**: Standards compliance, TDD methodology documentation
- **Analysis Gates**: Research comprehensiveness, routing decision quality

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

### The 80/20 Commands (Framework 2.4.0)
```bash
/auto "..."     # TDD-aware intelligent routing (70% faster)
/task "..."     # Single component with TDD enforcement
/feature "..."  # Complete features with PRD + TDD integration
/query "..."    # Test-aware research only
/docs "..."     # Documentation with TDD methodology
/protocol "..." # Maximum quality gates for production
```

### Key Principles (Enhanced in 2.4.0)
- **TDD First** - All development enforces RED-GREEN-REFACTOR
- **Quality Gates** - Universal validation prevents errors  
- **Critical Thinking** - 30-second analysis before action
- **Parallel Execution** - 70% performance improvement
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