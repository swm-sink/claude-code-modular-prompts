| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-08   | stable |


# Quality Gates & Production Standards

> **Comprehensive Guide**: Quality gates, production standards, TDD enforcement, security requirements, and performance standards all in one place.


# Overview

The Claude Code Framework implements a comprehensive quality system with automated gates and production standards that ensure consistent, high-quality software delivery across all development activities.


# What Are Quality Gates?

Quality gates are **non-bypassable validation checkpoints** that:
- Automatically enforce quality standards during development
- Block progression when quality criteria aren't met
- Provide clear feedback on what needs to be fixed
- Generate audit trails for compliance and improvement


# Key Benefits

- **Consistent Quality**: Every commit meets the same high standards
- **Early Detection**: Issues caught immediately, not in production
- **Reduced Technical Debt**: Quality built-in from the start
- **Compliance Ready**: Automated evidence collection and audit trails
- **Developer Productivity**: Clear guidance on what's required


# Quality Gate Categories


# 1. Foundational Gates
Applied to **ALL commands** - basic quality requirements every operation must satisfy.

- **Critical Thinking Validation**: 30-second minimum analysis with documented alternatives
- **Requirement Clarity**: Clear, testable requirements with measurable success criteria  
- **Module Integration Compliance**: Proper module usage and dependency management
- **Error Handling Completeness**: Comprehensive error scenarios and recovery mechanisms


# 2. Development Gates
Applied to code modification commands (`/task`, `/swarm`, `/feature`, `/protocol`).

- **TDD Cycle Compliance**: Strict RED-GREEN-REFACTOR enforcement
- **Code Quality Standards**: Linting, complexity limits, maintainability
- **Security Requirements**: Threat modeling and vulnerability prevention
- **Performance Validation**: Response time and resource usage requirements


# 3. Coordination Gates
Applied to multi-component commands (`/swarm`, `/feature`, `/protocol`).

- **Multi-Agent Synchronization**: Clear agent boundaries and coordination protocols
- **Session Tracking Completeness**: Progress tracking and context preservation
- **Integration Validation**: End-to-end system validation


# 4. Documentation Gates
Applied to documentation commands (`/docs`) and development with documentation.

- **Documentation Standards Compliance**: Framework 3.0 format and content standards
- **TDD Methodology Documentation**: Proper TDD references and workflow examples


# 5. Analysis Gates
Applied to research commands (`/query`, `/auto` routing decisions).

- **Research Comprehensiveness**: Thorough analysis with evidence-based conclusions
- **Routing Decision Quality**: Sound complexity assessment and command selection


# Production Standards & Requirements


# Before Code Complete
```
✓ All tests passing
✓ Coverage ≥90%
✓ Zero linting errors
✓ Type checking passes
✓ Documentation updated
✓ Session shows TDD compliance
```


# Before Deployment
```
✓ Security scan passed
✓ Performance validated
✓ Error handling complete
✓ Monitoring configured
✓ Rollback plan ready
✓ Session completed with outcomes
```


# Command-Specific Gate Configuration


# `/task` Command Gates

**Required Gates**: Foundational + Development  
**Enforcement**: BLOCKING

```xml
<universal_quality_gates enforcement = "MANDATORY">
  <gate_set>task_command_gates</gate_set>
  <blocking_conditions>
    <condition>TDD cycle not completed (RED-GREEN-REFACTOR)</condition>
    <condition>Test coverage below 90%</condition>
    <condition>Security threats not mitigated</condition>
    <condition>Performance requirements not met</condition>
  </blocking_conditions>
</universal_quality_gates>
```


# `/swarm` Command Gates

**Required Gates**: Foundational + Development + Coordination  
**Enforcement**: BLOCKING

```xml
<universal_quality_gates enforcement = "MANDATORY">
  <gate_set>swarm_command_gates</gate_set>
  <blocking_conditions>
    <condition>Agent coordination conflicts detected</condition>
    <condition>Integration tests failing</condition>
    <condition>Session tracking incomplete</condition>
    <condition>TDD compliance violations across agents</condition>
  </blocking_conditions>
</universal_quality_gates>
```


# `/protocol` Command Gates

**Required Gates**: ALL categories (strictest enforcement)  
**Enforcement**: BLOCKING

