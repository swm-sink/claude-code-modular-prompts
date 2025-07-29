#!/bin/bash
# Placeholder Replacement Script for /adapt-to-project command
# This script replaces placeholders in Claude Code templates

set -e

CONFIG_FILE="${1:-/tmp/project-detection.json}"
CLAUDE_DIR="${2:-.claude}"
DRY_RUN="${3:-false}"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Error: Config file not found: $CONFIG_FILE"
    echo "Run detect-project.sh first to generate the configuration."
    exit 1
fi

echo "🔄 Starting placeholder replacement..."

# Read values from JSON (basic parsing without jq dependency)
PROJECT_NAME=$(grep '"project_name"' "$CONFIG_FILE" | sed 's/.*"project_name": *"\([^"]*\)".*/\1/')
DOMAIN=$(grep '"domain"' "$CONFIG_FILE" | sed 's/.*"domain": *"\([^"]*\)".*/\1/')
TECH_STACK=$(grep '"tech_stack"' "$CONFIG_FILE" | sed 's/.*"tech_stack": *"\([^"]*\)".*/\1/')
PRIMARY_LANGUAGE=$(grep '"primary_language"' "$CONFIG_FILE" | sed 's/.*"primary_language": *"\([^"]*\)".*/\1/')
TESTING_FRAMEWORK=$(grep '"testing_framework"' "$CONFIG_FILE" | sed 's/.*"testing_framework": *"\([^"]*\)".*/\1/')
CI_CD_PLATFORM=$(grep '"ci_cd_platform"' "$CONFIG_FILE" | sed 's/.*"ci_cd_platform": *"\([^"]*\)".*/\1/')

echo "📋 Using configuration:"
echo "  Project Name: $PROJECT_NAME"
echo "  Domain: $DOMAIN"
echo "  Tech Stack: $TECH_STACK"
echo "  Primary Language: $PRIMARY_LANGUAGE"
echo "  Testing Framework: $TESTING_FRAMEWORK"
echo "  CI/CD Platform: $CI_CD_PLATFORM"
echo ""

# Find all files with placeholders
PLACEHOLDER_FILES=$(find "$CLAUDE_DIR/commands" -name "*.md" -type f -exec grep -l "\[INSERT_" {} \; 2>/dev/null)

if [ -z "$PLACEHOLDER_FILES" ]; then
    echo "✅ No placeholder files found to update."
    exit 0
fi

echo "📁 Files containing placeholders:"
echo "$PLACEHOLDER_FILES" | while read file; do echo "  - $file"; done
echo ""

REPLACEMENT_COUNT=0

# Function to perform replacement
replace_in_file() {
    local file="$1"
    local search="$2"
    local replace="$3"
    
    if grep -q "$search" "$file" 2>/dev/null; then
        if [ "$DRY_RUN" = "true" ]; then
            echo "  [DRY RUN] Would replace '$search' with '$replace' in $file"
        else
            # Use sed to replace placeholders
            if [[ "$OSTYPE" == "darwin"* ]]; then
                # macOS sed
                sed -i '' "s/$search/$replace/g" "$file"
            else
                # GNU sed
                sed -i "s/$search/$replace/g" "$file"
            fi
            echo "  ✅ Replaced '$search' with '$replace' in $file"
        fi
        REPLACEMENT_COUNT=$((REPLACEMENT_COUNT + 1))
    fi
}

# Escape special characters for sed
escape_for_sed() {
    echo "$1" | sed 's/[[\.*^$()+?{|]/\\&/g'
}

# Escape the replacement values
SAFE_PROJECT_NAME=$(escape_for_sed "$PROJECT_NAME")
SAFE_DOMAIN=$(escape_for_sed "$DOMAIN")
SAFE_TECH_STACK=$(escape_for_sed "$TECH_STACK")
SAFE_PRIMARY_LANGUAGE=$(escape_for_sed "$PRIMARY_LANGUAGE")
SAFE_TESTING_FRAMEWORK=$(escape_for_sed "$TESTING_FRAMEWORK")
SAFE_CI_CD_PLATFORM=$(escape_for_sed "$CI_CD_PLATFORM")

echo "🔄 Performing replacements..."

# Process each file
echo "$PLACEHOLDER_FILES" | while read -r file; do
    if [ -f "$file" ]; then
        echo "📝 Processing: $file"
        
        # Replace common placeholders
        replace_in_file "$file" "\\[INSERT_PROJECT_NAME\\]" "$SAFE_PROJECT_NAME"
        replace_in_file "$file" "\\[INSERT_DOMAIN\\]" "$SAFE_DOMAIN"
        replace_in_file "$file" "\\[INSERT_TECH_STACK\\]" "$SAFE_TECH_STACK"
        replace_in_file "$file" "\\[INSERT_PRIMARY_LANGUAGE\\]" "$SAFE_PRIMARY_LANGUAGE"
        replace_in_file "$file" "\\[INSERT_TESTING_FRAMEWORK\\]" "$SAFE_TESTING_FRAMEWORK"
        replace_in_file "$file" "\\[INSERT_CI_CD_PLATFORM\\]" "$SAFE_CI_CD_PLATFORM"
        
        # Additional common placeholders with defaults
        replace_in_file "$file" "\\[INSERT_TEAM_SIZE\\]" "small"
        replace_in_file "$file" "\\[INSERT_WORKFLOW_TYPE\\]" "agile"
        replace_in_file "$file" "\\[INSERT_COMPANY_NAME\\]" "YourCompany"
        replace_in_file "$file" "\\[INSERT_USER_BASE\\]" "users"
        replace_in_file "$file" "\\[INSERT_SECURITY_LEVEL\\]" "standard"
        replace_in_file "$file" "\\[INSERT_PERFORMANCE_PRIORITY\\]" "balanced"
        replace_in_file "$file" "\\[INSERT_DEPLOYMENT_TARGET\\]" "production"
    fi
done

if [ "$DRY_RUN" = "true" ]; then
    echo ""
    echo "🔍 DRY RUN COMPLETE"
    echo "Total replacements that would be made: $REPLACEMENT_COUNT"
    echo "Run without --dry-run to perform actual replacements."
else
    echo ""
    echo "✅ REPLACEMENT COMPLETE"
    echo "Total replacements made: $REPLACEMENT_COUNT"
    echo "All placeholders have been updated with your project-specific values."
fi