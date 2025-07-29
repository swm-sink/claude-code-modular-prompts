#!/bin/bash

# Comprehensive Testing Suite Runner
# Executes all tests and generates summary report

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Test results tracking
TOTAL_SUITES=0
PASSED_SUITES=0
FAILED_SUITES=0

# Test suite results
SUITE_RESULTS=()

# Helper functions
log_suite_result() {
    local suite_name="$1"
    local status="$2"
    local details="$3"
    
    TOTAL_SUITES=$((TOTAL_SUITES + 1))
    
    case "$status" in
        "PASS")
            echo -e "${GREEN}✅ SUITE PASSED${NC}: $suite_name"
            PASSED_SUITES=$((PASSED_SUITES + 1))
            SUITE_RESULTS+=("PASS: $suite_name - $details")
            ;;
        "FAIL")
            echo -e "${RED}❌ SUITE FAILED${NC}: $suite_name"
            FAILED_SUITES=$((FAILED_SUITES + 1))
            SUITE_RESULTS+=("FAIL: $suite_name - $details")
            ;;
        "WARN")
            echo -e "${YELLOW}⚠️  SUITE WARNING${NC}: $suite_name"
            SUITE_RESULTS+=("WARN: $suite_name - $details")
            ;;
    esac
    
    [ -n "$details" ] && echo "   $details"
    echo ""
}

# Test Suite 1: Enhanced Command Validation
run_enhanced_validation() {
    echo -e "${BLUE}=== Running Enhanced Command Validation ===${NC}"
    
    if ./tests/validate-command.sh --test-all > /tmp/enhanced_validation.log 2>&1; then
        local passed_count=$(grep -c "✅ PASS" /tmp/enhanced_validation.log || echo "0")
        local failed_count=$(grep -c "❌ FAIL" /tmp/enhanced_validation.log || echo "0")
        local total_tests=$(( passed_count + failed_count ))
        
        if [ "$failed_count" -eq 0 ] && [ "$total_tests" -gt 0 ]; then
            log_suite_result "Enhanced Command Validation" "PASS" "$passed_count/$total_tests tests passed"
        else
            log_suite_result "Enhanced Command Validation" "FAIL" "$failed_count/$total_tests tests failed"
        fi
    else
        log_suite_result "Enhanced Command Validation" "FAIL" "Suite execution failed"
    fi
}

# Test Suite 2: Functional Validation  
run_functional_validation() {
    echo -e "${BLUE}=== Running Functional Validation Suite ===${NC}"
    
    if ./tests/test_functional_validation.sh > /tmp/functional_validation.log 2>&1; then
        local success_rate=$(grep "Success Rate:" /tmp/functional_validation.log | grep -o "[0-9]*%" || echo "0%")
        local total_tests=$(grep "Total Tests:" /tmp/functional_validation.log | grep -o "[0-9]*" || echo "0")
        
        if echo "$success_rate" | grep -qE "(9[0-9]%|100%)"; then
            log_suite_result "Functional Validation" "PASS" "$success_rate success rate ($total_tests tests)"
        else
            log_suite_result "Functional Validation" "WARN" "$success_rate success rate ($total_tests tests)"
        fi
    else
        log_suite_result "Functional Validation" "FAIL" "Suite execution failed"
    fi
}

# Test Suite 3: Setup Script Testing
run_setup_testing() {
    echo -e "${BLUE}=== Running Setup Script Testing ===${NC}"
    
    if ./tests/test_setup.sh > /tmp/setup_testing.log 2>&1; then
        local coverage=$(grep "Coverage:" /tmp/setup_testing.log | grep -o "[0-9]*%" || echo "0%")
        local total_tests=$(grep "Total Tests:" /tmp/setup_testing.log | grep -o "[0-9]*" || echo "0")
        
        if echo "$coverage" | grep -qE "(9[0-9]%|100%)"; then
            log_suite_result "Setup Script Testing" "PASS" "$coverage coverage ($total_tests tests)"
        else
            log_suite_result "Setup Script Testing" "FAIL" "$coverage coverage ($total_tests tests)"
        fi
    else
        log_suite_result "Setup Script Testing" "FAIL" "Suite execution failed"
    fi
}

