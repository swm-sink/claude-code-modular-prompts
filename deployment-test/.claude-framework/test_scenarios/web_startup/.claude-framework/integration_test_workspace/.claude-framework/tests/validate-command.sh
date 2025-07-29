#!/bin/bash

# Command Validation Script for Claude Code Modular Prompts
# Validates YAML front matter and basic structure requirements

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Validation counters
ERRORS=0
WARNINGS=0

# Function to print colored output
print_result() {
    local status=$1
    local message=$2
    if [ "$status" = "PASS" ]; then
        echo -e "${GREEN}✅ PASS${NC}: $message"
    elif [ "$status" = "FAIL" ]; then
        echo -e "${RED}❌ FAIL${NC}: $message"
        ((ERRORS++))
    elif [ "$status" = "WARN" ]; then
        echo -e "${YELLOW}⚠️  WARN${NC}: $message"
        ((WARNINGS++))
    fi
}

# Function to validate YAML front matter
validate_yaml_frontmatter() {
    local file=$1
    
    # Check if file starts with YAML front matter
    if ! head -1 "$file" | grep -q "^---$"; then
        print_result "FAIL" "Missing YAML front matter delimiter at start"
        return 1
    fi
    
    # Find the closing YAML delimiter
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    if [ -z "$yaml_end" ]; then
        print_result "FAIL" "Missing closing YAML front matter delimiter"
        return 1
    fi
    
    print_result "PASS" "YAML front matter structure valid"
    return 0
}

# Function to extract YAML content
extract_yaml_content() {
    local file=$1
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    
    if [ -n "$yaml_end" ]; then
        sed -n "2,$((yaml_end-1))p" "$file"
    fi
}

# Function to validate required fields
validate_required_fields() {
    local file=$1
    local yaml_content=$(extract_yaml_content "$file")
    
    # Check for required fields
    local required_fields=("name" "description")
    
    for field in "${required_fields[@]}"; do
        if echo "$yaml_content" | grep -q "^${field}:"; then
            print_result "PASS" "Required field '$field' present"
        else
            print_result "FAIL" "Missing required field: $field"
        fi
    done
}

# Function to validate optional fields and provide suggestions
validate_optional_fields() {
    local file=$1
    local yaml_content=$(extract_yaml_content "$file")
    
    # Check for helpful optional fields
    local optional_fields=("usage" "tools" "category")
    
    for field in "${optional_fields[@]}"; do
        if echo "$yaml_content" | grep -q "^${field}:"; then
            print_result "PASS" "Optional field '$field' present"
        else
            print_result "WARN" "Optional field '$field' missing (recommended)"
        fi
    done
}

# Function to validate content length
validate_content_length() {
    local file=$1
    local yaml_end=$(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)
    
    if [ -n "$yaml_end" ]; then
        local content_lines=$(tail -n +$((yaml_end+1)) "$file" | wc -l)
        local content_chars=$(tail -n +$((yaml_end+1)) "$file" | wc -c)
        
        if [ "$content_lines" -lt 3 ]; then
            print_result "FAIL" "Content too short: only $content_lines lines"
        elif [ "$content_chars" -lt 50 ]; then
            print_result "FAIL" "Content too short: only $content_chars characters"
        else
            print_result "PASS" "Content length adequate ($content_lines lines, $content_chars chars)"
        fi
    else
        print_result "FAIL" "Cannot validate content length - YAML structure invalid"
    fi
}

# Function to validate file basics
validate_file_basics() {
    local file=$1
    
    # Check if file exists
    if [ ! -f "$file" ]; then
        print_result "FAIL" "File does not exist: $file"
        return 1
    fi
    
    # Check if file is readable
    if [ ! -r "$file" ]; then
        print_result "FAIL" "File is not readable: $file"
        return 1
    fi
    
    # Check if file is not empty
    if [ ! -s "$file" ]; then
        print_result "FAIL" "File is empty: $file"
        return 1
    fi
    
    # Check file extension
    if [[ "$file" != *.md ]]; then
        print_result "WARN" "File does not have .md extension"
    fi
    
    print_result "PASS" "File basics valid"
    return 0
}

# Function to validate Claude Code slash command compatibility
validate_claude_code_compatibility() {
    local file=$1
    local yaml_content=$(extract_yaml_content "$file")
    
    # Check for valid slash command name
    local name_line=$(echo "$yaml_content" | grep "^name:")
    if [ -n "$name_line" ]; then
        local command_name=$(echo "$name_line" | sed 's/name: *//g' | tr -d '"')
        if [[ "$command_name" =~ ^/[a-zA-Z][a-zA-Z0-9-]*$ ]]; then
            print_result "PASS" "Valid slash command name: $command_name"
        else
            print_result "FAIL" "Invalid slash command name format: $command_name"
        fi
    fi
    
    # Check for allowed-tools field (Claude Code specific)
    if echo "$yaml_content" | grep -q "^allowed-tools:"; then
        print_result "PASS" "Claude Code allowed-tools field present"
    else
        print_result "WARN" "Missing allowed-tools field (Claude Code compatibility)"
    fi
    
    # Check for template placeholders (template commands)
    local content=$(tail -n +$(($(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)+1)) "$file")
    local placeholder_count=$(echo "$content" | grep -o "\[INSERT_[A-Z_]*\]" | wc -l)
    if [ "$placeholder_count" -gt 0 ]; then
        print_result "PASS" "Template command with $placeholder_count placeholders"
    else
        print_result "PASS" "Finalized command (no placeholders)"
    fi
}

