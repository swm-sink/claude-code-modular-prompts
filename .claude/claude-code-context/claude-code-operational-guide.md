# Claude Code Operational Guide

*Critical operational knowledge for Claude Code template development*

## 🎯 Core Understanding

### Claude Code Native Tools (MANDATORY USE)
```
File Operations:
- Read        → Use instead of: cat, head, tail, less
- Write       → Use instead of: echo >, touch
- Edit        → Use instead of: sed, awk
- MultiEdit   → Use for: multiple edits in one file

Search Operations:
- Glob        → Use instead of: find
- Grep        → Use instead of: grep (uses ripgrep internally)
- LS          → Use instead of: ls

System:
- Bash        → Use for: git, npm, other system commands
- WebSearch   → Use for: finding documentation
- WebFetch    → Use for: retrieving web content
```

### Command Structure Reality
```
.claude/
├── commands/           # Slash commands (markdown files)
│   ├── core/          # Namespaced as /core:command
│   └── dev/           # Namespaced as /dev:command
├── agents/            # Sub-agents (markdown files)
├── settings.json      # Hooks and configuration
└── CLAUDE.md         # Project context (auto-loaded)
```

### YAML Frontmatter (Correct Format)
```yaml
---
name: command-name
description: Brief description
usage: "command-name [args]"
allowed-tools: [Read, Write, Edit, Bash]
argument-hint: "file-path | --option"
model: opus
---
```

## 🚨 Critical Limitations

### Context Window Management
- **Size**: 200k tokens (~150k words) maximum
- **Cost**: Every message includes full history
- **Reset**: Use `/clear` or `/compact` when needed
- **CLAUDE.md**: Keep under 5k tokens

### Usage Limits (Claude.ai)
- **Session**: 5-hour rolling window
- **Pro**: 40-80 hours/week
- **Max**: Higher limits, same window
- **API**: Separate, pay-per-token

### Stateless Nature
- No memory between sessions
- Entire context reloaded each time
- Project state via CLAUDE.md only
- No persistent variables

## ✅ What Actually Works

### Real Features
1. **Slash Commands**: Markdown templates in `.claude/commands/`
2. **Sub-Agents**: Specialized prompts in `.claude/agents/`
3. **Hooks**: Automation via `settings.json`
4. **MCP**: External tool integration
5. **Headless Mode**: `claude -p "prompt"`

### Proven Patterns
1. **Self-contained commands**: Each command complete
2. **Clear instructions**: Direct, specific prompts
3. **Tool usage**: Explicit tool specifications
4. **Batch operations**: Multiple ops in one call
5. **Context management**: Strategic use of CLAUDE.md

## ❌ What Doesn't Work

### Fictional Features (Avoid)
1. **Dynamic component loading**: No runtime assembly
2. **Dependency resolution**: No automatic management
3. **State management**: No persistence between runs
4. **Component composition**: No real framework
5. **Automated orchestration**: Just markdown instructions

### Anti-Patterns
1. **Over-abstraction**: Complex frameworks
2. **False promises**: "Automated" features that aren't
3. **XML metadata**: Unused by Claude Code
4. **Component dependencies**: Not actually resolved
5. **Integration claims**: No real system integration

## 🔧 Hooks Configuration

### Working Example
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "npm run format"
      }]
    }]
  }
}
```

### Hook Events
- `PreToolUse`: Before tool execution
- `PostToolUse`: After tool success
- `UserPromptSubmit`: On prompt submission
- `Stop`: When Claude finishes

## 🚀 Best Practices

### Command Design
1. **Single Purpose**: One task per command
2. **Clear Names**: `/dev:test-unit` not `/test`
3. **Arguments**: Use `$ARGUMENTS` placeholder
4. **Examples**: Include usage examples
5. **Tools**: Specify `allowed-tools` explicitly

### Project Setup
1. **CLAUDE.md**: Project overview and context
2. **Commands**: Organized by namespace
3. **Agents**: Specialized sub-agents
4. **Settings**: Hooks and automation
5. **Documentation**: Clear, honest, accurate

### Performance
1. **Batch Operations**: Multiple tools in one response
2. **Context Pruning**: Regular cleanup
3. **Model Selection**: Right model for task
4. **Token Awareness**: Monitor usage
5. **Session Planning**: Strategic timing

## 📊 Reality Check

### What This Means for Templates
1. **Templates are prompts**: Not executable code
2. **Commands are independent**: No real dependencies
3. **Agents are instructions**: Not running processes
4. **Components are snippets**: Not loadable modules
5. **Framework is conceptual**: Not functional

### Honest Capabilities
- ✅ Reusable prompt templates
- ✅ Organized command structure
- ✅ Markdown-based configuration
- ✅ Git-shareable workflows
- ✅ Team collaboration via commands

### Not Capabilities
- ❌ Runtime component assembly
- ❌ Dynamic dependency management
- ❌ State persistence
- ❌ Automated orchestration
- ❌ True framework functionality

## 🎯 Recommended Approach

### For This Project
1. **Simplify**: Remove complex abstractions
2. **Clarify**: Mark conceptual vs functional
3. **Focus**: Self-contained commands
4. **Document**: Honest capabilities
5. **Deliver**: Working templates, not frameworks

### Command Template Pattern
```markdown
---
name: feature-build
description: Build a new feature with tests
allowed-tools: [Read, Write, Edit, Bash, Grep]
---

# Build New Feature

I'll help you build a new feature. Here's my approach:

1. First, I'll understand the requirements
2. Then create the implementation with tests
3. Finally, ensure everything integrates properly

What feature would you like to build?
```

This pattern:
- Self-contained
- Clear purpose
- No false dependencies
- Direct value
- Honest capabilities