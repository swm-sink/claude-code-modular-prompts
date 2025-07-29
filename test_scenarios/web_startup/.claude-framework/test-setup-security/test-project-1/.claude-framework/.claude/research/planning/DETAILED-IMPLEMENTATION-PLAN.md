# Detailed Implementation Plan

## Overview
Step-by-step implementation guide with specific commands, file edits, and validation checkpoints.

## Track A: Documentation Accuracy (30 minutes)

### A1.1: Verify Current Command Counts
**Command**: 
```bash
find .claude/commands -name "*.md" | wc -l
find .claude/commands -path "*/deprecated/*" -name "*.md" | wc -l
find .claude/commands -name "*.md" ! -path "*/deprecated/*" | wc -l
```

**Expected**: 79 total, 49 deprecated, 30 active
**Action**: Record exact numbers for documentation

### A1.2: Update CLAUDE.md Line 34
**File**: `/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca/CLAUDE.md`
**Current Line 34**: `| Commands | 67 | 67 unique | ✅ No duplicates found |`
**New Line 34**: `| Commands | 79 total (30 active) | 79 unique | ✅ No duplicates found |`

**Implementation**:
```bash
# Read current line
grep -n "Commands.*67" CLAUDE.md

# Make edit using Edit tool
Edit CLAUDE.md "| Commands | 67 | 67 unique | ✅ No duplicates found |" "| Commands | 79 total (30 active) | 79 unique | ✅ No duplicates found |"
```

### A1.3: Update CLAUDE.md Line 9
**Current Line 9**: `│   ├── commands/     # 67 commands (all unique, no duplicates)`
**New Line 9**: `│   ├── commands/     # 79 commands: 30 active + 49 deprecated`

### A1.4: Update README.md Command Counts
**File**: `/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca/README.md`
**Updates Needed**:
- Line 7: "67 commands" → "79 commands (30 active)"
- Line 28: "34 Active Commands" → "30 Active Commands" 
- Line 30: "49 Archived Commands" → "49 Deprecated Commands"

### A1.5: Validation Checkpoint
**Command**: 
```bash
grep -n "67\|34 Active" CLAUDE.md README.md
```
**Success**: Should return no matches

## Track B: File Organization (35 minutes)

### B1.1: Create Planning Directory
**Command**:
```bash
mkdir -p .claude/research/planning
```

### B1.2: Move TEMP Files
**Files to Move**:
- `TEMP-claude-code-research-detailed-plan.md`
- `TEMP-claude-code-research-plan-outline.md`
- `TEMP-research-plan-critique.md`
- `TEMP-research-todo-list.md`

**Commands**:
```bash
mv TEMP-*.md .claude/research/planning/
ls -la TEMP-* || echo "No TEMP files remaining"
```

### B1.3: Update .gitignore if Needed
**Check**: 
```bash
cat .gitignore | grep -i temp
```
**Action**: Add `TEMP-*.md` if not already present

### B1.4: Commit Research Directory
**Commands**:
```bash
git add .claude/research/
git status
git commit -m "feat: add comprehensive Claude Code research collection

- 15 verified sources documented
- 5 pattern categories identified
- Best practices and anti-patterns compiled
- Examples and synthesis documents created"
```

### B1.5: Validation Checkpoint
**Commands**:
```bash
ls -la | grep TEMP || echo "Root directory clean"
git status | grep "research" || echo "Research committed"
```

## Track C: Testing Methodology (2-4 hours)

### C1.1: Define Testing Scope
**Deliverable**: Document what constitutes a "test" for .md command files

**Research Questions**:
1. What makes a command "functional"?
2. How can we validate command structure?
3. What are the critical failure modes?

**Approach**:
```markdown
# Command Testing Methodology

## Test Categories
1. **Structural Tests**: YAML front matter valid
2. **Content Tests**: Required sections present
3. **Syntax Tests**: Markdown properly formatted
4. **Reference Tests**: Components/tools referenced exist

## Test Tools Evaluation
- PromptFoo: Designed for prompt testing
- Custom validation: Simple shell/python scripts
- Manual review: Structured checklist approach
```

### C1.2: Create Simple Validation Script
**File**: `tests/validate-command.sh`
**Content**:
```bash
#!/bin/bash
# Simple command validation script

validate_command() {
    local file="$1"
    echo "Validating: $file"
    
    # Check YAML front matter
    if ! head -n 10 "$file" | grep -q "^---$"; then
        echo "❌ Missing YAML front matter"
        return 1
    fi
    
    # Check required fields
    if ! grep -q "^name:" "$file"; then
        echo "❌ Missing name field"
        return 1
    fi
    
    echo "✅ Basic validation passed"
    return 0
}

# Test if file provided
if [ "$1" ]; then
    validate_command "$1"
else
    echo "Usage: $0 <command-file.md>"
fi
```

