# Claude Code Starter Framework

**🚀 Save 6+ months of Claude Code learning** - A comprehensive integration framework providing battle-tested patterns, anti-pattern prevention, and professional architecture instantly.

## Why This Framework?

Starting a Claude Code project from scratch means:
- ❌ **Months learning Claude Code quirks** the hard way
- ❌ **Discovering anti-patterns** through painful failures
- ❌ **Building context management** from scratch
- ❌ **Creating component architecture** yourself
- ❌ **Reinventing orchestration patterns**

**This framework gives you 6-8 months of hard-won knowledge instantly.**

## What You Get

✅ **79 Battle-Tested Command Patterns** - Multiple approaches to common tasks  
✅ **65 Reusable Components** - Modular building blocks for custom commands  
✅ **48+ Anti-Patterns Documented** - Avoid common mistakes automatically  
✅ **Professional Architecture** - Enterprise-ready from day one  
✅ **Context Engineering** - Optimized Claude Code integration  
✅ **Git Submodule Ready** - Easy updates and maintenance  

## Quick Start (5 Minutes)

### Option 1: Git Submodule (Recommended)
```bash
# Add framework to your project
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Initialize with your project
cd .claude-framework
./setup.sh --project-name "my-awesome-project" --profile web-dev

# Your .claude/ directory is now configured!
cd .. && ls .claude/
```

### Option 2: Direct Integration
```bash
# Clone and adapt
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts
./adapt.sh --target ../my-project --profile data-science
```

## What Gets Installed

```
your-project/
├── .claude/                    # Your Claude Code configuration
│   ├── commands/              # Selected command patterns
│   │   ├── core/             # Essential: help, task, auto, query
│   │   └── [domain]/         # Web-dev, data-science, devops, etc.
│   ├── components/           # 65 reusable prompt building blocks
│   ├── context/             # Anti-patterns & best practices
│   └── CLAUDE.md           # Project-specific context
├── .claude-framework/       # Framework source (submodule)
└── [your existing files]
```

## Profiles Available

- **`general`** - Core commands only (help, task, auto, query, dev)
- **`web-dev`** - Frontend/backend development patterns
- **`data-science`** - Analysis, notebooks, ML workflows  
- **`devops`** - Infrastructure, CI/CD, monitoring
- **`custom`** - Interactive selection

## Before & After

### Without Framework (6+ months)
```
empty-project/
├── README.md
└── [your code]

# You'll spend months:
# - Learning Claude Code patterns
# - Discovering what works/doesn't work
# - Building command architecture
# - Creating reusable components
# - Avoiding anti-patterns the hard way
```

### With Framework (5 minutes)
```bash
./setup.sh --project-name "my-project"
```

```
my-project/
├── .claude/
│   ├── commands/core/        # Professional patterns ready
│   ├── components/          # 65 reusable building blocks
│   └── context/            # Anti-patterns prevented
├── README.md
└── [your code]

# You now have:
# ✅ Professional Claude Code setup
# ✅ Battle-tested patterns
# ✅ Anti-pattern protection
# ✅ Extensible architecture
# ✅ 6+ months of knowledge
```

## Advanced Usage

### Customize for Your Domain
```bash
# Add project-specific commands
cat > .claude/commands/my-app/deploy.md << 'EOF'
---
name: /deploy
description: Deploy my application
---

Guide me through deploying this specific application...
EOF
```

### Update Framework
```bash
# Pull latest improvements (if using submodule)
cd .claude-framework
git pull origin main
./update.sh  # Preserves your customizations
```

### Simplify Complex Patterns
```bash
# Remove XML complexity if not needed
cd .claude
./adapt.sh --simplify
```

## Documentation

- **[Setup Guide](SETUP.md)** - Detailed installation instructions
- **[Adaptation Guide](ADAPTATION-GUIDE.md)** - Customization patterns *(coming soon)*
- **[Integration Patterns](INTEGRATION-PATTERNS.md)** - Git submodule workflows *(coming soon)*
- **[FAQ](FAQ.md)** - Common questions *(coming soon)*

## Anti-Pattern Protection

This framework automatically prevents 48+ documented anti-patterns including:
- LLM hallucinations and metric invention
- Git commit theater and false success claims  
- Context pollution and token waste
- Prompt injection vulnerabilities
- Remediation theater

See `.claude/context/` for complete documentation.

## Success Stories

> *"Saved us 3 months on our Claude Code project. Had professional patterns running in 10 minutes."*  
> — Development Team Lead

> *"The anti-patterns alone saved us from major mistakes. Framework paid for itself immediately."*  
> — Senior Prompt Engineer

*[Add your success story!](https://github.com/swm-sink/claude-code-modular-prompts/discussions)*

## Community

- **[Discussions](https://github.com/swm-sink/claude-code-modular-prompts/discussions)** - Q&A and sharing
- **[Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)** - Bug reports and features
- **[Contributing](CONTRIBUTING.md)** - Add your patterns *(coming soon)*

## Why Not Build From Scratch?

| Approach | Time | Quality | Anti-Patterns | Architecture |
|----------|------|---------|---------------|--------------|
| **From Scratch** | 6+ months | Trial & error | Learn the hard way | DIY |
| **This Framework** | 5 minutes | Battle-tested | Prevented automatically | Professional |

## What's Included

### 79 Command Patterns
- **Core**: help, task, auto, query, dev
- **Development**: debugging, refactoring, building
- **Quality**: testing, analysis, monitoring  
- **Security**: assessment, management, auditing
- **DevOps**: deployment, CI/CD, infrastructure

### 65 Reusable Components
- Validation frameworks
- Error handling patterns
- Progress reporting
- Context management
- Orchestration patterns

### Context Engineering
- Token optimization
- Context window management
- Hierarchical loading
- Anti-pattern prevention
- Best practices

## License

MIT License - Use freely in your projects.

## Support

- **Quick Setup**: See [SETUP.md](SETUP.md)
- **Issues**: [GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)
- **Questions**: [GitHub Discussions](https://github.com/swm-sink/claude-code-modular-prompts/discussions)

---

**⚡ Get 6+ months of Claude Code knowledge in 5 minutes. Your future self will thank you.**

```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh
```