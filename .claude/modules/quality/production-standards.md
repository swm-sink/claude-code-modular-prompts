| version | last_updated | status |
|---------|--------------|--------|
| 1.1.0   | 2025-07-07   | stable |

# Production Standards Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="production_standards" category="quality">
  
  <purpose>
    Mandatory enterprise quality gates, security standards, and performance requirements for production-ready code.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Create GitHub session for compliance tracking</step>
    <step>2. Validate ALL production requirements upfront</step>
    <step>3. ENFORCE TDD: No code without failing tests first</step>
    <step>4. Apply threat modeling from security/threat-modeling.md</step>
    <step>5. Implement with performance benchmarks in mind</step>
    <step>6. Run ALL quality gates (coverage, security, performance)</step>
    <step>7. Generate compliance documentation automatically</step>
    <step>8. Block deployment if ANY gate fails</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="automatic">Production deployments, enterprise features, quality-focused development tasks</condition>
    <condition type="explicit">User requests production standards enforcement or enterprise compliance</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="pre_implementation_gates" order="1">
      <requirements>
        Requirements documented and approved with clear acceptance criteria
        Architecture design reviewed with security threat model completed
        Performance requirements defined with SLAs and monitoring strategy
      </requirements>
      <actions>
        Validate requirements documentation and stakeholder approval
        Review architecture design for scalability and security considerations
        Complete security threat model with identified mitigations
        Define performance SLAs and establish monitoring strategy with alerts
      </actions>
      <validation>
        GitHub session created with architecture decisions and security considerations
        Requirements clearly documented with measurable acceptance criteria
        Threat model completed with documented security controls
      </validation>
    </phase>
    
    <phase name="code_completion_gates" order="2">
      <requirements>
        TDD compliance as defined in quality/tdd.md#coverage_requirements
        Zero linting errors and complete type checking with security scan passed
        Comprehensive documentation with API docs and code comments
      </requirements>
      <actions>
        Enforce RED-GREEN-REFACTOR TDD cycle with session documentation
        Execute comprehensive testing: unit, integration, security scanning
        Perform peer code review with security-focused examination
        Update documentation: API specs, code comments, README, session notes
      </actions>
      <validation>
        All tests pass with coverage thresholds met and TDD compliance documented
        Zero linting errors, clean type checking, and security vulnerabilities resolved
        Documentation complete with API examples and implementation decisions
      </validation>
    </phase>
    
    <phase name="deployment_gates" order="3">
      <requirements>
        Security standards met with penetration testing and compliance verification
        Performance testing completed with SLA requirements satisfied
        Operational readiness confirmed with monitoring and runbooks prepared
      </requirements>
      <actions>
        Execute comprehensive security assessment with vulnerability scanning
        Perform load testing and stress testing to validate SLA compliance
        Configure health checks, graceful shutdown, and monitoring systems
        Prepare operational runbooks and backup/restore procedures
      </actions>
      <validation>
        Security assessment passed with compliance requirements verified
        Performance testing confirms SLA requirements met under load
        Operational systems ready with monitoring, alerts, and recovery procedures
      </validation>
    </phase>
    
  </implementation>
  
  <mandatory_quality_gates enforcement="strict">
    <gate name="tdd_compliance" requirement="Complete TDD compliance per quality/tdd.md#coverage_requirements and quality/tdd.md#quality_gates"/>
    <gate name="security_standards" requirement="Zero critical vulnerabilities, penetration test passed, threat model completed"/>
    <gate name="performance_slas" requirement="p95 response time under 200ms, load testing confirms capacity"/>
    <gate name="code_quality" requirement="Zero linting errors, complete type checking, peer review approved"/>
    <gate name="documentation" requirement="API documentation complete, code comments current, session updated"/>
    <gate name="operational_readiness" requirement="Monitoring configured, runbooks prepared, backup tested"/>
    <gate name="feature_validation" requirement="All validation requirements per quality/feature-validation.md#validation_checklists met"/>
    <gate name="predictive_analytics" requirement="Quality score prediction ≥85%, risk assessment completed, optimization applied"/>
    <gate name="automated_quality" requirement="Real-time quality monitoring active, automated remediation enabled"/>
  </mandatory_quality_gates>
  
  <security_standards grade="financial">
    <data_protection>
      <encryption>AES-256 at rest, TLS 1.3+ in transit, field-level for PII, HSM key management</encryption>
      <access_controls>Multi-factor authentication, RBAC, secure session management, audit logging</access_controls>
      <vulnerability_prevention>Parameterized queries, input sanitization, output encoding, modern cryptography</vulnerability_prevention>
    </data_protection>
    <compliance_frameworks>
      <gdpr>Data principles, user rights, privacy by design, consent management</gdpr>
      <pci_dss>No card storage, encrypted transmission, network segmentation, monitoring</pci_dss>
      <sox>Financial controls, audit trails, change management, access reviews</sox>
    </compliance_frameworks>
  </security_standards>
  
  <performance_requirements>
    <response_times>
      <api_endpoints>p50 under 100ms, p95 under 200ms, p99 under 500ms, 30s timeout maximum</api_endpoints>
      <web_pages>Initial load under 3s, interactive under 5s, LCP under 2.5s, CLS under 0.1</web_pages>
      <database_ops>Simple queries under 10ms, complex under 100ms, transactions under 50ms</database_ops>
    </response_times>
    <resource_limits>
      <compute>Memory under 512MB per instance, CPU under 80% sustained, efficient resource usage</compute>
      <database>Connection pooling, 30s query timeout, 60s transaction timeout, 5min idle timeout</database>
      <external_services>Circuit breakers, conservative timeouts with retries, graceful degradation</external_services>
    </resource_limits>
  </performance_requirements>
  
  <context_aware_validation>
    <native_error_messaging>
      <context_adaptation>Error messages adapt to request complexity and user context</context_adaptation>
      <memory_optimization>Token-efficient error reporting for 200k window</memory_optimization>
      <recovery_guidance>Smart suggestions based on Claude Code native capabilities</recovery_guidance>
      <complexity_awareness>
        <simple_requests>Lightweight validation, minimal overhead, direct guidance</simple_requests>
        <complex_requests>Comprehensive validation with predictive analysis and escalation guidance</complex_requests>
        <multi_agent_work>Session-based validation with coordination checks and context preservation</multi_agent_work>
      </complexity_awareness>
    </native_error_messaging>
    
    <predictive_quality_gates>
      <complexity_prediction>Predict quality gate requirements based on request analysis</complexity_prediction>
      <escalation_triggers>Automatic escalation based on predictive analytics</escalation_triggers>
      <context_optimization>Quality gates that optimize for 200k token window</context_optimization>
      <success_probability>Calculate success likelihood for different approaches</success_probability>
      <resource_allocation>Predict context window requirements for quality validation</resource_allocation>
    </predictive_quality_gates>
    
    <real_time_quality_monitoring>
      <execution_analytics>Monitor quality metrics during task execution</execution_analytics>
      <predictive_intervention>Intervene before quality degradation occurs</predictive_intervention>
      <adaptive_quality_gates>Adjust quality requirements based on complexity analysis</adaptive_quality_gates>
      <success_optimization>Optimize approach based on predicted success probability</success_optimization>
    </real_time_quality_monitoring>
    
    <intelligent_validation_routing>
      <context_complexity_scoring>
        <simple_validation>Basic checks for straightforward requests (< 5 operations)</simple_validation>
        <moderate_validation>Enhanced checks with pattern analysis (5-15 operations)</moderate_validation>
        <comprehensive_validation>Full quality suite with predictive analytics (15+ operations)</comprehensive_validation>
      </context_complexity_scoring>
      <validation_pattern_selection>
        <lightweight>Fast validation for simple changes with minimal quality impact</lightweight>
        <standard>Normal validation suite for typical development work</standard>
        <enterprise>Full production standards for critical/complex implementations</enterprise>
      </validation_pattern_selection>
      <predictive_validation_enhancement>
        <quality_score_prediction>Predict final quality score before execution begins</quality_score_prediction>
        <risk_assessment>Analyze risk factors and recommend mitigation strategies</risk_assessment>
        <optimization_recommendations>Suggest approach optimizations based on analytics</optimization_recommendations>
        <automated_quality_remediation>Automatically apply quality improvements during execution</automated_quality_remediation>
      </predictive_validation_enhancement>
    </intelligent_validation_routing>
  </context_aware_validation>

  <error_handling_standards>
    <exception_hierarchy>
      <business_errors>Custom exceptions for domain-specific error conditions</business_errors>
      <validation_errors>Input validation failures with detailed field-level feedback</validation_errors>
      <system_errors>Infrastructure and external service failures with recovery guidance</system_errors>
      <security_errors>Authentication and authorization failures with audit logging</security_errors>
    </exception_hierarchy>
    <response_format>
      <structure>Error code, human-friendly message, context details, request ID, help link</structure>
      <logging>Structured JSON logs with correlation IDs and full context preservation</logging>
      <alerting>Critical errors trigger immediate alerts with escalation procedures</alerting>
    </response_format>
  </error_handling_standards>
  
  <monitoring_requirements>
    <golden_signals>
      <latency>Response time distribution: p50, p95, p99 percentiles</latency>
      <traffic>Requests per second with trend analysis and capacity planning</traffic>
      <errors>Error rate percentage with breakdown by type and severity</errors>
      <saturation>Resource utilization with proactive capacity alerts</saturation>
    </golden_signals>
    <business_metrics>
      <user_actions>Key user flow completion rates and conversion tracking</user_actions>
      <transactions>Business transaction volumes with financial impact analysis</transactions>
      <features>Feature adoption rates and usage pattern analysis</features>
    </business_metrics>
    <alerting_rules>
      <error_rate>Alert when error rate exceeds 1% for 5 minutes</error_rate>
      <response_time>Alert when p95 response time exceeds 500ms for 10 minutes</response_time>
      <external_deps>Alert when external service error rate exceeds 50% for 2 minutes</external_deps>
    </alerting_rules>
  </monitoring_requirements>
  
  <deployment_process>
    <blue_green_deployment>
      <canary_phases>5% traffic for 15 minutes, 25% for 30 minutes, 100% for 60 minutes</canary_phases>
      <success_criteria>Error rate under 0.5%, p95 response time under 200ms, stable business metrics</success_criteria>
      <rollback_triggers>Error rate over 2%, response time over 500ms p95, business metric drop over 10%</rollback_triggers>
    </blue_green_deployment>
    <quality_verification>
      <pre_deployment>All quality gates verified, performance benchmarks met, security scan passed</pre_deployment>
      <during_deployment>Real-time monitoring with automated rollback on threshold breaches</during_deployment>
      <post_deployment>Verification of monitoring systems and performance within SLA</post_deployment>
    </quality_verification>
  </deployment_process>
  
  <session_integration>
    <compliance_tracking>
      <development_audit>All code changes linked to sessions, review approvals documented</development_audit>
      <quality_evidence>Test results preserved with timestamps, TDD compliance tracked</quality_evidence>
      <security_audit>Scan results preserved for 3 years, incident response documented</security_audit>
      <change_management>Production changes approved and logged with complete audit trail</change_management>
    </compliance_tracking>
    <session_lifecycle>
      <pre_development>Requirements analysis, architecture decisions, security considerations</pre_development>
      <during_development>TDD progress, quality gate results, code review feedback</during_development>
      <pre_deployment>Quality gates passed, performance testing, security approval</pre_deployment>
      <post_deployment>Deployment results, monitoring confirmation, lessons learned</post_deployment>
    </session_lifecycle>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for compliance tracking sessions
      security/financial-compliance.md for enterprise security standards
      quality/tdd.md for test-driven development enforcement
      development/prompt-engineering.md for prompt quality standards
      quality/error-recovery.md for analytics-driven quality optimization
      quality/error-recovery.md for resilient quality assurance workflows
    </depends_on>
    <provides_to>
      development/task-management.md for quality gate integration
      quality/production-standards.md for enhanced enterprise standards
      development/prompt-engineering.md for production prompt standards
      quality/error-recovery.md for quality-aware escalation decisions
      All commands for mandatory production quality enforcement with predictive capabilities
    </provides_to>
  </integration_points>
  
</module>
```