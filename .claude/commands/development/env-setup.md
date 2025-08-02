---
name: /env-setup
description: Configure environments with automated secret management and zero-trust security (v1.0)
version: "1.0"
usage: '/env-setup [environment-name] [--clone-from existing-env] [--variables key=value] [--auto-detect]'
category: development
allowed-tools:
- Write
- Read
- Edit
- Bash
- Grep
security: input-validation-framework.md
dependencies:
- /dev-setup
- /security
- /pipeline
validation:
  pre-execution: "Validate environment names, check permissions, scan for secrets"
  during-execution: "Monitor configuration changes, validate connections"
  post-execution: "Verify environment health, test connectivity, audit changes"
progressive-disclosure:
  layer-integration: "Layer 1: Basic env vars, Layer 2: Secret management, Layer 3: Full infrastructure as code"
  options:
    - name: basic
      description: "Simple environment variables setup"
    - name: managed
      description: "Secrets and configuration management"
    - name: infrastructure
      description: "Complete IaC with GitOps integration"
safety-checks:
  - "Secret scanning and masking"
  - "Configuration drift detection"
  - "Access control validation"
  - "Audit trail generation"
error-recovery:
  - "Configuration rollback"
  - "Secret recovery procedures"
  - "Environment restoration"
performance:
  - "Parallel service validation"
  - "Configuration caching"
  - "Lazy secret loading"
security-features:
  - "Zero-trust architecture"
  - "Encrypted secret storage"
  - "RBAC enforcement"
  - "Compliance validation"
---

# Environment Configuration for lusaka (v1.0)

I'll help you set up and manage secure environment configurations with automated secret management, zero-trust security, and infrastructure as code integration.

## 🚀 Progressive Disclosure Layers

### Layer 1: Quick Environment Setup (30 seconds)
```bash
/env-setup development    # Basic development environment
/env-setup production     # Production with auto-detection
/env-setup --auto-detect  # Detect and configure automatically
```

### Layer 2: Managed Configuration (5 minutes)
```bash
/env-setup staging --with-secrets --vault integration
/env-setup production --clone-from staging --override DB_HOST=prod-db
```

### Layer 3: Infrastructure as Code (15+ minutes)
```bash
/env-setup --iac --terraform --with-gitops
/env-setup --kubernetes --helm-values --sealed-secrets
```

## 🔒 Security-First Configuration

### Input Validation
All inputs undergo comprehensive security validation:

```python
# Real-time validation with performance metrics
validation_results = {
    "environment_name": "✅ Validated (alphanumeric + dash/underscore)",
    "secrets_detected": "🔒 3 credentials automatically masked",
    "urls_validated": "✅ All endpoints verified against allowlist",
    "injection_attempts": "🛡️ 0 detected and blocked",
    "validation_time": "4.2ms (under 50ms requirement)"
}
```

### Secret Management
**Automatic secret detection and protection:**
- 🔍 Scans for API keys, passwords, tokens
- 🔒 Encrypts secrets at rest
- 🔑 Integrates with vault systems
- 📊 Tracks secret usage and rotation

## 🌍 Environment Types

### Development Environment
```bash
/env-setup development --auto-configure
```
**Features:**
- Debug logging enabled
- Local service endpoints
- Mock external services
- Fast iteration cycle
- Test data seeding

### Staging Environment
```bash
/env-setup staging --clone-from production --scale 0.5
```
**Features:**
- Production parity
- Reduced resource allocation
- Integration test ready
- Performance monitoring
- Canary deployment capable

### Production Environment
```bash
/env-setup production --high-availability --monitoring
```
**Features:**
- Zero-downtime deployment
- Auto-scaling configuration
- Full observability
- Disaster recovery
- Compliance validation

## 🛠️ Advanced Configuration

### Multi-Environment Management
```bash
# Create feature branch environment
/env-setup feature-auth --clone-from development --ttl 7d

# Promote configuration
/env-setup promote development to staging

# Environment diff
/env-setup diff staging production
```

### Infrastructure as Code
```yaml
# Auto-generated terraform/kubernetes configs
environments:
  production:
    replicas: 3
    resources:
      cpu: "2000m"
      memory: "4Gi"
    secrets:
      source: vault
      path: "secret/production"
    monitoring:
      enabled: true
      alerts: critical
```

### GitOps Integration
```bash
/env-setup --gitops --repo git@github.com:org/configs
```
**Workflow:**
1. Configuration changes create PR
2. Automated validation runs
3. Security scanning
4. Approval and merge
5. Automatic deployment

## 📊 Configuration Management

### Variable Injection
```bash
/env-setup production --variables \
  API_URL=$SECURE_API_URL \
  DB_HOST=$PROD_DB_HOST \
  FEATURE_FLAGS=payments,notifications
```

### Dynamic Configuration
```python
# Runtime configuration updates
config = {
    "feature_flags": {
        "dynamic": true,
        "source": "launchdarkly",
        "fallback": "config/features.json"
    },
    "scaling": {
        "auto": true,
        "min": 2,
        "max": 10,
        "metrics": ["cpu", "memory", "requests"]
    }
}
```

## 🔍 Validation & Health Checks

### Automated Validation Suite
```bash
/env-setup validate production
```
**Checks performed:**
- ✅ Service connectivity (all endpoints)
- ✅ Database migrations status
- ✅ Secret accessibility
- ✅ SSL certificate validity
- ✅ DNS resolution
- ✅ Load balancer health
- ✅ Monitoring agent status

### Continuous Validation
```yaml
# .env-monitoring.yml
health_checks:
  interval: 60s
  endpoints:
    - api: /health
    - database: :5432
    - cache: :6379
  alerts:
    - slack: "#ops-alerts"
    - pagerduty: critical
```

## 🚨 Security Features

### Zero-Trust Architecture
- No implicit trust between services
- mTLS for service communication
- Regular credential rotation
- Audit logging for all access

### Compliance Validation
```bash
/env-setup audit production --compliance SOC2,GDPR
```
**Reports:**
- Access control matrix
- Secret usage tracking
- Configuration drift
- Compliance violations

## 🎯 Quick Examples

### Basic Setup
```bash
# Development with defaults
/env-setup dev

# Production with monitoring
/env-setup prod --monitoring datadog
```

### Advanced Scenarios
```bash
# Blue-green deployment
/env-setup blue --clone-from green --inactive
/env-setup switch-traffic blue 10%

# Disaster recovery
/env-setup dr --clone-from production --region us-west
```

### Team Workflows
```bash
# Onboard new developer
/env-setup onboard john.doe --clone-from team-defaults

# Create review environment
/env-setup review-pr-123 --ttl 24h --clone-from staging
```

---

Ready to configure your environments? Choose your approach:
- 🚀 **Quick**: Auto-detect and configure
- 🔒 **Secure**: Full secret management
- 🏗️ **Complete**: Infrastructure as code with GitOps