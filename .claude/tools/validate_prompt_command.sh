#!/bin/bash
# Validation script for /prompt command functionality

echo "🔍 Validating /prompt Command Implementation"
echo "==========================================="

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Base directory
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Validation checks
ERRORS=0
WARNINGS=0

# Function to check file exists
check_file() {
    local file="$1"
    local description="$2"
    
    if [ -f "$BASE_DIR/$file" ]; then
        echo -e "${GREEN}✓${NC} $description exists"
    else
        echo -e "${RED}✗${NC} $description missing: $file"
        ((ERRORS++))
    fi
}

# Function to check directory exists
check_dir() {
    local dir="$1"
    local description="$2"
    
    if [ -d "$BASE_DIR/$dir" ]; then
        echo -e "${GREEN}✓${NC} $description exists"
    else
        echo -e "${YELLOW}⚠${NC} $description missing: $dir (creating...)"
        mkdir -p "$BASE_DIR/$dir"
        ((WARNINGS++))
    fi
}

# Function to validate XML structure
validate_xml() {
    local file="$1"
    local description="$2"
    
    if command -v xmllint &> /dev/null; then
        if xmllint --noout "$BASE_DIR/$file" 2>/dev/null; then
            echo -e "${GREEN}✓${NC} $description has valid XML"
        else
            echo -e "${RED}✗${NC} $description has invalid XML"
            ((ERRORS++))
        fi
    else
        echo -e "${YELLOW}⚠${NC} xmllint not found, skipping XML validation"
        ((WARNINGS++))
    fi
}

echo ""
echo "1. Checking Required Files..."
echo "-----------------------------"
check_file "commands/prompt.md" "Command definition"
check_file "modules/development/prompt-engineering.md" "Module implementation"
check_file "prompts/templates/prompt_help.md" "Help documentation"
check_file "examples/prompt_command_usage.md" "Usage examples"

echo ""
echo "2. Checking Directory Structure..."
echo "----------------------------------"
check_dir "prompts/templates" "Templates directory"
check_dir "prompts/metrics" "Metrics directory"
check_dir "prompts/tests" "Tests directory"

echo ""
echo "3. Validating XML Structure..."
echo "------------------------------"
validate_xml "commands/prompt.md" "Command file"
validate_xml "modules/development/prompt-engineering.md" "Module file"

echo ""
echo "4. Checking Integration Points..."
echo "---------------------------------"

# Check delegation pattern
if grep -q "delegation target=\"modules/development/prompt-engineering.md\"" "$BASE_DIR/commands/prompt.md"; then
    echo -e "${GREEN}✓${NC} Delegation pattern correctly implemented"
else
    echo -e "${RED}✗${NC} Delegation pattern not found or incorrect"
    ((ERRORS++))
fi

# Check subcommands
for cmd in create evaluate test improve; do
    if grep -q "subcommand name=\"$cmd\"" "$BASE_DIR/commands/prompt.md"; then
        echo -e "${GREEN}✓${NC} Subcommand '$cmd' defined"
    else
        echo -e "${RED}✗${NC} Subcommand '$cmd' missing"
        ((ERRORS++))
    fi
done

echo ""
echo "5. Running Python Tests..."
echo "-------------------------"
if [ -f "$BASE_DIR/tests/test_prompt_command.py" ]; then
    cd "$BASE_DIR/.." && python "$BASE_DIR/tests/test_prompt_command.py" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} Python tests passed"
    else
        echo -e "${RED}✗${NC} Python tests failed"
        ((ERRORS++))
    fi
else
    echo -e "${YELLOW}⚠${NC} Python test file not found"
    ((WARNINGS++))
fi

echo ""
echo "==========================================="
echo "Validation Summary"
echo "==========================================="

if [ $ERRORS -eq 0 ]; then
    if [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ All checks passed!${NC}"
        echo "The /prompt command is fully implemented and ready for use."
    else
        echo -e "${YELLOW}⚠️  Validation completed with $WARNINGS warnings${NC}"
        echo "The /prompt command is functional but some optional features may be limited."
    fi
    exit 0
else
    echo -e "${RED}❌ Validation failed with $ERRORS errors${NC}"
    if [ $WARNINGS -gt 0 ]; then
        echo -e "   Also found $WARNINGS warnings"
    fi
    echo "Please fix the errors before using the /prompt command."
    exit 1
fi