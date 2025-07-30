---
name: /cd-rollback
description: "Rollback lusaka deployment on Cloud Server"
usage: /cd-rollback [--version previous-version] [--environment production|staging] [--emergency]
category: devops
allowed-tools: Bash, Read, Write, Edit
---

# Deployment Rollback for lusaka

I'll help you safely rollback **lusaka** deployments on **Cloud Server** with protection for your **developers** users.

## Rollback Configuration

- **Project**: lusaka
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