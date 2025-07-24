# User Guide - Claude Code Modular Prompts Framework

## Table of Contents
- [User Guide - Claude Code Modular Prompts Framework](#user-guide---claude-code-modular-prompts-framework)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Learning Path](#learning-path)
    - [🎯 **Foundation Level** (0-1 hours)](#-foundation-level-0-1-hours)
    - [🔧 **Intermediate Level** (1-5 hours)](#-intermediate-level-1-5-hours)
    - [🚀 **Advanced Level** (5+ hours)](#-advanced-level-5-hours)
    - [🏆 **Expert Level** (10+ hours)](#-expert-level-10-hours)
  - [Quick Reference](#quick-reference)
    - [Essential Commands Summary](#essential-commands-summary)
    - [Getting Help](#getting-help)
  - [Contributing](#contributing)
  - [Next Steps](#next-steps)
  - [Quick Links](#quick-links)

## Overview
This user guide provides comprehensive documentation for mastering the Claude Code Modular Prompts Framework. Follow the progressive skill-building path below to go from beginner to expert.

**New to the framework?** Start with the [Getting Started Guide](../../GETTING_STARTED.md) for 5-minute setup.

**Looking for quick answers?** Check the [CLAUDE.md Quick Reference](../../CLAUDE.md#quick-reference) or [FAQ](faq.md).

**Need help with issues?** See the [Troubleshooting Guide](troubleshooting.md).

## Learning Path

### 🎯 **Foundation Level** (0-1 hours)
**Goal**: Get framework working and understand basic concepts

1. **[Getting Started](../../GETTING_STARTED.md)** - 5-minute setup
2. **[Basic Commands](commands/README.md)** - Essential command overview
3. **[Quick Examples](../../examples/01-beginner/)** - Try working examples

**Success Criteria**: Can use `/auto`, `/task`, `/feature`, `/query` commands successfully

---

### 🔧 **Intermediate Level** (1-5 hours)
**Goal**: Master all commands and understand quality enforcement

1. **[Command Examples](../../examples/01-beginner/basic-commands/)** - Hands-on command learning
   - [Auto Command](../../examples/01-beginner/basic-commands/auto-command.md) - Intelligent routing
   - [Task Command](../../examples/01-beginner/basic-commands/task-command.md) - Focused TDD development
   - [Query Command](../../examples/01-beginner/basic-commands/query-command.md) - Research and analysis

2. **[Workflow Patterns](../../examples/02-intermediate/multi-command-workflows/)** - Real-world usage patterns
   - [Bug Investigation Workflow](../../examples/02-intermediate/multi-command-workflows/bug-investigation.md)
   - [Feature Development Workflow](../../examples/02-intermediate/multi-command-workflows/feature-development.md)
   - [Refactoring Workflow](../../examples/02-intermediate/multi-command-workflows/refactoring-workflow.md)

3. **[Quality Enforcement](quality-enforcement.md)** - Understanding TDD and quality gates

**Success Criteria**: Can choose the right command for any task and understand quality enforcement

---

### 🚀 **Advanced Level** (5+ hours)
**Goal**: Customize framework, create modules, and use meta-prompting

1. **[Advanced Usage](../advanced/)** - Advanced techniques
   - [Custom Modules](../advanced/custom-modules.md)
   - [Meta-Prompting](../advanced/meta-prompting.md)
   - [Framework Customization](../advanced/framework-customization.md)

2. **[Project Configuration](project-configuration.md)** - Deep PROJECT_CONFIG.xml customization

3. **[Team Integration](team-integration.md)** - Multi-developer workflows

**Success Criteria**: Can extend framework with custom modules and optimize for team workflows

---

### 🏆 **Expert Level** (10+ hours)
**Goal**: Contribute to framework and create sophisticated customizations

1. **[Framework Development](framework-development.md)** - Contributing to the framework
2. **[Architecture Deep Dive](architecture-deep-dive.md)** - Understanding framework internals
3. **[Performance Optimization](performance-optimization.md)** - Optimizing for scale

**Success Criteria**: Can contribute modules, optimize performance, and help others

---

## Quick Reference

For a comprehensive quick reference including commands, workflows, configuration, and troubleshooting, see the [CLAUDE.md Quick Reference](../../CLAUDE.md#quick-reference).

### Essential Commands Summary
- **[/auto](../../examples/01-beginner/basic-commands/auto-command.md)** - Intelligent routing when uncertain
- **[/task](../../examples/01-beginner/basic-commands/task-command.md)** - Single component with TDD
- **[/query](../../examples/01-beginner/basic-commands/query-command.md)** - Research without modifications

For hands-on command learning, see the [Command Examples](../../examples/01-beginner/basic-commands/).

### Getting Help

1. **[Troubleshooting Guide](troubleshooting.md)** - Common issues and solutions
2. **[FAQ](faq.md)** - Frequently asked questions
3. **[GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)** - Report bugs
4. **Framework Help**: Use `/query "framework question"` for framework-specific help

## Contributing

We welcome contributions to improve the user guide:

1. **Documentation**: Improve existing guides or add new ones
2. **Examples**: Add real-world usage examples
3. **Workflows**: Share successful workflow patterns
4. **Issues**: Report documentation bugs or gaps

See [Contributing Guidelines](../../CONTRIBUTING.md) for details.

---

## Next Steps

1. **Start with Foundation**: Complete [Getting Started](../../GETTING_STARTED.md)
2. **Try Examples**: Work through [Quick Start Examples](../../examples/01-beginner/)
3. **Master Commands**: Read [Command Guides](commands/)
4. **Build Skills**: Progress through the learning path at your own pace

> 💡 **Tip**: The framework learns from your usage patterns. The more you use it, the better it becomes at understanding your specific needs and coding style.

## Quick Links

- **[Getting Started](../../GETTING_STARTED.md)** - Setup and first steps
- **[Examples](../../examples/)** - Working examples
- **[Command Examples](../../examples/01-beginner/basic-commands/)** - Hands-on command learning
- **[Workflow Examples](../../examples/02-intermediate/multi-command-workflows/)** - Real-world patterns
- **[Advanced](../advanced/)** - Advanced techniques
- **[PROJECT_CONFIG.xml](../../PROJECT_CONFIG.xml)** - Configuration template