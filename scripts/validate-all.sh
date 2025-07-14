#!/bin/bash

# Comprehensive validation script that runs all framework validators

echo "🔍 Starting comprehensive framework validation..."
echo "=============================================="

# Track errors
ERRORS=0

# 1. Reference validation
echo -e "\n📚 Validating cross-references..."
if python scripts/validate-references.py; then
    echo "✅ Reference validation passed"
else
    echo "❌ Reference validation failed"
    ERRORS=$((ERRORS + 1))
fi

# 2. Structure validation
echo -e "\n🏗️ Validating directory structure..."
if python scripts/verify-structure.py; then
    echo "✅ Structure validation passed"
else
    echo "❌ Structure validation failed"
    ERRORS=$((ERRORS + 1))
fi

# 3. Module validation (if exists)
if [ -f "scripts/validate-modules.py" ]; then
    echo -e "\n📦 Validating modules..."
    if python scripts/validate-modules.py; then
        echo "✅ Module validation passed"
    else
        echo "❌ Module validation failed"
        ERRORS=$((ERRORS + 1))
    fi
fi

# 4. Command validation (if exists)
if [ -f "scripts/validate-commands.py" ]; then
    echo -e "\n🎯 Validating commands..."
    if python scripts/validate-commands.py; then
        echo "✅ Command validation passed"
    else
        echo "❌ Command validation failed"
        ERRORS=$((ERRORS + 1))
    fi
fi

# Summary
echo -e "\n=============================================="
if [ $ERRORS -eq 0 ]; then
    echo "✅ All validations passed successfully!"
    exit 0
else
    echo "❌ $ERRORS validation(s) failed"
    echo "Please review the errors above and fix them."
    exit 1
fi