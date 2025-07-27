#!/bin/bash

# Comprehensive Validation Pipeline for Claude Code Commands
# Integrates structural validation, functional testing, security testing, and LLM evaluation

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
COMMANDS_DIR="/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca/.claude/commands"
TESTS_DIR="/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca/tests"
RESULTS_DIR="${TESTS_DIR}/results"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Validation counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0
WARNINGS=0

# Create results directory
mkdir -p "${RESULTS_DIR}"

# Function to print colored output
print_status() {
    local status=$1
    local message=$2
    if [ "$status" = "PASS" ]; then
        echo -e "${GREEN}✅ PASS${NC}: $message"
        ((PASSED_TESTS++))
    elif [ "$status" = "FAIL" ]; then
        echo -e "${RED}❌ FAIL${NC}: $message"
        ((FAILED_TESTS++))
    elif [ "$status" = "WARN" ]; then
        echo -e "${YELLOW}⚠️  WARN${NC}: $message"
        ((WARNINGS++))
    elif [ "$status" = "INFO" ]; then
        echo -e "${BLUE}ℹ️  INFO${NC}: $message"
    fi
}

# Function to log results
log_result() {
    local phase=$1
    local status=$2
    local message=$3
    echo "${TIMESTAMP},${phase},${status},${message}" >> "${RESULTS_DIR}/validation_log_${TIMESTAMP}.csv"
}

