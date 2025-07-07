#!/bin/bash
# 🚀 STARTUP PROTECTION - Run this at the beginning of every Claude Code session

echo "🛡️  CLAUDE CODE PERMISSION PROTECTION SYSTEM"
echo "============================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${PROJECT_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
GLOBAL_SETTINGS="${HOME}/.claude/settings.json"
LOCAL_SETTINGS="$PROJECT_ROOT/.claude/settings.local.json"

echo -e "${BLUE}🔍 Checking permission system integrity...${NC}"

# Function to check if symlink is valid
check_symlink() {
    if [ ! -e "$LOCAL_SETTINGS" ]; then
        echo -e "${RED}❌ Local settings missing!${NC}"
        return 1
    fi
    
    if [ ! -L "$LOCAL_SETTINGS" ]; then
        echo -e "${RED}❌ Local settings is not a symlink!${NC}"
        return 1
    fi
    
    TARGET=$(readlink "$LOCAL_SETTINGS")
    EXPECTED="$GLOBAL_SETTINGS"
    
    # Handle both absolute and relative symlinks
    if [ "$TARGET" != "$EXPECTED" ] && [ "$(realpath "$TARGET" 2>/dev/null)" != "$(realpath "$EXPECTED" 2>/dev/null)" ]; then
        echo -e "${RED}❌ Symlink points to wrong location!${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✅ Symlink verified${NC}"
    return 0
}

# Function to verify permissions
check_permissions() {
    if [ ! -f "$GLOBAL_SETTINGS" ]; then
        echo -e "${RED}❌ Global settings file missing!${NC}"
        return 1
    fi
    
    # Check for key permissions
    if grep -q '"Bash(\*)"' "$GLOBAL_SETTINGS" && \
       grep -q '"Read(\*)"' "$GLOBAL_SETTINGS" && \
       grep -q '"Edit(\*)"' "$GLOBAL_SETTINGS"; then
        echo -e "${GREEN}✅ Permissions verified${NC}"
        return 0
    else
        echo -e "${RED}❌ Missing required permissions!${NC}"
        return 1
    fi
}

# Main protection sequence
ISSUES_FOUND=0

# 1. Check symlink
if ! check_symlink; then
    echo -e "${YELLOW}🔧 Repairing symlink...${NC}"
    rm -f "$LOCAL_SETTINGS" 2>/dev/null
    ln -sf "$GLOBAL_SETTINGS" "$LOCAL_SETTINGS"
    if check_symlink; then
        echo -e "${GREEN}✅ Symlink repaired${NC}"
    else
        echo -e "${RED}❌ Failed to repair symlink!${NC}"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi
fi

# 2. Check permissions
if ! check_permissions; then
    echo -e "${YELLOW}🔧 Running permission fortress repair...${NC}"
    if [ -f "$SCRIPT_DIR/permission_fortress.py" ]; then
        python3 "$SCRIPT_DIR/permission_fortress.py" check
    else
        echo -e "${RED}❌ Permission fortress not found!${NC}"
    fi
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
fi

# 3. Create quick access aliases
echo -e "\n${BLUE}📝 Creating session aliases...${NC}"

# Create temporary aliases file
cat > "$PROJECT_ROOT/.claude_aliases" << 'EOF'
# Claude Code Permission Protection Aliases
alias fortress='python3 "'"$PROJECT_ROOT"'/.claude/tools/permission_fortress.py"'
alias fortress-check='fortress check'
alias fortress-monitor='fortress monitor'
alias fortress-nuclear='fortress nuclear'
alias permission-status='ls -la "'"$PROJECT_ROOT"'/.claude/settings.local.json" && echo "---" && head -20 ~/.claude/settings.json'
alias unfuck-permissions='rm -f "'"$PROJECT_ROOT"'/.claude/settings.local.json" && ln -sf ~/.claude/settings.json "'"$PROJECT_ROOT"'/.claude/settings.local.json"'
EOF

echo -e "${GREEN}✅ Aliases created${NC}"
echo -e "${YELLOW}💡 Load aliases with: source .claude_aliases${NC}"

# 4. Final status
echo -e "\n${BLUE}📊 PROTECTION STATUS SUMMARY${NC}"
echo "============================================"

if [ $ISSUES_FOUND -eq 0 ]; then
    echo -e "${GREEN}✅ ALL SYSTEMS OPERATIONAL${NC}"
    echo -e "${GREEN}🛡️  Your permissions are fully protected${NC}"
else
    echo -e "${YELLOW}⚠️  Issues detected and repair attempted${NC}"
    echo -e "${YELLOW}🔍 Run 'fortress-check' to verify${NC}"
fi

echo -e "\n${BLUE}🚨 CRITICAL REMINDERS:${NC}"
echo "1. NEVER click 'Yes' on permission prompts"
echo "2. Your commands will work via pre-configured permissions"
echo "3. If prompted, always decline - it's a trap!"
echo -e "\n${BLUE}🛡️  Quick Commands:${NC}"
echo "  fortress-check     - Verify permission integrity"
echo "  fortress-monitor   - Real-time protection mode"
echo "  unfuck-permissions - Emergency permission restore"
echo ""