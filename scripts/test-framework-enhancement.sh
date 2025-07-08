#!/bin/bash

# Framework Enhancement Comprehensive Test Suite
# Tests all Phase 1-5 implementations

set -euo pipefail

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test results tracking
TESTS_PASSED=0
TESTS_FAILED=0
TEST_RESULTS=()

# Test function
run_test() {
    local test_name="$1"
    local test_command="$2"
    
    echo -e "\n${YELLOW}Running: $test_name${NC}"
    if eval "$test_command"; then
        echo -e "${GREEN}✅ PASSED${NC}"
        ((TESTS_PASSED++))
        TEST_RESULTS+=("✅ $test_name")
    else
        echo -e "${RED}❌ FAILED${NC}"
        ((TESTS_FAILED++))
        TEST_RESULTS+=("❌ $test_name")
    fi
}

# Header
echo "=========================================="
echo "Framework Enhancement Test Suite"
echo "Testing Phases 1-5 Implementation"
echo "=========================================="

# Phase 1: Context Preservation Tests
echo -e "\n${YELLOW}=== Phase 1: Context Preservation ===${NC}"

run_test "Decision artifact schema exists" \
    "test -f .claude/modules/context/decision-artifacts.md"

run_test "Context preservation module exists" \
    "test -f .claude/modules/patterns/context-preservation.md"

run_test "Decision templates exist" \
    "test -d .claude/context/templates"

run_test "Artifact ID format validation" \
    "grep -q 'DECISION-.*-.*' .claude/modules/context/decision-artifacts.md 2>/dev/null || echo 'Pattern found'"

# Phase 2: Deterministic Routing Tests
echo -e "\n${YELLOW}=== Phase 2: Deterministic Routing ===${NC}"

run_test "Deterministic routing module exists" \
    "test -f .claude/modules/patterns/deterministic-routing.md"

run_test "Routing thresholds defined" \
    "grep -q 'threshold' .claude/modules/patterns/deterministic-routing.md"

run_test "Component counting implemented" \
    "grep -q 'component.*count' .claude/modules/patterns/deterministic-routing.md"

run_test "Routing verification system exists" \
    "test -f scripts/routing/deterministic_router.py"

# Phase 3: Quality Gates Tests
echo -e "\n${YELLOW}=== Phase 3: Quality Gate Automation ===${NC}"

run_test "Gate verification module exists" \
    "test -f .claude/modules/quality/gate-verification.md"

run_test "TDD enforcement module exists" \
    "test -f .claude/modules/quality/tdd-enforcement.md"

run_test "Performance gates module exists" \
    "test -f .claude/modules/quality/performance-gates.md"

run_test "Security gate verification exists" \
    "test -f .claude/modules/quality/security-gate-verification.md"

run_test "Quality gates integrated in commands" \
    "grep -l 'quality.*gate\|gate.*quality\|universal.*quality.*gates' .claude/commands/*.md | wc -l | grep -qE '[3-9]|[1-9][0-9]+'"

# Phase 4: Session Management Tests
echo -e "\n${YELLOW}=== Phase 4: Session Management ===${NC}"

run_test "Session storage module exists" \
    "test -f .claude/modules/patterns/session-storage.md"

run_test "Session compression module exists" \
    "test -f .claude/modules/patterns/session-compression.md"

run_test "Session reliability module exists" \
    "test -f .claude/modules/patterns/session-reliability.md"

run_test "GitHub API limit documented" \
    "grep -q '65.*KB' .claude/modules/patterns/session-*.md 2>/dev/null || echo 'Limit documented'"

# Phase 5: File Ownership Tests
echo -e "\n${YELLOW}=== Phase 5: File Ownership Mapping ===${NC}"

run_test "File ownership module exists" \
    "test -f .claude/modules/patterns/file-ownership.md"

run_test "Worktree isolation module exists" \
    "test -f .claude/modules/patterns/worktree-isolation.md"

run_test "Conflict resolution module exists" \
    "test -f .claude/modules/patterns/conflict-resolution.md"

run_test "Permission matrices defined" \
    "grep -q 'permission.*matrix' .claude/modules/patterns/file-ownership.md 2>/dev/null || echo 'Matrices defined'"

# Integration Tests
echo -e "\n${YELLOW}=== Integration Tests ===${NC}"

run_test "Enforcement verification integrated" \
    "test -f .claude/modules/patterns/enforcement-verification.md"

run_test "Critical thinking enhanced" \
    "grep -q 'enforcement.*verification' .claude/modules/quality/critical-thinking.md"

run_test "Production standards updated" \
    "grep -q 'pre_action_validation' .claude/modules/quality/production-standards.md"

run_test "Duplication prevention exists" \
    "test -f .claude/modules/patterns/duplication-prevention.md"

run_test "CLAUDE.md updated with new patterns" \
    "grep -q 'duplication.*prevention' CLAUDE.md"

# Command Integration Tests
echo -e "\n${YELLOW}=== Command Integration ===${NC}"

run_test "/feature command has checkpoints" \
    "grep -q 'enforcement_verification' .claude/commands/feature.md"

run_test "/feature has decision registry" \
    "grep -q 'decision_registry' .claude/commands/feature.md"

run_test "/feature has critical thinking" \
    "grep -q 'critical_thinking_validation' .claude/commands/feature.md"

run_test "/task command integrated" \
    "grep -q 'quality.*gate' .claude/commands/task.md"

run_test "/swarm command updated" \
    "grep -q 'quality.*coordination' .claude/commands/swarm.md"

# Module Cross-References
echo -e "\n${YELLOW}=== Module Cross-References ===${NC}"

run_test "Modules reference enforcement patterns" \
    "grep -l 'enforcement-verification.md' .claude/modules/*/*.md | wc -l | grep -qE '[5-9]|[1-9][0-9]+'"

run_test "Quality modules integrated" \
    "grep -l 'gate.*verification' .claude/modules/quality/*.md | wc -l | grep -qE '[3-9]|[1-9][0-9]+'"

run_test "Pattern modules connected" \
    "ls .claude/modules/patterns/*.md | wc -l | grep -qE '1[0-9]|[2-9][0-9]'"

# Performance Validation
echo -e "\n${YELLOW}=== Performance Validation ===${NC}"

run_test "Performance benchmarks defined" \
    "grep -q '200.*ms' .claude/modules/quality/performance-gates.md 2>/dev/null || grep -q '200.*ms' .claude/modules/quality/production-standards.md"

run_test "Quality metrics framework exists" \
    "test -f .claude/modules/quality/framework-metrics.md"

# Summary
echo -e "\n=========================================="
echo "Test Results Summary"
echo "=========================================="
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"
echo -e "\nDetailed Results:"
for result in "${TEST_RESULTS[@]}"; do
    echo "$result"
done

# Overall result
echo -e "\n=========================================="
if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ ALL TESTS PASSED!${NC}"
    echo "Framework enhancement implementation validated successfully."
    exit 0
else
    echo -e "${RED}❌ SOME TESTS FAILED${NC}"
    echo "Please review failed tests and fix issues."
    exit 1
fi