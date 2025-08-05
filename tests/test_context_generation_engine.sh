#!/bin/bash

# Context Generation Engine Test Suite - RED PHASE
# Tests the core context generation functionality promised by /begin-consultation

set -e

echo "🔴 RED PHASE: Context Generation Engine Tests"

# Test Configuration
PROJECT_ROOT="/Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon"
TEST_PROJECT_DIR="$PROJECT_ROOT/test_context_generation"
CLAUDE_DIR="$TEST_PROJECT_DIR/.claude"

# Cleanup and Setup
cleanup() {
    rm -rf "$TEST_PROJECT_DIR" 2>/dev/null || true
}

setup_test_project() {
    cleanup
    mkdir -p "$TEST_PROJECT_DIR"
    cd "$TEST_PROJECT_DIR"
    
    # Create minimal project structure for testing
    mkdir -p src tests docs
    echo "# Test Project" > README.md
    echo '{"name": "test-project", "version": "1.0.0"}' > package.json
}

# Test 1: Context Generation Engine Command Exists
test_context_generation_command_exists() {
    echo "Test 1: Context Generation Engine command should exist"
    
    if [ ! -f "$PROJECT_ROOT/.claude/commands/generate-context.md" ]; then
        echo "❌ FAIL: Context Generation Engine command missing"
        echo "Expected: $PROJECT_ROOT/.claude/commands/generate-context.md"
        return 1
    fi
    
    echo "✅ PASS: Context Generation Engine command exists"
    return 0
}

# Test 2: Context Generation Creates Directory Structure
test_context_directory_creation() {
    echo "Test 2: Context generation should create .claude/context/ directory"
    
    setup_test_project
    
    # Execute context generation using our script
    "$PROJECT_ROOT/scripts/generate-context.sh" --project-path="$TEST_PROJECT_DIR" --phase=technical-analysis
    
    if [ ! -d "$CLAUDE_DIR/context" ]; then
        echo "❌ FAIL: Context directory not created"
        echo "Expected: $CLAUDE_DIR/context/"
        cleanup
        return 1
    fi
    
    echo "✅ PASS: Context directory created"
    cleanup
    return 0
}

# Test 3: Technical Analysis Context Generation
test_technical_analysis_context() {
    echo "Test 3: Technical analysis should generate framework detection context"
    
    setup_test_project
    
    # Expected context files after technical analysis
    expected_files=(
        "$CLAUDE_DIR/context/technical-architecture.md"
        "$CLAUDE_DIR/context/framework-detection.md"
        "$CLAUDE_DIR/context/project-structure.md"
        "$CLAUDE_DIR/context/development-patterns.md"
    )
    
    # Execute technical analysis context generation
    "$PROJECT_ROOT/scripts/generate-context.sh" --phase=technical-analysis --project-path="$TEST_PROJECT_DIR"
    
    for file in "${expected_files[@]}"; do
        if [ ! -f "$file" ]; then
            echo "❌ FAIL: Technical analysis context file missing: $file"
            cleanup
            return 1
        fi
    done
    
    echo "✅ PASS: Technical analysis context files generated"
    cleanup
    return 0
}

# Test 4: Domain Intelligence Context Generation
test_domain_intelligence_context() {
    echo "Test 4: Domain intelligence should generate business context"
    
    setup_test_project
    
    # Expected context files after domain intelligence
    expected_files=(
        "$CLAUDE_DIR/context/business-domain.md"
        "$CLAUDE_DIR/context/user-workflows.md"
        "$CLAUDE_DIR/context/data-models.md"
        "$CLAUDE_DIR/context/integration-patterns.md"
    )
    
    # Execute domain intelligence context generation
    "$PROJECT_ROOT/scripts/generate-context.sh" --phase=domain-intelligence --project-path="$TEST_PROJECT_DIR"
    
    for file in "${expected_files[@]}"; do
        if [ ! -f "$file" ]; then
            echo "❌ FAIL: Domain intelligence context file missing: $file"
            cleanup
            return 1
        fi
    done
    
    echo "✅ PASS: Domain intelligence context files generated"
    cleanup
    return 0
}

# Test 5: Context Navigation System
test_context_navigation_system() {
    echo "Test 5: Context generation should create navigation system"
    
    setup_test_project
    
    # Expected navigation files
    expected_files=(
        "$CLAUDE_DIR/context/navigation-index.md"
        "$CLAUDE_DIR/context/context-hierarchy.md"
        "$CLAUDE_DIR/context/cross-references.md"
    )
    
    # Execute complete context generation
    "$PROJECT_ROOT/scripts/generate-context.sh" --complete --project-path="$TEST_PROJECT_DIR"
    
    for file in "${expected_files[@]}"; do
        if [ ! -f "$file" ]; then
            echo "❌ FAIL: Navigation system file missing: $file"
            cleanup
            return 1
        fi
    done
    
    echo "✅ PASS: Context navigation system created"
    cleanup
    return 0
}

