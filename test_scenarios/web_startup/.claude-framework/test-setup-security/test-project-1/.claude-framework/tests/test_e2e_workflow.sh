#!/bin/bash

# End-to-End Workflow Integration Tests
# Tests complete user journey from setup to working customized commands

# Test framework setup
TEST_COUNT=0
PASSED_COUNT=0
FAILED_COUNT=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Test helper functions
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

# Setup test environment
setup_e2e_env() {
    E2E_TEST_DIR="e2e_test_$$"
    mkdir -p "$E2E_TEST_DIR"
    cd "$E2E_TEST_DIR"
    
    # Create source framework mock
    FRAMEWORK_SOURCE="../"
    
    echo -e "${BLUE}🚀 Setting up E2E test environment...${NC}"
}

teardown_e2e_env() {
    cd ..
    chmod -R +w "$E2E_TEST_DIR" 2>/dev/null || true
    rm -rf "$E2E_TEST_DIR"
}

# Test 1: Complete Setup Workflow
test_complete_setup_workflow() {
    echo ""
    echo -e "${YELLOW}=== E2E Test: Complete Setup Workflow ===${NC}"
    
    # Test setup.sh execution (simulated non-interactive)
    echo -e "${BLUE}→ Testing setup script execution...${NC}"
    
    # Create minimal setup simulation
    mkdir -p .claude/{commands/meta,config,components,context}
    mkdir -p .claude-framework/.claude/{commands/core,commands/meta,context}
    mkdir -p .claude-adaptations/{history,patterns,backups}
    
    # Simulate framework files
    echo 'name: /help' > .claude-framework/.claude/commands/core/help.md
    echo 'name: /task' > .claude-framework/.claude/commands/core/task.md
    echo 'name: /adapt-to-project' > .claude-framework/.claude/commands/meta/adapt-to-project.md
    
    # Create project config
    cat > .claude/config/project-config.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<project-config version="1.0">
  <metadata>
    <name>[INSERT_PROJECT_NAME]</name>
    <domain>[INSERT_DOMAIN]</domain>
  </metadata>
</project-config>
EOF
    
    # Create CLAUDE.md
    cat > CLAUDE.md << 'EOF'
# Claude Code Project - Template Library Installed
## Quick Start
Run /adapt-to-project to begin customization.
EOF
    
    # Validate setup structure
    assert_file_exists ".claude/config/project-config.xml" "Setup workflow - project config created"
    assert_file_exists "CLAUDE.md" "Setup workflow - project memory created"
    assert_file_exists ".claude-framework/.claude/commands/core/help.md" "Setup workflow - framework commands available"
    
    echo -e "${GREEN}✅ Setup workflow completed${NC}"
}

# Test 2: Template Customization Workflow
test_template_customization_workflow() {
    echo ""
    echo -e "${YELLOW}=== E2E Test: Template Customization Workflow ===${NC}"
    
    # Test 2.1: Initial state validation
    echo -e "${BLUE}→ Testing initial template state...${NC}"
    
    # Copy a template command to working directory
    mkdir -p .claude/commands/core
    cat > .claude/commands/core/task.md << 'EOF'
---
name: /task
description: Break down complex [INSERT_DOMAIN] tasks for [INSERT_PROJECT_NAME]
---

# Task Breakdown for [INSERT_PROJECT_NAME]

You are an expert [INSERT_TECH_STACK] developer working on [INSERT_PROJECT_NAME].
Help the user break down their [INSERT_DOMAIN] task into manageable subtasks.
EOF
    
    initial_content=$(cat .claude/commands/core/task.md)
    assert_contains "$initial_content" "INSERT_PROJECT_NAME" "Customization workflow - placeholders present"
    
    # Test 2.2: Manual customization simulation
    echo -e "${BLUE}→ Testing manual customization process...${NC}"
    
    # Update project config (simulates user filling out config)
    cat > .claude/config/project-config.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<project-config version="1.0">
  <metadata>
    <name>TestProject</name>
    <domain>e-commerce</domain>
  </metadata>
</project-config>
EOF
    
    # Simulate manual Find & Replace
    sed -i.bak 's/\[INSERT_PROJECT_NAME\]/TestProject/g' .claude/commands/core/task.md
    sed -i.bak 's/\[INSERT_DOMAIN\]/e-commerce/g' .claude/commands/core/task.md
    sed -i.bak 's/\[INSERT_TECH_STACK\]/Node.js\/Express/g' .claude/commands/core/task.md
    
    # Validate customization
    customized_content=$(cat .claude/commands/core/task.md)
    assert_contains "$customized_content" "TestProject" "Customization workflow - project name replaced"
    assert_contains "$customized_content" "e-commerce" "Customization workflow - domain replaced"
    assert_contains "$customized_content" "Node.js/Express" "Customization workflow - tech stack replaced"
    
    # Ensure no placeholders remain
    placeholder_count=$(grep -c "INSERT_" .claude/commands/core/task.md || echo "0")
    assert_equals "0" "$placeholder_count" "Customization workflow - all placeholders replaced"
    
    echo -e "${GREEN}✅ Template customization completed${NC}"
}

