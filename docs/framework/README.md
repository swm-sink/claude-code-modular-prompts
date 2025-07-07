# Claude Code Prompts Storage System

## Overview
This directory contains the centralized prompt management system for the Claude Code Modular Agents framework. It provides versioned, categorized, and easily retrievable prompts for various AI-assisted development tasks.

## Directory Structure

```
.claude/prompts/
├── README.md                    # This file
├── prompt-schema.json          # JSON schema for prompt validation
├── TEMPLATE_FORMAT.md          # Template format specification
├── NAMING_CONVENTIONS.md       # Naming conventions guide
├── queries/                    # Information retrieval prompts
│   └── code-analysis-v1.0.0.json
├── features/                   # Feature implementation prompts
│   └── api-endpoint-v1.0.0.json
├── reviews/                    # Code review prompts
│   └── security-audit-v1.0.0.json
├── patterns/                   # Reusable pattern prompts
│   └── multi-agent-coordination-v1.0.0.json
├── templates/                  # Meta-templates for prompt generation
└── archived/                   # Version history
    ├── v1/                     # Version 1.x.x prompts
    └── v2/                     # Version 2.x.x prompts
```

## Quick Start

### 1. Finding a Prompt
```bash
# List all prompts in a category
ls .claude/prompts/features/

# Search for specific prompts
find .claude/prompts -name "*api*" -type f

# View prompt details
cat .claude/prompts/features/api-endpoint-v1.0.0.json
```

### 2. Using a Prompt
```bash
# Reference in commands
/task --prompt=features-api-endpoint-v1.0.0

# Or use directly with variable substitution
/auto --prompt=queries-code-analysis-v1.0.0 --vars='{"language": "Python", "file_path": "src/main.py"}'
```

### 3. Creating a New Prompt
1. Choose appropriate category
2. Follow naming conventions
3. Use prompt-schema.json for structure
4. Add comprehensive metadata
5. Include examples and validation

## Prompt Categories

### 🔍 Queries (`/queries`)
Information retrieval and analysis prompts:
- Code analysis and quality assessment
- Architecture and design reviews
- Dependency and security scanning
- Performance profiling

### 🚀 Features (`/features`)
Implementation and development prompts:
- API endpoint creation
- Component development
- Database schema design
- Integration implementation

### 🔒 Reviews (`/reviews`)
Quality assurance and review prompts:
- Security audits
- Code reviews
- Performance optimization
- Accessibility checks

### 🎯 Patterns (`/patterns`)
Reusable architectural patterns:
- Multi-agent coordination
- Error handling strategies
- Authentication patterns
- Data flow architectures

### 📋 Templates (`/templates`)
Meta-templates for generating other prompts:
- Prompt generators
- Category templates
- Variable extractors

## Versioning System

### Semantic Versioning
All prompts follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes to template structure
- **MINOR**: New features or non-breaking enhancements
- **PATCH**: Bug fixes or minor improvements

### Version History
```json
{
  "versioning": {
    "previousVersions": ["1.0.0", "1.1.0"],
    "changelog": [
      {
        "version": "1.2.0",
        "date": "2024-01-06",
        "changes": ["Added authentication support", "Enhanced error handling"]
      }
    ]
  }
}
```

## Metadata Structure

Each prompt includes comprehensive metadata:

```json
{
  "id": "unique-identifier",
  "version": "1.0.0",
  "category": "features",
  "name": "Human Readable Name",
  "description": "What this prompt does",
  "metadata": {
    "created": "2024-01-06T00:00:00Z",
    "author": "system",
    "tags": ["relevant", "tags"],
    "dependencies": ["other-prompt-ids"]
  }
}
```

## Variable System

### Basic Variables
```json
{
  "template": "Analyze {{language}} code in {{file_path}}",
  "variables": [
    {
      "name": "language",
      "type": "string",
      "required": true,
      "examples": ["Python", "JavaScript"]
    }
  ]
}
```

### Advanced Features
- **Conditionals**: `{{#if include_tests}}...{{/if}}`
- **Loops**: `{{#each items}}{{this}}{{/each}}`
- **Defaults**: `{{timeout|default:60}}`

## Best Practices

### 1. Prompt Design
- Keep prompts focused on single tasks
- Include clear success criteria
- Provide comprehensive examples
- Estimate token usage

### 2. Categorization
- Use appropriate categories
- Tag comprehensively
- Document dependencies
- Version everything

### 3. Maintenance
- Update changelog for changes
- Archive old versions properly
- Deprecate gracefully
- Test before releasing

## Integration with Framework

### Command Integration
```bash
# Direct prompt reference
/task --prompt=features-api-endpoint-v1.0.0

# With variable override
/auto --prompt=queries-code-analysis-v1.0.0 \
      --vars='{"include_refactoring": true}'
```

### Multi-Agent Support
```json
{
  "metadata": {
    "agentType": "specialist",
    "coordinationLevel": "high",
    "requiresSession": true
  }
}
```

### Session Management
Prompts can specify session requirements:
```json
{
  "metadata": {
    "requiresSession": true,
    "estimatedDuration": 300,
    "atomicSteps": 15
  }
}
```

## Validation and Testing

### Schema Validation
```bash
# Validate a prompt against schema
python .claude/tools/validate_prompt.py features/new-prompt-v1.0.0.json
```

### Testing Checklist
- [ ] Valid JSON structure
- [ ] Conforms to schema
- [ ] Variables properly defined
- [ ] Examples provided
- [ ] Success criteria clear
- [ ] Token estimate accurate

## Contributing

### Adding New Prompts
1. Fork and create feature branch
2. Design prompt following guidelines
3. Add to appropriate category
4. Include comprehensive tests
5. Submit PR with examples

### Updating Existing Prompts
1. Increment version appropriately
2. Update changelog
3. Archive old version if major change
4. Update dependencies
5. Test backward compatibility

## Advanced Usage

### Prompt Composition
Combine multiple prompts:
```json
{
  "dependencies": [
    "code-analysis-comprehensive",
    "security-audit-basic"
  ]
}
```

### Dynamic Variables
Runtime variable resolution:
```json
{
  "variables": [
    {
      "name": "timestamp",
      "type": "string",
      "default": "{{NOW}}"
    }
  ]
}
```

### Performance Optimization
```json
{
  "performance": {
    "estimatedTokens": 800,
    "complexity": "medium",
    "cacheable": true,
    "timeout": 30
  }
}
```

## Troubleshooting

### Common Issues

1. **Prompt Not Found**
   - Check naming convention
   - Verify category placement
   - Ensure version exists

2. **Variable Errors**
   - Validate variable names
   - Check required fields
   - Verify type matching

3. **Performance Issues**
   - Review token estimates
   - Check complexity rating
   - Consider prompt splitting

## Future Enhancements

- [ ] Prompt composition engine
- [ ] AI-powered prompt optimization
- [ ] Usage analytics dashboard
- [ ] Automated testing framework
- [ ] Version migration tools
- [ ] Prompt marketplace integration

## Resources

- [Template Format Specification](./TEMPLATE_FORMAT.md)
- [Naming Conventions](./NAMING_CONVENTIONS.md)
- [JSON Schema](./prompt-schema.json)
- [Framework Documentation](../README.md)