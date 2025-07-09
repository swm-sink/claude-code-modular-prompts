| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-08   | stable |

# /protocol - Production-ready development with mandatory quality gates

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Production-ready development with MANDATORY quality gates">
  
  <delegation target="modules/quality/production-standards.md">
    Validate requirements → Enforce TDD → Apply security → Verify performance → Ensure compliance
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Production compliance decisions</uses_pattern>
    <uses_pattern from="patterns/tdd-cycle-pattern.md">Mandatory TDD enforcement</uses_pattern>
    <uses_pattern from="patterns/quality-validation-pattern.md">Production quality assurance</uses_pattern>
    <uses_pattern from="patterns/session-management-pattern.md">Compliance tracking and audit trail</uses_pattern>
    <uses_pattern from="patterns/integration-pattern.md">Production system integration</uses_pattern>
    <uses_pattern from="patterns/error-recovery-pattern.md">Production-grade error handling</uses_pattern>
    <uses_pattern from="patterns/performance-optimization-pattern.md">Production performance standards</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Create GitHub session for comprehensive compliance tracking</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What session creation approach optimizes compliance tracking?
          - What framework identification strategy supports production standards?
          - How does session creation connect to audit trail requirements and compliance success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Compliance Question: What compliance frameworks apply to this production system?]
          - [Complexity Question: How complex is this system requiring production standards?]
          - [Escalation Question: Should I escalate to /swarm for multi-system integration?]
          - [Audit Question: What audit trail requirements must be established?]
          - [Tracking Question: What compliance tracking ensures maximum production quality?]
          - [Framework Question: What framework identification optimizes compliance success?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this session creation optimal for compliance tracking?
          - What evidence supports the framework identification approach?
          - How will this session maximize compliance success and audit trail quality?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can session creation be combined with compliance analysis for efficiency?</tool_optimization>
        <context_efficiency>How can session creation optimize context window usage for compliance tracking?</context_efficiency>
        <dependency_analysis>What session creation is sequential vs parallel for compliance setup?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>COMPLIANCE_SESSION: #[number] tracking [frameworks] with [audit_requirements]</output_format>
      <validation>Session created with appropriate compliance tracking framework with enhanced reasoning</validation>
      <enforcement>BLOCK if compliance requirements unclear or session creation fails</enforcement>
      <context_transfer>Session creation and compliance framework for requirements validation</context_transfer>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Validate ALL production requirements with TDD methodology</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What requirements validation approach optimizes production quality?
          - What TDD methodology strategy supports regulatory compliance?
          - How does validation connect to production standards and testability?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Testability Question: Are requirements testable and measurable?]
          - [Compliance Question: What regulatory compliance must be verified through tests?]
          - [TDD Question: How will TDD validate security and performance requirements?]
          - [Criteria Question: Are acceptance criteria sufficient for production validation?]
          - [Validation Question: What validation approach ensures maximum production quality?]
          - [Methodology Question: What TDD methodology optimizes requirements validation?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this validation approach optimal for production requirements?
          - What evidence supports the TDD methodology strategy?
          - How will this validation maximize production quality and compliance?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can requirements validation be optimized for parallel analysis?</tool_optimization>
        <context_efficiency>How can validation optimize context window usage for production standards?</context_efficiency>
        <dependency_analysis>What validation is sequential vs parallel for TDD methodology?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>REQUIREMENTS_VALIDATION: [requirements] with TDD validation plan</output_format>
      <validation>All requirements validated as testable with clear TDD approach with enhanced reasoning</validation>
      <enforcement>BLOCK if requirements not testable or TDD plan incomplete</enforcement>
      <context_transfer>Requirements validation and TDD plan for enforcement</context_transfer>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>ENFORCE strict TDD: RED-GREEN-REFACTOR for production code</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What TDD enforcement approach optimizes production quality?
          - What RED-GREEN-REFACTOR strategy supports compliance requirements?
          - How does TDD enforcement connect to production standards and quality assurance?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Testing Question: Am I writing failing tests FIRST for all functionality?]
          - [Coverage Question: Do tests cover security requirements and edge cases?]
          - [Performance Question: Are performance tests included in TDD cycle?]
          - [Quality Question: Will TDD methodology ensure production quality?]
          - [Enforcement Question: What TDD enforcement ensures maximum production quality?]
          - [Compliance Question: What testing approach optimizes compliance validation?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this TDD enforcement optimal for production code?
          - What evidence supports the RED-GREEN-REFACTOR strategy?
          - How will this enforcement maximize production quality and compliance?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can TDD enforcement be optimized for parallel test development?</tool_optimization>
        <context_efficiency>How can enforcement optimize context window usage for production standards?</context_efficiency>
        <dependency_analysis>What TDD enforcement is sequential vs parallel for production quality?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TDD_ENFORCEMENT: RED tests written for [components] covering [compliance_areas]</output_format>
      <validation>Comprehensive failing tests written BEFORE any implementation with enhanced reasoning</validation>
      <enforcement>BLOCK any implementation before failing tests exist - use quality/tdd.md</enforcement>
      <context_transfer>TDD enforcement and testing for security validation</context_transfer>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply comprehensive threat modeling and security testing</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What threat modeling approach optimizes security validation?
          - What security testing strategy supports production compliance?
          - How does security modeling connect to TDD methodology and threat mitigation?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Threats Question: What security threats apply to this production system?]
          - [Controls Question: Are security controls testable through TDD?]
          - [Compliance Question: How do I validate compliance with security frameworks?]
          - [Integration Question: Are security tests part of the TDD cycle?]
          - [Modeling Question: What threat modeling ensures maximum security validation?]
          - [Testing Question: What security testing optimizes production compliance?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this threat modeling optimal for security validation?
          - What evidence supports the security testing strategy?
          - How will this modeling maximize security compliance and threat mitigation?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can threat modeling be optimized for parallel security analysis?</tool_optimization>
        <context_efficiency>How can modeling optimize context window usage for security validation?</context_efficiency>
        <dependency_analysis>What security modeling is sequential vs parallel for threat mitigation?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>SECURITY_VALIDATION: Threat model complete with security tests [implemented/verified]</output_format>
      <validation>Security threats identified and addressed through testable controls with enhanced reasoning</validation>
      <enforcement>BLOCK if threat model incomplete or security tests missing</enforcement>
      <context_transfer>Security validation and threat model for performance implementation</context_transfer>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Implement with performance benchmarks and TDD validation</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What implementation approach optimizes performance validation?
          - What TDD strategy supports performance benchmarking?
          - How does implementation connect to performance targets and test validation?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Requirements Question: Are performance requirements testable and measurable?]
          - [Testing Question: Do performance tests run as part of TDD cycle?]
          - [Target Question: Will implementation meet <200ms p95 performance target?]
          - [Regression Question: Are performance regression tests in place?]
          - [Implementation Question: What implementation approach ensures maximum performance validation?]
          - [Validation Question: What TDD validation optimizes performance benchmarking?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this implementation approach optimal for performance validation?
          - What evidence supports the TDD strategy for performance?
          - How will this implementation maximize performance targets and validation?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can implementation be optimized for parallel performance validation?</tool_optimization>
        <context_efficiency>How can implementation optimize context window usage for performance testing?</context_efficiency>
        <dependency_analysis>What implementation is sequential vs parallel for performance validation?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>PERFORMANCE_IMPLEMENTATION: Code with performance tests [passing/benchmarked]</output_format>
      <validation>Implementation meets performance requirements with test validation with enhanced reasoning</validation>
      <enforcement>BLOCK if performance targets not met or tests failing</enforcement>
      <context_transfer>Performance implementation and benchmarks for quality gate validation</context_transfer>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Validate ALL quality gates with comprehensive coverage</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What quality gate validation approach optimizes production standards?
          - What comprehensive coverage strategy supports deployment readiness?
          - How does validation connect to quality assurance and compliance requirements?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Coverage Question: Is test coverage ≥95% for production standards?]
          - [Security Question: Do all security scans pass with zero critical issues?]
          - [Performance Question: Are performance benchmarks met and documented?]
          - [Documentation Question: Is compliance documentation complete and auditable?]
          - [Validation Question: What quality gate validation ensures maximum production readiness?]
          - [Standards Question: What comprehensive coverage optimizes quality assurance?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this quality gate validation optimal for production standards?
          - What evidence supports the comprehensive coverage approach?
          - How will this validation maximize production readiness and compliance?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can quality gate validation be optimized for parallel coverage analysis?</tool_optimization>
        <context_efficiency>How can validation optimize context window usage for quality assurance?</context_efficiency>
        <dependency_analysis>What validation is sequential vs parallel for quality gate compliance?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>QUALITY_GATES: Coverage [%], Security [clean], Performance [met], Docs [complete]</output_format>
      <validation>All quality gates pass with documented evidence with enhanced reasoning</validation>
      <enforcement>BLOCK deployment if ANY quality gate fails - must resolve</enforcement>
      <context_transfer>Quality gate validation for compliance documentation</context_transfer>
    </checkpoint>
    <checkpoint id="7" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Generate compliance documentation with audit trail</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What documentation generation approach optimizes compliance validation?
          - What audit trail strategy supports regulatory requirements?
          - How does documentation connect to compliance frameworks and deployment readiness?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Generation Question: Is all compliance documentation automatically generated?]
          - [Audit Question: Are audit trails complete and tamper-evident?]
          - [Requirements Question: Will documentation satisfy regulatory requirements?]
          - [Artifacts Question: Are deployment artifacts properly signed and tracked?]
          - [Documentation Question: What documentation generation ensures maximum compliance validation?]
          - [Trail Question: What audit trail optimizes regulatory compliance?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this documentation generation optimal for compliance validation?
          - What evidence supports the audit trail strategy?
          - How will this documentation maximize regulatory compliance and deployment readiness?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can documentation generation be optimized for parallel compliance validation?</tool_optimization>
        <context_efficiency>How can generation optimize context window usage for audit trails?</context_efficiency>
        <dependency_analysis>What documentation is sequential vs parallel for compliance validation?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>COMPLIANCE_DOCS: Generated with [frameworks] compliance and audit trail</output_format>
      <validation>Complete compliance documentation with proper audit trails with enhanced reasoning</validation>
      <enforcement>BLOCK if documentation incomplete or audit trail insufficient</enforcement>
      <context_transfer>Complete compliance documentation with audit trail validation</context_transfer>
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