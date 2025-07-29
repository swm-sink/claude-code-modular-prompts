# Installation Test Suite - v1.0

**Purpose**: Comprehensive testing framework for validating installation methods across different environments and project types.

**Test Coverage**: 3 installation methods × 3 environments × 3 project types = 27 test scenarios

---

## 🧪 Test Matrix

### Installation Methods
1. **Git Submodule Integration** (Recommended for updates)
2. **Direct Copy Integration** (Standalone deployment)
3. **Selective Import** (Choose specific components)

### Target Environments
1. **macOS** (Darwin, Homebrew ecosystem)
2. **Linux** (Ubuntu/Debian, package managers)
3. **Windows** (WSL, Git Bash, native)

### Project Types
1. **New Project** (Empty directory, fresh setup)
2. **Existing Project** (Has .claude/ directory already)
3. **Large Project** (Complex structure, many files)

---

## 📋 Test Scenarios

### Scenario 1: Git Submodule - New Project - macOS
```bash
# Test Environment Setup
mkdir test-new-macos && cd test-new-macos
git init

# Installation Test
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh

# Validation Checklist
[ ] .claude-framework submodule created correctly
[ ] .claude/ working directory created
[ ] setup.sh executed without errors
[ ] Guide commands functional (/adapt-to-project)
[ ] Template structure intact (102 commands)
[ ] Documentation accessible
```

### Scenario 2: Direct Copy - Existing Project - Linux
```bash
# Test Environment Setup
mkdir test-existing-linux && cd test-existing-linux
mkdir .claude && echo "existing content" > .claude/settings.json

# Installation Test
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../test-existing-linux

# Validation Checklist
[ ] Existing .claude/ content preserved
[ ] New templates merged correctly
[ ] No file conflicts or overwrites
[ ] Backup created for existing files
[ ] Installation completed successfully
[ ] Both old and new commands accessible
```

### Scenario 3: Selective Import - Large Project - Windows
```bash
# Test Environment Setup (Windows WSL)
mkdir test-large-windows && cd test-large-windows
# Simulate large project structure
mkdir -p src/{components,services,utils} docs tests

# Installation Test
git clone https://github.com/swm-sink/claude-code-modular-prompts
# Manual selective copy of specific commands
cp claude-code-modular-prompts/.claude/commands/core/*.md .claude/commands/core/
cp claude-code-modular-prompts/.claude/commands/development/*.md .claude/commands/development/

# Validation Checklist
[ ] Only selected commands copied
[ ] No unnecessary files imported
[ ] Project structure unchanged
[ ] Selected commands functional
[ ] Dependencies resolved correctly
[ ] Documentation links work
```

---

## 🔍 Detailed Test Procedures

### Pre-Test Environment Setup

#### macOS Setup
```bash
# Verify prerequisites
which git || echo "Install git via Homebrew"
which bash || echo "Bash should be available"
git --version  # Should be 2.20+
```

#### Linux Setup (Ubuntu/Debian)
```bash
# Install prerequisites
sudo apt update
sudo apt install git bash curl
git --version  # Should be 2.20+
```

#### Windows Setup
```bash
# Using WSL or Git Bash
git --version  # Should be 2.20+
# Verify bash shell available
bash --version
```

### Installation Method Testing

#### Method 1: Git Submodule Testing
```bash
#!/bin/bash
# test-submodule-installation.sh

echo "Testing Git Submodule Installation..."

# Test 1: Fresh project
mkdir test-submodule-fresh && cd test-submodule-fresh
git init
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Verify submodule
git submodule status
ls -la .claude-framework/

# Run setup
cd .claude-framework && ./setup.sh
cd ..

# Validate installation
[ -d ".claude" ] && echo "✅ .claude directory created"
[ -f ".claude/commands/core/help.md" ] && echo "✅ Core commands installed"
[ -f ".claude/commands/meta/adapt-to-project.md" ] && echo "✅ Guide commands available"

# Test update mechanism
cd .claude-framework
git pull origin main
./setup.sh  # Should update templates
cd ..

echo "Submodule installation test completed"
```

#### Method 2: Direct Copy Testing
```bash
#!/bin/bash
# test-direct-installation.sh

echo "Testing Direct Copy Installation..."

# Test 1: Clean installation
mkdir test-direct-clean && cd test-direct-clean
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../test-direct-clean
cd ../test-direct-clean

# Validate installation
[ -d ".claude" ] && echo "✅ .claude directory created"
[ $(find .claude/commands -name "*.md" | wc -l) -eq 102 ] && echo "✅ All 102 commands copied"

# Test 2: Existing project merge
mkdir test-direct-existing && cd test-direct-existing
mkdir .claude/commands/custom
echo "custom command" > .claude/commands/custom/my-command.md

# Install over existing
cd ../claude-code-modular-prompts && ./setup.sh ../test-direct-existing
cd ../test-direct-existing

# Validate merge
[ -f ".claude/commands/custom/my-command.md" ] && echo "✅ Existing files preserved"
[ -f ".claude/commands/core/help.md" ] && echo "✅ New templates added"

echo "Direct copy installation test completed"
```

