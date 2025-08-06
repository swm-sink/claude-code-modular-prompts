# Parallel Agent Context Template

## Agent Identity
**Agent ID**: [UNIQUE_IDENTIFIER]
**Agent Type**: [Builder|Updater|Archiver|Cleaner]
**Assigned Tasks**: [TASK_NUMBERS]
**Execution Mode**: [parallel|sequential|mixed]

## Critical Context
### Current State
- **Session Status**: [From claude.local.md]
- **Completed Tasks**: [LIST]
- **In-Progress Tasks**: [LIST]
- **Blocked Tasks**: [LIST]

### Task Specifications
```yaml
assigned_tasks:
  - task_number: [N]
    description: [EXACT_DESCRIPTION]
    dependencies: [TASK_NUMBERS]
    conflicts: [FILE_PATHS]
    risk_level: [low|medium|high]
    validation_required: [true|false]
```

## Execution Constraints
### Resource Locks
- **Files to Modify**: [EXCLUSIVE_LIST]
- **Directories to Create**: [EXCLUSIVE_LIST]
- **Shared Resources**: [READ_ONLY_LIST]

### Coordination Protocol
```yaml
claim_protocol:
  - Check claude.local.md for task status
  - Claim task with atomic update
  - Verify no other agent claimed
  - Proceed or back off

progress_protocol:
  - Update status every 5 minutes
  - Report completion immediately
  - Log failures with details
  - Update claude.local.md atomically
```

## Safety Rules
1. **Never modify files claimed by another agent**
2. **Always validate task completion before marking done**
3. **On conflict, back off and retry**
4. **On failure, rollback and report**
5. **Never proceed without successful claim**

## Communication Patterns
### Success Report
```yaml
task: [NUMBER]
status: complete
evidence: [TEST_RESULTS]
commit: [HASH]
next: [READY_TASKS]
```

### Failure Report
```yaml
task: [NUMBER]
status: failed
error: [DETAILS]
rollback: [COMPLETED]
blocked: [DEPENDENT_TASKS]
```

## Quality Standards
- **TDD Requirement**: [full|lightweight|none]
- **Validation Type**: [comprehensive|basic|trust]
- **Commit Pattern**: [atomic|batch]
- **Documentation**: [required|optional]