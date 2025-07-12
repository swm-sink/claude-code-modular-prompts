# Terminology Standardization Guide

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-12   | stable |

## Purpose

This guide enforces consistent terminology across all documentation to eliminate user confusion and maintain professional standards throughout the Claude Code Modular Prompts Framework.

## Standardization Authority

**Source**: CLAUDE.md - Framework Control Document
**Enforcement**: MANDATORY across all documentation files

## Primary Terminology Standards

### Framework Identity
- **PREFERRED**: "Claude Code Modular Prompts Framework" (full official name)
- **STANDARD**: "framework" (not "system" or "platform")
- **CONTEXT**: When referring to the overall system, always use "framework"

### Technical References
- **PREFERRED**: "claude-code" (hyphenated in technical contexts)
- **CONTEXT**: Command references, file paths, technical documentation
- **EXAMPLE**: "claude-code-modular-prompts.git"

### Command Terminology
- **PREFERRED**: "command" (not "cmd" or "instruction")
- **CONTEXT**: All references to /task, /swarm, /auto, etc.
- **CONSISTENCY**: "command system", "command usage", "framework commands"

### Module References
- **PREFERRED**: "module" (not "component" or "plugin")
- **CONTEXT**: All references to framework modules
- **CONSISTENCY**: "module composition", "module runtime", "framework modules"

## Prohibited Terminology

### Inconsistent Framework Terms
- ❌ "system" (unless referring to operating system)
- ❌ "platform" (unless referring to deployment platform)
- ❌ "tool" (when referring to the framework)

### Inconsistent Command Terms
- ❌ "cmd" 
- ❌ "instruction"
- ❌ "directive"

### Inconsistent Module Terms
- ❌ "component"
- ❌ "plugin"
- ❌ "extension"

## Special Cases

### Technical Documentation
- Repository names: "claude-code-modular-prompts" (hyphenated)
- File paths: "claude-code" (hyphenated)
- URLs: "claude-code" (hyphenated)

### User-Facing Documentation
- Product name: "Claude Code Modular Prompts Framework" (full name)
- Short reference: "framework" (not system/platform)
- Commands: "framework commands" (not framework instructions)

### Domain-Specific Contexts
- **Architecture**: "framework architecture", "module composition"
- **Development**: "framework development", "command development"
- **Integration**: "framework integration", "module integration"

## Implementation Rules

### Global Replacements
1. "system" → "framework" (except OS contexts)
2. "platform" → "framework" (except deployment contexts)
3. "cmd" → "command"
4. "instruction" → "command"
5. "component" → "module"
6. "plugin" → "module"

### Context-Sensitive Replacements
- Configuration contexts: Always "framework configuration"
- Technical contexts: Always "framework architecture"
- User contexts: Always "framework usage"

## Quality Validation

### Automated Checks
- No instances of prohibited terminology
- Consistent capitalization of "Framework" in titles
- Proper hyphenation in technical contexts

### Manual Review Points
- Professional tone throughout
- Consistent user experience
- Clear technical communication

## Version Control

### Update Requirements
- All terminology changes require version table updates
- Consistency score tracking mandatory
- Cross-reference validation required

### Enforcement
- **Blocking**: Documentation with inconsistent terminology
- **Validation**: Required before any documentation approval
- **Monitoring**: Continuous compliance checking

---

*This guide ensures the Claude Code Modular Prompts Framework maintains professional, consistent terminology that reduces user confusion and enhances documentation quality.*