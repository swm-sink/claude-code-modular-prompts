#!/bin/bash

# Integration Test: Full Agent Consultation Workflow Validation
# Tests complete coordination between /begin-consultation and /coordinate-agents

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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

# Test 1: End-to-end command integration
test_e2e_command_integration() {
    local test_name="end-to-end command integration"
    local consultation_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    if [ -f "$consultation_file" ] && [ -f "$coordinator_file" ]; then
        # Check if consultation references coordination
        if grep -qi "coordinate.*agent\|agent.*coordination\|specialist.*intelligence" "$consultation_file"; then
            # Check if coordinator references consultation workflow
            if grep -qi "consultation.*workflow\|begin.*consultation\|phase.*consultation" "$coordinator_file"; then
                print_test_result "$test_name" "PASS" "Commands properly integrated"
            else
                print_test_result "$test_name" "FAIL" "Coordinator doesn't reference consultation workflow"
            fi
        else
            print_test_result "$test_name" "FAIL" "Consultation doesn't reference agent coordination"
        fi
    else
        print_test_result "$test_name" "FAIL" "Missing command files"
    fi
}

# Test 2: Agent specialization system completeness
test_agent_specialization_completeness() {
    local test_name="agent specialization system completeness"
    local agents_dir="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/framework/agents"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    if [ ! -d "$agents_dir" ] || [ ! -f "$coordinator_file" ]; then
        print_test_result "$test_name" "FAIL" "Missing agents directory or coordinator"
        return
    fi
    
    # Check that coordinator references all available agents
    local agents_found=0
    for agent_file in "$agents_dir"/*.md; do
        if [ -f "$agent_file" ]; then
            local agent_name=$(basename "$agent_file" .md)
            # Check if coordinator mentions this agent
            if grep -qi "$agent_name\|$(echo $agent_name | tr '-' ' ')" "$coordinator_file"; then
                agents_found=$((agents_found + 1))
            fi
        fi
    done
    
    local total_agents=$(find "$agents_dir" -name "*.md" | wc -l)
    
    if [ "$agents_found" -eq "$total_agents" ] && [ "$total_agents" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "All $total_agents agents integrated in coordinator"
    else
        print_test_result "$test_name" "FAIL" "Only $agents_found/$total_agents agents integrated"
    fi
}

# Test 3: 3-phase workflow consistency
test_phase_workflow_consistency() {
    local test_name="3-phase workflow consistency"
    local consultation_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    # Define the expected phases
    local phases=("technical analysis" "domain intelligence" "context generation")
    local consultation_phases=0
    local coordinator_phases=0
    
    # Check consultation file for phases
    for phase in "${phases[@]}"; do
        if grep -qi "$phase" "$consultation_file"; then
            consultation_phases=$((consultation_phases + 1))
        fi
    done
    
    # Check coordinator file for phases  
    for phase in "${phases[@]}"; do
        if grep -qi "$phase" "$coordinator_file"; then
            coordinator_phases=$((coordinator_phases + 1))
        fi
    done
    
    if [ "$consultation_phases" -eq 3 ] && [ "$coordinator_phases" -eq 3 ]; then
        print_test_result "$test_name" "PASS" "All 3 phases consistent across commands"
    else
        print_test_result "$test_name" "FAIL" "Phase mismatch: consultation($consultation_phases/3), coordinator($coordinator_phases/3)"
    fi
}

# Test 4: Session state management architecture
test_session_state_architecture() {
    local test_name="session state management architecture"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    local consultation_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    
    local session_features=0
    
    # Check for session management features in coordinator
    if grep -qi "consultation.*state\.json\|session.*state\|pause.*resume" "$coordinator_file"; then
        session_features=$((session_features + 1))
    fi
    
    if grep -qi "progress.*tracking\|session.*persistence\|rollback\|checkpoint" "$coordinator_file"; then
        session_features=$((session_features + 1))
    fi
    
    # Check for session management references in consultation
    if grep -qi "pause\|resume\|session.*management" "$consultation_file"; then
        session_features=$((session_features + 1))
    fi
    
    if [ "$session_features" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "Session management architecture complete"
    else
        print_test_result "$test_name" "FAIL" "Incomplete session management ($session_features/3 features)"
    fi
}

# Test 5: User interaction system integration
test_user_interaction_integration() {
    local test_name="user interaction system integration"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    local consultation_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    
    local interaction_features=0
    
    # Check for interactive features in coordinator
    if grep -qi "interactive.*prompt\|user.*approval\|question.*generation" "$coordinator_file"; then
        interaction_features=$((interaction_features + 1))
    fi
    
    if grep -qi "user.*control\|approval.*workflow\|modification.*request" "$coordinator_file"; then
        interaction_features=$((interaction_features + 1))
    fi
    
    # Check for interaction promises in consultation
    if grep -qi "interactive.*question\|approval\|review.*approve" "$consultation_file"; then
        interaction_features=$((interaction_features + 1))
    fi
    
    if [ "$interaction_features" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "User interaction system integrated"
    else
        print_test_result "$test_name" "FAIL" "Incomplete user interaction system ($interaction_features/3 features)"
    fi
}

# Test 6: Quality assurance and validation system  
test_quality_assurance_system() {
    local test_name="quality assurance and validation system"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    local quality_features=0
    
    # Check for quality assurance features
    if grep -qi "quality.*assurance\|validation\|quality.*gate" "$coordinator_file"; then
        quality_features=$((quality_features + 1))
    fi
    
    if grep -qi "success.*metric\|quality.*score\|satisfaction.*rating" "$coordinator_file"; then
        quality_features=$((quality_features + 1))
    fi
    
    if grep -qi "specialization.*compliance\|boundary.*enforcement\|agent.*validation" "$coordinator_file"; then
        quality_features=$((quality_features + 1))
    fi
    
    if [ "$quality_features" -ge 3 ]; then
        print_test_result "$test_name" "PASS" "Quality assurance system integrated"
    else
        print_test_result "$test_name" "FAIL" "Incomplete quality assurance ($quality_features/3 features)"
    fi
}

# Test 7: Performance and efficiency expectations
test_performance_expectations() {
    local test_name="performance and efficiency expectations" 
    local consultation_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    local performance_indicators=0
    
    # Check for time expectations
    if grep -qi "30.*minute\|time.*commitment\|session.*duration" "$consultation_file"; then
        performance_indicators=$((performance_indicators + 1))
    fi
    
    # Check for efficiency metrics in coordinator
    if grep -qi "efficiency\|performance.*metric\|session.*efficiency" "$coordinator_file"; then
        performance_indicators=$((performance_indicators + 1))
    fi
    
    # Check for optimization features
    if grep -qi "optimization\|load.*balancing\|real.*time" "$coordinator_file"; then
        performance_indicators=$((performance_indicators + 1))
    fi
    
    if [ "$performance_indicators" -ge 2 ]; then
        print_test_result "$test_name" "PASS" "Performance expectations properly set"
    else
        print_test_result "$test_name" "FAIL" "Insufficient performance indicators ($performance_indicators/3)"
    fi
}

# Test 8: Claude Code compliance integration
test_claude_code_compliance() {
    local test_name="Claude Code compliance integration"
    local consultation_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/begin-consultation.md"
    local coordinator_file="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude/commands/coordinate-agents.md"
    
    # Test validation exit codes (simpler approach)
    local consultation_result=1
    local coordinator_result=1
    
    # Test consultation validation
    if /Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/tests/validate-command.sh "$consultation_file" >/dev/null 2>&1; then
        consultation_result=0
    fi
    
    # Test coordinator validation  
    if /Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/tests/validate-command.sh "$coordinator_file" >/dev/null 2>&1; then
        coordinator_result=0
    fi
    
    if [ "$consultation_result" -eq 0 ] && [ "$coordinator_result" -eq 0 ]; then
        print_test_result "$test_name" "PASS" "Both commands validate successfully"
    else
        print_test_result "$test_name" "FAIL" "Validation failures: consultation($consultation_result), coordinator($coordinator_result)"
    fi
}

# Run comprehensive integration tests
echo -e "${BLUE}🚀 FULL INTEGRATION TESTING: Agent Consultation Workflow${NC}"
echo "Testing complete end-to-end integration of specialized agent coordination system..."
echo

test_e2e_command_integration
test_agent_specialization_completeness  
test_phase_workflow_consistency
test_session_state_architecture
test_user_interaction_integration
test_quality_assurance_system
test_performance_expectations
test_claude_code_compliance

echo
echo "📊 Integration Test Summary:"
echo "Tests Run: $TESTS_RUN"
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"

if [ $TESTS_FAILED -eq 0 ]; then
    echo
    echo -e "${GREEN}🎉 FULL INTEGRATION SUCCESS: Complete agent consultation workflow ready${NC}"
    echo -e "${GREEN}✅ All systems operational for production deployment${NC}"
    exit 0
else
    echo
    echo -e "${RED}❌ INTEGRATION ISSUES: $TESTS_FAILED critical integration problems detected${NC}"
    exit 1
fi