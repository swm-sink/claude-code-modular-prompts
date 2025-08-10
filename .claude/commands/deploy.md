---
name: deploy
description: Prepare and validate code for deployment
usage: "/deploy [--env production|staging] [--checklist]"
allowed-tools: [Read, Grep, Bash, WebSearch]
---

# Deployment Preparation

I'll ensure your code is ready for deployment.

## Pre-Deployment Checks

1. **Code Quality**
   - No console.logs or debug statements
   - No hardcoded secrets or API keys
   - No TODO/FIXME comments
   - All tests passing

2. **Security Audit**
   - Environment variables configured
   - Sensitive data protected
   - Dependencies up to date
   - No vulnerable packages

3. **Performance Review**
   - Bundle size check
   - Database queries optimized
   - Caching configured
   - Assets optimized

4. **Configuration**
   - Environment configs set
   - Build scripts verified
   - CI/CD pipeline ready
   - Rollback plan documented

## Deployment Checklist

I'll generate a custom checklist:
- [ ] Tests passing
- [ ] Lint clean
- [ ] Security scan complete
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] Changelog prepared
- [ ] Rollback tested

## Output

- Deployment readiness report
- Issues that need fixing
- Optimization suggestions
- Final checklist

Starting deployment validation...