---
version: 1.0.0
last_updated: 2025-01-07
status: stable
---

<module name="multi_agent" category="patterns">
  
  <purpose>
    Define and implement native Claude Code multi-agent patterns using Task() and Batch() for parallel execution.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Complex tasks requiring 3+ components or specialized expertise</condition>
    <condition type="explicit">User requests /swarm command or multi-agent coordination</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="pattern_selection" order="1">
      <requirements>
        Task complexity assessed for heterogeneous vs homogeneous work
        Component count and expertise diversity evaluated
        GitHub session automatically created for coordination tracking
      </requirements>
      <actions>
        Analyze task requirements for specialized expertise diversity
        Count affected system components and integration complexity
        Select Task() pattern for heterogeneous work or Batch() for homogeneous work
        Create mandatory GitHub session for multi-agent coordination
      </actions>
      <validation>
        Pattern selection justified by task analysis (Task() vs Batch())
        Session created with proper multi-agent tracking labels
        Agent assignments align with required specialized expertise
      </validation>
    </phase>
    
    <phase name="agent_coordination" order="2">
      <requirements>
        All Task() or Batch() calls executed in single message for true parallelism
        Agents have independent, non-dependent work assignments
        Session serves as communication and progress tracking hub
      </requirements>
      <actions>
        Execute all agent assignments in parallel using single message
        Ensure agent independence with no sequential dependencies
        Document agent roles and responsibilities in session
        Establish progress tracking and milestone reporting structure
      </actions>
      <validation>
        All agents active and working in parallel coordination
        No blocking dependencies between agent assignments
        Session actively tracking progress from all agents
      </validation>
    </phase>
    
    <phase name="completion_coordination" order="3">
      <requirements>
        All agent work completed successfully with quality verification
        Integration testing completed across all agent deliverables
        Session documentation complete with lessons learned
      </requirements>
      <actions>
        Verify all agent deliverables meet quality standards
        Execute integration testing across all agent outputs
        Document architectural decisions and coordination patterns
        Complete session with comprehensive outcome documentation
      </actions>
      <validation>
        All agent work integrated successfully without conflicts
        Quality standards met across all deliverables
        Session documentation complete with reusable patterns
      </validation>
    </phase>
    
  </implementation>
  
  <agent_patterns>
    <task_pattern>
      <description>Heterogeneous work requiring different specialized skills</description>
      <usage>Task("Frontend Architect", "React component architecture with TypeScript and Redux")</usage>
      <usage>Task("Backend Architect", "FastAPI microservices with PostgreSQL and async operations")</usage>
      <usage>Task("Security Specialist", "OAuth2 JWT authentication with RBAC")</usage>
      <usage>Task("DevOps Engineer", "Kubernetes deployment with auto-scaling and monitoring")</usage>
      <coordination>All Task() calls in ONE message for true parallelism</coordination>
    </task_pattern>
    <batch_pattern>
      <description>Homogeneous work distributed in parallel</description>
      <usage>Batch(["Refactor UserService to SOLID principles", "Refactor ProductService to SOLID principles"])</usage>
      <coordination>Single Batch() call for similar operations across multiple targets</coordination>
    </batch_pattern>
    <prompt_evaluation_pattern>
      <description>Comprehensive prompt engineering evaluation using specialized agents</description>
      <usage>Task("Prompt Engineer", "Evaluate prompt clarity and specificity metrics")</usage>
      <usage>Task("Quality Specialist", "Assess robustness and error handling")</usage>
      <usage>Task("Performance Analyst", "Benchmark effectiveness and response quality")</usage>
      <coordination>Parallel evaluation from multiple expert perspectives in single message</coordination>
    </prompt_evaluation_pattern>
  </agent_patterns>
  
  <specialized_roles>
    <system_architect>
      Expertise: Overall system design, technology decisions, integration patterns
      Deliverables: Architecture documentation, technology recommendations, integration specs
    </system_architect>
    <security_specialist>
      Expertise: Threat modeling, vulnerability assessment, compliance implementation
      Deliverables: Security documentation, threat models, compliance reports
    </security_specialist>
    <performance_engineer>
      Expertise: Optimization, scalability analysis, benchmarking
      Deliverables: Performance reports, optimization recommendations, scalability plans
    </performance_engineer>
    <frontend_architect>
      Expertise: UI/UX implementation, client-side optimization, responsive design
      Deliverables: UI components, frontend architecture, user experience flows
    </frontend_architect>
    <backend_engineer>
      Expertise: Server-side logic, API design, database integration
      Deliverables: Backend services, API documentation, database schemas
    </backend_engineer>
    <devops_engineer>
      Expertise: Infrastructure, deployment, monitoring, CI/CD
      Deliverables: Infrastructure code, deployment pipelines, monitoring systems
    </devops_engineer>
    <prompt_engineer>
      Expertise: AI prompt design, evaluation frameworks, testing methodologies
      Deliverables: Optimized prompts, evaluation reports, testing frameworks
    </prompt_engineer>
  </specialized_roles>
  
  <coordination_rules>
    <independence_requirement>
      No dependencies between agents - all work must be parallelizable
      Agents cannot wait for other agent outputs to begin their work
      Shared context provided through session documentation only
    </independence_requirement>
    <session_communication>
      All agents access same session for shared context and decisions
      Progress updates documented in session comments with agent attribution
      Blocking issues escalated through session for team coordination
      Architectural decisions recorded in session for future reference
    </session_communication>
  </coordination_rules>
  
  <quality_assurance>
    <individual_responsibility>
      Each agent responsible for testing their specific components
      Code quality standards enforced for all agent deliverables
      Documentation requirements met by each specialized agent
    </individual_responsibility>
    <integration_coordination>
      Integration testing validates compatibility between agent outputs
      End-to-end testing confirms complete system functionality
      Performance testing verifies system meets SLA requirements
    </integration_coordination>
  </quality_assurance>
  
  <session_integration>
    <mandatory_creation>
      All multi-agent work automatically creates GitHub session
      Session provides coordination hub for agent communication
      Progress tracking enables visibility into parallel work streams
    </mandatory_creation>
    <session_documentation>
      Agent assignments and specialized responsibilities
      Progress milestones and completion status tracking
      Architectural decisions requiring cross-agent coordination
      Integration results and quality verification outcomes
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for automatic session creation
      quality/tdd.md for individual agent testing requirements
      development/task-management.md for quality standards enforcement
      development/prompt-engineering.md for prompt evaluation workflows
    </depends_on>
    <provides_to>
      patterns/intelligent-routing.md for multi-agent escalation triggers
      development/prompt-engineering.md for parallel evaluation execution
      All commands for parallel execution coordination patterns
    </provides_to>
  </integration_points>
  
</module>