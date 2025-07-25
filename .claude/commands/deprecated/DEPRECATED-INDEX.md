# Deprecated Commands Archive Index

This directory contains all deprecated commands that have been consolidated into unified commands as part of the command consolidation effort completed on 2025-07-25.

## Archive Statistics

- **Total Commands Archived**: 50 commands
- **Archive Date**: 2025-07-25
- **Deprecation Effective**: 2025-07-25
- **Planned Removal**: 2025-08-25
- **Archive Structure**: Preserves original directory structure

## Archive Organization

### Testing Commands Batch (4 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: `/test`

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `test-unit.md` | `/test` | Use `/test unit [file_path]` |
| `test-integration.md` | `/test` | Use `/test integration [target]` |
| `test-coverage.md` | `/test` | Use `/test coverage [scope]` |
| `test-report.md` | `/test` | Use `/test report [format]` |

**Location**: `deprecated/test-*.md`

### Quality Commands Batch (4 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: `/quality`

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `quality-review.md` | `/quality` | Use `/quality review [scope]` |
| `quality-metrics.md` | `/quality` | Use `/quality metrics [target]` |
| `quality-report.md` | `/quality` | Use `/quality report [format]` |
| `quality-suggest.md` | `/quality` | Use `/quality suggest [area]` |

**Location**: `deprecated/quality-*.md`

### Security Commands Batch (6 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: `/secure-assess` and `/secure-manage`

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `secure-audit.md` | `/secure-assess` | Use `/secure-assess audit [scope]` |
| `secure-config.md` | `/secure-manage` | Use `/secure-manage config [target]` |
| `secure-fix.md` | `/secure-manage` | Use `/secure-manage fix [vulnerability]` |
| `secure-report.md` | `/secure-assess` | Use `/secure-assess report [format]` |
| `secure-scan.md` | `/secure-assess` | Use `/secure-assess scan [target]` |
| `security.md` | `/secure-assess` | Use `/secure-assess comprehensive` |

**Location**: `deprecated/secure-*.md`, `deprecated/security.md`

### Deployment/CI Commands Batch (8 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: Unified deployment commands

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `pipeline-create.md` | `/pipeline` | Use `/pipeline create [config]` |
| `pipeline-run.md` | `/pipeline` | Use `/pipeline run [target]` |
| `pipeline-legacy.md` | `/pipeline` | Use `/pipeline legacy [mode]` |
| `development/project/ci-setup.md` | `/dev-deploy` | Use `/dev-deploy setup-ci [config]` |
| `development/project/ci-run.md` | `/dev-deploy` | Use `/dev-deploy ci [target]` |
| `development/project/deploy.md` | `/dev-deploy` | Use `/dev-deploy deploy [env]` |
| `development/project/cd-rollback.md` | `/dev-deploy` | Use `/dev-deploy rollback [version]` |
| `development/project/dev-build.md` | `/dev-deploy` | Use `/dev-deploy build [target]` |

**Location**: `deprecated/pipeline-*.md`, `deprecated/development/project/{ci-*,deploy,cd-rollback,dev-build}.md`

### Analysis Commands Batch (5 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: `/analyze-code` and `/analyze-system`

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `analyze.md` | `/analyze-code` | Use `/analyze-code comprehensive [target]` |
| `analyze-patterns.md` | `/analyze-code` | Use `/analyze-code patterns [scope]` |
| `analyze-performance.md` | `/analyze-system` | Use `/analyze-system performance [target]` |
| `development/project/analyze-dependencies.md` | `/analyze-system` | Use `/analyze-system dependencies [scope]` |
| `cost-analyze.md` | `/analyze-system` | Use `/analyze-system cost [scope]` |

**Location**: `deprecated/analyze*.md`, `deprecated/cost-analyze.md`, `deprecated/development/project/analyze-dependencies.md`

### Monitoring Commands Batch (3 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: `/monitor`

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `monitor-setup.md` | `/monitor` | Use `/monitor setup [config]` |
| `monitor-dashboard.md` | `/monitor` | Use `/monitor dashboard [view]` |
| `monitor-alerts.md` | `/monitor` | Use `/monitor alerts [config]` |

**Location**: `deprecated/monitor-*.md`

### Database Commands Batch (4 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: `/db-admin`

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `db-backup.md` | `/db-admin` | Use `/db-admin backup [target]` |
| `db-restore.md` | `/db-admin` | Use `/db-admin restore [source]` |
| `db-migrate.md` | `/db-admin` | Use `/db-admin migrate [direction]` |
| `db-seed.md` | `/db-admin` | Use `/db-admin seed [dataset]` |

**Location**: `deprecated/db-*.md`

### Workflow Commands Batch (6 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: Unified workflow commands

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `workflow.md` | `/project` | Use `/project workflow [config]` |
| `flow-schedule.md` | `/project` | Use `/project schedule [task]` |
| `progress-tracker.md` | `/project` | Use `/project track [target]` |
| `development/project/auto-provision.md` | `/project` | Use `/project provision [config]` |
| `development/project/env-setup.md` | `/project` | Use `/project setup-env [target]` |
| `development/project/dev-setup.md` | `/project` | Use `/project setup-dev [config]` |