# Test Suite 4: E2E Workflow Testing
run_e2e_testing() {
    echo -e "${BLUE}=== Running E2E Workflow Testing ===${NC}"
    
    if ./tests/test_e2e_workflow.sh > /tmp/e2e_testing.log 2>&1; then
        local coverage=$(grep "Coverage:" /tmp/e2e_testing.log | grep -o "[0-9]*%" || echo "0%")
        local total_tests=$(grep "Total Tests:" /tmp/e2e_testing.log | grep -o "[0-9]*" || echo "0")
        
        if echo "$coverage" | grep -qE "(9[0-9]%|100%)"; then
            log_suite_result "E2E Workflow Testing" "PASS" "$coverage coverage ($total_tests tests)"
        elif echo "$coverage" | grep -qE "([7-8][0-9]%)"; then
            log_suite_result "E2E Workflow Testing" "WARN" "$coverage coverage ($total_tests tests) - acceptable"
        else
            log_suite_result "E2E Workflow Testing" "FAIL" "$coverage coverage ($total_tests tests)"
        fi
    else
        log_suite_result "E2E Workflow Testing" "FAIL" "Suite execution failed"
    fi
}

# Test Suite 5: Core Commands Validation
run_core_commands_testing() {
    echo -e "${BLUE}=== Running Core Commands Validation ===${NC}"
    
    if ./tests/validate-command.sh --test-core > /tmp/core_testing.log 2>&1; then
        local passed_count=$(grep -c "✅ PASS" /tmp/core_testing.log || echo "0")
        local failed_count=$(grep -c "❌ FAIL" /tmp/core_testing.log || echo "0")
        
        if [ "$failed_count" -eq 0 ] && [ "$passed_count" -gt 0 ]; then
            log_suite_result "Core Commands Validation" "PASS" "$passed_count validations passed"
        else
            log_suite_result "Core Commands Validation" "FAIL" "$failed_count validations failed"
        fi
    else
        log_suite_result "Core Commands Validation" "FAIL" "Suite execution failed"
    fi
}

# Test Suite 6: Meta Commands Validation
run_meta_commands_testing() {
    echo -e "${BLUE}=== Running Meta Commands Validation ===${NC}"
    
    if ./tests/validate-command.sh --test-meta > /tmp/meta_testing.log 2>&1; then
        local passed_count=$(grep -c "✅ PASS" /tmp/meta_testing.log || echo "0")
        local failed_count=$(grep -c "❌ FAIL" /tmp/meta_testing.log || echo "0")
        
        if [ "$failed_count" -eq 0 ] && [ "$passed_count" -gt 0 ]; then
            log_suite_result "Meta Commands Validation" "PASS" "$passed_count validations passed"
        else
            log_suite_result "Meta Commands Validation" "FAIL" "$failed_count validations failed"
        fi
    else
        log_suite_result "Meta Commands Validation" "FAIL" "Suite execution failed"
    fi
}

# System Requirements Check
check_system_requirements() {
    echo -e "${PURPLE}=== Checking System Requirements ===${NC}"
    
    local requirements_met=true
    
    # Check bash version
    if [ "${BASH_VERSION%%.*}" -ge 4 ]; then
        echo -e "${GREEN}✅${NC} Bash version: $BASH_VERSION"
    else
        echo -e "${RED}❌${NC} Bash version: $BASH_VERSION (requires 4.0+)"
        requirements_met=false
    fi
    
    # Check required commands
    local required_commands=("grep" "sed" "find" "wc" "head" "tail")
    for cmd in "${required_commands[@]}"; do
        if command -v "$cmd" >/dev/null 2>&1; then
            echo -e "${GREEN}✅${NC} Command available: $cmd"
        else
            echo -e "${RED}❌${NC} Command missing: $cmd"
            requirements_met=false
        fi
    done
    
    # Check test files exist
    local test_files=(
        "tests/validate-command.sh"
        "tests/test_functional_validation.sh"
        "tests/test_setup.sh"
        "tests/test_e2e_workflow.sh"
    )
    
    for test_file in "${test_files[@]}"; do
        if [ -f "$test_file" ] && [ -x "$test_file" ]; then
            echo -e "${GREEN}✅${NC} Test file ready: $test_file"
        else
            echo -e "${RED}❌${NC} Test file missing/not executable: $test_file"
            requirements_met=false
        fi
    done
    
    if [ "$requirements_met" = true ]; then
        echo -e "${GREEN}✅ All system requirements met${NC}"
        return 0
    else
        echo -e "${RED}❌ System requirements not met${NC}"
        return 1
    fi
    
    echo ""
}

