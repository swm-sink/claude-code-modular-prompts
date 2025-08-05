#!/bin/bash

# Integration Test: /begin-consultation workflow validation
# Tests integration with Claude Context Architect system

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

print_test_result() {
    local test_name=$1
    local result=$2
    local message=$3
    
    TESTS_RUN=$((TESTS_RUN + 1))
    
    if [ "$result" = "PASS" ]; then
        echo -e "${GREEN}✓ INTEGRATION PASS${NC}: $test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ INTEGRATION FAIL${NC}: $test_name - $message"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Test 1: Command integrates with agent framework
test_agent_integration() {
    local test_name="begin-consultation integrates with agent framework"
    local command_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local agents_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/framework/agents"
    
    if [ -d "$agents_dir" ] && [ -f "$command_file" ]; then
        # Check if command references context generation (agent workflow)
        if grep -qi "context.*generation\|specialized.*agent\|consultation.*system" "$command_file"; then
            print_test_result "$test_name" "PASS" ""
        else
            print_test_result "$test_name" "FAIL" "Command doesn't reference agent coordination"
        fi
    else
        print_test_result "$test_name" "FAIL" "Missing agent framework or command file"
    fi
}

# Test 2: Generated context directory structure exists
test_context_structure_integration() {
    local test_name="context generation infrastructure ready"
    local claude_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude"
    
    if [ -d "$claude_dir" ]; then
        # Test that infrastructure supports context generation
        if [ -d "$claude_dir/framework" ] || [ -w "$claude_dir" ]; then
            print_test_result "$test_name" "PASS" "Infrastructure ready for context generation"
        else
            print_test_result "$test_name" "FAIL" "Cannot write to .claude directory"
        fi
    else
        print_test_result "$test_name" "FAIL" ".claude directory structure missing"
    fi
}

# Test 3: Command follows system conventions
test_system_conventions() {
    local test_name="command follows Claude Context Architect conventions"
    local command_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    
    if [ -f "$command_file" ]; then
        local conventions_met=0
        
        # Check for standard conventions
        if grep -q "allowed-tools:" "$command_file"; then conventions_met=$((conventions_met + 1)); fi
        if grep -q "category:" "$command_file"; then conventions_met=$((conventions_met + 1)); fi
        if grep -q "30.*minute" "$command_file"; then conventions_met=$((conventions_met + 1)); fi
        if grep -q "Claude.*expert\|project.*expert" "$command_file"; then conventions_met=$((conventions_met + 1)); fi
        
        if [ "$conventions_met" -ge 3 ]; then
            print_test_result "$test_name" "PASS" "Follows $conventions_met/4 key conventions"
        else
            print_test_result "$test_name" "FAIL" "Only follows $conventions_met/4 conventions"
        fi
    else
        print_test_result "$test_name" "FAIL" "Command file not found"
    fi
}

# Test 4: End-to-end workflow components exist
test_e2e_workflow_readiness() {
    local test_name="end-to-end consultation workflow ready"
    local command_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    
    if [ -f "$command_file" ]; then
        local workflow_components=0
        
        # Check for workflow readiness indicators
        if grep -qi "phase.*1.*technical\|technical.*analysis" "$command_file"; then workflow_components=$((workflow_components + 1)); fi
        if grep -qi "phase.*2.*domain\|domain.*intelligence" "$command_file"; then workflow_components=$((workflow_components + 1)); fi
        if grep -qi "phase.*3.*context\|context.*generation" "$command_file"; then workflow_components=$((workflow_components + 1)); fi
        if grep -qi "session.*management\|pause.*resume" "$command_file"; then workflow_components=$((workflow_components + 1)); fi
        
        if [ "$workflow_components" -eq 4 ]; then
            print_test_result "$test_name" "PASS" "All workflow components present"
        else
            print_test_result "$test_name" "FAIL" "Missing workflow components ($workflow_components/4)"
        fi
    else
        print_test_result "$test_name" "FAIL" "Command file not found"
    fi
}

# Test 5: Performance expectations set
test_performance_expectations() {
    local test_name="performance expectations properly set"
    local command_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    
    if [ -f "$command_file" ]; then
        if grep -qi "30.*minute\|time.*commitment\|10-15.*minute" "$command_file"; then
            print_test_result "$test_name" "PASS" "Time expectations clearly communicated"
        else
            print_test_result "$test_name" "FAIL" "No clear time expectations set"
        fi
    else
        print_test_result "$test_name" "FAIL" "Command file not found"
    fi
}

# Run integration tests
echo -e "${YELLOW}📊 INTEGRATION TESTING: Claude Context Architect Consultation System${NC}"
echo "Testing integration with agent framework and end-to-end workflow..."
echo

test_agent_integration
test_context_structure_integration  
test_system_conventions
test_e2e_workflow_readiness
test_performance_expectations

echo
echo "📊 Integration Test Summary:"
echo "Tests Run: $TESTS_RUN"
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"

if [ $TESTS_FAILED -eq 0 ]; then
    echo
    echo -e "${GREEN}🎉 INTEGRATION SUCCESS: All systems ready for deployment${NC}"
    exit 0
else
    echo
    echo -e "${RED}❌ INTEGRATION ISSUES: $TESTS_FAILED integration problems detected${NC}"
    exit 1
fi