# Troubleshooting Guide

## 🔴 Common Problems & Solutions

### "Can't find .claude-architect/ directory"
**Problem**: LS tool returns empty on hidden directories  
**Solution**: 
```bash
# DON'T use: LS .claude-architect
# DO use: ls -la .claude-architect/
```

### "Phase 5 complete but nothing works"
**Problem**: Status tracking vs reality mismatch  
**Root Cause**: YAML files created ≠ functionality working  
**Solution**: 
1. Check actual functionality: `/deep-discovery start`
2. Update status based on what works, not what exists
3. Read `PROJECT-STATE-VERIFICATION.md` for real status

### "Should I create new implementation?"
**Decision Tree**:
```
Need feature X?
├── Check if backend has it: ls .claude-architect/*/
├── Found it?
│   ├── YES → Wire command to use it
│   └── NO → Check again (probably missed it)
└── Really not there?
    └── Ask user before creating
```

### "Integration path unclear"
**Problem**: Don't know how to connect frontend to backend  
**Solution Pattern**:
```markdown
# In frontend command (.claude/commands/X.md):
1. Read backend config:
   config = Read('.claude-architect/[module]/[file].yaml')
   
2. Execute backend logic:
   [Apply the patterns/templates/flows from backend]
   
3. Save to backend:
   Write('.claude-architect/results/[output]')
```

### "91 files in root directory"
**Problem**: Documentation debt  
**Solution**: 
- DON'T create new plans
- DO update existing: PROJECT-STATE-VERIFICATION.md
- Archive old: `mkdir .archive && mv *PLAN*.md .archive/`

### "YAML files don't do anything"
**Understanding**: YAML = data, not programs
```yaml
# This DOESN'T execute:
pipeline:
  - analyze
  - generate
  
# Commands must READ it and DO the work
```

## 🔍 Diagnostic Commands

### Check Integration Level
```bash
# How many commands reference backend?
grep -l "claude-architect" .claude/commands/*.md | wc -l

# Which ones are integrated?
grep -l "claude-architect" .claude/commands/*.md

# What backend components exist?
ls -la .claude-architect/
```

### Verify Functionality
```bash
# Test discovery
/discover-project --dry-run
# Check: Does it reference backend?

# Test generation  
/generate-commands --dry-run
# Check: Does it use templates?

# Test orchestration
/deep-discovery status
# Check: Does it show real state?
```

## 🆘 When All Else Fails

### Emergency Reset
1. **Save current state**: `cp -r .claude .claude.backup-$(date +%Y%m%d)`
2. **Read reality check**: `cat PROJECT-STATE-VERIFICATION.md`
3. **Pick ONE thing**: Make `/discover-project` work end-to-end
4. **Test it works**: Actually run it
5. **Then continue**: One working feature at a time

### Still Stuck?
**Create minimal test**:
```bash
# Pick simplest possible integration:
echo "Can /discover-project read .claude-architect/research/?" 
# Make just that work
# Build from there
```

## 🚫 Anti-Debugging Patterns

**DON'T**:
- Add more YAML configuration
- Create another plan
- Build parallel implementation
- Claim it's fixed without testing

**DO**:
- Test actual functionality
- Wire existing components
- Fix one thing completely
- Verify before proceeding

---
*Load this only when debugging - not part of standard context*