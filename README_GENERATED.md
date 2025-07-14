# Claude Code Modular Prompts Framework

## 30-Second Understanding

**What**: Smart commands that automatically adapt to your tech stack and project needs
**How**: Drop 3 files into your project, start with `/auto "your task"`
**Result**: Claude Code produces better code, enforces quality, learns your patterns

**Perfect for**: Any development project (React, Python, Go, mobile, data science)

## Quick Start (2 minutes)

```bash
# Step 1: Install (30 seconds)
git clone https://github.com/swm-sink/claude-code-modular-prompts.git
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/

# Step 2: Configure (30 seconds)
cd your-project/
# Edit PROJECT_CONFIG.xml to match your tech stack

# Step 3: Run (60 seconds)
/auto "add user authentication"
# → Framework analyzes your project and provides tech-specific solution
```

**✅ Success Indicators**: 
- Claude Code suggests tech-specific solutions
- Framework follows your project patterns
- Quality enforcement works automatically

## Choose Your Journey

### 🏃‍♂️ **I want to use it now** (5 minutes)
👉 **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete setup with PROJECT_CONFIG.xml customization

### 🔬 **I want to understand it first** (15 minutes)
👉 **[examples/quick-start/](examples/quick-start/)** - Working examples you can try immediately

### 🚀 **I want to master it** (1+ hours)
👉 **[docs/](docs/)** - Full documentation, advanced patterns, and customization guides

## Essential Commands

**🤖 `/auto "your request"`** - Intelligent routing that picks the best approach
```bash
/auto "add user authentication"     # → Routes to /feature for new feature
/auto "fix login bug"              # → Routes to /task for focused fix
/auto "understand auth system"     # → Routes to /query for research
```

**🔧 `/task "focused work"`** - Single component with guaranteed TDD
```bash
/task "add password validation"    # → Creates tests first, then implementation
```

**🏗️ `/feature "complete feature"`** - Full feature with requirements analysis
```bash
/feature "shopping cart system"    # → PRD → planning → implementation → validation
```

**🔍 `/query "research question"`** - Understand before changing
```bash
/query "how does our auth work?"   # → Analysis without modifications
```

## Success Validation

**✅ Tier 1 Complete** (2 minutes):
- [ ] Framework responds to `/auto` command
- [ ] Suggestions match your tech stack
- [ ] Quality enforcement works (mentions tests, security, etc.)

**✅ Tier 2 Complete** (15 minutes):
- [ ] `/task` creates tests before implementation
- [ ] `/feature` produces PRD and plans
- [ ] `/query` analyzes without changing code
- [ ] Commands suggest project-specific patterns

**✅ Tier 3 Complete** (1+ hours):
- [ ] Framework learns your coding style
- [ ] Meta-commands optimize for your project
- [ ] Custom modules integrate smoothly
- [ ] Team members can use shared configuration

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

## Framework 3.0 Features

**🧠 Meta-Prompting**: Self-improving framework that learns your patterns
**🎯 Intelligent Routing**: `/auto` command routes to optimal approach
**⚡ Quality Gates**: Automatic TDD, security, and performance enforcement
**🔧 Project Adaptation**: Uses PROJECT_CONFIG.xml to customize for your stack
**📊 Module Runtime**: 88 specialized modules with deterministic execution
**🔒 Safety Boundaries**: Human oversight with instant rollback capabilities

## Requirements

- **Claude Code** (Claude Desktop App) - Framework 3.0 optimized
- **Git** for version control and session tracking
- **GitHub CLI** (`gh`) for issue tracking and session management
- **Python 3.8+** for framework health monitoring
- **Basic terminal knowledge** for command execution

## Contributing

Framework 3.0 is designed for extensibility:
1. **Commands** go in `.claude/commands/` with module runtime integration
2. **Implementation modules** go in `.claude/modules/` by category
3. **Follow Framework 3.0** standards with quality gates and TDD
4. **Keep modules focused** - single responsibility with clear interfaces

## Support

- **Issues**: [GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)
- **Discussions**: [GitHub Discussions](https://github.com/swm-sink/claude-code-modular-prompts/discussions)
- **Quick Help**: Use `/query "your question"` for research

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

**🚀 Start with `/auto` and let the framework handle the complexity!**

*"Commands delegate, modules implement, meta-prompting evolves."*
