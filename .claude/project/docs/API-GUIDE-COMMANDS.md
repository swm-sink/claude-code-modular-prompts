# API Documentation for Guide Commands

This document provides comprehensive API documentation for all guide commands in the Claude Code Template Library. These commands help users manually customize the framework for their specific projects.

## Overview

Guide commands provide **manual customization instructions** rather than automated functionality. They generate checklists, provide copy-paste configurations, and guide users through the manual adaptation process.

### Core Principle
All guide commands follow this pattern:
1. **Assess** - Help user understand what needs to be done
2. **Guide** - Provide step-by-step instructions  
3. **Validate** - Help user verify their manual work

## Command Reference

### `/adapt-to-project`

**Purpose**: Primary entry point for framework customization

**Usage**: 
```
/adapt-to-project [--express|--guided] [--dry-run]
```

**Options**:
- `--express`: Fast 15-20 minute customization with 50 yes/no questions
- `--guided`: Detailed 30-45 minute customization with explanations
- `--dry-run`: Preview output without making recommendations

**What It Provides**:
- Complete replacement guide for all placeholders
- Copy-paste ready `project-config.yaml`
- File-by-file update instructions
- Domain-specific command recommendations
- Validation checklist

**Expected User Workflow**:
1. User runs command and chooses mode
2. Answers questions about their project
3. Receives comprehensive customization checklist
4. Manually implements all changes
5. Runs `/validate-adaptation` to verify

**Output Format**:
```markdown
## Replacement Guide
File: .claude/commands/core/task.md
- Line 12: Replace "[INSERT_PROJECT_NAME]" with "YourProject"

## Copy-Paste Configuration
[Complete YAML content]

## Validation Steps
□ Task 1
□ Task 2
```

### `/validate-adaptation`

**Purpose**: Help users verify their manual customization work

**Usage**:
```
/validate-adaptation [--verbose] [--auto-run]
```

**Options**:
- `--verbose`: Provide detailed explanation for each check
- `--auto-run`: Skip explanations, provide direct checklist

**What It Provides**:
- Manual validation commands to run
- Checklist for verification
- Readiness score calculation guide
- Next steps based on findings

**Expected User Workflow**:
1. User completes manual customization
2. Runs validation command
3. Follows manual check instructions
4. Calculates own readiness score
5. Identifies remaining work needed

**Validation Categories**:
- Placeholder replacement verification
- Configuration file validation
- Command selection review
- Framework structure check

### `/replace-placeholders`

**Purpose**: Provide comprehensive list of all placeholders needing replacement

**Usage**:
```
/replace-placeholders [--category=<category>] [--file=<path>]
```

**Options**:
- `--category`: Focus on specific command category (core, dev, quality, etc.)
- `--file`: Show placeholders for specific file

**What It Provides**:
- Complete placeholder inventory
- Replacement suggestions based on common patterns
- File-by-file replacement guides
- Context-aware recommendations

**Placeholder Categories**:
- **Project Identity**: `[INSERT_PROJECT_NAME]`, `[INSERT_COMPANY_NAME]`
- **Technical Stack**: `[INSERT_TECH_STACK]`, `[INSERT_PRIMARY_LANGUAGE]`
- **Team Context**: `[INSERT_TEAM_SIZE]`, `[INSERT_WORKFLOW_TYPE]`
- **Domain Specific**: `[INSERT_TESTING_FRAMEWORK]`, `[INSERT_CI_CD_PLATFORM]`

### `/sync-from-reference`

**Purpose**: Guide users through updating their customized framework

**Usage**:
```
/sync-from-reference [--preview] [--conflict-resolution=<method>]
```

**Options**:
- `--preview`: Show what would change without providing instructions
- `--conflict-resolution`: Handle conflicts (manual, preserve-custom, take-reference)

**What It Provides**:
- Git commands for safe updates
- Conflict resolution strategies
- Backup instructions
- Re-customization checklist

**Update Process Guide**:
1. Backup current customizations
2. Update reference framework
3. Identify conflicts
4. Manual merge resolution
5. Re-validate customizations

### `/undo-adaptation`

**Purpose**: Provide recovery instructions if customization goes wrong

**Usage**:
```
/undo-adaptation [--level=<level>] [--preserve=<items>]
```

**Options**:
- `--level`: Undo scope (placeholders-only, config-only, full-reset)
- `--preserve`: What to keep (custom-commands, local-config, documentation)

**What It Provides**:
- Step-by-step recovery instructions
- Selective restoration options
- Backup and restore commands
- Prevention strategies for future

**Recovery Levels**:
- **Placeholder Reset**: Restore original placeholders
- **Config Reset**: Reset configuration files
- **Full Reset**: Complete framework restoration
- **Selective Reset**: Custom recovery plan

### `/share-adaptation`

**Purpose**: Create shareable adaptation patterns for teams

**Usage**:
```
/share-adaptation [--format=<format>] [--include=<items>]
```

