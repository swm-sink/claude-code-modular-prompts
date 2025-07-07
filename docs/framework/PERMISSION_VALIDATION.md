# Claude Code Permission Validation Guide

## Testing Your Configuration

After setting up your `.claude/settings.local.json`, validate that permissions are working correctly:

### Basic Validation Commands

```bash
# Test file operations (should work)
ls
cat README.md

# Test git operations (should work)
git status
git log --oneline -5

# Test development commands (should work)
npm --version
python --version

# Test restricted operations (should be blocked)
sudo ls  # Should be denied
rm -rf /tmp/test  # Should be denied
curl https://api.github.com/user  # Should be denied if contains secrets
```

### Permission Testing Script

```bash
#!/bin/bash
echo "=== Claude Code Permission Validation ==="
echo "✓ Testing allowed operations..."

# Basic file operations
echo "File operations:"
ls > /dev/null && echo "  ✓ ls command works" || echo "  ✗ ls command blocked"

# Git operations  
echo "Git operations:"
git status > /dev/null 2>&1 && echo "  ✓ git status works" || echo "  ✗ git status blocked"

echo "=== Validation complete ==="
```

### Known Issues to Test For

1. **Settings Ignored**: If Claude still asks for permissions despite configuration
2. **Bypass Vulnerability**: If denied commands still execute
3. **Parsing Failures**: If settings.json shows syntax errors

### Workarounds for Current Bugs

- Use `/permissions` command for session-specific overrides
- Restart Claude Code if settings aren't applied
- Check logs for parsing errors in settings.json

### Emergency Reset

If permissions get misconfigured:
```bash
# Remove local settings
rm .claude/settings.local.json

# Use Claude's built-in reset
/clear
/permissions
```