### C1.3: Test Validation on Sample Commands
**Commands**:
```bash
chmod +x tests/validate-command.sh
./tests/validate-command.sh .claude/commands/core/task.md
./tests/validate-command.sh .claude/commands/core/query.md
./tests/validate-command.sh .claude/commands/core/auto.md
```

### C1.4: Document Testing Approach
**File**: `tests/README.md`
**Content**: Description of testing methodology and validation results

### C1.5: Update CLAUDE.md with Testing Info
**Addition to CLAUDE.md**:
```markdown
## Testing Strategy
- Structural validation: YAML front matter and required fields
- Content validation: Required sections present
- Manual review: Functionality and examples
- Current coverage: 5 core commands validated
```

## Sequential Integration Phase (2 hours)

### I1: Documentation Consolidation
**Objective**: Ensure all project metrics are consistent

**Steps**:
1. **Cross-Reference Check**:
```bash
grep -r "67\|34 active\|commands" CLAUDE.md README.md .claude/research/README.md
```

2. **Create Metrics Summary**:
```markdown
# Project Metrics Summary
- Total command files: 79
- Active commands: 30
- Deprecated commands: 49
- Components: 63
- Context files: 7
- Test coverage: Basic validation for 5 commands
```

3. **Update All References**:
- CLAUDE.md: Status table
- README.md: Quick start section
- Research README: If applicable

### I2: Quality Review
**Anti-Pattern Check**:
```bash
# Check for theatrical language
grep -ri "amazing\|incredible\|revolutionary\|exceptional" CLAUDE.md README.md

# Check for fabricated metrics
grep -ri "[0-9]\+\.[0-9]\+%" CLAUDE.md README.md

# Check for unsubstantiated claims
grep -ri "guarantee\|proven\|definitely" CLAUDE.md README.md
```

**Success**: No matches found

### I3: Final Commit Strategy
**Commit Sequence**:
1. Documentation fixes (Track A)
2. File organization (Track B) 
3. Testing framework (Track C)
4. Integration changes

**Commands**:
```bash
# Documentation fixes
git add CLAUDE.md README.md
git commit -m "docs: correct command counts and project metrics"

# File organization  
git add .
git commit -m "chore: organize TEMP files and clean project structure"

# Testing framework (if implemented)
git add tests/
git commit -m "feat: add basic command validation framework"

# Final integration
git add .
git commit -m "feat: complete project finalization

- Accurate documentation (79 total, 30 active commands)
- Clean file organization
- Basic testing validation
- Anti-pattern compliance verified"
```

## Implementation Timeline

### Day 1 Morning (2 hours)
- [ ] Track A: Documentation fixes (30 min)
- [ ] Track B: File organization (35 min)
- [ ] Track C1: Testing research (45 min)
- [ ] Checkpoint: Quick wins completed

### Day 1 Afternoon (2-3 hours)
- [ ] Track C2-C4: Testing implementation (2-3 hours)
- [ ] Checkpoint: Testing approach defined

### Day 2 Morning (1-2 hours)
- [ ] Integration Phase (2 hours)
- [ ] Final quality review
- [ ] Commit strategy execution

## Success Validation

### Essential Checkpoints
1. **Documentation**: `grep "67\|34 active" CLAUDE.md README.md` returns no matches
2. **File Organization**: `ls TEMP-*` returns "No such file or directory"
3. **Git State**: `git status` shows clean working directory
4. **Anti-Patterns**: Quality review passes all checks

### Completion Criteria
- [ ] All command counts accurate
- [ ] Root directory clean
- [ ] Research work committed
- [ ] Testing approach documented
- [ ] Clean git history
- [ ] Anti-pattern guidelines followed

## Contingency Plans

### If Testing Framework Fails
**Fallback**: Document that testing requires manual review
**Action**: Create structured review checklist instead
**Time**: 30 minutes to document approach

### If Documentation Changes Create Conflicts
**Fallback**: Single source of truth in CLAUDE.md
**Action**: Reference CLAUDE.md from other files
**Time**: 15 minutes to implement references

### If Time Runs Short
**Priority Order**:
1. Track A (essential)
2. Track B (essential)  
3. Integration documentation (essential)
4. Track C (optional)

---
*Detailed Plan Date: 2025-07-27*
*Total Estimated Time: 4-7 hours*
*Critical Path: 3 hours*