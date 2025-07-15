# User Guide - Claude Code Modular Prompts Framework

## Overview
This user guide provides comprehensive documentation for mastering the Claude Code Modular Prompts Framework. Follow the progressive skill-building path below to go from beginner to expert.

## Learning Path

### 🎯 **Foundation Level** (0-1 hours)
**Goal**: Get framework working and understand basic concepts

1. **[Getting Started](../../GETTING_STARTED.md)** - 5-minute setup
2. **[Basic Commands](commands/README.md)** - Essential command overview
3. **[Quick Examples](../../examples/quick-start/)** - Try working examples

**Success Criteria**: Can use `/auto`, `/task`, `/feature`, `/query` commands successfully

---

### 🔧 **Intermediate Level** (1-5 hours)
**Goal**: Master all commands and understand quality enforcement

1. **[Command Mastery](commands/)** - Deep dive into each command
   - [Auto Command](commands/auto-command.md) - Intelligent routing
   - [Task Command](commands/task-command.md) - Focused TDD development
   - [Feature Command](commands/feature-command.md) - Complete feature lifecycle
   - [Query Command](commands/query-command.md) - Research and analysis

2. **[Workflow Patterns](workflows/)** - Real-world usage patterns
   - [Bug Fixing Workflow](workflows/bug-fixing-workflow.md)
   - [Feature Development Workflow](workflows/feature-development-workflow.md)
   - [Code Research Workflow](workflows/code-research-workflow.md)

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

### Essential Commands
```bash
/auto "your request"          # Intelligent routing - use when unsure
/task "focused work"          # Single component with TDD
/feature "complete feature"   # Full feature lifecycle with PRD
/query "research question"    # Analysis without modifications
```

### Support Commands
```bash
/session "long-running work"  # Extended work sessions
/swarm "complex coordination" # Multi-agent coordination
/protocol "production work"   # Production-ready workflows
/docs "documentation"         # Documentation generation
```

### Meta Commands
```bash
/meta-review "analyze performance"    # Framework analysis
/meta-optimize "improve efficiency"   # Performance optimization
/meta-evolve "adapt to patterns"     # Adaptive learning
/meta-govern "enforce compliance"     # Governance and compliance
```

## Common Workflows

### New Feature Development
```bash
1. /query "understand existing related functionality"
2. /feature "implement new feature with requirements"
3. /task "add specific component or fix"
4. /protocol "prepare for production deployment"
```

### Bug Investigation and Fix
```bash
1. /query "analyze the bug and understand root cause"
2. /task "implement fix with comprehensive tests"
3. /protocol "ensure fix meets production standards"
```

### Code Research and Documentation
```bash
1. /query "analyze codebase and create documentation"
2. /docs "generate comprehensive documentation"
3. /task "add missing tests or improve coverage"
```

## Configuration Quick Start

### Basic PROJECT_CONFIG.xml
```xml
<project_config>
  <tech_stack>
    <primary_language>python</primary_language>
    <framework>django</framework>
  </tech_stack>
  <commands>
    <test>pytest --cov=src</test>
    <lint>flake8 src</lint>
  </commands>
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
    </test_coverage>
  </quality_standards>
</project_config>
```

## Troubleshooting

### Common Issues

**Issue**: Commands not working
- **Solution**: Check CLAUDE.md is in project root
- **Check**: Verify .claude directory exists

**Issue**: Generic responses
- **Solution**: Customize PROJECT_CONFIG.xml for your tech stack
- **Check**: Verify configuration is project-specific

**Issue**: Quality gates not enforcing
- **Solution**: Check quality_standards in PROJECT_CONFIG.xml
- **Check**: Verify enforcement is set to "blocking"

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
2. **Try Examples**: Work through [Quick Start Examples](../../examples/quick-start/)
3. **Master Commands**: Read [Command Guides](commands/)
4. **Build Skills**: Progress through the learning path at your own pace

> 💡 **Tip**: The framework learns from your usage patterns. The more you use it, the better it becomes at understanding your specific needs and coding style.

## Quick Links

- **[Getting Started](../../GETTING_STARTED.md)** - Setup and first steps
- **[Examples](../../examples/)** - Working examples
- **[Commands](commands/)** - Detailed command documentation
- **[Workflows](workflows/)** - Real-world patterns
- **[Advanced](../advanced/)** - Advanced techniques
- **[PROJECT_CONFIG.xml](../../PROJECT_CONFIG.xml)** - Configuration template