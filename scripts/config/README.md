# Configuration Scripts

Framework configuration management utilities for users to customize and validate their framework setup.

## Directory Structure

```
config/
├── README.md               # This file
├── framework/              # Core framework configuration utilities
└── routing/                # Intelligent routing configuration
```

## Framework Configuration (`framework/`)

### Core Configuration Utilities
- `template_resolver.py` - Resolves configuration templates
- `xml_utils.py` - XML configuration utilities
- `config_integration.py` - Configuration integration helpers
- `script_validator.py` - Script validation utilities

**Usage**:
```bash
# Resolve templates
python scripts/config/framework/template_resolver.py

# XML utilities
python scripts/config/framework/xml_utils.py
```

**Note**: Configuration validation has been moved to `scripts/validation/project_config_validator.py` for better organization.

## Routing Configuration (`routing/`)

### Intelligent Routing
- `deterministic_router.py` - Deterministic command routing logic

**Purpose**: Manages how commands are routed and processed within the framework.

**Usage**:
```bash
python scripts/config/routing/deterministic_router.py
```

## Configuration Files

The framework uses several configuration file types:
- **PROJECT_CONFIG.xml**: Main project configuration
- **Settings files**: JSON-based settings
- **Template files**: Customizable templates

## Validation

Always validate your configuration after changes:
```bash
python scripts/validation/project_config_validator.py
```

## Integration

Configuration scripts integrate with:
- Framework command system
- Module loading system
- Quality gates
- Template resolution

## Requirements

- Python 3.8+
- Framework access
- Valid configuration files