<module name="feature_workflow" category="development">
  
  <purpose>
    Execute comprehensive feature development workflow with PRD-first approach, MVP strategy, and iterative validation ensuring production-ready features.
  </purpose>
  
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
        Delegate to modules/development/prd-generation.md for PRD creation
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
        Delegate to modules/development/mvp-strategy.md for MVP definition
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
        Delegate to modules/development/iterative-testing.md for TDD implementation
        Implement feature in small, testable increments
        Conduct regular stakeholder demos and feedback sessions
        Maintain high test coverage with quality assertions
      </actions>
      <validation>
        All code follows TDD RED-GREEN-REFACTOR cycle
        Test coverage maintained above 90% throughout development
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
        Delegate to modules/quality/feature-validation.md for validation execution
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
    <gate name="prd_approval" requirement="Complete PRD with stakeholder sign-off"/>
    <gate name="mvp_definition" requirement="Clear MVP scope with technical feasibility"/>
    <gate name="tdd_compliance" requirement="Full TDD cycle with 90% test coverage"/>
    <gate name="security_review" requirement="Security implications assessed and resolved"/>
    <gate name="performance_validation" requirement="Performance requirements met and verified"/>
    <gate name="user_acceptance" requirement="All acceptance criteria validated"/>
    <gate name="deployment_readiness" requirement="Production deployment approved"/>
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
      development/prd-generation.md for PRD creation process
      development/mvp-strategy.md for MVP definition methodology
      development/iterative-testing.md for TDD implementation
      quality/feature-validation.md for validation procedures
      patterns/session-management.md for GitHub issue integration
    </depends_on>
    <provides_to>
      Commands/feature.md for complete feature development workflow
      quality/production-standards.md for feature quality requirements
      patterns/multi-agent.md for complex feature coordination
    </provides_to>
  </integration_points>
  
</module>