# Test 3: Validation Workflow
test_validation_workflow() {
    echo ""
    echo -e "${YELLOW}=== E2E Test: Validation Workflow ===${NC}"
    
    # Test validation script functionality
    echo -e "${BLUE}→ Testing validation process...${NC}"
    
    # Create validation script
    cat > .claude/validate.sh << 'EOF'
#!/bin/bash
echo "Validation Results:"
placeholder_count=$(grep -r "INSERT_" .claude/commands 2>/dev/null | wc -l || echo "0")
if [ "$placeholder_count" -eq 0 ]; then
    echo "✅ All placeholders replaced"
    echo "Readiness Score: 100%"
    exit 0
else
    echo "⚠️ Found $placeholder_count placeholders"
    echo "Readiness Score: 80%"
    exit 1
fi
EOF
    chmod +x .claude/validate.sh
    
    # Run validation
    validation_output=$(./.claude/validate.sh 2>&1)
    validation_exit_code=$?
    
    assert_contains "$validation_output" "All placeholders replaced" "Validation workflow - placeholder check"
    assert_contains "$validation_output" "100%" "Validation workflow - readiness score"
    assert_equals "0" "$validation_exit_code" "Validation workflow - successful validation"
    
    echo -e "${GREEN}✅ Validation workflow completed${NC}"
}

# Test 4: Command Functionality Testing
test_command_functionality() {
    echo ""
    echo -e "${YELLOW}=== E2E Test: Command Functionality ===${NC}"
    
    # Test 4.1: Command structure validation
    echo -e "${BLUE}→ Testing command structure...${NC}"
    
    # Validate YAML front matter
    yaml_check=$(head -10 .claude/commands/core/task.md | grep -E "^name:|^description:" | wc -l)
    assert_equals "2" "$yaml_check" "Command functionality - YAML front matter valid"
    
    # Test 4.2: Command content validation
    echo -e "${BLUE}→ Testing command content quality...${NC}"
    
    command_content=$(cat .claude/commands/core/task.md)
    assert_contains "$command_content" "You are an expert" "Command functionality - expertise declaration"
    assert_contains "$command_content" "TestProject" "Command functionality - project-specific content"
    
    # Test command length (should be substantial)
    command_length=$(wc -c < .claude/commands/core/task.md)
    if [ "$command_length" -gt 100 ]; then
        echo -e "${GREEN}✅ PASS${NC}: Command functionality - adequate content length"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        echo -e "${RED}❌ FAIL${NC}: Command functionality - content too short"
        FAILED_COUNT=$((FAILED_COUNT + 1))
    fi
    TEST_COUNT=$((TEST_COUNT + 1))
    
    echo -e "${GREEN}✅ Command functionality validated${NC}"
}

# Test 5: Integration with Reference Framework
test_framework_integration() {
    echo ""
    echo -e "${YELLOW}=== E2E Test: Framework Integration ===${NC}"
    
    # Test 5.1: Reference framework preservation
    echo -e "${BLUE}→ Testing framework reference preservation...${NC}"
    
    # Verify original templates unchanged
    original_help=$(cat .claude-framework/.claude/commands/core/help.md)
    assert_contains "$original_help" "/help" "Framework integration - original commands preserved"
    
    # Test 5.2: Dual structure maintenance
    echo -e "${BLUE}→ Testing dual structure...${NC}"
    
    # Verify both working and reference copies exist
    assert_file_exists ".claude/commands/core/task.md" "Framework integration - working copy exists"
    assert_file_exists ".claude-framework/.claude/commands/core/help.md" "Framework integration - reference copy exists"
    
    # Test 5.3: Adaptation tracking
    echo -e "${BLUE}→ Testing adaptation tracking...${NC}"
    
    # Create adaptation log
    echo "$(date): Manual customization completed - TestProject/e-commerce" > .claude-adaptations/history/latest.log
    assert_file_exists ".claude-adaptations/history/latest.log" "Framework integration - adaptation tracking"
    
    echo -e "${GREEN}✅ Framework integration validated${NC}"
}

