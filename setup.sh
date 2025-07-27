#!/bin/bash
# Claude Code Framework Setup Script
# Initializes framework in user's project

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
PROJECT_NAME=""
PROFILE="general"
TARGET_DIR="../"
PRESERVE_EXISTING=true

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --project-name)
            PROJECT_NAME="$2"
            shift 2
            ;;
        --profile)
            PROFILE="$2"
            shift 2
            ;;
        --target)
            TARGET_DIR="$2"
            shift 2
            ;;
        --force)
            PRESERVE_EXISTING=false
            shift
            ;;
        --help)
            echo "Usage: ./setup.sh [options]"
            echo ""
            echo "Options:"
            echo "  --project-name NAME    Set project name for customization"
            echo "  --profile PROFILE      Choose profile: general, web-dev, data-science, devops, custom"
            echo "  --target DIR          Target directory (default: ../)"
            echo "  --force               Overwrite existing .claude directory"
            echo "  --help                Show this help message"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Header
echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Claude Code Framework Setup v1.0      ║${NC}"
echo -e "${BLUE}║  6+ months of knowledge in 5 minutes   ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Get project name if not provided
if [ -z "$PROJECT_NAME" ]; then
    echo -e "${YELLOW}What's your project name?${NC}"
    read -p "> " PROJECT_NAME
fi

# Check if .claude exists
if [ -d "$TARGET_DIR/.claude" ] && [ "$PRESERVE_EXISTING" = true ]; then
    echo -e "${YELLOW}⚠️  .claude directory already exists in target.${NC}"
    echo "Options:"
    echo "1) Merge with existing (recommended)"
    echo "2) Backup and replace"
    echo "3) Cancel"
    read -p "Choose [1-3]: " choice
    
    case $choice in
        1)
            echo -e "${GREEN}→ Merging with existing configuration...${NC}"
            ;;
        2)
            echo -e "${YELLOW}→ Backing up existing .claude to .claude.backup...${NC}"
            mv "$TARGET_DIR/.claude" "$TARGET_DIR/.claude.backup"
            ;;
        3)
            echo -e "${RED}✗ Setup cancelled${NC}"
            exit 0
            ;;
    esac
fi

# Create directory structure
echo -e "${GREEN}→ Creating directory structure...${NC}"
mkdir -p "$TARGET_DIR/.claude"/{commands,components,context,templates}

# Function to copy with filtering
copy_commands() {
    local source_pattern=$1
    local dest_dir=$2
    local description=$3
    
    echo -e "${BLUE}  → Installing $description...${NC}"
    mkdir -p "$dest_dir"
    
    # Copy files matching pattern
    find .claude/commands -name "$source_pattern" -type f | while read -r file; do
        cp "$file" "$dest_dir/" 2>/dev/null || true
    done
}

# Install based on profile
echo -e "${GREEN}→ Installing $PROFILE profile...${NC}"

case $PROFILE in
    general)
        # Core commands only
        copy_commands "help.md" "$TARGET_DIR/.claude/commands/core" "help command"
        copy_commands "task.md" "$TARGET_DIR/.claude/commands/core" "task command"
        copy_commands "auto.md" "$TARGET_DIR/.claude/commands/core" "auto command"
        copy_commands "query.md" "$TARGET_DIR/.claude/commands/core" "query command"
        copy_commands "dev.md" "$TARGET_DIR/.claude/commands/development" "dev command"
        ;;
        
    web-dev)
        # Core + web development
        copy_commands "*.md" "$TARGET_DIR/.claude/commands/core" "core commands"
        copy_commands "dev*.md" "$TARGET_DIR/.claude/commands/development" "development commands"
        copy_commands "test*.md" "$TARGET_DIR/.claude/commands/testing" "testing commands"
        # Add web-specific patterns
        cat > "$TARGET_DIR/.claude/commands/web/component-gen.md" << 'EOF'
---
name: /component-gen
description: Generate React/Vue/Angular components
---

