# Claude Code Best Practices

*Based on research from 50+ sources including official Anthropic documentation, community best practices, and proven patterns from 2025.*

## Core Principles

### Context Engineering Over Prompt Engineering
- **Context engineering is 10x better than prompt engineering** - manage what Claude knows and when
- Use CLAUDE.md for persistent project memory that survives sessions
- Optimize context window with /clear, /compact, and strategic file loading
- Keep CLAUDE.md under 5k tokens - split larger content into separate files

### Token Optimization Strategies
- Use /clear frequently between unrelated tasks to reset context
- Monitor context window usage - when approaching 50% of limit, summarize with /compact
- Exclude noise: node_modules/, .git/, *.log files from context loading
- Create lean, focused files rather than large monolithic ones

## Slash Commands Best Practices

### YAML Frontmatter Structure
```yaml
---
name: /command-name
description: "Clear description of what this command does"
usage: /command-name [arguments]
category: core|development|quality|specialized
tools: Read, Write, Edit, MultiEdit, Bash, Grep, Glob, LS
---
```

### Command Design Patterns
- **One command, one clear purpose** - avoid multi-function commands
- **Use $ARGUMENTS for parameterization** - enables flexible command usage
- **Natural language instructions** - write commands as clear prompts
- **Include examples** - show expected usage patterns

## Automation Features

### Hooks for True Automation
- **PreToolUse**: Execute before Claude uses specific tools
- **PostToolUse**: Execute after successful tool usage
- **Notification**: Execute when Claude sends notifications
- **Stop**: Execute when Claude finishes generating response

### Headless Mode for CI/CD
```bash
# Basic headless execution
claude -p "analyze codebase for security issues"

# With JSON output for parsing
claude -p "run tests and report results" --output-format stream-json
```

## Team Collaboration

### Shared Command Libraries
- Store commands in `.claude/commands/` and commit to git
- Use consistent YAML frontmatter across team
- Create team-specific commands in `.claude/commands/team/`
- Document project-specific patterns in CLAUDE.md

### Permission Management
- Use read-only permissions by default for safety
- Require explicit approval for file modifications
- Block dangerous commands: rm, sudo, curl, wget
- Allow auto-approval for safe tools: Read, Grep, Glob, LS

## Performance Optimization

### Context Window Management
- **Maximum effective context**: ~150,000 tokens (Claude 4)
- **Optimal session length**: Use /clear when context gets noisy
- **Strategic file loading**: Only include relevant files in context
- **Memory management**: Use persistent memory for important project info

### Sub-Agents for Parallelization
- Create specialized sub-agents for specific tasks
- Store in `.claude/agents/` directory with YAML frontmatter
- Use for parallel processing of complex problems
- Define clear boundaries and responsibilities

## Security Best Practices

### Data Protection
- Never include production secrets or API keys in prompts
- Use placeholder values or configuration examples
- Exclude sensitive directories: ~/.ssh/, /etc/, credentials/
- Limit file size processing to prevent memory issues

### Safe Command Execution
- Always review bash commands before execution
- Use virtual environments for untrusted code execution
- Implement command approval workflows for destructive operations
- Monitor file access patterns for anomalies

## Common Anti-Patterns to Avoid

### False Automation Promises
- ❌ Commands that claim automation but only provide instructions
- ❌ "Interactive" commands that require extensive manual work
- ❌ Placeholder systems that break when not customized

### Context Window Waste
- ❌ Loading entire codebases into context indiscriminately
- ❌ Keeping irrelevant conversation history
- ❌ Including generated reports and logs in active context

### Prompt Engineering Mistakes
- ❌ Overly complex multi-step orchestration
- ❌ Generic commands that try to do everything
- ❌ Missing examples and usage patterns

## Framework Detection Patterns

### Common Project Files to Scan
```javascript
// JavaScript/Node.js
package.json, package-lock.json, yarn.lock

// Python  
requirements.txt, setup.py, pyproject.toml, Pipfile

// Java
pom.xml, build.gradle, build.xml

// Other Languages
go.mod (Go), Cargo.toml (Rust), composer.json (PHP), Gemfile (Ruby)
```

### Automated Configuration
- Detect tech stack from project files
- Set appropriate tools and permissions
- Configure language-specific commands
- Enable framework-specific validations

This context file should be automatically loaded by Claude Code to inform all command responses with research-validated best practices.