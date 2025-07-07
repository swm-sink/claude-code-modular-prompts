# Claude Code Framework Settings

## Overview

The settings system provides centralized configuration for the Claude Code Modular Agents framework. All framework behavior, command definitions, quality standards, and execution patterns are controlled through these settings.

## File Structure

```
.claude/settings/
├── settings.json              # Main framework settings (version controlled)
├── settings.local.json        # Personal overrides (gitignored)
├── settings.local.example.json # Template for local settings
└── README.md                  # This file
```

## Main Settings File (`settings.json`)

The main settings file contains all framework configuration organized into logical sections:

### 1. Framework Information
```json
{
  "framework": {
    "name": "Claude Code Modular Agents",
    "version": "2.0.0",
    "description": "...",
    "reality_check": "..."
  }
}
```

### 2. Command Definitions
Each command specifies:
- `description`: What the command does
- `delegation`: Which module handles implementation
- `features`: Command-specific settings and capabilities

Example:
```json
"auto": {
  "description": "Intelligent routing with research-first approach",
  "delegation": "modules/patterns/intelligent-routing.md",
  "features": {
    "research_mandatory": true,
    "complexity_analysis": true,
    "route_to_best_command": true
  }
}
```

### 3. Execution Settings
Global settings that apply across all commands:
- `parallel_execution`: Tool execution optimization
- `read_before_write`: Safety requirement
- `research_first`: Evidence-based approach
- `quality_gates`: Enforcement level
- `token_optimization`: Efficiency settings

### 4. Quality Standards
Defines framework-wide quality requirements:
- TDD cycle enforcement
- Minimum test coverage
- Security standards
- Performance targets
- Documentation requirements

### 5. Module System
Controls how the modular architecture works:
- Delegation patterns
- Token limits
- XML interface requirements
- Dynamic composition rules

### 6. Multi-Agent Patterns
Defines coordination patterns for complex work:
- Task pattern (specialized expertise)
- Batch pattern (similar work across targets)
- Swarm pattern (complex coordination)

### 7. GitHub Integration
Settings for issue tracking and session management:
- Issue templates
- Automation triggers
- Complexity thresholds
- Epic tracking

### 8. Permissions
Security and operation permissions:
- Framework operations
- File operations
- Git operations
- Quality enforcement

## Local Settings (`settings.local.json`)

Personal preferences and development overrides that should not be committed:

```json
{
  "user_preferences": {
    "default_command": "auto",
    "verbose_output": false,
    "preferred_language": "python"
  },
  "development_overrides": {
    "skip_quality_gates": false,
    "debug_mode": false
  }
}
```

## Legacy Files (Deprecated)

The following files have been consolidated into `settings.json` and should no longer be used:
- `commands.json` → Merged into `settings.json` under "commands"
- `core.json` → Merged into framework, execution, and quality sections
- `patterns.json` → Merged into multi_agent_patterns and execution_settings
- `permissions.json` → Merged into permissions section

## Adding New Settings

When adding new settings:

1. **Determine the appropriate section** based on what the setting controls
2. **Use clear, descriptive names** that indicate the setting's purpose
3. **Provide sensible defaults** that work for most use cases
4. **Document the setting** in this README
5. **Consider if it should be overridable** in local settings

## Settings Priority

Settings are loaded in this order (later overrides earlier):
1. Default values in code
2. `settings.json` (main configuration)
3. `settings.local.json` (personal overrides)
4. Environment variables (if implemented)
5. Command-line arguments (if implemented)

## Validation

Settings are validated at framework startup to ensure:
- Required fields are present
- Values are within acceptable ranges
- Delegation targets exist
- No circular dependencies

## Best Practices

1. **Never commit `settings.local.json`** - it's gitignored for a reason
2. **Test changes thoroughly** - settings affect all framework behavior
3. **Maintain backwards compatibility** when updating settings structure
4. **Document all changes** in commit messages and this README
5. **Use type-appropriate values** - booleans for flags, strings for text, numbers for limits

## Troubleshooting

Common issues and solutions:

### Settings not taking effect
- Check for typos in setting names
- Ensure settings.local.json is valid JSON
- Verify the setting is in the correct section
- Restart the framework after changes

### Conflicts between settings
- Local settings override main settings
- More specific settings override general ones
- Check the settings priority order

### Invalid JSON errors
- Use a JSON validator to check syntax
- Common issues: trailing commas, missing quotes, unescaped characters

## Migration Guide

If upgrading from the old multi-file system:

1. **Backup existing settings** before migration
2. **Review the consolidated settings.json** to understand the new structure
3. **Create settings.local.json** from the example for personal preferences
4. **Remove old JSON files** after confirming migration success
5. **Update any scripts or tools** that referenced the old files

## Support

For questions or issues with settings:
1. Check this README first
2. Review example configurations
3. Consult the framework documentation
4. Create an issue if you find a bug