# Function to test command prompt effectiveness
validate_prompt_effectiveness() {
    local file=$1
    local content=$(tail -n +$(($(grep -n "^---$" "$file" | sed -n '2p' | cut -d: -f1)+1)) "$file")
    
    # Check for clear instruction patterns
    if echo "$content" | grep -qi "you are\|I will\|I'll help\|help you"; then
        print_result "PASS" "Clear instruction pattern present"
    else
        print_result "WARN" "No clear instruction pattern found"
    fi
    
    # Check for specific context references
    if echo "$content" | grep -qi "project\|domain\|tech stack"; then
        print_result "PASS" "Context-aware prompt detected"
    else
        print_result "WARN" "Generic prompt - consider adding context awareness"
    fi
    
    # Check for structured approach
    if echo "$content" | grep -qE "##|\*\*|1\.|2\.|3\."; then
        print_result "PASS" "Structured approach with sections/steps"
    else
        print_result "WARN" "Consider adding structure to prompt"
    fi
}

# Main validation function
validate_command() {
    local file=$1
    
    echo "Validating: $file"
    echo "----------------------------------------"
    
    # Reset counters for this file
    ERRORS=0
    WARNINGS=0
    
    # Run all validations
    validate_file_basics "$file" || return 1
    validate_yaml_frontmatter "$file"
    validate_required_fields "$file"
    validate_optional_fields "$file"
    validate_content_length "$file"
    validate_claude_code_compatibility "$file"
    validate_prompt_effectiveness "$file"
    
    # Summary
    echo "----------------------------------------"
    if [ $ERRORS -eq 0 ]; then
        print_result "PASS" "File validation completed successfully"
        if [ $WARNINGS -gt 0 ]; then
            echo -e "${YELLOW}Warnings: $WARNINGS${NC}"
        fi
        return 0
    else
        print_result "FAIL" "File validation failed with $ERRORS errors"
        if [ $WARNINGS -gt 0 ]; then
            echo -e "${YELLOW}Warnings: $WARNINGS${NC}"
        fi
        return 1
    fi
}

# Function to run functional tests on commands
run_functional_tests() {
    local test_type="$1"
    shift
    local files=("$@")
    
    echo "Running functional tests ($test_type)..."
    echo "======================================="
    
    case "$test_type" in
        "core")
            echo "Testing core commands for essential functionality..."
            ;;
        "meta")
            echo "Testing meta/guide commands for adaptation workflow..."
            ;;
        "development")
            echo "Testing development workflow commands..."
            ;;
        *)
            echo "Testing general command functionality..."
            ;;
    esac
    
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            validate_command "$file"
            echo ""
        fi
    done
}

# Main script execution
main() {
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <command-file.md> [command-file2.md ...]"
        echo "       $0 --test-core     # Test core commands only"
        echo "       $0 --test-meta     # Test meta commands only"
        echo "       $0 --test-all      # Test all commands"
        echo ""
        echo "Validates Claude Code command files for:"
        echo "  - YAML front matter structure"
        echo "  - Required fields (name, description)"
        echo "  - Optional fields (usage, tools, category)"
        echo "  - Adequate content length"
        echo "  - Claude Code compatibility"
        echo "  - Prompt effectiveness"
        echo ""
        exit 1
    fi
    
    # Handle special test modes
    if [ "$1" = "--test-core" ]; then
        core_commands=(
            ".claude/commands/core/help.md"
            ".claude/commands/core/task.md"
            ".claude/commands/core/auto.md"
            ".claude/commands/core/project-task.md"
        )
        run_functional_tests "core" "${core_commands[@]}"
        return $?
    elif [ "$1" = "--test-meta" ]; then
        meta_commands=(
            ".claude/commands/meta/adapt-to-project.md"
            ".claude/commands/meta/validate-adaptation.md"
            ".claude/commands/meta/welcome.md"
            ".claude/commands/meta/sync-from-reference.md"
        )
        run_functional_tests "meta" "${meta_commands[@]}"
        return $?
    elif [ "$1" = "--test-all" ]; then
        all_commands=($(find .claude/commands -name "*.md" -not -path "*/deprecated/*" | head -64))
        run_functional_tests "all" "${all_commands[@]}"
        return $?
    fi
    
    local total_files=$#
    local passed_files=0
    local failed_files=0
    
    echo "Claude Code Command Validator"
    echo "============================="
    echo "Validating $total_files file(s)..."
    echo ""
    
    for file in "$@"; do
        if validate_command "$file"; then
            ((passed_files++))
        else
            ((failed_files++))
        fi
        echo ""
    done
    
    # Final summary
    echo "============================="
    echo "Enhanced Validation Summary:"
    echo "  Total files: $total_files"
    echo -e "  ${GREEN}Passed: $passed_files${NC}"
    if [ $failed_files -gt 0 ]; then
        echo -e "  ${RED}Failed: $failed_files${NC}"
        echo ""
        echo "Claude Code Compatibility: FAILED"
        echo "Some commands are not compatible with Claude Code slash command format."
        exit 1
    else
        echo "  Failed: 0"
        echo ""
        echo -e "${GREEN}Claude Code Compatibility: PASSED${NC}"
        echo -e "${GREEN}All commands validated for Claude Code usage!${NC}"
        exit 0
    fi
}

# Run main function with all arguments
main "$@"