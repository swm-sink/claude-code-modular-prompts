---
name: /deploy
description: Deploy [INSERT_PROJECT_NAME] to [INSERT_DEPLOYMENT_TARGET] using [INSERT_CI_CD_PLATFORM]
usage: /deploy [environment] [--strategy blue-green|canary|rolling]
category: devops
tools: Bash, Read, Write, Edit
security_level: CRITICAL
---

# Deploy [INSERT_PROJECT_NAME]

<!-- SECURITY: Include command security wrapper for injection prevention -->
<include>components/security/command-security-wrapper.md</include>

**CRITICAL SECURITY NOTICE**: This command executes deployment operations with elevated privileges. ALL inputs are validated using security wrapper functions to prevent command injection, path traversal, and credential exposure.

I'll help you deploy **[INSERT_PROJECT_NAME]** to **[INSERT_DEPLOYMENT_TARGET]** using your configured **[INSERT_CI_CD_PLATFORM]** pipeline with comprehensive security validation.

## Deployment Configuration

- **Project**: [INSERT_PROJECT_NAME]
- **Tech Stack**: [INSERT_TECH_STACK]
- **Target**: [INSERT_DEPLOYMENT_TARGET]
- **CI/CD**: [INSERT_CI_CD_PLATFORM]
- **Security**: [INSERT_SECURITY_LEVEL]

## Deployment Strategies

### For [INSERT_TEAM_SIZE] Teams

Based on your team size and [INSERT_WORKFLOW_TYPE] workflow:

#### Blue-Green Deployment
Zero-downtime deployment for [INSERT_USER_BASE] (with security validation):
```bash
/deploy production --strategy blue-green
# SECURITY: Environment 'production' validated using validateEnvironmentName()
# SECURITY: Strategy 'blue-green' validated against allowed deployment strategies
# SECURITY: All deployment commands validated against DEPLOY_ALLOWED_COMMANDS
```

#### Canary Deployment
Gradual rollout for [INSERT_PERFORMANCE_PRIORITY] systems (with security validation):
```bash
/deploy production --strategy canary --percentage 10
# SECURITY: Environment validated, strategy validated, percentage value sanitized
# SECURITY: All canary deployment commands validated against security allowlist
```

#### Rolling Update
Standard deployment for [INSERT_DEPLOYMENT_TARGET] (with security validation):
```bash
/deploy staging --strategy rolling
# SECURITY: Environment 'staging' validated using validateEnvironmentName()
# SECURITY: Rolling update commands validated against DEPLOY_ALLOWED_COMMANDS
```

## Pre-Deployment Checks - SECURITY ENHANCED

Your [INSERT_SECURITY_LEVEL] security level requires:
- **MANDATORY**: Input validation using security wrapper functions
- **MANDATORY**: Environment name validation using validateEnvironmentName()
- **MANDATORY**: Deployment strategy validation against allowed strategies
- **MANDATORY**: All deployment commands validated against DEPLOY_ALLOWED_COMMANDS allowlist
- Security scanning with sanitized results
- Dependency vulnerability check with secure reporting
- Configuration validation with path traversal prevention
- Health check endpoints with sanitized responses
- **MANDATORY**: Credential protection and masking
- **MANDATORY**: Error message sanitization

## Environment-Specific Settings

### [INSERT_DEPLOYMENT_TARGET] Configuration
- Auto-scaling policies
- Load balancer settings
- Database connection strings
- Environment variables

## Integration with [INSERT_CI_CD_PLATFORM]

Your deployment pipeline includes:
- Build stage for [INSERT_TECH_STACK]
- Test execution with [INSERT_TESTING_FRAMEWORK]
- Security scanning
- Deployment automation
- Post-deployment validation

## Rollback Strategy

For [INSERT_USER_BASE] protection:
- Automatic rollback triggers
- Manual rollback command
- Database migration reversal
- State preservation

## Monitoring Integration

Post-deployment for [INSERT_PROJECT_NAME]:
- Application metrics
- Error rate monitoring
- Performance baselines
- User experience tracking

**SECURITY EXECUTION PROCESS:**

1. **Input Validation**: All deployment parameters validated using security wrapper
2. **Environment Validation**: Environment name validated using validateEnvironmentName()
3. **Strategy Validation**: Deployment strategy validated against security policies
4. **Command Validation**: All deployment commands validated against DEPLOY_ALLOWED_COMMANDS
5. **Credential Protection**: All sensitive data masked and protected
6. **Secure Execution**: Deployment executed using executeSecureCommand() wrapper
7. **Audit Logging**: Complete security audit trail maintained
8. **Error Sanitization**: All error messages sanitized to prevent information disclosure

**ALLOWED ENVIRONMENTS**: development, staging, production, test, dev, stage, prod
**ALLOWED STRATEGIES**: blue-green, canary, rolling
**ALLOWED COMMANDS**: docker, kubectl, helm, systemctl, aws, gcloud, az, terraform

Which environment would you like to deploy to? (Environment will be validated for security compliance)