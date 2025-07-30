#!/bin/bash
# Claude Code Template Library Setup - Interactive Installation

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Get target directory
TARGET_DIR="${1:-.}"

echo -e "${BLUE}🚀 Claude Code Template Library Setup${NC}"
echo ""

# Create absolute path
if [ ! -d "$TARGET_DIR" ]; then
    echo "📁 Creating directory: $TARGET_DIR"
    mkdir -p "$TARGET_DIR"
fi
TARGET_DIR=$(cd "$TARGET_DIR" && pwd)

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if .claude directory exists in source
if [ ! -d "$SCRIPT_DIR/.claude" ]; then
    echo "❌ Error: .claude directory not found in $SCRIPT_DIR"
    echo "Expected to find complete template library at: $SCRIPT_DIR/.claude"
    exit 1
fi

# Count templates for user feedback
TEMPLATE_COUNT=$(find "$SCRIPT_DIR/.claude" -name "*.md" | wc -l | xargs)
echo "📚 Found $TEMPLATE_COUNT template files to install"

# Backup existing .claude if it exists
if [ -d "$TARGET_DIR/.claude" ]; then
    echo -e "${YELLOW}⚠️  Backing up existing .claude to .claude.backup${NC}"
    mv "$TARGET_DIR/.claude" "$TARGET_DIR/.claude.backup"
fi

# Copy .claude directory with progress
echo -e "${BLUE}📋 Copying templates to $TARGET_DIR/.claude${NC}"
cp -r "$SCRIPT_DIR/.claude" "$TARGET_DIR/"

# Verify copy succeeded
COPIED_COUNT=$(find "$TARGET_DIR/.claude" -name "*.md" 2>/dev/null | wc -l | xargs)
if [ "$COPIED_COUNT" != "$TEMPLATE_COUNT" ]; then
    echo "❌ Error: Copy verification failed ($COPIED_COUNT != $TEMPLATE_COUNT files)"
    exit 1
fi

# Create basic CLAUDE.md if it doesn't exist
if [ ! -f "$TARGET_DIR/CLAUDE.md" ]; then
    echo "📝 Creating CLAUDE.md project memory file"
    cat > "$TARGET_DIR/CLAUDE.md" << 'EOF'
# Claude Code Project

**Project Type**: [Your project type here]
**Tech Stack**: [Your technology stack]

## Template Library

Claude Code template library installed with 64 active commands.

To customize templates automatically, run:
```
/adapt-to-project
```

This will detect your project type and replace all placeholders automatically.

## 🚀 Commands That Work Right Now

These 5 commands work immediately (no customization needed):
- `/quick-help` - Command guide and help system
- `/quick-task` - Universal task execution (any language/framework)
- `/quick-dev` - Development assistance and code review
- `/quick-quality` - Code quality analysis and fixes
- `/quick-test` - Testing generation and execution

## 📚 After Customization (64 total commands)

Run `/adapt-to-project` to unlock project-specific commands:
- `/help`, `/task`, `/dev`, `/quality`, `/test` (enhanced versions)
- Plus 59 additional specialized commands for your tech stack

EOF
fi

echo ""
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo ""
echo "📍 Location: $TARGET_DIR/.claude"
echo "📊 Templates: $COPIED_COUNT files installed"
echo ""
echo -e "${BLUE}🎯 Next Steps:${NC}"
echo "1. Open Claude Code in your project directory"
echo "2. Run: /adapt-to-project"
echo "3. Answer a few questions for automatic customization"
echo "4. Start using your customized commands!"
echo ""
echo -e "${YELLOW}💡 Need help? Run /help in Claude Code${NC}"