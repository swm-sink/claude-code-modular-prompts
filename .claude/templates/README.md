| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | $(date '+%Y-%m-%d') | stable |

# Framework Templates Directory

## Overview

This directory contains standardized templates for creating new framework components with consistent structure, quality standards, and integration patterns.

## Available Templates

### Core Templates

1. **command-template.md** - Template for creating new framework commands
   - Includes thinking patterns, module runtime integration, and quality gates
   - Optimized for Claude 4 with interleaved thinking patterns
   - Atomic safety and rollback procedures included

2. **module-documentation-template.md** - Template for creating new framework modules
   - Comprehensive interface contracts and dependency management
   - Error handling and integration patterns
   - Performance and quality standards

## Usage Guidelines

### Creating a New Command

1. Copy `command-template.md` to `.claude/commands/[command-name].md`
2. Replace all placeholder text in brackets `[...]`
3. Update the version table with current date
4. Customize thinking patterns for your specific command
5. Define module dependencies and integration points
6. Add command-specific implementation details

### Creating a New Module

1. Copy `module-documentation-template.md` to appropriate module directory
2. Replace all placeholder text in brackets `[...]`
3. Update the version table with current date
4. Define clear interface contracts
5. Add comprehensive usage examples
6. Document dependencies and integration points

## Template Standards

### Required Elements

All templates must include:
- Version table with semantic versioning
- Clear purpose and scope definition
- Interface contracts (for modules) or thinking patterns (for commands)
- Error handling and recovery procedures
- Integration points with existing framework
- Quality standards and testing requirements

### Optional Elements

Templates may include:
- Performance characteristics
- Usage examples
- Troubleshooting guides
- Extension points
- Maintenance procedures

## Quality Requirements

### Documentation Standards
- All public interfaces must be documented
- Clear examples for common use cases
- Comprehensive error handling documentation
- Integration patterns with existing components

### Code Standards
- Minimum 90% test coverage
- All errors must be handled gracefully
- Performance targets must be specified
- Security considerations documented

## Framework Integration

### Command Integration
- Must integrate with module runtime engine
- Required to follow thinking pattern templates
- Must support atomic commits and rollback
- Integration with quality gates mandatory

### Module Integration
- Must define clear interface contracts
- Required to specify dependencies
- Must support error recovery patterns
- Integration with testing framework mandatory

## Maintenance

### Template Updates
- Templates updated with framework version
- Breaking changes documented in changelog
- Backward compatibility maintained when possible
- Migration guides provided for major changes

### Quality Assurance
- Regular review of template usage
- Feedback collection from template users
- Performance monitoring of template-based components
- Continuous improvement based on usage patterns

## Related Documentation

- `.claude/commands/` - Example implementations using command template
- `.claude/modules/` - Example implementations using module template
- `.claude/system/quality/` - Quality standards and validation
- `.claude/prompt_eng/patterns/` - Thinking pattern templates

## Support

For questions about template usage:
1. Check existing command/module implementations
2. Review framework documentation
3. Consult quality standards documentation
4. Create GitHub issue if problems persist