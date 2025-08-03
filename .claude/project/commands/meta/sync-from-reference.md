---
name: /sync-from-reference
description: Pull updates from framework while preserving your customizations (v1.0)
version: "1.0"
usage: '/sync-from-reference [--preview] [--approve-all] [--rollback] [--validate-before] [--layer=1|2|3]'
category: meta
allowed-tools:
- Read
- Write
- Edit
- Grep
- Bash
- Glob
- TodoWrite
dependencies: [validate-adaptation, adapt-to-project, undo-adaptation]
validation:
  pre-execution: Backup current .claude directory before any changes
  during-execution: Validate each file operation for safety
  post-execution: Run comprehensive validation after sync
progressive-disclosure:
  layer-integration: Preserves layer-specific customizations during sync
  layer-1-protection: Quick command templates preserved
  layer-2-protection: Customization configs maintained
  layer-3-protection: Component assembly framework protected
safety-features:
  automatic-backup: Creates timestamped backup before sync
  conflict-detection: Identifies customized files before overwriting
  rollback-capability: Can restore previous state if issues occur
  dry-run-mode: Preview all changes without applying
tracking:
  sync-log: Automatic sync history tracking
  change-manifest: Detailed list of all modifications
  customization-preservation: Tracks user customizations
---

# Sync from Reference (v1.0)

## 🎯 Enhanced Framework Synchronization with Safety Features

**v1.0 Enhancement**: This command now provides intelligent sync capabilities with automatic backup, rollback support, and Progressive Disclosure layer protection to safely update your framework while preserving all customizations.

### 🚀 What's New in v1.0
- **Automatic Backup**: Creates timestamped backup before any changes
- **Layer Protection**: Preserves Progressive Disclosure customizations
- **Rollback Support**: Can restore previous state if issues occur
- **Smart Conflict Detection**: Identifies customized files before overwriting
- **Dry Run Mode**: Preview all changes without applying them
- **Sync History Tracking**: Automatic logging of all sync operations

### 🛡️ Safety Features

#### Pre-Sync Protection
- Automatic backup creation with timestamp
- Customization detection and preservation
- Validation of source framework integrity

#### During-Sync Safety
- File-by-file validation
- Conflict resolution prompts
- Progressive update application

#### Post-Sync Validation
- Automatic validation run
- Rollback option if issues detected
- Comprehensive sync report generation

## How Manual Sync Works

### 1. You Check for Updates
```bash
# If using git submodule:
cd .claude-framework
git fetch origin
git log HEAD..origin/main --oneline  # See what's new
```

### 2. You Review Changes
```bash
# Compare specific files
diff .claude/commands/core/task.md .claude-framework/commands/core/task.md

# Or see all differences
diff -r .claude/ .claude-framework/
```

### 3. You Decide What to Sync
- **New files**: Safe to copy
- **Your customized files**: Keep your version
- **Unchanged files with updates**: Consider updating

## Enhanced v1.0 Sync Process

### Step 1: Pre-Sync Safety Check (--validate-before)
```bash
# v1.0 Automatic backup
echo "Creating safety backup..."
cp -r .claude ".claude.backup-$(date +%Y%m%d-%H%M%S)"

# Validate current state
echo "Validating current adaptation..."
# Run /validate-adaptation internally
```

### Step 2: Smart Update Detection
```bash
# v1.0 Enhanced detection with layer awareness
echo "=== Checking for updates ==="

# Update reference framework
cd .claude-framework
git fetch origin
git log HEAD..origin/main --oneline

# Layer-specific checks
echo "Layer 1 (Auto-Generation) Updates:"
find .claude-framework/templates -newer .claude/.sync-timestamp 2>/dev/null

echo "Layer 2 (Customization) Updates:"
find .claude-framework/customization -newer .claude/.sync-timestamp 2>/dev/null

echo "Layer 3 (Components) Updates:"
find .claude-framework/components -newer .claude/.sync-timestamp 2>/dev/null
```

### Step 3: Intelligent File Categorization
```bash
# v1.0 Smart categorization with customization detection
echo "=== Analyzing files ==="

# Detect customized files
grep -l "PROJECT_NAME\|DOMAIN\|TECH_STACK" .claude/commands/*/*.md > .customized-files.tmp

# Categorize updates
echo "Safe to update (no customizations):"
find .claude-framework -name "*.md" | while read f; do
  local_file=".claude/${f#.claude-framework/}"
  if ! grep -q "$local_file" .customized-files.tmp; then
    echo "  ✓ $f"
  fi
done

echo "Requires manual review (customized):"
while read customized; do
  echo "  ⚠️  $customized"
done < .customized-files.tmp
```

### Step 3: Manual Review Strategy
I'll help you categorize files:

**Safe to Copy (New Files)**:
```bash
# Example: Copy new command
cp .claude-framework/commands/new-command.md .claude/commands/
```

**Skip (Your Customized Files)**:
- Files where you've replaced placeholders
- Commands you've modified
- Keep your versions

**Consider Updating (Unchanged Files)**:
- Files you haven't customized
- May have bug fixes or improvements
- Compare before copying

### Step 4: Manual Merge Process
For files you want to update:
```bash
# See differences first
diff .claude/commands/file.md .claude-framework/commands/file.md

# If you want the update
cp .claude-framework/commands/file.md .claude/commands/

# Then re-apply your customizations
```

## What I Can Help With

