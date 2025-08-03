# Claude Code Template Library - Validation Guide

This comprehensive guide helps you manually validate that your template customization is complete and correct. Work through each section systematically to ensure your adapted Claude Code project is ready for use.

## 📋 Quick Validation Checklist

**Print this checklist and check off items as you complete them:**

```
PRE-FLIGHT CHECKS
□ Setup script completed successfully
□ Dual directory structure exists (.claude/ and .claude-framework/)
□ project-config.yaml file exists and is filled out
□ CLAUDE.md exists at project root
□ Git repository initialized (if using version control)

PLACEHOLDER VALIDATION (15 Standard Placeholders)
□ [INSERT_PROJECT_NAME] - Replaced in all files
□ [INSERT_DOMAIN] - Replaced in all files
□ [INSERT_TECH_STACK] - Replaced in all files
□ [INSERT_TEAM_SIZE] - Replaced in all files
□ [INSERT_COMPANY_NAME] - Replaced in all files
□ [INSERT_CLOUD_PROVIDER] - Replaced in all files
□ [INSERT_CI_CD_PLATFORM] - Replaced in all files
□ [INSERT_TEST_FRAMEWORK] - Replaced in all files
□ [INSERT_DATABASE_TYPE] - Replaced in all files
□ [INSERT_MONITORING_PLATFORM] - Replaced in all files
□ [INSERT_DEPLOYMENT_SCHEDULE] - Replaced in all files
□ [INSERT_COMPLIANCE_REQUIREMENTS] - Replaced in all files
□ [INSERT_VERSION_CONTROL] - Replaced in all files
□ [INSERT_DOCUMENTATION_TOOL] - Replaced in all files
□ [INSERT_CONTAINER_PLATFORM] - Replaced in all files

COMMAND VALIDATION
□ Core commands customized (/task, /help, /auto, /query)
□ Unnecessary commands removed
□ Domain-specific commands retained
□ All retained commands have valid YAML front matter
□ No duplicate command names exist

FUNCTIONAL VALIDATION
□ Test 3-5 key commands in Claude Code
□ Commands produce expected output
□ No error messages about missing tools
□ Placeholders don't appear in command output

DOCUMENTATION VALIDATION
□ README.md reflects your project
□ CLAUDE.md updated with project details
□ Custom documentation added (if needed)
□ Examples work with your configuration
```

## 🔍 Detailed Validation Steps

### Step 1: Structure Validation

**Check directory structure:**
```bash
# Run this from your project root
ls -la .claude/
ls -la .claude-framework/
ls -la .claude/commands/
```

**Expected output:**
- `.claude/` - Your working directory (read-write)
- `.claude-framework/` - Reference library (read-only)
- Commands organized by category in `.claude/commands/`

### Step 2: Placeholder Validation

**Find remaining placeholders:**
```bash
# Search for any remaining INSERT_ placeholders
grep -r "INSERT_" .claude/commands/ --include="*.md" | head -20

# Count remaining placeholders
grep -r "INSERT_" .claude/commands/ --include="*.md" | wc -l
```

