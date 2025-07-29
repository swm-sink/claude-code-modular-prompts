#!/bin/bash

# TDD Tests for validate-adaptation.sh
# These tests MUST pass before implementation is complete

# Test framework setup
TEST_COUNT=0
PASSED_COUNT=0
FAILED_COUNT=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Helper functions
assert_equals() {
    local expected="$1"
    local actual="$2" 
    local test_name="$3"
    
    TEST_COUNT=$((TEST_COUNT + 1))
    
    if [ "$expected" = "$actual" ]; then
        echo -e "${GREEN}✅ PASS${NC}: $test_name"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        echo -e "${RED}❌ FAIL${NC}: $test_name"
        echo "   Expected: '$expected'"
        echo "   Actual:   '$actual'"
        FAILED_COUNT=$((FAILED_COUNT + 1))
    fi
}

assert_contains() {
    local haystack="$1"
    local needle="$2"
    local test_name="$3"
    
    TEST_COUNT=$((TEST_COUNT + 1))
    
    if echo "$haystack" | grep -q "$needle"; then
        echo -e "${GREEN}✅ PASS${NC}: $test_name"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        echo -e "${RED}❌ FAIL${NC}: $test_name"
        echo "   Expected '$haystack' to contain '$needle'"
        FAILED_COUNT=$((FAILED_COUNT + 1))
    fi
}

assert_file_exists() {
    local file_path="$1"
    local test_name="$2"
    
    TEST_COUNT=$((TEST_COUNT + 1))
    
    if [ -f "$file_path" ]; then
        echo -e "${GREEN}✅ PASS${NC}: $test_name"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        echo -e "${RED}❌ FAIL${NC}: $test_name"
        echo "   File '$file_path' does not exist"
        FAILED_COUNT=$((FAILED_COUNT + 1))
    fi
}

# Setup test environment
setup_test_env() {
    TEST_DIR="/tmp/claude_test_$$"
    mkdir -p "$TEST_DIR"
    cd "$TEST_DIR"
    
    # Create basic structure
    mkdir -p .claude/commands/core
    mkdir -p .claude/config
    mkdir -p .claude-framework
    
    # Source the validation script functions
    if [ -f "/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca/validate-adaptation.sh" ]; then
        source "/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca/validate-adaptation.sh"
    fi
}

teardown_test_env() {
    cd /
    rm -rf "$TEST_DIR"
}

# Test 1: Directory Structure Validation
test_check_directory_structure() {
    echo ""
    echo "=== Test Group: Directory Structure ==="
    
    # Test: Should pass with correct structure
    mkdir -p .claude .claude-framework
    result=$(check_directory_structure 2>&1)
    assert_contains "$result" "Directory structure correct" "Directory structure validation - valid case"
    
    # Test: Should fail without .claude
    rm -rf .claude
    result=$(check_directory_structure 2>&1)
    assert_contains "$result" "Missing directories" "Directory structure validation - missing .claude"
    
    # Test: Should fail without .claude-framework  
    mkdir -p .claude
    rm -rf .claude-framework
    result=$(check_directory_structure 2>&1)
    assert_contains "$result" "Missing directories" "Directory structure validation - missing .claude-framework"
}

# Test 2: Placeholder Count Validation
test_count_placeholders() {
    echo ""
    echo "=== Test Group: Placeholder Counting ==="
    
    # Setup test files
    mkdir -p .claude/commands/core
    
    # Test: No placeholders
    echo "name: /test" > .claude/commands/core/test.md
    echo "description: A test command" >> .claude/commands/core/test.md
    count=$(count_remaining_placeholders)
    assert_equals "0" "$count" "Placeholder count - no placeholders"
    
    # Test: Single placeholder
    echo "Content with [INSERT_PROJECT_NAME] placeholder" >> .claude/commands/core/test.md
    count=$(count_remaining_placeholders)
    assert_equals "1" "$count" "Placeholder count - single placeholder"
    
    # Test: Multiple placeholders
    echo "name: /test2" > .claude/commands/core/test2.md
    echo "[INSERT_DOMAIN] and [INSERT_TECH_STACK]" >> .claude/commands/core/test2.md
    count=$(count_remaining_placeholders)
    assert_equals "3" "$count" "Placeholder count - multiple placeholders"
}

