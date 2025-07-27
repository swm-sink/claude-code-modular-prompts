#!/bin/bash
# Claude Code Framework Adaptation Script
# Adapts framework patterns to existing projects

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Default values
TARGET_DIR=""
PROFILE="general"
UPDATE_MODE=false
PRESERVE_CUSTOM=true

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --target)
            TARGET_DIR="$2"
            shift 2
            ;;
        --profile)
            PROFILE="$2"
            shift 2
            ;;
        --update)
            UPDATE_MODE=true
            shift
            ;;
        --preserve-custom)
            PRESERVE_CUSTOM=true
            shift
            ;;
        --help)
            echo "Usage: ./adapt.sh --target PROJECT_DIR [options]"
            echo ""
            echo "Options:"
            echo "  --target DIR          Target project directory (required)"
            echo "  --profile PROFILE     Choose profile: general, web-dev, data-science, devops"
            echo "  --update             Update existing integration"
            echo "  --preserve-custom    Preserve customizations during update"
            echo "  --help               Show this help message"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Validate target
if [ -z "$TARGET_DIR" ]; then
    echo -e "${RED}Error: --target directory required${NC}"
    echo "Usage: ./adapt.sh --target ../my-project"
    exit 1
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}Error: Target directory does not exist: $TARGET_DIR${NC}"
    exit 1
fi

# Header
echo -e "${PURPLE}╔════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║    Claude Code Framework Adaptation        ║${NC}"
echo -e "${PURPLE}║    Customizing patterns for your project   ║${NC}"
echo -e "${PURPLE}╚════════════════════════════════════════════╝${NC}"
echo ""

# Function to analyze project
analyze_project() {
    echo -e "${BLUE}→ Analyzing target project...${NC}"
    
    # Detect project type
    PROJECT_TYPE="general"
    
    if [ -f "$TARGET_DIR/package.json" ]; then
        if grep -q "react\|vue\|angular" "$TARGET_DIR/package.json" 2>/dev/null; then
            PROJECT_TYPE="web-dev"
            echo "  ✓ Detected: Web development project"
        elif grep -q "express\|fastify\|koa" "$TARGET_DIR/package.json" 2>/dev/null; then
            PROJECT_TYPE="backend"
            echo "  ✓ Detected: Backend project"
        fi
    elif [ -f "$TARGET_DIR/requirements.txt" ] || [ -f "$TARGET_DIR/setup.py" ]; then
        if grep -q "pandas\|numpy\|scikit" "$TARGET_DIR/requirements.txt" 2>/dev/null; then
            PROJECT_TYPE="data-science"
            echo "  ✓ Detected: Data science project"
        fi
    elif [ -f "$TARGET_DIR/Dockerfile" ] || [ -f "$TARGET_DIR/.gitlab-ci.yml" ]; then
        PROJECT_TYPE="devops"
        echo "  ✓ Detected: DevOps project"
    fi
    
    # Override with user profile if specified
    if [ "$PROFILE" != "general" ]; then
        PROJECT_TYPE="$PROFILE"
        echo "  → Using specified profile: $PROFILE"
    fi
}

# Function to select patterns
select_patterns() {
    echo -e "${BLUE}→ Selecting patterns for $PROJECT_TYPE...${NC}"
    
    # Create temp directory for selected patterns
    TEMP_DIR=$(mktemp -d)
    
    case $PROJECT_TYPE in
        web-dev)
            # Frontend patterns
            cp .claude/commands/core/{help,task,auto,query}.md "$TEMP_DIR/" 2>/dev/null || true
            cp .claude/commands/development/dev.md "$TEMP_DIR/" 2>/dev/null || true
            cp .claude/commands/quality/test.md "$TEMP_DIR/" 2>/dev/null || true
            
            # Add web-specific
            cat > "$TEMP_DIR/component.md" << 'EOF'
---
name: /component
description: Create frontend components
---

I'll help you create a component. What type do you need?
EOF
            ;;
            
        data-science)
            # Analysis patterns
            cp .claude/commands/core/{help,task,auto,query}.md "$TEMP_DIR/" 2>/dev/null || true
            cp .claude/commands/quality/analyze-*.md "$TEMP_DIR/" 2>/dev/null || true
            
            # Add data-specific
            cat > "$TEMP_DIR/notebook.md" << 'EOF'
---
name: /notebook
description: Jupyter notebook assistance
---

