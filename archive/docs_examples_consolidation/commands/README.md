# Command Documentation

## Overview
This directory contains detailed documentation for each framework command. For quick reference, see the [CLAUDE.md Quick Reference](../../../CLAUDE.md#quick-reference).

## Command Index

### Core Commands
- [Auto Command](auto-command.md) - Intelligent routing when uncertain about approach
- [Task Command](task-command.md) - Single component focused development with TDD
- [Feature Command](feature-command.md) - Complete feature lifecycle with PRD
- [Query Command](query-command.md) - Research and analysis without modifications

### Coordination Commands
- [Swarm Command](swarm-command.md) - Multi-agent coordination for complex tasks
- [Session Command](session-command.md) - Long-running work with context preservation
- [Protocol Command](protocol-command.md) - Production-ready workflows with safety

### Support Commands
- [Docs Command](docs-command.md) - Documentation generation and management

### Meta Commands
- [Meta Review](meta-review-command.md) - Framework performance analysis
- [Meta Optimize](meta-optimize-command.md) - Framework performance improvement
- [Meta Evolve](meta-evolve-command.md) - Framework adaptation and learning

## Usage Guidelines

### Command Selection Decision Tree
```
Single task <50 lines → /task
Multiple files → /feature
Research/analysis → /query
Uncertain approach → /auto
Complex coordination → /swarm
Extended work → /session
Production deployment → /protocol
Documentation → /docs
```

### Best Practices
1. **Start with /auto** when unsure which command to use
2. **Use /query** to understand code before modifying
3. **Follow TDD** - all commands enforce test-driven development
4. **Check quality gates** - ensure standards are met before completion

## Next Steps
1. Read the individual command documentation for detailed usage
2. Try the [examples](../../../examples/) for hands-on learning
3. Progress through the [learning path](../README.md#learning-path)