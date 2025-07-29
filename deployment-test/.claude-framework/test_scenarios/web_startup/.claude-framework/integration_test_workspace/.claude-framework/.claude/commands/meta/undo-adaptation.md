---
name: /undo-adaptation
description: "Revert adaptations to previous state with full recovery capability"
usage: /undo-adaptation [--last|--to-snapshot snapshot-id] [--preview]
category: meta-commands
tools: Read, Write, MultiEdit, Bash
---

# Manual Recovery Guide for Framework Adaptations

## 🎯 What This Command Actually Does

**I'm a recovery guide, not an undo system.** I'll help you manually recover from adaptation mistakes by:
- 📋 Providing manual backup and recovery strategies
- 🔍 Suggesting version control commands
- 📝 Creating recovery checklists
- 💡 Recommending best practices for safe adaptation

## ⚠️ What I Cannot Do
- ❌ Automatically create or restore backups
- ❌ Track adaptation history
- ❌ Revert changes programmatically
- ❌ Maintain snapshots or state

## Manual Recovery Options

### Using Git (Recommended)
If you're using version control:
```bash
# View recent changes
git status
git diff

# Revert specific files
git checkout -- .claude/commands/core/task.md

# Revert all framework changes
git checkout -- .claude/

# Or reset to previous commit
git reset --hard HEAD~1
```

### Manual Backup Recovery
If you created manual backups:
```bash
# List your backups
ls -la .claude.backup*

# Restore from backup
cp -r .claude.backup-20250728/* .claude/
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

## Recovery Assistance

Tell me your situation:
1. **"I replaced wrong values"** → I'll guide you through reverting
2. **"I deleted important files"** → I'll help you restore them
3. **"I need to start over"** → I'll provide a clean slate guide
4. **"I want to prevent this"** → I'll share backup strategies