---
name: /help
description: "Get help with available commands and Claude Code usage"
usage: /help [command-name]
category: core
tools: Read, Grep
---

# Claude Code Command Help

## Available Commands

### Core Commands
- **`/help`** - This help system (shows all commands)
- **`/task`** - Execute any development task
- **`/analyze`** - Analyze code, architecture, or problems
- **`/review`** - Code review and suggestions
- **`/debug`** - Debug issues and errors

### Specialized Commands  
- **`/test`** - Generate and run tests
- **`/docs`** - Create documentation
- **`/optimize`** - Performance optimization
- **`/secure`** - Security analysis
- **`/deploy`** - Deployment assistance

## How to Use Commands

**Basic Usage:**
```
/task "add user authentication to my app"
/analyze "why is my API slow?"
/review src/components/UserForm.jsx
/debug "login fails with 500 error"
```

**Command Help:**
```
/help task     # Get detailed help for /task command
/help analyze  # Get detailed help for /analyze command
```

## Tips for Effective Usage

1. **Be Specific**: Instead of "help me code", try "/task 'add JWT authentication to Express API'"

2. **Provide Context**: Include file paths, error messages, or specific requirements

3. **Use Natural Language**: Commands understand conversational requests

4. **Iterate**: Start with broad requests, then refine based on results

## Command Categories

- **Development**: `/task`, `/analyze`, `/review`, `/debug`
- **Quality**: `/test`, `/optimize`, `/secure`  
- **Documentation**: `/docs`, `/help`
- **Operations**: `/deploy`

All commands work with any programming language, framework, or project type.

Ready to start? Try: `/task "your development goal here"`