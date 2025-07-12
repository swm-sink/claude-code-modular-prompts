# Scripts Directory - User Operations

This directory contains user-facing operational scripts for the Claude Code Framework. These scripts are designed for everyday framework operations, setup, and utilities.

## Directory Structure

```
scripts/
├── README.md               # This file - user guide to available scripts
├── setup/                  # User setup utilities
├── config/                 # Configuration management
└── utilities/              # User utility scripts
```

## User-Facing Scripts

### Setup Scripts (`setup/`)
**Purpose**: Initial framework setup and configuration
- `setup_precommit.sh` - Sets up pre-commit hooks for framework validation

### Configuration Scripts (`config/`)
**Purpose**: Framework configuration and management utilities
- `framework/` - Core framework configuration utilities
  - `config_validator.py` - Validates framework configuration files
  - `template_resolver.py` - Resolves configuration templates
  - `xml_utils.py` - XML configuration utilities
- `routing/` - Intelligent routing configuration
  - `deterministic_router.py` - Deterministic command routing logic

### Utility Scripts (`utilities/`)
**Purpose**: General purpose utilities for framework users
- `check-duplications.py` - Scans for duplicate content across modules
- `visualize.py` - Creates visual representations of framework structure

## Usage

All scripts should be run from the project root:

```bash
# Setup scripts
bash scripts/setup/setup_precommit.sh

# Configuration validation
python scripts/config/framework/config_validator.py

# Utilities
python scripts/utilities/check-duplications.py
python scripts/utilities/visualize.py
```

## For Developers

Development, testing, validation, and monitoring scripts have been moved to organized directories:

- **Development Scripts**: `internal/development/` - Development tools, testing, optimization
- **Validation Scripts**: `internal/validation/` - Quality assurance and validation tools
- **Monitoring Scripts**: `internal/monitoring/` - Health monitoring and performance tracking

See respective README files in those directories for development-focused scripts.

## Output and Logs

Script outputs are ignored by git (configured in .gitignore):
- `scripts/output/`
- `scripts/logs/`
- `*.output`
- `*.result`

## Support

For issues with scripts:
1. Check the specific script's documentation
2. Verify your environment meets requirements
3. Run with `-v` or `--verbose` flags when available
4. Consult the framework documentation in `docs/`