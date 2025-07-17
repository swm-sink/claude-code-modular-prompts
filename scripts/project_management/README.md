# Project Management Scripts

High-level project management and configuration tools for comprehensive project operations.

## Scripts

### `config_parser.py`
**Purpose**: PROJECT_CONFIG.xml parsing and analysis utilities

**Features**:
- Deep XML configuration parsing
- Configuration validation and schema checking
- Hierarchical setting resolution
- Template variable expansion
- Configuration comparison and diff analysis
- Export to multiple formats (JSON, YAML, environment variables)

**Usage**:
```bash
# Parse and display configuration
python scripts/project_management/config_parser.py

# Analyze configuration structure
python scripts/project_management/config_parser.py --analyze

# Export to JSON format
python scripts/project_management/config_parser.py --export-json config.json

# Debug configuration resolution
python scripts/project_management/config_parser.py --debug
```

**Configuration Analysis Features**:
- **Schema Validation**: Ensures XML follows framework schema
- **Completeness Check**: Identifies missing required configurations
- **Consistency Validation**: Checks for conflicting settings
- **Template Resolution**: Expands all template variables
- **Dependency Analysis**: Maps configuration dependencies

## Integration

Project management scripts provide:
- **Configuration backbone** for all other framework components
- **Project setup foundation** for initialization workflows
- **Settings management** for framework customization
- **Integration points** for CI/CD and deployment pipelines

## Future Enhancements

This directory is designed to grow with additional project management tools:
- Project metrics and analytics
- Resource planning and allocation
- Team coordination utilities
- Project lifecycle management
- Configuration migration tools

## Dependencies

Scripts in this directory may depend on:
- `scripts/lib/` utilities for common functionality
- `scripts/validation/` for configuration validation
- PROJECT_CONFIG.xml as the central configuration source
- Framework structure defined in .claude/ directory