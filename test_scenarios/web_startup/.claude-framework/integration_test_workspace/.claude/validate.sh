#!/bin/bash
# Validate customization progress

echo "Claude Code Template Customization Check"
echo "================================="

# Check for unreplaced placeholders
echo -n "Checking for placeholders... "
placeholder_count=$(grep -r "INSERT_" .claude/commands 2>/dev/null | wc -l)
if [ $placeholder_count -gt 0 ]; then
    echo "❌ Found $placeholder_count unreplaced placeholders"
else
    echo "✅ All placeholders replaced"
fi

# Check project config
echo -n "Checking project configuration... "
if grep -q "INSERT_PROJECT_NAME" .claude/config/project-config.yaml; then
    echo "❌ Project not configured"
else
    echo "✅ Project configured"
fi

# Calculate readiness
if [ $placeholder_count -eq 0 ]; then
    echo ""
    echo "Readiness Score: 100% ✨"
    echo "Your framework is fully adapted!"
else
    score=$((100 - ($placeholder_count * 2)))
    [ $score -lt 0 ] && score=0
    echo ""
    echo "Readiness Score: ${score}%"
    echo "Run /adapt-to-project to get customization guide"
fi
