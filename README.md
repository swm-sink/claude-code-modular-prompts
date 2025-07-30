# Claude Code Essential Commands

**7 universal commands that work immediately with any programming language or framework.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-green.svg)](https://github.com/swm-sink/claude-code-modular-prompts/releases)

## 🚀 Quick Start (30 seconds)

```bash
# Install 7 essential commands
./setup-minimal.sh /path/to/your/project

# Start using immediately (in Claude Code)
/help                              # See all commands
/task "add user authentication"    # Execute any development task
/analyze "why is my app slow?"     # Analyze code or problems
```

**That's it. No configuration, no customization, no manual work.**

## What You Get

**7 Universal Commands (Work Immediately):**
- **`/help`** - Command guide and help system
- **`/task`** - Execute any development task 
- **`/analyze`** - Analyze code, architecture, problems
- **`/review`** - Code review with suggestions
- **`/debug`** - Debug issues and errors
- **`/test`** - Generate tests and run test suites
- **`/docs`** - Create documentation

**Works with any programming language or framework** - JavaScript, Python, Java, Go, React, Django, Spring, etc.

## How It Works

1. **Install**: Run `./setup-minimal.sh your-project` (copies 7 commands, 30 seconds)
2. **Use**: Open Claude Code in your project, try `/task "your goal"`
3. **Done**: Commands automatically adapt to your tech stack - no configuration needed

## Usage Examples

**Development Tasks:**
```
/task "implement JWT authentication"
/task "optimize database queries" 
/task "add real-time chat functionality"
```

**Code Analysis:**
```
/analyze "why is my app slow?"
/analyze src/components/UserDashboard.jsx
/debug "users can't log in"
```

**Code Review & Testing:**
```
/review src/auth/login.js
/test --generate src/utils/validation.js
/docs --api src/controllers/users.js
```

## Installation

**Recommended:**
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts
./setup-minimal.sh /path/to/your/project
```

**Or as git submodule:**
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-templates
cd .claude-templates && ./setup-minimal.sh ../
```

## File Structure After Installation

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

## Universal Compatibility

**Works with any programming language or framework:**
- JavaScript, TypeScript, Python, Java, Go, Rust, C#, PHP, Ruby
- React, Vue, Angular, Django, Spring, Laravel, Rails, Express
- Any project type: web apps, APIs, mobile apps, desktop apps, scripts

## Requirements

- Claude Code desktop application
- Git (for cloning)

## Why This Saves Time

**Without these commands**: Write Claude Code prompts from scratch, learn through trial and error, repeat common patterns.

**With these commands**: Use proven patterns immediately, commands adapt automatically to your project.

## FAQ

**Do these commands work with my tech stack?**
Yes - they automatically adapt to any programming language or framework.

**Can I add more commands later?**
Yes - you can copy additional commands from the full template library if needed.

**What if I need project-specific customization?**
The commands work universally, but you can modify them in your `.claude/commands/` directory.

## Getting Help

- Start with `/help` command in Claude Code
- Use `/task "what you want to accomplish"` for most development needs
- Commands provide detailed examples and explanations

## Advanced Usage

**Need more commands?** This repo also contains a comprehensive template library with 64+ additional commands that require manual customization. See `./setup.sh` and `README-MINIMAL.md` for details.

## License

MIT - Use freely in your projects.

---

*7 essential commands that work immediately with any programming language or framework.*