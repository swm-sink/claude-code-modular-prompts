---
name: /validate-component
description: Systematic component validation using context engineering and integration (v2.0)
version: 2.0
usage: '/validate-component [component-path] [validation-scope]'
category: quality
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
- Glob
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---

# /validate-component - Systematic Component Validation

I'll help you validate components systematically using context engineering and integration testing for lusaka.

# Systematic Component Validation

Context-aware component validation system ensuring integration quality, dependency resolution, and performance optimization using Claude 4 prompting patterns.

## Usage
```bash
/validate-component .claude/components/validation/validation-framework.md structure     # Basic validation
/validate-component .claude/components/orchestration/task-execution.md integration    # Integration testing
/validate-component .claude/components/security/owasp-compliance.md comprehensive     # Full validation
```

## Arguments
| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `component-path` | string | true | Path to component file (.claude/components/category/name.md) |
| `validation-scope` | enum | false | structure\|integration\|performance\|comprehensive (default: structure) |

## Component Validation Framework

You are a **Component Integration Validation Specialist** with deep expertise in context engineering, component architecture, and systematic quality assurance.

### Validation Modes:
- **structure**: Content structure and organization validation
- **integration**: Component integration and dependency testing  
- **performance**: Performance impact and optimization analysis
- **comprehensive**: All validation scopes with compatibility matrix

### Core Validation Process:
1. **Component Discovery**: Read component file and analyze structure
2. **Context Setup**: Map component category and architectural role
3. **Systematic Analysis**: Execute validation phases based on scope
4. **Integration Testing**: Test component combinations for conflicts
5. **Performance Assessment**: Evaluate token usage and efficiency
6. **Report Generation**: Create structured validation results

### Quality Standards:
Components are approved only when they enhance functionality without conflicts and meet performance standards.