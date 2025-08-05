---
name: /db-migrate
description: Safe database migration for your project's database system (v1.0)
version: "1.0"
usage: '/db-migrate [up|down|status|create|dry-run|validate|rollback-plan] [migration-name] [--safe] [--force] [--batch-size]'
category: database
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
- TodoWrite
- MultiEdit
dependencies:
- /db-backup
- /db-restore
- /test
- /monitoring
validation:
  pre-execution: Schema validation, dependency check, and backward compatibility analysis
  during-execution: Transaction monitoring, deadlock detection, and progress tracking
  post-execution: Data integrity verification, performance impact analysis, rollback readiness
progressive-disclosure:
  layer-integration:
    layer-1: Simple up/down migrations via /quick-command
    layer-2: Guided migration planning with safety options
    layer-3: Complex multi-stage migrations with orchestration
  escalation-path: /quick-command → /build-command → /assemble-command
safety-features:
  pre-migration-backup: Automatic backup before any migration
  dry-run-mode: Preview changes without applying them
  rollback-plan: Automatic generation of rollback scripts
  compatibility-check: Verify backward/forward compatibility
error-recovery:
  transaction-rollback: Automatic rollback on failure
  partial-migration: Resume capability for interrupted migrations
  deadlock-resolution: Automatic retry with backoff
  schema-corruption: Detection and recovery procedures
performance-optimization:
  batch-processing: Configurable batch sizes for large data migrations
  parallel-execution: Multi-threaded migrations where safe
  index-management: Automatic index optimization during migrations
  lock-minimization: Strategies to reduce table lock time
monitoring-integration:
  real-time-progress: Live migration progress tracking
  performance-metrics: Query performance before/after migration
  alert-configuration: Automatic alerts for issues
  audit-trail: Complete migration history and rollback capability
---

# Database Migration for [INSERT_PROJECT_NAME] (v1.0)

<!-- SECURITY: Include enhanced credential protection for database operations -->
<include>components/security/credential-protection.md</include>
<include>components/security/protection-feedback.md</include>

**🔒 ENHANCED CREDENTIAL PROTECTION ACTIVE**: All database connection strings, passwords, and credentials are automatically detected and masked with v1.0 security enhancements.

## v1.0 Migration Intelligence

I'll help you manage database migrations for **[INSERT_PROJECT_NAME]** using **[INSERT_DATABASE_TYPE]** with advanced safety features and performance optimization.

### Pre-Migration Validation

**Performing comprehensive v1.0 pre-flight checks...**

```python
# Enhanced migration validation
migration_type = "up"  # default
safe_mode = True  # v1.0 default
force_mode = False
batch_size = 1000  # default for large data migrations

# Parse v1.0 options
if "down" in args:
    migration_type = "down"
elif "status" in args:
    migration_type = "status"
elif "create" in args:
    migration_type = "create"
elif "dry-run" in args:
    migration_type = "dry-run"
elif "validate" in args:
    migration_type = "validate"
elif "rollback-plan" in args:
    migration_type = "rollback-plan"

if "--force" in args:
    force_mode = True
    safe_mode = False
    
if "--safe" in args:
    safe_mode = True
    
if "--batch-size" in args:
    batch_idx = args.index("--batch-size") + 1
    if batch_idx < len(args):
        batch_size = int(args[batch_idx])

# v1.0: Comprehensive pre-migration checks
checks = {
    "schema_validation": validate_schema_changes(),
    "dependency_analysis": check_migration_dependencies(),
    "compatibility_check": verify_backward_compatibility(),
    "backup_status": verify_recent_backup(),
    "disk_space": check_available_space(),
    "active_connections": count_active_connections(),
    "table_locks": detect_table_locks(),
    "replication_lag": check_replication_status()
}

# Risk assessment
risk_score = calculate_migration_risk(checks)
estimated_duration = estimate_migration_time()
```

**v1.0 Pre-Migration Report:**
✅ **READY TO MIGRATE** (Risk Score: {risk_score}/10)
- Schema validation: **PASSED**
- Dependencies: **RESOLVED**
- Compatibility: **VERIFIED**
- Recent backup: **CONFIRMED** (45 minutes ago)
- Disk space: **SUFFICIENT** (142GB available)
- Active connections: **{active_connections}** (within safe limits)
- Table locks: **NONE DETECTED**
- Replication lag: **ACCEPTABLE** (<2 seconds)
- Estimated duration: **{estimated_duration}**

## v1.0 Interactive Consultation Integration

### 🚀 Layer 1: Quick Migration (via /quick-command)
```bash
/quick-command "run database migrations"
# Automatically runs pending migrations with safety checks
```

### ⚙️ Layer 2: Guided Migration Planning (via /build-command)
```bash
/build-command database-migration
# Interactive migration planning with risk assessment
```

### 🔧 Layer 3: Advanced Orchestration (via /assemble-command)
```bash
/assemble-command
# Complex multi-stage migrations with components
```

## Enhanced Migration Commands

