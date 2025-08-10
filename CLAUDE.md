# Conductor Commands - Claude Code Project Context

## What This Project Actually Is

**Conductor Commands** is a collection of simple Claude Code slash commands (markdown files) that guide Claude to take specific actions using its native tools. This is a pure Claude Code native project - everything happens within Claude conversations.

## Current Project State

### Actual Structure
```
lisbon/
├── .claude/
│   ├── commands/        # 22 working commands (20 main + 2 initialization)
│   │   └── initialization/  # 2 setup commands
│   └── settings.json    # Claude Code configuration
├── docs/                # Documentation and analysis
├── CLAUDE.md           # This file - project context
├── README.md           # User-facing documentation
├── claude.todos.yaml   # Development tracking
└── claude.local.md     # Session state (git-ignored)
```

### What Exists
- **22 Claude Code commands** in `.claude/commands/` (20 main + 2 initialization)
- **Simple prompts** that make Claude use its tools (Read, Write, WebSearch, etc.)
- **Optimized commands** (most 30-45 lines)
- **Documentation** explaining the approach

### What Does NOT Exist
- No `.claude-architect/` directory
- No complex agent orchestration system
- No shell scripts or Python scripts
- No elaborate YAML configuration files
- No persistent state management
- No multi-phase consultation system

## Core Understanding

### Commands Are Prompts, Not Programs
Claude Code commands are markdown files that:
- Guide Claude's behavior in conversations
- Tell Claude which tools to use
- Are stateless (no memory between invocations)
- Should be simple and action-oriented

### Design Principles
1. **Simplicity**: Commands should be 40-50 lines ideally
2. **Action-oriented**: Commands make Claude DO things, not describe things
3. **Tool-focused**: Heavy use of Claude's native tools
4. **Honest**: Only promise what can actually be delivered

## Available Commands

### Getting Started
- `/welcome` - Interactive guide for new users
- `/help` - Get help with commands
- `/orchestrate` - Quick project setup
- `/setup` - Initialize Claude Code structure

### Core Analysis
- `/project-analysis` - Analyze codebase  
- `/anti-pattern-audit` - Find and fix issues
- `/context-generation` - Create CLAUDE.md
- `/discover` - Discover project patterns

### Development
- `/implement` - Build features with TDD
- `/plan` - Plan implementation
- `/generate` - Generate code/commands
- `/validate` - Check code quality
- `/refactor` - Safe code improvement
- `/debug` - Interactive debugging

### Testing
- `/test-unit` - Create unit tests
- `/test-integration` - Integration tests
- `/test-e2e` - End-to-end tests

### Utilities
- `/commit` - Create git commits
- `/explore` - Investigate codebase
- `/deploy` - Deployment preparation

### Initialization (in .claude/commands/initialization/)
- `/initialize` - Basic initialization
- `/quick-setup` - Fast setup

## How Commands Work

1. User types command in Claude Code conversation
2. Claude reads the command's markdown file
3. Claude follows instructions to use tools
4. User gets concrete results

Example:
```bash
/project-analysis
# Claude uses Glob, Read, Grep to analyze project
# Provides actionable insights
```

## Development Guidelines

### Creating New Commands
- Keep under 100 lines (40-50 ideal)
- Use YAML frontmatter correctly
- Specify allowed-tools
- Write clear, actionable instructions
- Test in actual Claude Code

### YAML Frontmatter Format
```yaml
---
name: command-name
description: Brief description
usage: "/command-name [args]"
allowed-tools: [Read, Write, WebSearch]
---
```

### Anti-Patterns to Avoid
- Don't create 800-line "god commands"
- Don't use XML pseudo-code that doesn't execute
- Don't promise features that don't exist
- Don't create complex multi-phase processes

## Project Philosophy

### What We Believe
- **Simplicity over complexity**
- **Action over documentation**
- **Tools over theater**
- **Honesty over marketing**

### What We Reject
- Complex orchestration that doesn't work
- Promises of non-existent features
- Overly complex command structures
- Documentation pretending to be functionality

## Testing Approach

Since Claude Code commands are prompts, not programs, "testing" means:
1. Validating command syntax (YAML frontmatter)
2. Testing commands produce expected outcomes
3. Ensuring no hallucinations or drift
4. Verifying reasonable execution time

See `TESTING-STRATEGY.md` for details.

## Maintenance

### Key Files
- **This file (CLAUDE.md)**: Project context and truth
- **README.md**: User documentation
- **claude.todos.yaml**: Development tracking
- **PROJECT-STATUS.md**: Current status report

### Documentation Strategy
- One fact, one location
- Reference, don't duplicate
- Keep documentation aligned with reality
- Update immediately when things change

## Current State

All 22 commands follow our simplicity principle:
- Commands optimized to 30-45 lines (most under 40)
- XML pseudo-code has been removed
- Commands are action-oriented prompts
- No complex orchestration or frameworks
- Three new essential commands added (debug, refactor, deploy)
- Performance optimized (reduced token usage by ~30%)

## For LLM Agents

### When working on this project:
1. Commands are prompts that guide Claude's behavior
2. Keep commands simple (40-50 lines)
3. Use Claude's native tools directly
4. Don't create complex systems that can't work in stateless environment
5. Test commands by running them in Claude Code

### Available tools you should use in commands:
- Read, Write, Edit, MultiEdit
- Glob, Grep, LS
- WebSearch, WebFetch
- Bash (with appropriate restrictions)
- Task (for sub-agents)
- TodoWrite

### Remember:
- Claude Code is stateless between invocations
- Commands cannot persist data between runs
- Everything happens in conversation context
- Simplicity is the ultimate sophistication

---

*Last updated: 2025-01-10*
*This file is the single source of truth for project context*