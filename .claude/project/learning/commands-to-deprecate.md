# Commands to Deprecate

**Date**: 2025-07-25
**Total Commands to Deprecate**: 27

## Deprecation List with Rationale

### Testing Commands (4 deprecations)

1. **`test-integration.md`**
   - **Rationale**: Functionality merged into `/test` command
   - **Migration**: Use `/test integration` or `/test --type=integration`

2. **`test-coverage.md`**
   - **Rationale**: Coverage is standard feature of `/test`
   - **Migration**: Use `/test --coverage`

3. **`test-report.md`**
   - **Rationale**: Reporting integrated into `/test`
   - **Migration**: Use `/test --report=html`

4. **`dev-test.md`**
   - **Rationale**: Redundant with enhanced `/test` command
   - **Migration**: Use `/test` with development options

### Security Commands (4 deprecations)

5. **`secure-scan.md`**
   - **Rationale**: Scanning integrated into `/security`
   - **Migration**: Use `/security scan` or `/security --scan`

6. **`secure-config.md`**
   - **Rationale**: Configuration validation part of `/security`
   - **Migration**: Use `/security config` or `/security --validate-config`

7. **`secure-report.md`**
   - **Rationale**: Reporting integrated into `/security`
   - **Migration**: Use `/security --report`

8. **`security.md`**
   - **Rationale**: Duplicate of secure-audit functionality
   - **Migration**: Use `/security` (consolidated command)

### Quality Commands (3 deprecations)

9. **`quality-metrics.md`**
   - **Rationale**: Metrics collection integrated into `/quality`
   - **Migration**: Use `/quality --metrics`

10. **`quality-report.md`**
    - **Rationale**: Reporting integrated into `/quality`
    - **Migration**: Use `/quality --report`

11. **`quality-suggest.md`**
    - **Rationale**: Suggestions integrated into `/quality`
    - **Migration**: Use `/quality --suggest`

### Pipeline Commands (2 deprecations)

12. **`pipeline-create.md`**
    - **Rationale**: Creation integrated into `/pipeline`
    - **Migration**: Use `/pipeline create` or `/pipeline --new`

13. **`pipeline-run.md`**
    - **Rationale**: Execution integrated into `/pipeline`
    - **Migration**: Use `/pipeline run` or `/pipeline --execute`

### Analysis Commands (2 deprecations)

14. **`analyze-dependencies.md`**
    - **Rationale**: Dependency analysis integrated into `/analyze`
    - **Migration**: Use `/analyze --dependencies`

15. **`analyze-patterns.md`**
    - **Rationale**: Pattern detection integrated into `/analyze`
    - **Migration**: Use `/analyze --patterns`

### Monitor Commands (2 deprecations)

16. **`monitor-dashboard.md`**
    - **Rationale**: Dashboard management integrated into `/monitor`
    - **Migration**: Use `/monitor dashboard` or `/monitor --dashboard`

17. **`monitor-alerts.md`**
    - **Rationale**: Alert management integrated into `/monitor`
    - **Migration**: Use `/monitor alerts` or `/monitor --alerts`

### Database Commands (2 deprecations)

18. **`db-restore.md`**
    - **Rationale**: Restore functionality integrated into `/database`
    - **Migration**: Use `/database restore`

19. **`db-seed.md`**
    - **Rationale**: Seeding functionality integrated into `/database`
    - **Migration**: Use `/database seed`

### DAG Commands (1 deprecation)

20. **`dag-executor.md`**
    - **Rationale**: Execution integrated into `/dag`
    - **Migration**: Use `/dag execute` or `/dag --run`

### Specialized Commands (7 potential deprecations)

21. **`flow-schedule.md`**
    - **Rationale**: Scheduling better handled by `/pipeline`
    - **Migration**: Use `/pipeline --schedule`

22. **`hierarchical.md`**
    - **Rationale**: Hierarchical processing integrated into orchestration
    - **Migration**: Use `/dag` with hierarchical options

23. **`map-reduce.md`**
    - **Rationale**: Map-reduce pattern integrated into `/dag`
    - **Migration**: Use `/dag --map-reduce`

24. **`mass-transformation.md`**
    - **Rationale**: Mass operations integrated into `/pipeline`
    - **Migration**: Use `/pipeline --batch`

25. **`mutation.md`**
    - **Rationale**: Data mutation integrated into development commands
    - **Migration**: Use appropriate development command

26. **`progress-tracker.md`**
    - **Rationale**: Progress tracking integrated into `/monitor`
    - **Migration**: Use `/monitor --progress`

27. **`protocol.md`**
    - **Rationale**: Protocol definitions integrated into orchestration
    - **Migration**: Use relevant orchestration command

## Deprecation Implementation Plan

### Phase 1: Soft Deprecation (Days 1-7)
1. Add deprecation notices to command files
2. Implement command forwarding to new locations
3. Log usage of deprecated commands

### Phase 2: User Notification (Days 8-21)
1. Display migration warnings on command use
2. Provide migration guides
3. Track migration progress

### Phase 3: Hard Deprecation (Days 22-30)
1. Commands show deprecation error
2. Provide final migration path
3. Prepare for removal

### Phase 4: Removal (Day 31+)
1. Archive deprecated command files
2. Update all documentation
3. Clean up references

## Deprecation Notice Template

```markdown
---
deprecated: true
deprecated_date: 2025-07-25
removal_date: 2025-08-25
migration_path: /test
---

# DEPRECATED: This command has been consolidated

This command has been deprecated and will be removed on 2025-08-25.

**Migration Path**: Use `/test` with the following options:
- For integration testing: `/test integration`
- For coverage reports: `/test --coverage`

**Reason**: Consolidating testing commands to reduce complexity and improve user experience.
```

## Success Criteria

- All deprecated commands have migration paths
- Zero feature loss during consolidation
- User migration completed within 30 days
- Documentation updated for all changes
- No broken workflows after deprecation