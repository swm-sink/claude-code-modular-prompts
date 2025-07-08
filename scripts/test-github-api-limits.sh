#!/bin/bash
# Test script to verify real GitHub API limits for issue body size

set -euo pipefail

echo "=== GitHub API Limit Testing ==="
echo "Testing real limits for issue body size..."
echo

# Function to create test content of specific size
create_test_content() {
    local size_kb=$1
    local content=""
    
    # Generate content using repeated text (more realistic than just 'A')
    local base_text="This is test content for GitHub API limit testing. "
    local base_length=${#base_text}
    local chars_needed=$((size_kb * 1024))
    local repetitions=$((chars_needed / base_length))
    
    for ((i=0; i<repetitions; i++)); do
        content+="$base_text"
    done
    
    echo "$content"
}

# Function to test GitHub issue creation with specific size
test_github_issue_size() {
    local size_kb=$1
    local test_title="TEST: API Limit Test - ${size_kb}KB Body"
    local test_content=$(create_test_content $size_kb)
    
    echo "Testing ${size_kb}KB body size..."
    
    # Try to create issue with gh CLI
    if gh issue create \
        --title "$test_title" \
        --body "$test_content" \
        --label "test,api-limit-test" \
        2>&1 | tee /tmp/gh_test_${size_kb}kb.log; then
        
        echo "✓ SUCCESS: ${size_kb}KB body accepted"
        
        # Get the issue number from the output
        local issue_url=$(grep -oE 'https://github.com/[^/]+/[^/]+/issues/[0-9]+' /tmp/gh_test_${size_kb}kb.log | head -1)
        if [ -n "$issue_url" ]; then
            local issue_number=$(echo "$issue_url" | grep -oE '[0-9]+$')
            echo "  Created issue #$issue_number"
            
            # Close the test issue
            gh issue close "$issue_number" --reason "completed" --comment "Test completed successfully"
            echo "  Closed test issue #$issue_number"
        fi
        
        return 0
    else
        echo "✗ FAILED: ${size_kb}KB body rejected"
        
        # Check if it's a body size error
        if grep -q "body is too long" /tmp/gh_test_${size_kb}kb.log || \
           grep -q "422" /tmp/gh_test_${size_kb}kb.log; then
            echo "  Error: Body size limit exceeded"
        else
            echo "  Error: $(cat /tmp/gh_test_${size_kb}kb.log)"
        fi
        
        return 1
    fi
}

# Function to test comment size limits
test_github_comment_size() {
    local size_kb=$1
    local test_issue_number=$2
    local test_content=$(create_test_content $size_kb)
    
    echo "Testing ${size_kb}KB comment size on issue #$test_issue_number..."
    
    if gh issue comment "$test_issue_number" \
        --body "$test_content" \
        2>&1 | tee /tmp/gh_comment_test_${size_kb}kb.log; then
        
        echo "✓ SUCCESS: ${size_kb}KB comment accepted"
        return 0
    else
        echo "✗ FAILED: ${size_kb}KB comment rejected"
        
        if grep -q "body is too long" /tmp/gh_comment_test_${size_kb}kb.log || \
           grep -q "422" /tmp/gh_comment_test_${size_kb}kb.log; then
            echo "  Error: Comment size limit exceeded"
        else
            echo "  Error: $(cat /tmp/gh_comment_test_${size_kb}kb.log)"
        fi
        
        return 1
    fi
}

# Main testing sequence
main() {
    # Test issue body sizes (binary search approach)
    echo "=== Testing Issue Body Size Limits ==="
    echo
    
    # Start with known working size and test upward
    local sizes=(32 48 56 60 62 64 65 66 68 70 72 80)
    local max_working_size=0
    
    for size in "${sizes[@]}"; do
        if test_github_issue_size $size; then
            max_working_size=$size
        else
            echo "Found limit between ${max_working_size}KB and ${size}KB"
            break
        fi
        echo
        sleep 2  # Rate limiting protection
    done
    
    echo
    echo "=== Testing Comment Size Limits ==="
    echo
    
    # Create a test issue for comment testing
    local test_issue_url=$(gh issue create \
        --title "TEST: Comment Size Limit Testing" \
        --body "This issue is for testing comment size limits" \
        --label "test,api-limit-test" | grep -oE 'https://github.com/[^/]+/[^/]+/issues/[0-9]+')
    
    local test_issue_number=$(echo "$test_issue_url" | grep -oE '[0-9]+$')
    echo "Created test issue #$test_issue_number for comment testing"
    echo
    
    # Test comment sizes
    local comment_sizes=(32 48 56 60 62 64 65 66 68 70)
    local max_comment_size=0
    
    for size in "${comment_sizes[@]}"; do
        if test_github_comment_size $size $test_issue_number; then
            max_comment_size=$size
        else
            echo "Found comment limit between ${max_comment_size}KB and ${size}KB"
            break
        fi
        echo
        sleep 2  # Rate limiting protection
    done
    
    # Clean up test issue
    gh issue close "$test_issue_number" --reason "completed" --comment "Comment size testing completed"
    echo "Closed test issue #$test_issue_number"
    
    echo
    echo "=== Test Summary ==="
    echo "Maximum working issue body size: ${max_working_size}KB"
    echo "Maximum working comment size: ${max_comment_size}KB"
    echo
    echo "Note: GitHub's actual limit is ~65KB for issue bodies and comments"
    echo "This includes all formatting and metadata overhead"
}

# Check if gh CLI is authenticated
if ! gh auth status >/dev/null 2>&1; then
    echo "Error: GitHub CLI not authenticated. Run 'gh auth login' first."
    exit 1
fi

# Run main testing
main