# Test 3: Configuration Validation
test_validate_configuration() {
    echo ""
    echo "=== Test Group: Configuration Validation ==="
    
    mkdir -p .claude/config
    
    # Test: Missing config file
    result=$(validate_project_config 2>&1)
    status=$?
    assert_equals "1" "$status" "Configuration validation - missing file"
    
    # Test: Config with placeholders
    cat > .claude/config/project-config.xml << 'EOF'
<project-config>
  <name>[INSERT_PROJECT_NAME]</name>
  <domain>[INSERT_DOMAIN]</domain>
</project-config>
EOF
    result=$(validate_project_config 2>&1)
    status=$?
    assert_equals "1" "$status" "Configuration validation - has placeholders"
    
    # Test: Complete config
    cat > .claude/config/project-config.xml << 'EOF'
<project-config>
  <name>TestProject</name>
  <domain>testing</domain>
</project-config>
EOF
    result=$(validate_project_config 2>&1)
    status=$?
    assert_equals "0" "$status" "Configuration validation - complete config"
}

# Test 4: Duplicate Command Detection
test_check_duplicate_commands() {
    echo ""
    echo "=== Test Group: Duplicate Command Detection ==="
    
    # Clean start for this test
    rm -rf .claude
    mkdir -p .claude/commands/core .claude/commands/dev
    
    # Test: No duplicates
    echo "name: /test1" > .claude/commands/core/test1.md
    echo "name: /test2" > .claude/commands/dev/test2.md
    count=$(count_duplicate_commands)
    assert_equals "0" "$count" "Duplicate detection - no duplicates"
    
    # Test: One duplicate
    echo "name: /test1" > .claude/commands/dev/test1_duplicate.md
    count=$(count_duplicate_commands)
    assert_equals "1" "$count" "Duplicate detection - one duplicate"
}

# Test 5: Core Command Validation
test_validate_core_commands() {
    echo ""
    echo "=== Test Group: Core Command Validation ==="
    
    mkdir -p .claude/commands/core
    
    # Test: Missing all core commands
    count=$(count_core_commands)
    assert_equals "0" "$count" "Core commands - none present"
    
    # Test: Some core commands present
    echo "name: /task" > .claude/commands/core/task.md
    echo "name: /help" > .claude/commands/core/help.md
    count=$(count_core_commands)
    assert_equals "2" "$count" "Core commands - partial set"
    
    # Test: All core commands present
    echo "name: /auto" > .claude/commands/core/auto.md
    echo "name: /query" > .claude/commands/core/query.md
    count=$(count_core_commands)
    assert_equals "4" "$count" "Core commands - complete set"
}

# Test 6: Score Calculation
test_calculate_score() {
    echo ""
    echo "=== Test Group: Score Calculation ==="
    
    # Test: Perfect score
    score=$(calculate_readiness_score 0 0 0 1 4)
    assert_equals "100" "$score" "Score calculation - perfect score"
    
    # Test: Score with placeholders
    score=$(calculate_readiness_score 5 0 0 1 4)
    assert_equals "90" "$score" "Score calculation - with placeholders"
    
    # Test: Score with config issues
    score=$(calculate_readiness_score 0 5 0 1 4)
    assert_equals "90" "$score" "Score calculation - with config issues"
    
    # Test: Score with duplicates
    score=$(calculate_readiness_score 0 0 2 1 4)
    assert_equals "90" "$score" "Score calculation - with duplicates"
    
    # Test: Score doesn't go below 0
    score=$(calculate_readiness_score 100 100 100 0 0)
    assert_equals "0" "$score" "Score calculation - minimum score"
}

# Test 7: Output Format Validation
test_output_format() {
    echo ""
    echo "=== Test Group: Output Format ==="
    
    # Test: Output contains required sections
    output=$(generate_validation_report 100 0 0 0 1 4 10 2>&1)
    assert_contains "$output" "READINESS SCORE" "Output format - contains score"
    assert_contains "$output" "directory structure" "Output format - contains structure check"
    assert_contains "$output" "placeholders" "Output format - contains placeholder check"
}

# Test 8: Edge Cases and Error Handling
test_edge_cases() {
    echo ""
    echo "=== Test Group: Edge Cases ==="
    
    # Test: Empty directory
    rm -rf .claude .claude-framework
    result=$(check_directory_structure 2>&1)
    assert_contains "$result" "Missing directories" "Edge case - empty directory"
    
    # Test: Malformed command files
    mkdir -p .claude/commands/core
    echo "invalid yaml" > .claude/commands/core/bad.md
    count=$(count_remaining_placeholders)
    # Should not crash, should continue counting
    assert_equals "0" "$count" "Edge case - malformed files don't crash"
    
    # Test: Very large numbers
    score=$(calculate_readiness_score 999999 0 0 1 4)
    assert_equals "0" "$score" "Edge case - very large placeholder count"
    
    # Test: Negative inputs to score calculation (become additions)
    score=$(calculate_readiness_score -5 -1 -2 1 4)
    # -5 becomes +10, -1 becomes +10, -2 becomes +10: 100 + 10 + 10 + 10 = 130
    assert_equals "130" "$score" "Edge case - negative inputs become additions"
}