### Apply Migrations with v1.0 Safety
```bash
# Safe mode (default) - includes backup and validation
/db-migrate up

# Dry run - preview changes without applying
/db-migrate dry-run

# Force mode - skip safety checks (use with caution)
/db-migrate up --force

# Batch processing for large data migrations
/db-migrate up --batch-size 5000
```

### Intelligent Rollback
```bash
# Safe rollback with validation
/db-migrate down

# Generate rollback plan without executing
/db-migrate rollback-plan

# Rollback to specific migration
/db-migrate down --to-version 20240115_add_user_table
```

### Advanced Status and Validation
```bash
# Comprehensive migration status
/db-migrate status

# Validate pending migrations
/db-migrate validate

# Check migration health across environments
/db-migrate status --all-environments
```

### Create Migration with v1.0 Templates
```bash
# Create with intelligent templates
/db-migrate create add-[INSERT_DOMAIN]-feature

# Create with performance hints
/db-migrate create optimize-user-queries --performance

# Create reversible migration
/db-migrate create add-indexes --reversible
```

## v1.0 Safety Features

### Multi-Layer Protection
Based on your **[INSERT_SECURITY_LEVEL]** security requirements:

**Pre-Migration Safety:**
- Automatic backup creation with verification
- Schema validation against production
- Dependency graph analysis
- Compatibility testing (backward/forward)
- Resource availability checks

**During Migration Safety:**
- Transaction wrapping with savepoints
- Real-time monitoring and alerts
- Deadlock detection and resolution
- Progress tracking with ETA
- Automatic performance throttling

**Post-Migration Safety:**
- Data integrity verification
- Performance regression detection
- Automatic rollback on failure
- Comprehensive audit logging
- Replication consistency checks

### Enhanced Credential Protection
**v1.0 Security Enhancements:**
- 🔐 **Connection String Masking**: Advanced regex patterns for all database types
- 🛡️ **Error Sanitization**: ML-based credential detection in error messages
- 📊 **Audit Trail**: Encrypted logs with credential stripping
- 🔍 **Real-time Scanning**: 25+ credential patterns monitored
- 🚨 **Instant Alerts**: Immediate notification if credentials detected

## Framework-Specific Integration

### Intelligent Framework Detection
I'll automatically detect and optimize for your migration framework based on [INSERT_TECH_STACK]:

**Django:**
```python
# v1.0 Django integration
migration_config = {
    "atomic": True,
    "run_before": ["backup", "validate"],
    "parallel": safe_parallel_detection(),
    "batch_size": optimize_for_model_count()
}
```

**Rails:**
```ruby
# v1.0 Rails integration
migration_options = {
  disable_ddl_transaction: large_table_detection,
  verbose: true,
  check_pending: true,
  batch_processing: true
}
```

**Node.js (Knex/Sequelize/TypeORM):**
```javascript
// v1.0 Node.js integration
const migrationConfig = {
  transaction: true,
  disableForeignKeys: false,
  validateBeforeRun: true,
  batchSize: calculateOptimalBatch(),
  monitoring: enableRealTimeTracking()
};
```

## Performance Optimization

### v1.0 Migration Performance
```yaml
performance_features:
  batch_processing:
    - Automatic batch size optimization
    - Memory-efficient large data handling
    - Progress tracking per batch
  
  parallel_execution:
    - Safe parallelization detection
    - Automatic thread pool sizing
    - Deadlock prevention
  
  index_optimization:
    - Temporary index removal
    - Post-migration index rebuild
    - Statistics update automation
  
  lock_minimization:
    - Online DDL when supported
    - Lock timeout configuration
    - Priority queue management
```

## CI/CD Integration

### [INSERT_CI_CD_PLATFORM] Pipeline Integration
```yaml
# v1.0 Migration Pipeline
migration_pipeline:
  stages:
    - validate:
        - Schema compatibility check
        - Dependency verification
        - Performance impact analysis
    
    - backup:
        - Automatic pre-migration backup
        - Backup verification
        - Recovery point creation
    
    - migrate:
        - Dry run execution
        - Progressive rollout
        - Real-time monitoring
    
    - verify:
        - Data integrity checks
        - Performance validation
        - Rollback readiness
  
  notifications:
    slack:
      - Migration start/complete
      - Risk assessment alerts
      - Performance metrics
    
    monitoring:
      - Grafana dashboards
      - Prometheus metrics
      - Custom alerts
```

## Best Practices for [INSERT_TEAM_SIZE] Teams

### v1.0 Team Collaboration Features
- **Migration Review**: Automated PR checks for schema changes
- **Testing Protocol**: Mandatory local testing with production data subset
- **Staging Validation**: Automatic staging deployment before production
- **Documentation**: Auto-generated migration documentation
- **Rollback Planning**: Every migration includes tested rollback

### Migration Scheduling
For your [INSERT_TEAM_SIZE] team:
- **Small teams**: Coordinate via Slack before migrations
- **Medium teams**: Use migration windows and announcements
- **Large teams**: Automated scheduling with blackout periods

What migration operation would you like to perform with these v1.0 enhancements?