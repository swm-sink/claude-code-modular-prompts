# Deprecated Commands Audit

## Decision: Promote to Main Library with Placeholders

These commands provide high value and should be moved to appropriate categories with placeholder integration:

### Database Operations (→ .claude/commands/database/)
- **db-migrate.md** → Essential for [INSERT_DATABASE_TYPE] migrations
- **db-backup.md** → Critical for [INSERT_PROJECT_NAME] data safety
- **db-restore.md** → Recovery operations for [INSERT_DATABASE_TYPE]
- **db-seed.md** → Test data for [INSERT_TESTING_FRAMEWORK]

### Deployment & CI/CD (→ .claude/commands/devops/)
- **deploy.md** → Deploy [INSERT_PROJECT_NAME] to [INSERT_DEPLOYMENT_TARGET]
- **ci-setup.md** → Configure [INSERT_CI_CD_PLATFORM] pipelines
- **ci-run.md** → Execute [INSERT_CI_CD_PLATFORM] workflows
- **cd-rollback.md** → Rollback [INSERT_PROJECT_NAME] deployments

### Security (→ .claude/commands/security/)
- **secure-scan.md** → Security scanning for [INSERT_SECURITY_LEVEL]
- **secure-audit.md** → Audit [INSERT_PROJECT_NAME] security

### Testing (→ .claude/commands/testing/)
- **test-unit.md** → Unit tests with [INSERT_TESTING_FRAMEWORK]
- **test-integration.md** → Integration tests for [INSERT_API_STYLE] APIs

### Development Environment (→ .claude/commands/development/)
- **dev-setup.md** → Setup [INSERT_TECH_STACK] development
- **env-setup.md** → Configure [INSERT_PROJECT_NAME] environments

### Monitoring (→ .claude/commands/monitoring/)
- **monitor-setup.md** → Setup monitoring for [INSERT_DEPLOYMENT_TARGET]
- **monitor-alerts.md** → Configure alerts for [INSERT_PROJECT_NAME]

## Decision: Delete (Low Value/Redundant)

These commands are too generic, unclear, or already replaced:

### Vague/Unclear Purpose
- **existing.md** - Unclear name, replaced by /dev analyze
- **new.md** - Too generic
- **workflow.md** - Too broad, no clear purpose
- **quality-suggest.md** - Vague functionality

### Already Replaced/Redundant
- **pipeline-legacy.md** - Legacy = not needed
- **analyze.md** - Too generic, have specific analyze commands
- **security.md** - Too broad, have specific security commands
- **progress-tracker.md** - Redundant with TodoWrite

### Low Value Generic Commands
- **code-format.md** - Too language-specific, let users add
- **code-lint.md** - Too language-specific
- **deps-update.md** - Too framework-specific
- **cost-analyze.md** - Too niche

### Overly Complex/Specific
- **flow-schedule.md** - Too specific workflow
- **quality-metrics.md** - Too abstract
- **quality-report.md** - Redundant with other reporting
- **test-report.md** - Redundant with test commands

## Implementation Plan

1. **Move high-value commands** to main library with placeholders
2. **Delete low-value commands** entirely
3. **Update command references** in other files
4. **Validate no broken dependencies**

Total: 
- **18 commands to promote** with placeholders
- **20 commands to delete** as low value

This reduces deprecated from 42 to 0, adding 18 valuable commands to main library.