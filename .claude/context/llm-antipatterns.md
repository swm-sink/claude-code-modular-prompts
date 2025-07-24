# LLM Anti-Patterns - Lessons Learned

## What NOT to do

### 1. Documentation Explosion
- ❌ Creating multiple README files (found 34!)
- ❌ Meta-documentation about documentation
- ❌ Excessive planning documents
- ❌ 341 markdown files for a command library
- ✅ One README per major component maximum

### 2. Directory Chaos
- ❌ Nesting directories 5+ levels deep
- ❌ Creating .main, .backup, .archive copies
- ❌ Moving files without actual cleanup (tallinn → .main)
- ❌ Duplicate command structures in multiple places
- ✅ Maximum 3-level nesting, period

### 3. Command Proliferation
- ❌ 171 commands that overlap
- ❌ Commands without clear purpose
- ❌ Untested command implementations
- ❌ Multiple versions of same functionality
- ✅ 50 curated, tested, purposeful commands

### 4. Over-Engineering
- ❌ Complex agent hierarchies without implementation
- ❌ Excessive categorization and taxonomy
- ❌ Planning instead of doing
- ❌ 20+ component subdirectories
- ✅ Simple, working solutions first

### 5. Promise vs Reality Gap
- ❌ Documentation promises vs actual implementation
- ❌ "90% test coverage" with 0% actual tests
- ❌ "50-70 commands" with 171 actual files
- ❌ TDD rhetoric without TDD practice
- ✅ Match documentation to reality

## Root Cause: LLM Verbose Generation Syndrome

LLMs tend to:
- Generate excessive documentation instead of code
- Create complex structures without implementation
- Make promises in documentation without execution
- Confuse planning with doing

## Prevention Strategy

1. **Enforce atomic commits** - One task, one commit
2. **Reality checks** - Verify claims with actual metrics
3. **Simplicity first** - Start minimal, expand if needed
4. **Implementation focus** - Code before documentation
5. **Regular cleanup** - Don't let chaos accumulate