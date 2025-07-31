---
name: /undo-adaptation
description: Revert adaptations to previous state with full recovery capability (v2.0)
version: 2.0
usage: '/undo-adaptation [--last|--to-snapshot snapshot-id] [--preview] [--layer=1|2|3] [--selective]'
category: meta
allowed-tools:
- Read
- Write
- MultiEdit
- Bash
- Glob
- TodoWrite
dependencies: [validate-adaptation, sync-from-reference, adapt-to-project]
validation:
  pre-execution: Verify backup availability before recovery
  during-execution: Validate each recovery operation
  post-execution: Run comprehensive validation after recovery
progressive-disclosure:
  layer-integration: Layer-aware recovery preserves appropriate customizations
  layer-1-recovery: Quick command and template restoration
  layer-2-recovery: Customization framework restoration
  layer-3-recovery: Component assembly system restoration
recovery-features:
  automatic-detection: Finds all available backups automatically
  selective-recovery: Choose specific files or directories to restore
  validation-integration: Automatic post-recovery validation
  git-integration: Seamless integration with version control
safety-features:
  preview-mode: See what would be restored before applying
  partial-recovery: Restore only affected components
  validation-check: Ensures restored state is functional
tracking:
  recovery-log: Automatic logging of all recovery operations
  state-comparison: Shows differences between current and backup
---

# Undo Adaptation (v2.0)

## 🎯 Enhanced Recovery System with Intelligent Restoration

**v2.0 Enhancement**: This command now provides intelligent recovery capabilities with automatic backup detection, layer-aware restoration, selective recovery options, and comprehensive validation to safely restore your framework to any previous state.

### 🚀 What's New in v2.0
- **Automatic Backup Detection**: Finds all available backups and sync points
- **Layer-Aware Recovery**: Preserves customizations by Progressive Disclosure layer
- **Selective Recovery**: Choose specific files or directories to restore
- **Preview Mode**: See exactly what will be restored before applying
- **Git Integration**: Seamless recovery from version control
- **Validation Integration**: Automatic post-recovery validation

### 🛡️ Recovery Features

#### Intelligent Backup Detection
- Automatically finds all .claude.backup-* directories
- Detects git commits with framework changes
- Lists sync manifests from sync operations
- Shows recovery options sorted by date

#### Layer-Specific Recovery
- **Layer 1**: Restore quick command templates only
- **Layer 2**: Restore customization framework only
- **Layer 3**: Restore component assembly system only
- **Full**: Complete framework restoration

#### Selective Recovery Options
- Restore specific commands or categories
- Preserve certain customizations
- Mix and match from different backups
- Cherry-pick individual files

## Enhanced v2.0 Recovery Options

### Automatic Backup Detection
```bash
# v2.0 finds all recovery points automatically
echo "=== Available Recovery Points ==="

# Find all backups
echo "Backups:"
ls -la .claude.backup-* 2>/dev/null | sort -r

# Find sync manifests
echo "Sync Points:"
ls -la .claude/SYNC-MANIFEST-*.json 2>/dev/null | sort -r

# Git recovery points
echo "Git Commits:"
git log --oneline -10 -- .claude/ 2>/dev/null
```

### Layer-Specific Recovery (--layer=N)
```bash
# v2.0 Layer 1 recovery only
echo "Restoring Layer 1 (Auto-Generation)..."
cp .claude.backup-latest/commands/core/quick-command.md .claude/commands/core/
cp -r .claude.backup-latest/templates/ .claude/

# v2.0 Layer 2 recovery only
echo "Restoring Layer 2 (Customization)..."
cp .claude.backup-latest/commands/core/build-command.md .claude/commands/core/
cp -r .claude.backup-latest/customization/ .claude/

# v2.0 Layer 3 recovery only
echo "Restoring Layer 3 (Assembly)..."
cp .claude.backup-latest/commands/core/assemble-command.md .claude/commands/core/
cp -r .claude.backup-latest/components/ .claude/
cp -r .claude.backup-latest/assembly-templates/ .claude/
```

### Selective Recovery (--selective)
```bash
# v2.0 Interactive selection
echo "=== Selective Recovery Mode ==="
echo "Choose what to restore:"
echo "1. Commands only"
echo "2. Components only"
echo "3. Configuration only"
echo "4. Specific categories"
echo "5. Individual files"
```

