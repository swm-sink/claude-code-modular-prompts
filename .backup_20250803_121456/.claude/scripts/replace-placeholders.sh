#!/bin/bash
# Enhanced Placeholder Replacement Script - Research-Based Implementation
# Automated replacement of placeholders in Claude Code templates using framework detection

set -e

PROJECT_PATH="${1:-.}"
DRY_RUN="${2:-false}"
BACKUP_ENABLED="${3:-true}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}✅${NC} $1"
}

warning() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

error() {
    echo -e "${RED}❌${NC} $1"
}

# Enhanced framework detection
detect_project_values() {
    log "Running enhanced framework detection..."
    
    # Use the framework detection script if available
    local detection_script="$PROJECT_PATH/.claude/scripts/detect-framework.sh"
    if [[ -f "$detection_script" ]]; then
        local detection_output
        detection_output=$("$detection_script" "$PROJECT_PATH" json)
        
        # Parse JSON output (simplified)
        PROJECT_NAME=$(echo "$detection_output" | grep -o '"name": "[^"]*"' | cut -d'"' -f4)
        PROJECT_TYPE=$(echo "$detection_output" | grep -o '"project_type": "[^"]*"' | cut -d'"' -f4)
    fi
    
    # Fallback to manual detection
    if [[ -z "$PROJECT_NAME" ]]; then
        if [[ -f "$PROJECT_PATH/package.json" ]]; then
            PROJECT_NAME=$(grep -o '"name":\s*"[^"]*"' "$PROJECT_PATH/package.json" | cut -d'"' -f4)
        fi
        PROJECT_NAME="${PROJECT_NAME:-$(basename "$PROJECT_PATH")}"
    fi
    
    # Enhanced tech stack detection
    TECH_STACK="Unknown"
    PRIMARY_LANGUAGE="JavaScript"
    TESTING_FRAMEWORK="Jest"
    BUILD_TOOL="npm"
    
    # JavaScript/Node.js detection
    if [[ -f "$PROJECT_PATH/package.json" ]]; then
        local package_content=$(cat "$PROJECT_PATH/package.json")
        PRIMARY_LANGUAGE="JavaScript"
        
        # TypeScript detection
        if [[ -f "$PROJECT_PATH/tsconfig.json" ]] || echo "$package_content" | grep -q '"typescript"'; then
            PRIMARY_LANGUAGE="TypeScript"
            TECH_STACK="TypeScript"
        else
            TECH_STACK="JavaScript"
        fi
        
        # Framework detection
        echo "$package_content" | grep -q '"react"' && TECH_STACK="$TECH_STACK + React"
        echo "$package_content" | grep -q '"vue"' && TECH_STACK="$TECH_STACK + Vue.js"
        echo "$package_content" | grep -q '"angular"' && TECH_STACK="$TECH_STACK + Angular"
        echo "$package_content" | grep -q '"express"' && TECH_STACK="$TECH_STACK + Express"
        echo "$package_content" | grep -q '"next"' && TECH_STACK="$TECH_STACK + Next.js"
        
        # Testing framework detection
        echo "$package_content" | grep -q '"jest"' && TESTING_FRAMEWORK="Jest"
        echo "$package_content" | grep -q '"vitest"' && TESTING_FRAMEWORK="Vitest"
        echo "$package_content" | grep -q '"mocha"' && TESTING_FRAMEWORK="Mocha"
        
        # Build tool detection
        echo "$package_content" | grep -q '"vite"' && BUILD_TOOL="Vite"
        echo "$package_content" | grep -q '"webpack"' && BUILD_TOOL="Webpack"
    fi
    
    # Python detection
    if [[ -f "$PROJECT_PATH/requirements.txt" ]] || [[ -f "$PROJECT_PATH/setup.py" ]] || [[ -f "$PROJECT_PATH/pyproject.toml" ]]; then
        PRIMARY_LANGUAGE="Python"
        TECH_STACK="Python"
        TESTING_FRAMEWORK="pytest"
        BUILD_TOOL="pip"
        
        if [[ -f "$PROJECT_PATH/requirements.txt" ]]; then
            local req_content=$(cat "$PROJECT_PATH/requirements.txt")
            echo "$req_content" | grep -q "django" && TECH_STACK="$TECH_STACK + Django"
            echo "$req_content" | grep -q "flask" && TECH_STACK="$TECH_STACK + Flask"
            echo "$req_content" | grep -q "fastapi" && TECH_STACK="$TECH_STACK + FastAPI"
        fi
        
        [[ -f "$PROJECT_PATH/manage.py" ]] && TECH_STACK="$TECH_STACK + Django"
    fi
    
    # Get git author information
    if [[ -d "$PROJECT_PATH/.git" ]]; then
        GIT_AUTHOR=$(git -C "$PROJECT_PATH" config user.name 2>/dev/null || echo "Developer")
        GIT_EMAIL=$(git -C "$PROJECT_PATH" config user.email 2>/dev/null || echo "developer@example.com")
    else
        GIT_AUTHOR="Developer"
        GIT_EMAIL="developer@example.com"
    fi
    
    # Domain classification
    case "$PROJECT_TYPE" in
        "fullstack-web-app") DOMAIN="web-development" ;;
        "api-backend") DOMAIN="backend-api" ;;
        "frontend-spa") DOMAIN="frontend-development" ;;
        "cli-tool") DOMAIN="cli-development" ;;
        *) DOMAIN="software-development" ;;
    esac

    
    log "Detected project values:"
    echo "  Project Name: $PROJECT_NAME"
    echo "  Domain: $DOMAIN"
    echo "  Tech Stack: $TECH_STACK"
    echo "  Primary Language: $PRIMARY_LANGUAGE"
    echo "  Testing Framework: $TESTING_FRAMEWORK"
    echo "  Build Tool: $BUILD_TOOL"
    echo "  Author: $GIT_AUTHOR"
}