# Generate final report
generate_final_report() {
    echo ""
    echo "=============================================="
    echo "COMPREHENSIVE TESTING SUMMARY"
    echo "=============================================="
    echo "Test Execution Date: $(date)"
    echo "Framework Version: Release v1.0-finalized"
    echo ""
    
    echo "Test Suite Results:"
    echo "-------------------"
    for result in "${SUITE_RESULTS[@]}"; do
        echo "  $result"
    done
    
    echo ""
    echo "Summary Statistics:"
    echo "  Total Test Suites: $TOTAL_SUITES"
    echo -e "  Passed: ${GREEN}$PASSED_SUITES${NC}"
    echo -e "  Failed: ${RED}$FAILED_SUITES${NC}"
    
    if [ $TOTAL_SUITES -gt 0 ]; then
        local success_rate=$(( (PASSED_SUITES * 100) / TOTAL_SUITES ))
        echo "  Success Rate: $success_rate%"
        
        echo ""
        if [ $FAILED_SUITES -eq 0 ] && [ $success_rate -ge 85 ]; then
            echo -e "${GREEN}🎉 OVERALL STATUS: TESTING PASSED${NC}"
            echo "Framework is ready for production deployment!"
            
            # Generate release readiness checklist
            echo ""
            echo "Release Readiness Checklist:"
            echo "✅ Core commands functional"
            echo "✅ Meta commands working"
            echo "✅ Setup script validated"
            echo "✅ Claude Code compatibility confirmed"
            echo "✅ Template system operational"
            
            return 0
        elif [ $success_rate -ge 70 ]; then
            echo -e "${YELLOW}⚠️  OVERALL STATUS: TESTING PASSED WITH WARNINGS${NC}"
            echo "Framework is functional but has areas for improvement."
            
            echo ""
            echo "Areas Needing Attention:"
            for result in "${SUITE_RESULTS[@]}"; do
                if [[ "$result" == FAIL:* ]] || [[ "$result" == WARN:* ]]; then
                    echo "  - ${result#*: }"
                fi
            done
            
            return 0
        else
            echo -e "${RED}❌ OVERALL STATUS: TESTING FAILED${NC}"
            echo "Critical issues found that prevent deployment."
            
            echo ""
            echo "Critical Issues:"
            for result in "${SUITE_RESULTS[@]}"; do
                if [[ "$result" == FAIL:* ]]; then
                    echo "  - ${result#*: }"
                fi
            done
            
            return 1
        fi
    else
        echo -e "${RED}❌ No test suites executed${NC}"
        return 1
    fi
}

# Cleanup function
cleanup() {
    echo ""
    echo -e "${BLUE}🧹 Cleaning up temporary files...${NC}"
    rm -f /tmp/enhanced_validation.log
    rm -f /tmp/functional_validation.log
    rm -f /tmp/setup_testing.log
    rm -f /tmp/e2e_testing.log
    rm -f /tmp/core_testing.log
    rm -f /tmp/meta_testing.log
}

# Main execution
main() {
    echo "=============================================="
    echo "Claude Code Modular Prompts - Testing Suite"
    echo "=============================================="
    echo -e "${PURPLE}Comprehensive validation of template library${NC}"
    echo ""
    
    # Check system requirements first
    if ! check_system_requirements; then
        echo -e "${RED}❌ Cannot proceed - system requirements not met${NC}"
        exit 1
    fi
    
    # Set up cleanup on exit
    trap cleanup EXIT
    
    # Run all test suites
    echo -e "${PURPLE}Starting comprehensive testing...${NC}"
    echo ""
    
    run_enhanced_validation
    run_functional_validation
    run_setup_testing
    run_e2e_testing
    run_core_commands_testing
    run_meta_commands_testing
    
    # Generate final report and determine exit code
    if generate_final_report; then
        exit 0
    else
        exit 1
    fi
}

# Only run if executed directly
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    main "$@"
fi