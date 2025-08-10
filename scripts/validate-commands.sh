#!/bin/bash

# Claude Code Command Validation Script
# Tests all commands for structural validity and best practices

set -e

COMMANDS_DIR=".claude/commands"
ERRORS=0
WARNINGS=0

echo "========================================="
echo "Claude Code Command Validation"
echo "========================================="
echo ""

# Function to validate YAML frontmatter
validate_yaml() {
    local file=$1
    local basename=$(basename "$file")
    
    echo "Validating: $basename"
    
    # Check for required YAML fields
    if ! grep -q "^name:" "$file"; then
        echo "  ❌ ERROR: Missing 'name' field"
        ((ERRORS++))
    fi
    
    if ! grep -q "^description:" "$file"; then
        echo "  ❌ ERROR: Missing 'description' field"
        ((ERRORS++))
    fi
    
    if ! grep -q "^usage:" "$file"; then
        echo "  ⚠️  WARNING: Missing 'usage' field"
        ((WARNINGS++))
    fi
    
    if ! grep -q "^allowed-tools:" "$file"; then
        echo "  ⚠️  WARNING: Missing 'allowed-tools' field"
        ((WARNINGS++))
    fi
    
    # Check line count (should be under 100, ideally 40-50)
    lines=$(wc -l < "$file")
    if [ "$lines" -gt 100 ]; then
        echo "  ❌ ERROR: Command has $lines lines (max: 100)"
        ((ERRORS++))
    elif [ "$lines" -gt 50 ]; then
        echo "  ⚠️  WARNING: Command has $lines lines (ideal: 40-50)"
        ((WARNINGS++))
    else
        echo "  ✅ Size: $lines lines"
    fi
    
    # Check for XML pseudo-code anti-pattern (exclude usage field and help placeholders)
    # Exclude common placeholder patterns like <command>, <file>, <args>
    if grep -v "^usage:" "$file" | grep -v "help <command>" | grep -v "<file>" | grep -v "<args>" | grep -q "<[a-z_]*>" 2>/dev/null; then
        echo "  ❌ ERROR: Contains XML pseudo-code"
        ((ERRORS++))
    fi
    
    echo ""
}

# Validate all command files
for file in $COMMANDS_DIR/*.md $COMMANDS_DIR/*/*.md; do
    if [ -f "$file" ]; then
        validate_yaml "$file"
    fi
done

# Summary
echo "========================================="
echo "Validation Summary"
echo "========================================="
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [ "$ERRORS" -eq 0 ]; then
    if [ "$WARNINGS" -eq 0 ]; then
        echo "✅ All commands pass validation!"
    else
        echo "⚠️  Commands pass with $WARNINGS warnings"
    fi
    exit 0
else
    echo "❌ Validation failed with $ERRORS errors"
    exit 1
fi