# Create backup if enabled
create_backup() {
    if [[ "$BACKUP_ENABLED" == "true" && "$DRY_RUN" == "false" ]]; then
        local backup_dir="$PROJECT_PATH/.claude.backup"
        if [[ -d "$PROJECT_PATH/.claude" ]]; then
            log "Creating backup at $backup_dir"
            cp -r "$PROJECT_PATH/.claude" "$backup_dir"
            success "Backup created successfully"
        fi
    fi
}

# Count total placeholders
count_placeholders() {
    local total=0
    local claude_dir="$PROJECT_PATH/.claude"
    
    if [[ -d "$claude_dir/commands" ]]; then
        while IFS= read -r -d '' file; do
            local count
            count=$(grep -c '\[INSERT_[^]]*\]' "$file" 2>/dev/null || true)
            total=$((total + count))
        done < <(find "$claude_dir/commands" -name "*.md" -print0)
    fi
    
    echo "$total"
}

# Enhanced replacement function
perform_replacements() {
    local claude_dir="$PROJECT_PATH/.claude"
    local total_replaced=0
    local files_processed=0
    
    if [[ ! -d "$claude_dir/commands" ]]; then
        error "Commands directory not found at $claude_dir/commands"
        return 1
    fi
    
    log "Starting comprehensive placeholder replacement..."
    
    # Define all replacements
    declare -A replacements=(
        ["[INSERT_PROJECT_NAME]"]="$PROJECT_NAME"
        ["[INSERT_DOMAIN]"]="$DOMAIN"
        ["[INSERT_TECH_STACK]"]="$TECH_STACK"
        ["[INSERT_PRIMARY_LANGUAGE]"]="$PRIMARY_LANGUAGE"
        ["[INSERT_TESTING_FRAMEWORK]"]="$TESTING_FRAMEWORK"
        ["[INSERT_BUILD_TOOL]"]="$BUILD_TOOL"
        ["[INSERT_AUTHOR]"]="$GIT_AUTHOR"
        ["[INSERT_EMAIL]"]="$GIT_EMAIL"
        ["[INSERT_COMPANY_NAME]"]="$GIT_AUTHOR Development"
        ["[INSERT_VERSION]"]="1.0.0"
        ["[INSERT_LICENSE]"]="MIT"
        ["[INSERT_CI_CD_PLATFORM]"]="GitHub Actions"
        ["[INSERT_DEPLOYMENT_TARGET]"]="Production"
        ["[INSERT_TEAM_SIZE]"]="Small Team"
        ["[INSERT_WORKFLOW_TYPE]"]="Agile"
        ["[INSERT_USER_BASE]"]="users"
        ["[INSERT_SECURITY_LEVEL]"]="standard"
        ["[INSERT_PERFORMANCE_PRIORITY]"]="balanced"
        ["[INSERT_SRC_DIR]"]="src"
        ["[INSERT_TEST_DIR]"]="tests"
        ["[INSERT_BUILD_DIR]"]="build"
        ["[INSERT_DATABASE_TYPE]"]="PostgreSQL"
        ["[INSERT_API_VERSION]"]="v1"
        ["[INSERT_PORT]"]="3000"
        ["[INSERT_ENVIRONMENT]"]="development"
    )
    
    # Process all command files
    while IFS= read -r -d '' file; do
        local file_modified=false
        local file_replacements=0
        
        for placeholder in "${!replacements[@]}"; do
            local replacement="${replacements[$placeholder]}"
            
            # Count occurrences
            local count
            count=$(grep -c "$placeholder" "$file" 2>/dev/null || true)
            
            if [[ $count -gt 0 ]]; then
                if [[ "$DRY_RUN" == "false" ]]; then
                    # Perform replacement using sed
                    local escaped_placeholder
                    local escaped_replacement
                    escaped_placeholder=$(echo "$placeholder" | sed 's/[][\.*^$()+?{|}/\\&/g')
                    escaped_replacement=$(echo "$replacement" | sed 's/[[\.*^$()+?{|]/\\&/g')
                    
                    sed -i.bak "s|$escaped_placeholder|$escaped_replacement|g" "$file"
                    rm "$file.bak" 2>/dev/null || true
                fi
                
                file_replacements=$((file_replacements + count))
                file_modified=true
            fi
        done
        
        if [[ "$file_modified" == "true" ]]; then
            files_processed=$((files_processed + 1))
            total_replaced=$((total_replaced + file_replacements))
            
            if [[ "$DRY_RUN" == "true" ]]; then
                echo "  [DRY RUN] $(basename "$file") - $file_replacements replacements"
            else
                echo "  ✅ $(basename "$file") - $file_replacements replacements"
            fi
        fi
        
    done < <(find "$claude_dir/commands" -name "*.md" -print0)
    
    log "Replacement summary:"
    echo "  Files processed: $files_processed"
    echo "  Total replacements: $total_replaced"
    
    return 0
}