```xml
<universal_quality_gates enforcement = "MANDATORY">
  <gate_set>protocol_command_gates</gate_set>
  <blocking_conditions>
    <condition>ANY quality gate failure</condition>
    <condition>Production standards not met</condition>
    <condition>Compliance requirements violated</condition>
    <condition>Security audit findings unresolved</condition>
  </blocking_conditions>
</universal_quality_gates>
```


# TDD Standards & Enforcement


# Core TDD Requirements

```xml
<tdd_enforcement>
  <red_phase_validation>
    <check>Tests written before implementation</check>
    <check>Tests fail for expected reasons</check>
    <check>All acceptance criteria covered</check>
  </red_phase_validation>
  <green_phase_validation>
    <check>Minimal implementation passes tests</check>
    <check>No premature optimization</check>
    <check>Coverage thresholds met</check>
  </green_phase_validation>
  <refactor_phase_validation>
    <check>Tests remain green throughout</check>
    <check>Code quality improved</check>
    <check>No behavior changes</check>
  </refactor_phase_validation>
</tdd_enforcement>
```


# Test Structure
```bash
tests/
├── unit/           # Fast, isolated tests
├── integration/    # Component interaction tests  
├── e2e/           # End-to-end workflow tests
└── fixtures/      # Test data and mocks
```

**Test Distribution**: 70% unit, 20% integration, 10% E2E


# Security Requirements


# Data Protection
```yaml
mandatory_for_sensitive_data:
  - Encryption at rest (AES-256)
  - Encryption in transit (TLS 1.3+)
  - Field-level encryption for PII
  - Secure key management
```


# Authentication & Authorization
```yaml
required_patterns:
  - Multi-factor authentication
  - Role-based access control
  - Session management
  - Rate limiting
  - Audit logging
```


# Security Gates Configuration
```xml
<security_gates>
  <threat_modeling>
    <methodology>STRIDE (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation)</methodology>
    <requirement>Threat model before external interface changes</requirement>
    <validation>Security controls mapped to identified threats</validation>
  </threat_modeling>
  <vulnerability_scanning>
    <tools>SAST, dependency scanning, secrets detection</tools>
    <blocking_threshold>Zero HIGH, max 5 MEDIUM severity issues</blocking_threshold>
    <frequency>Every commit for SAST, daily for dependencies</frequency>
  </vulnerability_scanning>
</security_gates>
```


# Performance Standards


# Response Time Requirements
- **API Endpoints**: <200ms (p95)
- **Web Pages**: <3s initial load
- **Database Queries**: <100ms
- **Background Jobs**: SLA defined


# Resource Usage Limits
```yaml
limits:
  memory: <512MB per instance
  cpu: <80% sustained
  connections: Pooled and limited
  disk: Monitored and alerted
```


# Performance Gates Configuration
```xml
<performance_gates>
  <response_time_requirements>
    <api_endpoints>p50 < 100ms, p95 < 200ms, p99 < 500ms</api_endpoints>
    <web_pages>LCP < 2.5s, FID < 100ms, CLS < 0.1</web_pages>
    <background_tasks>Complete within 30s or provide progress updates</background_tasks>
  </response_time_requirements>
  <resource_requirements>
    <memory>< 512MB sustained, < 1GB peak</memory>
    <cpu>< 80% sustained under normal load</cpu>
    <database>Query timeout 30s, transaction timeout 60s</database>
  </resource_requirements>
</performance_gates>
```


# Error Handling Standards


# Comprehensive Coverage
```python
try:
    result = risky_operation()
except SpecificError as e:
    # Specific handling
    log_error(e, context)
    return graceful_fallback()
except Exception as e:
    # Generic handling
    alert_oncall(e)
    return safe_default()
finally:
    # Cleanup always runs
    release_resources()
```


# Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User-friendly message",
    "details": {...},
    "request_id": "uuid",
    "help": "link_to_docs"
  }
}
```


# Common Gate Failures and Solutions


# TDD Violations

**Problem**: Implementation written before tests
```
❌ TDD violation: Implementation written before tests. Restarting with RED phase.
```

**Solution**:
1. Delete the implementation code
2. Write failing tests that specify the expected behavior
3. Verify tests fail for the right reasons
4. Implement minimal code to make tests pass


# Security Gate Failures

**Problem**: Missing threat model
```
❌ Security gate failure: Threat model required for external interface changes
```

**Solution**:
1. Identify the external interfaces (APIs, file uploads, user inputs)
2. Apply STRIDE methodology to each interface
3. Document identified threats and mitigations
4. Implement security controls for each threat


# Performance Gate Failures

**Problem**: Response time exceeds requirements
```
❌ Performance gate failure: p95 response time 350ms exceeds 200ms requirement
```

**Solution**:
1. Identify performance bottlenecks through profiling
2. Optimize database queries, caching, or algorithms
3. Add performance tests to prevent regression
4. Re-run benchmarks to verify improvements


# Monitoring & Observability


# Required Metrics
```python

