#!/bin/bash

# Test Task #4: Move .claude/agents/context-engineer.md to .archive-integration-approach/agents/
# RED Phase: This test should FAIL initially

set -e

echo "=== Testing Task #4: Move context-engineer.md agent ==="

# Test 1: Source file should NOT exist after move
echo "Test 1: Checking source file no longer exists..."
if [ -f ".claude/agents/context-engineer.md" ]; then
    echo "❌ FAIL: Source file .claude/agents/context-engineer.md still exists"
    exit 1
else
    echo "✅ PASS: Source file .claude/agents/context-engineer.md no longer exists"
fi

# Test 2: Target file should exist after move
echo "Test 2: Checking target file exists..."
if [ -f ".archive-integration-approach/agents/context-engineer.md" ]; then
    echo "✅ PASS: Target file .archive-integration-approach/agents/context-engineer.md exists"
else
    echo "❌ FAIL: Target file .archive-integration-approach/agents/context-engineer.md does not exist"
    exit 1
fi

# Test 3: Target file should have expected agent header structure
echo "Test 3: Checking target file has expected agent header..."
if grep -q "^# Context Engineer Agent$" ".archive-integration-approach/agents/context-engineer.md"; then
    echo "✅ PASS: Target file contains expected agent header"
else
    echo "❌ FAIL: Target file missing expected agent header"
    exit 1
fi

# Test 4: Target file should contain agent specialization content
echo "Test 4: Checking target file contains agent specialization..."
if grep -q "## Agent Specialization" ".archive-integration-approach/agents/context-engineer.md"; then
    echo "✅ PASS: Target file contains Agent Specialization section"
else
    echo "❌ FAIL: Target file missing Agent Specialization section"
    exit 1
fi

# Test 5: Target file should contain 11-layer architecture content
echo "Test 5: Checking target file contains 11-layer architecture..."
if grep -q "11-layer Context Window Architecture" ".archive-integration-approach/agents/context-engineer.md"; then
    echo "✅ PASS: Target file contains 11-layer architecture content"
else
    echo "❌ FAIL: Target file missing 11-layer architecture content"
    exit 1
fi

# Test 6: File permissions should be preserved
echo "Test 6: Checking file permissions are preserved..."
if [ -r ".archive-integration-approach/agents/context-engineer.md" ]; then
    echo "✅ PASS: Target file has read permissions"
else
    echo "❌ FAIL: Target file missing read permissions"
    exit 1
fi

# Test 7: File should have substantial content (expect ~4-5KB based on actual size)
echo "Test 7: Checking file has expected content size..."
file_size=$(wc -c < ".archive-integration-approach/agents/context-engineer.md")
if [ "$file_size" -gt 3000 ]; then
    echo "✅ PASS: Target file has substantial content ($file_size bytes)"
else
    echo "❌ FAIL: Target file appears too small ($file_size bytes)"
    exit 1
fi

echo "=== All tests passed for Task #4 ==="