**Options**:
- `--format`: Output format (markdown, yaml, json)
- `--include`: What to share (config-only, commands-only, full-pattern)

**What It Provides**:
- Shareable configuration templates
- Team adaptation guides
- Standardization instructions
- Import procedures for team members

### `/import-pattern`

**Purpose**: Help users apply shared adaptation patterns

**Usage**:
```
/import-pattern <pattern-source> [--validate] [--preview]
```

**Options**:
- `--validate`: Check pattern compatibility first
- `--preview`: Show what would be applied

**What It Provides**:
- Pattern compatibility validation
- Import instructions
- Conflict resolution guidance
- Customization merge strategies

### `/welcome`

**Purpose**: Interactive onboarding for new users

**Usage**:
```
/welcome [--experience=<level>] [--goal=<objective>]
```

**Options**:
- `--experience`: User level (beginner, intermediate, advanced)
- `--goal`: Primary objective (quick-start, full-custom, team-deploy)

**What It Provides**:
- Personalized getting started guide
- Recommended learning path
- Essential commands introduction
- Quick wins for immediate value

## Integration Patterns

### Command Chaining
Commands are designed to work together:
```
/welcome → /adapt-to-project → /validate-adaptation → /replace-placeholders
```

### Error Recovery
Each command provides error recovery guidance:
```
/validate-adaptation (finds issues) → /replace-placeholders → /undo-adaptation (if needed)
```

### Team Workflows
For team standardization:
```
/adapt-to-project → /share-adaptation → /import-pattern (team members)
```

## Common Usage Patterns

### First-Time Setup
1. `/welcome` - Get oriented
2. `/adapt-to-project --express` - Quick customization
3. `/validate-adaptation` - Verify work
4. `/replace-placeholders` - Fix any missed items

### Team Standardization
1. Lead: `/adapt-to-project --guided` - Detailed customization
2. Lead: `/share-adaptation --format=yaml` - Create team pattern
3. Team: `/import-pattern <shared-config>` - Apply standardization
4. All: `/validate-adaptation` - Verify consistency

### Framework Updates
1. `/sync-from-reference --preview` - Check what's new
2. Backup current customizations
3. `/sync-from-reference` - Get update instructions
4. Manual merge and resolution
5. `/validate-adaptation` - Verify updated setup

### Recovery Scenarios
1. `/validate-adaptation` - Identify problems
2. `/undo-adaptation --level=placeholders-only` - Selective reset
3. `/replace-placeholders` - Re-customize
4. `/validate-adaptation` - Verify recovery

## Advanced Features

### Context-Aware Recommendations
Guide commands consider:
- Project domain (web-dev, data-science, devops)
- Technology stack indicators
- Team size implications  
- Workflow complexity needs

### Extensibility
Commands can be extended with:
- Domain-specific question sets
- Custom placeholder patterns
- Industry-specific templates
- Compliance requirement checks

### Validation Framework
Built-in validation covers:
- Structural integrity
- Placeholder completeness
- Configuration consistency
- Command compatibility

## Best Practices for Users

### Before Using Guide Commands
1. **Understand your project context** - Tech stack, team size, domain
2. **Have project information ready** - Names, technologies, workflows
3. **Plan customization scope** - What commands you actually need
4. **Backup important work** - Before making major changes

### During Customization
1. **Follow the guided sequence** - Don't skip validation steps
2. **Take notes on custom changes** - For future reference and sharing
3. **Test as you go** - Validate each major customization step
4. **Keep reference framework** - For future updates and comparison

### After Customization
1. **Document your patterns** - Use `/share-adaptation` for teams
2. **Regular validation** - Periodic `/validate-adaptation` runs
3. **Stay current** - Use `/sync-from-reference` for updates
4. **Share learnings** - Help improve the framework

## Troubleshooting Guide

### Common Issues

**"Too many placeholders found"**
- Use `/replace-placeholders --category=core` to focus on essentials first
- Break work into smaller batches
- Validate frequently with `/validate-adaptation`

**"Validation shows low readiness score"**
- Review `/adapt-to-project` output carefully
- Focus on project-specific customizations first
- Remove unused commands to improve signal-to-noise

**"Conflicts during framework updates"**
- Use `/sync-from-reference --conflict-resolution=manual`
- Backup customizations before updating
- Consider `/undo-adaptation` and re-customization for major conflicts

**"Team members have inconsistent setups"**
- Use `/share-adaptation` to create team standards
- Implement `/import-pattern` workflow for new team members
- Regular team `/validate-adaptation` reviews

### Getting Help
Each command provides help with context-aware suggestions. The framework is designed for self-service, but commands will guide you to:
- Relevant documentation sections
- Common solution patterns
- Community resources and examples
- Recovery procedures when needed

---

*This API documentation reflects the current implementation of guide commands in the Claude Code Template Library. For the most current information, use the `/help` command within Claude Code.*