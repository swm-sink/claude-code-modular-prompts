---
name: /validate-adaptation
description: Check adaptation completeness and calculate readiness score (v2.0)
version: 2.0
usage: '/validate-adaptation [--verbose] [--auto-run] [--layer=1|2|3] [--export-report]'
category: meta
allowed-tools:
- Read
- Grep
- TodoWrite
- Bash
- Glob
dependencies: [adapt-to-project, replace-placeholders, quick-command, build-command, assemble-command]
validation:
  pre-execution: Check for .claude/ directory existence
  during-execution: Validate each checklist item systematically
  post-execution: Generate readiness score and action plan
progressive-disclosure:
  layer-integration: Validates adaptations for all 3 layers
  layer-1-checks: Auto-generation template readiness
  layer-2-checks: Customization JSON configs validation
  layer-3-checks: Component assembly framework integrity
error-recovery:
  missing-structure: Provides recovery instructions
  incomplete-adaptation: Generates specific fix commands
  validation-failures: Detailed remediation guidance
export-formats:
  markdown: Full validation report
  json: Machine-readable scores
  checklist: Interactive TODO format
---

# Validate Adaptation (v2.0)

## 🎯 Enhanced Validation with Progressive Disclosure Support

**v2.0 Enhancement**: This command now provides layer-aware validation with automated scanning capabilities and comprehensive readiness assessment across all three Progressive Disclosure layers.

### 🚀 What's New in v2.0
- **Layer-Aware Validation**: Specific checks for each Progressive Disclosure layer
- **Automated Scanning**: Uses Bash and Glob tools for systematic validation
- **Export Capabilities**: Generate reports in multiple formats
- **Error Recovery**: Detailed remediation for validation failures
- **Dependency Tracking**: Validates related command configurations

### 📊 Validation Capabilities by Layer

#### Layer 1 Validation (Auto-Generation)
- Quick command template availability
- Auto-generation readiness assessment
- Basic project detection capabilities

#### Layer 2 Validation (Guided Customization)
- Customization JSON config integrity
- Option filtering effectiveness
- Build command configuration

#### Layer 3 Validation (Component Assembly)
- Component library completeness
- Assembly template validation
- Compatibility matrix verification

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

## Enhanced v2.0 Validation Suite

### Automated Validation Commands
```bash
# v2.0 Enhanced validation with layer support
echo "=== Progressive Disclosure Layer Validation ==="

# Layer 1: Auto-Generation Readiness
echo "Layer 1 - Quick Command Templates:"
ls -la .claude/templates/*.template 2>/dev/null | wc -l

# Layer 2: Customization Configs
echo "Layer 2 - Build Configs:"
ls -la .claude/customization/*.json 2>/dev/null | wc -l

# Layer 3: Assembly Framework
echo "Layer 3 - Components:"
find .claude/components -name "*.md" 2>/dev/null | wc -l

# Comprehensive placeholder scan
echo "=== Checking Placeholders ==="
grep -r "\[INSERT_" .claude/ 2>/dev/null | wc -l

# Configuration validation
echo "=== Checking Config ==="
cat .claude/config/project-config.yaml 2>/dev/null || echo "No config found"

# Command inventory
echo "=== Command Count by Category ==="
for dir in .claude/commands/*/; do
  echo "$(basename "$dir"): $(find "$dir" -name "*.md" 2>/dev/null | wc -l)"
done

# v2.0 Feature validation
echo "=== v2.0 Features ==="
grep -l "version: 2.0" .claude/commands/*/*.md 2>/dev/null | wc -l
```

### Layer-Specific Validation

#### --layer=1 Validation
```bash
# Validate Layer 1 auto-generation readiness
echo "Checking /quick-command availability..."
test -f .claude/commands/core/quick-command.md && echo "✓ Found" || echo "✗ Missing"

echo "Checking templates..."
ls -la .claude/templates/*.template 2>/dev/null
```

#### --layer=2 Validation  
```bash
# Validate Layer 2 customization framework
echo "Checking /build-command..."
test -f .claude/commands/core/build-command.md && echo "✓ Found" || echo "✗ Missing"

echo "Checking customization configs..."
ls -la .claude/customization/*.json 2>/dev/null
```

#### --layer=3 Validation
```bash
# Validate Layer 3 assembly system
echo "Checking /assemble-command..."
test -f .claude/commands/core/assemble-command.md && echo "✓ Found" || echo "✗ Missing"

echo "Checking component library..."
find .claude/components -type f -name "*.md" | head -10
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

## Enhanced v2.0 Validation Report

### Export Options (--export-report)

#### Markdown Format (Default)
```markdown
ADAPTATION VALIDATION REPORT v2.0
=================================
Date: [TODAY'S DATE]
Project: [YOUR PROJECT NAME]
Framework Version: 2.0

PROGRESSIVE DISCLOSURE READINESS
--------------------------------
Layer 1 (Auto-Generation): [READY/NOT READY]
- Quick Command: [✓/✗]
- Templates: [COUNT]
- Readiness: [XX]%

Layer 2 (Customization): [READY/NOT READY]  
- Build Command: [✓/✗]
- JSON Configs: [COUNT]
- Readiness: [XX]%

Layer 3 (Assembly): [READY/NOT READY]
- Assemble Command: [✓/✗]
- Components: [COUNT]
- Readiness: [XX]%

CORE VALIDATION METRICS
-----------------------
Placeholders Found: [NUMBER]
Configuration Status: [EXISTS/MISSING]
Command Count: [NUMBER] ([NUMBER] v2.0)
Customization Level: [BASIC/MODERATE/ADVANCED]

Overall Readiness Score: [XX]%

RECOMMENDED ACTIONS
-------------------
1. [SPECIFIC ACTION WITH COMMAND]
2. [SPECIFIC ACTION WITH COMMAND]
3. [SPECIFIC ACTION WITH COMMAND]
```

#### JSON Format (--export-report --format=json)
```json
{
  "validation_report": {
    "version": "2.0",
    "date": "[ISO_DATE]",
    "project": "[PROJECT_NAME]",
    "progressive_disclosure": {
      "layer1": {
        "ready": false,
        "quick_command": false,
        "templates": 0,
        "score": 0
      },
      "layer2": {
        "ready": false,
        "build_command": false,
        "configs": 0,
        "score": 0
      },
      "layer3": {
        "ready": false,
        "assemble_command": false,
        "components": 0,
        "score": 0
      }
    },
    "core_metrics": {
      "placeholders": 0,
      "configuration": false,
      "commands": {
        "total": 0,
        "v2_0": 0
      },
      "customization_level": "basic"
    },
    "overall_score": 0,
    "actions": []
  }
}
```

### Error Recovery Guidance

#### Missing Progressive Disclosure Commands
```bash
# Quick fix for missing layer commands
echo "Installing Progressive Disclosure commands..."
cp .claude-framework/commands/core/quick-command.md .claude/commands/core/
cp .claude-framework/commands/core/build-command.md .claude/commands/core/
cp .claude-framework/commands/core/assemble-command.md .claude/commands/core/
```

#### v2.0 Migration Path
```bash
# Upgrade existing commands to v2.0
echo "Run these commands to upgrade:"
echo "/convert-to-v2 --batch=all"
echo "/validate-adaptation --layer=all"
```

Would you like me to run the comprehensive validation now?