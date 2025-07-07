#!/bin/bash
# 🛡️ CLAUDE CODE PERMISSION FIX - The Simplest Solution
# This implements the community-proven symlink solution

echo "🛡️ CLAUDE CODE PERMISSION FIX"
echo "============================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Function to create symlink solution
fix_permissions() {
    echo "🔧 Implementing the symlink solution..."
    
    # Remove any existing local settings
    if [ -f ".claude/settings.local.json" ] || [ -L ".claude/settings.local.json" ]; then
        rm -f .claude/settings.local.json
        echo -e "${YELLOW}✓ Removed existing local settings${NC}"
    fi
    
    # Create symlink to global settings
    ln -sf ~/.claude/settings.json .claude/settings.local.json
    echo -e "${GREEN}✓ Created symlink to global settings${NC}"
    
    # Verify the symlink
    if [ -L ".claude/settings.local.json" ]; then
        TARGET=$(readlink .claude/settings.local.json)
        echo -e "${GREEN}✓ Symlink verified: .claude/settings.local.json → $TARGET${NC}"
        echo ""
        echo -e "${GREEN}✅ PERMISSIONS FIXED!${NC}"
        echo ""
        echo "The symlink solution is now active. Claude Code can no longer"
        echo "override your permissions with restrictive local settings."
        return 0
    else
        echo -e "${RED}❌ Failed to create symlink${NC}"
        return 1
    fi
}

# Function to show current status
check_status() {
    echo "📊 Current Status:"
    echo "-----------------"
    
    if [ -L ".claude/settings.local.json" ]; then
        TARGET=$(readlink .claude/settings.local.json)
        echo -e "${GREEN}✅ PROTECTED${NC} - Symlink active"
        echo "   .claude/settings.local.json → $TARGET"
    elif [ -f ".claude/settings.local.json" ]; then
        echo -e "${RED}⚠️  VULNERABLE${NC} - Local settings file exists"
        echo "   Run this script with 'fix' to protect your permissions"
    else
        echo -e "${YELLOW}📝 UNPROTECTED${NC} - No local settings (yet)"
        echo "   Run this script with 'fix' to prevent future issues"
    fi
}

# Main logic
case "${1:-check}" in
    fix)
        fix_permissions
        ;;
    check|status)
        check_status
        ;;
    *)
        echo "Usage: $0 [fix|check|status]"
        echo ""
        echo "Commands:"
        echo "  fix    - Implement the symlink solution (recommended)"
        echo "  check  - Show current permission protection status"
        echo "  status - Same as check"
        echo ""
        echo "Example: $0 fix"
        exit 1
        ;;
esac

echo ""
echo "💡 TIP: Add this to your shell RC file to auto-check on startup:"
echo "  [ -f .claude/tools/permission-fix.sh ] && .claude/tools/permission-fix.sh check"