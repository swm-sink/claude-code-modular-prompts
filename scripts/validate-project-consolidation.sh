#!/bin/bash

# Project Management Consolidation Validation Script
# Validates the consolidation of project management commands into unified /project command

echo "🔍 Project Management Consolidation Validation"
echo "=============================================="

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

VALIDATION_ERRORS=0
VALIDATION_WARNINGS=0

# Helper functions
check_exists() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $1 exists"
        return 0
    else
        echo -e "${RED}✗${NC} $1 missing"
        ((VALIDATION_ERRORS++))
        return 1
    fi
}

check_deprecated() {
    local file="$1"
    local expected_replacement="$2"
    
    if [ -f "$file" ]; then
        if grep -q "deprecated: true" "$file" && grep -q "deprecated_date: \"2025-07-25\"" "$file"; then
            if grep -q "replacement_command: \"$expected_replacement\"" "$file"; then
                echo -e "${GREEN}✓${NC} $file properly deprecated to $expected_replacement"
                return 0
            else
                echo -e "${YELLOW}⚠${NC} $file deprecated but replacement command incorrect"
                ((VALIDATION_WARNINGS++))
                return 1
            fi
        else
            echo -e "${RED}✗${NC} $file not properly deprecated"
            ((VALIDATION_ERRORS++))
            return 1
        fi
    else
        echo -e "${RED}✗${NC} $file does not exist"
        ((VALIDATION_ERRORS++))
        return 1
    fi
}

check_unified_command_completeness() {
    local file="$1"
    
    if [ -f "$file" ]; then
        echo -e "${BLUE}📋 Checking unified command completeness...${NC}"
        
        # Check for all required modes
        local modes=("setup" "provision" "workflow" "schedule" "track" "rollback" "run")
        for mode in "${modes[@]}"; do
            if grep -q "${mode}_mode>" "$file"; then
                echo -e "${GREEN}✓${NC} Mode '$mode' implemented"
            else
                echo -e "${RED}✗${NC} Mode '$mode' missing or incomplete"
                ((VALIDATION_ERRORS++))
            fi
        done
        
        # Check for required components
        local components=("validation-framework" "command-execution" "error-handling" "progress-reporting" 
                         "adaptive-thinking" "owasp-compliance" "dag-orchestrator" "ci-cd-integration")
        
        for component in "${components[@]}"; do
            if grep -q "$component" "$file"; then
                echo -e "${GREEN}✓${NC} Component '$component' included"
            else
                echo -e "${YELLOW}⚠${NC} Component '$component' not found (may be optional)"
                ((VALIDATION_WARNINGS++))
            fi
        done
        
    else
        echo -e "${RED}✗${NC} Unified command $file does not exist"
        ((VALIDATION_ERRORS++))
    fi
}

echo ""
echo -e "${BLUE}📁 Checking unified command creation...${NC}"
check_exists ".claude/commands/project.md"

echo ""
echo -e "${BLUE}🔍 Validating unified command completeness...${NC}"
check_unified_command_completeness ".claude/commands/project.md"

echo ""
echo -e "${BLUE}⚠️  Checking deprecated commands...${NC}"

# Core project management commands that should be deprecated
check_deprecated ".claude/commands/workflow.md" "/project workflow"
check_deprecated ".claude/commands/flow-schedule.md" "/project schedule"  
check_deprecated ".claude/commands/progress-tracker.md" "/project track"

# Development/project commands that should be deprecated
check_deprecated ".claude/commands/development/project/auto-provision.md" "/project provision"
check_deprecated ".claude/commands/development/project/env-setup.md" "/project setup"
check_deprecated ".claude/commands/development/project/dev-setup.md" "/project setup"
check_deprecated ".claude/commands/development/project/cd-rollback.md" "/project rollback"
check_deprecated ".claude/commands/development/project/ci-run.md" "/project run"

echo ""
echo -e "${BLUE}🔗 Checking integration points...${NC}"

# Check that related commands still exist and integrate properly
related_commands=(
    ".claude/commands/pipeline.md"
    ".claude/commands/security.md" 
    ".claude/commands/quality/quality.md"
    ".claude/commands/core/analyze.md"
)

for cmd in "${related_commands[@]}"; do
    if [ -f "$cmd" ]; then
        echo -e "${GREEN}✓${NC} Integration point $cmd exists"
    else
        echo -e "${YELLOW}⚠${NC} Integration point $cmd missing (may affect functionality)"
        ((VALIDATION_WARNINGS++))
    fi
done

echo ""
echo -e "${BLUE}📊 Checking for command conflicts...${NC}"

# Look for potential command name conflicts
if grep -r "name.*project" .claude/commands/ --exclude="project.md" | grep -v deprecated | grep -v "DEPRECATED"; then
    echo -e "${YELLOW}⚠${NC} Potential command name conflicts found (review above output)"
    ((VALIDATION_WARNINGS++))
else
    echo -e "${GREEN}✓${NC} No command name conflicts detected"
fi

echo ""
echo -e "${BLUE}📝 Functionality Coverage Verification...${NC}"

# Check that key functionality from legacy commands is preserved
legacy_features=(
    "workflow.*orchestration"
    "progress.*tracking" 
    "environment.*setup"
    "infrastructure.*provision"
    "rollback.*recovery"
    "ci.*execution"
    "schedule.*automation"
)

unified_file=".claude/commands/project.md"
if [ -f "$unified_file" ]; then
    for feature in "${legacy_features[@]}"; do
        if grep -qi "$feature" "$unified_file"; then
            echo -e "${GREEN}✓${NC} Feature pattern '$feature' preserved"
        else
            echo -e "${YELLOW}⚠${NC} Feature pattern '$feature' may not be fully preserved"
            ((VALIDATION_WARNINGS++))
        fi
    done
else
    echo -e "${RED}✗${NC} Cannot verify functionality coverage - unified command missing"
    ((VALIDATION_ERRORS++))
fi

echo ""
echo "=============================================="
echo -e "${BLUE}📊 VALIDATION SUMMARY${NC}"
echo "=============================================="

if [ $VALIDATION_ERRORS -eq 0 ] && [ $VALIDATION_WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ ALL VALIDATIONS PASSED${NC}"
    echo "The project management consolidation is complete and valid."
elif [ $VALIDATION_ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  VALIDATION COMPLETED WITH WARNINGS${NC}"
    echo "Errors: $VALIDATION_ERRORS, Warnings: $VALIDATION_WARNINGS"
    echo "The consolidation is functional but has minor issues to review."
else
    echo -e "${RED}❌ VALIDATION FAILED${NC}"
    echo "Errors: $VALIDATION_ERRORS, Warnings: $VALIDATION_WARNINGS"
    echo "Critical issues must be resolved before the consolidation is complete."
fi

echo ""
echo -e "${BLUE}🎯 Consolidation Benefits Achieved:${NC}"
echo "• Unified interface for all project management operations"
echo "• Consistent argument patterns and behavior across modes"
echo "• Cross-mode integration capabilities"
echo "• Reduced command complexity (8 commands → 1 command with 7 modes)"
echo "• Enhanced functionality through combined capabilities"

echo ""
echo -e "${BLUE}📋 Next Steps:${NC}"
echo "1. Review any warnings or errors above"
echo "2. Test the unified /project command functionality"  
echo "3. Update any documentation that references deprecated commands"
echo "4. Communicate the changes to users"
echo "5. Plan removal of deprecated commands after 2025-08-25"

exit $VALIDATION_ERRORS