# Phase 2 Implementation Plan - Optimal Approach

## Executive Summary
This plan addresses 4 critical objectives with minimal iteration risk through careful pre-validation and batch operations.

## Pre-Implementation Validation ✅

### Files Confirmed to Exist
- [x] `.claude/commands/coordinate-agents.md` - Contains 6 references to `/integrate-agents`
- [x] `.claude/commands/manage-session-state.md` - Contains 1 reference to `/integrate-agents`
- [x] `CLAUDE.md` - Needs updates per tasks 16-19
- [x] `README.md` - Needs generation approach alignment
- [x] `claude.todos.yaml` - Master task list

### Current State Analysis
- **Phase 2 Progress**: 4/13 tasks complete (Tasks 12-15)
- **Remaining Tasks**: 16-24 (9 tasks)
- **Documentation Files in Root**: 73 files needing organization
- **Stale References**: 7 total across 2 command files

## Implementation Strategy

### Batch Operation Groups

#### Group A: CLAUDE.md Updates (Tasks 16-19) - CRITICAL
**Strategy**: Single multi-edit operation to avoid context window issues
**Risk Level**: High (requires approval)

```yaml
edits:
  task_16_warning:
    location: "After GENERATIVE VISION section"
    content: "Add explicit warning against integration approach"
    
  task_17_what_provides:
    location: "Lines 766-777 (What This Library Provides)"
    change: "Update to reflect Deep Discovery Generation"
    
  task_18_current_status:
    location: "Lines 987-1003"
    change: "Fix to show transformation progress"
    
  task_19_xml_metadata:
    location: "Lines 149-245"
    change: "Update project_type to deep_discovery_generation_engine"
```

#### Group B: New Documentation Files (Tasks 20-22) - PARALLEL
**Strategy**: Create simultaneously as independent files
**Risk Level**: Low

```yaml
files_to_create:
  - DEEP-DISCOVERY-ARCHITECTURE.md
  - PROJECT-DNA-SPECIFICATION.md  
  - GENERATION-NOT-INTEGRATION.md
```

#### Group C: Command Fixes - IMMEDIATE
**Strategy**: Fix stale references before continuing
**Risk Level**: Low

```yaml
fixes:
  coordinate-agents.md:
    - Remove lines 58-67 (integrate-agents references)
    - Update integration architecture section
    
  manage-session-state.md:
    - Update line 60 to remove integrate-agents reference
```

#### Group D: Documentation Organization - CLEANUP
**Strategy**: Move files to appropriate subdirectories
**Risk Level**: Low

```yaml
organization:
  docs/planning/:
    - All *-PLAN.md files
    - All *-STRATEGY.md files
    
  docs/reports/:
    - All *-REPORT.md files
    - All *-SUMMARY.md files
    
  docs/guides/:
    - All *-GUIDE.md files
    - All installation/setup files
    
  archive/:
    - Obsolete transformation artifacts
```

#### Group E: README Update (Task 23) - PUBLIC FACING
**Strategy**: Comprehensive rewrite for generation approach
**Risk Level**: Medium

## Execution Sequence

### Phase 1: Fix Breaking Issues (15 min)
1. Fix stale references in command files (Group C)
2. Commit: "Fix: Remove stale integration references from commands"

### Phase 2: Core Updates (30 min)
3. Batch update CLAUDE.md (Group A - Tasks 16-19)
4. Commit: "Tasks #16-19: Update CLAUDE.md for Deep Discovery Generation"

### Phase 3: Create New Docs (20 min)
5. Parallel create 3 new documentation files (Group B - Tasks 20-22)
6. Commit: "Tasks #20-22: Add Deep Discovery documentation"

### Phase 4: Public Update (15 min)
7. Update README.md (Group E - Task 23)
8. Commit: "Task #23: Update README for Deep Discovery approach"

### Phase 5: Cleanup (20 min)
9. Archive claude.local.md (Task 24)
10. Organize documentation (Group D)
11. Commit: "Task #24 + Cleanup: Archive and organize documentation"

## Risk Mitigation

### Context Window Management
- Use MultiEdit for CLAUDE.md changes
- Read only necessary sections, not entire file
- Batch related changes together

### Validation Checkpoints
- After each group, validate changes
- Run grep to confirm no stale references remain
- Check file moves don't break references

### Rollback Strategy
- Each phase is atomic with its own commit
- Can revert any phase independently
- Backup CLAUDE.md before major edits

## Success Criteria

### Must Have
- [ ] All `/integrate-agents` references removed
- [ ] CLAUDE.md reflects Deep Discovery Generation
- [ ] README accurately describes the project
- [ ] Phase 2 tasks 16-24 complete

### Should Have
- [ ] Documentation organized into subdirectories
- [ ] Root directory cleaned up
- [ ] Clear navigation structure

### Nice to Have
- [ ] Updated XML metadata throughout
- [ ] Consistent terminology across all docs
- [ ] Removed obsolete files

## Communication Plan

### Progress Updates
- Update TodoWrite after each phase
- Update claude.todos.yaml task status
- Clear commit messages with task references

### Validation Reports
- Generate report after each group
- Final comprehensive validation report
- Sign-off checklist at completion

## Time Estimate
- **Total**: 100 minutes (1 hour 40 minutes)
- **Buffer**: 20 minutes for validation
- **Grand Total**: 2 hours

## Pre-Flight Checklist
- [x] All target files exist and are accessible
- [x] Understand all task requirements
- [x] Have rollback strategy
- [x] Know success criteria
- [x] Communication plan clear

Ready to execute with minimal iteration risk.