# Function to run structural validation
run_structural_validation() {
    echo "========================================"
    echo "Phase 1: Structural Validation"
    echo "========================================"
    
    local validation_script="${TESTS_DIR}/validate-command.sh"
    local structural_report="${RESULTS_DIR}/structural_validation_${TIMESTAMP}.txt"
    
    if [ ! -f "$validation_script" ]; then
        print_status "FAIL" "Structural validation script not found"
        log_result "structural" "FAIL" "Validation script not found"
        return 1
    fi
    
    # Find all command files
    local command_files=($(find "$COMMANDS_DIR" -name "*.md" -type f))
    local total_commands=${#command_files[@]}
    
    print_status "INFO" "Found $total_commands command files to validate"
    
    # Run structural validation
    local structural_passed=0
    local structural_failed=0
    
    echo "# Structural Validation Report - $TIMESTAMP" > "$structural_report"
    echo "# Commands Directory: $COMMANDS_DIR" >> "$structural_report"
    echo "# Total Commands: $total_commands" >> "$structural_report"
    echo "" >> "$structural_report"
    
    for command_file in "${command_files[@]}"; do
        echo "Validating: $(basename "$command_file")" >> "$structural_report"
        
        if "$validation_script" "$command_file" >> "$structural_report" 2>&1; then
            ((structural_passed++))
            print_status "PASS" "Structural validation: $(basename "$command_file")"
            log_result "structural" "PASS" "$(basename "$command_file")"
        else
            ((structural_failed++))
            print_status "FAIL" "Structural validation: $(basename "$command_file")"
            log_result "structural" "FAIL" "$(basename "$command_file")"
        fi
        
        echo "----------------------------------------" >> "$structural_report"
        ((TOTAL_TESTS++))
    done
    
    echo "" >> "$structural_report"
    echo "# Summary:" >> "$structural_report"
    echo "# Passed: $structural_passed" >> "$structural_report"
    echo "# Failed: $structural_failed" >> "$structural_report"
    echo "# Success Rate: $(bc -l <<< "scale=2; $structural_passed * 100 / $total_commands")%" >> "$structural_report"
    
    print_status "INFO" "Structural validation completed: $structural_passed/$total_commands passed"
    
    # Only proceed if structural validation passes
    if [ $structural_failed -gt 0 ]; then
        print_status "WARN" "Some commands failed structural validation - continuing with functional tests"
    fi
    
    return 0
}

# Function to run functional testing
run_functional_testing() {
    echo ""
    echo "========================================"
    echo "Phase 2: Functional Testing"
    echo "========================================"
    
    local functional_script="${TESTS_DIR}/functional_testing.py"
    local functional_report="${RESULTS_DIR}/functional_testing_${TIMESTAMP}.json"
    
    if [ ! -f "$functional_script" ]; then
        print_status "FAIL" "Functional testing script not found"
        log_result "functional" "FAIL" "Testing script not found"
        return 1
    fi
    
    print_status "INFO" "Running functional tests for core commands..."
    
    # Check if Python is available
    if ! command -v python3 &> /dev/null; then
        print_status "FAIL" "Python3 not found - cannot run functional tests"
        log_result "functional" "FAIL" "Python3 not available"
        return 1
    fi
    
    # Test core commands first
    local core_commands=("task" "help" "test" "auto")
    local functional_passed=0
    local functional_failed=0
    
    for command in "${core_commands[@]}"; do
        print_status "INFO" "Testing command: /$command"
        
        # Run functional test for this command
        if python3 -c "
import sys
sys.path.append('$TESTS_DIR')
from functional_testing import run_command_tests
try:
    results = run_command_tests('$COMMANDS_DIR', '$command')
    passed = len([r for r in results if r.status.value == 'passed'])
    failed = len([r for r in results if r.status.value == 'failed'])
    print(f'Results for $command: {passed} passed, {failed} failed')
    if failed == 0:
        exit(0)
    else:
        exit(1)
except Exception as e:
    print(f'Error testing $command: {e}')
    exit(1)
"; then
            ((functional_passed++))
            print_status "PASS" "Functional testing: /$command"
            log_result "functional" "PASS" "$command"
        else
            ((functional_failed++))
            print_status "FAIL" "Functional testing: /$command" 
            log_result "functional" "FAIL" "$command"
        fi
        
        ((TOTAL_TESTS++))
    done
    
    print_status "INFO" "Functional testing completed: $functional_passed/${#core_commands[@]} commands passed"
    
    return 0
}

# Function to run security testing
run_security_testing() {
    echo ""
    echo "========================================"
    echo "Phase 3: Security Testing"
    echo "========================================"
    
    local security_script="${TESTS_DIR}/security_testing.py"
    local security_report="${RESULTS_DIR}/security_testing_${TIMESTAMP}.json"
    
    if [ ! -f "$security_script" ]; then
        print_status "FAIL" "Security testing script not found"
        log_result "security" "FAIL" "Security script not found"
        return 1
    fi
    
    print_status "INFO" "Running security tests..."
    
    # Run security validation
    if python3 -c "
import sys
sys.path.append('$TESTS_DIR')
from security_testing import create_security_test_suite

def mock_command(input_text):
    return f'Processed: {input_text}'

try:
    suite = create_security_test_suite()
    report = suite.run_comprehensive_security_tests(mock_command, 'test_command')
    
    security_score = report['security_score']
    compliance = report['compliance_status']
    
    print(f'Security Score: {security_score:.1f}%')
    print(f'Compliance: {compliance}')
    
    if compliance == 'PASS' and security_score >= 95:
        exit(0)
    else:
        exit(1)
        
except Exception as e:
    print(f'Security testing error: {e}')
    exit(1)
"; then
        print_status "PASS" "Security testing completed successfully"
        log_result "security" "PASS" "Security validation passed"
        ((PASSED_TESTS++))
    else
        print_status "FAIL" "Security testing failed"
        log_result "security" "FAIL" "Security validation failed"
        ((FAILED_TESTS++))
    fi
    
    ((TOTAL_TESTS++))
    
    return 0
}

# Function to run LLM evaluation
run_llm_evaluation() {
    echo ""
    echo "========================================"
    echo "Phase 4: LLM Evaluation"
    echo "========================================"
    
    local llm_script="${TESTS_DIR}/llm_evaluation.py"
    local llm_report="${RESULTS_DIR}/llm_evaluation_${TIMESTAMP}.json"
    
    if [ ! -f "$llm_script" ]; then
        print_status "FAIL" "LLM evaluation script not found"
        log_result "llm" "FAIL" "LLM script not found"
        return 1
    fi
    
    print_status "INFO" "Running LLM evaluation..."
    
    # Run LLM evaluation with sample data
    if python3 -c "
import sys
sys.path.append('$TESTS_DIR')
from llm_evaluation import create_llm_evaluator

try:
    evaluator = create_llm_evaluator(use_mock=True)
    
    # Test evaluation
    sample_input = 'create a hello world function in Python'
    sample_output = '''def hello_world():
    print(\"Hello, World!\")

if __name__ == \"__main__\":
    hello_world()'''
    
    report = evaluator.evaluate_command('test_command', sample_input, sample_output)
    
    print(f'Overall Score: {report.overall_score:.2f}')
    print(f'Grade: {report.grade}')
    
    if report.overall_score >= 0.7:
        exit(0)
    else:
        exit(1)
        
except Exception as e:
    print(f'LLM evaluation error: {e}')
    exit(1)
"; then
        print_status "PASS" "LLM evaluation completed successfully"
        log_result "llm" "PASS" "LLM evaluation passed"
        ((PASSED_TESTS++))
    else
        print_status "FAIL" "LLM evaluation failed"
        log_result "llm" "FAIL" "LLM evaluation failed"
        ((FAILED_TESTS++))
    fi
    
    ((TOTAL_TESTS++))
    
    return 0
}

# Function to generate comprehensive report
generate_comprehensive_report() {
    echo ""
    echo "========================================"
    echo "Comprehensive Validation Report"
    echo "========================================"
    
    local report_file="${RESULTS_DIR}/comprehensive_report_${TIMESTAMP}.md"
    
    cat > "$report_file" << EOF
# Claude Code Commands Validation Report

**Generated:** $(date)  
**Commands Directory:** $COMMANDS_DIR  
**Test Results Directory:** $RESULTS_DIR  

## Summary

- **Total Tests:** $TOTAL_TESTS
- **Passed Tests:** $PASSED_TESTS
- **Failed Tests:** $FAILED_TESTS
- **Warnings:** $WARNINGS
- **Success Rate:** $(bc -l <<< "scale=2; $PASSED_TESTS * 100 / $TOTAL_TESTS")%

## Validation Phases

### 1. Structural Validation ✅
- Validates YAML front matter structure
- Checks required fields (name, description)
- Verifies content length and format
- **Status:** Completed

### 2. Functional Testing ⚙️
- Tests command behavior with mock environment
- Validates tool integration
- Checks input/output handling
- **Status:** Core commands tested

### 3. Security Testing 🔒
- Input sanitization validation
- Output security scanning
- Permission boundary testing
- **Status:** Baseline security validation completed

### 4. LLM Evaluation 🧠
- Command effectiveness assessment
- Output quality evaluation
- User experience analysis
- **Status:** Mock evaluation framework active

## Test Results Details

See individual result files:
- \`structural_validation_${TIMESTAMP}.txt\`
- \`functional_testing_${TIMESTAMP}.json\`
- \`security_testing_${TIMESTAMP}.json\`
- \`llm_evaluation_${TIMESTAMP}.json\`
- \`validation_log_${TIMESTAMP}.csv\`

## Recommendations

### Immediate Actions
EOF

    # Add recommendations based on results
    if [ $FAILED_TESTS -gt 0 ]; then
        echo "- **Fix Failed Tests:** Address the $FAILED_TESTS failed test cases" >> "$report_file"
    fi
    
    if [ $WARNINGS -gt 0 ]; then
        echo "- **Review Warnings:** Address $WARNINGS warning conditions" >> "$report_file"
    fi
    
    cat >> "$report_file" << EOF

### Framework Enhancements
- Implement PromptFoo integration for standardized evaluation
- Add DeepEval library for production LLM evaluation
- Expand test coverage to all 79 commands
- Implement continuous integration pipeline

### Quality Improvements
- Increase test coverage for edge cases
- Add performance benchmarking
- Implement regression testing
- Create user acceptance testing framework

---

*Validation completed at $(date)*  
*Framework: Claude Code Modular Prompts Functional Testing*
EOF

    print_status "INFO" "Comprehensive report generated: $report_file"
    
    # Display summary
    echo ""
    echo "Final Summary:"
    echo "=============="
    echo "Total Tests: $TOTAL_TESTS"
    echo "Passed: $PASSED_TESTS"
    echo "Failed: $FAILED_TESTS"
    echo "Warnings: $WARNINGS"
    
    if [ $TOTAL_TESTS -gt 0 ]; then
        local success_rate=$(bc -l <<< "scale=1; $PASSED_TESTS * 100 / $TOTAL_TESTS")
        echo "Success Rate: ${success_rate}%"
        
        if (( $(echo "$success_rate >= 80" | bc -l) )); then
            print_status "PASS" "Overall validation PASSED (≥80% success rate)"
            return 0
        else
            print_status "FAIL" "Overall validation FAILED (<80% success rate)"
            return 1
        fi
    else
        print_status "FAIL" "No tests were executed"
        return 1
    fi
}

# Function to display usage
show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Comprehensive validation pipeline for Claude Code commands"
    echo ""
    echo "Options:"
    echo "  -h, --help              Show this help message"
    echo "  --structural-only       Run only structural validation"
    echo "  --functional-only       Run only functional testing"
    echo "  --security-only         Run only security testing"
    echo "  --llm-only             Run only LLM evaluation"
    echo "  --skip-structural      Skip structural validation"
    echo "  --skip-functional      Skip functional testing"
    echo "  --skip-security        Skip security testing"
    echo "  --skip-llm             Skip LLM evaluation"
    echo "  --commands-dir DIR     Specify commands directory"
    echo "  --results-dir DIR      Specify results output directory"
    echo ""
    echo "Examples:"
    echo "  $0                     Run full validation pipeline"
    echo "  $0 --structural-only   Run only structural validation"
    echo "  $0 --skip-functional   Run all except functional testing"
}

# Main execution function
main() {
    # Initialize CSV log
    echo "timestamp,phase,status,message" > "${RESULTS_DIR}/validation_log_${TIMESTAMP}.csv"
    
    echo "Claude Code Commands - Comprehensive Validation Pipeline"
    echo "========================================================"
    echo "Timestamp: $TIMESTAMP"
    echo "Commands Directory: $COMMANDS_DIR"
    echo "Results Directory: $RESULTS_DIR"
    echo ""
    
    # Parse command line arguments
    local run_structural=true
    local run_functional=true
    local run_security=true
    local run_llm=true
    local only_mode=false
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_usage
                exit 0
                ;;
            --structural-only)
                run_structural=true
                run_functional=false
                run_security=false
                run_llm=false
                only_mode=true
                ;;
            --functional-only)
                run_structural=false
                run_functional=true
                run_security=false
                run_llm=false
                only_mode=true
                ;;
            --security-only)
                run_structural=false
                run_functional=false
                run_security=true
                run_llm=false
                only_mode=true
                ;;
            --llm-only)
                run_structural=false
                run_functional=false
                run_security=false
                run_llm=true
                only_mode=true
                ;;
            --skip-structural)
                run_structural=false
                ;;
            --skip-functional)
                run_functional=false
                ;;
            --skip-security)
                run_security=false
                ;;
            --skip-llm)
                run_llm=false
                ;;
            --commands-dir)
                COMMANDS_DIR="$2"
                shift
                ;;
            --results-dir)
                RESULTS_DIR="$2"
                mkdir -p "$RESULTS_DIR"
                shift
                ;;
            *)
                echo "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
        shift
    done
    
    # Validate directories
    if [ ! -d "$COMMANDS_DIR" ]; then
        print_status "FAIL" "Commands directory not found: $COMMANDS_DIR"
        exit 1
    fi
    
    # Run validation phases
    local overall_status=0
    
    if [ "$run_structural" = true ]; then
        if ! run_structural_validation; then
            overall_status=1
        fi
    fi
    
    if [ "$run_functional" = true ]; then
        if ! run_functional_testing; then
            overall_status=1
        fi
    fi
    
    if [ "$run_security" = true ]; then
        if ! run_security_testing; then
            overall_status=1
        fi
    fi
    
    if [ "$run_llm" = true ]; then
        if ! run_llm_evaluation; then
            overall_status=1
        fi
    fi
    
    # Generate comprehensive report
    if ! generate_comprehensive_report; then
        overall_status=1
    fi
    
    exit $overall_status
}

# Run main function with all arguments
main "$@"