I'll help you generate a component. Which framework are you using?
EOF
        ;;
        
    data-science)
        # Core + data science
        copy_commands "*.md" "$TARGET_DIR/.claude/commands/core" "core commands"
        copy_commands "analyze*.md" "$TARGET_DIR/.claude/commands/analysis" "analysis commands"
        copy_commands "query*.md" "$TARGET_DIR/.claude/commands/analysis" "query commands"
        ;;
        
    devops)
        # Core + DevOps
        copy_commands "*.md" "$TARGET_DIR/.claude/commands/core" "core commands"
        copy_commands "pipeline*.md" "$TARGET_DIR/.claude/commands/devops" "pipeline commands"
        copy_commands "deploy*.md" "$TARGET_DIR/.claude/commands/devops" "deployment commands"
        copy_commands "monitor*.md" "$TARGET_DIR/.claude/commands/devops" "monitoring commands"
        ;;
        
    custom)
        echo -e "${YELLOW}Interactive selection coming soon. Using general profile for now.${NC}"
        copy_commands "*.md" "$TARGET_DIR/.claude/commands/core" "core commands"
        ;;
esac

# Copy essential components
echo -e "${GREEN}→ Installing components...${NC}"
cp -r .claude/components/* "$TARGET_DIR/.claude/components/" 2>/dev/null || true

# Copy context files (critical for anti-patterns)
echo -e "${GREEN}→ Installing context engineering...${NC}"
cp .claude/context/*.md "$TARGET_DIR/.claude/context/" 2>/dev/null || true

# Create project-specific CLAUDE.md
echo -e "${GREEN}→ Creating project configuration...${NC}"
cat > "$TARGET_DIR/.claude/CLAUDE.md" << EOF
# $PROJECT_NAME - Claude Code Configuration

This project uses the Claude Code Modular Prompts framework.

## Active Commands
- \`/help\` - List available commands
- \`/task\` - TDD workflow guidance  
- \`/auto\` - Intelligent task routing
- See \`.claude/commands/\` for all available commands

## Anti-Patterns
Anti-patterns are automatically loaded from \`.claude/context/\` to prevent common mistakes.

## Customization
Add project-specific commands in \`.claude/commands/$PROJECT_NAME/\`

---
*Framework integrated on $(date)*
EOF

# Create a simple adapter for common customizations
cat > "$TARGET_DIR/.claude/adapt.sh" << 'EOF'
#!/bin/bash
# Quick adaptation script for common customizations

echo "Quick customization options:"
echo "1) Simplify XML patterns"
echo "2) Add domain command"
echo "3) Remove unused commands"
read -p "Choose [1-3]: " choice

case $choice in
    1)
        echo "Simplifying XML patterns..."
        find .claude/commands -name "*.md" -exec sed -i.bak 's/<[^>]*>//g' {} \;
        echo "✓ XML patterns removed"
        ;;
    2)
        read -p "Command name (e.g., deploy): " cmd_name
        mkdir -p .claude/commands/custom
        cat > .claude/commands/custom/$cmd_name.md << 'EOC'
---
name: /$cmd_name
description: Custom command
---

Your command implementation here...
EOC
        echo "✓ Created /custom/$cmd_name"
        ;;
    3)
        ls .claude/commands
        read -p "Directory to remove: " dir_name
        mv .claude/commands/$dir_name .claude/commands/.$dir_name.archived
        echo "✓ Archived $dir_name commands"
        ;;
esac
EOF
chmod +x "$TARGET_DIR/.claude/adapt.sh"

# Final summary
echo ""
echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║         Setup Complete! 🎉             ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}What was installed:${NC}"
echo "  ✓ Claude Code commands for $PROFILE profile"
echo "  ✓ Reusable components library"
echo "  ✓ Anti-pattern prevention system"
echo "  ✓ Context engineering framework"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. cd $TARGET_DIR"
echo "  2. Review .claude/commands/ and remove unwanted patterns"
echo "  3. Run .claude/adapt.sh for quick customizations"
echo "  4. Start Claude Code and try /help"
echo ""
echo -e "${GREEN}You just saved 6+ months of Claude Code learning!${NC}"
echo ""
echo -e "${BLUE}Need help?${NC} See SETUP.md or visit GitHub issues"