### Preview Mode (--preview)
```bash
# v2.0 See what would be restored
echo "=== PREVIEW MODE ==="
echo "The following would be restored from .claude.backup-20250731:"

# Show differences
diff -r .claude .claude.backup-20250731 | grep "Only in .claude.backup" | head -20

echo "No changes applied. Remove --preview to execute recovery."
```

## Manual Backup Strategy

### Before Making Changes
**Always create a manual backup first:**
```bash
# Simple backup
cp -r .claude .claude.backup-$(date +%Y%m%d-%H%M%S)

# Or use git
git add .
git commit -m "Backup before adaptation"
```

### Organizing Your Backups
Recommended structure:
```
project/
├── .claude/                    # Current working version
├── .claude.backup-20250728/    # Manual backups
├── .claude.backup-20250727/
└── .claude-framework/          # Original reference
```

### Recovery Checklist
When you need to recover:
- [ ] Stop current work immediately
- [ ] Identify what went wrong
- [ ] Locate appropriate backup
- [ ] Test recovery in safe location first
- [ ] Apply recovery
- [ ] Verify functionality

## Recovery Scenarios

### Scenario 1: Bad Placeholder Replacement
**Problem**: Replaced wrong values throughout files
**Recovery**:
```bash
# If using git
git diff .claude/  # See what changed
git checkout -- .claude/  # Revert all

# If no git, from backup
cp -r .claude.backup-latest/.claude .
```

### Scenario 2: Deleted Important Commands
**Problem**: Removed commands you need
**Recovery**:
```bash
# From reference framework
cp .claude-framework/commands/[command].md .claude/commands/

# Or from backup
cp .claude.backup/commands/[command].md .claude/commands/
```

### Scenario 3: Broken Configuration
**Problem**: Framework not working after changes
**Recovery**:
```bash
# Start fresh from reference
rm -rf .claude
cp -r .claude-framework/.claude .
# Then reapply your customizations carefully
```

## Creating Your Own History

### Manual Change Log
Create `.claude/CHANGES.md`:
```markdown
# Adaptation History

## 2025-07-28 - Placeholder Replacement
- Replaced [INSERT_PROJECT_NAME] with "MyApp"
- Replaced [INSERT_DOMAIN] with "web-dev"
- Files affected: 45
- Backup: .claude.backup-20250728/

## 2025-07-27 - Initial Setup
- Imported framework
- Selected web-dev commands
- Files affected: 25
- Backup: .claude.backup-20250727/
```

### Git History (Better)
```bash
# View your adaptation history
git log --oneline -- .claude/

# See what changed in each commit
git show <commit-hash>
```

## Selective Recovery

### Recovering Specific Files
```bash
# From git
git checkout HEAD~1 -- .claude/commands/core/task.md

# From backup
cp .claude.backup/commands/core/task.md .claude/commands/core/

# From reference
cp .claude-framework/commands/core/task.md .claude/commands/core/
```

### Recovering by Category
```bash
# Example: Restore all database commands
cp .claude-framework/commands/database/*.md .claude/commands/database/

# Or from backup
cp .claude.backup/commands/database/*.md .claude/commands/database/
```

## Prevention is Better Than Recovery

### Before Any Adaptation
1. **Always use version control**
   ```bash
   git init
   git add .
   git commit -m "Before framework adaptation"
   ```

2. **Create manual backup**
   ```bash
   cp -r .claude .claude.backup-$(date +%Y%m%d)
   ```

3. **Document what you're doing**
   ```bash
   echo "Adapting for web-dev project" > .claude/ADAPTATION-NOTES.md
   ```

### Safe Adaptation Workflow
1. Backup → 2. Make small changes → 3. Test → 4. Commit → 5. Repeat

### If Things Go Wrong
1. Don't panic
2. Stop making changes
3. Assess the damage
4. Use appropriate recovery method
5. Learn from the mistake

## Common Recovery Situations

### "I messed up all my placeholders"
```bash
# Option 1: Revert with git
git checkout -- .claude/

# Option 2: Start fresh
rm -rf .claude
cp -r .claude-framework/.claude .
# Then use /adapt-to-project again
```

### "I deleted files I need"
```bash
# Restore from framework
cp .claude-framework/commands/needed-command.md .claude/commands/

# Or check git
git status  # Shows deleted files
git checkout -- path/to/deleted/file
```

