| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Feature Workflow Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="feature_workflow" category="planning">
  
  <purpose>
    Execute comprehensive feature development workflow with PRD-first approach, MVP strategy, and iterative validation ensuring production-ready features.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Generate comprehensive PRD using planning/prd-generation.md patterns</step>
    <step>2. Auto-detect tech stack and existing patterns in codebase</step>
    <step>3. Create GitHub session for tracking ALWAYS</step>
    <step>4. Define MVP using planning/mvp-strategy.md with clear phases</step>
    <step>5. Calculate complexity: >15 score triggers delegation to /swarm</step>
    <step>6. Execute with TDD: Write ALL tests FIRST before implementation</step>
    <step>7. Apply quality gates from production-standards.md throughout</step>
    <step>8. Auto-generate documentation via development/documentation.md</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="explicit">User requests /feature command or feature development</condition>
    <condition type="automatic">Complex feature requirements detected requiring structured approach</condition>
  </trigger_conditions>
  
  <methodology enforcement="mandatory">
    
    <step name="prd_generation" order="1">
      <purpose>Generate comprehensive Product Requirements Document with stakeholder alignment</purpose>
      <requirements>
        Complete user story mapping with acceptance criteria
        Business value and success metrics clearly defined
        Technical feasibility assessment completed
        Stakeholder approval obtained before proceeding
      </requirements>
      <actions>
        Delegate to planning/prd-generation.md for manual PRD OR planning/intelligent-prd.md for autonomous PRD creation
        Ensure all PRD standards from planning/prd-core.md are followed
        Conduct stakeholder review and approval process
        Define clear success metrics and KPIs
        Document assumptions and constraints
      </actions>
      <validation>
        PRD document complete with all required sections
        Stakeholder sign-off obtained and documented
        Success metrics measurable and achievable
        Technical feasibility confirmed by architecture review
      </validation>
      <deliverables>
        Comprehensive PRD document with user stories
        Stakeholder approval documentation
        Success metrics and KPI definitions
        Technical architecture overview
      </deliverables>
    </step>
    
    <step name="mvp_strategy" order="2">
      <purpose>Define Minimum Viable Product with core functionality and implementation strategy</purpose>
      <requirements>
        Core functionality identified and prioritized
        Technical architecture designed and validated
        Resource requirements estimated accurately
        Implementation timeline established
      </requirements>
      <actions>
        Delegate to modules/planning/mvp-strategy.md for MVP definition
        Prioritize features using MoSCoW method
        Design technical architecture with scalability considerations
        Create implementation roadmap with milestones
      </actions>
      <validation>
        MVP scope clearly defined and agreed
        Technical architecture validated by peers
        Resource estimates realistic and achievable
        Implementation timeline approved by stakeholders
      </validation>
      <deliverables>
        MVP scope document with feature priorities
        Technical architecture design
        Resource allocation plan
        Implementation timeline with milestones
      </deliverables>
    </step>
    
    <step name="iterative_development" order="3">
      <purpose>Execute TDD-driven development with continuous feedback integration</purpose>
      <requirements>
        TDD cycle strictly followed throughout development
        Continuous integration with automated testing
        Regular stakeholder feedback integration
        Progressive enhancement approach maintained
      </requirements>
      <actions>
        Delegate to modules/testing/iterative-testing.md for TDD implementation
        Implement feature in small, testable increments
        Conduct regular stakeholder demos and feedback sessions
        Maintain high test coverage with quality assertions
      </actions>
      <validation>
        All code follows TDD RED-GREEN-REFACTOR cycle
        Test coverage maintained per quality/tdd.md standards throughout development
        Stakeholder feedback integrated at each iteration
        No regression bugs introduced during development
      </validation>
      <deliverables>
        Production-ready code with comprehensive test suite
        Stakeholder feedback integration documentation
        Test coverage reports and quality metrics
        Continuous integration pipeline configuration
      </deliverables>
    </step>
    
    <step name="feature_validation" order="4">
      <purpose>Comprehensive testing including user acceptance and performance validation</purpose>
      <requirements>
        All acceptance criteria validated through testing
        Performance requirements met and verified
        Security implications assessed and addressed
        User experience validated through testing
      </requirements>
      <actions>
        Delegate to modules/quality/production-standards.md for validation execution
        Execute comprehensive test suite including integration tests
        Conduct performance testing and optimization
        Perform security review and vulnerability assessment
      </actions>
      <validation>
        All acceptance criteria met and documented
        Performance benchmarks achieved and verified
        Security review completed with no critical issues
        User experience validated through testing scenarios
      </validation>
      <deliverables>
        Comprehensive test results and validation reports
        Performance benchmarks and optimization results
        Security review documentation
        User experience validation results
      </deliverables>
    </step>
    
    <step name="deployment_strategy" order="5">
      <purpose>Feature flag integration and rollout planning with monitoring capabilities</purpose>
      <requirements>
        Feature flag integration implemented
        Rollout strategy defined with rollback capabilities
        Monitoring and alerting configured
        Production deployment readiness confirmed
      </requirements>
      <actions>
        Implement feature flag integration for controlled rollout
        Configure monitoring and alerting for feature health
        Prepare rollback procedures and documentation
        Conduct production deployment readiness review
      </actions>
      <validation>
        Feature flags working correctly in all environments
        Monitoring and alerting properly configured
        Rollback procedures tested and documented
        Production deployment approved by stakeholders
      </validation>
      <deliverables>
        Feature flag configuration and documentation
        Monitoring and alerting setup
        Rollback procedures and documentation
        Production deployment approval
      </deliverables>
    </step>
    
  </methodology>
  
  <quality_gates enforcement="strict">
    <gate name="prd_approval" requirement="Complete PRD with stakeholder sign-off" blocking="true"/>
    <gate name="mvp_definition" requirement="Clear MVP scope with technical feasibility" blocking="true"/>
    <gate name="tdd_enforcement" requirement="Mandatory TDD enforcement per quality/tdd-enforcement.md" blocking="true"/>
    <gate name="security_verification" requirement="Security gate verification per quality/security-gate-verification.md" blocking="true"/>
    <gate name="performance_benchmarks" requirement="Performance gates per quality/performance-gates.md" blocking="true"/>
    <gate name="gate_verification" requirement="Comprehensive quality gate verification per quality/gate-verification.md" blocking="true"/>
    <gate name="user_acceptance" requirement="All acceptance criteria validated" blocking="true"/>
    <gate name="deployment_readiness" requirement="Production deployment approved" blocking="true"/>
  </quality_gates>
  
  <session_integration enforcement="automatic">
    <mandatory_conditions>
      All feature development automatically creates GitHub issue session
      Multi-phase development requiring systematic tracking
      Cross-component integration and coordination
    </mandatory_conditions>
    <session_documentation>
      PRD generation process and stakeholder approvals
      MVP strategy decisions and technical architecture
      Iterative development progress with test metrics
      Feature validation results and deployment readiness
      Lessons learned and process improvements
    </session_documentation>
  </session_integration>
  
  <escalation_logic>
    <trigger condition="stakeholder_conflict">Conflicting requirements → escalate to /swarm for resolution</trigger>
    <trigger condition="technical_complexity">Complex architecture → escalate to /swarm for specialist input</trigger>
    <trigger condition="cross_team_dependencies">Multiple team coordination → escalate to /swarm</trigger>
    <trigger condition="performance_constraints">System-wide optimization → escalate to /swarm</trigger>
  </escalation_logic>
  
  <integration_points>
    <depends_on>
      planning/prd-core.md for shared PRD standards and templates
      planning/prd-generation.md OR planning/intelligent-prd.md for PRD creation process
      planning/mvp-strategy.md for MVP definition methodology
      quality/tdd-enforcement.md for non-bypassable TDD enforcement
      quality/security-gate-verification.md for security verification
      quality/performance-gates.md for performance benchmarking
      quality/gate-verification.md for comprehensive quality gate orchestration
      quality/production-standards.md for validation procedures
      patterns/session-management.md for GitHub issue integration
    </depends_on>
    <provides_to>
      Commands/feature.md for complete feature development workflow
      quality/production-standards.md for feature quality requirements
      patterns/multi-agent.md for complex feature coordination
    </provides_to>
    <smart_planning_integration>
      <prd_mode_selection>Automatically selects between manual and intelligent PRD based on context complexity</prd_mode_selection>
      <quality_integration>All quality modules (tdd.md, feature-validation.md, production-standards.md) integrated at appropriate workflow steps</quality_integration>
      <pattern_integration>Leverages patterns/session-management.md for coordination and patterns/multi-agent.md for complex features</pattern_integration>
    </smart_planning_integration>
  </integration_points>
  
</module>
```