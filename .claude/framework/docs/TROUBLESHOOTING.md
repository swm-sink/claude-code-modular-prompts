# Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### Submodule Not Cloning
**Problem**: `git submodule add` fails or hangs

**Solutions**:
1. Check network connection
2. Verify repository URL
3. Try with SSH instead of HTTPS:
   ```bash
   git submodule add git@github.com:USER/repo.git .claude-context
   ```
4. Clear git cache:
   ```bash
   git rm --cached .claude-context
   git submodule add https://github.com/USER/repo.git .claude-context
   ```

#### Setup Script Fails
**Problem**: `./setup.sh` returns errors

**Solutions**:
1. Check permissions:
   ```bash
   chmod +x setup.sh
   chmod +x .submodule/*.sh
   ```
2. Verify bash is available:
   ```bash
   which bash
   ```
3. Run with debug mode:
   ```bash
   bash -x setup.sh
   ```

### Mode Detection Issues

#### Wrong Mode Detected
**Problem**: Commands operate in wrong mode

**Diagnosis**:
```bash
source .submodule/detect_mode.sh
echo "Mode: $CLAUDE_MODE"
echo "Root: $CLAUDE_ROOT"
echo "Scope: $CLAUDE_SCOPE"
```

**Solutions**:
1. Check transformation marker:
   ```bash
   ls -la .transformation/active
   ```
2. Clear overrides:
   ```bash
   unset CLAUDE_MODE_OVERRIDE
   ```
3. Force correct mode:
   ```bash
   # For framework mode
   rm -f .transformation/active
   
   # For transformation mode
   touch .transformation/active
   ```

#### Environment Variables Not Set
**Problem**: Commands fail with undefined variables

**Solution**:
Always source detect_mode.sh:
```bash
source .claude-context/.submodule/detect_mode.sh
```

### Command Execution Issues

#### Command Not Found
**Problem**: Slash commands not recognized

**Solutions**:
1. Verify command exists:
   ```bash
   ls .claude/framework/commands/*/*.md
   ```
2. Check command naming:
   - Must end with `.md`
   - Must have valid YAML frontmatter
3. Restart Claude Code session

#### Tools Not Available
**Problem**: "Tool not available" errors

**Solution**:
Check allowed-tools in command:
```yaml
---
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob]
---
```

#### Working Directory Issues
**Problem**: Commands operate in wrong directory

**Solution**:
Use CLAUDE_SCOPE:
```bash
cd "$CLAUDE_SCOPE"
```

### Integration Issues

#### Parent Project Not Found
**Problem**: Framework can't find parent project

**Solutions**:
1. Check directory structure:
   ```bash
   pwd
   ls ../..
   ```
2. Verify submodule location:
   ```bash
   git submodule status
   ```
3. Manual override:
   ```bash
   export CLAUDE_ROOT=/path/to/submodule
   export CLAUDE_SCOPE=/path/to/parent
   ```

#### Context Not Loading
**Problem**: Context files not being used

**Solutions**:
1. Check context directory:
   ```bash
   ls "$CLAUDE_CONTEXT_DIR"
   ```
2. Verify file permissions:
   ```bash
   find .claude -name "*.md" -not -readable
   ```
3. Check CLAUDE.md location:
   ```bash
   ls CLAUDE.md .claude/CLAUDE.md
   ```

### Validation Failures

#### VERIFY Protocol Errors
**Problem**: Research validation fails

**Solutions**:
1. Check source links are valid
2. Ensure evidence is documented
3. Run research validator:
   ```bash
   /3_invoke_agent research-validator
   ```

#### Context Structure Invalid
**Problem**: Context validation errors

**Solutions**:
1. Use validation command:
   ```bash
   /5_validate_context
   ```
2. Check template compliance
3. Fix identified issues

### Performance Issues

#### Slow Command Execution
**Problem**: Commands take too long

**Solutions**:
1. Reduce context size
2. Use file hop patterns
3. Clear unnecessary context:
   ```bash
   # Archive old context
   mv .claude/context/old-*.md .claude/context/archive/
   ```

#### Memory/Token Limits
**Problem**: Context window exceeded

**Solutions**:
1. Split large contexts
2. Use hierarchical organization
3. Implement rotation strategy

### Team Collaboration Issues

#### Merge Conflicts in CLAUDE.md
**Problem**: Git conflicts in shared context

**Solutions**:
1. Use sections for different team members
2. Regular sync meetings
3. Automated merge strategy:
   ```bash
   git config merge.tool vimdiff
   ```

#### Inconsistent Context
**Problem**: Team members have different contexts

**Solutions**:
1. Regular context reviews
2. Shared validation:
   ```bash
   /6_team_sync
   ```
3. Version control discipline

### Agent Issues

#### Agent Not Responding
**Problem**: Agent invocation fails

**Solutions**:
1. Check agent file exists
2. Verify agent format
3. Use correct invocation:
   ```bash
   /3_invoke_agent agent-name
   ```

#### Wrong Agent Behavior
**Problem**: Agent does unexpected things

**Solutions**:
1. Check specialization match
2. Review agent prompt
3. Use appropriate agent for task

### Recovery Procedures

#### Restore from Backup
```bash
# Find backups
ls -la .backup_*

# Restore specific backup
cp -r .backup_20240115_120000/.claude .
```

#### Reset to Clean State
```bash
# WARNING: Backs up then resets
./.transformation/commands/backup_existing.sh
rm -rf .transformation/
rm -f .claude/framework/
git submodule update --init
```

#### Emergency Mode Override
```bash
# Force specific mode for recovery
export CLAUDE_MODE_OVERRIDE=framework
# Do recovery work
unset CLAUDE_MODE_OVERRIDE
```

## Getting Help

### Diagnostic Information
When reporting issues, include:

```bash
# Run diagnostic script
cat << 'EOF' > diagnose.sh
#!/bin/bash
echo "=== Diagnostic Information ==="
echo "Date: $(date)"
echo "PWD: $(pwd)"
echo "Git Root: $(git rev-parse --show-toplevel 2>/dev/null || echo 'Not in git')"
echo
source .submodule/detect_mode.sh 2>/dev/null
echo "CLAUDE_MODE: $CLAUDE_MODE"
echo "CLAUDE_ROOT: $CLAUDE_ROOT"
echo "CLAUDE_SCOPE: $CLAUDE_SCOPE"
echo "CLAUDE_CONTEXT_DIR: $CLAUDE_CONTEXT_DIR"
echo
echo "Directory Structure:"
find . -type d -name ".claude*" -o -name ".transformation" -o -name ".submodule" | head -20
echo
echo "Key Files:"
ls -la .transformation/active 2>/dev/null || echo ".transformation/active: Not found"
ls -la .submodule/detect_mode.sh 2>/dev/null || echo "detect_mode.sh: Not found"
EOF

bash diagnose.sh
```

### Support Resources

1. Check documentation:
   - `MODE_DETECTION.md`
   - `DEVELOPER_GUIDE.md`
   - Framework README files

2. Run tests:
   ```bash
   ./.transformation/tests/test_mode_detection.sh
   ./.transformation/tests/test_integration.sh
   ```

3. Review anti-patterns:
   - `.claude/context/antipatterns/`

Remember: Most issues stem from mode detection or missing environment setup. Always start troubleshooting there.