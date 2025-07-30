# Claude Code Essential Commands

**7 universal commands that work immediately with any programming language or framework.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-green.svg)](https://github.com/swm-sink/claude-code-modular-prompts/releases)

## 🚀 Instant Setup (30 seconds)

```bash
# 1. Copy commands to your project  
./setup-minimal.sh /path/to/your/project

# 2. Start using commands immediately
# (Open Claude Code in your project directory)
/help              # See all commands
/task "add user authentication"
```

**That's it! No configuration, no placeholders, no customization required.**

## ✨ What You Get

**7 Essential Commands (Work Immediately):**

| Command | Purpose | Example |
|---------|---------|---------|
| **`/help`** | Command guide and help | `/help` or `/help task` |
| **`/task`** | Execute any development task | `/task "add login form"` |
| **`/analyze`** | Analyze code, architecture, problems | `/analyze "performance issues"` |
| **`/review`** | Code review with suggestions | `/review src/auth.js` |
| **`/debug`** | Debug issues and errors | `/debug "API returns 500"` |
| **`/test`** | Generate and run tests | `/test --generate src/auth.js` |
| **`/docs`** | Create documentation | `/docs --api src/routes/` |

## 🎯 Universal Compatibility

**Works with any:**
- **Languages**: JavaScript, Python, Java, Go, Rust, C#, PHP, Ruby, Swift, etc.
- **Frameworks**: React, Vue, Django, Spring, Express, Laravel, Rails, etc.
- **Project Types**: Web apps, APIs, mobile apps, desktop apps, scripts, etc.

**No configuration needed** - commands automatically adapt to your project.

## 📋 Real Usage Examples

### Development Tasks
```
/task "implement JWT authentication"
/task "optimize database queries" 
/task "add real-time chat functionality"
/task "set up CI/CD pipeline"
```

### Code Analysis
```
/analyze "why is my app slow?"
/analyze src/components/UserDashboard.jsx
/analyze "memory usage keeps growing"
```

### Code Review
```
/review src/auth/login.js
/review "my payment processing implementation"  
/review components/PaymentForm.tsx
```

### Debugging
```
/debug "users can't log in"
/debug "TypeError: Cannot read property 'name' of undefined"
/debug "database connection timeout"
```

### Testing
```
/test --generate src/utils/validation.js
/test --run --coverage
/test --fix "failing authentication tests"
```

### Documentation
```
/docs --generate README
/docs --api src/controllers/users.js
/docs --update "installation instructions"
```

## 📁 What Gets Installed

**Minimal Structure (7 files):**
```
your-project/
├── .claude/
│   ├── commands/
│   │   ├── help.md      # Command guide
│   │   ├── task.md      # Universal task execution
│   │   ├── analyze.md   # Code/system analysis  
│   │   ├── review.md    # Code review
│   │   ├── debug.md     # Issue debugging
│   │   ├── test.md      # Testing assistance
│   │   └── docs.md      # Documentation generation
│   └── settings.json    # Claude Code configuration
└── CLAUDE.md            # Project memory (optional)
```

**Total: 8 files, ~50KB** (vs 255 files, 2MB+ in complex systems)

## ⚡ Performance & Simplicity

**What makes this different:**
- ✅ **Works immediately** - no setup or customization
- ✅ **Universal** - adapts to any tech stack automatically  
- ✅ **Lightweight** - 7 commands vs 64+ in complex alternatives
- ✅ **No placeholders** - commands work as-is
- ✅ **No manual work** - copy and use
- ✅ **Language agnostic** - same commands for all projects

**Honest comparison:**
- **Complex template libraries**: 255+ files, hours of customization, many broken commands
- **This system**: 7 files, 30-second setup, all commands work immediately

## 🛠️ Installation Options

### Option 1: Direct Setup (Recommended)
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts
./setup-minimal.sh /path/to/your/project
```

### Option 2: Download Specific Commands
Copy individual `.md` files from `.claude-minimal/commands/` to your `.claude/commands/` directory.

### Option 3: As Git Submodule
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-templates
cd .claude-templates
./setup-minimal.sh ../
```

## 🎓 Getting Started Guide

### First Time Using Claude Code?
1. **Install commands**: Run `./setup-minimal.sh your-project`
2. **Open Claude Code** in your project directory
3. **Try the help command**: `/help`
4. **Start with a task**: `/task "your development goal"`

### Experienced Users?
- All commands work without configuration
- No learning curve - use natural language descriptions
- Commands automatically detect your tech stack
- Start with `/task` for any development work

## 🔄 Comparison with Complex Alternatives

| Feature | This System | Complex Template Libraries |
|---------|-------------|----------------------------|
| **Setup Time** | 30 seconds | 30+ minutes |
| **Commands Working Immediately** | 7/7 (100%) | 5/64 (8%) |
| **Customization Required** | None | Hours of manual work |
| **File Count** | 8 files | 255+ files |
| **Learning Curve** | None | Steep |
| **Maintenance** | None | High |

## 🤝 When to Use This vs Alternatives

**Use this system when:**
- ✅ You want commands that work immediately
- ✅ You don't want to spend time on setup/customization
- ✅ You work with multiple different tech stacks
- ✅ You prefer simplicity over complexity
- ✅ You're new to Claude Code and want to start quickly

**Use complex template libraries when:**
- ❓ You enjoy extensive customization and setup processes
- ❓ You want 64+ commands (most requiring manual configuration)
- ❓ You have time to invest in learning complex systems
- ❓ You work with only one specific tech stack

## 📚 Philosophy: Simplicity Over Complexity

**Core Principle**: *Commands should work immediately and adapt automatically.*

**Design Decisions:**
- **No placeholders** that require manual replacement
- **No project-specific customization** required
- **Universal compatibility** instead of tech-stack-specific commands
- **Quality over quantity** - 7 excellent commands vs 64+ mixed-quality commands
- **Honest documentation** that matches actual capabilities

## 🐛 Issues & Support

**Common Questions:**
- **Q**: Do I need to customize anything? **A**: No, all commands work immediately.
- **Q**: Does this work with my tech stack? **A**: Yes, commands automatically adapt.
- **Q**: Can I add more commands? **A**: Yes, copy from the full library or write your own.

**Getting Help:**
- Check `/help` command first
- Use `/task "what you want to accomplish"` for most development needs
- Commands provide detailed examples and explanations

## 📄 License

MIT License - use freely in your projects.

---

*Simple, honest, effective. 7 commands that actually work immediately.*