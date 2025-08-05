#!/bin/bash

# Test: Session State Persistence System
# Following TDD Red-Green-Refactor cycle

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Test result tracking
print_test_result() {
    local test_name=$1
    local result=$2
    local message=$3
    
    TESTS_RUN=$((TESTS_RUN + 1))
    
    if [ "$result" = "PASS" ]; then
        echo -e "${GREEN}✓ PASS${NC}: $test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗ FAIL${NC}: $test_name - $message"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Cleanup function for test isolation
cleanup_test_state() {
    local state_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/consultation-state.json"
    if [ -f "$state_file" ]; then
        rm "$state_file"
    fi
}

# Test 1: Session state management command exists (SHOULD FAIL INITIALLY)
test_session_state_command_exists() {
    local test_name="session state management command exists"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ -f "$state_command" ]; then
        print_test_result "$test_name" "PASS" ""
    else
        print_test_result "$test_name" "FAIL" "Session state command not found at $state_command"
    fi
}

# Test 2: JSON state file creation (SHOULD FAIL INITIALLY)
test_json_state_file_creation() {
    local test_name="JSON state file creation capability"
    local state_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/consultation-state.json"
    local claude_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude"
    
    cleanup_test_state
    
    # Test that we can create the state file (directory exists and is writable)
    if [ -d "$claude_dir" ] && [ -w "$claude_dir" ]; then
        # Try to create a test state file
        echo '{"test": true}' > "$state_file" 2>/dev/null
        if [ -f "$state_file" ]; then
            print_test_result "$test_name" "PASS" "Can create state file"
            cleanup_test_state
        else
            print_test_result "$test_name" "FAIL" "Cannot create state file in .claude directory"
        fi
    else
        print_test_result "$test_name" "FAIL" ".claude directory not writable or doesn't exist"
    fi
}