I'll help with your notebook. What analysis are you working on?
EOF
            ;;
            
        devops)
            # Infrastructure patterns
            cp .claude/commands/core/{help,auto}.md "$TEMP_DIR/" 2>/dev/null || true
            cp .claude/commands/pipeline.md "$TEMP_DIR/" 2>/dev/null || true
            cp .claude/commands/development/project/deploy.md "$TEMP_DIR/" 2>/dev/null || true
            ;;
            
        *)
            # General patterns
            cp .claude/commands/core/{help,task,auto,query,dev}.md "$TEMP_DIR/" 2>/dev/null || true
            ;;
    esac
}

# Function to simplify patterns
simplify_patterns() {
    echo -e "${BLUE}→ Simplifying patterns for easier use...${NC}"
    
    # Remove complex XML structures
    find "$TEMP_DIR" -name "*.md" -type f | while read -r file; do
        # Keep YAML frontmatter, simplify content
        sed -i.bak '/<[^>]*>/d' "$file" 2>/dev/null || true
        
        # Remove complex component includes
        sed -i.bak '/include.*components/d' "$file" 2>/dev/null || true
        
        # Clean up backup files
        rm -f "$file.bak"
    done
}

# Function to install adapted patterns
install_patterns() {
    echo -e "${GREEN}→ Installing adapted patterns...${NC}"
    
    # Backup existing if updating
    if [ "$UPDATE_MODE" = true ] && [ -d "$TARGET_DIR/.claude" ]; then
        echo "  → Backing up existing configuration..."
        cp -r "$TARGET_DIR/.claude" "$TARGET_DIR/.claude.backup.$(date +%Y%m%d_%H%M%S)"
    fi
    
    # Create structure
    mkdir -p "$TARGET_DIR/.claude"/{commands,components,context}
    
    # Copy adapted commands
    cp "$TEMP_DIR"/*.md "$TARGET_DIR/.claude/commands/" 2>/dev/null || true
    
    # Copy essential components (simplified)
    mkdir -p "$TARGET_DIR/.claude/components"
    cp .claude/components/validation/input-validation.md "$TARGET_DIR/.claude/components/" 2>/dev/null || true
    cp .claude/components/error-handling.md "$TARGET_DIR/.claude/components/" 2>/dev/null || true
    
    # Copy critical context (anti-patterns)
    cp .claude/context/llm-antipatterns.md "$TARGET_DIR/.claude/context/" 2>/dev/null || true
    cp .claude/context/git-history-antipatterns.md "$TARGET_DIR/.claude/context/" 2>/dev/null || true
    
    # Preserve custom commands if updating
    if [ "$UPDATE_MODE" = true ] && [ "$PRESERVE_CUSTOM" = true ]; then
        if [ -d "$TARGET_DIR/.claude.backup."* ]; then
            latest_backup=$(ls -t "$TARGET_DIR"/.claude.backup.* | head -1)
            if [ -d "$latest_backup/commands/custom" ]; then
                echo "  → Preserving custom commands..."
                cp -r "$latest_backup/commands/custom" "$TARGET_DIR/.claude/commands/" 2>/dev/null || true
            fi
        fi
    fi
    
    # Clean up temp
    rm -rf "$TEMP_DIR"
}

# Function to create project config
create_config() {
    echo -e "${GREEN}→ Creating project configuration...${NC}"
    
    PROJECT_NAME=$(basename "$TARGET_DIR")
    
    cat > "$TARGET_DIR/.claude/PROJECT.md" << EOF
# $PROJECT_NAME - Claude Code Integration

## Framework Version
Adapted from Claude Code Modular Prompts on $(date)
Profile: $PROJECT_TYPE

## Customization Notes
- Patterns have been simplified for easier use
- XML complexity removed
- Add your own commands in .claude/commands/

## Anti-Patterns Active
The following anti-patterns are being prevented:
- LLM hallucinations and metric invention
- Git commit theater and false success claims
- See .claude/context/ for details

## Quick Commands
- \`/help\` - See available commands
- \`/task\` - TDD workflow
- \`/auto\` - Smart task routing

---
*To update: run adapt.sh --update from framework directory*
EOF
}

# Main execution
analyze_project
select_patterns
simplify_patterns
install_patterns
create_config

# Summary
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║        Adaptation Complete! 🎉             ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}What was adapted:${NC}"
echo "  ✓ Patterns selected for $PROJECT_TYPE"
echo "  ✓ Complex XML removed for simplicity"
echo "  ✓ Anti-patterns protection installed"
echo "  ✓ Project configuration created"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. cd $TARGET_DIR"
echo "  2. Review .claude/commands/"
echo "  3. Add project-specific commands"
echo "  4. Test with Claude Code"
echo ""
echo -e "${GREEN}Your project now has professional Claude Code integration!${NC}"