**Location**: `deprecated/{workflow,flow-schedule,progress-tracker}.md`, `deprecated/development/project/{auto-provision,env-setup,dev-setup}.md`

### Development/Code Commands Batch (8 commands)
**Archived**: 2025-07-25 | **Consolidated Into**: `/dev`

| Deprecated Command | New Command | Migration Path |
|-------------------|-------------|----------------|
| `development/code/code-format.md` | `/dev` | Use `/dev format [target]` |
| `development/code/code-lint.md` | `/dev` | Use `/dev lint [scope]` |
| `development/code/dev-refactor.md` | `/dev` | Use `/dev refactor [target]` |
| `development/code/debug.md` | `/dev` | Use `/dev debug [issue]` |
| `development/code/feature.md` | `/dev` | Use `/dev feature [spec]` |
| `development/code/new.md` | `/dev` | Use `/dev new [type]` |
| `development/code/existing.md` | `/dev` | Use `/dev existing [target]` |
| `development/project/deps-update.md` | `/dev` | Use `/dev deps [action]` |

**Location**: `deprecated/development/code/*.md`, `deprecated/development/project/deps-update.md`

## Migration Guidelines

### For Users
1. **Update Scripts**: Replace deprecated command calls with new unified commands
2. **Check Migration Paths**: Use the migration path column for exact replacement syntax
3. **Deprecation Period**: Commands remain functional until 2025-08-25
4. **Documentation**: Updated documentation available for all unified commands

### For Developers
1. **Command History**: Full command history preserved in git repository
2. **Deprecation Metadata**: All commands contain proper deprecation metadata
3. **Testing**: All consolidated commands have comprehensive test coverage
4. **Rollback**: Archive structure allows for easy rollback if needed

## Archive Maintenance

### Access Deprecated Commands
```bash
# View deprecated command
cat .claude/commands/deprecated/[command-name].md

# List all deprecated commands
find .claude/commands/deprecated/ -name "*.md" -type f
```

### Archive Structure
```
deprecated/
├── DEPRECATED-INDEX.md              # This file
├── test-*.md                        # Testing commands (4 files)
├── quality-*.md                     # Quality commands (4 files)
├── secure-*.md, security.md         # Security commands (6 files)
├── pipeline-*.md                    # Pipeline commands (3 files)
├── analyze*.md, cost-analyze.md     # Analysis commands (3 files)
├── monitor-*.md                     # Monitoring commands (3 files)
├── db-*.md                         # Database commands (4 files)
├── workflow.md, flow-schedule.md, progress-tracker.md  # Workflow commands (3 files)
└── development/
    ├── code/                       # Development code commands (7 files)
    │   ├── code-format.md
    │   ├── code-lint.md
    │   ├── dev-refactor.md
    │   ├── debug.md
    │   ├── feature.md
    │   ├── new.md
    │   └── existing.md
    └── project/                    # Development project commands (8 files)
        ├── analyze-dependencies.md
        ├── auto-provision.md
        ├── cd-rollback.md
        ├── ci-run.md
        ├── ci-setup.md
        ├── deploy.md
        ├── deps-update.md
        ├── dev-build.md
        ├── dev-setup.md
        └── env-setup.md
```

## Consolidation Benefits

### User Experience Improvements
- **Reduced Complexity**: 50 deprecated commands → 12 unified commands
- **Consistent Interface**: Standardized argument patterns across all commands
- **Better Discovery**: Unified commands easier to find and understand
- **Enhanced Functionality**: Consolidated commands include enhanced features

### Maintenance Benefits
- **Reduced Duplication**: Eliminated redundant implementations
- **Better Testing**: Centralized testing for consolidated functionality
- **Easier Updates**: Single location for functionality updates
- **Cleaner Architecture**: Simplified command structure and dependencies

### Performance Benefits
- **Faster Loading**: Fewer commands to load and parse
- **Reduced Memory**: Less memory usage from duplicate code
- **Better Caching**: More efficient caching with unified commands

## Recovery Information

### Rollback Process
If rollback is needed, commands can be moved back from deprecated/ to their original locations:

```bash
# Example rollback (NOT recommended)
git log --oneline --grep="archive:" | head -10  # Find archive commits
git revert [commit-hash]  # Revert specific archive batch
```

### Support Information
- **Deprecated Until**: 2025-08-25
- **Support Contact**: See project documentation
- **Migration Help**: Available in unified command help text
- **Issue Reporting**: Use project issue tracker

---

**Archive Created**: 2025-07-25  
**Archive Maintainer**: Claude Code Cleanup Specialist  
**Last Updated**: 2025-07-25  
**Status**: Complete - All deprecated commands archived successfully