# /deploy - Deployment & Production Workflows

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Execute deployment and production workflows including build preparation, deployment validation, production monitoring, and rollback procedures. Ideal for releasing code to production environments safely and reliably.

**Note**: This is a simplified version that focuses on core deployment functionality without complex orchestration frameworks.

---

## How It Works

### 1. Pre-Deployment Preparation
- **Build Validation**: Ensure code builds successfully
- **Test Execution**: Run comprehensive test suites
- **Security Checks**: Validate security requirements
- **Dependency Verification**: Check dependencies and compatibility

### 2. Deployment Planning
- **Environment Setup**: Prepare target deployment environment
- **Configuration Management**: Manage environment-specific configurations
- **Rollback Strategy**: Plan rollback procedures and checkpoints
- **Monitoring Setup**: Configure monitoring and alerting

### 3. Deployment Execution
- **Safe Deployment**: Execute deployment with safety measures
- **Health Monitoring**: Monitor system health during deployment
- **Validation Testing**: Verify deployment success
- **Performance Monitoring**: Monitor performance post-deployment

### 4. Post-Deployment
- **System Validation**: Validate system functionality
- **Performance Analysis**: Analyze system performance
- **Monitoring Setup**: Ensure monitoring is operational
- **Documentation Updates**: Update deployment documentation

---

## Usage Examples

```bash
# Deploy to staging environment
/deploy --environment staging

# Deploy to production with monitoring
/deploy --environment production --monitor

# Deploy with rollback plan
/deploy --environment production --rollback-plan

# Deploy specific version
/deploy --version 1.2.3 --environment production

# Deploy with health checks
/deploy --environment production --health-checks
```

---

## What It Does

### Build & Validation
- Validates code builds successfully
- Runs comprehensive test suites
- Performs security and quality checks
- Verifies dependencies and compatibility

### Environment Management
- Prepares deployment environments
- Manages environment-specific configurations
- Sets up infrastructure and services
- Configures monitoring and logging

### Safe Deployment
- Executes deployment with safety measures
- Monitors system health during deployment
- Validates deployment success
- Provides rollback capabilities

### Post-Deployment Support
- Validates system functionality
- Monitors performance and health
- Provides ongoing support and maintenance
- Documents deployment procedures

---

## Deployment Types

### Staging Deployment
```
PURPOSE: Deploy to staging environment for testing
APPROACH: Full deployment with testing validation
OUTPUT: Staging environment ready for testing
```

### Production Deployment
```
PURPOSE: Deploy to production environment
APPROACH: Safe deployment with monitoring and rollback
OUTPUT: Production system updated and monitored
```

### Rollback Deployment
```
PURPOSE: Rollback to previous stable version
APPROACH: Quick rollback with minimal downtime
OUTPUT: System restored to previous stable state
```

### Emergency Deployment
```
PURPOSE: Deploy critical fixes immediately
APPROACH: Expedited deployment with safety measures
OUTPUT: Critical issues resolved quickly
```

---

## Output Format

### Deployment Summary
```
DEPLOYMENT_TYPE: [staging/production/rollback/emergency]
ENVIRONMENT: [target-environment]
VERSION: [deployed-version]
STATUS: [preparing/deploying/validating/completed]
```

### Pre-Deployment Checks
```
BUILD_STATUS: [build-validation-results]
TEST_RESULTS: [test-execution-results]
SECURITY_CHECKS: [security-validation-status]
DEPENDENCIES: [dependency-verification-results]
```

### Deployment Results
```
DEPLOYMENT_STATUS: [success/failure/partial]
HEALTH_CHECKS: [system-health-validation]
PERFORMANCE: [performance-metrics]
ROLLBACK_AVAILABLE: [rollback-readiness-status]
```

### Post-Deployment Monitoring
```
SYSTEM_HEALTH: [ongoing-health-monitoring]
PERFORMANCE_METRICS: [performance-monitoring-results]
ALERTS: [active-alerts-and-notifications]
DOCUMENTATION: [updated-deployment-documentation]
```

---

## Deployment Process

### 1. Pre-Deployment Phase
- Validate code builds and tests pass
- Perform security and quality checks
- Verify dependencies and compatibility
- Prepare deployment environment

### 2. Deployment Planning Phase
- Plan deployment strategy and timeline
- Set up environment configurations
- Prepare rollback procedures
- Configure monitoring and alerting

### 3. Deployment Execution Phase
- Execute deployment with safety measures
- Monitor system health during deployment
- Validate deployment success
- Activate monitoring and alerting

### 4. Post-Deployment Phase
- Validate system functionality
- Monitor performance and health
- Address any issues or alerts
- Update documentation and procedures

---

## Key Features

### ✅ Safe Deployment
- Comprehensive pre-deployment validation
- Incremental deployment with health checks
- Rollback capabilities and procedures
- Risk mitigation and safety measures

### ✅ Environment Management
- Multi-environment support
- Configuration management
- Infrastructure preparation
- Service orchestration

### ✅ Monitoring & Alerting
- Real-time health monitoring
- Performance tracking
- Alert configuration and management
- Issue detection and notification

### ✅ Documentation & Compliance
- Deployment documentation
- Compliance validation
- Audit trail and logging
- Knowledge preservation

---

## Deployment Strategies

### Blue-Green Deployment
- **Approach**: Maintain two identical production environments
- **Benefits**: Zero downtime, instant rollback
- **Use Cases**: High availability requirements
- **Complexity**: Requires infrastructure duplication

### Rolling Deployment
- **Approach**: Gradual replacement of instances
- **Benefits**: Minimal resource requirements
- **Use Cases**: Scalable applications
- **Complexity**: Moderate setup complexity

