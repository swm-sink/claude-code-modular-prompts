# Deployment Commands

Advanced deployment automation with CI/CD integration, rollback capabilities, and multi-environment support for safe, reliable software delivery.

## Command Overview

The deployment commands provide comprehensive automation for software delivery pipelines, supporting multiple environments, rollback strategies, and integration with popular CI/CD platforms. All commands include safety validations and confirmation workflows.

## Available Commands

### Core Deployment

#### `/deploy`
Execute deployment pipelines with comprehensive validation and rollback capabilities.

**Usage**:
```bash
/deploy production                    # Deploy to production environment
/deploy staging --dry-run            # Preview staging deployment
/deploy production --rollback        # Rollback production deployment
```

**Features**:
- Multi-environment support (development, staging, production)
- Dry-run capability for safe testing
- Automatic rollback on failure
- Health check validation
- Deployment approval workflows

#### `/global-deploy`
Orchestrate global deployments across multiple regions with compliance and localization support.

**Usage**:
```bash
/global-deploy all-regions           # Deploy to all configured regions
/global-deploy --region us-east-1    # Deploy to specific region
/global-deploy --compliance gdpr     # Deploy with GDPR compliance
```

**Features**:
- Multi-region deployment orchestration
- Compliance framework integration (GDPR, SOC2, etc.)
- Cultural and localization preferences
- Blue-green deployment strategies
- Canary release management

### CI/CD Integration

#### `/ci setup`
Configure continuous integration pipelines with automated testing and quality gates.

**Usage**:
```bash
/ci setup github-actions             # Set up GitHub Actions workflow
/ci setup gitlab-ci                  # Configure GitLab CI pipeline
/ci setup jenkins                    # Set up Jenkins pipeline
```

#### `/ci run`
Execute CI/CD pipelines with progress monitoring and failure handling.

**Usage**:
```bash
/ci run main-build                   # Run main build pipeline
/ci run test-suite                   # Execute test pipeline
/ci run deploy-staging               # Run staging deployment
```

### Provisioning & Infrastructure

#### `/auto-provision`
Automated infrastructure provisioning with cloud provider integration.

**Usage**:
```bash
/auto-provision aws                  # Provision AWS infrastructure
/auto-provision kubernetes          # Set up Kubernetes cluster
/auto-provision terraform           # Apply Terraform configuration
```

### Rollback & Recovery

#### `/cd-rollback`
Safe rollback capabilities with validation and confirmation workflows.

**Usage**:
```bash
/cd-rollback production              # Rollback production deployment
/cd-rollback --version 1.2.3        # Rollback to specific version
/cd-rollback --emergency             # Emergency rollback procedure
```

## Safety & Compliance Features

### Deployment Safety
- **Pre-deployment Validation**: Comprehensive checks before deployment
- **User Confirmation**: Required approval for production deployments  
- **Health Monitoring**: Continuous health checks during deployment
- **Automatic Rollback**: Fail-safe rollback on error detection
- **Audit Logging**: Complete audit trail of all deployment activities

### Constitutional AI Integration
- **Safety Frameworks**: Constitutional compliance for all deployment operations
- **Risk Assessment**: Automated risk evaluation for deployment changes
- **Approval Workflows**: Multi-level approval for high-risk deployments
- **Compliance Monitoring**: Continuous compliance validation

## Configuration Requirements

Deployment commands integrate with `PROJECT_CONFIG.xml` for environment-specific settings:

```xml
<deployment>
  <environments>
    <environment name="production">
      <deploy_command>npm run deploy:prod</deploy_command>
      <health_check_url>https://api.example.com/health</health_check_url>
      <rollback_command>npm run rollback</rollback_command>
    </environment>
  </environments>
  <ci_platform>github-actions</ci_platform>
  <compliance_requirements>
    <requirement>GDPR</requirement>
    <requirement>SOC2</requirement>
  </compliance_requirements>
</deployment>
```

## Integration Patterns

### Component Integration
All deployment commands leverage shared framework components:

- `components/deployment/ci-cd-integration.md` - CI/CD pipeline integration
- `components/interaction/request-user-confirmation.md` - Approval workflows
- `components/interaction/progress-reporting.md` - Deployment progress tracking
- `components/workflow/error-handling.md` - Error recovery patterns
- `components/security/owasp-compliance.md` - Security validation
- `components/reporting/generate-structured-report.md` - Deployment reporting

### Error Handling
- **Circuit Breaker Patterns**: Prevent cascading failures
- **Graceful Degradation**: Maintain service availability during issues
- **Recovery Workflows**: Automated recovery from common failure scenarios
- **Monitoring Integration**: Real-time monitoring and alerting

## Best Practices

### Production Deployments
1. **Always use dry-run first** to validate deployment plan
2. **Require explicit confirmation** for production deployments
3. **Monitor health checks** throughout deployment process
4. **Maintain rollback readiness** with tested rollback procedures
5. **Document all changes** with comprehensive deployment reports

### Multi-Environment Strategy
1. **Progressive deployment** through development → staging → production
2. **Environment-specific validation** with appropriate test suites
3. **Configuration management** with environment-specific settings
4. **Access controls** with role-based deployment permissions

### Compliance & Security
1. **Constitutional AI compliance** for all deployment operations
2. **Security scanning** before deployment execution
3. **Audit trail maintenance** for compliance requirements
4. **Regular compliance reviews** and validation cycles

## Troubleshooting

### Common Issues
- **Failed Health Checks**: Automatic rollback triggered, check application logs
- **Permission Errors**: Verify deployment credentials and access controls
- **Configuration Issues**: Validate PROJECT_CONFIG.xml deployment settings
- **Network Timeouts**: Check network connectivity and firewall rules

### Emergency Procedures
- **Emergency Rollback**: Use `/cd-rollback --emergency` for immediate rollback
- **Service Recovery**: Follow documented incident response procedures
- **Escalation**: Contact deployment team for critical issues

## Monitoring & Observability

### Deployment Metrics
- Deployment success rate and frequency
- Rollback frequency and root causes
- Time to deployment (lead time)
- Mean time to recovery (MTTR)
- Change failure rate

### Alerting
- Failed deployment notifications
- Health check failure alerts
- Rollback execution notifications
- Compliance violation alerts

---

*For detailed usage examples and advanced configuration, see the individual command documentation files in this directory.* 