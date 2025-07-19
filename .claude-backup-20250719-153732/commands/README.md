| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 100%     |

# Commands Directory - Framework Core Commands

## Overview

This directory contains the **15 production-ready commands** that form the backbone of the Claude Code framework. Each command delegates to specialized modules through the Module Runtime Engine, providing intelligent automation for development workflows.

## Core Commands (Always Available)

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/auto` | Intelligent routing and decision making | When unsure which command to use |
| `/task` | Single component TDD development | Focused work on 1-3 files |
| `/feature` | Complete feature development with PRD | New features requiring 2-10 files |
| `/swarm` | Multi-component coordination | Complex work requiring >10 files |
| `/query` | Research and analysis (no modifications) | Understanding code or investigation |
| `/session` | GitHub issue management | Long-running work sessions |
| `/docs` | Documentation generation | Creating project documentation |
| `/protocol` | Quality gates and compliance | Production deployments and critical work |

## Setup Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/init` | Framework initialization | First-time project setup |
| `/init-custom` | Custom domain setup | Specialized project types |
| `/init-new` | New project creation | Starting from scratch |
| `/init-research` | Research-focused setup | R&D and analysis projects |
| `/init-validate` | Setup validation | Verify framework configuration |

## Advanced Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/chain` | Multi-command workflows | Complex sequential operations |

## Command Architecture

### Delegation Pattern

All commands follow a consistent **delegation pattern**:

1. **Parse** user request and validate inputs
2. **Route** to appropriate modules via Module Runtime Engine
3. **Coordinate** module interactions and state management
4. **Execute** with quality gates and error recovery
5. **Return** results with comprehensive reporting

### Module Integration

Commands **never implement business logic directly**. Instead they:
- Delegate to specialized modules in `/modules/` directory
- Coordinate cross-module interactions
- Handle error recovery and graceful degradation
- Enforce universal quality gates
- Manage session state and artifacts

### Quality Enforcement

Every command execution includes:
- **TDD Enforcement**: RED→GREEN→REFACTOR cycle validation
- **Security Gates**: Threat modeling and vulnerability assessment
- **Performance Validation**: Response time and resource monitoring
- **Coverage Requirements**: 90%+ test coverage verification
- **Documentation Standards**: Auto-generated documentation

## Quick Start Guide

### For New Users
1. Start with `/auto "your request"` - it will route to the best command
2. Use `/init` to set up the framework in your project
3. Try `/task "simple request"` for focused development work

### For Experienced Users
1. `/feature` for complete feature development with PRD
2. `/swarm` for complex multi-component coordination
3. `/query` for research before implementation
4. `/session` for managing long-running development work

### For Advanced Workflows
1. `/chain` for multi-command workflows
2. `/protocol` for production-grade quality enforcement
3. `/docs` for comprehensive documentation generation

## Command Selection Guidelines

| Scenario | Recommended Command | Alternative |
|----------|-------------------|-------------|
| Single file changes | `/task` | `/auto` |
| New feature with design | `/feature` | `/auto` |
| Large refactoring | `/swarm` | `/chain` |
| Code investigation | `/query` | - |
| Long development session | `/session` | `/feature` |
| Documentation needs | `/docs` | - |
| Production deployment | `/protocol` | `/feature` + `/protocol` |

## Error Recovery

All commands include **comprehensive error recovery**:
- **Atomic Operations**: Each command can be safely rolled back
- **Graceful Degradation**: Partial failures don't break entire workflows
- **Intelligent Retry**: Exponential backoff for transient failures
- **Human Escalation**: Clear escalation paths for complex issues

## Performance Optimization

Commands are optimized for **Claude 4 capabilities**:
- **Parallel Execution**: Independent operations run concurrently
- **Context Efficiency**: 200K context window optimization
- **Token Management**: Intelligent token budget allocation
- **Thinking Patterns**: Integrated critical thinking checkpoints

## Integration Points

### Framework Integration
- **Module Runtime Engine**: All commands use standardized module loading
- **Quality Gates**: Universal quality enforcement across all commands
- **Session Management**: Integrated GitHub issue tracking and context preservation
- **Error Recovery**: Framework-wide error handling and rollback capabilities

### External Integration
- **Claude Code CLI**: Primary interface for all command execution
- **GitHub**: Automated issue creation and PR management
- **Git**: Conventional commits and worktree isolation
- **Testing Frameworks**: Integrated TDD and coverage enforcement

## Development Guidelines

### Adding New Commands
1. **Follow delegation pattern** - commands coordinate, modules implement
2. **Use Module Runtime Engine** for standardized module loading
3. **Implement quality gates** for consistency and reliability
4. **Add comprehensive tests** for command validation
5. **Document thoroughly** with examples and usage patterns

### Modifying Existing Commands
1. **Maintain interface contracts** - don't break existing integrations
2. **Preserve delegation pattern** - keep business logic in modules
3. **Test extensively** - ensure no regressions in functionality
4. **Update documentation** - keep usage guides current

## See Also

- `/modules/` - Specialized modules for domain-specific logic
- `/system/` - Framework infrastructure and quality gates
- `/prompt_eng/` - Advanced prompt engineering patterns
- Main README.md - Complete framework overview