# Test 3: State file structure validation (SHOULD FAIL INITIALLY)
test_state_file_structure() {
    local test_name="consultation state file structure validation"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command doesn't exist"
        return
    fi
    
    # Check if command mentions required state structure components
    local structure_components=0
    if grep -qi "consultation.*metadata\|session.*id\|created.*at" "$state_command"; then 
        structure_components=$((structure_components + 1)); 
    fi
    if grep -qi "phase.*management\|current.*phase\|completed.*phases" "$state_command"; then 
        structure_components=$((structure_components + 1)); 
    fi
    if grep -qi "user.*interaction\|user.*responses\|pending.*approvals" "$state_command"; then 
        structure_components=$((structure_components + 1)); 
    fi
    if grep -qi "agent.*coordination\|active.*agents\|agent.*outputs" "$state_command"; then 
        structure_components=$((structure_components + 1)); 
    fi
    
    if [ "$structure_components" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "State structure components present"
    else
        print_test_result "$test_name" "FAIL" "Missing state structure components ($structure_components/4)"
    fi
}

# Test 4: Save consultation state functionality (SHOULD FAIL INITIALLY)
test_save_consultation_state() {
    local test_name="save consultation state functionality"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command doesn't exist"
        return
    fi
    
    # Check if command mentions save/write functionality
    if grep -qi "save.*state\|write.*state\|persist.*state\|create.*state" "$state_command"; then
        print_test_result "$test_name" "PASS" "Save state functionality mentioned"
    else
        print_test_result "$test_name" "FAIL" "No save state functionality found"
    fi
}

# Test 5: Load consultation state functionality (SHOULD FAIL INITIALLY)
test_load_consultation_state() {
    local test_name="load consultation state functionality"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command doesn't exist"
        return
    fi
    
    # Check if command mentions load/read functionality
    if grep -qi "load.*state\|read.*state\|restore.*state\|resume.*state" "$state_command"; then
        print_test_result "$test_name" "PASS" "Load state functionality mentioned"
    else
        print_test_result "$test_name" "FAIL" "No load state functionality found"
    fi
}

# Test 6: Phase progress tracking (SHOULD FAIL INITIALLY)
test_phase_progress_tracking() {
    local test_name="phase progress tracking functionality"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command doesn't exist"
        return
    fi
    
    # Check for phase tracking indicators
    local tracking_features=0
    if grep -qi "phase.*progress\|progress.*tracking\|completion.*percentage" "$state_command"; then 
        tracking_features=$((tracking_features + 1)); 
    fi
    if grep -qi "current.*phase\|active.*phase\|phase.*status" "$state_command"; then 
        tracking_features=$((tracking_features + 1)); 
    fi
    if grep -qi "completed.*phases\|finished.*phases\|phase.*history" "$state_command"; then 
        tracking_features=$((tracking_features + 1)); 
    fi
    
    if [ "$tracking_features" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Phase tracking functionality present"
    else
        print_test_result "$test_name" "FAIL" "Insufficient phase tracking features ($tracking_features/3)"
    fi
}

# Test 7: Pause/resume functionality (SHOULD FAIL INITIALLY)
test_pause_resume_functionality() {
    local test_name="pause/resume consultation functionality"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command doesn't exist"
        return
    fi
    
    # Check for pause/resume functionality
    local pause_resume_features=0
    if grep -qi "pause.*consultation\|pause.*session\|suspend.*session" "$state_command"; then 
        pause_resume_features=$((pause_resume_features + 1)); 
    fi
    if grep -qi "resume.*consultation\|resume.*session\|continue.*session" "$state_command"; then 
        pause_resume_features=$((pause_resume_features + 1)); 
    fi
    if grep -qi "pause.*point\|checkpoint\|save.*point" "$state_command"; then 
        pause_resume_features=$((pause_resume_features + 1)); 
    fi
    
    if [ "$pause_resume_features" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Pause/resume functionality present"
    else
        print_test_result "$test_name" "FAIL" "Insufficient pause/resume features ($pause_resume_features/3)"
    fi
}

# Test 8: Integration with consultation workflow (SHOULD FAIL INITIALLY)
test_consultation_workflow_integration() {
    local test_name="integration with consultation workflow"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    local consultation_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command doesn't exist"
        return
    fi
    
    if [ ! -f "$consultation_command" ]; then
        print_test_result "$test_name" "FAIL" "Begin consultation command doesn't exist"
        return
    fi
    
    # Check if consultation command references state management
    if grep -qi "session.*state\|manage.*session\|state.*persistence" "$consultation_command"; then
        # Check if state command references consultation workflow
        if grep -qi "consultation.*workflow\|begin.*consultation\|consultation.*process" "$state_command"; then
            print_test_result "$test_name" "PASS" "Integration references present"
        else
            print_test_result "$test_name" "FAIL" "State command doesn't reference consultation workflow"
        fi
    else
        print_test_result "$test_name" "FAIL" "Consultation command doesn't reference state management"
    fi
}

# Test 9: Error handling and validation (SHOULD FAIL INITIALLY)
test_error_handling_validation() {
    local test_name="error handling and validation system"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command doesn't exist"
        return
    fi
    
    # Check for error handling features
    local error_handling=0
    if grep -qi "error.*handling\|validation\|corrupted.*state" "$state_command"; then 
        error_handling=$((error_handling + 1)); 
    fi
    if grep -qi "backup\|recovery\|rollback\|restore" "$state_command"; then 
        error_handling=$((error_handling + 1)); 
    fi
    if grep -qi "permission.*error\|file.*error\|json.*error" "$state_command"; then 
        error_handling=$((error_handling + 1)); 
    fi
    
    if [ "$error_handling" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Error handling system present"
    else
        print_test_result "$test_name" "FAIL" "Insufficient error handling ($error_handling/3 features)"
    fi
}

# Run all tests
echo "🔴 RED PHASE: Running failing tests for Session State Persistence System..."
echo "Expected: Most tests should FAIL initially (TDD Red phase)"
echo

test_session_state_command_exists
test_json_state_file_creation
test_state_file_structure
test_save_consultation_state
test_load_consultation_state
test_phase_progress_tracking
test_pause_resume_functionality
test_consultation_workflow_integration
test_error_handling_validation

echo
echo "📊 Test Summary:"
echo "Tests Run: $TESTS_RUN"
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"

if [ $TESTS_FAILED -gt 6 ]; then
    echo
    echo "🔴 RED PHASE SUCCESS: Most tests failing as expected (TDD requirement)"
    echo "Next: Implement minimal session state system to make these tests pass (GREEN phase)"
    exit 0  # Expected failure in RED phase
else
    echo
    echo "⚠️  UNEXPECTED: Too few test failures in RED phase ($TESTS_FAILED)"
    echo "TDD requires most tests to fail before implementation"
    exit 1
fi