When you tell me you want to sync:
- I'll provide the right commands to run
- I'll explain what to look for
- I'll suggest safe update strategies
- I'll help you create a sync checklist

## Example Guidance I Provide

```markdown
MANUAL SYNC CHECKLIST
====================

Based on your description, here's what to do:

New Files to Copy:
□ cp .claude-framework/commands/api-gateway.md .claude/commands/
□ cp .claude-framework/commands/test-contract.md .claude/commands/

Files to Compare (you haven't customized):
□ diff .claude/commands/query.md .claude-framework/commands/query.md
□ diff .claude/commands/help.md .claude-framework/commands/help.md

Files to Skip (you've customized):
□ /deploy - Keep your AWS adaptations
□ /test-unit - Keep your Jest customizations

After Copying New Files:
□ Add placeholders for your project
□ Run validation checks
```

## Conflict Resolution

If a command has both:
- Framework updates
- Your customizations

Options:
1. Keep your version (default)
2. View differences
3. Manual merge
4. Create backup and update

## Best Practices

### Before Syncing
- Commit your current state
- Run `/validate-adaptation` 
- Note your customizations

### After Syncing
- Review new commands
- Run `/adapt-to-project` for new items
- Test critical workflows
- Update documentation

## Enhanced v1.0 Sync Tracking

### Automatic Sync History (v1.0)
```bash
# v1.0 creates detailed sync manifest automatically
cat > .claude/SYNC-MANIFEST-$(date +%Y%m%d-%H%M%S).json << 'EOF'
{
  "sync_date": "$(date -Iseconds)",
  "framework_version": "$(cd .claude-framework && git describe --tags)",
  "framework_commit": "$(cd .claude-framework && git rev-parse HEAD)",
  "operations": {
    "files_added": [],
    "files_updated": [],
    "files_skipped": [],
    "customizations_preserved": []
  },
  "validation": {
    "pre_sync_score": 0,
    "post_sync_score": 0,
    "issues_found": []
  },
  "backup_location": ".claude.backup-$(date +%Y%m%d-%H%M%S)"
}
EOF
```

### Rollback Support (--rollback)
```bash
# v1.0 Easy rollback to previous state
echo "=== Available Backups ==="
ls -la .claude.backup-* | tail -5

# Rollback to specific backup
echo "To rollback, use:"
echo "rm -rf .claude"
echo "mv .claude.backup-TIMESTAMP .claude"
echo "/validate-adaptation"
```

### Dry Run Mode (--preview)
```bash
# v1.0 Preview all changes without applying
echo "=== DRY RUN MODE ==="
echo "The following changes would be made:"

# Show what would be copied
echo "New files to add:"
find .claude-framework -name "*.md" -type f | while read f; do
  local_file=".claude/${f#.claude-framework/}"
  [ ! -f "$local_file" ] && echo "  + $f"
done

# Show what would be updated
echo "Files to update:"
# ... comparison logic ...

echo "No changes have been applied. Remove --preview to execute."
```

## Layer-Specific Sync Guidance (--layer=N)

### Layer 1 Sync (Auto-Generation)
```bash
# Sync only Layer 1 components
echo "Syncing Layer 1 (Auto-Generation) components..."
cp -n .claude-framework/commands/core/quick-command.md .claude/commands/core/
cp -r .claude-framework/templates/*.template .claude/templates/
echo "Layer 1 sync complete"
```

### Layer 2 Sync (Customization)
```bash
# Sync only Layer 2 components
echo "Syncing Layer 2 (Customization) framework..."
cp -n .claude-framework/commands/core/build-command.md .claude/commands/core/
cp -r .claude-framework/customization/*.json .claude/customization/
echo "Layer 2 sync complete"
```

### Layer 3 Sync (Assembly)
```bash
# Sync only Layer 3 components
echo "Syncing Layer 3 (Assembly) system..."
cp -n .claude-framework/commands/core/assemble-command.md .claude/commands/core/
rsync -av --ignore-existing .claude-framework/components/ .claude/components/
cp -r .claude-framework/assembly-templates/ .claude/
echo "Layer 3 sync complete"
```

## Post-Sync Validation Report

### v1.0 Automatic Post-Sync Report
```markdown
SYNC COMPLETION REPORT v1.0
===========================
Date: [TIMESTAMP]
Sync Type: [FULL|LAYER-SPECIFIC|PREVIEW]

FILES SYNCED
------------
Added: [COUNT] files
Updated: [COUNT] files  
Skipped: [COUNT] files (customized)
Preserved: [COUNT] customizations

VALIDATION RESULTS
------------------
Pre-Sync Score: [XX]%
Post-Sync Score: [XX]%
Issues Found: [LIST]

LAYER STATUS
------------
Layer 1: [SYNCED|SKIPPED|ERROR]
Layer 2: [SYNCED|SKIPPED|ERROR]
Layer 3: [SYNCED|SKIPPED|ERROR]

NEXT STEPS
----------
1. Run /validate-adaptation --layer=all
2. Test critical workflows
3. Review new features in [LIST]

ROLLBACK AVAILABLE
------------------
Backup: [BACKUP_PATH]
Command: /sync-from-reference --rollback
```

## How Can I Help?

Tell me:
1. **"I want to check for updates"** → I'll provide the commands
2. **"I found new files"** → I'll help you evaluate them
3. **"I need to merge changes"** → I'll guide you through it
4. **"Preview sync for Layer 2"** → I'll show layer-specific changes
5. **"Rollback last sync"** → I'll restore your previous state