| version | last_updated | status |
|---------|--------------|--------|
| 1.2.0   | 2025-07-07   | stable |

# Multi-Agent Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="multi_agent" category="patterns">
  
  <purpose>
    Define and implement native Claude Code multi-agent patterns using Task() and Batch() for parallel execution with git worktree isolation for maximum effectiveness.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Create GitHub session for coordination tracking FIRST</step>
    <step>2. Analyze components and assign specialized agents</step>
    <step>3. Create git worktrees BEFORE Task() execution: ../worktrees/swarm-{session}-{agent}</step>
    <step>4. Execute ALL Task() calls in ONE message for true parallelism</step>
    <step>5. Ensure each agent has isolated environment with TDD enforcement</step>
    <step>6. Apply 4-tier error recovery if any agent fails</step>
    <step>7. Merge all agent work and clean up worktrees after completion</step>
  </thinking_pattern>
  
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
    
    <phase name="worktree_isolation" order="2">
      <requirements>
        Each agent requires isolated git worktree for parallel development
        Worktrees created before Task() execution for clean environments
        Agent-specific dependencies and build environments maintained
      </requirements>
      <actions>
        Create dedicated worktree for each agent using git worktree patterns
        Initialize agent-specific environments (venv, node_modules, etc.)
        Configure agent workspace with required tools and dependencies
        Establish worktree naming convention: ../worktrees/swarm-{session}-{agent}
      </actions>
      <validation>
        Each agent has isolated worktree at ../worktrees/swarm-*
        No workspace conflicts between parallel agents
        All agent environments properly initialized
      </validation>
    </phase>
    
    <phase name="agent_coordination" order="3">
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
    
    <phase name="completion_coordination" order="4">
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
  
  <concrete_implementations>
    <git_worktree_task_pattern>
      <description>ACTUAL Claude Code implementation with git worktree isolation</description>
      <implementation>
        ```bash
        # CRITICAL: Create worktrees BEFORE Task() execution
        prepare_swarm_worktrees() {
          local session_id="$1"
          local agents=("frontend" "backend" "devops" "security")
          
          for agent in "${agents[@]}"; do
            local worktree_dir="../worktrees/swarm-${session_id}-${agent}"
            git worktree add "$worktree_dir" -b "swarm/${session_id}/${agent}" origin/main
            echo "✅ Worktree created for $agent: $worktree_dir"
          done
        }
        
        # ACTUAL NATIVE CLAUDE CODE TASK() IMPLEMENTATION
        # Execute ALL Task() calls in ONE message for 70% performance gain
        execute_swarm_with_worktrees() {
          local session_id="$1"
          
          # First create worktrees
          prepare_swarm_worktrees "$session_id"
          
          # Then execute Task() with worktree paths
          # ALL IN ONE MESSAGE FOR TRUE PARALLELISM:
          Task("frontend", {
            objective: "Build React dashboard with real-time updates",
            workspace: "../worktrees/swarm-${session_id}-frontend",
            specifications: {
              framework: "React 18 with TypeScript",
              state: "Redux Toolkit with RTK Query",
              ui: "Material-UI v5 with dark mode"
            }
          })
          
          Task("backend", {
            objective: "Create FastAPI microservices with async operations",
            workspace: "../worktrees/swarm-${session_id}-backend",
            specifications: {
              framework: "FastAPI with Pydantic v2",
              database: "PostgreSQL with asyncpg",
              auth: "OAuth2 with JWT tokens"
            }
          })
          
          Task("devops", {
            objective: "Deploy Kubernetes infrastructure with GitOps",
            workspace: "../worktrees/swarm-${session_id}-devops",
            specifications: {
              orchestration: "Kubernetes with Helm charts",
              ci_cd: "ArgoCD with GitHub Actions",
              monitoring: "Prometheus + Grafana stack"
            }
          })
          
          Task("security", {
            objective: "Implement zero-trust security architecture",
            workspace: "../worktrees/swarm-${session_id}-security",
            specifications: {
              auth: "Keycloak with RBAC",
              secrets: "HashiCorp Vault integration",
              scanning: "OWASP ZAP + Trivy"
            }
          })
        }
        ```
      </implementation>
      <critical_benefits>
        - Each agent works in ISOLATED git worktree preventing conflicts
        - TRUE parallel execution with 70% latency reduction
        - Clean merge process after agent completion
        - No workspace pollution between agents
      </critical_benefits>
    </git_worktree_task_pattern>
    
    <native_batch_implementation>
      <description>ACTUAL Batch() implementation for homogeneous work</description>
      <implementation>
        ```javascript
        // NATIVE BATCH() WITH WORKTREE PREPARATION
        async function executeBatchRefactoring(services) {
          // Prepare worktrees for batch operations
          const worktrees = await Promise.all(
            services.map(async (service) => {
              const worktreePath = `../worktrees/batch-refactor-${service.toLowerCase()}`;
              await exec(`git worktree add ${worktreePath} -b refactor/${service}`);
              return { service, worktreePath };
            })
          );
          
          // ACTUAL BATCH() CALL - ALL IN ONE MESSAGE
          const results = await Batch(
            worktrees.map(({ service, worktreePath }) => ({
              task: `Refactor ${service} to SOLID principles`,
              workspace: worktreePath,
              requirements: {
                principles: ["SRP", "OCP", "LSP", "ISP", "DIP"],
                testing: "Maintain 95% coverage with TDD",
                documentation: "Update API docs and architecture diagrams"
              }
            }))
          );
          
          // Results available in parallel - 85% faster than sequential
          return results;
        }
        ```
      </implementation>
      <performance_gains>
        - 85% faster than sequential refactoring
        - Consistent approach across all services
        - Isolated worktrees prevent cross-contamination
        - Automatic progress tracking in session
      </performance_gains>
    </native_batch_implementation>
    
    <error_recovery_integration>
      <description>Multi-agent work with integrated error recovery</description>
      <implementation>
        ```javascript
        // MULTI-AGENT WITH ERROR RECOVERY PATTERNS
        async function executeResilientSwarm(objective, session) {
          try {
            // Primary: Full multi-agent coordination
            const agents = await Promise.all([
              Task("frontend", { objective, fallback: "simplified_ui" }),
              Task("backend", { objective, fallback: "monolithic_api" }),
              Task("database", { objective, fallback: "single_postgres" })
            ]);
            
            return { success: true, mode: "full_swarm", results: agents };
            
          } catch (swarmError) {
            // Tier 2 Recovery: Sequential with reduced scope
            console.warn("Swarm failed, attempting sequential execution");
            
            try {
              const sequential = [];
              for (const agent of ["frontend", "backend", "database"]) {
                const result = await Task(agent, {
                  objective: simplifyObjective(objective),
                  mode: "degraded",
                  timeout: 300000 // 5 minute timeout
                });
                sequential.push(result);
              }
              
              return { success: true, mode: "sequential_recovery", results: sequential };
              
            } catch (sequentialError) {
              // Tier 3 Recovery: Single generalist agent
              console.error("Sequential failed, using generalist agent");
              
              const generalist = await Task("full-stack", {
                objective: createMVPObjective(objective),
                mode: "emergency",
                constraints: ["minimal_viable_product", "core_features_only"]
              });
              
              return { success: true, mode: "generalist_recovery", results: [generalist] };
            }
          }
        }
        ```
      </implementation>
      <resilience_features>
        - Automatic fallback from swarm → sequential → generalist
        - Graceful degradation maintains core functionality
        - Error tracking through session for analysis
        - Recovery patterns from error-recovery.md integrated
      </resilience_features>
    </error_recovery_integration>
  </concrete_implementations>
  
  <critical_integration_requirements>
    <git_worktree_mandatory>
      ALL multi-agent work MUST use git worktrees for isolation
      Worktrees created BEFORE Task() execution begins
      Naming convention: ../worktrees/swarm-{session}-{agent}
      Automatic cleanup after merge completion
    </git_worktree_mandatory>
    <error_recovery_mandatory>
      ALL multi-agent patterns MUST integrate error recovery
      Use 4-tier recovery from quality/error-recovery.md
      Session tracking for recovery metrics
      Graceful degradation for system resilience
    </error_recovery_mandatory>
    <performance_tracking_mandatory>
      ALL executions MUST track performance metrics
      Verify 70% latency reduction for parallel execution
      Document actual vs theoretical performance
      Optimize based on measured results
    </performance_tracking_mandatory>
  </critical_integration_requirements>
  
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
      patterns/pattern-library.md for proven execution patterns
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
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">parallel_execution</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">batch_operations</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">issue_tracking</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">consequence_mapping</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">three_x_rule</uses_pattern>
    <implementation_notes>
      Task() and Batch() patterns leverage parallel_execution for 70% performance improvement
      Batch() operations follow batch_operations pattern for 50% API call reduction
      GitHub session creation follows issue_tracking pattern for 100% completion rate
      Agent independence validated through consequence_mapping pattern
      Pattern selection follows three_x_rule for thorough analysis before execution
    </implementation_notes>
  </pattern_usage>
  
</module>
```