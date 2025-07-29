#!/bin/bash
# Installation Methods Testing Script
# Tests all three installation methods in isolated environments

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test configuration
TEST_DIR="installation-test-$(date +%s)"
RESULTS_FILE="installation-test-results-$(date +%Y%m%d-%H%M%S).log"
REPO_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo -e "${BLUE}🧪 Claude Code Template Library - Installation Testing${NC}"
echo "============================================================="
echo "Test Directory: $TEST_DIR"
echo "Results File: $RESULTS_FILE"
echo "Source Repo: $REPO_PATH"
echo ""

# Create test environment
mkdir -p "$TEST_DIR"
cd "$TEST_DIR"

# Initialize results log
echo "Installation Test Results - $(date)" > "$RESULTS_FILE"
echo "====================================" >> "$RESULTS_FILE"
echo "" >> "$RESULTS_FILE"

# Test 1: Setup Script Direct Execution
echo -e "${YELLOW}Test 1: Setup Script Direct Execution${NC}"
echo "Test 1: Setup Script Direct Execution" >> "$RESULTS_FILE"

mkdir test1-direct && cd test1-direct
if "$REPO_PATH/setup.sh" .; then
    echo -e "${GREEN}✅ Setup script executed successfully${NC}"
    echo "✅ Setup script executed successfully" >> "../$RESULTS_FILE"
    
    # Validate installation
    if [ -d ".claude" ]; then
        echo -e "${GREEN}✅ .claude directory created${NC}"
        echo "✅ .claude directory created" >> "../$RESULTS_FILE"
        
        COMMAND_COUNT=$(find .claude/commands -name "*.md" 2>/dev/null | wc -l)
        echo -e "${BLUE}📊 Commands installed: $COMMAND_COUNT${NC}"
        echo "📊 Commands installed: $COMMAND_COUNT" >> "../$RESULTS_FILE"
        
        if [ "$COMMAND_COUNT" -gt 50 ]; then
            echo -e "${GREEN}✅ Command count acceptable${NC}"
            echo "✅ Command count acceptable" >> "../$RESULTS_FILE"
        else
            echo -e "${RED}❌ Command count too low${NC}"
            echo "❌ Command count too low" >> "../$RESULTS_FILE"
        fi
        
        # Test essential commands
        if [ -f ".claude/commands/core/help.md" ]; then
            echo -e "${GREEN}✅ Essential commands present${NC}"
            echo "✅ Essential commands present" >> "../$RESULTS_FILE"
        else
            echo -e "${RED}❌ Essential commands missing${NC}"
            echo "❌ Essential commands missing" >> "../$RESULTS_FILE"
        fi
    else
        echo -e "${RED}❌ .claude directory not created${NC}"
        echo "❌ .claude directory not created" >> "../$RESULTS_FILE"
    fi
else
    echo -e "${RED}❌ Setup script failed${NC}"
    echo "❌ Setup script failed" >> "../$RESULTS_FILE"
fi
cd ..
echo "" >> "$RESULTS_FILE"

# Test 2: Selective Copy Test
echo -e "${YELLOW}Test 2: Selective Copy Test${NC}"
echo "Test 2: Selective Copy Test" >> "$RESULTS_FILE"

mkdir test2-selective && cd test2-selective
mkdir -p .claude/commands/core

# Copy specific commands
if cp "$REPO_PATH/.claude/commands/core/help.md" .claude/commands/core/ 2>/dev/null; then
    echo -e "${GREEN}✅ Selective copy successful${NC}"
    echo "✅ Selective copy successful" >> "../$RESULTS_FILE"
    
    # Verify selective nature
    SELECTIVE_COUNT=$(find .claude/commands -name "*.md" | wc -l)
    echo -e "${BLUE}📊 Selective commands: $SELECTIVE_COUNT${NC}"
    echo "📊 Selective commands: $SELECTIVE_COUNT" >> "../$RESULTS_FILE"
    
    if [ "$SELECTIVE_COUNT" -eq 1 ]; then
        echo -e "${GREEN}✅ Selective import working correctly${NC}"
        echo "✅ Selective import working correctly" >> "../$RESULTS_FILE"
    else
        echo -e "${YELLOW}⚠️ Unexpected selective count${NC}"
        echo "⚠️ Unexpected selective count" >> "../$RESULTS_FILE"
    fi
else
    echo -e "${RED}❌ Selective copy failed${NC}"
    echo "❌ Selective copy failed" >> "../$RESULTS_FILE"
fi
cd ..
echo "" >> "$RESULTS_FILE"

# Test 3: Existing Project Integration
echo -e "${YELLOW}Test 3: Existing Project Integration${NC}"
echo "Test 3: Existing Project Integration" >> "$RESULTS_FILE"

mkdir test3-existing && cd test3-existing
mkdir -p .claude/commands/custom
echo "# Custom Command" > .claude/commands/custom/my-command.md

