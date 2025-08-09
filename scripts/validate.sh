#!/bin/bash

# Claude Context Architect - Simple System Validation Script
# Validates the elegant, functional command system

# Color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'  
RED='\033[0;31m'
NC='\033[0m' # No Color

# ============================================================================
# CORE VALIDATION FUNCTIONS (Testable)
# ============================================================================

# Function: Check if directory structure is correct
# Returns: 0 if correct, 1 if incorrect
# Output: Status message
check_directory_structure() {
    if [ -d ".claude" ] && [ -d ".claude/commands" ]; then
        echo -e "   ${GREEN}✅ Directory structure correct${NC}"
        return 0
    else
        echo -e "   ${RED}❌ Missing .claude/commands directory${NC}"
        return 1
    fi
}

# Function: Count remaining INSERT_ placeholders in command files
# Returns: Number of individual placeholders found (not lines)
count_remaining_placeholders() {
    if [ ! -d ".claude/commands" ]; then
        echo "0"
        return
    fi
    
    local count
    # Count actual placeholder occurrences, not lines
    count=$(grep -ro "\[INSERT_[^]]*\]" .claude/commands/ --include="*.md" 2>/dev/null | wc -l | tr -d ' ')
    echo "$count"
}

# Function: Validate project configuration file
# Returns: 0 if valid, 1 if invalid
validate_project_config() {
    if [ ! -f ".claude/config/project-config.yaml" ]; then
        return 1
    fi
    
    local config_placeholders
    config_placeholders=$(grep "INSERT_" .claude/config/project-config.yaml 2>/dev/null | wc -l | tr -d ' ')
    
    if [ "$config_placeholders" -eq 0 ]; then
        return 0
    else
        return 1
    fi
}

# Function: Count duplicate command names
# Returns: Number of duplicate commands
count_duplicate_commands() {
    if [ ! -d ".claude/commands" ]; then
        echo "0"
        return
    fi
    
    local duplicates
    duplicates=$(find .claude/commands -name "*.md" -type f 2>/dev/null | \
        xargs grep "^name: " 2>/dev/null | \
        sed 's/.*name: //' | \
        sort | uniq -d | wc -l | tr -d ' ')
    echo "$duplicates"
}

# Function: Count present core commands
# Returns: Number of core commands found
count_core_commands() {
    if [ ! -d ".claude/commands" ]; then
        echo "0"
        return
    fi
    
    local core_commands=("welcome-simple" "discover-project-simple" "generate-commands-simple" "list-commands")
    local found=0
    
    for cmd in "${core_commands[@]}"; do
        if [ -f ".claude/commands/${cmd}.md" ]; then
            ((found++))
        fi
    done
    
    echo "$found"
}

# Function: Calculate readiness score
# Args: placeholder_count config_issues duplicates structure_ok core_count
# Returns: Score 0-100
calculate_readiness_score() {
    local placeholder_count="$1"  # Kept for compatibility but not used
    local config_issues="$2"      # Kept for compatibility but not used
    local duplicates="$3"
    local structure_ok="$4"
    local core_count="$5"
    
    local score=100
    
    # Simple scoring for elegant system
    [ "$duplicates" -gt 0 ] && score=$((score - duplicates * 10))
    [ "$structure_ok" -eq 0 ] && score=$((score - 30))
    [ "$core_count" -lt 4 ] && score=$((score - (4 - core_count) * 15))
    
    # Don't go below 0
    [ $score -lt 0 ] && score=0
    
    echo "$score"
}

