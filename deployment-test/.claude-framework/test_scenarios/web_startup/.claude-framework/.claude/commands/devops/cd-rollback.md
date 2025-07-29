---
name: /cd-rollback
description: "Rollback [INSERT_PROJECT_NAME] deployment on [INSERT_DEPLOYMENT_TARGET]"
usage: /cd-rollback [--version previous-version] [--environment production|staging] [--emergency]
category: devops
tools: Bash, Read, Write, Edit
---

# Deployment Rollback for [INSERT_PROJECT_NAME]

I'll help you safely rollback **[INSERT_PROJECT_NAME]** deployments on **[INSERT_DEPLOYMENT_TARGET]** with protection for your **[INSERT_USER_BASE]** users.

## Rollback Configuration

- **Project**: [INSERT_PROJECT_NAME]
- **Platform**: [INSERT_DEPLOYMENT_TARGET]
- **CI/CD**: [INSERT_CI_CD_PLATFORM]
- **Security**: [INSERT_SECURITY_LEVEL]

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
For [INSERT_USER_BASE] protection:
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

### For [INSERT_DEPLOYMENT_TARGET]
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

For [INSERT_DATABASE_TYPE]:
- Migration reversal
- Data compatibility
- Schema rollback
- Backup restoration

## Safety Features

Your [INSERT_SECURITY_LEVEL] level ensures:
- Approval requirements
- Audit logging
- Backup creation
- Recovery testing

## Team Coordination

For [INSERT_TEAM_SIZE] teams:
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

## Integration with [INSERT_WORKFLOW_TYPE]

Your workflow requires:
- Change approval
- Documentation
- Testing validation
- Team sign-off

What type of rollback do you need to perform?