**Expected result:** 
- 0 placeholders remaining (or only in commands you haven't customized yet)

**Check specific placeholders:**
```bash
# Check each placeholder individually
grep -r "INSERT_PROJECT_NAME" .claude/ --include="*.md"
grep -r "INSERT_DOMAIN" .claude/ --include="*.md"
grep -r "INSERT_TECH_STACK" .claude/ --include="*.md"
# ... repeat for all 15 placeholders
```

### Step 3: Configuration Validation

**Verify project-config.yaml:**
```bash
# Check if properly filled out
cat .claude/config/project-config.yaml | grep INSERT_

# Should return nothing if all placeholders are replaced
```

**Validate YAML front matter in commands:**
```bash
# Check for required fields
for file in .claude/commands/**/*.md; do
  echo "Checking: $file"
  head -10 "$file" | grep -E "^name:|^description:"
done
```

### Step 4: Command Inventory

**List all available commands:**
```bash
# Get list of all commands
find .claude/commands -name "*.md" -type f | \
  xargs grep "^name:" | \
  awk -F: '{print $3}' | \
  sort | uniq
```

**Check for duplicates:**
```bash
# Find duplicate command names
find .claude/commands -name "*.md" -type f | \
  xargs grep "^name:" | \
  awk -F: '{print $3}' | \
  sort | uniq -d
```

**Expected:** No output (no duplicates)

### Step 5: Functional Testing

**Test core commands in Claude Code:**

1. **Test /help command:**
   ```
   /help
   ```
   Expected: Shows your project name and customized help

2. **Test /task command:**
   ```
   /task "Create a new user authentication feature"
   ```
   Expected: References your tech stack and project context

3. **Test domain-specific command:**
   ```
   /auto "Set up development environment"
   ```
   Expected: Uses your specific tools and configuration

### Step 6: Quality Checks

**Check for common issues:**

1. **Partial replacements:**
   ```bash
   # Look for incomplete replacements
   grep -r "INSERT_.*]" .claude/ --include="*.md" | grep -v "\[INSERT_"
   ```

2. **Broken markdown:**
   ```bash
   # Check for unclosed code blocks
   for file in .claude/commands/**/*.md; do
     count=$(grep -c '```' "$file")
     if [ $((count % 2)) -ne 0 ]; then
       echo "Unclosed code block in: $file"
     fi
   done
   ```

3. **Empty descriptions:**
   ```bash
   # Find commands with empty descriptions
   grep -r "^description: *$" .claude/commands/ --include="*.md"
   ```

## 📊 Calculating Readiness Score

Use this formula to calculate your adaptation readiness:

```
Base Score Calculation:
- Each replaced standard placeholder: +6 points (15 × 6 = 90)
- project-config.yaml completed: +5 points
- Core commands tested: +5 points
Total possible: 100 points

Deductions:
- Each remaining placeholder in active commands: -2 points
- Each broken command: -5 points
- Missing required files: -10 points each
```

**Score Interpretation:**
- **90-100%**: Production ready! 🎉
- **70-89%**: Good progress, finish core replacements
- **50-69%**: Functional but needs work
- **Below 50%**: Continue customization

## 🛠️ Validation Script

Create this helper script as `validate-adaptation.sh`:

```bash
#!/bin/bash

echo "=== Claude Code Template Validation ==="
echo ""

# Check structure
echo "1. Checking directory structure..."
if [ -d ".claude" ] && [ -d ".claude-framework" ]; then
    echo "   ✅ Directory structure correct"
else
    echo "   ❌ Missing directories"
fi

# Count placeholders
echo ""
echo "2. Checking for remaining placeholders..."
count=$(grep -r "INSERT_" .claude/commands/ --include="*.md" 2>/dev/null | wc -l)
if [ "$count" -eq 0 ]; then
    echo "   ✅ All placeholders replaced"
else
    echo "   ⚠️  Found $count remaining placeholders"
fi

# Check config
echo ""
echo "3. Checking project configuration..."
if [ -f ".claude/config/project-config.yaml" ]; then
    config_count=$(grep "INSERT_" .claude/config/project-config.yaml | wc -l)
    if [ "$config_count" -eq 0 ]; then
        echo "   ✅ Configuration complete"
    else
        echo "   ❌ Configuration has $config_count unreplaced placeholders"
    fi
else
    echo "   ❌ Configuration file missing"
fi

# Check for duplicates
echo ""
echo "4. Checking for duplicate commands..."
duplicates=$(find .claude/commands -name "*.md" -type f | \
    xargs grep "^name:" 2>/dev/null | \
    awk -F: '{print $3}' | \
    sort | uniq -d | wc -l)
if [ "$duplicates" -eq 0 ]; then
    echo "   ✅ No duplicate commands"
else
    echo "   ❌ Found $duplicates duplicate command names"
fi

# Calculate score
echo ""
echo "5. Calculating readiness score..."
score=100
[ "$count" -gt 0 ] && score=$((score - count * 2))
[ "$config_count" -gt 0 ] && score=$((score - 10))
[ "$duplicates" -gt 0 ] && score=$((score - duplicates * 5))
[ $score -lt 0 ] && score=0

echo ""
echo "===================================="
echo "READINESS SCORE: ${score}%"
echo "===================================="

if [ $score -eq 100 ]; then
    echo "🎉 Your adaptation is complete!"
elif [ $score -ge 90 ]; then
    echo "📈 Almost there! Just a few items left."
elif [ $score -ge 70 ]; then
    echo "👍 Good progress. Focus on remaining placeholders."
else
    echo "🔧 Keep working on your customization."
fi
```

Make it executable:
```bash
chmod +x validate-adaptation.sh
./validate-adaptation.sh
```

## 🚨 Common Validation Issues

### Issue: Placeholders in Output
**Symptom:** Commands show `[INSERT_XXX]` in their responses  
**Fix:** You missed replacing placeholders in that command file

### Issue: Commands Not Found
**Symptom:** Claude Code says "Unknown command"  
**Fix:** Check YAML front matter has correct `name:` field

### Issue: Partial Replacements
**Symptom:** Seeing `]PROJECT_NAME]` or similar  
**Fix:** Your Find/Replace caught part of the placeholder

### Issue: Wrong Values After Replace
**Symptom:** Commands reference wrong technology  
**Fix:** You may have done replacements in wrong order

## 📝 Post-Validation Steps

Once validation passes:

1. **Document Your Choices**
   Create `ADAPTATION-NOTES.md`:
   ```markdown
   # Adaptation Notes for [Your Project]
   
   ## Placeholder Values Used
   - PROJECT_NAME: MyAwesomeApp
   - DOMAIN: e-commerce
   - TECH_STACK: Node.js/Express/PostgreSQL
   ...
   
   ## Commands Removed
   - /quantum-compute (not needed)
   - /blockchain-deploy (not applicable)
   
   ## Custom Modifications
   - Enhanced /deploy for our CI/CD
   - Added custom error handling to /task
   ```

2. **Test in Real Scenarios**
   - Run through a typical workflow
   - Test edge cases
   - Verify integrations work

3. **Share Your Success**
   - Use `/share-adaptation` to document your pattern
   - Submit to community via CONTRIBUTING.md
   - Help others with similar projects

## 🆘 Getting Help

If validation fails or you're stuck:

1. **Re-run the setup script** (won't overwrite customizations)
2. **Check EXAMPLES.md** for similar projects
3. **Use `/validate-adaptation` command** for interactive help
4. **Submit an issue** with your validation output

---

**Remember:** Validation ensures your templates work correctly. Take time to be thorough - it's worth it! 🎯