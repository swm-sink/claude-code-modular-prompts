# Commands Directory

*Version: 1.0.0*
*Purpose: Command definitions and routing*

## 📁 Directory Structure

This directory contains command definitions that are referenced in CLAUDE.md. Currently, commands are defined inline in CLAUDE.md's architecture section, but this directory exists for:

1. **Future Migration**: Moving command definitions from CLAUDE.md to individual files
2. **Custom Commands**: User-defined commands can be added here
3. **Command Extensions**: Additional command-specific logic

## 🔗 Current Command Architecture

Commands are currently defined in CLAUDE.md under the `<architecture>` section with @ links to their implementing modules:

```xml
<cmd name="/auto" module="@modules/patterns/intelligent-routing.md"/>
<cmd name="/task" module="@modules/patterns/tdd-cycle-pattern.md"/>
<!-- etc -->
```

## 📝 Command Definition Format (Future)

When commands are migrated to individual files, they will follow this structure:

```markdown
# Command: /command-name
Purpose: One-line description
Module: @modules/category/implementation.md

## Interface
- Input: Description of expected input
- Output: Description of output
- Options: Any command options

## Validation
- Input validation rules
- Pre-conditions
- Security checks

## Error Handling
- Common errors and recovery
- User-friendly messages
```

## 🚀 Adding Custom Commands

To add a custom command:

1. Create a new file: `command-name.md`
2. Follow the format above
3. Add entry to CLAUDE.md architecture section
4. Implement module in appropriate location

## 🔒 Security Note

All commands must validate input using patterns from SECURITY_VALIDATION.md before delegation to modules.

---

*Note: This directory structure addresses the architectural gap identified during framework hardening.*