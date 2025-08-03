#!/bin/bash

# Test Integration Script
# Tests the complete integration flow for both transformation and framework modes

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0
WARNINGS=0

# Helper functions
test_file_exists() {
    local file="$1"
    local description="$2"
    
    echo -n "Checking $description... "
    TESTS_RUN=$((TESTS_RUN + 1))
    
    if [[ -f "$file" ]]; then
        echo -e "${GREEN}EXISTS${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}MISSING${NC}"
        echo "  Expected file: $file"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

test_directory_exists() {
    local dir="$1"
    local description="$2"
    
    echo -n "Checking $description... "
    TESTS_RUN=$((TESTS_RUN + 1))
    
    if [[ -d "$dir" ]]; then
        echo -e "${GREEN}EXISTS${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}MISSING${NC}"
        echo "  Expected directory: $dir"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

test_script_executable() {
    local script="$1"
    local description="$2"
    
    echo -n "Checking $description is executable... "
    TESTS_RUN=$((TESTS_RUN + 1))
    
    if [[ -x "$script" ]]; then
        echo -e "${GREEN}EXECUTABLE${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}NOT EXECUTABLE${NC}"
        echo "  Script: $script"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

test_environment_variable() {
    local var_name="$1"
    local expected_value="$2"
    local description="$3"
    
    echo -n "Checking $description... "
    TESTS_RUN=$((TESTS_RUN + 1))
    
    # Source detect_mode.sh
    source ../../.submodule/detect_mode.sh 2>/dev/null
    
    local actual_value="${!var_name}"
    
    if [[ -n "$expected_value" ]]; then
        if [[ "$actual_value" == "$expected_value" ]]; then
            echo -e "${GREEN}CORRECT${NC} ($actual_value)"
            TESTS_PASSED=$((TESTS_PASSED + 1))
            return 0
        else
            echo -e "${RED}INCORRECT${NC}"
            echo "  Expected: $expected_value"
            echo "  Actual: $actual_value"
            TESTS_FAILED=$((TESTS_FAILED + 1))
            return 1
        fi
    else
        if [[ -n "$actual_value" ]]; then
            echo -e "${GREEN}SET${NC} ($actual_value)"
            TESTS_PASSED=$((TESTS_PASSED + 1))
            return 0
        else
            echo -e "${RED}NOT SET${NC}"
            TESTS_FAILED=$((TESTS_FAILED + 1))
            return 1
        fi
    fi
}

# Start testing
echo "=== Integration Tests ==="
echo
echo "Running from: $(pwd)"
echo

# Test core directory structure
echo "--- Directory Structure ---"
test_directory_exists "../../.transformation" ".transformation directory"
test_directory_exists "../../.claude/framework" ".claude/framework directory"
test_directory_exists "../../.claude/project" ".claude/project directory"
test_directory_exists "../../.submodule" ".submodule directory"

echo

# Test core scripts
echo "--- Core Scripts ---"
test_file_exists "../../.submodule/detect_mode.sh" "detect_mode.sh"
test_script_executable "../../.submodule/detect_mode.sh" "detect_mode.sh"
test_file_exists "../../.submodule/setup.sh" "setup.sh"
test_script_executable "../../.submodule/setup.sh" "setup.sh"
test_file_exists "../../.transformation/commands/backup_existing.sh" "backup_existing.sh"

echo

# Test templates
echo "--- Templates ---"
test_file_exists "../../.submodule/templates/.gitmodules.template" ".gitmodules template"
test_file_exists "../../.submodule/templates/.gitignore.template" ".gitignore template"

echo

# Test README files
echo "--- Documentation ---"
test_file_exists "../../.transformation/README.md" "transformation README"
test_file_exists "../../.claude/framework/README.md" "framework README"
test_file_exists "../../.submodule/README.md" "submodule README"

echo

# Test marker files
echo "--- Marker Files ---"
if [[ -f "../../.transformation/active" ]]; then
    echo -e "Transformation mode marker: ${GREEN}ACTIVE${NC}"
else
    echo -e "Transformation mode marker: ${YELLOW}INACTIVE${NC}"
    WARNINGS=$((WARNINGS + 1))
fi

echo

# Test environment variables
echo "--- Environment Variables ---"
# Clear any overrides
unset CLAUDE_MODE_OVERRIDE

# Test in current state
test_environment_variable "CLAUDE_MODE" "" "CLAUDE_MODE"
test_environment_variable "CLAUDE_ROOT" "" "CLAUDE_ROOT"
test_environment_variable "CLAUDE_SCOPE" "" "CLAUDE_SCOPE"
test_environment_variable "CLAUDE_CONTEXT_DIR" "" "CLAUDE_CONTEXT_DIR"

echo

# Test mode switching
echo "--- Mode Switching ---"
echo -n "Testing transformation mode activation... "
touch ../../.transformation/active
source ../../.submodule/detect_mode.sh 2>/dev/null
if [[ "$CLAUDE_MODE" == "transformation" ]]; then
    echo -e "${GREEN}PASS${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
else
    echo -e "${RED}FAIL${NC}"
    TESTS_FAILED=$((TESTS_FAILED + 1))
fi
TESTS_RUN=$((TESTS_RUN + 1))

echo -n "Testing framework mode activation... "
rm -f ../../.transformation/active
source ../../.submodule/detect_mode.sh 2>/dev/null
if [[ "$CLAUDE_MODE" == "framework" ]]; then
    echo -e "${GREEN}PASS${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
else
    echo -e "${RED}FAIL${NC}"
    TESTS_FAILED=$((TESTS_FAILED + 1))
fi
TESTS_RUN=$((TESTS_RUN + 1))

echo

# Summary
echo "=== Test Summary ==="
echo "Tests run: $TESTS_RUN"
echo -e "Tests passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests failed: ${RED}$TESTS_FAILED${NC}"
if [[ $WARNINGS -gt 0 ]]; then
    echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
fi
echo

# Exit code
if [[ $TESTS_FAILED -eq 0 ]]; then
    echo -e "${GREEN}All integration tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some integration tests failed!${NC}"
    exit 1
fi