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

# Main script execution
main() {
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <command-file.md> [command-file2.md ...]"
        echo ""
        echo "Validates Claude Code command files for:"
        echo "  - YAML front matter structure"
        echo "  - Required fields (name, description)"
        echo "  - Optional fields (usage, tools, category)"
        echo "  - Adequate content length"
        echo ""
        exit 1
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
    echo "Validation Summary:"
    echo "  Total files: $total_files"
    echo -e "  ${GREEN}Passed: $passed_files${NC}"
    if [ $failed_files -gt 0 ]; then
        echo -e "  ${RED}Failed: $failed_files${NC}"
        exit 1
    else
        echo "  Failed: 0"
        echo -e "${GREEN}All validations passed!${NC}"
        exit 0
    fi
}

# Run main function with all arguments
main "$@"