# Function: Count total commands
# Returns: Total number of command files
count_total_commands() {
    if [ ! -d ".claude/commands" ]; then
        echo "0"
        return
    fi
    
    local total
    total=$(find .claude/commands -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    echo "$total"
}

# Function: Generate validation report  
# Args: score placeholder_count config_issues duplicates structure_ok core_count total_commands
generate_validation_report() {
    local score="$1"
    local placeholder_count="$2"
    local config_issues="$3"
    local duplicates="$4"
    local structure_ok="$5"
    local core_count="$6" 
    local total_commands="$7"
    
    echo "=== Claude Context Architect - System Validation ==="
    echo ""
    
    # 1. Directory structure
    echo "1. Checking directory structure..."
    if [ "$structure_ok" -eq 1 ]; then
        echo -e "   ${GREEN}✅ Directory structure correct${NC}"
    else
        echo -e "   ${RED}❌ Missing .claude/commands directory${NC}"
    fi
    
    # 2. Core commands
    echo ""
    echo "2. Checking essential commands..."
    if [ "$core_count" -eq 4 ]; then
        echo -e "   ${GREEN}✅ All essential commands present${NC}"
    else
        echo -e "   ${YELLOW}⚠️  Some essential commands missing ($core_count/4 found)${NC}"
        echo "   Required: welcome-simple, discover-project-simple, generate-commands-simple, list-commands"
    fi
    
    # 3. Duplicates
    echo ""
    echo "3. Checking for duplicate commands..."
    if [ "$duplicates" -eq 0 ]; then
        echo -e "   ${GREEN}✅ No duplicate commands${NC}"
    else
        echo -e "   ${RED}❌ Found $duplicates duplicate command names${NC}"
    fi
    
    # 4. Command inventory
    echo ""
    echo "4. Command inventory..."
    echo "   Total commands: $total_commands"
    echo "   Essential commands: $core_count/4"
    
    # Score and recommendations
    echo ""
    echo "===================================="
    if [ "$score" -ge 90 ]; then
        echo -e "${GREEN}SYSTEM STATUS: READY${NC}"
    elif [ "$score" -ge 70 ]; then
        echo -e "${YELLOW}SYSTEM STATUS: PARTIALLY READY${NC}"
    else
        echo -e "${RED}SYSTEM STATUS: NOT READY${NC}"
    fi
    echo "===================================="
    
    echo ""
    if [ "$score" -ge 90 ]; then
        echo -e "${GREEN}✅ System is ready for use!${NC}"
        echo "Run /welcome-simple to begin"
    else
        echo -e "${YELLOW}⚠️ System needs attention${NC}"
        [ "$structure_ok" -eq 0 ] && echo "  - Create .claude/commands directory"
        [ "$core_count" -lt 4 ] && echo "  - Install missing essential commands"
    fi
}

# Function: Provide score-based recommendations
provide_recommendations() {
    local score="$1"
    local placeholder_count="$2"
    local config_issues="$3"
    local duplicates="$4"
    
    if [ "$score" -eq 100 ]; then
        echo -e "${GREEN}🎉 Your adaptation is complete!${NC}"
        echo "Next steps:"
        echo "  1. Test your commands in Claude Code"
        echo "  2. Remove any unnecessary commands"
        echo "  3. Document your adaptation pattern"
    elif [ "$score" -ge 90 ]; then
        echo -e "${GREEN}📈 Almost there! Just a few items left.${NC}"
        echo "Focus on:"
        [ "$placeholder_count" -gt 0 ] && echo "  - Replace remaining placeholders"
        [ "$config_issues" -gt 0 ] && echo "  - Complete project configuration"
    elif [ "$score" -ge 70 ]; then
        echo -e "${YELLOW}👍 Good progress. Keep customizing!${NC}"
        echo "Priority tasks:"
        [ "$placeholder_count" -gt 10 ] && echo "  - Replace placeholders (high priority)"
        [ "$config_issues" -gt 0 ] && echo "  - Fill out project-config.yaml"
        [ "$duplicates" -gt 0 ] && echo "  - Resolve duplicate commands"
    else
        echo -e "${RED}🔧 Significant customization needed.${NC}"
        echo "Start with:"
        echo "  1. Run: /adapt-to-project"
        echo "  2. Fill out .claude/config/project-config.yaml"
        echo "  3. Use Find & Replace for placeholders"
    fi
}

# ============================================================================
# MAIN EXECUTION FUNCTION
# ============================================================================

run_validation() {
    echo "7. Calculating readiness score..."
    
    # Collect metrics
    local structure_ok=1
    check_directory_structure >/dev/null || structure_ok=0
    
    local placeholder_count
    placeholder_count=$(count_remaining_placeholders)
    
    local config_issues=0
    validate_project_config || config_issues=1
    
    local duplicates
    duplicates=$(count_duplicate_commands)
    
    local core_count
    core_count=$(count_core_commands)
    
    local total_commands
    total_commands=$(count_total_commands)
    
    # Calculate score
    local score
    score=$(calculate_readiness_score "$placeholder_count" "$config_issues" "$duplicates" "$structure_ok" "$core_count")
    
    # Generate report
    generate_validation_report "$score" "$placeholder_count" "$config_issues" "$duplicates" "$structure_ok" "$core_count" "$total_commands"
    
    # Return appropriate exit code
    if [ "$score" -ge 90 ]; then
        return 0
    else
        return 1
    fi
}

# ============================================================================
# SCRIPT ENTRY POINT
# ============================================================================

# Only run main execution if script is executed directly (not sourced for testing)
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    run_validation
    exit $?
fi