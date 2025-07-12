| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-12   | stable |

# .claude Directory - Framework Core

## Overview

The `.claude` directory contains the **complete Claude Code framework implementation** - a powerful modular system for automated development workflows. This framework provides intelligent command routing, comprehensive quality gates, and advanced prompt engineering capabilities optimized for Claude 4.

## Quick Start

### For New Users
```bash
# Start with intelligent routing - it will guide you to the right command
/auto "your development request"

# Or try these common commands:
/task "fix this bug"           # Single file/component work
/feature "add user auth"       # Complete feature development  
/query "how does this work"    # Research and analysis
```

### For Experienced Users
```bash
/init                          # Set up framework in your project
/swarm "complex refactoring"   # Multi-component coordination
/session "long development"    # Managed development sessions
/docs "create documentation"   # Documentation generation
```

## Framework Architecture

```
.claude/
├── commands/              # 15 production commands (auto, task, feature, swarm, etc.)
├── modules/               # 100+ specialized modules organized by domain
│   ├── patterns/         # Execution patterns and orchestration
│   ├── quality/          # Quality gates and TDD enforcement  
│   ├── security/         # Security validation and threat modeling
│   ├── development/      # Development workflows and task management
│   └── meta/             # Framework meta-operations and self-improvement
├── prompt_eng/            # Advanced prompt engineering patterns
│   ├── frameworks/       # RISE, TRACE, CARE, CLEAR, SOAR frameworks
│   ├── personas/         # 25+ specialized engineering personas
│   └── patterns/         # Thinking patterns and composition
├── system/                # Framework infrastructure
│   ├── quality/          # Quality gates infrastructure (36 modules)
│   ├── security/         # Security frameworks and compliance
│   ├── context/          # Context management and preservation
│   └── session/          # Session tracking and reliability
├── domain/                # Domain-specific templates and adaptation
└── meta/                  # Self-improving meta-framework capabilities
```

## Navigation by Use Case

### I want to use the framework
- **Start here**: Use `/auto "your request"` for intelligent routing
- **Commands**: See `/commands/README.md` for all 15 available commands
- **Setup**: Use `/init` to configure the framework for your project

### I want to understand the framework
- **Architecture**: See `/modules/README.md` for module organization
- **Quality System**: See `/system/quality/` for quality gates and TDD
- **Advanced Features**: See `/prompt_eng/` for prompt engineering patterns

### I want to extend the framework
- **Add Commands**: See `/commands/` directory and follow delegation patterns
- **Add Modules**: See `/modules/` categories and standardized interfaces
- **Custom Domains**: See `/domain/` for domain-specific customization

### I want to troubleshoot
- **Common Issues**: Check README files in each major directory
- **Quality Problems**: See `/system/quality/universal-quality-gates.md`
- **Performance**: See `/modules/patterns/performance-optimization-pattern.md`

## Core Components

### Commands Directory

**Location**: `commands/`
**Purpose**: Framework 3.0 command implementations with Module Runtime Engine integration that delegate to modules with universal quality gates and meta-prompting capabilities

#### Available Commands

| Command | File | Purpose |
|---------|------|---------|
| `/auto` | `auto.md` | Intelligent routing and decision making |
| `/task` | `task.md` | Single component TDD development |
| `/feature` | `feature.md` | Complete feature development with PRD |
| `/swarm` | `swarm.md` | Multi-component coordination |
| `/query` | `query.md` | Research and analysis (no modifications) |
| `/session` | `session.md` | GitHub issue management |
| `/docs` | `docs.md` | Documentation generation |
| `/protocol` | `protocol.md` | Quality gates and compliance |

#### Command Pattern

All commands follow the **delegation pattern**:
1. **Parse** user request
2. **Validate** inputs and preconditions
3. **Delegate** to appropriate modules
4. **Coordinate** module interactions
5. **Return** results to user

### Modules Directory

**Location**: `modules/`
**Purpose**: 100+ modular components organized by domain with Framework 3.0 capabilities

#### Module Categories

