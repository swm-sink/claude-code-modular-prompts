#!/bin/bash
# TDD Integration Test Suite: Agent Integration System End-to-End
# Purpose: Test complete agent integration workflow from consultation to context generation

set -e
echo "=== Agent Integration System - Integration Tests ==="

# Setup test environment
TEST_PROJECT_DIR="/tmp/agent-integration-test-$(date +%s)"
mkdir -p "$TEST_PROJECT_DIR"

# Cleanup function
cleanup() {
    rm -rf "$TEST_PROJECT_DIR"
    rm -f .claude/consultation-state.json
    rm -rf .claude/context/
    rm -rf .claude/logs/
}
trap cleanup EXIT

# Test 1: Agent Integration Script Basic Functionality
echo "Test 1: Agent Integration Script Basic Execution"
if ./scripts/integrate-agents.sh test-mode > /dev/null 2>&1; then
    echo "✅ PASS: Agent integration script executes without errors"
else
    echo "❌ FAIL: Agent integration script execution failed"
    exit 1
fi

# Test 2: Individual Agent Invocation
echo "Test 2: Individual Agent Invocation"
if ./scripts/invoke-agent.sh context-engineer "$TEST_PROJECT_DIR" > /dev/null 2>&1; then
    echo "✅ PASS: Individual agent invocation works"
else
    echo "❌ FAIL: Individual agent invocation failed"
    exit 1
fi

# Test 3: Agent Output Generation
echo "Test 3: Agent Output Generation"
./scripts/invoke-agent.sh context-engineer "$TEST_PROJECT_DIR" > /dev/null 2>&1
if [ -f ".claude/context/technical-architecture.md" ]; then
    echo "✅ PASS: Agent generates expected output files"
else
    echo "❌ FAIL: Agent did not generate expected output"
    exit 1
fi

# Test 4: Session State Integration
echo "Test 4: Session State Integration"
./scripts/integrate-agents.sh context-engineer "$TEST_PROJECT_DIR" > /dev/null 2>&1
if [ -f ".claude/consultation-state.json" ]; then
    echo "✅ PASS: Session state file is created during agent execution"
else
    echo "❌ FAIL: Session state integration not working"
    exit 1
fi

# Test 5: Agent Coordination with Existing Commands
echo "Test 5: Agent Coordination Integration"
if grep -q "integrate-agents" ".claude/commands/coordinate-agents.md"; then
    if grep -q "agent_execution" ".claude/commands/manage-session-state.md"; then
        echo "✅ PASS: Agent integration properly coordinated with existing commands"
    else
        echo "❌ FAIL: Session state command missing agent execution integration"
        exit 1
    fi
else
    echo "❌ FAIL: Coordination command missing integration reference"
    exit 1
fi

# Test 6: Phase Execution Workflow
echo "Test 6: Phase Execution Workflow"
if ./scripts/integrate-agents.sh phase-1 "$TEST_PROJECT_DIR" > /dev/null 2>&1; then
    if [ -f ".claude/context/technical-architecture.md" ] && [ -f ".claude/context/research-evidence.md" ]; then
        echo "✅ PASS: Phase execution generates expected outputs"
    else
        echo "❌ FAIL: Phase execution missing expected outputs"
        exit 1
    fi
else
    echo "❌ FAIL: Phase execution failed"
    exit 1
fi

# Test 7: Agent Definition Validation
echo "Test 7: Agent Definition Validation"
for agent in context-engineer command-builder research-validator; do
    if [ -f ".claude/agents/${agent}.md" ]; then
        if grep -q "Agent Specialization" ".claude/agents/${agent}.md"; then
            if grep -q "Core Expertise" ".claude/agents/${agent}.md"; then
                echo "✅ PASS: Agent $agent has proper definition structure"
            else
                echo "❌ FAIL: Agent $agent missing core expertise section"
                exit 1
            fi
        else
            echo "❌ FAIL: Agent $agent missing specialization section"
            exit 1
        fi
    else
        echo "❌ FAIL: Agent $agent definition file missing"
        exit 1
    fi
done

# Test 8: Log Generation and Error Handling
echo "Test 8: Logging and Error Handling"
./scripts/integrate-agents.sh context-engineer "$TEST_PROJECT_DIR" > /dev/null 2>&1
if [ -f ".claude/logs/agent-integration.log" ]; then
    if grep -q "INFO" ".claude/logs/agent-integration.log"; then
        echo "✅ PASS: Logging system working correctly"
    else
        echo "❌ FAIL: Log file exists but no INFO messages found"
        exit 1
    fi
else
    echo "❌ FAIL: Log file not generated"
    exit 1
fi

# Test 9: Integration with Context Generation
echo "Test 9: Integration with Context Generation"
./scripts/integrate-agents.sh context-engineer "$TEST_PROJECT_DIR" > /dev/null 2>&1
if [ -d ".claude/context" ] && [ "$(find .claude/context -name '*.md' | wc -l)" -gt 0 ]; then
    echo "✅ PASS: Agent integration creates context directory and files"
else
    echo "❌ FAIL: Context generation integration not working"
    exit 1
fi

# Test 10: Cross-Agent Communication
echo "Test 10: Cross-Agent Communication and Coordination"
./scripts/integrate-agents.sh phase-2 "$TEST_PROJECT_DIR" > /dev/null 2>&1
if [ -f ".claude/context/command-integration.md" ]; then
    echo "✅ PASS: Multi-agent phase execution successful"
else
    echo "❌ FAIL: Cross-agent communication failed"
    exit 1
fi

echo "=== Agent Integration System - Integration Tests Complete ==="