#!/bin/bash
# Project Validation Script - Based on ULTRATHINK Learnings
# Run this before commits to catch common issues

echo "🔍 Running Project Validation..."
echo "================================"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track errors
ERRORS=0

# Function to report issues
report_issue() {
    echo -e "${RED}❌ $1${NC}"
    ((ERRORS++))
}

report_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

report_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

echo ""
echo "1. File System Hygiene"
echo "----------------------"

# Check for __pycache__
PYCACHE_COUNT=$(find . -name "__pycache__" -type d | wc -l)
if [ $PYCACHE_COUNT -gt 0 ]; then
    report_issue "Found $PYCACHE_COUNT __pycache__ directories"
    echo "   Run: find . -name '__pycache__' -type d -exec rm -rf {} +"
else
    report_success "No __pycache__ directories found"
fi

# Check for backup files
BACKUP_COUNT=$(find . -name "*.backup" -o -name "*.v1-backup" | wc -l)
if [ $BACKUP_COUNT -gt 0 ]; then
    report_issue "Found $BACKUP_COUNT backup files"
    echo "   Run: find . -name '*.backup' -o -name '*.v1-backup' -exec rm {} \;"
else
    report_success "No backup files found"
fi

# Check for Python files in root
PY_ROOT_COUNT=$(ls *.py 2>/dev/null | wc -l)
if [ $PY_ROOT_COUNT -gt 0 ]; then
    report_warning "Found $PY_ROOT_COUNT Python files in root directory"
    echo "   Consider moving to scripts/ directory"
else
    report_success "No Python files in root directory"
fi

echo ""
echo "2. Directory Structure"
echo "---------------------"

# Check directory depth (excluding .git and node_modules)
MAX_DEPTH=$(find . -type d -not -path "./.git/*" -not -path "./node_modules/*" | awk -F'/' '{print NF-1}' | sort -nr | head -1)
if [ $MAX_DEPTH -gt 3 ]; then
    report_issue "Directory depth exceeds 3 levels (found: $MAX_DEPTH)"
    echo "   Deep directories:"
    find . -type d -not -path "./.git/*" -not -path "./node_modules/*" | awk -F'/' '{if(NF-1 > 3) print "   " $0}'
else
    report_success "Directory depth within limits (max: $MAX_DEPTH)"
fi

echo ""
echo "3. Hardcoded Paths"
echo "------------------"

# Check for hardcoded absolute paths
HARDCODED_PATHS=$(grep -r "/Users\|/home\|C:\\\\" . --include="*.json" --include="*.md" --include="*.sh" --include="*.py" 2>/dev/null | grep -v "Binary file" | wc -l)
if [ $HARDCODED_PATHS -gt 0 ]; then
    report_issue "Found $HARDCODED_PATHS hardcoded absolute paths"
    echo "   Files with absolute paths:"
    grep -r "/Users\|/home\|C:\\\\" . --include="*.json" --include="*.md" --include="*.sh" --include="*.py" 2>/dev/null | grep -v "Binary file" | head -5 | awk -F: '{print "   " $1}'
else
    report_success "No hardcoded absolute paths found"
fi

echo ""
echo "4. YAML Consistency"
echo "-------------------"

# Check for command: vs name: in YAML
COMMAND_COUNT=$(grep -r "^command:" .claude/commands --include="*.md" 2>/dev/null | wc -l)
NAME_COUNT=$(grep -r "^name:" .claude/commands --include="*.md" 2>/dev/null | wc -l)
if [ $COMMAND_COUNT -gt 0 ] && [ $NAME_COUNT -gt 0 ]; then
    report_issue "Mixed YAML fields: found both 'command:' ($COMMAND_COUNT) and 'name:' ($NAME_COUNT)"
elif [ $COMMAND_COUNT -gt 0 ]; then
    report_warning "Using 'command:' field - consider standardizing to 'name:'"
else
    report_success "Consistent YAML field usage"
fi

echo ""
echo "5. Documentation Integrity"
echo "-------------------------"

# Check for hardcoded counts
HARDCODED_COUNTS=$(grep -r "\b[0-9]\+\s*command\|[0-9]\+\s*component" . --include="*.md" 2>/dev/null | grep -v "step\|Step\|Phase" | wc -l)
if [ $HARDCODED_COUNTS -gt 0 ]; then
    report_warning "Found $HARDCODED_COUNTS potential hardcoded counts"
    echo "   Consider using qualitative terms instead"
else
    report_success "No obvious hardcoded counts found"
fi

echo ""
echo "6. Security Check"
echo "-----------------"

# Check for potential secrets
SECRETS=$(grep -r "password\s*=\|secret\s*=\|api_key\s*=\|token\s*=" . --include="*.md" --include="*.json" --include="*.py" --include="*.sh" 2>/dev/null | grep -v "example\|test\|demo" | wc -l)
if [ $SECRETS -gt 0 ]; then
    report_issue "Found $SECRETS potential exposed secrets"
    echo "   Review these files carefully"
else
    report_success "No obvious exposed secrets found"
fi

echo ""
echo "================================"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ All validation checks passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ Found $ERRORS issues that need attention${NC}"
    exit 1
fi