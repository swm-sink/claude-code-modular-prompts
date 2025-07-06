# 🔧 PERMISSION TROUBLESHOOTING GUIDE

## Quick Reference

### 🚨 Emergency One-Liner
```bash
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### 🏥 Full Recovery
```bash
.claude/tools/emergency_permission_recovery.sh
```

### 🛡️ Check Health
```bash
python .claude/tools/permission_fortress.py check
```

## Common Issues & Solutions

### 1. ❌ "Permission Denied" Errors

**Symptoms:**
- Commands fail with permission errors
- Claude asks for permissions repeatedly
- Previously working commands stop working

**Solution:**
```bash
# Run emergency recovery
.claude/tools/emergency_permission_recovery.sh

# Or quick fix
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### 2. 🔄 Symlink Points to Temp Directory

**Symptoms:**
- Symlink exists but points to `/var/folders/`, `/tmp/`, or similar
- Permissions work temporarily then break
- Fortress reports "symlink hijacked"

**Cause:** Claude Code sometimes creates temp directory redirects

**Solution:**
```bash
# The fortress now auto-detects this!
python .claude/tools/permission_fortress.py check

# Manual fix if needed
rm -f .claude/settings.local.json
ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### 3. 📝 Local Settings is Not a Symlink

**Symptoms:**
- `.claude/settings.local.json` exists as a regular file
- Permissions get overwritten
- Changes don't persist

**Solution:**
```bash
# Backup the file first (if it has custom settings)
cp .claude/settings.local.json .claude/permission_backups/manual_backup.json

# Then convert to symlink
rm -f .claude/settings.local.json
ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### 4. 🚫 Permission Prompts Keep Appearing

**CRITICAL:** Never click "Yes" on permission prompts!

**Why:** Clicking "Yes" resets permissions to minimal set

**What to do:**
1. Always click "No" or close the prompt
2. The command will still work via pre-configured permissions
3. If it doesn't work, run recovery script

### 5. 🔍 Fortress Can't Find Settings

**Symptoms:**
- "Global settings file not found"
- "Permission fortress check failed"

**Solution:**
```bash
# Create global settings directory
mkdir -p ~/.claude

# Run emergency recovery to create settings
.claude/tools/emergency_permission_recovery.sh
```

## Diagnostic Commands

### Check Symlink Status
```bash
# See what the symlink points to
ls -la .claude/settings.local.json

# Get the actual target
readlink .claude/settings.local.json

# Get the fully resolved path
readlink -f .claude/settings.local.json
```

### View Current Permissions
```bash
# Count permissions
cat ~/.claude/settings.json | jq '.permissions.allow | length'

# List all permissions
cat ~/.claude/settings.json | jq '.permissions.allow[]'
```

### Check Fortress Logs
```bash
# View recent activity
tail -20 .claude/permission_fortress.log

# Search for errors
grep ERROR .claude/permission_fortress.log
```

## Prevention Tips

### 1. Enable Startup Protection
Add to your `~/.zshrc` or `~/.bashrc`:
```bash
source /path/to/project/.claude/tools/fortress_startup.sh
```

### 2. Run Continuous Monitoring
```bash
# In a separate terminal
python .claude/tools/permission_fortress.py monitor
```

### 3. Use Aliases
```bash
alias fortress='python /path/to/project/.claude/tools/permission_fortress.py'
alias fix-permissions='.claude/tools/emergency_permission_recovery.sh'
```

## Advanced Troubleshooting

### Manual Permission Repair
If automated tools fail:

```bash
# 1. Remove all permission files
rm -f .claude/settings.local.json
rm -f .claude/settings.json

# 2. Create comprehensive global settings
cat > ~/.claude/settings.json << 'EOF'
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1"
  },
  "permissions": {
    "allow": [
      "Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)",
      "Glob(*)", "Grep(*)", "LS(*)", "Task(*)", "WebFetch(*)", 
      "WebSearch(*)", "TodoRead(*)", "TodoWrite(*)",
      "NotebookRead(*)", "NotebookEdit(*)", "exit_plan_mode(*)",
      "mcp__ide__getDiagnostics(*)", "mcp__ide__executeCode(*)", "mcp__*"
    ],
    "deny": [
      "Bash(rm -rf /:*)", "Bash(sudo su:*)", "Bash(dd:*)", "Bash(mkfs:*)"
    ]
  },
  "model": "opus"
}
EOF

# 3. Create symlink
cd /path/to/project
ln -sf ~/.claude/settings.json .claude/settings.local.json

# 4. Verify
python .claude/tools/permission_fortress.py check
```

### Debug Mode
For detailed troubleshooting:
```bash
# Run fortress with verbose logging
python .claude/tools/permission_fortress.py check 2>&1 | tee debug.log

# Check file system events
fswatch -x .claude/settings.local.json
```

## When All Else Fails

1. **Restart Claude Code** - Sometimes a fresh start helps
2. **Check GitHub Issues** - Known bugs: #2014, #961
3. **Nuclear Option** - Delete all Claude settings and start fresh:
   ```bash
   rm -rf ~/.claude
   rm -rf .claude/settings*
   .claude/tools/emergency_permission_recovery.sh
   ```

## Remember

- 🚫 **NEVER** accept permission prompts
- ✅ **ALWAYS** use the symlink strategy
- 🛡️ **MONITOR** with fortress for peace of mind
- 🔧 **RECOVER** quickly with emergency scripts

The permission system is robust once properly configured. These issues are due to Claude Code bugs, not your configuration.