# Test 9: Integration Tests
test_integration() {
    echo ""
    echo "=== Test Group: Integration Tests ==="
    
    # Test: Full validation workflow
    mkdir -p .claude/commands/core .claude/config .claude-framework
    echo "name: /task" > .claude/commands/core/task.md
    echo "name: /help" > .claude/commands/core/help.md  
    echo "name: /auto" > .claude/commands/core/auto.md
    echo "name: /query" > .claude/commands/core/query.md
    cat > .claude/config/project-config.xml << 'EOF'
<project-config>
  <name>TestProject</name>
</project-config>
EOF
    
    # Run full validation
    result=$(run_validation 2>&1)
    status=$?
    assert_equals "0" "$status" "Integration - perfect setup passes validation"
    assert_contains "$result" "100%" "Integration - perfect score displayed"
}

# Test 10: Additional Coverage Tests  
test_additional_coverage() {
    echo ""
    echo "=== Test Group: Additional Coverage ==="
    
    # Test: count_total_commands with no directory
    rm -rf .claude
    count=$(count_total_commands)
    assert_equals "0" "$count" "Additional - count commands with no directory"
    
    # Test: Multiple placeholder types in one file
    mkdir -p .claude/commands/core
    cat > .claude/commands/core/multi.md << 'EOF'
name: /multi
description: Test [INSERT_PROJECT_NAME] and [INSERT_DOMAIN] and [INSERT_TECH_STACK]  
Content with [INSERT_TEAM_SIZE] placeholder
EOF
    count=$(count_remaining_placeholders)
    assert_equals "4" "$count" "Additional - multiple placeholder types"
    
    # Test: Config with mixed content
    mkdir -p .claude/config
    cat > .claude/config/project-config.xml << 'EOF'
<project-config>
  <name>RealProject</name>
  <domain>[INSERT_DOMAIN]</domain>
</project-config>
EOF
    result=$(validate_project_config 2>&1)
    status=$?
    assert_equals "1" "$status" "Additional - mixed config validation"
    
    # Test: Score calculation edge cases
    score=$(calculate_readiness_score 0 0 0 0 0)
    assert_equals "70" "$score" "Additional - score with missing structure and core"
    
    # Test: Empty files don't break parsing
    echo "" > .claude/commands/core/empty.md
    count=$(count_remaining_placeholders)
    assert_equals "4" "$count" "Additional - empty files don't affect count"
}

# Test 11: Provide Recommendations Coverage
test_recommendations() {
    echo ""
    echo "=== Test Group: Recommendations Coverage ==="
    
    # Test all recommendation paths
    result=$(provide_recommendations 100 0 0 0 2>&1)
    assert_contains "$result" "Your adaptation is complete" "Recommendations - perfect score"
    
    result=$(provide_recommendations 95 5 0 0 2>&1) 
    assert_contains "$result" "Almost there" "Recommendations - high score"
    
    result=$(provide_recommendations 75 15 1 2 2>&1)
    assert_contains "$result" "Good progress" "Recommendations - medium score"
    
    result=$(provide_recommendations 50 50 1 5 2>&1)
    assert_contains "$result" "Significant customization needed" "Recommendations - low score"
}

# Main test execution
main() {
    echo "======================================"
    echo "TDD Tests for validate-adaptation.sh"
    echo "======================================"
    
    # Setup
    setup_test_env
    
    # Run all tests
    test_check_directory_structure
    test_count_placeholders  
    test_validate_configuration
    test_check_duplicate_commands
    test_validate_core_commands
    test_calculate_score
    test_output_format
    test_edge_cases
    test_integration
    test_additional_coverage
    test_recommendations
    
    # Cleanup
    teardown_test_env
    
    # Report results
    echo ""
    echo "======================================"
    echo "TEST RESULTS"
    echo "======================================"
    echo "Total Tests: $TEST_COUNT"
    echo -e "Passed: ${GREEN}$PASSED_COUNT${NC}"
    echo -e "Failed: ${RED}$FAILED_COUNT${NC}"
    
    coverage=$(( (PASSED_COUNT * 100) / TEST_COUNT ))
    echo "Coverage: $coverage%"
    
    if [ $coverage -ge 90 ]; then
        echo -e "${GREEN}✅ TDD Requirements Met (90%+ coverage)${NC}"
        exit 0
    else
        echo -e "${RED}❌ TDD Requirements NOT Met (<90% coverage)${NC}"
        exit 1
    fi
}

# Only run if executed directly (not sourced)
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    main "$@"
fi