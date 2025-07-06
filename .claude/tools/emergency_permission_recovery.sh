#!/bin/bash
# 🚨 EMERGENCY PERMISSION RECOVERY - Enhanced Version
# Use this when permissions are completely broken or symlinks are hijacked

set -e  # Exit on error

echo "🚨 EMERGENCY PERMISSION RECOVERY SYSTEM"
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get paths
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
GLOBAL_SETTINGS="$HOME/.claude/settings.json"
LOCAL_SETTINGS="$PROJECT_ROOT/.claude/settings.local.json"
BACKUP_DIR="$PROJECT_ROOT/.claude/permission_backups"
FORTRESS_PY="$PROJECT_ROOT/.claude/tools/permission_fortress.py"

echo -e "${BLUE}📍 Project root: $PROJECT_ROOT${NC}"
echo -e "${BLUE}📍 Global settings: $GLOBAL_SETTINGS${NC}"
echo ""

# Step 1: Check current state
echo -e "${YELLOW}🔍 Step 1: Checking current state...${NC}"
if [ -L "$LOCAL_SETTINGS" ]; then
    TARGET=$(readlink "$LOCAL_SETTINGS")
    echo -e "   Symlink exists, pointing to: $TARGET"
    
    # Check if it's pointing to temp directory
    if [[ "$TARGET" == */tmp/* ]] || [[ "$TARGET" == */var/folders/* ]] || [[ "$TARGET" == */T/* ]]; then
        echo -e "${RED}   ❌ CRITICAL: Symlink hijacked to temp directory!${NC}"
        NEEDS_REPAIR=true
    elif [[ "$TARGET" != "$GLOBAL_SETTINGS" ]]; then
        echo -e "${RED}   ❌ Symlink pointing to wrong location${NC}"
        NEEDS_REPAIR=true
    else
        echo -e "${GREEN}   ✅ Symlink appears correct${NC}"
        NEEDS_REPAIR=false
    fi
elif [ -f "$LOCAL_SETTINGS" ]; then
    echo -e "${RED}   ❌ Local settings exists but is NOT a symlink${NC}"
    NEEDS_REPAIR=true
else
    echo -e "${RED}   ❌ Local settings missing entirely${NC}"
    NEEDS_REPAIR=true
fi

# Step 2: Backup current state
echo ""
echo -e "${YELLOW}🔍 Step 2: Creating safety backup...${NC}"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Backup global settings if they exist
if [ -f "$GLOBAL_SETTINGS" ]; then
    cp "$GLOBAL_SETTINGS" "$BACKUP_DIR/global_backup_$TIMESTAMP.json"
    echo -e "${GREEN}   ✅ Global settings backed up${NC}"
fi

# Backup local settings if they exist and aren't a symlink
if [ -f "$LOCAL_SETTINGS" ] && [ ! -L "$LOCAL_SETTINGS" ]; then
    cp "$LOCAL_SETTINGS" "$BACKUP_DIR/local_backup_$TIMESTAMP.json"
    echo -e "${GREEN}   ✅ Local settings backed up${NC}"
fi

# Step 3: Repair if needed
if [ "$NEEDS_REPAIR" = true ]; then
    echo ""
    echo -e "${YELLOW}🔧 Step 3: Performing emergency repair...${NC}"
    
    # Remove broken symlink or file
    echo -e "   Removing broken/hijacked symlink..."
    rm -f "$LOCAL_SETTINGS"
    
    # Ensure global settings exist with comprehensive permissions
    echo -e "   Ensuring global settings have comprehensive permissions..."
    mkdir -p "$(dirname "$GLOBAL_SETTINGS")"
    
    if [ ! -f "$GLOBAL_SETTINGS" ]; then
        echo -e "   Creating new global settings..."
        cat > "$GLOBAL_SETTINGS" << 'EOF'
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1"
  },
  "permissions": {
    "allow": [
      "Bash(*)",
      "Read(*)",
      "Edit(*)",
      "Write(*)",
      "MultiEdit(*)",
      "Glob(*)",
      "Grep(*)",
      "LS(*)",
      "Task(*)",
      "WebFetch(*)",
      "WebSearch(*)",
      "NotebookRead(*)",
      "NotebookEdit(*)",
      "TodoRead(*)",
      "TodoWrite(*)",
      "exit_plan_mode(*)",
      "mcp__ide__getDiagnostics(*)",
      "mcp__ide__executeCode(*)",
      "mcp__*"
    ],
    "deny": [
      "Bash(rm -rf /:*)",
      "Bash(sudo su:*)",
      "Bash(dd:*)",
      "Bash(mkfs:*)"
    ]
  },
  "model": "opus"
}
EOF
    fi
    
    # Create correct symlink
    echo -e "   Creating correct symlink..."
    ln -sf "$GLOBAL_SETTINGS" "$LOCAL_SETTINGS"
    
    echo -e "${GREEN}   ✅ Emergency repair complete!${NC}"
else
    echo ""
    echo -e "${GREEN}✅ No repair needed - symlink is healthy${NC}"
fi

# Step 4: Run fortress validation
echo ""
echo -e "${YELLOW}🏰 Step 4: Running fortress validation...${NC}"
if [ -f "$FORTRESS_PY" ]; then
    python "$FORTRESS_PY" check
else
    echo -e "${RED}   ⚠️  Fortress tool not found, skipping validation${NC}"
fi

# Step 5: Final verification
echo ""
echo -e "${YELLOW}🔍 Step 5: Final verification...${NC}"
if [ -L "$LOCAL_SETTINGS" ]; then
    TARGET=$(readlink "$LOCAL_SETTINGS")
    RESOLVED=$(cd "$(dirname "$LOCAL_SETTINGS")" && readlink -f "$(basename "$LOCAL_SETTINGS")")
    echo -e "${GREEN}   ✅ Symlink exists${NC}"
    echo -e "      Raw target: $TARGET"
    echo -e "      Resolved: $RESOLVED"
    
    # Final safety check
    if [[ "$TARGET" == */tmp/* ]] || [[ "$TARGET" == */var/folders/* ]]; then
        echo -e "${RED}   ❌ WARNING: Still pointing to temp directory!${NC}"
        echo -e "${RED}   Run this script again or use: rm -f '$LOCAL_SETTINGS' && ln -sf '$GLOBAL_SETTINGS' '$LOCAL_SETTINGS'${NC}"
    else
        echo -e "${GREEN}   ✅ Recovery successful!${NC}"
    fi
else
    echo -e "${RED}   ❌ Symlink still missing!${NC}"
fi

echo ""
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${YELLOW}⚠️  IMPORTANT REMINDERS:${NC}"
echo -e "1. ${RED}NEVER${NC} click 'Yes' on permission prompts"
echo -e "2. Commands will work via pre-configured permissions"
echo -e "3. If prompted for permissions, always ${RED}DECLINE${NC}"
echo -e "4. Run 'fortress monitor' for continuous protection"
echo -e "${BLUE}═══════════════════════════════════════${NC}"