# Developer Guide

## Claude Code Context Engineering Framework

Welcome to the developer guide for the Claude Code Context Engineering framework. This guide explains how to use the research-driven system to build robust context for your Claude Code projects.

## Quick Start

### 1. Installation as Git Submodule

```bash
cd your-project
git submodule add https://github.com/USER/claude-code-modular-prompts.git .claude-context
cd .claude-context
./setup.sh
```

### 2. Follow the Numbered Commands

The framework provides 35 numbered scaffolding commands organized by phase:

```
Phase -1: Context Foundation (5 commands)
Phase 0: Environment Verification (3 commands)  
Phase 1: Research-Driven Patterns (5 commands)
Phase 2: Context Engineering (5 commands)
Phase 3: Agent Architecture (5 commands)
Phase 4: Command Engineering (3 commands)
Phase 5: Integration & Validation (4 commands)
Phase 6: Team Collaboration (2 commands)
Phase 7: Continuous Improvement (2 commands)
```

Start with Phase -1 and work through sequentially.

## Core Concepts

### Research-Driven Approach

Every decision is backed by evidence using the VERIFY protocol:
- **V**alidate sources and claims
- **E**vidence-based documentation
- **R**eference authoritative sources
- **I**ntegrate multiple perspectives
- **F**act-check all assertions
- **Y**ield verifiable outcomes

### Context Engineering

Instead of 100+ commands, focus on building rich context that Claude can use:
- Context templates in `.claude/context/`
- Research findings in `.claude/research/`
- Team knowledge in `CLAUDE.md`

### Agent Architecture

5 specialized agents handle specific aspects:
1. `context-engineer` - Manages context structures
2. `research-validator` - Validates sources
3. `pattern-extractor` - Extracts patterns
4. `discovery-navigator` - Finds relevant context
5. `integration-assistant` - Helps integration

## Framework Structure

```
.claude-context/                    # Git submodule root
├── .claude/
│   └── framework/
│       ├── agents/                # 5 framework agents
│       ├── commands/              # 35 numbered commands
│       ├── context/               # Context templates
│       └── docs/                  # Documentation
├── .submodule/
│   ├── detect_mode.sh            # Mode detection
│   ├── setup.sh                  # Initial setup
│   └── templates/                # Integration templates
└── .transformation/              # Stage 1 only (not in submodule)
```

## Using the Commands

### Command Naming Convention

Commands are numbered to indicate execution order:
- `-1_*` - Pre-foundation setup
- `0_*` - Environment verification
- `1_*` through `7_*` - Main phases

### Example: Starting a New Project

```bash
# Phase -1: Set up context foundation
/-1_init_context

# Phase 0: Verify environment
/0_verify_setup

# Phase 1: Extract research patterns
/1_extract_patterns

# Continue through phases...
```

### Command Structure

Each command follows a research-driven pattern:

```markdown
---
name: command-name
description: What it does
allowed-tools: [Read, Write, Edit, Bash]
---

## Purpose
Clear statement of intent backed by research

## Research Foundation
- Links to relevant research
- Evidence for approach
- Anti-patterns to avoid

## Implementation
Step-by-step process with validation
```

## Working with Agents

### Agent Invocation

Agents are invoked through commands:

```bash
# Use pattern extractor
/3_invoke_agent pattern-extractor

# Use research validator
/3_invoke_agent research-validator
```

### Agent Specialization

Each agent has a specific role:
- Don't use `context-engineer` for validation
- Don't use `research-validator` for extraction
- Match agent to task for best results

## Context Templates

### Creating New Context

Use provided templates:

```bash
# Create project context
cp .claude/framework/context/templates/PROJECT_CONTEXT.md .claude/context/

# Create team knowledge
cp .claude/framework/context/templates/TEAM_KNOWLEDGE.md CLAUDE.md
```

### Context Best Practices

1. **Be specific** - Concrete examples over abstractions
2. **Include evidence** - Link to sources
3. **Document decisions** - Explain why
4. **Update regularly** - Context evolves

## Integration Patterns

### For Existing Projects

1. Add as submodule
2. Run setup.sh
3. Use `-1_analyze_existing` to understand current state
4. Build context incrementally

### For New Projects

1. Add as submodule
2. Run setup.sh
3. Start with Phase -1 commands
4. Build context as you develop

### For Teams

1. Share via git
2. Use Phase 6 collaboration commands
3. Maintain team knowledge in CLAUDE.md
4. Regular context reviews

## Validation & Quality

### VERIFY Protocol

Always validate:
```bash
# Validate context structure
/5_validate_context

# Verify research sources
/1_verify_research

# Check integration
/5_integration_check
```

### Anti-Pattern Prevention

Common pitfalls:
- Creating too many commands (use context instead)
- Skipping research phase (always validate)
- Ignoring team knowledge (document everything)
- Breaking the numbered flow (follow phases)

## Troubleshooting

See `TROUBLESHOOTING.md` for common issues.

## Advanced Usage

### Custom Agents

Create specialized agents:
```bash
# Use agent template
/4_create_agent my-specialist
```

### Context Hierarchies

Build layered context:
- Global: Framework templates
- Project: Your customizations
- Team: Shared knowledge
- Personal: Local overrides

### Performance Optimization

- Use file hop patterns
- Minimize context size
- Regular context pruning
- Efficient research storage

## Next Steps

1. Complete Phase -1 setup
2. Verify environment (Phase 0)
3. Extract initial patterns (Phase 1)
4. Build your context systematically
5. Validate and iterate

Remember: The goal is rich context, not many commands. Quality over quantity.