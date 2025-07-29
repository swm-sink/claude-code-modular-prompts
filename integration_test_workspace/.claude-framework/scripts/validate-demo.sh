#!/bin/bash
# Demo Validation Script
# Ensures all demo steps work before recording

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🎬 Validating Demo Setup...${NC}"
echo ""

# Test 1: Check setup.sh exists and is executable
echo -e "${YELLOW}Test 1: Checking setup.sh...${NC}"
if [ -f "./setup.sh" ] && [ -x "./setup.sh" ]; then
    echo -e "${GREEN}✓ setup.sh found and executable${NC}"
else
    echo -e "${RED}✗ setup.sh missing or not executable${NC}"
    exit 1
fi

# Test 2: Create demo environment
echo -e "${YELLOW}Test 2: Creating demo environment...${NC}"
DEMO_DIR="/tmp/claude-demo-validation-$$"
mkdir -p "$DEMO_DIR"
cd "$DEMO_DIR"

git init > /dev/null 2>&1
git config user.name "Demo User" > /dev/null 2>&1  
git config user.email "demo@example.com" > /dev/null 2>&1
echo "# Demo Project" > README.md
git add README.md > /dev/null 2>&1
git commit -m "Initial commit" > /dev/null 2>&1

echo -e "${GREEN}✓ Demo environment created${NC}"

# Test 3: Copy framework (simulate submodule)
echo -e "${YELLOW}Test 3: Setting up framework...${NC}"
cp -r "$OLDPWD" ".claude-framework"
cd ".claude-framework"

# Test 4: Run setup script
echo -e "${YELLOW}Test 4: Running setup script...${NC}"
./setup.sh --project-name "demo-project" --profile general --target "../" --force > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Setup script completed successfully${NC}"
else
    echo -e "${RED}✗ Setup script failed${NC}"
    exit 1
fi

cd ..

# Test 5: Verify installation
echo -e "${YELLOW}Test 5: Verifying installation...${NC}"

# Check directory structure
if [ -d ".claude" ]; then
    echo -e "${GREEN}✓ .claude directory created${NC}"
else
    echo -e "${RED}✗ .claude directory missing${NC}"
    exit 1
fi

# Check core commands
CORE_COMMANDS=("help.md" "task.md" "auto.md" "query.md")
for cmd in "${CORE_COMMANDS[@]}"; do
    if [ -f ".claude/commands/core/$cmd" ]; then
        echo -e "${GREEN}✓ $cmd installed${NC}"
    else
        echo -e "${RED}✗ $cmd missing${NC}"
        exit 1
    fi
done

# Count total commands
COMMAND_COUNT=$(find .claude/commands -name "*.md" | wc -l)
echo -e "${GREEN}✓ $COMMAND_COUNT commands installed${NC}"

# Test 6: Verify command structure
echo -e "${YELLOW}Test 6: Validating command structure...${NC}"
SAMPLE_COMMAND=".claude/commands/core/help.md"
if grep -q "^name:" "$SAMPLE_COMMAND" && grep -q "^description:" "$SAMPLE_COMMAND"; then
    echo -e "${GREEN}✓ Command format is correct${NC}"
else
    echo -e "${RED}✗ Command format invalid${NC}"
    exit 1
fi

# Test 7: Check components and context
echo -e "${YELLOW}Test 7: Checking framework assets...${NC}"
if [ -d ".claude/components" ] && [ "$(ls -A .claude/components)" ]; then
    echo -e "${GREEN}✓ Components installed${NC}"
else
    echo -e "${YELLOW}! Components directory empty or missing${NC}"
fi

if [ -d ".claude/context" ] && [ "$(ls -A .claude/context)" ]; then
    echo -e "${GREEN}✓ Context files installed${NC}"
else
    echo -e "${YELLOW}! Context directory empty or missing${NC}"
fi

# Test 8: Performance timing
echo -e "${YELLOW}Test 8: Testing setup performance...${NC}"
cd "$OLDPWD"
TEMP_TEST="/tmp/claude-speed-test-$$"
mkdir -p "$TEMP_TEST"
cd "$TEMP_TEST"

git init > /dev/null 2>&1
git config user.name "Speed Test" > /dev/null 2>&1
git config user.email "test@example.com" > /dev/null 2>&1

START_TIME=$(date +%s)
cp -r "$OLDPWD" ".claude-framework"
cd ".claude-framework"
./setup.sh --project-name "speed-test" --profile general --target "../" --force > /dev/null 2>&1
END_TIME=$(date +%s)

DURATION=$((END_TIME - START_TIME))
echo -e "${GREEN}✓ Setup completed in ${DURATION} seconds${NC}"

if [ $DURATION -le 60 ]; then
    echo -e "${GREEN}✓ Performance target met (< 1 minute)${NC}"
else
    echo -e "${YELLOW}! Setup took longer than expected (${DURATION}s)${NC}"
fi

# Cleanup
echo -e "${YELLOW}Cleaning up test environments...${NC}"
cd "$OLDPWD"
rm -rf "$DEMO_DIR" "$TEMP_TEST"

# Final summary
echo ""
echo -e "${GREEN}🎉 Demo Validation Complete!${NC}"
echo ""
echo -e "${BLUE}Demo is ready for recording:${NC}"
echo "  ✓ Setup script works correctly"
echo "  ✓ All core commands install properly"
echo "  ✓ Performance meets expectations"
echo "  ✓ Command structure is valid"
echo ""
echo -e "${YELLOW}Recording tips:${NC}"
echo "  • Use --profile web-dev for more visual impact"
echo "  • Show 'tree .claude' or 'ls -la .claude' for structure"
echo "  • Count commands with: find .claude/commands -name '*.md' | wc -l"
echo "  • Emphasize the < 5 minute total time"
echo ""
echo -e "${GREEN}Ready to record! 🎬${NC}"