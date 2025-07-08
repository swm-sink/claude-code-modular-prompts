| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /protocol - Production-ready development with mandatory quality gates

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Production-ready development with MANDATORY quality gates">
  
  <delegation target="modules/quality/production-standards.md">
    Validate requirements → Enforce TDD → Apply security → Verify performance → Ensure compliance
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Create GitHub session for compliance tracking</step>
    <step>2. Validate ALL production requirements upfront</step>
    <step>3. ENFORCE TDD: No code without failing tests first</step>
    <step>4. Apply threat modeling from security modules</step>
    <step>5. Implement with performance benchmarks in mind</step>
    <step>6. Run ALL quality gates (coverage, security, performance)</step>
    <step>7. Generate compliance documentation automatically</step>
    <step>8. Block deployment if ANY gate fails</step>
  </thinking_pattern>
  
  <depends_on>
    quality/production-standards.md for complete protocol implementation
    quality/tdd.md for test-driven development standards
    security/threat-modeling.md for security analysis
    security/financial-compliance.md for regulatory requirements
    patterns/session-management.md for GitHub issue coordination
    patterns/pattern-library.md for proven execution patterns
    quality/error-recovery.md for resilient implementations
  </depends_on>
  
  <pattern_usage>
    • Uses tdd_cycle pattern for mandatory RED-GREEN-REFACTOR discipline
    • Applies explicit_validation for comprehensive error checking
    • Implements issue_tracking for complex production workflows
    • Leverages consequence_mapping for compliance impact analysis
    • Uses quality_gates pattern for production readiness validation
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/quality/production-standards.md for full implementation
  </pattern_usage>
  
  <usage_examples>
    /protocol "Implement wire transfer processing"      → Financial compliance
    /protocol "Add patient record system"               → Healthcare HIPAA
    /protocol "Make payment processing SOX compliant"   → Regulatory compliance
    /protocol "Build real-time trading platform"       → Critical systems
  </usage_examples>
  
  <strict_enforcement target="production_standards">
    <primary_rule>MUST satisfy ALL quality gates before production deployment</primary_rule>
    <verification>95% coverage + security scan + performance baseline + documentation complete</verification>
    <consequence>Production deployment blocked until all compliance requirements satisfied</consequence>
  </strict_enforcement>
  
  <escalation_triggers>
    <trigger condition="multi_system_integration">Complex integrations → escalate to /swarm</trigger>
    <trigger condition="regulatory_complexity">Multiple compliance frameworks → escalate to /swarm</trigger>
    <trigger condition="enterprise_deployment">Large-scale deployment → escalate to /swarm</trigger>
  </escalation_triggers>
  
  <quality_requirements>
    <requirement name="test_coverage">Minimum 95% coverage with quality assertions</requirement>
    <requirement name="security_scan">Automated security vulnerability assessment</requirement>
    <requirement name="performance_baseline">p95 < 200ms performance validation</requirement>
    <requirement name="compliance_check">Regulatory framework compliance verification</requirement>
    <requirement name="documentation">Complete API and deployment documentation</requirement>
  </quality_requirements>
  
</command>
```

────────────────────────────────────────────────────────────────────────────────

## Production Standards Enforcement

```xml
<production_enforcement>
  <mandatory_gates>TDD compliance | Security audit | Performance validation | Documentation complete</mandatory_gates>
  <compliance_frameworks>PCI DSS | SOX | HIPAA | GDPR | SOC2</compliance_frameworks>
  <quality_metrics>95% test coverage | Zero critical vulnerabilities | <200ms p95 performance</quality_metrics>
</production_enforcement>
```

────────────────────────────────────────────────────────────────────────────────

## Example

```xml
<protocol_usage>
  <financial>/protocol "Payment processing system" → PCI DSS compliance</financial>
  <healthcare>/protocol "Patient data management" → HIPAA compliance</healthcare>
  <enterprise>/protocol "Audit trail system" → SOX compliance</enterprise>
  <critical>/protocol "Real-time trading platform" → High availability standards</critical>
</protocol_usage>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Delegates to modules/quality/production-standards.md for complete implementation details including quality gate enforcement, compliance frameworks, and audit trail requirements.