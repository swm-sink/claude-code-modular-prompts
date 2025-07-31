# Tests Directory

This directory contains testing frameworks, validation scripts, and test methodologies for the Claude Code Template Library.

## Testing Framework Overview

### Core Testing Philosophy
See **`TESTING-METHODOLOGY.md`** for complete testing approach and framework documentation.

## Test Scripts

### Installation Testing
- **`test_setup.sh`** - Setup script validation
- **`test-installation-methods.sh`** - Multiple installation method testing
- **`test_validate_adaptation.sh`** - Adaptation validation testing

### Functional Testing
- **`test_functional_validation.sh`** - Feature functionality validation
- **`test_e2e_workflow.sh`** - End-to-end workflow testing

### Command Validation
- **`validate-command.sh`** - Individual command structure validation
- **`run_all_tests.sh`** - Comprehensive test suite execution

### Framework Files
- **`__init__.py`** - Python testing framework initialization
- **`TESTING-METHODOLOGY.md`** - Complete testing strategy and approach

## Testing Scope

### Structural Validation
- **YAML Front Matter** - Command metadata validation
- **Content Structure** - Command documentation adequacy
- **File Organization** - Directory structure validation

### Functional Testing  
- **Installation Methods** - All installation approaches
- **Command Effectiveness** - Template functionality
- **Integration Testing** - Claude Code compatibility

### Quality Assurance
- **Performance Testing** - Response time optimization
- **Error Handling** - Failure recovery testing
- **Cross-Platform** - Multi-environment compatibility

## Usage Guide

### Running Individual Tests
```bash
# Validate specific command structure
./validate-command.sh .claude/commands/core/task.md

# Test installation methods
./test-installation-methods.sh

# Validate setup process
./test_setup.sh
```

### Running Complete Test Suite
```bash
# Execute all tests
./run_all_tests.sh

# End-to-end workflow testing
./test_e2e_workflow.sh
```

### Validation Testing
```bash
# Test adaptation validation
./test_validate_adaptation.sh

# Functional validation testing
./test_functional_validation.sh
```

## Test Results

### Current Validation Status
- **Structural Validation**: 100% (88/88 commands passing)
- **YAML Compliance**: 100% (all commands have proper metadata)
- **Installation Testing**: Multi-environment compatibility verified

### Test Coverage
- **Command Templates**: All 88 commands validated
- **Installation Methods**: All 3 methods tested
- **Platform Support**: macOS, Linux, Windows compatibility

## Development Guidelines

### Writing New Tests
1. Follow patterns in existing test scripts
2. Use clear test descriptions and error messages
3. Ensure tests are idempotent (can run multiple times)
4. Add comprehensive error handling

### Test Execution Standards
- Tests should be fast (< 30 seconds per script)
- Tests should be independent (no dependencies between tests)
- Tests should clean up after themselves
- Tests should provide clear pass/fail indicators

## Framework Integration

### Continuous Integration
- Tests designed for CI/CD pipeline integration
- Clear exit codes for automation
- Detailed logging for debugging

### Quality Gates
- All tests must pass before release
- New features require corresponding tests
- Breaking changes require test updates

*For detailed testing methodology and philosophy, see `TESTING-METHODOLOGY.md`*