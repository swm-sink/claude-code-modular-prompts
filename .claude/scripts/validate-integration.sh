#!/bin/bash
# Validate Frontend-Backend Integration
# This script verifies that frontend commands properly reference backend components

echo "================================================"
echo "Frontend-Backend Integration Validation"
echo "================================================"
echo ""

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0

# Function to check if a file references backend
check_integration() {
    local file=$1
    local backend_path=$2
    local description=$3
    
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    if grep -q "$backend_path" "$file" 2>/dev/null; then
        echo -e "${GREEN}✅ PASS${NC}: $description"
        echo "   File: $file"
        echo "   References: $backend_path"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
    else
        echo -e "${RED}❌ FAIL${NC}: $description"
        echo "   File: $file"
        echo "   Missing reference to: $backend_path"
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
    fi
    echo ""
}

echo "=== Checking Core Command Integration ==="
echo ""

# Check /discover-project integration
check_integration \
    ".claude/commands/discover-project.md" \
    ".claude-architect/research/" \
    "/discover-project integrates with research backend"

check_integration \
    ".claude/commands/discover-project.md" \
    "analysis-framework.md" \
    "/discover-project uses analysis framework"

check_integration \
    ".claude/commands/discover-project.md" \
    "pattern-extraction-engine.md" \
    "/discover-project uses pattern extraction"

check_integration \
    ".claude/commands/discover-project.md" \
    "research-database.yaml" \
    "/discover-project uses research database"

# Check /generate-commands integration
check_integration \
    ".claude/commands/generate-commands.md" \
    ".claude-architect/command-forge/" \
    "/generate-commands integrates with command-forge backend"

check_integration \
    ".claude/commands/generate-commands.md" \
    "generation-engine.yaml" \
    "/generate-commands uses generation engine"

check_integration \
    ".claude/commands/generate-commands.md" \
    "pattern-library.yaml" \
    "/generate-commands uses pattern library"

# Check /deep-discovery orchestration
check_integration \
    ".claude/commands/deep-discovery.md" \
    "/discover-project" \
    "/deep-discovery orchestrates /discover-project"

check_integration \
    ".claude/commands/deep-discovery.md" \
    "/generate-commands" \
    "/deep-discovery orchestrates /generate-commands"

check_integration \
    ".claude/commands/deep-discovery.md" \
    "INTEGRATED" \
    "/deep-discovery documents integration status"

echo "================================================"
echo "Integration Validation Summary"
echo "================================================"
echo ""
echo "Total Checks: $TOTAL_CHECKS"
echo -e "${GREEN}Passed: $PASSED_CHECKS${NC}"
echo -e "${RED}Failed: $FAILED_CHECKS${NC}"
echo ""

# Calculate integration percentage
if [ $TOTAL_CHECKS -gt 0 ]; then
    INTEGRATION_PERCENT=$((PASSED_CHECKS * 100 / TOTAL_CHECKS))
    echo "Integration Level: ${INTEGRATION_PERCENT}%"
    
    if [ $INTEGRATION_PERCENT -eq 100 ]; then
        echo -e "${GREEN}✅ FULL INTEGRATION ACHIEVED!${NC}"
    elif [ $INTEGRATION_PERCENT -ge 80 ]; then
        echo -e "${GREEN}Good integration level${NC}"
    elif [ $INTEGRATION_PERCENT -ge 60 ]; then
        echo -e "${YELLOW}Moderate integration level${NC}"
    else
        echo -e "${RED}Low integration level - needs work${NC}"
    fi
else
    echo "No checks performed"
fi

echo ""
echo "================================================"

# Exit with error if any checks failed
if [ $FAILED_CHECKS -gt 0 ]; then
    exit 1
else
    exit 0
fi