# Run setup over existing structure
if "$REPO_PATH/setup.sh" .; then
    echo -e "${GREEN}✅ Setup over existing project successful${NC}"
    echo "✅ Setup over existing project successful" >> "../$RESULTS_FILE"
    
    # Check if existing files preserved
    if [ -f ".claude/commands/custom/my-command.md" ]; then
        echo -e "${GREEN}✅ Existing files preserved${NC}"
        echo "✅ Existing files preserved" >> "../$RESULTS_FILE"
    else
        echo -e "${RED}❌ Existing files overwritten${NC}"
        echo "❌ Existing files overwritten" >> "../$RESULTS_FILE"
    fi
    
    # Check if new files added
    if [ -f ".claude/commands/core/help.md" ]; then
        echo -e "${GREEN}✅ New templates added${NC}"
        echo "✅ New templates added" >> "../$RESULTS_FILE"
    else
        echo -e "${RED}❌ New templates not added${NC}"
        echo "❌ New templates not added" >> "../$RESULTS_FILE"
    fi
else
    echo -e "${RED}❌ Setup over existing project failed${NC}"
    echo "❌ Setup over existing project failed" >> "../$RESULTS_FILE"
fi
cd ..
echo "" >> "$RESULTS_FILE"

# Test 4: Error Handling
echo -e "${YELLOW}Test 4: Error Handling${NC}"
echo "Test 4: Error Handling" >> "$RESULTS_FILE"

# Test invalid target directory
if "$REPO_PATH/setup.sh" "/nonexistent/invalid/path" 2>/dev/null; then
    echo -e "${RED}❌ Should have failed with invalid path${NC}"
    echo "❌ Should have failed with invalid path" >> "$RESULTS_FILE"
else
    echo -e "${GREEN}✅ Correctly handled invalid path${NC}"
    echo "✅ Correctly handled invalid path" >> "$RESULTS_FILE"
fi
echo "" >> "$RESULTS_FILE"

# Test 5: Template Integrity Check
echo -e "${YELLOW}Test 5: Template Integrity Check${NC}"
echo "Test 5: Template Integrity Check" >> "$RESULTS_FILE"

cd test1-direct
# Check for placeholder presence
if grep -r "\[INSERT_" .claude/commands/ >/dev/null 2>&1; then
    echo -e "${GREEN}✅ Placeholders found in templates${NC}"
    echo "✅ Placeholders found in templates" >> "../$RESULTS_FILE"
    
    PLACEHOLDER_COUNT=$(grep -r "\[INSERT_" .claude/commands/ | wc -l)
    echo -e "${BLUE}📊 Placeholders found: $PLACEHOLDER_COUNT${NC}"
    echo "📊 Placeholders found: $PLACEHOLDER_COUNT" >> "../$RESULTS_FILE"
else
    echo -e "${YELLOW}⚠️ No placeholders found - may be pre-customized${NC}"
    echo "⚠️ No placeholders found - may be pre-customized" >> "../$RESULTS_FILE"
fi

# Check YAML frontmatter
YAML_COUNT=$(grep -r "^---$" .claude/commands/ | wc -l)
echo -e "${BLUE}📊 YAML frontmatter blocks: $YAML_COUNT${NC}"
echo "📊 YAML frontmatter blocks: $YAML_COUNT" >> "../$RESULTS_FILE"

if [ "$YAML_COUNT" -gt 100 ]; then
    echo -e "${GREEN}✅ Templates have proper metadata${NC}"
    echo "✅ Templates have proper metadata" >> "../$RESULTS_FILE"
else
    echo -e "${YELLOW}⚠️ Some templates may lack metadata${NC}"
    echo "⚠️ Some templates may lack metadata" >> "../$RESULTS_FILE"
fi
cd ..
echo "" >> "$RESULTS_FILE"

# Generate test summary
echo -e "${BLUE}📊 Test Summary${NC}"
echo "Test Summary" >> "$RESULTS_FILE"
echo "============" >> "$RESULTS_FILE"

# Count results
TOTAL_TESTS=5
PASSED_TESTS=$(grep -c "✅" "$RESULTS_FILE" || echo "0")
FAILED_TESTS=$(grep -c "❌" "$RESULTS_FILE" || echo "0")
WARNING_TESTS=$(grep -c "⚠️" "$RESULTS_FILE" || echo "0")

echo -e "${GREEN}✅ Passed: $PASSED_TESTS${NC}"
echo -e "${RED}❌ Failed: $FAILED_TESTS${NC}"
echo -e "${YELLOW}⚠️ Warnings: $WARNING_TESTS${NC}"

echo "✅ Passed: $PASSED_TESTS" >> "$RESULTS_FILE"
echo "❌ Failed: $FAILED_TESTS" >> "$RESULTS_FILE"
echo "⚠️ Warnings: $WARNING_TESTS" >> "$RESULTS_FILE"
echo "" >> "$RESULTS_FILE"
echo "Test completed at: $(date)" >> "$RESULTS_FILE"

# Copy results to parent directory
cp "$RESULTS_FILE" ..

# Cleanup option
echo ""
echo -e "${YELLOW}Test directory: $(pwd)${NC}"
echo -e "${YELLOW}Results file: ../$RESULTS_FILE${NC}"
echo ""
echo "Clean up test directory? (y/n)"
read -r cleanup
if [ "$cleanup" = "y" ]; then
    cd .. && rm -rf "$TEST_DIR"
    echo -e "${GREEN}Test directory cleaned up${NC}"
else
    echo -e "${BLUE}Test directory preserved for inspection${NC}"
fi

echo ""
echo -e "${BLUE}Installation testing completed!${NC}"
echo -e "${BLUE}Results available in: $RESULTS_FILE${NC}"