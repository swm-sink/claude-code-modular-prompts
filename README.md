# Claude Code Modular Prompts Framework

> 🚀 **Transform Claude Code from good to exceptional**: Intelligent commands that adapt to YOUR project, enforce quality automatically, and get smarter over time.

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/swm-sink/claude-code-modular-prompts)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude 4](https://img.shields.io/badge/Claude-4%20Optimized-purple.svg)](CLAUDE.md)
[![Framework](https://img.shields.io/badge/Framework-3.0%20Meta--Prompting-purple.svg)](CLAUDE.md)

## 30-Second Understanding

**What**: Smart commands that automatically adapt to your tech stack and project needs
**How**: Drop 3 files into your project, start with `/auto "your task"`
**Result**: Claude Code produces better code, enforces quality, learns your patterns

**Perfect for**: Any project (React, Python, Go, mobile, data science, etc.)

```bash
# 1. Copy framework to your project (30 seconds)
git clone https://github.com/swm-sink/claude-code-modular-prompts.git
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/

# 2. Start using immediately (30 seconds)
cd your-project/
/auto "add user authentication"        # ← Framework adapts to YOUR tech stack
```

**✅ Success Indicators**: Claude Code suggests tech-specific solutions, follows your project patterns, enforces quality automatically

## Choose Your Journey

### 🏃‍♂️ **I want to use it now** (5 minutes)
👉 **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete setup with PROJECT_CONFIG.xml customization

### 🔬 **I want to understand it first** (15 minutes) 
👉 **[examples/quick-start/](examples/quick-start/)** - Working examples you can try immediately

### 🚀 **I want to master it** (1+ hours)
👉 **[docs/](docs/)** - Full documentation, advanced patterns, and customization guides


## Essential Commands (Pick One to Start)

**🤖 `/auto "your request"`** - Let framework decide the best approach
```bash
/auto "add user authentication"     # → Routes to /feature for new feature
/auto "fix login bug"              # → Routes to /task for focused fix
/auto "understand auth system"     # → Routes to /query for research
```

**🔧 `/task "focused work"`** - Single component, guaranteed TDD
```bash
/task "add password validation"    # → Creates tests first, then implementation
```

**🏗️ `/feature "complete feature"`** - Full feature with requirements
```bash
/feature "shopping cart system"    # → PRD → planning → implementation → validation
```

**🔍 `/query "research question"`** - Understand before changing
```bash
/query "how does our auth work?"   # → Analysis without modifications
```

> **Start with `/auto`** - it's intelligent routing that picks the right approach for your specific request.


## What This Framework Actually Does

**✅ Makes Claude Code Smarter**:
- **Adapts to YOUR tech stack**: Same command → React components for React projects, Python classes for Django
- **Enforces quality automatically**: TDD, test coverage, security checks
- **Learns your patterns**: Gets better at producing code that matches your style
- **Routes intelligently**: `/auto` picks the right command based on your request

**❌ What It's NOT**:
- **Not autonomous**: It's enhanced prompts, not AI agents
- **Not magic**: Still requires your thinking and decisions
- **Not one-size-fits-all**: Adapts to YOUR specific project


## See It In Action

### 🔧 Simple Fix (2 minutes)
```bash
/task "Fix password reset email"
```
**Result**: Creates failing test → implements fix → verifies tests pass → ready to commit

### 🏗️ Complete Feature (20 minutes)  
```bash
/feature "User profile with avatar upload"
```
**Result**: Writes PRD → plans architecture → implements with tests → validates functionality

### 🔍 Understanding Code (5 minutes)
```bash
/query "How does our authentication system work?"
```
**Result**: Analyzes code → explains architecture → identifies patterns → suggests improvements

> **Next Step**: Try one of these examples in your project! Each command adapts to your specific tech stack.


## Success Validation

**✅ Tier 1 Complete** (30 seconds - 5 minutes):
- [ ] Framework responds to `/auto` command
- [ ] Suggestions match your tech stack
- [ ] Quality enforcement works (mentions tests, security, etc.)

**✅ Tier 2 Complete** (5-60 minutes):
- [ ] `/task` creates tests before implementation
- [ ] `/feature` produces PRD and plans
- [ ] `/query` analyzes without changing code
- [ ] Commands suggest project-specific patterns

**✅ Tier 3 Complete** (1+ hours):
- [ ] Framework learns your coding style
- [ ] Meta-commands optimize for your project
- [ ] Custom modules integrate smoothly
- [ ] Team members can use shared configuration

## Ready to Level Up?

**🎯 Master the Basics**: Try all 4 essential commands in your project  
**🔧 Customize Framework**: Edit PROJECT_CONFIG.xml for your exact needs  
**🚀 Advanced Usage**: Explore [docs/](docs/) for meta-prompting and custom modules  

> **Remember**: Framework gets smarter about YOUR project every time you use it!


# File Format Standard (Framework 3.0)

All framework files follow a standardized table-based format:


# Version Table Header
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |
```


# Document Structure
```markdown

# Document Title

```xml
<command purpose = "Clear purpose statement">
  <!-- XML-structured content -->
</command>
```

```


# Framework 3.0 Format Elements
- **Version table**: Tracks versions, updates, and status with temporal standards
- **Horizontal separators**: 80-character lines using ``
- **XML configuration blocks**: Structured, semantic content with Claude 4 optimization
- **Thinking patterns**: Interleaved thinking blocks with critical analysis
- **Module runtime**: Deterministic execution with quality gates
- **Meta-prompting**: Self-improvement capabilities with safety boundaries


# Templates Available
- **Command template**: `.claude/templates/command-template.md` (Framework 3.0)
- **Module template**: `.claude/templates/module-template.md` (Framework 3.0)
- **Quality gates**: Universal validation framework
- **TDD integration**: Mandatory test-driven development patterns


## Documentation & Resources

### 🚀 **Getting Started** (Choose Your Path)
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete 5-minute setup guide
- **[examples/quick-start/](examples/quick-start/)** - Try working examples immediately  
- **[examples/project-configs/](examples/project-configs/)** - Pre-built configs for your tech stack

### 📖 **User Guides** (Build Your Skills)
- **[docs/user-guide/](docs/user-guide/)** - Systematic skill building
- **[docs/user-guide/commands/](docs/user-guide/commands/)** - Master all commands
- **[docs/user-guide/workflows/](docs/user-guide/workflows/)** - Real-world patterns

### 🔧 **Advanced Usage** (Framework Mastery)
- **[docs/advanced/](docs/advanced/)** - Custom modules, meta-prompting, optimization
- **[examples/advanced/](examples/advanced/)** - Sophisticated usage patterns
- **[CLAUDE.md](CLAUDE.md)** - Complete framework reference (developers)


# Requirements

- **Claude Code** (Claude Desktop App) - Framework 3.0 optimized
- **Git** for version control and session tracking
- **GitHub CLI** (`gh`) for issue tracking and session management
- **Python 3.8+** for framework health monitoring and analytics
- **Basic terminal knowledge** for command execution


# Contributing

We welcome contributions! Framework 3.0 is designed for extensibility:
1. **Commands** go in `.claude/commands/` with module runtime integration
2. **Implementation modules** go in `.claude/modules/` by category
3. **Follow Framework 3.0** standards with quality gates and TDD
4. **Keep modules focused** - single responsibility with clear interfaces
5. **Use templates** for consistent formatting and structure
6. **Test your contributions** with the validation framework


# Support

- **Issues**: [GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)
- **Discussions**: [GitHub Discussions](https://github.com/swm-sink/claude-code-modular-prompts/discussions)
- **Quick Help**: Use `/query "your question"` for research or `/docs generate` for documentation


# License

MIT License - see [LICENSE](LICENSE) file for details.

---

<p align = "center">
  <strong>🚀 Framework 3.0: Start with <code>/auto</code> and let meta-prompting handle the complexity!</strong>
</p>

<p align = "center">
  <em>"Commands delegate, modules implement, meta-prompting evolves."</em>
</p>

<p align = "center">
  <strong>Framework 3.0 Features:</strong><br>
  📊 Module Runtime Engine | 🧠 Meta-Prompting | ✅ Universal Quality Gates<br>
  🔍 Claude 4 Optimization | 🎯 TDD Enforcement | 📈 Self-Improvement
</p>