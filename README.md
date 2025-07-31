# Claude Code Modular Prompts - Template Library

**Comprehensive collection of 88 Claude Code command templates with 94 reusable components for rapid project customization.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-green.svg)](https://github.com/swm-sink/claude-code-modular-prompts/releases)

## 🚀 Quick Start (30 seconds)

```bash
# Install template library
./setup.sh /path/to/your/project

# Start using immediately (in Claude Code)
/help                              # See all commands
/task "add user authentication"    # Execute any development task
/analyze "why is my app slow?"     # Analyze code or problems
```

**Templates require customization - use guide commands for step-by-step help.**

## What You Get

**88 Command Templates:**
- **Core Commands** (12): Essential development workflows
- **Quality Commands** (12): Testing, validation, analysis tools
- **Specialized Commands** (11): Advanced workflows and patterns
- **Meta Commands** + others (53): Template adaptation, management, and specialized tools

**94 Reusable Components:**
- **Atomic Components** (21): Simple building blocks
- **Regular Components** (73): Complex reusable patterns

**Template Library Features:**
- Manual customization guides with placeholder replacement
- Anti-pattern documentation (48+ documented pitfalls)
- Multiple integration methods (git submodule, direct copy, selective)
- Comprehensive testing and validation frameworks

## How It Works

1. **Import Templates**: Choose integration method (git submodule recommended)
2. **Customize**: Use guide commands like `/adapt-to-project` for customization checklists
3. **Replace Placeholders**: Manual find/replace of [INSERT_XXX] placeholders in your editor
4. **Validate**: Use `/validate-adaptation` to verify your customizations
5. **Maintain**: Use `/sync-from-reference` for updates from the template library

## Installation Methods

### Method 1: Git Submodule (Recommended)
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh
```

### Method 2: Direct Integration
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../your-project
```

### Method 3: Selective Copy
Choose specific commands/components to copy manually.

## Usage Examples

**Template Customization:**
```
/adapt-to-project           # Get customization checklist
/replace-placeholders       # See all placeholders to replace
/validate-adaptation        # Verify your customizations
```

**Command Template Usage:**
```
/task "implement authentication"    # Use customized task template
/test "run integration tests"       # Use customized test template  
/analyze "performance bottlenecks"  # Use customized analysis template
```

**Component Assembly:**
```
# Build custom commands from atomic components
# Copy from .claude/components/atomic/ into your slash commands
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

**Need more commands?** This repo also contains:

1. **Template Library**: 81+ additional command templates that require manual customization. See `./setup.sh` for details.

2. **Atomic Components**: 21 simple building blocks (5-10 lines each) for creating custom commands:
   - Input validation, output formatting, error handling
   - File operations, search functionality, progress indicators  
   - See `.claude/COMPONENT-ASSEMBLY-GUIDE.md` for usage

**Note**: The template library and components require manual work. Only the 7 core commands work immediately without customization.

## License

MIT - Use freely in your projects.

---

*7 essential commands that work immediately with any programming language or framework.*