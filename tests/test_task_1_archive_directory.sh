#!/bin/bash
# TDD Test Suite: Task #1 - Archive Directory Structure Creation
# Purpose: Test creation of .archive-integration-approach/ directory structure

set -e
echo "=== Task #1 Archive Directory Structure - TDD Tests ==="

# Test 1: Main Archive Directory Exists
echo "Test 1: Main Archive Directory Creation"
if [ -d ".archive-integration-approach" ]; then
    echo "✅ PASS: Main archive directory exists"
else
    echo "❌ FAIL: Main archive directory missing"
    exit 1
fi

# Test 2: Commands Subdirectory Exists
echo "Test 2: Commands Subdirectory Creation"
if [ -d ".archive-integration-approach/commands" ]; then
    echo "✅ PASS: Commands subdirectory exists"
else
    echo "❌ FAIL: Commands subdirectory missing"
    exit 1
fi

# Test 3: Agents Subdirectory Exists
echo "Test 3: Agents Subdirectory Creation"
if [ -d ".archive-integration-approach/agents" ]; then
    echo "✅ PASS: Agents subdirectory exists"
else
    echo "❌ FAIL: Agents subdirectory missing"
    exit 1
fi

# Test 4: Scripts Subdirectory Exists
echo "Test 4: Scripts Subdirectory Creation"
if [ -d ".archive-integration-approach/scripts" ]; then
    echo "✅ PASS: Scripts subdirectory exists"
else
    echo "❌ FAIL: Scripts subdirectory missing"
    exit 1
fi

# Test 5: Tests Subdirectory Exists
echo "Test 5: Tests Subdirectory Creation"
if [ -d ".archive-integration-approach/tests" ]; then
    echo "✅ PASS: Tests subdirectory exists"
else
    echo "❌ FAIL: Tests subdirectory missing"
    exit 1
fi

# Test 6: LEARNING.md Documentation Exists
echo "Test 6: LEARNING.md Documentation"
if [ -f ".archive-integration-approach/LEARNING.md" ]; then
    echo "✅ PASS: LEARNING.md documentation exists"
else
    echo "❌ FAIL: LEARNING.md documentation missing"
    exit 1
fi

# Test 7: Directory Structure Integrity
echo "Test 7: Directory Structure Integrity"
EXPECTED_DIRS=(".archive-integration-approach" ".archive-integration-approach/commands" ".archive-integration-approach/agents" ".archive-integration-approach/scripts" ".archive-integration-approach/tests")
ALL_DIRS_EXIST=true

for dir in "${EXPECTED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "❌ FAIL: Missing directory: $dir"
        ALL_DIRS_EXIST=false
    fi
done

if [ "$ALL_DIRS_EXIST" = true ]; then
    echo "✅ PASS: All expected directories exist"
else
    echo "❌ FAIL: Directory structure incomplete"
    exit 1
fi

echo "=== Task #1 Archive Directory Structure - TDD Tests Complete ==="