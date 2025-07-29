#!/bin/bash
# Claude Code Prompt Templates Setup Script
# Installs template library for manual customization

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Default values
TARGET_DIR=""
INTEGRATION_METHOD=""
REPO_URL="https://github.com/swm-sink/claude-code-modular-prompts"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --help)
            echo "Claude Code Template Library Setup"
            echo ""
            echo "Usage: ./setup.sh [target-directory]"
            echo ""
            echo "Integration methods (you'll be prompted):"
            echo "  1. Git Submodule - Best for ongoing updates"
            echo "  2. Direct Copy - Full standalone copy"
            echo "  3. Selective Import - Choose specific components"
            echo ""
            echo "Examples:"
            echo "  ./setup.sh ../my-project    # Install in sibling directory"
            echo "  ./setup.sh .                # Install in current directory"
            echo "  ./setup.sh /path/to/project # Install in absolute path"
            exit 0
            ;;
        *)
            TARGET_DIR="$1"
            shift
            ;;
    esac
done

# Header
echo -e "${PURPLE}╔═══════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║    Claude Code Prompt Templates Setup v2.0        ║${NC}"
echo -e "${PURPLE}║  102 templates ready for manual customization     ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════╝${NC}"
echo ""

# Get target directory if not provided
if [ -z "$TARGET_DIR" ]; then
    echo -e "${YELLOW}Where should I install the template library?${NC}"
    echo -e "${BLUE}(Enter path or press Enter for current directory)${NC}"
    read -p "> " TARGET_DIR
    TARGET_DIR=${TARGET_DIR:-.}
fi

# Resolve absolute path
TARGET_DIR=$(cd "$TARGET_DIR" 2>/dev/null && pwd || { mkdir -p "$TARGET_DIR" && cd "$TARGET_DIR" && pwd; })

# Choose integration method
echo ""
echo -e "${YELLOW}How would you like to integrate the framework?${NC}"
echo ""
echo "1) Git Submodule (Recommended)"
echo "   ✓ Easy updates from upstream"
echo "   ✓ Clean git history"
echo "   ✓ Reference stays separate"
echo ""
echo "2) Direct Copy"
echo "   ✓ Fully standalone"
echo "   ✓ No git submodule complexity"
echo "   ✓ Complete ownership"
echo ""
echo "3) Selective Import"
echo "   ✓ Choose specific components"
echo "   ✓ Minimal footprint"
echo "   ✓ Maximum control"
echo ""
read -p "Choose [1-3]: " INTEGRATION_METHOD

# Check for existing installation
if [ -d "$TARGET_DIR/.claude" ] || [ -d "$TARGET_DIR/.claude-framework" ]; then
    echo ""
    echo -e "${YELLOW}⚠️  Existing Claude Code installation detected${NC}"
    echo "Options:"
    echo "1) Upgrade existing installation"
    echo "2) Backup and fresh install"
    echo "3) Cancel"
    read -p "Choose [1-3]: " existing_choice
    
    case $existing_choice in
        1)
            echo -e "${GREEN}→ Upgrading existing installation...${NC}"
            if [ -d "$TARGET_DIR/.claude" ]; then
                mv "$TARGET_DIR/.claude" "$TARGET_DIR/.claude.pre-upgrade"
            fi
            ;;
        2)
            timestamp=$(date +%Y%m%d_%H%M%S)
            echo -e "${YELLOW}→ Backing up to .claude-backup-$timestamp...${NC}"
            [ -d "$TARGET_DIR/.claude" ] && mv "$TARGET_DIR/.claude" "$TARGET_DIR/.claude-backup-$timestamp"
            [ -d "$TARGET_DIR/.claude-framework" ] && mv "$TARGET_DIR/.claude-framework" "$TARGET_DIR/.claude-framework-backup-$timestamp"
            ;;
        3)
            echo -e "${RED}✗ Setup cancelled${NC}"
            exit 0
            ;;
    esac
fi

# Create dual structure
echo ""
echo -e "${GREEN}→ Creating template library structure...${NC}"

