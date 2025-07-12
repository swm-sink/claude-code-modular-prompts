# Template System

| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

## Purpose
Template system for dynamic configuration and reusable components across the framework.

## Contents

### Configuration Templates
- `project_config.xml` - Main project configuration template
- `domain_config.xml` - Domain-specific configuration overrides
- `quality_config.xml` - Quality gate configuration template

### Code Templates
- `command_template.md` - Template for new commands
- `module_template.md` - Template for new modules
- `persona_template.md` - Template for new personas

### Documentation Templates
- `readme_template.md` - Standard README structure
- `guide_template.md` - User guide template
- `api_docs_template.md` - API documentation template

## Template Resolution
Templates support dynamic resolution with `[PROJECT_CONFIG: path | DEFAULT: value]` syntax.

## Integration
Templates are loaded by the configuration system and resolved at runtime.