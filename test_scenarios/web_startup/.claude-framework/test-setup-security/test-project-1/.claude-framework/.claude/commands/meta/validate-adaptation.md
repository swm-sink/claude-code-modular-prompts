---
name: /validate-adaptation
description: "Check adaptation completeness and calculate readiness score"
usage: /validate-adaptation [--verbose] [--auto-run]
category: meta-commands
tools: Read, Grep, TodoWrite
---

# Manual Validation Checklist

## 🎯 What This Command Actually Does

**I provide a validation checklist, not automated scanning.** I'll help you manually verify your adaptation by:
- 📋 Providing comprehensive checklists
- 🔍 Suggesting manual verification commands
- 📊 Helping you calculate your own readiness score
- 💡 Recommending next steps based on what you find

## ⚠️ What I Cannot Do
- ❌ Automatically scan your files for placeholders
- ❌ Read your configuration files
- ❌ Calculate scores programmatically
- ❌ Detect missing or misconfigured items

## Manual Validation Checklist

### 1. Check for Unreplaced Placeholders
Run these commands in your terminal to find placeholders:
```bash
# Find all remaining placeholders
grep -r "\[INSERT_" .claude/commands/
grep -r "\[INSERT_" .claude/components/
grep -r "\[INSERT_" .claude/context/
grep "\[INSERT_" CLAUDE.md
```

**Checklist:**
□ No results from placeholder search
□ All project-specific values replaced
□ Nested placeholders resolved

### 2. Verify Project Configuration
Check these files manually:
```bash
# Check if configuration exists
ls -la .claude/config/project-config.yaml
cat .claude/config/project-config.yaml
```

**Checklist:**
□ project-config.yaml exists
□ All fields have real values (not placeholders)
□ Domain matches your project type
□ Tech stack is accurate

### 3. Review Command Selection
```bash
# List your commands
ls -la .claude/commands/
ls -la .claude/commands/*/
```

**Checklist:**
□ Only commands you need are present
□ Domain-specific commands added
□ Unused commands removed
□ Core commands (help, task) retained

### 4. Check Framework Structure
```bash
# Verify structure
tree .claude/ -L 2
# or
find .claude -type d
```

**Checklist:**
□ .claude/commands/ exists with subfolders
□ .claude/components/ has key components  
□ .claude/context/ has anti-patterns
□ CLAUDE.md exists and is customized

## Manual Readiness Score Calculation

Calculate your score yourself:

### Scoring Guide
Start with 100% and subtract:
- **Each unreplaced placeholder found**: -5%
- **No project-config.yaml**: -20%
- **Using all default commands**: -10%
- **No domain customization**: -15%
- **Default security settings**: -10%

### Score Interpretation
- **0-40%**: Just imported, needs significant work
- **41-70%**: Basic adaptation started
- **71-90%**: Good adaptation progress
- **91-100%**: Fully customized for your project

### Example Calculation
```
Starting score: 100%
Found 6 placeholders: -30%
No domain commands: -15%
Using defaults: -10%
Final score: 45% (Basic adaptation needed)
```

## Validation Commands Summary

Copy and run these in your terminal:
```bash
# Full validation suite
echo "=== Checking Placeholders ==="
grep -r "\[INSERT_" .claude/ | wc -l

echo "=== Checking Config ==="
cat .claude/config/project-config.yaml 2>/dev/null || echo "No config found"

echo "=== Counting Commands ==="
find .claude/commands -name "*.md" | wc -l

echo "=== Checking Structure ==="
ls -la .claude/
```

## Next Steps Based on Your Findings

### If you found placeholders:
1. Run `/replace-placeholders` for a replacement guide
2. Manually update each file
3. Re-run validation checks

### If configuration is missing:
1. Create `.claude/config/project-config.yaml`
2. Copy the template from `/adapt-to-project`
3. Fill in your project values

### If using all defaults:
1. Remove commands you don't need
2. Add domain-specific commands
3. Customize core commands

## Manual Validation Report

After running the checks above, create your own report:
```markdown
ADAPTATION VALIDATION REPORT
===========================
Date: [TODAY'S DATE]
Project: [YOUR PROJECT NAME]

Placeholders Found: [NUMBER]
Configuration Status: [EXISTS/MISSING]
Command Count: [NUMBER]
Customization Level: [BASIC/MODERATE/ADVANCED]

Calculated Score: [XX]%

Next Actions:
1. [SPECIFIC ACTION]
2. [SPECIFIC ACTION]
3. [SPECIFIC ACTION]
```

Would you like help with any specific validation step?