# Business metrics
- User actions
- Transaction volumes
- Error rates
- Success rates


# Technical metrics  
- Response times
- Resource usage
- Queue depths
- Cache hit rates
```


# Logging Standards
```python
logger.info("action_completed", 
    user_id=user.id,
    action="purchase",
    amount=100.00,
    duration_ms=45
)
```


# Alerting Rules
```yaml
- metric: error_rate > 1%
  window: 5m
  severity: warning

- metric: response_time_p95 > 500ms  
  window: 10m
  severity: critical
```


# Deployment Standards


# Pre-deployment Checklist
```
□ Feature flags configured
□ Database migrations tested
□ Performance benchmarked
□ Security scan completed
□ Documentation updated
□ AI session linked to deployment
```


# Deployment Process
```
□ Blue-green deployment
□ Canary rollout (5% → 25% → 100%)
□ Health checks passing
□ Metrics normal
□ No error spike
```


# Post-deployment
```
□ Monitor metrics for 30min
□ Check error rates
□ Verify performance
□ Update status page
□ Notify stakeholders
□ Update session with deployment results
```


# CI/CD Integration


# Pre-Commit Hooks
```bash
#!/bin/bash

# .git/hooks/pre-commit


# TDD Validation
echo "Validating TDD compliance..."
if ! ./scripts/validate-tdd.sh; then
  echo "❌ TDD validation failed"
  exit 1
fi


# Security Scanning
echo "Running security scans..."
if ! ./scripts/security-scan.sh; then
  echo "❌ Security scan failed"
  exit 1
fi


# Performance Tests
echo "Running performance tests..."
if ! ./scripts/performance-test.sh; then
  echo "❌ Performance tests failed"
  exit 1
fi

echo "✅ All quality gates passed"
```


# GitHub Actions Integration
```yaml
name: Quality Gates
on: [push, pull_request]

jobs:
  quality-gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: TDD Validation
        run: ./scripts/validate-tdd.sh
        
      - name: Security Scanning
        run: ./scripts/security-scan.sh
        
      - name: Performance Testing
        run: ./scripts/performance-test.sh
        
      - name: Generate Quality Report
        run: ./scripts/generate-quality-report.sh
```


# Best Practices


# Core Principles
1. **Fail Safe**: Default to secure state
2. **Defense in Depth**: Multiple layers
3. **Least Privilege**: Minimal access
4. **Audit Everything**: Complete trail
5. **Monitor Proactively**: Alert before issues
6. **Track Development**: AI sessions for context
7. **Link Everything**: Sessions to PRs to deployments


# Quality Gate Customization
```xml
<!-- For legacy systems -->
<tdd_integration relaxed = "true">
  <coverage_requirement>70% minimum (gradually increase)</coverage_requirement>
  <legacy_code_exception>Wrapper tests acceptable for legacy integration</legacy_code_exception>
</tdd_integration>

<!-- For high-security systems -->
<security_gates strict = "true">
  <vulnerability_threshold>Zero HIGH, zero MEDIUM</vulnerability_threshold>
  <penetration_testing>Required for all external interfaces</penetration_testing>
  <compliance_frameworks>SOX, PCI-DSS, HIPAA</compliance_frameworks>
</security_gates>
```


# Compliance Requirements


# Data Privacy (GDPR)
- Data minimization
- Purpose limitation  
- Consent management
- Right to deletion
- Audit trail


# Financial (PCI DSS)
- No card data storage
- Tokenization required
- Network segmentation
- Access logging
- Regular audits


# Implementation Support

For detailed implementation support, refer to:
- **TDD Module**: `.claude/modules/quality/tdd.md`
- **Universal Quality Gates**: `.claude/modules/quality/universal-quality-gates.md`
- **Security Module**: `.claude/modules/security/threat-modeling.md`
- **Framework Documentation**: `docs/framework/`

**Quality is not an act, but a habit.** - Build it into every step of your development process.