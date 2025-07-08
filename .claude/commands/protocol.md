| version | last_updated | status |
|---------|--------------|--------|
| 2.4.1   | 2025-07-08   | stable |

# /protocol - Production-ready development with mandatory quality gates

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Production-ready development with MANDATORY quality gates">
  
  <delegation target="modules/quality/production-standards.md">
    Validate requirements → Enforce TDD → Apply security → Verify performance → Ensure compliance
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Create GitHub session for comprehensive compliance tracking</action>
      <critical_thinking>
        - What compliance frameworks apply to this production system?
        - How complex is this system requiring production standards?
        - Should I escalate to /swarm for multi-system integration?
        - What audit trail requirements must be established?
      </critical_thinking>
      <output_format>COMPLIANCE_SESSION: #[number] tracking [frameworks] with [audit_requirements]</output_format>
      <validation>Session created with appropriate compliance tracking framework</validation>
      <enforcement>BLOCK if compliance requirements unclear or session creation fails</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Validate ALL production requirements with TDD methodology</action>
      <critical_thinking>
        - Are requirements testable and measurable?
        - What regulatory compliance must be verified through tests?
        - How will TDD validate security and performance requirements?
        - Are acceptance criteria sufficient for production validation?
      </critical_thinking>
      <output_format>REQUIREMENTS_VALIDATION: [requirements] with TDD validation plan</output_format>
      <validation>All requirements validated as testable with clear TDD approach</validation>
      <enforcement>BLOCK if requirements not testable or TDD plan incomplete</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>ENFORCE strict TDD: RED-GREEN-REFACTOR for production code</action>
      <critical_thinking>
        - Am I writing failing tests FIRST for all functionality?
        - Do tests cover security requirements and edge cases?
        - Are performance tests included in TDD cycle?
        - Will TDD methodology ensure production quality?
      </critical_thinking>
      <output_format>TDD_ENFORCEMENT: RED tests written for [components] covering [compliance_areas]</output_format>
      <validation>Comprehensive failing tests written BEFORE any implementation</validation>
      <enforcement>BLOCK any implementation before failing tests exist - use quality/tdd.md</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Apply comprehensive threat modeling and security testing</action>
      <critical_thinking>
        - What security threats apply to this production system?
        - Are security controls testable through TDD?
        - How do I validate compliance with security frameworks?
        - Are security tests part of the TDD cycle?
      </critical_thinking>
      <output_format>SECURITY_VALIDATION: Threat model complete with security tests [implemented/verified]</output_format>
      <validation>Security threats identified and addressed through testable controls</validation>
      <enforcement>BLOCK if threat model incomplete or security tests missing</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Implement with performance benchmarks and TDD validation</action>
      <critical_thinking>
        - Are performance requirements testable and measurable?
        - Do performance tests run as part of TDD cycle?
        - Will implementation meet <200ms p95 performance target?
        - Are performance regression tests in place?
      </critical_thinking>
      <output_format>PERFORMANCE_IMPLEMENTATION: Code with performance tests [passing/benchmarked]</output_format>
      <validation>Implementation meets performance requirements with test validation</validation>
      <enforcement>BLOCK if performance targets not met or tests failing</enforcement>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING">
      <action>Validate ALL quality gates with comprehensive coverage</action>
      <critical_thinking>
        - Is test coverage ≥95% for production standards?
        - Do all security scans pass with zero critical issues?
        - Are performance benchmarks met and documented?
        - Is compliance documentation complete and auditable?
      </critical_thinking>
      <output_format>QUALITY_GATES: Coverage [%], Security [clean], Performance [met], Docs [complete]</output_format>
      <validation>All quality gates pass with documented evidence</validation>
      <enforcement>BLOCK deployment if ANY quality gate fails - must resolve</enforcement>
    </checkpoint>
    <checkpoint id="7" verify="true" enforcement="BLOCKING">
      <action>Generate compliance documentation with audit trail</action>
      <critical_thinking>
        - Is all compliance documentation automatically generated?
        - Are audit trails complete and tamper-evident?
        - Will documentation satisfy regulatory requirements?
        - Are deployment artifacts properly signed and tracked?
      </critical_thinking>
      <output_format>COMPLIANCE_DOCS: Generated with [frameworks] compliance and audit trail</output_format>
      <validation>Complete compliance documentation with proper audit trails</validation>
      <enforcement>BLOCK if documentation incomplete or audit trail insufficient</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <tdd_integration enforcement="MANDATORY">
    <production_tdd>Strictest TDD enforcement for production systems with ≥95% coverage</production_tdd>
    <compliance_testing>All regulatory requirements must be validated through automated tests</compliance_testing>
    <security_tdd>Security controls implemented through test-driven security methodology</security_tdd>
    <performance_tdd>Performance requirements validated through TDD with benchmark tests</performance_tdd>
    <validation>Reference quality/tdd.md#production_standards for strictest TDD enforcement</validation>
    <blocking_conditions>
      <condition>Any production code without comprehensive test coverage</condition>
      <condition>Implementation before failing tests exist</condition>
      <condition>Security controls not validated through tests</condition>
      <condition>Performance requirements not verified through automated tests</condition>
      <condition>Compliance requirements not testable or not tested</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before production development</module>
      <module>patterns/session-management.md - GitHub compliance tracking session</module>
      <module>quality/production-standards.md - Comprehensive production quality gates</module>
      <module>quality/tdd.md - Strictest TDD enforcement for production code</module>
      <module>security/threat-modeling.md - Security analysis and testing</module>
      <module>quality/pre-commit.md - Production-grade pre-commit validation</module>
    </core_stack>
    <contextual_modules>
      <conditional module="security/financial-compliance.md" condition="financial_system"/>
      <conditional module="patterns/multi-agent.md" condition="complex_system OR escalation_needed"/>
      <conditional module="development/code-review.md" condition="production_deployment"/>
      <conditional module="quality/error-recovery.md" condition="critical_system_failure"/>
    </contextual_modules>
  </module_execution>
  
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
  

  <prompt_construction>
    <assembly_preview>
      WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. Session     │ → Compliance tracking
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Creation    │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. Requirements│ → TDD validation
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Validation  │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. TDD         │ → Strictest enforcement
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Enforcement │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. Security    │ → Threat modeling
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Analysis    │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. Performance │ → Benchmark validation
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Validation  │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 6. Quality     │ → Production gates
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Gates       │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 7. Compliance  │ → Audit documentation
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Docs        │
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~20,000
      - Session & compliance: 2,000
      - Requirements validation: 2,500
      - TDD enforcement: 6,000
      - Security analysis: 3,000
      - Performance validation: 2,500
      - Quality gates: 2,000
      - Compliance docs: 2,000
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /protocol "Payment processing"
      [00:30] 🎯 SESSION: Compliance tracking #159 created
      [00:45] ✅ REQUIREMENTS: All validated as testable
      [01:00] 🔴 TDD: Writing comprehensive failing tests...
      [01:30] ✅ TDD: Implementation with 98% coverage
      [01:45] 🔒 SECURITY: Threat model completed, all clear
      [02:00] ⚡ PERFORMANCE: <150ms p95 achieved
      [02:15] 🎯 QUALITY: All production gates passed
      [02:30] 📋 COMPLIANCE: Audit trail documented
      [02:45] ✅ COMPLETE: Production-ready with compliance
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Reads checkpoint structure sequentially
      2. Executes critical_thinking questions internally
      3. Formats output according to output_format specifications
      4. Validates against enforcement rules before proceeding
      5. Applies parallel execution optimization where possible
    </parsing_behavior>

    <decision_points>
      - Checkpoint failures trigger enforcement actions
      - Module selection based on contextual conditions
      - Parallel execution for independent operations
      - Quality gate validation at completion boundaries
      - Error recovery through graceful degradation paths
    </decision_points>
  </claude_4_interpretation>

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