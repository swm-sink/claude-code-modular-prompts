#!/bin/bash
# validate.sh - Verify outputs and generated commands
# One of only 5 allowed scripts

set -e

echo "✅ Claude Context Architect - Validation"
echo "======================================"

# Check essential files exist
echo "Checking essential files..."
[ -f CLAUDE.md ] && echo "✓ CLAUDE.md exists" || echo "✗ CLAUDE.md missing"
[ -d .claude/commands ] && echo "✓ Commands directory exists" || echo "✗ Commands missing"
[ -d .claude/context ] && echo "✓ Context directory exists" || echo "✗ Context missing"

# Count generated commands
if [ -d outputs/generated-commands ]; then
    COUNT=$(find outputs/generated-commands -name "*.md" | wc -l)
    echo "✓ Generated $COUNT commands"
else
    echo "✗ No generated commands found"
fi

# Check for PROJECT-DNA
if [ -f outputs/project-dna/PROJECT-DNA.md ]; then
    echo "✓ PROJECT-DNA.md generated"
else
    echo "✗ PROJECT-DNA.md not found"
fi

echo ""
echo "Validation complete!"