# Test 6: Enhanced CLAUDE.md Generation
test_enhanced_claude_md_generation() {
    echo "Test 6: Context generation should enhance CLAUDE.md with project context"
    
    setup_test_project
    
    # Create initial CLAUDE.md
    echo "# Test Project Context" > "$TEST_PROJECT_DIR/CLAUDE.md"
    
    # Execute context generation with CLAUDE.md enhancement
    "$PROJECT_ROOT/scripts/generate-context.sh" --enhance-claude-md --project-path="$TEST_PROJECT_DIR"
    
    # Check if CLAUDE.md was enhanced
    if ! grep -q "## Project Context Architecture" "$TEST_PROJECT_DIR/CLAUDE.md"; then
        echo "❌ FAIL: CLAUDE.md not enhanced with project context"
        cleanup
        return 1
    fi
    
    echo "✅ PASS: CLAUDE.md enhanced with project context"
    cleanup
    return 0
}

# Test 7: Context Validation and Effectiveness
test_context_effectiveness_validation() {
    echo "Test 7: Context generation should include effectiveness validation"
    
    setup_test_project
    
    # Expected validation files
    expected_files=(
        "$CLAUDE_DIR/context/validation-metrics.md"
        "$CLAUDE_DIR/context/before-after-examples.md"
        "$CLAUDE_DIR/context/effectiveness-tests.md"
    )
    
    # Execute context generation with validation
    "$PROJECT_ROOT/scripts/generate-context.sh" --with-validation --project-path="$TEST_PROJECT_DIR"
    
    for file in "${expected_files[@]}"; do
        if [ ! -f "$file" ]; then
            echo "❌ FAIL: Context validation file missing: $file"
            cleanup
            return 1
        fi
    done
    
    echo "✅ PASS: Context effectiveness validation created"
    cleanup
    return 0
}

# Test 8: Interactive Approval Integration
test_interactive_approval_system() {
    echo "Test 8: Context generation should support interactive approval"
    
    setup_test_project
    
    # Test that context generation can be paused for user approval
    if [ ! -f "$PROJECT_ROOT/.claude/commands/generate-context.md" ]; then
        echo "❌ FAIL: Context generation command should support interactive approval"
        cleanup
        return 1
    fi
    
    # Check if command supports approval flow
    if ! grep -q "approval" "$PROJECT_ROOT/.claude/commands/generate-context.md" 2>/dev/null; then
        echo "❌ FAIL: Context generation should support interactive approval workflow"
        cleanup
        return 1
    fi
    
    echo "✅ PASS: Interactive approval system supported"
    cleanup
    return 0
}

# Test 9: Session State Integration
test_session_state_integration() {
    echo "Test 9: Context generation should integrate with session state management"
    
    setup_test_project
    
    # Test that context generation works with session state
    expected_state_file="$CLAUDE_DIR/context-generation-state.json"
    
    # Execute context generation with session state
    "$PROJECT_ROOT/scripts/generate-context.sh" --save-state --project-path="$TEST_PROJECT_DIR"
    
    if [ ! -f "$expected_state_file" ]; then
        echo "❌ FAIL: Context generation state not saved"
        cleanup
        return 1
    fi
    
    echo "✅ PASS: Session state integration working"
    cleanup
    return 0
}

# Run All Tests
run_all_tests() {
    echo "🔴 RED PHASE: Running Context Generation Engine Tests"
    echo "=============================================="
    
    failed_tests=()
    
    test_context_generation_command_exists || failed_tests+=("test_context_generation_command_exists")
    test_context_directory_creation || failed_tests+=("test_context_directory_creation")
    test_technical_analysis_context || failed_tests+=("test_technical_analysis_context")
    test_domain_intelligence_context || failed_tests+=("test_domain_intelligence_context")
    test_context_navigation_system || failed_tests+=("test_context_navigation_system")
    test_enhanced_claude_md_generation || failed_tests+=("test_enhanced_claude_md_generation")
    test_context_effectiveness_validation || failed_tests+=("test_context_effectiveness_validation")
    test_interactive_approval_system || failed_tests+=("test_interactive_approval_system")
    test_session_state_integration || failed_tests+=("test_session_state_integration")
    
    echo "=============================================="
    
    if [ ${#failed_tests[@]} -eq 0 ]; then
        echo "🟢 All tests passed! (This shouldn't happen in RED phase)"
        return 0
    else
        echo "🔴 RED PHASE: ${#failed_tests[@]} tests failed (expected in RED phase)"
        echo "Failed tests: ${failed_tests[*]}"
        echo ""
        echo "Next: Implement Context Generation Engine to make tests pass (GREEN phase)"
        return 1
    fi
}

# Main execution
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_all_tests
fi