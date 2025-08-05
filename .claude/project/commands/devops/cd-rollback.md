---
name: /cd-rollback
description: Rollback your project deployment on Cloud Server (v1.0)
version: "1.0"
usage: /cd-rollback [--version previous-version] [--environment production|staging] [--emergency] [--dry-run] [--health-check]
category: devops
allowed-tools:
- Bash
- Read
- Write
- Edit
- MultiEdit
- Grep
dependencies:
- /deploy
- /ci-run
- /monitor-alerts
- /pipeline
validation:
  pre-execution: Verify rollback target exists and is healthy
  during-execution: Monitor rollback progress and system health
  post-execution: Validate restored version functionality
progressive-disclosure:
  layer-integration: Layer 1 provides instant rollback, Layer 2 offers version selection, Layer 3 enables complex recovery strategies
  quick-start: /cd-rollback (immediate rollback to last known good)
  advanced-usage: Multi-stage rollback with traffic management and data migration
safety-mechanisms:
  - Automatic backup before rollback
  - Health check validation of target version
  - Traffic gradual shift during rollback
  - Data integrity verification
error-recovery:
  rollback-failure: Attempt alternate recovery strategies
  data-incompatibility: Provide migration path guidance
  service-unavailable: Emergency mode with bypass options
  partial-failure: Component-level recovery options
---

# Deployment Rollback for your project (v1.0)

## V1.0 Enhanced Features
- ⚡ **Instant Recovery**: One-click rollback to last known good version
- 🎯 **Smart Version Selection**: Automatic health validation of target versions
- 🔄 **Zero-Downtime Rollback**: Gradual traffic shifting during recovery
- 📊 **Real-time Monitoring**: Live rollback progress and health metrics
- 🛡️ **Data Protection**: Automatic backups and integrity verification

I'll help you safely rollback **your project** deployments on **Cloud Server** with protection for your **developers** users.

## Rollback Configuration

- **Project**: your-project
- **Platform**: Cloud Server
- **CI/CD**: GitHub Actions
- **Security**: standard

## Rollback Strategies

### Immediate Rollback
Roll back to previous version:
```bash
/cd-rollback --immediate
```
- Fastest recovery
- Minimal downtime
- Automatic validation

### Version-Specific Rollback
Roll back to specific version:
```bash
/cd-rollback --version v2.3.1
```
- Targeted recovery
- Skip problem versions
- Historical restore

### Emergency Rollback
Critical situation response:
```bash
/cd-rollback --emergency
```
- Bypass checks
- Immediate action
- Alert all teams

## Environment Options

### Production Rollback
For developers protection:
```bash
/cd-rollback --environment production
```
- User impact analysis
- Traffic management
- Data preservation

### Staging Rollback
Testing environment:
```bash
/cd-rollback --environment staging
```
- Validation testing
- Safe experimentation
- Pre-production checks

## Rollback Process

### For Cloud Server
1. **Pre-Rollback Checks**
   - Current state snapshot
   - Database compatibility
   - Configuration backup

2. **Execution Steps**
   - Traffic diversion
   - Service shutdown
   - Version switch
   - Service restart

3. **Validation**
   - Health checks
   - Smoke tests
   - User verification
   - Monitoring alerts

## Database Considerations

For PostgreSQL:
- Migration reversal
- Data compatibility
- Schema rollback
- Backup restoration

## Safety Features

Your standard level ensures:
- Approval requirements
- Audit logging
- Backup creation
- Recovery testing

## Team Coordination

For 1-5 developers teams:
- Incident communication
- Status updates
- Task assignment
- Post-mortem prep

## Monitoring During Rollback

Real-time tracking:
- Service health
- Error rates
- Performance metrics
- User experience

## Post-Rollback Tasks

After successful rollback:
1. Verify system stability
2. Communicate to users
3. Document incident
4. Plan forward fix
5. Update runbooks

## Integration with devops-focused

Your workflow requires:
- Change approval
- Documentation
- Testing validation
- Team sign-off

What type of rollback do you need to perform?

## V1.0 Interactive Consultation Examples

### Layer 1 (Instant Rollback)
```bash
/cd-rollback  # Immediate rollback to last stable version
```

### Layer 2 (Version Selection)
```bash
/cd-rollback --version v2.3.1 --environment production
/cd-rollback --emergency --skip-checks
/cd-rollback --dry-run --health-check
```

### Layer 3 (Advanced Recovery)
```bash
# Complex rollback with traffic management
/cd-rollback --version v2.2.0 \
  --environment production \
  --strategy canary \
  --traffic-shift "10,25,50,100" \
  --health-check-interval 30s \
  --data-migration backward \
  --backup-first \
  --notify "slack,pagerduty" \
  --approval-required
```

## Integration with Other Commands
- Deploy with `/deploy` for forward deployments
- Monitor with `/monitor-alerts` during rollback
- Run pipelines with `/ci-run` for validation
- Orchestrate with `/pipeline` for complex scenarios