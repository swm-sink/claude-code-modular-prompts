#!/bin/bash

# Context Generation Engine Integration Tests
# Tests integration with existing Claude Code system commands

set -e

echo "🔗 INTEGRATION PHASE: Context Generation System Integration Tests"

# Test Configuration
PROJECT_ROOT="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon"
TEST_PROJECT_DIR="$PROJECT_ROOT/test_integration"
CLAUDE_DIR="$TEST_PROJECT_DIR/.claude"

# Cleanup and Setup
cleanup() {
    rm -rf "$TEST_PROJECT_DIR" 2>/dev/null || true
}

setup_test_project() {
    cleanup
    mkdir -p "$TEST_PROJECT_DIR"
    cd "$TEST_PROJECT_DIR"
    
    # Copy Claude Code configuration
    mkdir -p "$CLAUDE_DIR"
    cp -r "$PROJECT_ROOT/.claude/commands" "$CLAUDE_DIR/" 2>/dev/null || true
    
    # Create test project files
    mkdir -p src tests docs
    echo "# Integration Test Project" > README.md
    echo '{"name": "integration-test", "version": "1.0.0"}' > package.json
    echo "# Test Project Context" > CLAUDE.md
}

# Integration Test 1: Context Generation + Begin Consultation Integration
test_begin_consultation_integration() {
    echo "Integration Test 1: /begin-consultation should work with /generate-context"
    
    setup_test_project
    
    # Test that begin-consultation command exists and references context generation
    if [ ! -f "$PROJECT_ROOT/.claude/commands/begin-consultation.md" ]; then
        echo "❌ FAIL: begin-consultation command missing"
        cleanup
        return 1
    fi
    
    # Check if begin-consultation references context generation
    if ! grep -q "context" "$PROJECT_ROOT/.claude/commands/begin-consultation.md"; then
        echo "❌ FAIL: begin-consultation should reference context generation"
        cleanup
        return 1
    fi
    
    # Test actual context generation works
    "$PROJECT_ROOT/scripts/generate-context.sh" --project-path="$TEST_PROJECT_DIR" --phase=technical-analysis
    
    if [ ! -d "$CLAUDE_DIR/context" ]; then
        echo "❌ FAIL: Context generation should work from begin-consultation workflow"
        cleanup
        return 1
    fi
    
    echo "✅ PASS: Begin consultation integrates with context generation"
    cleanup
    return 0
}

# Integration Test 2: Context Generation + Agent Coordination Integration
test_agent_coordination_integration() {
    echo "Integration Test 2: /coordinate-agents should work with context generation"
    
    setup_test_project
    
    # Test that coordinate-agents command exists
    if [ ! -f "$PROJECT_ROOT/.claude/commands/coordinate-agents.md" ]; then
        echo "❌ FAIL: coordinate-agents command missing"
        cleanup
        return 1
    fi
    
    # Test context generation with agent workflow
    "$PROJECT_ROOT/scripts/generate-context.sh" --project-path="$TEST_PROJECT_DIR" --phase=domain-intelligence
    
    # Verify context files that should be used by agents
    expected_files=(
        "$CLAUDE_DIR/context/business-domain.md"
        "$CLAUDE_DIR/context/user-workflows.md"
        "$CLAUDE_DIR/context/data-models.md"
        "$CLAUDE_DIR/context/integration-patterns.md"
    )
    
    for file in "${expected_files[@]}"; do
        if [ ! -f "$file" ]; then
            echo "❌ FAIL: Agent coordination missing context file: $file"
            cleanup
            return 1
        fi
    done
    
    echo "✅ PASS: Agent coordination integrates with context generation"
    cleanup
    return 0
}

