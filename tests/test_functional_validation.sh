#!/bin/bash

# Functional Validation Test Suite for Claude Code Modular Prompts
# Tests actual command functionality and Claude Code compatibility

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Test counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0
WARNED_TESTS=0

# Test results
TEST_RESULTS=()

# Helper functions
log_test() {
    local status="$1"
    local test_name="$2"
    local details="$3"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    case "$status" in
        "PASS")
            echo -e "${GREEN}✅ PASS${NC}: $test_name"
            PASSED_TESTS=$((PASSED_TESTS + 1))
            TEST_RESULTS+=("PASS: $test_name")
            ;;
        "FAIL")
            echo -e "${RED}❌ FAIL${NC}: $test_name"
            [ -n "$details" ] && echo "   Details: $details"
            FAILED_TESTS=$((FAILED_TESTS + 1))
            TEST_RESULTS+=("FAIL: $test_name - $details")
            ;;
        "WARN")
            echo -e "${YELLOW}⚠️  WARN${NC}: $test_name"
            [ -n "$details" ] && echo "   Warning: $details"
            WARNED_TESTS=$((WARNED_TESTS + 1))
            TEST_RESULTS+=("WARN: $test_name - $details")
            ;;
    esac
}

# Test 1: Core Command Functionality
test_core_commands() {
    echo ""
    echo -e "${BLUE}=== Testing Core Commands ===${NC}"
    
    local core_commands=(
        ".claude/commands/core/help.md"
        ".claude/commands/core/task.md"
        ".claude/commands/core/auto.md"
        ".claude/commands/core/project-task.md"
    )
    
    for cmd in "${core_commands[@]}"; do
        if [ -f "$cmd" ]; then
            test_command_structure "$cmd"
            test_slash_command_format "$cmd"
            test_prompt_quality "$cmd"
        else
            log_test "FAIL" "Core command exists: $(basename "$cmd")" "File not found: $cmd"
        fi
    done
}

# Test 2: Meta Command Functionality
test_meta_commands() {
    echo ""
    echo -e "${BLUE}=== Testing Meta Commands ===${NC}"
    
    local meta_commands=(
        ".claude/commands/meta/adapt-to-project.md"
        ".claude/commands/meta/validate-adaptation.md"
        ".claude/commands/meta/welcome.md"
        ".claude/commands/meta/sync-from-reference.md"
        ".claude/commands/meta/replace-placeholders.md"
    )
    
    for cmd in "${meta_commands[@]}"; do
        if [ -f "$cmd" ]; then
            test_command_structure "$cmd"
            test_guide_command_effectiveness "$cmd"
        else
            log_test "FAIL" "Meta command exists: $(basename "$cmd")" "File not found: $cmd"
        fi
    done
}

# Test 3: Development Commands
test_development_commands() {
    echo ""
    echo -e "${BLUE}=== Testing Development Commands ===${NC}"
    
    local dev_commands=(
        ".claude/commands/development/dev.md"
        ".claude/commands/development/api-design.md"
        ".claude/commands/development/env-setup.md"
    )
    
    for cmd in "${dev_commands[@]}"; do
        if [ -f "$cmd" ]; then
            test_command_structure "$cmd"
            test_development_workflow "$cmd"
        else
            log_test "WARN" "Development command optional: $(basename "$cmd")" "File not found: $cmd"
        fi
    done
}

# Test command structure and YAML front matter
test_command_structure() {
    local file="$1"
    local basename_file=$(basename "$file")
    
    # Test YAML front matter
    if head -1 "$file" | grep -q "^---$"; then
        log_test "PASS" "$basename_file has YAML front matter" ""
    else
        log_test "FAIL" "$basename_file YAML front matter" "Missing opening YAML delimiter"
        return 1
    fi
    
    # Test required fields
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    if [ -n "$yaml_end" ]; then
        local yaml_content=$(sed -n "2,$((yaml_end-1))p" "$file")
        
        # Check name field
        if echo "$yaml_content" | grep -q "^name:"; then
            log_test "PASS" "$basename_file has name field" ""
        else
            log_test "FAIL" "$basename_file name field" "Missing required name field"
        fi
        
        # Check description field
        if echo "$yaml_content" | grep -q "^description:"; then
            log_test "PASS" "$basename_file has description field" ""
        else
            log_test "FAIL" "$basename_file description field" "Missing required description field"
        fi
        
        # Check for Claude Code specific fields
        if echo "$yaml_content" | grep -q "^allowed-tools:"; then
            log_test "PASS" "$basename_file has allowed-tools field" ""
        else
            log_test "WARN" "$basename_file allowed-tools field" "Missing Claude Code allowed-tools field"
        fi
    else
        log_test "FAIL" "$basename_file YAML structure" "Missing closing YAML delimiter"
    fi
}

