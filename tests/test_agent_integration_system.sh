#!/bin/bash
# TDD Test Suite: Agent Integration System
# Purpose: Test the actual execution and integration of specialized agents

set -e
echo "=== Agent Integration System - Unit Tests ==="

# Test 1: Agent Integration Command Exists
echo "Test 1: Agent Integration Command Structure"
if [ -f ".claude/commands/integrate-agents.md" ]; then
    echo "✅ PASS: Agent integration command exists"
else
    echo "❌ FAIL: Agent integration command missing"
    exit 1
fi

# Test 2: Agent Definitions Directory Exists
echo "Test 2: Agent Definitions Structure"
if [ -d ".claude/agents" ]; then
    echo "✅ PASS: Agent definitions directory exists"
else
    echo "❌ FAIL: Agent definitions directory missing"
    exit 1
fi

# Test 3: Core Agent Implementations Exist
echo "Test 3: Core Agent Implementations"
AGENTS=("context-engineer" "command-builder" "research-validator")
for agent in "${AGENTS[@]}"; do
    if [ -f ".claude/agents/${agent}.md" ]; then
        echo "✅ PASS: ${agent} implementation exists"
    else
        echo "❌ FAIL: ${agent} implementation missing"
        exit 1
    fi
done

# Test 4: Agent Integration Script Exists
echo "Test 4: Agent Integration Execution Script"
if [ -f "scripts/integrate-agents.sh" ]; then
    echo "✅ PASS: Agent integration script exists"
else
    echo "❌ FAIL: Agent integration script missing"
    exit 1
fi

# Test 5: Agent Integration Script is Executable
echo "Test 5: Agent Integration Script Permissions"
if [ -x "scripts/integrate-agents.sh" ]; then
    echo "✅ PASS: Agent integration script is executable"
else
    echo "❌ FAIL: Agent integration script not executable"
    exit 1
fi

# Test 6: Agent Coordination Integration
echo "Test 6: Agent Coordination Integration"
if grep -q "integrate-agents" ".claude/commands/coordinate-agents.md"; then
    echo "✅ PASS: Agent coordination references integration system"
else
    echo "❌ FAIL: Agent coordination missing integration reference"
    exit 1
fi

# Test 7: Session State Integration
echo "Test 7: Session State Integration"
if grep -q "agent_execution" ".claude/commands/manage-session-state.md"; then
    echo "✅ PASS: Session state includes agent execution tracking"
else
    echo "❌ FAIL: Session state missing agent execution tracking"
    exit 1
fi

# Test 8: Agent Integration YAML Compliance
echo "Test 8: Agent Integration YAML Compliance"
if ./tests/validate-command.sh ".claude/commands/integrate-agents.md" > /dev/null 2>&1; then
    echo "✅ PASS: Agent integration command has valid YAML"
else
    echo "❌ FAIL: Agent integration command YAML invalid"
    exit 1
fi

# Test 9: Agent Invocation Mechanism
echo "Test 9: Agent Invocation Mechanism"
if [ -f "scripts/invoke-agent.sh" ]; then
    echo "✅ PASS: Agent invocation mechanism exists"
else
    echo "❌ FAIL: Agent invocation mechanism missing"
    exit 1
fi

echo "=== Agent Integration System - Unit Tests Complete ==="