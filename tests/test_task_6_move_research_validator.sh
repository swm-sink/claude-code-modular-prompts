#!/bin/bash

# Test Task #6: Move .claude/agents/research-validator.md to .archive-integration-approach/agents/
# LIGHTWEIGHT TDD - Final agent archival task

set -e

echo "=== Testing Task #6: Move research-validator.md agent (Final Agent Archival) ==="

# Test 1: Source file should NOT exist after move
echo "Test 1: Checking source file no longer exists..."
if [ -f ".claude/agents/research-validator.md" ]; then
    echo "❌ FAIL: Source file .claude/agents/research-validator.md still exists"
    exit 1
else
    echo "✅ PASS: Source file .claude/agents/research-validator.md no longer exists"
fi

# Test 2: Target file should exist after move
echo "Test 2: Checking target file exists..."
if [ -f ".archive-integration-approach/agents/research-validator.md" ]; then
    echo "✅ PASS: Target file .archive-integration-approach/agents/research-validator.md exists"
else
    echo "❌ FAIL: Target file .archive-integration-approach/agents/research-validator.md does not exist"
    exit 1
fi

# Test 3: Target file should contain research validator content
echo "Test 3: Checking target file contains research validator content..."
if grep -q "# Research Validator Agent" ".archive-integration-approach/agents/research-validator.md"; then
    echo "✅ PASS: Target file contains Research Validator Agent header"
else
    echo "❌ FAIL: Target file missing expected agent header"
    exit 1
fi

# Test 4: Target file should contain CRAAP methodology content
echo "Test 4: Checking target file contains CRAAP methodology..."
if grep -q "CRAAP test methodology" ".archive-integration-approach/agents/research-validator.md"; then
    echo "✅ PASS: Target file contains CRAAP methodology content"
else
    echo "❌ FAIL: Target file missing CRAAP methodology"
    exit 1
fi

# Test 5: File should have expected size (~3200 bytes)
echo "Test 5: Checking file has expected content size..."
file_size=$(wc -c < ".archive-integration-approach/agents/research-validator.md")
if [ "$file_size" -gt 2500 ] && [ "$file_size" -lt 4000 ]; then
    echo "✅ PASS: Target file has expected content size ($file_size bytes)"
else
    echo "❌ FAIL: Target file has unexpected size ($file_size bytes, expected ~3221)"
    exit 1
fi

# Test 6: CRITICAL - Archive directory should contain ALL THREE agent files (COMPLETION)
echo "Test 6: Checking complete agent archival..."
if [ -f ".archive-integration-approach/agents/context-engineer.md" ] && \
   [ -f ".archive-integration-approach/agents/command-builder.md" ] && \
   [ -f ".archive-integration-approach/agents/research-validator.md" ]; then
    echo "✅ PASS: Archive contains all three agent files - AGENT ARCHIVAL COMPLETE"
else
    echo "❌ FAIL: Archive missing expected agent files"
    exit 1
fi

# Test 7: CRITICAL - Source agents directory should be EMPTY (CLEAN SLATE)
echo "Test 7: Checking source agents directory is empty..."
if [ "$(ls -A .claude/agents/)" ]; then
    echo "❌ FAIL: .claude/agents/ directory is not empty"
    exit 1
else
    echo "✅ PASS: .claude/agents/ directory is EMPTY - READY FOR GENERATION ARCHITECTURE"
fi

echo "=== 🎉 ALL TESTS PASSED - AGENT ARCHIVAL PHASE COMPLETE ==="