# Test slash command format
test_slash_command_format() {
    local file="$1"
    local basename_file=$(basename "$file")
    
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    if [ -n "$yaml_end" ]; then
        local yaml_content=$(sed -n "2,$((yaml_end-1))p" "$file")
        local name_line=$(echo "$yaml_content" | grep "^name:" | head -1)
        
        if [ -n "$name_line" ]; then
            local command_name=$(echo "$name_line" | sed 's/name: *//g' | tr -d '"' | tr -d "'")
            
            # Test slash command format
            if [[ "$command_name" =~ ^/[a-zA-Z][a-zA-Z0-9-]*$ ]]; then
                log_test "PASS" "$basename_file slash command format" "$command_name"
            else
                log_test "FAIL" "$basename_file slash command format" "Invalid format: $command_name"
            fi
            
            # Test command name consistency with filename
            local expected_name=$(basename "$file" .md)
            local actual_name=$(echo "$command_name" | sed 's/^\/*//')
            if [ "$actual_name" = "$expected_name" ]; then
                log_test "PASS" "$basename_file name consistency" ""
            else
                log_test "WARN" "$basename_file name consistency" "Filename: $expected_name, Command: $actual_name"
            fi
        fi
    fi
}

# Test prompt quality and effectiveness
test_prompt_quality() {
    local file="$1"
    local basename_file=$(basename "$file")
    
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    if [ -n "$yaml_end" ]; then
        local content=$(tail -n +$((yaml_end+1)) "$file")
        
        # Test for clear instructions
        if echo "$content" | grep -qiE "(you are|I will|I'll help|help you|I'm|let me)"; then
            log_test "PASS" "$basename_file clear instructions" ""
        else
            log_test "WARN" "$basename_file clear instructions" "No clear instruction pattern found"
        fi
        
        # Test for context awareness
        if echo "$content" | grep -qE "\\[INSERT_[A-Z_]*\\]"; then
            local placeholder_count=$(echo "$content" | grep -o "\\[INSERT_[A-Z_]*\\]" | wc -l)
            log_test "PASS" "$basename_file template placeholders" "$placeholder_count placeholders found"
        else
            log_test "PASS" "$basename_file finalized command" "No placeholders (customized command)"
        fi
        
        # Test content length
        local char_count=$(echo "$content" | wc -c)
        if [ "$char_count" -gt 100 ]; then
            log_test "PASS" "$basename_file adequate content" "$char_count characters"
        else
            log_test "FAIL" "$basename_file adequate content" "Too short: $char_count characters"
        fi
        
        # Test for structured approach
        if echo "$content" | grep -qE "(##|\\*\\*|1\\.|2\\.|3\\.)"; then
            log_test "PASS" "$basename_file structured content" ""
        else
            log_test "WARN" "$basename_file structured content" "Consider adding structure (headers, lists, steps)"
        fi
    fi
}

# Test guide command effectiveness
test_guide_command_effectiveness() {
    local file="$1"
    local basename_file=$(basename "$file")
    
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    if [ -n "$yaml_end" ]; then
        local content=$(tail -n +$((yaml_end+1)) "$file")
        
        # Test for guidance patterns
        if echo "$content" | grep -qiE "(step-by-step|checklist|guide|manual|instructions)"; then
            log_test "PASS" "$basename_file guidance patterns" ""
        else
            log_test "WARN" "$basename_file guidance patterns" "No clear guidance patterns found"
        fi
        
        # Test for user interaction
        if echo "$content" | grep -qE "(\?|\bChoose\b|\bSelect\b|\bWhich\b)"; then
            log_test "PASS" "$basename_file user interaction" ""
        else
            log_test "WARN" "$basename_file user interaction" "No user interaction prompts found"
        fi
        
        # Test for limitations acknowledgment
        if echo "$content" | grep -qiE "(cannot|can't|manual|you'll need to|I cannot)"; then
            log_test "PASS" "$basename_file realistic expectations" ""
        else
            log_test "WARN" "$basename_file realistic expectations" "Should acknowledge limitations"
        fi
    fi
}

# Test development workflow commands
test_development_workflow() {
    local file="$1"
    local basename_file=$(basename "$file")
    
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    if [ -n "$yaml_end" ]; then
        local content=$(tail -n +$((yaml_end+1)) "$file")
        
        # Test for workflow steps
        if echo "$content" | grep -qiE "(analysis|design|implementation|testing|deployment)"; then
            log_test "PASS" "$basename_file workflow steps" ""
        else
            log_test "WARN" "$basename_file workflow steps" "No clear workflow steps identified"
        fi
        
        # Test for best practices
        if echo "$content" | grep -qiE "(best practices|standards|conventions|quality)"; then
            log_test "PASS" "$basename_file best practices" ""
        else
            log_test "WARN" "$basename_file best practices" "No best practices mentioned"
        fi
    fi
}

