#!/bin/bash

# Test Mode Detection Script
# Tests the mode detection logic in various scenarios

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Helper functions
run_test() {
    local test_name="$1"
    local expected_mode="$2"
    local expected_scope="$3"
    local setup_function="$4"
    local cleanup_function="$5"
    
    echo -n "Testing $test_name... "
    TESTS_RUN=$((TESTS_RUN + 1))
    
    # Setup test environment
    if [[ -n "$setup_function" ]]; then
        $setup_function
    fi
    
    # Source detect_mode.sh
    source ../../.submodule/detect_mode.sh 2>/dev/null
    
    # Check results
    if [[ "$CLAUDE_MODE" == "$expected_mode" ]]; then
        echo -e "${GREEN}PASS${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}FAIL${NC}"
        echo "  Expected mode: $expected_mode"
        echo "  Actual mode: $CLAUDE_MODE"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    # Cleanup
    if [[ -n "$cleanup_function" ]]; then
        $cleanup_function
    fi
    
    # Clear environment
    unset CLAUDE_MODE CLAUDE_ROOT CLAUDE_SCOPE CLAUDE_CONTEXT_DIR CLAUDE_MODE_OVERRIDE
}

# Test setup functions
setup_transformation_mode() {
    touch ../../.transformation/active
}

cleanup_transformation_mode() {
    rm -f ../../.transformation/active
}

setup_override_mode() {
    export CLAUDE_MODE_OVERRIDE=transformation
}

cleanup_override_mode() {
    unset CLAUDE_MODE_OVERRIDE
}

# Run tests
echo "=== Mode Detection Tests ==="
echo

# Test 1: Transformation mode via marker file
run_test "transformation mode (marker file)" "transformation" "" setup_transformation_mode cleanup_transformation_mode

# Test 2: Framework mode (default)
run_test "framework mode (default)" "framework" "" "" ""

# Test 3: Override mode
run_test "override mode" "transformation" "" setup_override_mode cleanup_override_mode

# Test 4: Git detection
(
    cd ../.. || exit 1
    # Ensure we're in a git repo
    if git rev-parse --git-dir > /dev/null 2>&1; then
        run_test "git root detection" "framework" "" "" ""
    else
        echo -e "${YELLOW}SKIP${NC} - Not in git repository"
    fi
)

# Summary
echo
echo "=== Test Summary ==="
echo "Tests run: $TESTS_RUN"
echo -e "Tests passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests failed: ${RED}$TESTS_FAILED${NC}"
echo

# Note about known limitations
if [[ $TESTS_FAILED -gt 0 ]]; then
    echo -e "${YELLOW}Note:${NC} Framework mode test may fail when run from within"
    echo "a transformation project due to dual detection methods."
    echo "See TEST_LIMITATIONS.md for details."
    echo
fi

# Exit code
if [[ $TESTS_FAILED -eq 0 ]]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed!${NC}"
    exit 1
fi