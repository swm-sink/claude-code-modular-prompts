# 🚀 CLAUDE CODE PERMISSION QUICK REFERENCE

## 🚨 EMERGENCY FIXES (Copy & Paste)

### Fix #1: Quick Symlink Repair (Most Common)
```bash
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### Fix #2: Full Recovery Script
```bash
.claude/tools/emergency_permission_recovery.sh
```

### Fix #3: Fortress Auto-Repair
```bash
python .claude/tools/permission_fortress.py check
```

## ⚡ COMMON COMMANDS

| What You Want | Command |
|--------------|---------|
| Check if permissions are OK | `python .claude/tools/permission_fortress.py check` |
| Fix broken permissions | `rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json` |
| Start monitoring | `python .claude/tools/permission_fortress.py monitor` |
| Emergency recovery | `.claude/tools/emergency_permission_recovery.sh` |
| Check symlink target | `readlink .claude/settings.local.json` |
| View permission count | `cat ~/.claude/settings.json \| jq '.permissions.allow \| length'` |
| Stop monitoring | `pkill -f 'permission_fortress.py monitor'` |

## 🔴 CRITICAL RULES

1. **NEVER** click "Yes" on permission prompts - ALWAYS decline
2. **NEVER** manually edit `.claude/settings.local.json`
3. **ALWAYS** maintain the symlink to `~/.claude/settings.json`

## 🟢 SIGNS EVERYTHING IS WORKING

- ✅ No permission prompts appear
- ✅ Commands execute without asking
- ✅ `fortress check` shows all green
- ✅ Symlink points to `~/.claude/settings.json`

## 🟡 WARNING SIGNS

- ⚠️ Claude asks for permissions
- ⚠️ Commands fail with "permission denied"
- ⚠️ Symlink points to `/var/folders/` or `/tmp/`
- ⚠️ `.claude/settings.local.json` is a regular file

## 💡 PRO TIPS

### Add to Shell Startup (~/.zshrc)
```bash
# Auto-protect on terminal start
source /path/to/project/.claude/tools/fortress_startup.sh

# Helpful aliases
alias fortress='python /path/to/project/.claude/tools/permission_fortress.py'
alias fix-perms='rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json'
```

### Background Monitoring
```bash
# Run in separate terminal
python .claude/tools/permission_fortress.py monitor

# Or run detached
nohup python .claude/tools/permission_fortress.py monitor &
```

## 📊 STATUS CHECK CHECKLIST

```bash
# 1. Is symlink present?
ls -la .claude/settings.local.json

# 2. Where does it point?
readlink .claude/settings.local.json

# 3. Are permissions comprehensive?
cat ~/.claude/settings.json | jq '.permissions.allow | length'  # Should be ~20+

# 4. Run fortress check
python .claude/tools/permission_fortress.py check
```

## 🆘 LAST RESORT

If nothing works:
```bash
# Nuclear option - complete reset
rm -rf ~/.claude
rm -rf .claude/settings*
.claude/tools/emergency_permission_recovery.sh
```

---

**Remember:** The fortress system is self-healing. Most issues resolve with a simple `fortress check`!