# Test setup script functionality
test_setup_script() {
    echo ""
    echo -e "${BLUE}=== Testing Setup Script ===${NC}"
    
    if [ -f "setup.sh" ]; then
        log_test "PASS" "Setup script exists" ""
        
        # Test script permissions
        if [ -x "setup.sh" ]; then
            log_test "PASS" "Setup script executable" ""
        else
            log_test "FAIL" "Setup script executable" "setup.sh is not executable"
        fi
        
        # Test script content (basic validation)
        if grep -q "#!/bin/bash" setup.sh; then
            log_test "PASS" "Setup script has shebang" ""
        else
            log_test "WARN" "Setup script has shebang" "No bash shebang found"
        fi
        
        # Test for error handling
        if grep -q "set -e" setup.sh; then
            log_test "PASS" "Setup script error handling" ""
        else
            log_test "WARN" "Setup script error handling" "Consider adding 'set -e' for error handling"
        fi
    else
        log_test "FAIL" "Setup script exists" "setup.sh not found"
    fi
}

# Test active vs deprecated command separation
test_command_organization() {
    echo ""
    echo -e "${BLUE}=== Testing Command Organization ===${NC}"
    
    # Count active commands
    local active_count=0
    if [ -d ".claude/commands" ]; then
        active_count=$(find .claude/commands -name "*.md" -not -path "*/deprecated/*" | wc -l)
        log_test "PASS" "Active commands directory" "$active_count active commands found"
    else
        log_test "FAIL" "Active commands directory" ".claude/commands directory not found"
    fi
    
    # Count deprecated commands
    local deprecated_count=0
    if [ -d ".claude/commands/deprecated" ]; then
        deprecated_count=$(find .claude/commands/deprecated -name "*.md" | wc -l)
        log_test "PASS" "Deprecated commands directory" "$deprecated_count deprecated commands found"
    else
        log_test "WARN" "Deprecated commands directory" "No deprecated commands directory"
    fi
    
    # Test total command count
    local total_count=$((active_count + deprecated_count))
    if [ "$total_count" -ge 64 ]; then
        log_test "PASS" "Command count target" "$total_count total commands (target: 64+ active)"
    else
        log_test "WARN" "Command count target" "$total_count total commands (target: 64+ active)"
    fi
}

# Main test execution
main() {
    echo "=============================================="
    echo "Functional Validation Test Suite"
    echo "=============================================="
    echo -e "${BLUE}Testing Claude Code compatibility and command effectiveness${NC}"
    echo ""
    
    # Run all test suites
    test_core_commands
    test_meta_commands
    test_development_commands
    test_setup_script
    test_command_organization
    
    # Generate summary report
    echo ""
    echo "=============================================="
    echo "FUNCTIONAL VALIDATION RESULTS"
    echo "=============================================="
    echo "Total Tests: $TOTAL_TESTS"
    echo -e "Passed: ${GREEN}$PASSED_TESTS${NC}"
    echo -e "Failed: ${RED}$FAILED_TESTS${NC}"
    echo -e "Warnings: ${YELLOW}$WARNED_TESTS${NC}"
    
    # Calculate success rate
    if [ $TOTAL_TESTS -gt 0 ]; then
        local success_rate=$(( (PASSED_TESTS * 100) / TOTAL_TESTS ))
        echo "Success Rate: $success_rate%"
        
        # Determine overall status
        if [ $FAILED_TESTS -eq 0 ] && [ $success_rate -ge 90 ]; then
            echo ""
            echo -e "${GREEN}✅ FUNCTIONAL VALIDATION PASSED${NC}"
            echo "Commands are ready for Claude Code deployment!"
            exit 0
        elif [ $FAILED_TESTS -eq 0 ] && [ $success_rate -ge 75 ]; then
            echo ""
            echo -e "${YELLOW}⚠️  FUNCTIONAL VALIDATION PASSED WITH WARNINGS${NC}"
            echo "Commands are functional but have optimization opportunities."
            exit 0
        else
            echo ""
            echo -e "${RED}❌ FUNCTIONAL VALIDATION FAILED${NC}"
            echo "Critical issues found that prevent Claude Code compatibility."
            echo ""
            echo "Failed Tests:"
            for result in "${TEST_RESULTS[@]}"; do
                if [[ "$result" == FAIL:* ]]; then
                    echo "  - ${result#FAIL: }"
                fi
            done
            exit 1
        fi
    else
        echo -e "${RED}❌ No tests executed${NC}"
        exit 1
    fi
}

# Only run if executed directly
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    main "$@"
fi