#### Method 3: Selective Import Testing
```bash
#!/bin/bash
# test-selective-installation.sh

echo "Testing Selective Import..."

# Create target project
mkdir test-selective && cd test-selective
mkdir -p .claude/commands/{core,development}

# Clone source
git clone https://github.com/swm-sink/claude-code-modular-prompts source-templates

# Selective copy
cp source-templates/.claude/commands/core/help.md .claude/commands/core/
cp source-templates/.claude/commands/core/task.md .claude/commands/core/
cp source-templates/.claude/commands/development/dev.md .claude/commands/development/

# Validate selective import
[ -f ".claude/commands/core/help.md" ] && echo "✅ Core commands imported"
[ -f ".claude/commands/development/dev.md" ] && echo "✅ Development commands imported"
[ ! -f ".claude/commands/database/db-migrate.md" ] && echo "✅ Unselected commands excluded"

echo "Selective import test completed"
```

### Cross-Platform Compatibility Testing

#### Path Handling Test
```bash
#!/bin/bash
# test-path-compatibility.sh

echo "Testing path handling across platforms..."

# Test absolute paths
setup.sh /tmp/test-absolute

# Test relative paths  
setup.sh ../test-relative
setup.sh ./test-current

# Test spaces in paths
setup.sh "../test with spaces"

# Test special characters (Linux/macOS)
setup.sh "../test-special-chars_123"

echo "Path compatibility test completed"
```

#### Permission Test
```bash
#!/bin/bash
# test-permissions.sh

echo "Testing file permissions..."

# Test script executability
chmod +x setup.sh
./setup.sh test-permissions

# Verify created files have correct permissions
ls -la test-permissions/.claude/commands/core/help.md
# Should be readable (644 or similar)

echo "Permission test completed"
```

---

## 🏗️ Automated Test Runner

### Master Test Script
```bash
#!/bin/bash
# run-installation-tests.sh

set -e

echo "🧪 Claude Code Template Library - Installation Test Suite"
echo "==========================================================="

# Test configuration
REPO_URL="https://github.com/swm-sink/claude-code-modular-prompts"
TEST_DIR="installation-tests-$(date +%s)"
RESULTS_FILE="test-results-$(date +%Y%m%d-%H%M%S).log"

mkdir "$TEST_DIR" && cd "$TEST_DIR"

# Test 1: Git Submodule Installation
echo "Test 1: Git Submodule Installation" | tee -a "$RESULTS_FILE"
mkdir submodule-test && cd submodule-test
git init
if git submodule add "$REPO_URL" .claude-framework; then
    echo "✅ Submodule added successfully" | tee -a "../$RESULTS_FILE"
    cd .claude-framework
    if ./setup.sh; then
        echo "✅ Setup completed successfully" | tee -a "../../$RESULTS_FILE"
    else
        echo "❌ Setup failed" | tee -a "../../$RESULTS_FILE"
    fi
    cd ..
else
    echo "❌ Submodule addition failed" | tee -a "../$RESULTS_FILE"
fi
cd ..

# Test 2: Direct Copy Installation
echo "Test 2: Direct Copy Installation" | tee -a "$RESULTS_FILE"
if git clone "$REPO_URL" direct-test; then
    echo "✅ Repository cloned successfully" | tee -a "$RESULTS_FILE"
    cd direct-test
    if ./setup.sh ../direct-target; then
        echo "✅ Direct installation completed" | tee -a "../$RESULTS_FILE"
        # Validate installation
        if [ -d "../direct-target/.claude" ]; then
            echo "✅ Target directory created" | tee -a "../$RESULTS_FILE"
            COMMAND_COUNT=$(find ../direct-target/.claude/commands -name "*.md" | wc -l)
            echo "📊 Commands installed: $COMMAND_COUNT" | tee -a "../$RESULTS_FILE"
        fi
    else
        echo "❌ Direct installation failed" | tee -a "../$RESULTS_FILE"
    fi
    cd ..
else
    echo "❌ Repository clone failed" | tee -a "$RESULTS_FILE"
fi

# Test 3: Error Handling
echo "Test 3: Error Handling" | tee -a "$RESULTS_FILE"
cd direct-test
# Test invalid target directory
if ./setup.sh /nonexistent/path 2>/dev/null; then
    echo "❌ Should have failed with invalid path" | tee -a "../$RESULTS_FILE"
else
    echo "✅ Correctly handled invalid path" | tee -a "../$RESULTS_FILE"
fi
cd ..

# Test Summary
echo "Installation Test Summary" | tee -a "$RESULTS_FILE"
echo "=========================" | tee -a "$RESULTS_FILE"
echo "Test completed at: $(date)" | tee -a "$RESULTS_FILE"
echo "Results saved to: $RESULTS_FILE" | tee -a "$RESULTS_FILE"

# Cleanup option
echo "Clean up test directory? (y/n)"
read -r cleanup
if [ "$cleanup" = "y" ]; then
    cd .. && rm -rf "$TEST_DIR"
    echo "Test directory cleaned up"
fi
```

