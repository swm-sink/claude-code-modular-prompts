---
name: /sync-from-reference
description: "Pull updates from framework while preserving your customizations"
usage: /sync-from-reference [--preview] [--approve-all]
category: meta-commands
tools: Read, Write, Edit, Grep, Bash
---

# Manual Sync Guide for Framework Updates

## 🎯 What This Command Actually Does

**I provide sync guidance, not automated syncing.** I'll help you manually update from the reference framework by:
- 📋 Showing git commands to check for updates
- 🔍 Explaining how to compare versions
- 📝 Providing manual merge strategies
- ✅ Creating verification checklists

## ⚠️ What I Cannot Do
- ❌ Automatically detect updates
- ❌ Merge files for you
- ❌ Track what you've customized
- ❌ Apply changes programmatically

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

## Manual Sync Process

### Step 1: Update Reference Framework
```bash
# If using git submodule:
cd .claude-framework
git pull origin main
cd ..

# If direct clone:
cd .claude-framework
git pull
cd ..
```

### Step 2: Find What's New
```bash
# List new commands
diff <(ls .claude/commands/) <(ls .claude-framework/commands/)

# Find new files
find .claude-framework -type f -name "*.md" | while read f; do
  if [ ! -f ".claude/${f#.claude-framework/}" ]; then
    echo "NEW: $f"
  fi
done
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

## Manual Tracking

To track your syncs manually:

### Create a Sync Log
```bash
# Create sync history file
echo "## Sync History" > .claude/SYNC-LOG.md
echo "" >> .claude/SYNC-LOG.md
echo "### $(date '+%Y-%m-%d')" >> .claude/SYNC-LOG.md
echo "- Updated from commit: $(cd .claude-framework && git rev-parse HEAD)" >> .claude/SYNC-LOG.md
echo "- New files added: [list]" >> .claude/SYNC-LOG.md
echo "- Files updated: [list]" >> .claude/SYNC-LOG.md
```

### Manual Backup Before Sync
```bash
# Always backup first
cp -r .claude .claude.backup-pre-sync-$(date +%Y%m%d)
```

## How Can I Help?

Tell me:
1. **"I want to check for updates"** → I'll provide the commands
2. **"I found new files"** → I'll help you evaluate them
3. **"I need to merge changes"** → I'll guide you through it
4. **"Help me track this sync"** → I'll create documentation