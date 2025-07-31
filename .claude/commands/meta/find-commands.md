---
name: /find-commands
description: Smart command discovery tool with filtering and search capabilities
usage: '[category] [keyword] [--list-categories]'
allowed-tools:  
- Read
- LS
- Grep
category: meta
---

# /find-commands - Smart Command Discovery

Discover commands and templates based on your needs with intelligent filtering and search.

## Usage Patterns

### Browse by Category
```
/find-commands core          # Show core development commands
/find-commands quality       # Show testing and validation commands  
/find-commands specialized   # Show advanced workflow commands
/find-commands meta          # Show template management commands
```

### Search by Keyword
```
/find-commands test          # Find all test-related commands
/find-commands api           # Find API-related templates
/find-commands security      # Find security-focused commands
```

### List All Categories
```
/find-commands --list-categories    # Show all available categories
```

## Available Categories

Based on current template library structure:

- **core** (12 commands): Essential development workflows
- **quality** (12 commands): Testing, validation, analysis tools
- **specialized** (11 commands): Advanced workflows and patterns  
- **meta** (14 commands): Template adaptation and management
- **development** (6 commands): Development setup and protocols
- **devops** (5 commands): CI/CD and deployment
- **testing** (5 commands): Comprehensive testing frameworks
- **database** (4 commands): Database operations
- **security** (4 commands): Security analysis and hardening
- **examples** (6 commands): Example implementations

## Quick Discovery Workflow

1. **Start broad**: `/find-commands --list-categories`
2. **Narrow down**: `/find-commands [category]` for category overview
3. **Search specific**: `/find-commands [keyword]` for targeted results
4. **Explore**: Read command files to understand functionality

## Integration with Customization

After finding relevant commands:
1. Use `/adapt-to-project` for customization guidance
2. Use `/replace-placeholders` to understand required changes
3. Use `/validate-adaptation` to verify customizations

## Pro Tips

- **Multiple keywords**: Use `/find-commands api test` to find API testing commands
- **Category + keyword**: Use `/find-commands quality performance` for performance testing
- **Explore examples**: The examples category shows real implementation patterns

This discovery tool helps you navigate the 82 available command templates efficiently.
