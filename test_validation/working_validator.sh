#!/bin/bash
# WORKING Configuration Validator
# Demonstrates FUNCTIONAL validation with error detection

validate_project_config() {
    local config_file="$1"
    local errors=0
    
    echo "=== VALIDATING: $config_file ==="
    
    # 1. XML Structure Validation
    if ! xmllint --noout "$config_file" 2>/dev/null; then
        echo "❌ FATAL: Invalid XML structure"
        return 1
    fi
    echo "✅ XML structure valid"
    
    # 2. Required Fields Validation
    if ! xmllint --xpath "//project_info/name/text()" "$config_file" >/dev/null 2>&1; then
        echo "❌ Missing required field: project_info/name"
        echo "💡 GUIDANCE: Add <name>Your Project Name</name> in project_info section"
        errors=$((errors + 1))
    else
        echo "✅ Project name found"
    fi
    
    if ! xmllint --xpath "//project_info/primary_language/text()" "$config_file" >/dev/null 2>&1; then
        echo "❌ Missing required field: project_info/primary_language"
        errors=$((errors + 1))
    else
        echo "✅ Primary language specified"
    fi
    
    # 3. Value Range Validation
    if xmllint --xpath "//test_coverage/threshold/text()" "$config_file" >/dev/null 2>&1; then
        coverage=$(xmllint --xpath "//test_coverage/threshold/text()" "$config_file" 2>/dev/null)
        if [ "$coverage" -gt 100 ] || [ "$coverage" -lt 0 ]; then
            echo "❌ Coverage threshold must be 0-100, got: $coverage"
            echo "💡 GUIDANCE: Set coverage threshold between 0-100. Recommended: 80% for new projects"
            errors=$((errors + 1))
        else
            echo "✅ Coverage threshold valid: $coverage%"
        fi
    fi
    
    # 4. Summary
    if [ $errors -eq 0 ]; then
        echo ""
        echo "✅ VALIDATION PASSED: Configuration is valid"
        return 0
    else
        echo ""
        echo "❌ VALIDATION FAILED: $errors errors found"
        return 1
    fi
}

# Test with valid config
echo "Testing valid configuration:"
validate_project_config "test_minimal_config.xml"

echo ""
echo "Testing broken configuration:"
validate_project_config "broken_config.xml"