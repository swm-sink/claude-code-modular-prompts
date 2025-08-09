# Claude Code Native Architecture Research Findings
*Date: 2025-01-09*
*Sources: Web search validated*

## 🎯 CRITICAL DISCOVERIES

### 1. Standard Claude Code Structure (2025)
```
project/
├── CLAUDE.md                  # Project context (auto-loaded)
├── CLAUDE.local.md           # Personal context (gitignored)
├── .claude/
│   ├── commands/             # Custom slash commands
│   ├── agents/               # Sub-agents with YAML frontmatter
│   └── settings.json         # Claude Code configuration
```

### 2. Command Structure - REAL Implementation
```markdown
---
name: command-name
description: When to use this command
tools: Read, Write, Glob, Grep  # Optional - inherits all if omitted
---

# Command implementation goes here
# Use $ARGUMENTS for parameters
# Commands EXECUTE, don't instruct
```

### 3. XML Tags in CLAUDE.md - Now Standard Practice (2025)
```markdown
<system_context>
Brief overview of what this system does
</system_context>

<patterns>
Key patterns and conventions
</patterns>

<critical_notes>
Things that will break if done wrong
</critical_notes>

<file_map>
Pointers to important files
</file_map>
```

### 4. Sub-Agent Structure
```markdown
---
name: specialized-agent
description: Specific action-oriented description
tools: tool1, tool2  # Optional
---

Agent's system prompt here
```

## 🚨 ANTI-PATTERNS TO AVOID

### From Research:
1. **Shell scripts for Claude operations** - Everything should be commands
2. **Not running code to verify** - Code hallucinations are easily caught
3. **Giving up at first hallucination** - Normal and manageable
4. **Not using TDD** - Most effective counter to hallucination
5. **Overloading context** - Keep CLAUDE.md concise
6. **Not allowing "I don't know"** - Reduces false information

## ✅ BEST PRACTICES (2025 Validated)

### Essential Commands
- `/init` - Creates CLAUDE.md file
- `/ide` - IDE integration
- `/clear` - Clear context (use often)
- `/commit` - Automated git commits
- `/create-pr` - Pull request creation

### Operating Modes
- **Default**: Interactive approval
- **Auto-Edit**: Changes without permission
- **Plan**: Start here for new features
- **Extended Thinking**: think < think hard < think harder < ultrathink

### TDD Approach (Critical)
1. Robot builds test and mock
2. Next prompt makes mock real
3. Most effective against hallucination
4. Robots "love" TDD approach

### Context Management
- CLAUDE.md in root or parent directories
- Project commands: `.claude/commands/`
- Personal commands: `~/.claude/commands/`
- Check into git for team sharing

## 📊 COMMUNITY INSIGHTS

### Working Implementations Found:
- **awesome-claude-code**: Curated collections of commands
- **Claude Command Suite**: 119+ custom commands, 54 agents
- **Workflow patterns**: ~150 LOC markdown workflows
- **State machine patterns**: Guide through distinct phases

### Key Patterns:
- Commands as markdown in `.claude/commands/`
- Workflows as prompts, not scripts
- Integration with dev tools (git, GitHub CLI)
- Multi-step workflows in single commands

## 🔧 TECHNICAL REQUIREMENTS

### Frontmatter Fields (Standard)
- `name`: Command identifier
- `description`: When to invoke
- `tools`: Optional tool list
- `usage`: How to call command

### File Naming
- Filename (minus .md) becomes command name
- Project commands: `/project:command-name`
- User commands: `/user:command-name`

### Permissions
- `claude --dangerously-skip-permissions` to avoid prompts
- Read-only by default
- Explicit permission for modifications

## 🎯 IMPLICATIONS FOR OUR PROJECT

### What We Got RIGHT:
- Using CLAUDE.md for project context
- XML semantic tagging approach
- Focus on executable commands

### What We Got WRONG:
- Shell scripts shouldn't exist
- Commands should be in .claude/commands/
- Sub-agents should use standard structure
- Don't need complex YAML configs

### What We MISSED:
- TDD as primary anti-hallucination strategy
- Extended thinking modes built-in
- Community has extensive libraries
- Workflows as markdown prompts

## 📝 UPDATED UNDERSTANDING

Claude Code in 2025 is:
1. **Markdown-first**: Everything is markdown with YAML frontmatter
2. **XML-enhanced**: Semantic tags for structure
3. **Command-driven**: Slash commands for everything
4. **TDD-focused**: Testing prevents hallucination
5. **Community-rich**: Extensive libraries available
6. **Shell-free**: No external scripts needed

## 🚀 RECOMMENDATIONS

1. **Adopt standard structure**: .claude/commands/, .claude/agents/
2. **Use XML tags**: Already standard practice
3. **Implement TDD**: Critical for reliability
4. **Study community**: Learn from working implementations
5. **No shell scripts**: Everything as Claude commands
6. **Keep it simple**: Concise CLAUDE.md, clear commands

---
*This research validates our pure Claude native approach but requires adjustments to match 2025 standards*