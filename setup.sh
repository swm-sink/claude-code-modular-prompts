#!/bin/bash
# Claude Context Architect Setup - Interactive Installation

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Get target directory
TARGET_DIR="${1:-.}"

echo -e "${BLUE}🚀 Claude Context Architect Setup${NC}"
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
    echo "Expected to find complete context engineering system at: $SCRIPT_DIR/.claude"
    exit 1
fi

# Count context files for user feedback
CONTEXT_COUNT=$(find "$SCRIPT_DIR/.claude" -name "*.md" | wc -l | xargs)
echo "📚 Found $CONTEXT_COUNT context engineering files to install"

# Backup existing .claude if it exists
if [ -d "$TARGET_DIR/.claude" ]; then
    echo -e "${YELLOW}⚠️  Backing up existing .claude to .claude.backup${NC}"
    mv "$TARGET_DIR/.claude" "$TARGET_DIR/.claude.backup"
fi

# Copy .claude directory with progress
echo -e "${BLUE}📋 Copying context engineering system to $TARGET_DIR/.claude${NC}"
cp -r "$SCRIPT_DIR/.claude" "$TARGET_DIR/"

# Verify copy succeeded
COPIED_COUNT=$(find "$TARGET_DIR/.claude" -name "*.md" 2>/dev/null | wc -l | xargs)
if [ "$COPIED_COUNT" != "$CONTEXT_COUNT" ]; then
    echo "❌ Error: Copy verification failed ($COPIED_COUNT != $CONTEXT_COUNT files)"
    exit 1
fi

# Create basic CLAUDE.md if it doesn't exist
if [ ! -f "$TARGET_DIR/CLAUDE.md" ]; then
    echo "📝 Creating CLAUDE.md project memory file"
    cat > "$TARGET_DIR/CLAUDE.md" << 'EOF'
# Claude Context Architect Project

**Project Type**: [Your project type here]
**Tech Stack**: [Your technology stack]

## Context Engineering System

Claude Context Architect installed - THE definitive Claude Code setup tool.

To begin 30+ minute consultation, run:
```
/begin-consultation
```

This will start interactive consultation with specialized agents to create your context system.

## 🚀 Ready for Consultation

Begin with any of these consultation commands:
- `/begin-consultation` - Start 30+ minute guided project analysis
- `/quick-help` - Get help with consultation process
- `/session-status` - Check current consultation progress
- `/resume-consultation` - Continue paused consultation session
- `/validate-context` - Test generated context effectiveness

## 📚 After Consultation (Complete Context System)

After consultation, you'll have:
- Multi-file hierarchical context system tailored to your project
- Specialized Claude that understands your architecture and patterns
- Session management for ongoing context evolution
- Validation framework to ensure context effectiveness

EOF
fi

echo ""
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo ""
echo "📍 Location: $TARGET_DIR/.claude"
echo "📊 Context System: $COPIED_COUNT files installed"
echo ""
echo -e "${BLUE}🎯 Next Steps:${NC}"
echo "1. Open Claude Code in your project directory"
echo "2. Run: /begin-consultation"
echo "3. Complete 30+ minute guided consultation with specialized agents"
echo "4. Get Claude that truly understands YOUR project!"
echo ""
echo -e "${YELLOW}💡 Need help? Run /quick-help for consultation guidance${NC}"