### Continuous Integration Test
```yaml
# .github/workflows/installation-test.yml
name: Installation Testing

on:
  push:
    branches: [ main, release/* ]
  pull_request:
    branches: [ main ]

jobs:
  test-installation:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        method: [submodule, direct, selective]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Test Installation Method
      run: |
        chmod +x ./tests/installation/test-${{ matrix.method }}.sh
        ./tests/installation/test-${{ matrix.method }}.sh
    
    - name: Validate Installation
      run: |
        ./tests/installation/validate-installation.sh
    
    - name: Upload Test Results
      uses: actions/upload-artifact@v3
      with:
        name: test-results-${{ matrix.os }}-${{ matrix.method }}
        path: test-results-*.log
```

---

## 📊 Test Results Template

### Test Report Format
```markdown
# Installation Test Results

**Date**: 2025-07-29
**Version**: v1.0.0
**Tester**: [Name/System]
**Environment**: [OS/Version]

## Test Summary
- **Total Tests**: 27
- **Passed**: XX
- **Failed**: XX
- **Skipped**: XX

## Detailed Results

### Git Submodule Installation
| Environment | Status | Duration | Notes |
|-------------|--------|----------|-------|
| macOS       | ✅ Pass | 30s     | No issues |
| Linux       | ✅ Pass | 25s     | No issues |
| Windows     | ❌ Fail | -       | Path issue |

### Direct Copy Installation
| Environment | Status | Duration | Notes |
|-------------|--------|----------|-------|
| macOS       | ✅ Pass | 45s     | No issues |
| Linux       | ✅ Pass | 40s     | No issues |
| Windows     | ✅ Pass | 60s     | WSL required |

### Selective Import
| Environment | Status | Duration | Notes |
|-------------|--------|----------|-------|
| macOS       | ✅ Pass | Manual  | User guided |
| Linux       | ✅ Pass | Manual  | User guided |
| Windows     | ✅ Pass | Manual  | User guided |

## Issues Found
1. **Windows Path Handling**: Native Windows paths not supported
2. **Submodule Updates**: Manual update process needs documentation
3. **Error Messages**: Some error messages not user-friendly

## Recommendations
1. Add Windows native path support
2. Create automated update script for submodules
3. Improve error message clarity
4. Add progress indicators to setup script
```

---

## ✅ Validation Checklist

### Post-Installation Validation
```bash
#!/bin/bash
# validate-installation.sh

echo "🔍 Validating Installation..."

# Check 1: Directory structure
[ -d ".claude" ] && echo "✅ .claude directory exists" || echo "❌ Missing .claude directory"
[ -d ".claude/commands" ] && echo "✅ Commands directory exists" || echo "❌ Missing commands directory"
[ -d ".claude/components" ] && echo "✅ Components directory exists" || echo "❌ Missing components directory"

# Check 2: Command count
COMMAND_COUNT=$(find .claude/commands -name "*.md" | wc -l)
echo "📊 Commands found: $COMMAND_COUNT"
[ "$COMMAND_COUNT" -eq 102 ] && echo "✅ All commands present" || echo "⚠️ Command count mismatch"

# Check 3: Essential commands
[ -f ".claude/commands/core/help.md" ] && echo "✅ Help command available" || echo "❌ Missing help command"
[ -f ".claude/commands/meta/adapt-to-project.md" ] && echo "✅ Guide commands available" || echo "❌ Missing guide commands"

# Check 4: Template integrity
if grep -r "\[INSERT_" .claude/commands/ >/dev/null; then
    echo "✅ Placeholders found in templates"
else
    echo "⚠️ No placeholders found - may be pre-customized"
fi

# Check 5: Documentation
[ -f "README.md" ] && echo "✅ README available" || echo "⚠️ No README found"
[ -f "INSTALLATION.md" ] && echo "✅ Installation guide available" || echo "⚠️ No installation guide"

echo "Validation completed"
```

This comprehensive installation test suite ensures the template library can be reliably deployed across different environments and integration scenarios.