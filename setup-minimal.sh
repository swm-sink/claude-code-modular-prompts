#!/bin/bash
# Claude Code Minimal Template Setup - Simple & Effective

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Get target directory
TARGET_DIR="${1:-.}"

echo -e "${BLUE}🚀 Claude Code Minimal Setup${NC}"
echo ""

# Create absolute path
if [ ! -d "$TARGET_DIR" ]; then
    echo "📁 Creating directory: $TARGET_DIR"
    mkdir -p "$TARGET_DIR"
fi
TARGET_DIR=$(cd "$TARGET_DIR" && pwd)

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if minimal .claude directory exists
if [ ! -d "$SCRIPT_DIR/.claude-minimal" ]; then
    echo "❌ Error: .claude-minimal directory not found in $SCRIPT_DIR"
    echo "This script installs the simplified version with 7 essential commands."
    exit 1
fi

# Count commands for user feedback
COMMAND_COUNT=$(find "$SCRIPT_DIR/.claude-minimal/commands" -name "*.md" | wc -l | xargs)
echo "📚 Installing $COMMAND_COUNT essential commands"

# Backup existing .claude if it exists
if [ -d "$TARGET_DIR/.claude" ]; then
    echo -e "${YELLOW}⚠️  Backing up existing .claude to .claude.backup${NC}"
    mv "$TARGET_DIR/.claude" "$TARGET_DIR/.claude.backup"
fi

# Copy minimal .claude directory
echo -e "${BLUE}📋 Copying commands to $TARGET_DIR/.claude${NC}"
cp -r "$SCRIPT_DIR/.claude-minimal" "$TARGET_DIR/.claude"

# Verify copy succeeded
COPIED_COUNT=$(find "$TARGET_DIR/.claude/commands" -name "*.md" 2>/dev/null | wc -l | xargs)
if [ "$COPIED_COUNT" != "$COMMAND_COUNT" ]; then
    echo "❌ Error: Copy verification failed ($COPIED_COUNT != $COMMAND_COUNT files)"
    exit 1
fi

# Create simple CLAUDE.md
if [ ! -f "$TARGET_DIR/CLAUDE.md" ]; then
    echo "📝 Creating CLAUDE.md project memory file"
    cat > "$TARGET_DIR/CLAUDE.md" << 'EOF'
# Claude Code Project

## Essential Commands (Ready to Use)

All commands work immediately with any programming language or framework:

- **`/help`** - Get help and see all available commands
- **`/task`** - Execute any development task 
- **`/analyze`** - Analyze code, architecture, or problems
- **`/review`** - Code review with suggestions
- **`/debug`** - Debug issues and errors
- **`/test`** - Generate tests and run test suites
- **`/docs`** - Create and maintain documentation

## Usage Examples

```
/task "add user authentication to my app"
/analyze "why is my API slow?"
/review src/components/UserForm.jsx
/debug "login fails with 500 error"
/test --generate src/auth.js
/docs --api src/routes/
```

## Getting Started

1. Try `/help` to see all commands
2. Use `/task "your goal"` for any development work
3. All commands work with any tech stack - no configuration needed

EOF
fi

echo ""
echo -e "${GREEN}✅ Minimal Setup Complete!${NC}"
echo ""
echo "📍 Location: $TARGET_DIR/.claude"  
echo "📊 Commands: $COPIED_COUNT ready-to-use commands"
echo ""
echo -e "${BLUE}🎯 What You Can Do Right Now:${NC}"
echo "1. Open Claude Code in your project directory"
echo "2. Try: /help"
echo "3. Try: /task \"add a login form to my app\""
echo "4. Try: /analyze \"performance issues\""
echo ""
echo -e "${GREEN}✨ No configuration needed - all commands work immediately!${NC}"