**patterns/** - Multi-agent coordination and intelligent routing
- `intelligent-routing.md` - Smart decision making with meta-prompting
- `multi-agent.md` - Agent coordination patterns
- `session-management.md` - Context preservation and GitHub integration
- `module-composition-framework.md` - Module Runtime Engine architecture
- `thinking-pattern-template.md` - Standardized thinking patterns

**quality/** - Universal quality gates and TDD enforcement
- `tdd.md` - Test-driven development with RED-GREEN-REFACTOR enforcement
- `universal-quality-gates.md` - Comprehensive quality validation
- `critical-thinking.md` - 30-second minimum analysis enforcement
- `error-recovery.md` - Intelligent failure recovery patterns

**security/** - Security validation and threat modeling
- `threat-modeling.md` - Security analysis and vulnerability assessment
- `security-checklist.md` - Security requirements and compliance
- `audit-framework.md` - Security audit and monitoring

**development/** - Development workflows and task management
- `task-management.md` - Development task coordination with TDD
- `documentation.md` - Documentation generation and standards
- `research-analysis.md` - Code analysis patterns and research methodology

**planning/** - Project planning and feature development
- `feature-workflow.md` - Feature development planning with PRD generation
- `project-planning.md` - Project coordination and MVP strategy

**testing/** - Testing frameworks and performance validation
- `testing-framework.md` - Testing coordination and automation
- `performance-testing.md` - Performance validation and benchmarking

**frameworks/** - Framework implementations
- `focus-framework.md` - FOCUS framework implementation
- `aware-framework.md` - AWARE cognitive process
- `rise-framework.md` - RISE framework (Role, Input, Steps, Expectation)
- `trace-framework.md` - TRACE framework (Task, Request, Action, Context, Expectation)

#### Module Interface

All modules implement a **standardized interface**:
- **Input specification**: Clear parameter requirements
- **Processing logic**: Domain-specific implementation
- **Output format**: Consistent return structure
- **Error handling**: Graceful failure patterns

### Templates Directory

**Location**: `templates/`
**Purpose**: Standardized document templates

Provides consistent formatting for:
- Documentation files
- Report generation
- Analysis documents
- Framework components

### Configuration

**settings.local.json**: Local framework configuration
- Command preferences
- Module settings
- Performance tuning
- Analytics configuration

## Architecture Principles

### 1. Command-Module Delegation

Commands **never implement business logic directly**. They:
- Parse user requests
- Validate inputs
- Delegate to appropriate modules
- Coordinate module interactions
- Handle errors and responses

### 2. Module Composition

Modules are **composable building blocks** that:
- Handle single domain responsibilities
- Accept standardized inputs
- Return consistent outputs
- Can be chained together
- Maintain state isolation

### 3. Interface Contracts

All components follow **clear interface contracts**:
- Input/output specifications
- Error handling patterns
- Performance expectations
- Dependency requirements

### 4. Modular Independence

Each module is **independently testable** and:
- Has minimal dependencies
- Can be developed separately
- Provides fallback behavior
- Supports graceful degradation

## Usage Guide

### For Command Development

1. **Study existing commands** in `commands/` directory
2. **Follow delegation pattern** - commands coordinate, modules implement
3. **Use standardized interfaces** for module interaction
4. **Implement error recovery** for robust operation

### For Module Development

1. **Choose appropriate domain** directory (patterns, quality, security, etc.)
2. **Follow module interface** specification
3. **Implement single responsibility** - one domain per module
4. **Provide clear documentation** with examples

### For Framework Users

1. **Commands are your interface** - use `/auto`, `/task`, `/feature`, etc.
2. **Let commands route** to appropriate modules automatically
3. **Trust the delegation** - modules handle implementation details
4. **Focus on your requirements** - framework handles the how

## Development Workflow

### Adding New Commands

1. Create new `.md` file in `commands/`
2. Implement delegation pattern
3. Reference appropriate modules
4. Add error recovery
5. Update documentation

### Adding New Modules

1. Choose appropriate domain directory
2. Create module with standardized interface
3. Implement domain-specific logic
4. Add comprehensive error handling
5. Write tests and documentation

### Modifying Existing Components

1. **Read first** - understand current implementation
2. **Maintain interfaces** - don't break contracts
3. **Test thoroughly** - ensure no regressions
4. **Update documentation** - keep guides current

## Quality Assurance

### Testing

All components must have:
- **Unit tests** for individual modules
- **Integration tests** for command-module interaction
- **Performance tests** for optimization
- **Error tests** for robustness

### Documentation

All components must include:
- **Clear purpose** statement
- **Interface specification** with examples
- **Usage guidelines** for developers
- **Error handling** documentation

### Validation

Framework includes automated validation:
- **Module interface** compliance
- **Command delegation** pattern adherence
- **Documentation** completeness
- **Performance** benchmarks

## Integration Points

### External Integration

The `.claude` directory integrates with:
- **Claude Code CLI** - Primary interface
- **GitHub APIs** - Issue and PR management
- **Git workflows** - Version control integration
- **Testing frameworks** - Automated validation

### Internal Integration

Components integrate through:
- **Standardized interfaces** between commands and modules
- **Shared configuration** through settings files
- **Common utilities** for repeated functionality
- **Error propagation** through composition hierarchy

## Best Practices

### Development

- **Start with modules** - implement domain logic first
- **Add commands** - create delegation layer
- **Test integration** - verify command-module interaction
- **Document thoroughly** - explain purpose and usage

### Usage

- **Use appropriate commands** - `/auto` for routing, `/task` for development
- **Trust the framework** - let commands handle coordination
- **Provide clear requests** - specific requirements get better results
- **Check documentation** - comprehensive guides available

### Maintenance

- **Regular validation** - run `scripts/validate.py`
- **Performance monitoring** - check benchmarks
- **Documentation updates** - keep guides current
- **Archive old versions** - preserve historical context

## Troubleshooting

### Common Issues

**Command not working**: Check command syntax and delegation pattern
**Module not found**: Verify module exists in appropriate domain directory
**Interface errors**: Ensure module implements standardized interface
**Performance issues**: Check module composition and optimization

### Debug Process

1. **Check command implementation** in `commands/`
2. **Verify module exists** in appropriate domain
3. **Test module independently** with known inputs
4. **Check error logs** for detailed information
5. **Use validation tools** to identify issues

### Support Resources

- **Documentation**: `docs/DOCUMENTATION_INDEX.md`
- **Examples**: `test-projects/` directory
- **Validation**: `scripts/validate.py`
- **Analysis**: `docs/reports/` directory

────────────────────────────────────────────────────────────────────────────────

## Quick Reference

### Most Used Commands
- `/auto "request"` - Smart routing (use when unsure)
- `/task "request"` - Single component development
- `/feature "request"` - Complete feature development
- `/query "request"` - Research without modifications

### Key Directories
- `commands/` - 8 command implementations with Framework 3.0 capabilities
- `modules/` - 100+ modular components organized by domain
- `templates/` - Document templates
- `security/` - Security configurations

### Framework 3.0 Development Pattern
1. **Commands delegate** to modules via Module Runtime Engine
2. **Modules implement** domain logic with universal quality gates
3. **Framework coordinates** interactions with meta-prompting intelligence
4. **Users focus** on requirements while system handles TDD enforcement

**Remember**: This directory contains the **Framework 3.0 engine** - the commands and modules that make Claude Code intelligent, autonomous, and self-improving.