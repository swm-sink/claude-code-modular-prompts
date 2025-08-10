#!/bin/bash

# Claude Code Command Testing Framework
# Tests command structure, quality, and functionality

# Don't exit on error to see all test results

# Simple output markers (no colors for better compatibility)
PASS="✓"
WARN="⚠"
FAIL="✗"

COMMANDS_DIR=".claude/commands"
ERRORS=0
WARNINGS=0
PASSED=0

echo "========================================="
echo "Claude Code Command Testing Suite"
echo "========================================="
echo ""

# Test 1: YAML Frontmatter Validation
test_yaml_frontmatter() {
    local file=$1
    local basename=$(basename "$file")
    local test_passed=true
    
    echo -n "  Testing YAML: "
    
    # Required fields
    if ! grep -q "^name:" "$file"; then
        echo "$FAIL Missing 'name' field"
        ((ERRORS++))
        test_passed=false
    fi
    
    if ! grep -q "^description:" "$file"; then
        echo "$FAIL Missing 'description' field"
        ((ERRORS++))
        test_passed=false
    fi
    
    if ! grep -q "^usage:" "$file"; then
        echo "$WARN Missing 'usage' field"
        ((WARNINGS++))
    fi
    
    if ! grep -q "^allowed-tools:" "$file"; then
        echo "$WARN Missing 'allowed-tools' field"
        ((WARNINGS++))
    fi
    
    if [ "$test_passed" = true ]; then
        echo "$PASS All required fields present"
        ((PASSED++))
    fi
}

# Test 2: Line Count Compliance
test_line_count() {
    local file=$1
    local lines=$(wc -l < "$file")
    
    echo -n "  Line count: "
    
    if [ "$lines" -le 50 ]; then
        echo "$PASS $lines lines (optimal)"
        ((PASSED++))
    elif [ "$lines" -le 60 ]; then
        echo "$WARN $lines lines (acceptable)"
        ((WARNINGS++))
    else
        echo "$FAIL $lines lines (too long)"
        ((ERRORS++))
    fi
}

# Test 3: Anti-Pattern Detection
test_antipatterns() {
    local file=$1
    
    echo -n "  Anti-patterns: "
    
    # Check for XML pseudo-code (excluding usage examples)
    if grep -v "^usage:" "$file" | grep -v "<command>" | grep -v "<file>" | grep -q "<[a-z_]*>" 2>/dev/null; then
        echo "$FAIL Contains XML pseudo-code"
        ((ERRORS++))
    else
        echo "$PASS No XML pseudo-code detected"
        ((PASSED++))
    fi
}

# Test 4: Tool Usage Validation
test_tool_usage() {
    local file=$1
    
    echo -n "  Tool usage: "
    
    # Extract allowed tools
    local tools=$(grep "^allowed-tools:" "$file" | sed 's/allowed-tools: //')
    
    # Check if tools list is reasonable (not empty, not too many)
    local tool_count=$(echo "$tools" | tr ',' '\n' | wc -l)
    
    if [ "$tool_count" -eq 0 ]; then
        echo "$FAIL No tools declared"
        ((ERRORS++))
    elif [ "$tool_count" -gt 8 ]; then
        echo "$WARN Too many tools ($tool_count)"
        ((WARNINGS++))
    else
        echo "$PASS $tool_count tools declared"
        ((PASSED++))
    fi
}

# Test 5: Content Quality
test_content_quality() {
    local file=$1
    
    echo -n "  Content quality: "
    
    # Check for action-oriented language
    if grep -q "I'll\|I will\|Let me" "$file"; then
        echo "$PASS Action-oriented"
        ((PASSED++))
    else
        echo "$WARN May lack action orientation"
        ((WARNINGS++))
    fi
}

# Main testing loop
echo "Testing Commands:"
echo "-----------------"

for file in $COMMANDS_DIR/*.md $COMMANDS_DIR/*/*.md; do
    if [ -f "$file" ]; then
        echo ""
        echo "Testing: $(basename "$file")"
        test_yaml_frontmatter "$file"
        test_line_count "$file"
        test_antipatterns "$file"
        test_tool_usage "$file"
        test_content_quality "$file"
    fi
done

# Summary
echo ""
echo "========================================="
echo "Test Summary"
echo "========================================="
echo "Passed: $PASSED tests"
echo "Warnings: $WARNINGS"
echo "Errors: $ERRORS"
echo ""

if [ "$ERRORS" -eq 0 ]; then
    if [ "$WARNINGS" -eq 0 ]; then
        echo "$PASS All tests passed perfectly!"
    else
        echo "$WARN Tests passed with $WARNINGS warnings"
    fi
    exit 0
else
    echo "$FAIL Tests failed with $ERRORS errors"
    exit 1
fi