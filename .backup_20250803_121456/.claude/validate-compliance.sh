#!/bin/bash
# Claude Code Compliance Validation for CI/CD
# 
# This script runs the master compliance validator and is designed 
# for integration into CI/CD pipelines.
#
# Exit codes:
#   0: All validations passed
#   1: Validation failures found  
#   2: Script error

set -e

echo "🔍 Claude Code Compliance Check"
echo "==============================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 2
fi

# Check if the validator script exists
VALIDATOR_SCRIPT=".claude/master-compliance-validator.py"
if [ ! -f "$VALIDATOR_SCRIPT" ]; then
    echo "❌ Compliance validator script not found: $VALIDATOR_SCRIPT"
    exit 2
fi

# Run the validation
echo "Running comprehensive compliance validation..."
python3 "$VALIDATOR_SCRIPT" --verbose

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS: All compliance checks passed"
    echo "🎉 Claude Code template library maintains 100% compliance"
elif [ $EXIT_CODE -eq 1 ]; then
    echo ""
    echo "❌ FAILURE: Compliance issues detected"
    echo "📋 Please review the validation report above and fix the issues"
    echo "💡 Run the validator locally to see detailed issue descriptions"
else
    echo ""
    echo "❌ ERROR: Validation script encountered an error"
fi

exit $EXIT_CODE