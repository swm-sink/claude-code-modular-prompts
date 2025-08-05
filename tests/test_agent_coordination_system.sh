#!/bin/bash

# Test: Agent Coordination System for Interactive Consultation
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

# Test 1: Agent Coordinator command exists (SHOULD FAIL INITIALLY)
test_agent_coordinator_exists() {
    local test_name="agent coordinator command exists"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    if [ -f "$coordinator_file" ]; then
        print_test_result "$test_name" "PASS" ""
    else
        print_test_result "$test_name" "FAIL" "Agent coordinator not found at $coordinator_file"
    fi
}

# Test 2: Specialized agents can be referenced/called (SHOULD FAIL INITIALLY)
test_agent_specialization_system() {
    local test_name="agent specialization system operational"
    local agents_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/framework/agents"
    local required_agents=("context-engineer.md" "command-builder.md" "research-validator.md")
    local found_agents=0
    
    if [ -d "$agents_dir" ]; then
        for agent in "${required_agents[@]}"; do
            if [ -f "$agents_dir/$agent" ]; then
                found_agents=$((found_agents + 1))
            fi
        done
        
        if [ "$found_agents" -eq 3 ]; then
            print_test_result "$test_name" "PASS" "All 3 specialized agents found"
        else
            print_test_result "$test_name" "FAIL" "Only $found_agents/3 specialized agents found"
        fi
    else
        print_test_result "$test_name" "FAIL" "Agents directory not found"
    fi
}

# Test 3: Phase coordination workflow exists (SHOULD FAIL INITIALLY)
test_phase_coordination_workflow() {
    local test_name="3-phase consultation coordination workflow"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    if [ ! -f "$coordinator_file" ]; then
        print_test_result "$test_name" "FAIL" "Coordinator file does not exist"
        return
    fi
    
    local phase_patterns=0
    # Check for phase coordination patterns
    if grep -qi "phase.*1.*technical\|technical.*analysis" "$coordinator_file"; then phase_patterns=$((phase_patterns + 1)); fi
    if grep -qi "phase.*2.*domain\|domain.*intelligence" "$coordinator_file"; then phase_patterns=$((phase_patterns + 1)); fi
    if grep -qi "phase.*3.*context\|context.*generation" "$coordinator_file"; then phase_patterns=$((phase_patterns + 1)); fi
    
    if [ "$phase_patterns" -eq 3 ]; then
        print_test_result "$test_name" "PASS" "All 3 consultation phases referenced"
    else
        print_test_result "$test_name" "FAIL" "Only $phase_patterns/3 consultation phases found"
    fi
}

# Test 4: Agent handoff protocols defined (SHOULD FAIL INITIALLY)
test_agent_handoff_protocols() {
    local test_name="agent handoff protocols defined"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    if [ ! -f "$coordinator_file" ]; then
        print_test_result "$test_name" "FAIL" "Coordinator file does not exist"
        return
    fi
    
    local handoff_indicators=0
    # Check for handoff coordination indicators
    if grep -qi "context-engineer\|Context Engineer" "$coordinator_file"; then handoff_indicators=$((handoff_indicators + 1)); fi
    if grep -qi "command-builder\|Command Builder" "$coordinator_file"; then handoff_indicators=$((handoff_indicators + 1)); fi
    if grep -qi "research-validator\|Research Validator" "$coordinator_file"; then handoff_indicators=$((handoff_indicators + 1)); fi
    if grep -qi "coordination\|handoff\|delegate" "$coordinator_file"; then handoff_indicators=$((handoff_indicators + 1)); fi
    
    if [ "$handoff_indicators" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "Agent handoff protocols present"
    else
        print_test_result "$test_name" "FAIL" "Insufficient handoff coordination ($handoff_indicators/4 indicators)"
    fi
}

# Test 5: Session state management architecture (SHOULD FAIL INITIALLY)
test_session_state_management() {
    local test_name="session state management architecture"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    local state_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/consultation-state.json"
    
    # Check if coordinator references session management
    local session_refs=0
    if [ -f "$coordinator_file" ]; then
        if grep -qi "session.*state\|consultation.*state\|pause.*resume" "$coordinator_file"; then 
            session_refs=$((session_refs + 1)); 
        fi
        if grep -qi "progress.*tracking\|phase.*progress\|current.*phase" "$coordinator_file"; then 
            session_refs=$((session_refs + 1)); 
        fi
    fi
    
    if [ "$session_refs" -ge 1 ]; then
        print_test_result "$test_name" "PASS" "Session state management referenced"
    else
        print_test_result "$test_name" "FAIL" "No session state management architecture found"
    fi
}

# Test 6: Interactive user prompts system (SHOULD FAIL INITIALLY)
test_interactive_prompts_system() {
    local test_name="interactive user prompts system"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    if [ ! -f "$coordinator_file" ]; then
        print_test_result "$test_name" "FAIL" "Coordinator file does not exist"
        return
    fi
    
    local interaction_patterns=0
    # Check for user interaction indicators
    if grep -qi "ask.*user\|user.*input\|interactive" "$coordinator_file"; then interaction_patterns=$((interaction_patterns + 1)); fi
    if grep -qi "question\|prompt\|response" "$coordinator_file"; then interaction_patterns=$((interaction_patterns + 1)); fi
    if grep -qi "approval\|confirm\|review" "$coordinator_file"; then interaction_patterns=$((interaction_patterns + 1)); fi
    
    if [ "$interaction_patterns" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Interactive prompts system present"
    else
        print_test_result "$test_name" "FAIL" "Insufficient interactive patterns ($interaction_patterns/3 found)"
    fi
}

# Test 7: Integration with begin-consultation command (SHOULD FAIL INITIALLY)
test_integration_with_consultation() {
    local test_name="integration with begin-consultation command"
    local consultation_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    if [ ! -f "$consultation_file" ]; then
        print_test_result "$test_name" "FAIL" "begin-consultation command not found"
        return
    fi
    
    if [ ! -f "$coordinator_file" ]; then
        print_test_result "$test_name" "FAIL" "Agent coordinator not found"
        return
    fi
    
    # Check if begin-consultation references agent coordination
    if grep -qi "agent\|coordinate\|specialist" "$consultation_file"; then
        print_test_result "$test_name" "PASS" "Integration references present"
    else
        print_test_result "$test_name" "FAIL" "No integration between consultation and agent coordination"
    fi
}

# Run all tests
echo "🔴 RED PHASE: Running failing tests for Agent Coordination System..."
echo "Expected: Most tests should FAIL initially (TDD Red phase)"
echo

test_agent_coordinator_exists
test_agent_specialization_system
test_phase_coordination_workflow
test_agent_handoff_protocols
test_session_state_management
test_interactive_prompts_system
test_integration_with_consultation

echo
echo "📊 Test Summary:"
echo "Tests Run: $TESTS_RUN"
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"

if [ $TESTS_FAILED -gt 4 ]; then
    echo
    echo "🔴 RED PHASE SUCCESS: Most tests failing as expected (TDD requirement)"
    echo "Next: Implement minimal agent coordination to make these tests pass (GREEN phase)"
    exit 0  # Expected failure in RED phase
else
    echo
    echo "⚠️  UNEXPECTED: Too few test failures in RED phase ($TESTS_FAILED)"
    echo "TDD requires most tests to fail before implementation"
    exit 1
fi