# Create all required directories
mkdir -p "$TARGET_DIR/.claude"/{commands/meta,components,context,config}
mkdir -p "$TARGET_DIR/.claude-adaptations"/{history,patterns,backups}

# Install framework based on chosen method
case $INTEGRATION_METHOD in
    1)
        # Git Submodule
        echo -e "${BLUE}→ Adding framework as git submodule...${NC}"
        cd "$TARGET_DIR"
        if [ -d .git ]; then
            git submodule add "$REPO_URL" .claude-framework 2>/dev/null || {
                echo -e "${YELLOW}  Submodule already exists, updating...${NC}"
                git submodule update --init .claude-framework
            }
        else
            echo -e "${YELLOW}  Target is not a git repository, using direct copy instead...${NC}"
            cp -r "$SCRIPT_DIR" "$TARGET_DIR/.claude-framework"
        fi
        ;;
        
    2)
        # Direct Copy
        echo -e "${BLUE}→ Copying framework (this may take a moment)...${NC}"
        cp -r "$SCRIPT_DIR" "$TARGET_DIR/.claude-framework"
        
        # Remove .git to make it standalone
        rm -rf "$TARGET_DIR/.claude-framework/.git"
        ;;
        
    3)
        # Selective Import
        echo -e "${BLUE}→ Selective import mode...${NC}"
        echo "Which components would you like to import?"
        echo "1) Core commands only (help, task, auto, query)"
        echo "2) Core + Development commands"
        echo "3) Core + Testing commands"
        echo "4) Core + Security commands"
        echo "5) Everything"
        read -p "Choose [1-5]: " import_choice
        
        # Create minimal framework reference
        mkdir -p "$TARGET_DIR/.claude-framework"
        
        case $import_choice in
            1)
                echo "→ Importing core commands..."
                mkdir -p "$TARGET_DIR/.claude-framework/commands/core"
                cp "$SCRIPT_DIR/.claude/commands/core"/{help,task,auto,query}.md "$TARGET_DIR/.claude-framework/commands/core/" 2>/dev/null || true
                ;;
            5)
                echo "→ Importing everything..."
                cp -r "$SCRIPT_DIR/.claude" "$TARGET_DIR/.claude-framework/"
                ;;
            *)
                echo "→ Custom selection not yet implemented, importing core..."
                mkdir -p "$TARGET_DIR/.claude-framework/commands/core"
                cp "$SCRIPT_DIR/.claude/commands/core"/*.md "$TARGET_DIR/.claude-framework/commands/core/" 2>/dev/null || true
                ;;
        esac
        ;;
esac

# Make framework read-only
echo -e "${GREEN}→ Making framework reference read-only...${NC}"
chmod -R a-w "$TARGET_DIR/.claude-framework" 2>/dev/null || true

# Initialize project-config.yaml
echo -e "${GREEN}→ Creating project configuration...${NC}"
cat > "$TARGET_DIR/.claude/config/project-config.yaml" << 'EOF'
# Claude Code Template Library - Project Configuration
project_config:
  version: "1.0"
  metadata:
    name: "[INSERT_PROJECT_NAME]"
    domain: "[INSERT_DOMAIN]"
    created: "$(date -u +%Y-%m-%d)"
    adaptation_mode: "not-started"
    readiness_score: 0
  
  placeholders:
    # Core placeholders - will be replaced during adaptation
    PROJECT_NAME: "[INSERT_PROJECT_NAME]"
    DOMAIN: "[INSERT_DOMAIN]"
    TECH_STACK: "[INSERT_TECH_STACK]"
    COMPANY_NAME: "[INSERT_COMPANY_NAME]"
    TEAM_SIZE: "[INSERT_TEAM_SIZE]"
    WORKFLOW_TYPE: "[INSERT_WORKFLOW_TYPE]"
    PRIMARY_LANGUAGE: "[INSERT_PRIMARY_LANGUAGE]"
    TESTING_FRAMEWORK: "[INSERT_TESTING_FRAMEWORK]"
    CI_CD_PLATFORM: "[INSERT_CI_CD_PLATFORM]"
    DEPLOYMENT_TARGET: "[INSERT_DEPLOYMENT_TARGET]"
    DATABASE_TYPE: "[INSERT_DATABASE_TYPE]"
    API_STYLE: "[INSERT_API_STYLE]"
    SECURITY_LEVEL: "[INSERT_SECURITY_LEVEL]"
    PERFORMANCE_PRIORITY: "[INSERT_PERFORMANCE_PRIORITY]"
    USER_BASE: "[INSERT_USER_BASE]"
  
  adaptations:
    applied: []
    # Adaptations will be tracked here
EOF

# Copy meta-commands
echo -e "${GREEN}→ Installing template customization commands...${NC}"
if [ -d "$SCRIPT_DIR/.claude/commands/meta" ]; then
    cp -r "$SCRIPT_DIR/.claude/commands/meta" "$TARGET_DIR/.claude/commands/"
else
    # Create a basic adapt-to-project command if not found
    mkdir -p "$TARGET_DIR/.claude/commands/meta"
    echo -e "${YELLOW}  Creating starter meta-command...${NC}"
fi

# Copy essential context files for anti-pattern prevention
echo -e "${GREEN}→ Installing anti-pattern prevention...${NC}"
if [ -d "$SCRIPT_DIR/.claude/context" ]; then
    cp "$SCRIPT_DIR/.claude/context"/*.md "$TARGET_DIR/.claude/context/" 2>/dev/null || true
fi

# Create initial CLAUDE.md for the project
echo -e "${GREEN}→ Creating project memory file...${NC}"
cat > "$TARGET_DIR/CLAUDE.md" << 'EOF'
# Claude Code Project - Template Library Installed

This project has the Claude Code template library installed and ready for manual customization.

## 🚀 Quick Start

Start a Claude Code conversation and run:
```
/adapt-to-project
```

This will guide you through the manual customization process with checklists and instructions.

## 📁 Structure

- `.claude/` - Your customized commands and configuration (will be populated during adaptation)
- `.claude-framework/` - Reference library (read-only, preserved for updates)
- `.claude-adaptations/` - Adaptation history and patterns

## 🎯 Adaptation Status

**Readiness Score**: 0% (Not adapted yet)

Run `/adapt-to-project` to begin customization.

---
*Template Library installed on $(date)*
EOF

# Create a validation script
echo -e "${GREEN}→ Creating validation script...${NC}"
cat > "$TARGET_DIR/.claude/validate.sh" << 'EOF'
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
EOF
chmod +x "$TARGET_DIR/.claude/validate.sh"

# Final summary
echo ""
echo -e "${PURPLE}╔═══════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║       Template Library Installed! 🎉              ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}✅ Installation Complete${NC}"
echo ""
echo -e "${BLUE}What was installed:${NC}"
echo "  📁 Dual structure created:"
echo "     • .claude/ (your workspace)"
echo "     • .claude-framework/ (reference library)"
echo "     • .claude-adaptations/ (tracking & history)"
echo "  📝 Project configuration initialized"
echo "  🛡️ Anti-pattern prevention ready"
echo "  🔧 Meta-commands for adaptation"
echo ""
echo -e "${YELLOW}🚀 Next Steps:${NC}"
echo ""
echo "  1. cd $TARGET_DIR"
echo "  2. Start Claude Code"
echo "  3. Run: ${GREEN}/adapt-to-project${NC}"
echo "     (This will provide manual customization guides)"
echo ""
echo -e "${BLUE}📊 Current Status:${NC}"
echo "  Readiness: 0% (awaiting adaptation)"
echo "  Placeholders: Active (need replacement)"
echo "  Configuration: Default (needs customization)"
echo ""
echo -e "${PURPLE}Ready to customize proven prompt templates!${NC}"
echo ""
echo "Run ${GREEN}.claude/validate.sh${NC} anytime to check adaptation progress"