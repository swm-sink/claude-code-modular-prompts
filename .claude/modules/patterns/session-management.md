<module name="session_management" category="patterns">
  
  <purpose>
    Intelligent GitHub issue-based session management for AI development context tracking and coordination.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Multi-agent work, complex tasks (3+ components), enterprise features</condition>
    <condition type="explicit">User requests session creation or complex task tracking</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="session_decision" order="1">
      <requirements>
        Task complexity assessed against mandatory, conditional, and optional thresholds
        Session type determined based on work category and tracking requirements
        AWARE framework integration planned for comprehensive context tracking
      </requirements>
      <actions>
        Apply session decision logic based on complexity, components, and command type
        Determine appropriate session type (multi-agent, development, research, security, enterprise)
        Plan AWARE framework integration for structured context tracking
        Assess audit trail requirements for compliance tracking
      </actions>
      <validation>
        Session decision justified by complexity analysis and tracking requirements
        Session type appropriate for work category and expected outcomes
        AWARE framework integration planned for systematic progress tracking
      </validation>
    </phase>
    
    <phase name="session_creation" order="2">
      <requirements>
        GitHub issue created with appropriate template and label configuration
        Session tracking capabilities established for progress monitoring
        Integration points configured for command and module coordination
      </requirements>
      <actions>
        Create GitHub issue using selected template with proper labels
        Configure session tracking for milestones, decisions, and blockers
        Establish integration with commands for automatic progress updates
        Setup compliance monitoring if required for regulatory work
      </actions>
      <validation>
        GitHub session created with correct template and labels
        Session tracking configured for comprehensive progress monitoring
        Integration points active for automatic updates from commands and modules
      </validation>
    </phase>
    
    <phase name="session_lifecycle" order="3">
      <requirements>
        Progress tracking maintained throughout work execution
        Session documentation updated with key decisions and milestones
        Session completion includes comprehensive outcome documentation
      </requirements>
      <actions>
        Track progress through automated updates from executing commands
        Document key architectural and implementation decisions
        Monitor quality gates and compliance checkpoints
        Complete session with outcome summary and lessons learned
      </actions>
      <validation>
        Session provides complete audit trail of work progression
        Key decisions documented with context and rationale
        Session completion includes comprehensive results and follow-up actions
      </validation>
    </phase>
    
  </implementation>
  
  <session_decision_logic>
    <mandatory_creation>
      /swarm commands always create sessions for multi-agent coordination
      Multi-component work affecting 3+ system components requires tracking
      System architecture changes requiring comprehensive documentation
      Compliance work requiring complete audit trail for regulatory purposes
    </mandatory_creation>
    <conditional_creation>
      Medium complexity tasks where tracking provides significant value
      Enterprise features with architectural implications requiring documentation
      Development work benefiting from progress tracking and decision documentation
    </conditional_creation>
    <optional_creation>
      Simple fixes with minimal scope and immediate completion
      Research queries focused on immediate development decisions
      Single-component modifications with clear and limited scope
    </optional_creation>
  </session_decision_logic>
  
  <session_types>
    <multi_agent_sessions>
      Purpose: Coordinate parallel work across multiple specialized agents
      Template: Multi-agent coordination with agent assignment tracking
      Features: Agent progress tracking, coordination timeline, integration milestones
    </multi_agent_sessions>
    <development_sessions>
      Purpose: Track complex development tasks with multiple phases
      Template: Development workflow with quality gate tracking
      Features: TDD progress, quality gate results, integration testing outcomes
    </development_sessions>
    <research_sessions>
      Purpose: Document comprehensive analysis and investigation work
      Template: Research documentation with findings and recommendations
      Features: Analysis methodology, findings documentation, actionable insights
    </research_sessions>
    <security_sessions>
      Purpose: Track security analysis, threat modeling, and compliance work
      Template: Security analysis with threat model and compliance tracking
      Features: Threat identification, mitigation tracking, compliance verification
    </security_sessions>
    <enterprise_sessions>
      Purpose: Enterprise-grade work requiring comprehensive audit trails
      Template: Enterprise compliance with regulatory tracking capabilities
      Features: Compliance checkpoints, audit trail, regulatory documentation
    </enterprise_sessions>
  </session_types>
  
  <session_lifecycle_management>
    <creation_phase>
      Session created with appropriate template and labels based on work type
      Initial requirements and success criteria documented
      Integration points established with relevant commands and modules
    </creation_phase>
    <active_phase>
      Progress updates from commands and modules automatically tracked
      Key decisions and architectural choices documented with context
      Quality gates and compliance checkpoints monitored and recorded
      Blocking issues escalated through session for team coordination
    </active_phase>
    <completion_phase>
      Comprehensive outcome summary with results and deliverables
      Lessons learned documented for future reference and improvement
      Follow-up actions identified and linked to future work planning
      Session archived with appropriate outcome labels for analytics
    </completion_phase>
  </session_lifecycle_management>
  
  <github_integration>
    <issue_creation>
      GitHub CLI integration for automated session creation
      Template selection based on session type and work requirements
      Label management for session status, type, and outcome tracking
    </issue_creation>
    <progress_tracking>
      Automated comments from commands documenting progress milestones
      Timeline integration showing session progression and decision points
      Cross-referencing with commits and PRs for complete development context
    </progress_tracking>
    <analytics_support>
      Session outcome tracking for effectiveness analysis
      Pattern recognition for successful session management approaches
      Metrics collection for continuous improvement of session processes
    </analytics_support>
  </github_integration>
  
  <aware_framework_integration>
    <assess_analyze>Session documents initial requirement analysis and complexity assessment</assess_analyze>
    <watch_assumptions>Session tracks assumption validation and requirement evolution</watch_assumptions>
    <architect_approach>Session records architectural decisions and approach rationale</architect_approach>
    <run_verification>Session documents execution progress and verification outcomes</run_verification>
    <evaluate_evolve>Session captures lessons learned and improvement recommendations</evaluate_evolve>
  </aware_framework_integration>
  
  <integration_points>
    <depends_on>
      None - foundational pattern providing session capabilities to all other modules
    </depends_on>
    <provides_to>
      patterns/multi-agent.md for automatic session creation in multi-agent work
      development/protocol-enforcement.md for compliance tracking sessions
      patterns/intelligent-routing.md for session decision logic
      All commands for progress tracking and context documentation
    </provides_to>
  </integration_points>
  
</module>