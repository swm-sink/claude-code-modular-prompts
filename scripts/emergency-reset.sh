#!/bin/bash
# Emergency reset - backs up and resets to clean state

echo "🚨 Claude Context Architect - Emergency Reset"
echo "============================================"
echo ""
echo "This will reset your Claude Context Architect installation."
echo "Current configuration will be backed up."
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Reset cancelled."
    exit 1
fi

# Create backup
BACKUP_DIR=".claude-backup-$(date +%Y%m%d-%H%M%S)"
echo "📦 Creating backup in $BACKUP_DIR..."
cp -r .claude "$BACKUP_DIR" 2>/dev/null
cp CLAUDE.md "$BACKUP_DIR/" 2>/dev/null
cp PROJECT-DNA.md "$BACKUP_DIR/" 2>/dev/null

# Reset to clean state
echo "🔄 Resetting to clean state..."

# Clear generated commands
rm -rf .claude/commands/generated/* 2>/dev/null

# Clear session states if they exist
rm -rf .claude/sessions/* 2>/dev/null

# Clear any PROJECT-DNA.md
rm -f PROJECT-DNA.md 2>/dev/null

# Reset CLAUDE.md to minimal
cat > CLAUDE.md << 'EOF'
# Project Context

## About This Project
*Reset to clean state - ready for new discovery*

## Status
- Installation: Complete
- Discovery: Not started
- Generation: Not started

## Quick Start
Run `/welcome-simple` to begin the 10-15 minute discovery process.

---
*Simple. Elegant. Functional.*
EOF

echo "✅ Reset complete!"
echo "📁 Previous configuration backed up to: $BACKUP_DIR"
echo ""
echo "To start fresh, run:"
echo "  /welcome-simple"
echo "  /discover-project-simple"
echo "  /generate-commands-simple"