### "Nothing works anymore"
```bash
# Nuclear option - start over
mv .claude .claude.broken
cp -r .claude-framework/.claude .

# Then examine what went wrong
diff -r .claude.broken .claude
```

## Enhanced v2.0 Recovery Tracking

### Automatic Recovery Log
```bash
# v2.0 creates detailed recovery log
cat > .claude/RECOVERY-LOG-$(date +%Y%m%d-%H%M%S).json << 'EOF'
{
  "recovery_date": "$(date -Iseconds)",
  "recovery_type": "[FULL|LAYER|SELECTIVE]",
  "source": {
    "type": "[BACKUP|GIT|SYNC]",
    "location": "[PATH_OR_COMMIT]",
    "date": "[SOURCE_DATE]"
  },
  "operations": {
    "files_restored": [],
    "files_preserved": [],
    "customizations_kept": []
  },
  "validation": {
    "pre_recovery_score": 0,
    "post_recovery_score": 0,
    "issues_resolved": [],
    "new_issues": []
  }
}
EOF
```

### Post-Recovery Validation
```bash
# v2.0 Automatic validation after recovery
echo "=== Post-Recovery Validation ==="

# Check framework integrity
echo "Checking framework structure..."
test -d .claude/commands && echo "✓ Commands directory" || echo "✗ Commands missing"
test -d .claude/components && echo "✓ Components directory" || echo "✗ Components missing"
test -d .claude/context && echo "✓ Context directory" || echo "✗ Context missing"

# Check Progressive Disclosure layers
echo "Checking Progressive Disclosure..."
test -f .claude/commands/core/quick-command.md && echo "✓ Layer 1" || echo "✗ Layer 1"
test -f .claude/commands/core/build-command.md && echo "✓ Layer 2" || echo "✗ Layer 2"
test -f .claude/commands/core/assemble-command.md && echo "✓ Layer 3" || echo "✗ Layer 3"

# Run full validation
echo "Running comprehensive validation..."
# Internal call to /validate-adaptation
```

### Recovery Comparison Report
```markdown
RECOVERY COMPLETION REPORT v2.0
================================
Date: [TIMESTAMP]
Recovery Type: [FULL|LAYER-SPECIFIC|SELECTIVE]
Source: [BACKUP_PATH|GIT_COMMIT]

FILES RECOVERED
---------------
Restored: [COUNT] files
Preserved: [COUNT] customizations
Skipped: [COUNT] files

VALIDATION RESULTS
------------------
Pre-Recovery Issues: [LIST]
Post-Recovery Status: [HEALTHY|ISSUES_FOUND]
Resolved Issues: [LIST]

LAYER STATUS
------------
Layer 1: [RESTORED|PRESERVED|PARTIAL]
Layer 2: [RESTORED|PRESERVED|PARTIAL]
Layer 3: [RESTORED|PRESERVED|PARTIAL]

CUSTOMIZATIONS
--------------
Preserved: [LIST]
Lost: [LIST]

NEXT STEPS
----------
1. Review restored configuration
2. Re-apply any lost customizations
3. Run /validate-adaptation
4. Test critical workflows
```

## Smart Recovery Scenarios (v2.0)

### Scenario: "I broke Layer 2 customization"
```bash
# v2.0 targeted recovery
/undo-adaptation --layer=2 --preview
# Shows only Layer 2 files that would be restored
# Preserves Layer 1 and 3 customizations
```

### Scenario: "I need yesterday's components only"
```bash
# v2.0 selective recovery
/undo-adaptation --selective --to-snapshot .claude.backup-20250730
# Interactive selection of just component files
```

### Scenario: "Show me what changed"
```bash
# v2.0 state comparison
/undo-adaptation --compare .claude.backup-latest
# Shows detailed diff between current and backup
```

## Recovery Assistance

Tell me your situation:
1. **"I replaced wrong values"** → I'll guide you through targeted recovery
2. **"I deleted important files"** → I'll help restore them selectively
3. **"I need to start over"** → I'll provide layer-aware reset options
4. **"I broke Layer 2"** → I'll restore just that layer
5. **"Show recovery options"** → I'll list all available recovery points
6. **"Compare with backup"** → I'll show what's different