# Validate results
validate_replacements() {
    local remaining
    remaining=$(count_placeholders)
    
    if [[ $remaining -eq 0 ]]; then
        success "All placeholders successfully replaced"
        return 0
    else
        warning "$remaining placeholders remain unprocessed"
        return 1
    fi
}

# Main execution function
main() {
    log "Enhanced Placeholder Replacement System"
    echo "Project: $PROJECT_PATH"
    echo "Mode: $(if [[ "$DRY_RUN" == "true" ]]; then echo "DRY RUN"; else echo "LIVE"; fi)"
    echo ""
    
    # Check if project has .claude directory
    if [[ ! -d "$PROJECT_PATH/.claude" ]]; then
        error ".claude directory not found at $PROJECT_PATH"
        echo "Please run this script from a project with Claude Code templates."
        exit 1
    fi
    
    # Count initial placeholders
    local initial_count
    initial_count=$(count_placeholders)
    log "Found $initial_count placeholders to replace"
    
    if [[ $initial_count -eq 0 ]]; then
        success "No placeholders found - project already customized"
        exit 0
    fi
    
    # Execute main workflow
    create_backup
    detect_project_values
    perform_replacements
    
    if [[ "$DRY_RUN" == "false" ]]; then
        validate_replacements
    fi
    
    echo ""
    if [[ "$DRY_RUN" == "true" ]]; then
        log "DRY RUN COMPLETE - No changes made"
        echo "Run without 'true' as second argument to perform actual replacement"
    else
        success "Placeholder replacement complete!"
        echo "Your Claude Code templates are now customized for your project"
    fi
}

# Handle help
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    echo "Enhanced Placeholder Replacement System"
    echo "Usage: $0 [PROJECT_PATH] [DRY_RUN] [BACKUP_ENABLED]"
    echo ""
    echo "Arguments:"
    echo "  PROJECT_PATH: Path to project directory (default: current directory)"
    echo "  DRY_RUN: 'true' for preview mode, 'false' for actual replacement (default: false)"
    echo "  BACKUP_ENABLED: 'true' to create backup, 'false' to skip (default: true)"
    echo ""
    echo "Examples:"
    echo "  $0                          # Replace in current directory"
    echo "  $0 /path/to/project         # Replace in specific project" 
    echo "  $0 . true                   # Dry run preview"
    echo "  $0 . false false            # Replace without backup"
    exit 0
fi

main "$@"