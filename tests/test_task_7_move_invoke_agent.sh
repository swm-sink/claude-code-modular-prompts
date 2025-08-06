#!/bin/bash
# Test for Task 7: Move scripts/invoke-agent.sh to archive
# TDD: RED-GREEN-REFACTOR-INTEGRATION

set -e

echo "=== Task 7 TDD Test Suite ==="
echo "Testing: Move scripts/invoke-agent.sh to .archive-integration-approach/scripts/"
echo ""

# Test setup
SOURCE_FILE="scripts/invoke-agent.sh"
TARGET_FILE=".archive-integration-approach/scripts/invoke-agent.sh"
ARCHIVE_DIR=".archive-integration-approach/scripts"

# Test 1: Source file should not exist after move
test_source_removed() {
    if [ -f "$SOURCE_FILE" ]; then
        echo "❌ Test 1 FAILED: Source file still exists at $SOURCE_FILE"
        return 1
    else
        echo "✅ Test 1 PASSED: Source file removed from $SOURCE_FILE"
        return 0
    fi
}

# Test 2: Target file should exist in archive
test_target_exists() {
    if [ ! -f "$TARGET_FILE" ]; then
        echo "❌ Test 2 FAILED: Target file not found at $TARGET_FILE"
        return 1
    else
        echo "✅ Test 2 PASSED: Target file exists at $TARGET_FILE"
        return 0
    fi
}

# Test 3: Archive directory structure exists
test_archive_structure() {
    if [ ! -d "$ARCHIVE_DIR" ]; then
        echo "❌ Test 3 FAILED: Archive directory not found at $ARCHIVE_DIR"
        return 1
    else
        echo "✅ Test 3 PASSED: Archive directory exists"
        return 0
    fi
}

# Test 4: File content preserved (size check)
test_content_preserved() {
    # Expected size based on actual file  
    EXPECTED_SIZE=8032  # bytes
    
    if [ -f "$TARGET_FILE" ]; then
        ACTUAL_SIZE=$(wc -c < "$TARGET_FILE" | tr -d ' ')
        if [ "$ACTUAL_SIZE" -gt 7900 ] && [ "$ACTUAL_SIZE" -lt 8200 ]; then
            echo "✅ Test 4 PASSED: File content preserved (size: $ACTUAL_SIZE bytes)"
            return 0
        else
            echo "❌ Test 4 FAILED: File size unexpected (got $ACTUAL_SIZE, expected ~$EXPECTED_SIZE)"
            return 1
        fi
    else
        echo "❌ Test 4 FAILED: Target file doesn't exist for content check"
        return 1
    fi
}

# Test 5: File is executable
test_file_executable() {
    if [ -f "$TARGET_FILE" ]; then
        if [ -x "$TARGET_FILE" ]; then
            echo "✅ Test 5 PASSED: File is executable"
            return 0
        else
            echo "❌ Test 5 FAILED: File is not executable"
            return 1
        fi
    else
        echo "❌ Test 5 FAILED: Target file doesn't exist"
        return 1
    fi
}

# Run all tests
echo "Running Task 7 validation tests..."
echo "================================="

FAILED=0

test_source_removed || FAILED=$((FAILED + 1))
test_target_exists || FAILED=$((FAILED + 1))
test_archive_structure || FAILED=$((FAILED + 1))
test_content_preserved || FAILED=$((FAILED + 1))
test_file_executable || FAILED=$((FAILED + 1))

echo "================================="
if [ $FAILED -eq 0 ]; then
    echo "✅ ALL TESTS PASSED - Task 7 complete!"
    exit 0
else
    echo "❌ $FAILED tests failed - Task 7 validation failed"
    exit 1
fi