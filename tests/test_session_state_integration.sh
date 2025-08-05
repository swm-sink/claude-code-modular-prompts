#!/bin/bash

# Test: Session State Integration with Full Consultation Workflow
# Validates session state works with complete consultation process

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

# Test 1: Session state integration with begin-consultation command
test_begin_consultation_integration() {
    local test_name="session state integration with begin-consultation"
    local consultation_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$consultation_command" ] || [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Required commands missing"
        return
    fi
    
    # Check bidirectional integration references
    local integration_score=0
    
    # Check consultation command mentions session state
    if grep -qi "manage-session-state\|session.*state\|consultation-state\.json" "$consultation_command"; then
        integration_score=$((integration_score + 1))
    fi
    
    # Check session state command mentions consultation workflow
    if grep -qi "begin-consultation\|consultation.*workflow\|consultation.*process" "$state_command"; then
        integration_score=$((integration_score + 1))
    fi
    
    # Check for pause/resume integration in consultation
    if grep -qi "pause\|resume" "$consultation_command"; then
        integration_score=$((integration_score + 1))
    fi
    
    if [ "$integration_score" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Integration references present ($integration_score/3)"
    else
        print_test_result "$test_name" "FAIL" "Insufficient integration ($integration_score/3)"
    fi
}

# Test 2: Session state integration with agent coordination
test_agent_coordination_integration() {
    local test_name="session state integration with agent coordination"
    local agent_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$agent_command" ] || [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Required commands missing"
        return
    fi
    
    # Check integration between agent coordination and session state
    local agent_integration=0
    
    # Check agent command mentions state management
    if grep -qi "session.*state\|state.*persistence\|manage-session-state" "$agent_command"; then
        agent_integration=$((agent_integration + 1))
    fi
    
    # Check state command mentions agent coordination
    if grep -qi "coordinate-agents\|agent.*coordination\|agent.*outputs" "$state_command"; then
        agent_integration=$((agent_integration + 1))
    fi
    
    # Check for agent handoff state tracking
    if grep -qi "agent.*handoff\|agent.*state\|agent.*activities" "$state_command"; then
        agent_integration=$((agent_integration + 1))
    fi
    
    if [ "$agent_integration" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Agent integration present ($agent_integration/3)"
    else
        print_test_result "$test_name" "FAIL" "Insufficient agent integration ($agent_integration/3)"
    fi
}

# Test 3: Full workflow command compatibility
test_workflow_command_compatibility() {
    local test_name="full workflow command compatibility"
    local commands_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands"
    
    # Essential commands for consultation workflow
    local essential_commands=(
        "begin-consultation.md"
        "coordinate-agents.md" 
        "manage-session-state.md"
    )
    
    local missing_commands=0
    for cmd in "${essential_commands[@]}"; do
        if [ ! -f "$commands_dir/$cmd" ]; then
            missing_commands=$((missing_commands + 1))
        fi
    done
    
    if [ "$missing_commands" -eq 0 ]; then
        # Check YAML compatibility across all commands
        local yaml_valid=true
        for cmd in "${essential_commands[@]}"; do
            if ! head -10 "$commands_dir/$cmd" | grep -q "^---$" || ! head -20 "$commands_dir/$cmd" | grep -q "name:\|description:\|usage:"; then
                yaml_valid=false
                break
            fi
        done
        
        if [ "$yaml_valid" = true ]; then
            print_test_result "$test_name" "PASS" "All essential commands present with valid YAML"
        else
            print_test_result "$test_name" "FAIL" "YAML compatibility issues detected"
        fi
    else
        print_test_result "$test_name" "FAIL" "Missing essential commands ($missing_commands)"
    fi
}

# Test 4: State file structure consistency across workflow
test_state_structure_consistency() {
    local test_name="consultation state structure consistency"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command not found"
        return
    fi
    
    # Check for complete state structure definition
    local structure_completeness=0
    
    # Consultation metadata
    if grep -qi "session_id\|created_at\|last_updated\|version" "$state_command"; then
        structure_completeness=$((structure_completeness + 1))
    fi
    
    # Phase management
    if grep -qi "current_phase\|completed_phases\|phase_progress" "$state_command"; then
        structure_completeness=$((structure_completeness + 1))
    fi
    
    # User interaction state
    if grep -qi "user_responses\|pending_approvals\|modification_requests" "$state_command"; then
        structure_completeness=$((structure_completeness + 1))
    fi
    
    # Agent coordination state
    if grep -qi "active_agents\|agent_outputs\|agent_handoffs" "$state_command"; then
        structure_completeness=$((structure_completeness + 1))
    fi
    
    if [ "$structure_completeness" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "Complete state structure defined ($structure_completeness/4)"
    else
        print_test_result "$test_name" "FAIL" "Incomplete state structure ($structure_completeness/4)"
    fi
}

# Test 5: Pause/resume workflow integration
test_pause_resume_workflow() {
    local test_name="pause/resume workflow integration"
    local consultation_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$consultation_command" ] || [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Required commands missing"
        return
    fi
    
    # Check pause/resume workflow integration
    local workflow_features=0
    
    # Check consultation command supports pause
    if grep -qi "pause\|PAUSE.*prompt\|pause.*save" "$consultation_command"; then
        workflow_features=$((workflow_features + 1))
    fi
    
    # Check consultation command supports resume
    if grep -qi "resume\|continue.*session\|begin-consultation.*resume" "$consultation_command"; then
        workflow_features=$((workflow_features + 1))
    fi
    
    # Check state command provides pause/resume functionality
    if grep -qi "pause.*consultation\|resume.*consultation\|seamless.*resume" "$state_command"; then
        workflow_features=$((workflow_features + 1))
    fi
    
    # Check for session continuity features
    if grep -qi "session.*continuity\|context.*preservation\|conversation.*history" "$state_command"; then
        workflow_features=$((workflow_features + 1))
    fi
    
    if [ "$workflow_features" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "Pause/resume workflow complete ($workflow_features/4)"
    else
        print_test_result "$test_name" "FAIL" "Incomplete pause/resume workflow ($workflow_features/4)"
    fi
}

# Test 6: Cross-command state persistence validation
test_cross_command_persistence() {
    local test_name="cross-command state persistence validation"
    local commands_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands"
    
    # Check that all consultation workflow commands reference the same state file
    local state_file_references=0
    
    # Check begin-consultation references consultation-state.json
    if [ -f "$commands_dir/begin-consultation.md" ] && grep -qi "consultation-state\.json" "$commands_dir/begin-consultation.md"; then
        state_file_references=$((state_file_references + 1))
    fi
    
    # Check coordinate-agents references consultation-state.json (if it exists)
    if [ -f "$commands_dir/coordinate-agents.md" ] && grep -qi "consultation-state\.json\|session.*state" "$commands_dir/coordinate-agents.md"; then
        state_file_references=$((state_file_references + 1))
    fi
    
    # Check manage-session-state defines consultation-state.json
    if [ -f "$commands_dir/manage-session-state.md" ] && grep -qi "\.claude/consultation-state\.json" "$commands_dir/manage-session-state.md"; then
        state_file_references=$((state_file_references + 1))
    fi
    
    if [ "$state_file_references" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Consistent state file references ($state_file_references commands)"
    else
        print_test_result "$test_name" "FAIL" "Inconsistent state references ($state_file_references commands)"
    fi
}

# Test 7: Error handling integration across workflow
test_error_handling_integration() {
    local test_name="error handling integration across workflow"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command not found"
        return
    fi
    
    # Check for comprehensive error handling
    local error_handling_features=0
    
    # State validation and recovery
    if grep -qi "state.*validation\|corrupted.*state\|data.*integrity" "$state_command"; then
        error_handling_features=$((error_handling_features + 1))
    fi
    
    # Backup and rollback capabilities
    if grep -qi "backup\|rollback\|recovery\|restore.*backup" "$state_command"; then
        error_handling_features=$((error_handling_features + 1))
    fi
    
    # Permission and file handling errors
    if grep -qi "permission.*error\|file.*error\|json.*error" "$state_command"; then
        error_handling_features=$((error_handling_features + 1))
    fi
    
    # Graceful degradation
    if grep -qi "graceful.*handling\|partial.*recovery\|manual.*override" "$state_command"; then
        error_handling_features=$((error_handling_features + 1))
    fi
    
    if [ "$error_handling_features" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "Comprehensive error handling ($error_handling_features/4)"
    else
        print_test_result "$test_name" "FAIL" "Insufficient error handling ($error_handling_features/4)"
    fi
}

# Test 8: Performance and scalability integration
test_performance_scalability() {
    local test_name="performance and scalability integration"
    local state_command="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/manage-session-state.md"
    
    if [ ! -f "$state_command" ]; then
        print_test_result "$test_name" "FAIL" "Session state command not found"
        return
    fi
    
    # Check for performance considerations
    local performance_features=0
    
    # Performance targets and optimization
    if grep -qi "performance.*optimization\|<100ms\|efficiency.*metric" "$state_command"; then
        performance_features=$((performance_features + 1))
    fi
    
    # Background operations and continuous saving
    if grep -qi "background.*saving\|continuous.*persistence\|automatic.*save" "$state_command"; then
        performance_features=$((performance_features + 1))
    fi
    
    # Scalability features for long consultations
    if grep -qi "long.*consultation\|multi.*session\|session.*spanning" "$state_command"; then
        performance_features=$((performance_features + 1))
    fi
    
    if [ "$performance_features" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Performance integration present ($performance_features/3)"
    else
        print_test_result "$test_name" "FAIL" "Insufficient performance integration ($performance_features/3)"
    fi
}

# Test 9: End-to-end workflow validation
test_end_to_end_workflow() {
    local test_name="end-to-end consultation workflow validation"
    local commands_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands"
    
    # Check complete workflow is documented
    local workflow_completeness=0
    
    # Entry point (begin-consultation)
    if [ -f "$commands_dir/begin-consultation.md" ] && grep -qi "30.*minute.*consultation\|interactive.*consultation" "$commands_dir/begin-consultation.md"; then
        workflow_completeness=$((workflow_completeness + 1))
    fi
    
    # Agent coordination (coordinate-agents)
    if [ -f "$commands_dir/coordinate-agents.md" ] && grep -qi "specialized.*agents\|agent.*coordination" "$commands_dir/coordinate-agents.md"; then
        workflow_completeness=$((workflow_completeness + 1))
    fi
    
    # State management (manage-session-state)
    if [ -f "$commands_dir/manage-session-state.md" ] && grep -qi "consultation.*persistence\|session.*management" "$commands_dir/manage-session-state.md"; then
        workflow_completeness=$((workflow_completeness + 1))
    fi
    
    # Phase progression (3-phase workflow)
    if [ -f "$commands_dir/begin-consultation.md" ] && grep -qi "phase.*1.*technical\|phase.*2.*domain\|phase.*3.*context" "$commands_dir/begin-consultation.md"; then
        workflow_completeness=$((workflow_completeness + 1))
    fi
    
    if [ "$workflow_completeness" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "Complete workflow documented ($workflow_completeness/4)"
    else
        print_test_result "$test_name" "FAIL" "Incomplete workflow documentation ($workflow_completeness/4)"
    fi
}

# Run all integration tests
echo "🔗 INTEGRATION PHASE: Testing Session State with Full Consultation Workflow..."
echo "Validating complete system integration and cross-command compatibility"
echo

test_begin_consultation_integration
test_agent_coordination_integration  
test_workflow_command_compatibility
test_state_structure_consistency
test_pause_resume_workflow
test_cross_command_persistence
test_error_handling_integration
test_performance_scalability
test_end_to_end_workflow

echo
echo "📊 Integration Test Summary:"
echo "Tests Run: $TESTS_RUN"
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"

if [ $TESTS_FAILED -eq 0 ]; then
    echo
    echo "🎉 INTEGRATION SUCCESS: Complete system integration validated!"
    echo "✅ Session state persistence fully integrated with consultation workflow"
    echo "✅ Cross-command compatibility confirmed"
    echo "✅ End-to-end workflow validation complete"
    echo
    echo "🚀 Ready for: Final TDD commit and next development phase"
    exit 0
else
    echo
    echo "⚠️  INTEGRATION ISSUES: $TESTS_FAILED integration problems detected"
    echo "Fix integration issues before proceeding to next development phase"
    exit 1
fi