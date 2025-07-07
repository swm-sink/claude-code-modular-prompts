| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# .claude Directory - Framework Core

────────────────────────────────────────────────────────────────────────────────

## Purpose

The `.claude` directory contains the **core implementation** of the Claude Code Modular Agents framework. This is where commands delegate to modules, creating a powerful composition system for automated development workflows.

## Directory Structure

```
.claude/
├── commands/              # Command implementations (8 files)
├── modules/               # Modular components (24+ files)
│   ├── patterns/         # Multi-agent patterns
│   ├── quality/          # Quality assurance
│   ├── security/         # Security validation
│   ├── development/      # Development workflows
│   ├── planning/         # Project planning
│   └── testing/          # Testing frameworks
├── templates/            # Document templates
├── security/             # Security configurations
├── analytics/            # Usage analytics
└── settings.local.json   # Local configuration
```

## Core Components

### Commands Directory

**Location**: `commands/`
**Purpose**: Command implementations that delegate to modules

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
**Purpose**: Domain-specific implementations

#### Module Categories

**patterns/** - Multi-agent coordination
- `intelligent-routing.md` - Smart decision making
- `multi-agent.md` - Agent coordination patterns
- `session-management.md` - Context preservation

**quality/** - Quality assurance
- `tdd.md` - Test-driven development
- `validation-framework.md` - Quality validation
- `error-recovery.md` - Error handling patterns

**security/** - Security validation
- `threat-modeling.md` - Security analysis
- `security-checklist.md` - Security requirements

**development/** - Development workflows
- `task-management.md` - Development task coordination
- `documentation.md` - Documentation generation
- `research-analysis.md` - Code analysis patterns

**planning/** - Project planning
- `feature-workflow.md` - Feature development planning
- `project-planning.md` - Project coordination

**testing/** - Testing frameworks
- `testing-framework.md` - Testing coordination
- `performance-testing.md` - Performance validation

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
- `commands/` - 8 command implementations
- `modules/` - 24+ domain-specific modules
- `templates/` - Document templates
- `security/` - Security configurations

### Development Pattern
1. **Commands delegate** to modules
2. **Modules implement** domain logic
3. **Framework coordinates** interactions
4. **Users focus** on requirements

**Remember**: This directory contains the **framework engine** - the commands and modules that make Claude Code powerful and autonomous.