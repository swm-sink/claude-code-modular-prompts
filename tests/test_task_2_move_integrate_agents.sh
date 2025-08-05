#!/bin/bash
# Test Suite for Task #2: Move scripts/integrate-agents.sh to archive
# Purpose: Verify file successfully moved to archive location
# TDD Phase: RED - Write failing tests first

set -e

# Test configuration
SCRIPT_NAME="test_task_2_move_integrate_agents.sh"
SOURCE_FILE="scripts/integrate-agents.sh"
ARCHIVE_FILE=".archive-integration-approach/scripts/integrate-agents.sh"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging function
log() {
    local level="$1"
    local message="$2"
    local timestamp="$(date '+%Y-%m-%d %H:%M:%S')"
    
    case "$level" in
        "PASS")
            echo -e "${GREEN}✅ [$timestamp] PASS: $message${NC}"
            ;;
        "FAIL")
            echo -e "${RED}❌ [$timestamp] FAIL: $message${NC}"
            ;;
        "INFO")
            echo -e "${YELLOW}ℹ️  [$timestamp] INFO: $message${NC}"
            ;;
    esac
}

# Test counter
TESTS_RUN=0
TESTS_PASSED=0

run_test() {
    local test_name="$1"
    local test_function="$2"
    
    TESTS_RUN=$((TESTS_RUN + 1))
    log "INFO" "Running test: $test_name"
    
    if $test_function; then
        log "PASS" "$test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        log "FAIL" "$test_name"
    fi
}

# RED Phase Tests - These should FAIL initially
test_source_file_exists() {
    if [ -f "$SOURCE_FILE" ]; then
        return 0
    else
        return 1
    fi
}

test_archive_directory_ready() {
    if [ -d ".archive-integration-approach/scripts" ]; then
        return 0
    else
        return 1
    fi
}

test_file_not_in_archive_yet() {
    # Should FAIL initially (file should not be in archive yet)
    if [ ! -f "$ARCHIVE_FILE" ]; then
        return 0
    else
        return 1
    fi
}

test_source_file_moved() {
    # Should PASS after move (file should be gone from source)
    if [ ! -f "$SOURCE_FILE" ]; then
        return 0
    else
        return 1
    fi
}

test_archive_file_present() {
    # Should FAIL initially (file should not be in archive yet)
    if [ -f "$ARCHIVE_FILE" ]; then
        return 0
    else
        return 1
    fi
}

test_file_content_preserved() {
    if [ -f "$ARCHIVE_FILE" ]; then
        # Check if file contains expected integration script content
        if grep -q "Agent Integration System" "$ARCHIVE_FILE"; then
            return 0
        else
            return 1
        fi
    else
        return 1
    fi
}

test_file_permissions_preserved() {
    if [ -f "$ARCHIVE_FILE" ]; then
        # Check if file is executable
        if [ -x "$ARCHIVE_FILE" ]; then
            return 0
        else
            return 1
        fi
    else
        return 1
    fi
}

# Main test execution
main() {
    log "INFO" "Starting TDD tests for Task #2: Move integrate-agents.sh"
    log "INFO" "TDD Phase: GREEN - Verifying implementation results"
    
    # Post-implementation tests - verify move was successful
    run_test "Archive directory is ready" test_archive_directory_ready
    run_test "Source file no longer exists (moved)" test_source_file_moved
    run_test "Archive file present (moved successfully)" test_archive_file_present
    run_test "File content preserved in archive" test_file_content_preserved
    run_test "File permissions preserved in archive" test_file_permissions_preserved
    
    # Summary
    log "INFO" "Test Summary: $TESTS_PASSED/$TESTS_RUN tests passed"
    
    if [ $TESTS_PASSED -eq $TESTS_RUN ]; then
        log "PASS" "All tests passed - Move operation successful"
        exit 0
    else
        log "FAIL" "Some tests failed - Implementation issues detected"
        exit 1
    fi
}

# Execute tests
main "$@"