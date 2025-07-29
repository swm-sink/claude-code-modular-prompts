#!/bin/bash

# Command Validation Script
# Validates all commands in .claude/commands for consistency

echo "🔍 Validating Claude Code Commands..."

ERRORS=0
TOTAL=0

# Function to validate a single command file
validate_command() {
    local file="$1"
    local errors=0
    
    echo "Checking: $(basename $file)"
    
    # Check YAML frontmatter exists
    if ! head -1 "$file" | grep -q "^---$"; then
        echo "  ❌ Missing YAML frontmatter"
        ((errors++))
    fi
    
    # Check required frontmatter fields
    if ! grep -q "^description:" "$file"; then
        echo "  ❌ Missing description field"
        ((errors++))
    fi
    
    if ! grep -q "^allowed-tools:" "$file"; then
        echo "  ❌ Missing allowed-tools field"
        ((errors++))
    fi
    
    # Check command name header exists
    if ! grep -q "^# /" "$file"; then
        echo "  ❌ Missing command name header (# /command-name)"
        ((errors++))
    fi
    
    # Check command_file XML structure exists
    if ! grep -q "<command_file>" "$file"; then
        echo "  ❌ Missing <command_file> XML structure"
        ((errors++))
    fi
    
    # Check claude_prompt section exists
    if ! grep -q "<claude_prompt>" "$file"; then
        echo "  ❌ Missing <claude_prompt> section"
        ((errors++))
    fi
    
    # Check for standard components
    if ! grep -q "input-validation.md" "$file"; then
        echo "  ⚠️  Missing standard input-validation component"
    fi
    
    if [ $errors -eq 0 ]; then
        echo "  ✅ Valid"
    else
        echo "  ❌ $errors errors found"
    fi
    
    return $errors
}

# Find all command files
echo "Scanning .claude/commands directory..."
echo ""

while IFS= read -r -d '' file; do
    if [[ $(basename "$file") != "README.md" ]]; then
        validate_command "$file"
        if [ $? -gt 0 ]; then
            ((ERRORS += $?))
        fi
        ((TOTAL++))
        echo ""
    fi
done < <(find .claude/commands -name "*.md" -print0)

# Summary
echo "📊 Validation Summary:"
echo "Total commands: $TOTAL"
echo "Commands with errors: $((TOTAL - (TOTAL - ERRORS)))"
echo "Total errors: $ERRORS"

if [ $ERRORS -eq 0 ]; then
    echo "✅ All commands are valid!"
    exit 0
else
    echo "❌ Validation failed with $ERRORS errors"
    exit 1
fi