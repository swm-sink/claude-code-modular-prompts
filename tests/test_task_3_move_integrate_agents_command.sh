#!/bin/bash

# Test Task #3: Move .claude/commands/integrate-agents.md to .archive-integration-approach/commands/
# RED Phase: This test should FAIL initially

set -e

echo "=== Testing Task #3: Move integrate-agents.md command ==="

# Test 1: Source file should NOT exist after move
echo "Test 1: Checking source file no longer exists..."
if [ -f ".claude/commands/integrate-agents.md" ]; then
    echo "❌ FAIL: Source file .claude/commands/integrate-agents.md still exists"
    exit 1
else
    echo "✅ PASS: Source file .claude/commands/integrate-agents.md no longer exists"
fi

# Test 2: Target file should exist after move
echo "Test 2: Checking target file exists..."
if [ -f ".archive-integration-approach/commands/integrate-agents.md" ]; then
    echo "✅ PASS: Target file .archive-integration-approach/commands/integrate-agents.md exists"
else
    echo "❌ FAIL: Target file .archive-integration-approach/commands/integrate-agents.md does not exist"
    exit 1
fi

# Test 3: Target file should have expected content structure
echo "Test 3: Checking target file has expected YAML frontmatter..."
if grep -q "^name: /integrate-agents$" ".archive-integration-approach/commands/integrate-agents.md"; then
    echo "✅ PASS: Target file contains expected YAML frontmatter (name: /integrate-agents)"
else
    echo "❌ FAIL: Target file missing expected YAML frontmatter"
    exit 1
fi

# Test 4: Target file should contain integration system content
echo "Test 4: Checking target file contains integration system content..."
if grep -q "Agent Integration System" ".archive-integration-approach/commands/integrate-agents.md"; then
    echo "✅ PASS: Target file contains Agent Integration System content"
else
    echo "❌ FAIL: Target file missing Agent Integration System content"
    exit 1
fi

# Test 5: File permissions should be preserved
echo "Test 5: Checking file permissions are preserved..."
if [ -r ".archive-integration-approach/commands/integrate-agents.md" ]; then
    echo "✅ PASS: Target file has read permissions"
else
    echo "❌ FAIL: Target file missing read permissions"
    exit 1
fi

echo "=== All tests passed for Task #3 ==="