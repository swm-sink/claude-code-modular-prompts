#!/bin/bash
# 🔴 TDD: Test Startup Protection Script - RED Phase

# Test framework setup
TESTS_PASSED=0
TESTS_FAILED=0
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Test helper functions
assert_equals() {
    if [ "$1" = "$2" ]; then
        echo -e "${GREEN}✓ $3${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ $3${NC}"
        echo "  Expected: $2"
        echo "  Actual: $1"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

assert_file_exists() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓ $2${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ $2${NC}"
        echo "  File not found: $1"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

assert_symlink_exists() {
    if [ -L "$1" ]; then
        echo -e "${GREEN}✓ $2${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ $2${NC}"
        echo "  Symlink not found: $1"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Setup test environment
setup_test_env() {
    export TEST_DIR=$(mktemp -d)
    export TEST_HOME="$TEST_DIR/home"
    export TEST_PROJECT="$TEST_DIR/project"
    
    mkdir -p "$TEST_HOME/.claude"
    mkdir -p "$TEST_PROJECT/.claude/tools"
    
    # Override paths in script
    export HOME="$TEST_HOME"
    export PROJECT_ROOT="$TEST_PROJECT"
}

cleanup_test_env() {
    rm -rf "$TEST_DIR"
}

# Test 1: Script creates necessary directories
test_creates_directories() {
    echo "Test: Script creates necessary directories"
    setup_test_env
    
    # This will fail until script is implemented
    source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>/dev/null || true
    
    assert_file_exists "$TEST_PROJECT/.claude_aliases" "Creates aliases file"
    
    cleanup_test_env
}

# Test 2: Script detects missing symlink
test_detects_missing_symlink() {
    echo -e "\nTest: Script detects missing symlink"
    setup_test_env
    
    # No symlink exists
    OUTPUT=$(source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>&1 || true)
    
    if echo "$OUTPUT" | grep -q "Local settings missing"; then
        echo -e "${GREEN}✓ Detects missing symlink${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ Failed to detect missing symlink${NC}"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    cleanup_test_env
}

# Test 3: Script repairs broken symlink
test_repairs_broken_symlink() {
    echo -e "\nTest: Script repairs broken symlink"
    setup_test_env
    
    # Create broken symlink
    touch "$TEST_PROJECT/.claude/settings.local.json"
    
    source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>/dev/null || true
    
    assert_symlink_exists "$TEST_PROJECT/.claude/settings.local.json" "Repairs broken symlink"
    
    cleanup_test_env
}

# Test 4: Script detects missing permissions
test_detects_missing_permissions() {
    echo -e "\nTest: Script detects missing permissions"
    setup_test_env
    
    # Create settings without permissions
    echo '{"env":{}}' > "$TEST_HOME/.claude/settings.json"
    
    OUTPUT=$(source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>&1 || true)
    
    if echo "$OUTPUT" | grep -q "Missing required permissions"; then
        echo -e "${GREEN}✓ Detects missing permissions${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ Failed to detect missing permissions${NC}"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    cleanup_test_env
}

# Test 5: Script creates working aliases
test_creates_working_aliases() {
    echo -e "\nTest: Script creates working aliases"
    setup_test_env
    
    source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>/dev/null || true
    
    if [ -f "$TEST_PROJECT/.claude_aliases" ]; then
        # Check alias content
        if grep -q "alias fortress=" "$TEST_PROJECT/.claude_aliases"; then
            echo -e "${GREEN}✓ Creates fortress alias${NC}"
            TESTS_PASSED=$((TESTS_PASSED + 1))
        else
            echo -e "${RED}✗ Missing fortress alias${NC}"
            TESTS_FAILED=$((TESTS_FAILED + 1))
        fi
        
        if grep -q "alias unfuck-permissions=" "$TEST_PROJECT/.claude_aliases"; then
            echo -e "${GREEN}✓ Creates unfuck-permissions alias${NC}"
            TESTS_PASSED=$((TESTS_PASSED + 1))
        else
            echo -e "${RED}✗ Missing unfuck-permissions alias${NC}"
            TESTS_FAILED=$((TESTS_FAILED + 1))
        fi
    fi
    
    cleanup_test_env
}

# Test 6: Script provides correct status summary
test_status_summary() {
    echo -e "\nTest: Script provides status summary"
    setup_test_env
    
    # Setup correct environment
    echo '{"permissions":{"allow":["Bash(*)","Read(*)","Edit(*)"],"deny":[]}}' > "$TEST_HOME/.claude/settings.json"
    ln -sf "$TEST_HOME/.claude/settings.json" "$TEST_PROJECT/.claude/settings.local.json"
    
    OUTPUT=$(source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>&1 || true)
    
    if echo "$OUTPUT" | grep -q "ALL SYSTEMS OPERATIONAL"; then
        echo -e "${GREEN}✓ Shows operational status${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ Wrong status shown${NC}"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    cleanup_test_env
}

# Test 7: Script handles permission fortress integration
test_fortress_integration() {
    echo -e "\nTest: Script integrates with permission fortress"
    setup_test_env
    
    # Create mock fortress script
    cat > "$TEST_PROJECT/.claude/tools/permission_fortress.py" << 'EOF'
#!/usr/bin/env python3
print("Permission fortress check executed")
EOF
    chmod +x "$TEST_PROJECT/.claude/tools/permission_fortress.py"
    
    OUTPUT=$(source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>&1 || true)
    
    # Should call fortress when permissions missing
    echo '{}' > "$TEST_HOME/.claude/settings.json"
    OUTPUT=$(source "$SCRIPT_DIR/../tools/startup_protection.sh" 2>&1 || true)
    
    if echo "$OUTPUT" | grep -q "Running permission fortress repair"; then
        echo -e "${GREEN}✓ Calls permission fortress${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ Failed to call permission fortress${NC}"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    cleanup_test_env
}

# Run all tests
echo "🔴 Running Startup Protection Tests (RED Phase)"
echo "=============================================="

test_creates_directories
test_detects_missing_symlink
test_repairs_broken_symlink
test_detects_missing_permissions
test_creates_working_aliases
test_status_summary
test_fortress_integration

# Summary
echo -e "\n=============================================="
echo "Test Results:"
echo -e "${GREEN}Passed: $TESTS_PASSED${NC}"
echo -e "${RED}Failed: $TESTS_FAILED${NC}"

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "\n${GREEN}All tests passed! Ready for GREEN phase.${NC}"
    exit 0
else
    echo -e "\n${RED}Tests failed. This is expected in RED phase.${NC}"
    exit 1
fi