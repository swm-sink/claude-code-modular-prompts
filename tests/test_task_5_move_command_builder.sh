#!/bin/bash

# Test Task #5: Move .claude/agents/command-builder.md to .archive-integration-approach/agents/
# RED Phase: This test should FAIL initially

set -e

echo "=== Testing Task #5: Move command-builder.md agent ==="

# Test 1: Source file should NOT exist after move
echo "Test 1: Checking source file no longer exists..."
if [ -f ".claude/agents/command-builder.md" ]; then
    echo "❌ FAIL: Source file .claude/agents/command-builder.md still exists"
    exit 1
else
    echo "✅ PASS: Source file .claude/agents/command-builder.md no longer exists"
fi

# Test 2: Target file should exist after move
echo "Test 2: Checking target file exists..."
if [ -f ".archive-integration-approach/agents/command-builder.md" ]; then
    echo "✅ PASS: Target file .archive-integration-approach/agents/command-builder.md exists"
else
    echo "❌ FAIL: Target file .archive-integration-approach/agents/command-builder.md does not exist"
    exit 1
fi

# Test 3: Target file should have expected agent header structure
echo "Test 3: Checking target file has expected agent header..."
if grep -q "^# Command Builder Agent$" ".archive-integration-approach/agents/command-builder.md"; then
    echo "✅ PASS: Target file contains expected agent header"
else
    echo "❌ FAIL: Target file missing expected agent header"
    exit 1
fi

# Test 4: Target file should contain agent specialization content
echo "Test 4: Checking target file contains agent specialization..."
if grep -q "## Agent Specialization" ".archive-integration-approach/agents/command-builder.md"; then
    echo "✅ PASS: Target file contains Agent Specialization section"
else
    echo "❌ FAIL: Target file missing Agent Specialization section"
    exit 1
fi

# Test 5: Target file should contain command creation expertise
echo "Test 5: Checking target file contains command creation content..."
if grep -q "Claude Code Command Creation" ".archive-integration-approach/agents/command-builder.md"; then
    echo "✅ PASS: Target file contains command creation expertise"
else
    echo "❌ FAIL: Target file missing command creation content"
    exit 1
fi

# Test 6: Target file should contain YAML optimization content
echo "Test 6: Checking target file contains YAML optimization..."
if grep -q "YAML optimization" ".archive-integration-approach/agents/command-builder.md"; then
    echo "✅ PASS: Target file contains YAML optimization content"
else
    echo "❌ FAIL: Target file missing YAML optimization content"
    exit 1
fi

# Test 7: File permissions should be preserved
echo "Test 7: Checking file permissions are preserved..."
if [ -r ".archive-integration-approach/agents/command-builder.md" ]; then
    echo "✅ PASS: Target file has read permissions"
else
    echo "❌ FAIL: Target file missing read permissions"
    exit 1
fi

# Test 8: File should have expected content size (~2875 bytes)
echo "Test 8: Checking file has expected content size..."
file_size=$(wc -c < ".archive-integration-approach/agents/command-builder.md")
if [ "$file_size" -gt 2000 ] && [ "$file_size" -lt 4000 ]; then
    echo "✅ PASS: Target file has expected content size ($file_size bytes)"
else
    echo "❌ FAIL: Target file has unexpected size ($file_size bytes, expected ~2875)"
    exit 1
fi

# Test 9: Archive directory should contain both agent files
echo "Test 9: Checking archive directory organization..."
if [ -f ".archive-integration-approach/agents/context-engineer.md" ] && [ -f ".archive-integration-approach/agents/command-builder.md" ]; then
    echo "✅ PASS: Archive directory contains both context-engineer.md and command-builder.md"
else
    echo "❌ FAIL: Archive directory missing expected agent files"
    exit 1
fi

echo "=== All tests passed for Task #5 ==="