# Integration Test 3: Context Generation + Session State Integration
test_session_state_integration() {
    echo "Integration Test 3: /manage-session-state should work with context generation"
    
    setup_test_project
    
    # Test that manage-session-state command exists
    if [ ! -f "$PROJECT_ROOT/.claude/commands/manage-session-state.md" ]; then
        echo "❌ FAIL: manage-session-state command missing"
        cleanup
        return 1
    fi
    
    # Test context generation with session state
    "$PROJECT_ROOT/scripts/generate-context.sh" --project-path="$TEST_PROJECT_DIR" --save-state
    
    # Verify session state file exists
    if [ ! -f "$CLAUDE_DIR/context-generation-state.json" ]; then
        echo "❌ FAIL: Session state not saved during context generation"
        cleanup
        return 1
    fi
    
    # Verify session state contains correct information
    if ! grep -q "technical-analysis" "$CLAUDE_DIR/context-generation-state.json"; then
        echo "❌ FAIL: Session state should contain phase information"
        cleanup
        return 1
    fi
    
    echo "✅ PASS: Session state management integrates with context generation"
    cleanup
    return 0
}

# Integration Test 4: Complete Workflow Integration
test_complete_workflow_integration() {
    echo "Integration Test 4: Complete consultation workflow integration"
    
    setup_test_project
    
    # Test complete workflow: consultation → context generation → validation
    "$PROJECT_ROOT/scripts/generate-context.sh" --complete --project-path="$TEST_PROJECT_DIR"
    
    # Verify all expected files are created
    expected_files=(
        "$CLAUDE_DIR/context/technical-architecture.md"
        "$CLAUDE_DIR/context/framework-detection.md"
        "$CLAUDE_DIR/context/project-structure.md" 
        "$CLAUDE_DIR/context/development-patterns.md"
        "$CLAUDE_DIR/context/business-domain.md"
        "$CLAUDE_DIR/context/user-workflows.md"
        "$CLAUDE_DIR/context/data-models.md"
        "$CLAUDE_DIR/context/integration-patterns.md"
        "$CLAUDE_DIR/context/navigation-index.md"
        "$CLAUDE_DIR/context/context-hierarchy.md"
        "$CLAUDE_DIR/context/cross-references.md"
        "$CLAUDE_DIR/context/validation-metrics.md"
        "$CLAUDE_DIR/context/before-after-examples.md"
        "$CLAUDE_DIR/context/effectiveness-tests.md"
        "$CLAUDE_DIR/context-generation-state.json"
    )
    
    missing_files=()
    for file in "${expected_files[@]}"; do
        if [ ! -f "$file" ]; then
            missing_files+=("$file")
        fi
    done
    
    if [ ${#missing_files[@]} -gt 0 ]; then
        echo "❌ FAIL: Complete workflow missing files: ${missing_files[*]}"
        cleanup
        return 1
    fi
    
    # Verify CLAUDE.md enhancement
    if ! grep -q "## Project Context Architecture" "$TEST_PROJECT_DIR/CLAUDE.md"; then
        echo "❌ FAIL: Complete workflow should enhance CLAUDE.md"
        cleanup
        return 1
    fi
    
    echo "✅ PASS: Complete workflow integration working"
    cleanup
    return 0
}

# Integration Test 5: Claude Code Command Compliance
test_claude_code_compliance() {
    echo "Integration Test 5: Context generation commands should be Claude Code compliant"
    
    # Test generate-context command YAML compliance
    if [ ! -f "$PROJECT_ROOT/.claude/commands/generate-context.md" ]; then
        echo "❌ FAIL: generate-context command should exist"
        return 1
    fi
    
    # Check YAML frontmatter exists
    if ! head -10 "$PROJECT_ROOT/.claude/commands/generate-context.md" | grep -q "name: /generate-context"; then
        echo "❌ FAIL: generate-context should have proper YAML frontmatter"
        return 1
    fi
    
    # Check required YAML fields
    required_fields=("name" "description" "usage" "allowed-tools" "category")
    for field in "${required_fields[@]}"; do
        if ! head -20 "$PROJECT_ROOT/.claude/commands/generate-context.md" | grep -q "$field:"; then
            echo "❌ FAIL: generate-context missing required YAML field: $field"
            return 1
        fi
    done
    
    echo "✅ PASS: Context generation commands are Claude Code compliant"
    return 0
}

# Integration Test 6: Error Handling Integration
test_error_handling_integration() {
    echo "Integration Test 6: Error handling should work across integrated systems"
    
    setup_test_project
    
    # Test invalid phase handling
    if "$PROJECT_ROOT/scripts/generate-context.sh" --phase=invalid-phase --project-path="$TEST_PROJECT_DIR" 2>/dev/null; then
        echo "❌ FAIL: Should reject invalid phase"
        cleanup
        return 1
    fi
    
    # Test invalid project path handling
    if "$PROJECT_ROOT/scripts/generate-context.sh" --project-path="/nonexistent/path" 2>/dev/null; then
        echo "❌ FAIL: Should reject invalid project path"
        cleanup
        return 1
    fi
    
    # Test partial failure recovery - create directory but make it readonly
    mkdir -p "$CLAUDE_DIR/context"
    chmod 444 "$CLAUDE_DIR/context" 2>/dev/null || true
    
    # This should fail gracefully
    if "$PROJECT_ROOT/scripts/generate-context.sh" --project-path="$TEST_PROJECT_DIR" 2>/dev/null; then
        echo "⚠️  WARNING: Should handle readonly directory gracefully"
    fi
    
    # Restore permissions
    chmod 755 "$CLAUDE_DIR/context" 2>/dev/null || true
    
    echo "✅ PASS: Error handling integration working"
    cleanup
    return 0
}

# Integration Test 7: Performance and Resource Integration
test_performance_integration() {
    echo "Integration Test 7: Performance integration with existing system"
    
    setup_test_project
    
    # Test that context generation doesn't create excessive files
    "$PROJECT_ROOT/scripts/generate-context.sh" --complete --project-path="$TEST_PROJECT_DIR"
    
    file_count=$(find "$CLAUDE_DIR/context" -name "*.md" | wc -l)
    if [ "$file_count" -gt 20 ]; then
        echo "❌ FAIL: Context generation creating too many files: $file_count"
        cleanup
        return 1
    fi
    
    # Test that generated files are reasonable size
    large_files=$(find "$CLAUDE_DIR/context" -name "*.md" -size +10k)
    if [ -n "$large_files" ]; then
        echo "⚠️  WARNING: Some context files are large: $large_files"
    fi
    
    echo "✅ PASS: Performance integration acceptable"
    cleanup
    return 0
}

# Run All Integration Tests
run_integration_tests() {
    echo "🔗 INTEGRATION PHASE: Running Context Generation Integration Tests"
    echo "=================================================================="
    
    failed_tests=()
    
    test_begin_consultation_integration || failed_tests+=("test_begin_consultation_integration")
    test_agent_coordination_integration || failed_tests+=("test_agent_coordination_integration")
    test_session_state_integration || failed_tests+=("test_session_state_integration")
    test_complete_workflow_integration || failed_tests+=("test_complete_workflow_integration")
    test_claude_code_compliance || failed_tests+=("test_claude_code_compliance")
    test_error_handling_integration || failed_tests+=("test_error_handling_integration")
    test_performance_integration || failed_tests+=("test_performance_integration")
    
    echo "=================================================================="
    
    if [ ${#failed_tests[@]} -eq 0 ]; then
        echo "🎉 All integration tests passed!"
        echo "🔗 Context Generation Engine successfully integrated with Claude Code system"
        return 0
    else
        echo "❌ Integration tests failed: ${#failed_tests[@]} failures"
        echo "Failed tests: ${failed_tests[*]}"
        echo ""
        echo "Integration issues detected - system requires fixes before deployment"
        return 1
    fi
}

# Main execution
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_integration_tests
fi