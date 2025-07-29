#!/bin/bash

# Security Test Runner for Command Injection Prevention
# Tests all security patterns implemented in vulnerable commands

set -e

echo "🔒 Claude Code Modular Prompts - Security Test Suite"
echo "=================================================="
echo "Testing command injection prevention for:"
echo "  - /dev command"
echo "  - /pipeline command" 
echo "  - /deploy command"
echo "  - /test-unit command"
echo ""

# Create results directory
mkdir -p tests/results

# Run Python security tests
echo "🐍 Running Python security tests..."
cd tests/security
python3 command_injection_prevention_tests.py

echo ""
echo "✅ Security tests completed!"
echo "📊 Check tests/results/ for detailed reports"