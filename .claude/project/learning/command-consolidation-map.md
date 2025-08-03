# Command Consolidation Map

**Date**: 2025-07-25
**Current State**: 67 commands
**Target State**: 40 commands
**Reduction**: 27 commands (40%)

## Consolidation Strategy

### 1. Testing Commands (6 → 2)

**Consolidate into `/test`:**
- `test-unit.md` → Primary base
- `test-integration.md` → Merge features
- `test-coverage.md` → Merge coverage
- `test-report.md` → Merge reporting
- `dev-test.md` → Merge dev features

**Keep specialized:** 
- `test-e2e.md` → Unique browser automation needs

**Key features to preserve:**
- All test types (unit, integration, e2e) 
- Coverage analysis with configurable thresholds
- Multi-environment support
- Comprehensive reporting

### 2. Security Commands (6 → 2)

**Consolidate into `/security`:**
- `secure-audit.md` → Primary base
- `secure-scan.md` → Merge scanning
- `secure-config.md` → Merge config validation
- `secure-report.md` → Merge reporting
- `security.md` → Redundant with secure-audit

**Keep specialized:**
- `secure-fix.md` → Automated remediation needs separate handling

**Key features to preserve:**
- OWASP compliance checking
- Vulnerability scanning
- Configuration hardening
- Compliance reporting

### 3. Quality Commands (5 → 2)

**Consolidate into `/quality`:**
- `quality-review.md` → Primary base
- `quality-metrics.md` → Merge metrics
- `quality-report.md` → Merge reporting
- `quality-suggest.md` → Merge suggestions

**Keep specialized:**
- `quality-enforce.md` → Quality gates need separate enforcement

**Key features to preserve:**
- Automated code review
- Quality metrics collection
- Improvement suggestions
- Standards compliance

### 4. Pipeline Commands (3 → 1)

**Consolidate into `/pipeline`:**
- `pipeline.md` → Primary base
- `pipeline-create.md` → Merge creation
- `pipeline-run.md` → Merge execution

**Key features to preserve:**
- Pipeline definition and creation
- Real-time execution monitoring
- Stage orchestration
- Error recovery

### 5. Analysis Commands (4 → 2)

**Enhance existing `/analyze`:**
- Add dependency analysis from `analyze-dependencies.md`
- Add pattern detection from `analyze-patterns.md`

**Keep specialized:**
- `analyze-performance.md` → Performance needs dedicated tooling

**Key features to preserve:**
- Dependency vulnerability scanning
- Design pattern detection
- Anti-pattern identification

### 6. Monitor Commands (3 → 1)

**Consolidate into `/monitor`:**
- `monitor-setup.md` → Primary base
- `monitor-dashboard.md` → Merge dashboard
- `monitor-alerts.md` → Merge alerting

**Key features to preserve:**
- Complete monitoring setup
- Dashboard customization
- Alert correlation
- Predictive analytics

### 7. Database Commands (4 → 2)

**Consolidate into `/database`:**
- `db-migrate.md` → Primary base
- `db-restore.md` → Merge restoration
- `db-seed.md` → Merge seeding

**Keep specialized:**
- `db-backup.md` → Backup needs separate scheduling

**Key features to preserve:**
- Migration with rollback
- Backup/restore operations
- Database seeding
- Integrity validation

### 8. DAG Commands (2 → 1)

**Consolidate into `/dag`:**
- `dag-orchestrate.md` → Primary base
- `dag-executor.md` → Merge execution

**Key features to preserve:**
- Dependency resolution
- Parallel processing
- Dynamic agent spawning
- Adaptive execution

## Merge Strategy for Each Consolidation

### Phase 1: Test Consolidation Example

```markdown
# /test command structure after consolidation

## Unified Interface
/test [type] [options]
  - type: unit|integration|e2e|all (default: all)
  - options: --coverage, --report, --parallel, --env

## Preserved Capabilities
- Unit testing with mocking
- Integration testing with containers
- Coverage thresholds and reporting
- Multi-format output (JSON, HTML, JUnit)
- Parallel execution
- Environment-specific configs
```

### Implementation Order

1. **Week 1**: Test and Security consolidation (highest overlap)
2. **Week 2**: Quality and Pipeline consolidation
3. **Week 3**: Analysis and Monitor consolidation  
4. **Week 4**: Database and DAG consolidation

## Deprecation Strategy

For each deprecated command:
1. Add deprecation notice to old command
2. Redirect to new consolidated command
3. Log usage to track migration
4. Remove after 30-day grace period

## Success Metrics

- Command count: 67 → 40 ✓
- Feature preservation: 100%
- User migration: Track via usage logs
- Performance: No degradation
- Documentation: Updated for all consolidations