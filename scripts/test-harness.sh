#!/bin/bash
# Minimal test harness - basic smoke tests only

echo "🧪 Claude Context Architect - Test Harness"
echo "========================================="

PASS=0
FAIL=0

# Test 1: Check .claude directory exists
if [ -d ".claude" ]; then
    echo "✅ .claude directory exists"
    ((PASS++))
else
    echo "❌ .claude directory missing"
    ((FAIL++))
fi

# Test 2: Check essential commands exist
for cmd in welcome-simple discover-project-simple generate-commands-simple list-commands; do
    if [ -f ".claude/commands/${cmd}.md" ]; then
        echo "✅ Command /${cmd} exists"
        ((PASS++))
    else
        echo "❌ Command /${cmd} missing"
        ((FAIL++))
    fi
done

# Test 3: Check YAML frontmatter in commands
for file in .claude/commands/*.md; do
    if grep -q "^---" "$file" && grep -q "^name:" "$file"; then
        ((PASS++))
    else
        echo "❌ Invalid YAML in $(basename $file)"
        ((FAIL++))
    fi
done

# Test 4: Check for CLAUDE.md
if [ -f "CLAUDE.md" ]; then
    echo "✅ CLAUDE.md exists"
    ((PASS++))
else
    echo "❌ CLAUDE.md missing"
    ((FAIL++))
fi

# Summary
echo ""
echo "========================================="
echo "Test Results: $PASS passed, $FAIL failed"
if [ $FAIL -eq 0 ]; then
    echo "✨ All tests passed!"
    exit 0
else
    echo "⚠️  Some tests failed"
    exit 1
fi