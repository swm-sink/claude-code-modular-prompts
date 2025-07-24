# GitHub Actions Workflows

This directory contains comprehensive CI/CD workflows for the Claude Code Framework project.

## 🚀 Workflows Overview

### 1. Continuous Integration (`ci.yml`)
**Triggers**: Push to main/develop, Pull requests, Daily schedule
**Purpose**: Core quality validation and testing

**Jobs**:
- **Security Scan**: Detects hardcoded secrets and validates environment configuration
- **Framework Validation**: Validates framework structure, .claude directory, and PROJECT_CONFIG.xml
- **Streamlit Tests**: Runs comprehensive test suite with 85% coverage requirement
- **Documentation Check**: Validates documentation completeness and internal links
- **Health Check**: Tests health monitoring system functionality
- **Deployment Test**: Validates Railway deployment configuration

### 2. Deployment Pipeline (`deployment.yml`)
**Triggers**: Push to main, Tags (v*), Manual workflow dispatch
**Purpose**: Automated deployment to Railway with staging/production environments

**Jobs**:
- **Pre-deployment Validation**: Environment selection and readiness checks
- **Security Pre-check**: Enhanced security scanning before deployment
- **Staging Deployment**: Automated deployment to Railway staging environment
- **Production Deployment**: Production deployment (tags only or manual trigger)
- **Health Checks**: Post-deployment validation and monitoring

### 3. Security Audit (`security.yml`)
**Triggers**: Push, Pull requests, Weekly schedule, Manual dispatch
**Purpose**: Comprehensive security analysis and vulnerability detection

**Jobs**:
- **Secret Scanning**: Advanced pattern matching for various secret types
- **Dependency Audit**: Python dependency vulnerability scanning with `safety` and `bandit`
- **Configuration Security**: Railway, Streamlit, and file permission audits
- **Network Security**: Hardcoded IP and insecure URL detection

### 4. Claude Framework Validation (`claude-framework.yml`)
**Triggers**: Changes to .claude/, CLAUDE.md, PROJECT_CONFIG.xml, Daily schedule
**Purpose**: Framework-specific validation and structure integrity

**Jobs**:
- **Framework Structure**: CLAUDE.md and .claude directory validation
- **Command Validation**: Core and meta command completeness checks
- **Module Validation**: Module categorization and documentation coverage
- **Quality Validation**: Quality gates and TDD enforcement verification
- **Integration Validation**: Command-module integration and cross-reference checks

## 🔧 Configuration Requirements

### Repository Secrets
For automated deployment, configure these secrets in your repository:

```
RAILWAY_TOKEN=your_railway_auth_token
```

### Environment Variables
The workflows use these environment variables:
- `PYTHON_VERSION`: "3.11" (Python version for testing)
- `NODE_VERSION`: "18" (Node.js version if needed)
- `FRAMEWORK_VERSION`: "3.0.0" (Claude Code Framework version)

## 🏆 Quality Standards

### Test Coverage Requirements
- Minimum 85% code coverage required for CI to pass
- Coverage reports uploaded to Codecov (if configured)
- Tests must pass in isolated environment

### Security Standards
- Zero tolerance for hardcoded secrets
- Weekly dependency vulnerability scans
- Comprehensive file permission audits
- Network security validation

### Framework Standards
- Complete command and module documentation
- Proper command-module integration
- Quality gates enforcement
- Atomic rollback protocol compliance

## 🚦 Workflow Status Badges

Add these badges to your README to show workflow status:

```markdown
![CI](https://github.com/swm-sink/claude-code-modular-prompts/workflows/Continuous%20Integration/badge.svg)
![Security](https://github.com/swm-sink/claude-code-modular-prompts/workflows/Security%20Audit/badge.svg)
![Framework](https://github.com/swm-sink/claude-code-modular-prompts/workflows/Claude%20Code%20Framework%20Validation/badge.svg)
```

## 📋 Workflow Triggers Summary

| Workflow | Push | PR | Schedule | Manual |
|----------|------|----|---------| -------|
| CI | ✅ main/develop | ✅ main | Daily 03:00 UTC | ✅ |
| Deployment | ✅ main, tags | ❌ | ❌ | ✅ |
| Security | ✅ main/develop | ✅ main | Weekly Sun 02:00 | ✅ |
| Framework | ✅ .claude changes | ✅ .claude changes | Daily 04:00 UTC | ✅ |

## 🔍 Troubleshooting

### Common Issues

1. **Coverage Failures**
   - Ensure tests achieve 85% minimum coverage
   - Check for missing test files
   - Verify pytest-cov configuration

2. **Security Scan Failures**
   - Remove any hardcoded API keys or secrets
   - Ensure .env is properly gitignored
   - Check dependency vulnerabilities

3. **Framework Validation Failures**
   - Verify .claude directory structure
   - Check CLAUDE.md completeness
   - Validate PROJECT_CONFIG.xml syntax

4. **Deployment Failures**
   - Verify Railway token in repository secrets
   - Check railway.json configuration
   - Ensure start.sh is executable

### Manual Workflow Execution

To manually trigger workflows:

```bash
# Trigger CI workflow
gh workflow run "Continuous Integration"

# Trigger security audit
gh workflow run "Security Audit"

# Trigger framework validation
gh workflow run "Claude Code Framework Validation"

# Trigger deployment (production)
gh workflow run "Deployment Pipeline" -f environment=production
```

## 📈 Monitoring and Metrics

### Workflow Success Rates
Monitor workflow success rates to identify recurring issues:
- Aim for >95% success rate on main branch
- Address recurring failures promptly
- Review weekly security audit results

### Performance Metrics
- CI workflow: Target <10 minutes completion
- Security audit: Target <15 minutes completion
- Framework validation: Target <5 minutes completion
- Deployment: Target <5 minutes to complete

## 🔄 Maintenance

### Regular Tasks
- **Monthly**: Review and update dependency versions
- **Quarterly**: Update GitHub Actions versions (e.g., actions/checkout@v4)
- **As needed**: Adjust coverage thresholds and quality standards
- **After framework changes**: Update workflow validation criteria

### Version Updates
When updating framework versions:
1. Update `FRAMEWORK_VERSION` in claude-framework.yml
2. Update documentation references
3. Test all workflows with new version
4. Update this README if workflow changes are made

---

**Last Updated**: 2025-07-18  
**Framework Version**: 3.0.0  
**Workflows**: 4 active workflows with comprehensive validation