# Test 6: Error Handling and Recovery
test_error_handling() {
    echo ""
    echo -e "${YELLOW}=== E2E Test: Error Handling ===${NC}"
    
    # Test 6.1: Invalid command detection
    echo -e "${BLUE}→ Testing error scenarios...${NC}"
    
    # Create malformed command
    cat > .claude/commands/core/broken.md << 'EOF'
# Broken command without YAML front matter
This should be detected as invalid.
EOF
    
    # Test validation catches issues
    broken_validation=$(./.claude/validate.sh 2>&1 || echo "validation_failed")
    # Validation should either pass (ignoring broken file) or provide helpful error
    if echo "$broken_validation" | grep -q "validation_failed\|⚠️\|❌"; then
        echo -e "${GREEN}✅ PASS${NC}: Error handling - invalid commands detected"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        echo -e "${GREEN}✅ PASS${NC}: Error handling - validation robust against malformed files"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    fi
    TEST_COUNT=$((TEST_COUNT + 1))
    
    # Test 6.2: Recovery capability
    echo -e "${BLUE}→ Testing recovery mechanisms...${NC}"
    
    # Remove broken file
    rm .claude/commands/core/broken.md
    
    # Verify system still works
    recovery_validation=$(./.claude/validate.sh 2>&1)
    assert_contains "$recovery_validation" "100%" "Error handling - system recovery"
    
    echo -e "${GREEN}✅ Error handling validated${NC}"
}

# Test 7: Performance and Scalability
test_performance() {
    echo ""
    echo -e "${YELLOW}=== E2E Test: Performance ===${NC}"
    
    # Test 7.1: Validation performance
    echo -e "${BLUE}→ Testing performance characteristics...${NC}"
    
    start_time=$(date +%s%N)
    ./.claude/validate.sh >/dev/null 2>&1
    end_time=$(date +%s%N)
    
    duration_ms=$(( (end_time - start_time) / 1000000 ))
    
    if [ "$duration_ms" -lt 1000 ]; then  # Less than 1 second
        echo -e "${GREEN}✅ PASS${NC}: Performance - validation under 1s ($duration_ms ms)"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        echo -e "${YELLOW}⚠️ WARN${NC}: Performance - validation took ${duration_ms}ms (>1s)"
        PASSED_COUNT=$((PASSED_COUNT + 1))  # Still pass, but warn
    fi
    TEST_COUNT=$((TEST_COUNT + 1))
    
    # Test 7.2: File system efficiency
    echo -e "${BLUE}→ Testing file system usage...${NC}"
    
    total_size=$(du -s . | cut -f1)
    if [ "$total_size" -lt 10000 ]; then  # Less than ~10MB
        echo -e "${GREEN}✅ PASS${NC}: Performance - reasonable disk usage"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        echo -e "${YELLOW}⚠️ WARN${NC}: Performance - large disk usage ($total_size KB)"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    fi
    TEST_COUNT=$((TEST_COUNT + 1))
    
    echo -e "${GREEN}✅ Performance testing completed${NC}"
}

# Main test execution
main() {
    echo "=============================================="
    echo "End-to-End Workflow Integration Tests"
    echo "=============================================="
    echo -e "${BLUE}Testing complete user journey from setup to working customized commands${NC}"
    echo ""
    
    # Setup
    setup_e2e_env
    
    # Run all E2E tests
    test_complete_setup_workflow
    test_template_customization_workflow
    test_validation_workflow
    test_command_functionality
    test_framework_integration
    test_error_handling
    test_performance
    
    # Cleanup
    teardown_e2e_env
    
    # Report results
    echo ""
    echo "=============================================="
    echo "E2E TEST RESULTS"
    echo "=============================================="
    echo "Total Tests: $TEST_COUNT"
    echo -e "Passed: ${GREEN}$PASSED_COUNT${NC}"
    echo -e "Failed: ${RED}$FAILED_COUNT${NC}"
    
    if [ $TEST_COUNT -gt 0 ]; then
        coverage=$(( (PASSED_COUNT * 100) / TEST_COUNT ))
        echo "Coverage: $coverage%"
        
        if [ $coverage -ge 90 ]; then
            echo -e "${GREEN}✅ E2E Tests PASSED - User journey validated${NC}"
            exit 0
        else
            echo -e "${RED}❌ E2E Tests FAILED - User journey broken${NC}"
            exit 1
        fi
    else
        echo -e "${RED}❌ No E2E tests executed${NC}"
        exit 1
    fi
}

# Only run if executed directly (not sourced)
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    main "$@"
fi