#!/bin/bash
# Minimal cleanup script - keeps project tidy

echo "🧹 Claude Context Architect - Cleanup"
echo "====================================="

# Remove any temporary files
find . -name "*.tmp" -o -name "*.bak" -o -name "*~" | xargs rm -f 2>/dev/null

# Clean up old session states if they exist
if [ -d ".claude/sessions" ]; then
    find .claude/sessions -name "*.md" -mtime +30 -delete 2>/dev/null
    echo "✅ Old session states cleaned"
fi

# Clean up any empty directories in .claude
find .claude -type d -empty -delete 2>/dev/null

# Remove any duplicate backups
if ls .claude.backup* 1> /dev/null 2>&1; then
    # Keep only the most recent backup
    ls -t .claude.backup* | tail -n +2 | xargs rm -rf 2>/dev/null
    echo "✅ Old backups removed"
fi

# Report
echo "✅ Temporary files removed"
echo "✅ Empty directories cleaned"
echo "✨ Cleanup complete!"