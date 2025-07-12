| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-12   | stable |

# Claude Code Framework 3.0 - Complete User Guide

> **The definitive guide to mastering the Claude Code Modular Prompts Framework with meta-prompting capabilities**

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Core Commands](#core-commands)
3. [Meta Commands](#meta-commands)
4. [Configuration System](#configuration-system)
5. [Quality Gates](#quality-gates)
6. [Advanced Features](#advanced-features)
7. [Troubleshooting](#troubleshooting)
8. [Best Practices](#best-practices)

---

## Quick Start

### Installation (2 minutes)

```bash
# Clone the framework
git clone https://github.com/swm-sink/claude-code-modular-prompts.git

# Copy to your project
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/
```

### First Commands (30 seconds)

```bash
# Not sure what to use? Start here:
/auto "Add user authentication to my app"

# Quick focused task:
/task "Fix the login bug"

# Just researching:
/query "How does our caching work?"
```

**You're ready to go!** The framework will guide you from here.

---

## Core Commands

### `/auto` - The Smart Router 🧠

**Purpose**: Meta-prompting intelligent routing with self-improvement

```bash
/auto "I need to add user authentication"
# → Analyzes your need
# → Routes to best command  
# → You don't need to think about which tool
```

**When to use**: When you're unsure which command to use

### `/task` - Focused Development 🎯

**Purpose**: Single component work with strict TDD enforcement

```bash
/task "Add password validation to the login form"
# → Single component work
# → Enforces TDD (tests first!)
# → Quick and focused
```

**When to use**: Bug fixes, small features, single component changes

### `/feature` - Complete Feature Development 🚀

**Purpose**: Full feature with PRD-driven approach

```bash
/feature "Build a shopping cart with checkout"
# → Creates Product Requirements Doc (PRD)
# → Plans MVP strategy
# → Implements systematically
# → Full test coverage
```

**When to use**: New features requiring comprehensive planning

### `/swarm` - Complex Multi-Component Work 👥

**Purpose**: Multi-agent coordination for complex projects

```bash
/swarm "Migrate from REST to GraphQL"
# → Creates GitHub tracking issue
# → Coordinates specialized modules
# → Handles dependencies
# → Tracks all progress
```

**When to use**: Architecture changes, multi-system work, complex refactoring

### `/query` - Research Without Changes 🔍

**Purpose**: Understanding code without modifications

```bash
/query "What design patterns are used in the auth system?"
# → Read-only analysis
# → No code modifications
# → Comprehensive report
```

**When to use**: Code analysis, architecture understanding, research

### `/docs` - Documentation Gateway 📚

**Purpose**: Documentation creation with FOCUS framework

```bash
/docs generate "API Guide"
# → Creates comprehensive documentation
# → Uses FOCUS framework
# → Maintains consistency
```

**When to use**: Creating or updating documentation

### `/session` - Session Management 📊

**Purpose**: Long-running work with GitHub tracking

```bash
/session create "feature work"
# → Creates GitHub issue
# → Tracks progress
# → Preserves context
```

**When to use**: Complex projects requiring tracking

### `/protocol` - Production Standards 🛡️

**Purpose**: Maximum quality enforcement for production

```bash
/protocol "deploy feature"
# → All quality gates enforced
# → Production-ready code
# → Maximum safety
```

**When to use**: Production-critical work

---

## Meta Commands

### `/meta-review` - Framework Audit 🔍

**Purpose**: Comprehensive framework audit and compliance reporting

```bash
/meta-review
# → Audits entire framework
# → Identifies issues
# → Provides remediation guidance
```

### `/meta-evolve` - Framework Evolution 🌱

**Purpose**: Safe framework evolution with human approval

```bash
/meta-evolve
# → Identifies improvement opportunities
# → Implements with safety boundaries
# → Human oversight maintained
```

### `/meta-optimize` - Performance Enhancement ⚡

**Purpose**: Continuous performance optimization

```bash
/meta-optimize
# → Analyzes usage patterns
# → Implements performance improvements
# → Tracks success metrics
```

### `/meta-govern` - Governance Framework 👑

**Purpose**: Policy enforcement with human oversight

```bash
/meta-govern
# → Enforces framework policies
# → Maintains safety boundaries
# → Provides human control
```

### `/meta-fix` - Compliance Diagnosis 🩺

**Purpose**: Automated issue diagnosis and correction

```bash
/meta-fix "TDD not followed"
# → Diagnoses specific issues
# → Provides guided remediation
# → Prevents recurrence
```

---

## Configuration System

### PROJECT_CONFIG.xml

The framework adapts to your project through `PROJECT_CONFIG.xml`:

```xml
<project_configuration version="1.0.0">
  <project_info>
    <name>Your Project</name>
    <domain>web-development</domain>
    <primary_language>typescript</primary_language>
  </project_info>
  
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>BLOCKING</enforcement>
    </test_coverage>
  </quality_standards>
  
  <!-- Full configuration options in PROJECT_CONFIG_TEMPLATE.md -->
</project_configuration>
```

### Dynamic Placeholders

The framework uses `[PROJECT_CONFIG: path | DEFAULT: value]` syntax:

```markdown
Test coverage: [PROJECT_CONFIG: quality_standards.test_coverage.threshold | DEFAULT: 90]%
Source directory: [PROJECT_CONFIG: project_structure.source_directory | DEFAULT: src]
```

### Configuration Tools

```bash
# Validate configuration
python scripts/framework/config_validator.py

# Test placeholder resolution  
python scripts/framework/template_resolver.py --text "Coverage: [PROJECT_CONFIG: quality_standards.test_coverage.threshold | DEFAULT: 90]%"

# Generate minimal config
python scripts/framework/config_validator.py --generate "My Project" --domain web-development --language typescript
```

---

## Quality Gates

### TDD Enforcement

**Mandatory RED→GREEN→REFACTOR cycle**:

1. **RED**: Write failing tests first
2. **GREEN**: Minimal code to pass tests  
3. **REFACTOR**: Improve design while keeping tests green

### Coverage Requirements

- **90%+ test coverage** mandatory
- Measured with appropriate tools (pytest-cov, jest, etc.)
- BLOCKING enforcement - commits fail if coverage < 90%

### Quality Standards

- **Security**: Threat modeling for all features
- **Performance**: 200ms p95 response time
- **Code Quality**: Zero linting errors, clean type checking

---

## Advanced Features

### Meta-Prompting

Framework 3.0 includes self-improvement capabilities:

- **Pattern Recognition**: Learns from usage patterns
- **Adaptive Routing**: Improves command selection over time
- **Performance Optimization**: Auto-optimizes based on success metrics
- **Safety Boundaries**: Human oversight with 60-second rollback

### Claude 4 Optimization

- **Interleaved Thinking**: 16K thinking length with advanced reasoning
- **Parallel Execution**: Batch tool calls for 70% performance improvement
- **200K Context**: Optimized context window management
- **Enhanced Reasoning**: Multi-perspective analysis with critical thinking

### Module Runtime Engine

- **Deterministic Execution**: Predictable module composition
- **Dependency Management**: Automatic module loading and orchestration
- **Quality Gates**: Universal validation at all levels
- **Error Recovery**: Graceful degradation with rollback capabilities

---

## Troubleshooting

### Common Issues

#### "Command not found"
```bash
✓ /task "Add login feature"     # Correct
✗ task "Add login feature"      # Missing /
✗ /task Add login feature       # Missing quotes
```

#### "Permission denied"
```bash
# One-line fix:
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```

#### "Not sure which command"
```bash
# Always start with:
/auto "what you want to do"
```

#### "TDD not followed"
```bash
# Use meta-fix:
/meta-fix "TDD not followed"
```

### Debug Commands

```bash
# Framework health check
python internal/monitoring/health_check.py

# Validate configuration
python scripts/framework/config_validator.py --verbose

# Check for script duplications
python scripts/framework/script_validator.py
```

---

## Best Practices

### Command Selection Decision Tree

```
Single file <50 lines → /task
Multiple files → /feature  
Research needed → /query
Complex architecture → /swarm
Not sure → /auto
```

### Workflow Patterns

1. **Research First**: Start with `/query` when understanding is needed
2. **Plan Before Code**: Use `/feature` for comprehensive development
3. **Track Complex Work**: Use `/session` for multi-phase projects
4. **Production Ready**: Use `/protocol` for critical production work

### Quality Practices

- **Always TDD**: Write tests first, no exceptions
- **Coverage Mandatory**: 90%+ coverage enforced
- **Think First**: 30-second critical thinking minimum
- **Document Decisions**: Use sessions for complex work

### Framework Evolution

- **Use Meta Commands**: Leverage `/meta-*` commands for framework improvement
- **Provide Feedback**: Framework learns from your usage patterns
- **Trust the System**: Let the framework handle complexity
- **Stay Updated**: Framework evolves and improves automatically

---

## Philosophy

> *"The best framework is the one you don't have to think about."*

> *"Commands delegate, modules implement, meta-prompting evolves."*

> *"Research deeply, implement wisely, track everything."*

**Framework 3.0 Principle**: Start with `/auto` and let meta-prompting handle the complexity!

---

**Need Help?** 

- Start with `/query "your question"` or `/auto "what you need"`
- Check [GETTING_STARTED.md](docs/GETTING_STARTED.md) for quick start
- Review [Documentation Index](docs/DOCUMENTATION_INDEX.md) for comprehensive guides

---

*🚀 Framework 3.0: Where meta-prompting meets practical development workflows*