### Canary Deployment
- **Approach**: Gradual rollout to subset of users
- **Benefits**: Risk mitigation, gradual validation
- **Use Cases**: New feature rollouts
- **Complexity**: Requires sophisticated routing

### Recreate Deployment
- **Approach**: Stop old version, deploy new version
- **Benefits**: Simple implementation
- **Use Cases**: Development environments
- **Complexity**: Involves downtime

---

## Environment Management

### Development Environment
- **Purpose**: Development and testing
- **Configuration**: Relaxed security, debugging enabled
- **Monitoring**: Basic monitoring and logging
- **Deployment**: Frequent, automated deployments

### Staging Environment
- **Purpose**: Production-like testing
- **Configuration**: Production-like settings
- **Monitoring**: Comprehensive monitoring
- **Deployment**: Scheduled, validated deployments

### Production Environment
- **Purpose**: Live user-facing system
- **Configuration**: Optimized for performance and security
- **Monitoring**: Real-time monitoring and alerting
- **Deployment**: Controlled, safe deployments

---

## Best Practices

### When to Use
- **Release Preparation**: Before releasing new versions
- **Production Updates**: When updating production systems
- **Emergency Fixes**: For critical issue resolution
- **Environment Refresh**: When refreshing environments

### Deployment Tips
- Always test deployments in staging first
- Use automated deployment pipelines
- Monitor system health during deployment
- Have rollback procedures ready
- Document deployment procedures

### Quality Guidelines
- Validate builds and tests before deployment
- Use incremental deployment strategies
- Monitor system performance post-deployment
- Maintain deployment documentation
- Learn from deployment issues

---

## Error Handling

### Common Issues
- **Build Failures**: Provides build debugging and resolution
- **Test Failures**: Suggests test fixes and validation
- **Deployment Failures**: Provides rollback and recovery procedures
- **Performance Issues**: Monitors and optimizes performance

### Graceful Degradation
- Provides partial deployment when full deployment fails
- Suggests alternative deployment strategies
- Maintains system stability during issues
- Documents failures and recovery procedures

---

## Integration

### Works Well With
- `/context-prime` - For project context before deployment
- `/test` - For comprehensive testing before deployment
- `/review` - For deployment script and configuration review
- `/debug` - For investigating deployment issues

### Typical Workflow
1. **Context**: `/context-prime` to understand project deployment context
2. **Testing**: `/test` to validate code before deployment
3. **Review**: `/review` to review deployment configurations
4. **Deployment**: `/deploy` to execute deployment safely

---

## Deployment Validation

### Pre-Deployment Validation
- **Build Validation**: Ensure code builds successfully
- **Test Execution**: Run comprehensive test suites
- **Security Checks**: Validate security requirements
- **Dependency Verification**: Check dependencies and versions

### Deployment Validation
- **Health Checks**: Verify system health during deployment
- **Functionality Tests**: Test core functionality
- **Performance Validation**: Monitor performance metrics
- **Integration Tests**: Validate external integrations

### Post-Deployment Validation
- **System Functionality**: Comprehensive functionality testing
- **Performance Monitoring**: Ongoing performance tracking
- **User Experience**: Validate user-facing functionality
- **Security Validation**: Verify security measures

---

## Monitoring & Alerting

### System Health Monitoring
- **Service Status**: Monitor service availability
- **Resource Usage**: Track CPU, memory, disk usage
- **Response Times**: Monitor application response times
- **Error Rates**: Track error frequencies and patterns

### Performance Monitoring
- **Throughput**: Monitor request processing rates
- **Latency**: Track response time distributions
- **Resource Efficiency**: Monitor resource utilization
- **Scalability**: Track system scaling behavior

### Alert Configuration
- **Threshold Alerts**: Set up threshold-based alerts
- **Anomaly Detection**: Monitor for unusual patterns
- **Escalation Procedures**: Define alert escalation paths
- **Notification Channels**: Configure notification methods

---

## Rollback Procedures

### Rollback Planning
- **Rollback Triggers**: Define when to rollback
- **Rollback Procedures**: Document rollback steps
- **Data Considerations**: Plan for data migration issues
- **Communication**: Establish communication procedures

### Rollback Execution
- **Quick Rollback**: Execute rollback quickly and safely
- **Health Validation**: Verify system health post-rollback
- **Impact Assessment**: Assess rollback impact
- **Recovery Planning**: Plan recovery from rollback

### Rollback Testing
- **Rollback Validation**: Test rollback procedures regularly
- **Automation**: Automate rollback procedures when possible
- **Documentation**: Document rollback experiences
- **Improvement**: Continuously improve rollback procedures

---

## Security Considerations

### Deployment Security
- **Access Control**: Secure deployment access and permissions
- **Secrets Management**: Manage secrets and credentials securely
- **Network Security**: Secure network configurations
- **Audit Logging**: Log deployment activities

### Production Security
- **Security Hardening**: Implement security best practices
- **Vulnerability Management**: Regular security assessments
- **Compliance**: Ensure regulatory compliance
- **Incident Response**: Prepare for security incidents

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple deployment workflow
- **No Module Dependencies**: Self-contained deployment logic
- **No Advanced Frameworks**: Basic deployment patterns
- **No Mandatory Enforcement**: Supportive deployment guidance

### Core Focus
- **Essential Deployment**: Core build, deploy, and monitor functionality
- **Practical Safety**: Basic safety measures and validation
- **Fast Execution**: Minimal overhead for quick deployments
- **Clear Results**: Well-structured deployment outcomes

---

**Note**: This simplified command provides core deployment functionality without the complexity of the full framework. For advanced features like complex orchestration, multi-agent deployment coordination, or advanced infrastructure management, use the full framework commands.