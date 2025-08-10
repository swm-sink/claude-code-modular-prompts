#!/bin/bash

# Validate Adaptive Commands
# Tests that new adaptive commands meet requirements

# Don't exit on error immediately
set +e

echo "====================================="
echo "Adaptive Command Validation"
echo "====================================="

# Counters
PASS=0
WARN=0
FAIL=0

# Function to check command exists and has proper structure
check_command() {
    local cmd_file=$1
    local cmd_name=$2
    local expected_modes=$3
    
    echo -n "Checking $cmd_name... "
    
    if [ ! -f "$cmd_file" ]; then
        echo "✗ File not found"
        ((FAIL++))
        return
    fi
    
    # Check YAML frontmatter
    if ! grep -q "^name: $cmd_name" "$cmd_file"; then
        echo "✗ Invalid YAML"
        ((FAIL++))
        return
    fi
    
    # Check for adaptive modes
    if [ "$expected_modes" != "0" ]; then
        if grep -q "<.*-mode>" "$cmd_file" || grep -q "<.*-build>" "$cmd_file" || grep -q "<.*-tests>" "$cmd_file"; then
            echo "✓ Has adaptive modes"
            ((PASS++))
        else
            echo "⚠ No adaptive modes found"
            ((WARN++))
        fi
    else
        echo "✓ Valid"
        ((PASS++))
    fi
}

# Function to check line count
check_line_count() {
    local cmd_file=$1
    local max_lines=$2
    local cmd_name=$(basename "$cmd_file" .md)
    
    local lines=$(wc -l < "$cmd_file")
    echo -n "  Line count for $cmd_name: $lines... "
    
    if [ "$lines" -le "$max_lines" ]; then
        echo "✓ Within limit"
        ((PASS++))
    else
        echo "⚠ Exceeds $max_lines lines"
        ((WARN++))
    fi
}

echo ""
echo "1. Checking New Adaptive Commands"
echo "-----------------------------------"

# Check core adaptive commands
check_command ".claude/commands/start.md" "start" 3
check_line_count ".claude/commands/start.md" 70

check_command ".claude/commands/analyze.md" "analyze" 3
check_line_count ".claude/commands/analyze.md" 80

check_command ".claude/commands/build.md" "build" 4
check_line_count ".claude/commands/build.md" 90

check_command ".claude/commands/test.md" "test" 4
check_line_count ".claude/commands/test.md" 80

echo ""
echo "2. Checking Simplified Utility Commands"
echo "----------------------------------------"

check_command ".claude/commands/debug.md" "debug" 3
check_line_count ".claude/commands/debug.md" 60

check_command ".claude/commands/anti-pattern-audit.md" "anti-pattern-audit" 0
check_line_count ".claude/commands/anti-pattern-audit.md" 70

check_command ".claude/commands/commit.md" "commit" 0
check_line_count ".claude/commands/commit.md" 40

echo ""
echo "3. Checking Obsolete Commands"
echo "------------------------------"

# These should be removed or marked deprecated
obsolete_commands=(
    "welcome"
    "orchestrate"
    "setup"
    "initialize"
    "quick-setup"
    "project-analysis"
    "explore"
    "discover"
    "plan"
    "generate"
    "implement"
    "test-unit"
    "test-integration"
    "test-e2e"
)

for cmd in "${obsolete_commands[@]}"; do
    if [ -f ".claude/commands/$cmd.md" ]; then
        echo "⚠ Obsolete command still exists: $cmd"
        ((WARN++))
    elif [ -f ".claude/commands/initialization/$cmd.md" ]; then
        echo "⚠ Obsolete command still exists: initialization/$cmd"
        ((WARN++))
    fi
done

echo ""
echo "4. Checking Progressive Questioning"
echo "------------------------------------"

# Check if commands avoid excessive questions
echo -n "Checking for minimal questions... "
excessive_questions=$(grep -h "?" .claude/commands/{start,analyze,build,test}.md 2>/dev/null | wc -l)
if [ "$excessive_questions" -lt 10 ]; then
    echo "✓ Minimal questions ($excessive_questions found)"
    ((PASS++))
else
    echo "⚠ Many questions ($excessive_questions found)"
    ((WARN++))
fi

echo ""
echo "5. Checking Tool Usage Optimization"
echo "------------------------------------"

# Check for reduced parallel agents
echo -n "Checking Task tool usage... "
task_usage=$(grep -h "Task" .claude/commands/*.md 2>/dev/null | wc -l)
if [ "$task_usage" -lt 20 ]; then
    echo "✓ Optimized Task usage ($task_usage references)"
    ((PASS++))
else
    echo "⚠ High Task usage ($task_usage references)"
    ((WARN++))
fi

# Check for unnecessary WebSearch
echo -n "Checking WebSearch usage... "
websearch_usage=$(grep -h "WebSearch" .claude/commands/*.md 2>/dev/null | wc -l)
if [ "$websearch_usage" -lt 10 ]; then
    echo "✓ Minimal WebSearch ($websearch_usage references)"
    ((PASS++))
else
    echo "⚠ Excessive WebSearch ($websearch_usage references)"
    ((WARN++))
fi

echo ""
echo "====================================="
echo "Validation Summary"
echo "====================================="
echo "Passed: $PASS"
echo "Warnings: $WARN"
echo "Failed: $FAIL"

if [ "$FAIL" -eq 0 ]; then
    echo ""
    echo "✓ All critical checks passed!"
    echo "Adaptive commands are ready for use."
    exit 0
else
    echo ""
    echo "✗ Some checks failed. Please fix before proceeding."
    exit 1
fi