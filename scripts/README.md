# Scripts Directory

Framework automation, validation, and configuration management utilities organized by function.

## 📁 Structure

### `automation/` - Project Automation
**Purpose**: Complete project lifecycle automation
- `deployment_pipeline.py` - Comprehensive deployment orchestrator with security scanning and rollback capabilities
- `health_monitor.py` - Framework health monitoring with real-time alerts and performance tracking  
- `project_initializer.py` - Intelligent project setup wizard with tech stack auto-detection
- `test_runner.py` - Multi-framework testing automation with quality gate enforcement

### `validation/` - Quality Assurance
**Purpose**: Framework validation and integrity checking
- `project_config_validator.py` - Unified PROJECT_CONFIG.xml validation system
- `reference_validator.py` - Cross-reference and link validation (moved from root)
- `performance_benchmark.py` - Framework performance analysis and optimization (moved from root)
- `validate_all.sh` - Comprehensive validation runner (moved from root)

### `project_management/` - Project Operations
**Purpose**: High-level project management and configuration
- `config_parser.py` - PROJECT_CONFIG.xml parsing and analysis utilities (moved from root)

### `config/` - Configuration Management
**Purpose**: Configuration management and framework integration
- `framework/` - Core framework configuration handling
- `routing/` - Intelligent routing and decision systems
- `configuration_monitor.py` - Real-time configuration monitoring
- `smart_defaults_engine.py` - Context-aware default value generation

### `lib/` - Shared Utilities
**Purpose**: Reusable utilities and standardized patterns
- `error_handling.py` - **NEW** Standardized error handling, logging, and exit codes
- `import_analysis.py` - Python import analysis and dependency mapping
- `module_utils.py` - Module discovery and validation utilities

### `setup/` - Initial Setup
**Purpose**: Framework installation and environment configuration
- `setup_precommit.sh` - Configure pre-commit hooks for framework validation

## 🚀 Usage Patterns

### Complete Project Lifecycle
```bash
# 1. Initialize new project
python scripts/automation/project_initializer.py

# 2. Run comprehensive validation
bash scripts/validation/validate_all.sh

# 3. Run tests with quality gates
python scripts/automation/test_runner.py --enforce-gates

# 4. Deploy to staging
python scripts/automation/deployment_pipeline.py --target staging

# 5. Monitor health
python scripts/automation/health_monitor.py --watch
```

### Configuration Management
```bash
# Validate project configuration
python scripts/validation/project_config_validator.py --validate

# Parse and analyze configuration
python scripts/project_management/config_parser.py --analyze

# Monitor configuration changes
python scripts/config/configuration_monitor.py --watch

# Generate optimal defaults
python scripts/config/smart_defaults_engine.py --analyze
```

### Quality Assurance Workflow
```bash
# Validate cross-references
python scripts/validation/reference_validator.py --fix

# Performance benchmarking
python scripts/validation/performance_benchmark.py --comprehensive

# Complete validation suite
bash scripts/validation/validate_all.sh
```

### Development and Debugging
```bash
# Analyze import dependencies
python scripts/lib/import_analysis.py --target src/

# Framework health check
python scripts/automation/health_monitor.py --check-all

# Configuration analysis
python scripts/project_management/config_parser.py --debug
```

## 📋 Standardized Patterns

### Error Handling
All scripts now use standardized error handling from `lib/error_handling.py`:
```python
from scripts.lib.error_handling import setup_logging, handle_errors, ScriptError

logger = setup_logging(__name__, verbose=args.verbose)

@handle_errors(logger)
def main():
    # Your script logic here
    return 0  # Success
```

### Exit Codes
- `0` - Success
- `1` - General error
- `2` - Validation error  
- `3` - Configuration error
- `4` - Permission error
- `130` - User cancelled

### Naming Conventions
- **Python scripts**: `script_name.py` (underscores)
- **Shell scripts**: `script-name.sh` (hyphens)
- **Descriptive names**: Clearly indicate purpose and function

## 🔧 Integration

All scripts integrate with:
- **PROJECT_CONFIG.xml** configuration system
- **.claude/** framework structure  
- **Git workflows** and pre-commit hooks
- **CI/CD pipelines** through standardized exit codes
- **Quality gates** and TDD enforcement
- **Standardized error handling** and logging

## 🛠️ Development Guidelines

When adding new scripts:

1. **Use error handling**: Import from `lib/error_handling.py`
2. **Follow naming**: Underscores for Python, hyphens for shell
3. **CLI interface**: Comprehensive argparse with examples
4. **Configuration**: Integrate with PROJECT_CONFIG.xml
5. **User feedback**: Progress tracking and clear messages
6. **Safety**: Include --dry-run modes
7. **Debugging**: Support --verbose output
8. **Documentation**: Include docstrings and help text

## 📈 Recent Improvements (Phase 2.3)

- ✅ **Reorganized structure** - Logical grouping by function
- ✅ **Standardized naming** - Consistent underscore/hyphen conventions  
- ✅ **Error handling** - Unified patterns across all scripts
- ✅ **Updated references** - Fixed all cross-references after moves
- ✅ **Enhanced documentation** - Clear structure and usage patterns