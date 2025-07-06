<module name="intelligent_routing" category="patterns">
  
  <purpose>
    Research-first intelligent routing that analyzes requests and dynamically composes optimal command and module combinations.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Complex requests requiring optimal approach selection, legacy command migration</condition>
    <condition type="explicit">User requests /auto command or multi-faceted problems</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="research_analysis" order="1">
      <requirements>
        Web research completed for current best practices and 2025 standards
        Codebase analysis identifies existing patterns and constraints
        Requirements extraction surfaces hidden complexities and assumptions
      </requirements>
      <actions>
        Execute web search for domain-specific best practices and current standards
        Analyze existing codebase patterns and architectural constraints
        Extract explicit requirements and infer implicit requirements from context
        Assess task complexity using component count and integration requirements
      </actions>
      <validation>
        Research findings provide current industry context and best practices
        Codebase analysis reveals existing patterns and integration opportunities
        Requirements analysis complete with both explicit and implicit needs identified
      </validation>
    </phase>
    
    <phase name="routing_decision" order="2">
      <requirements>
        Primary command selected based on complexity and scope analysis
        Required modules identified through trigger pattern matching
        Session requirements determined based on complexity and risk assessment
      </requirements>
      <actions>
        Apply routing decision matrix to select optimal primary command
        Compose required modules using intelligent selection rules
        Determine session requirements based on complexity triggers
        Generate decision justification with evidence-based reasoning
      </actions>
      <validation>
        Primary command selection justified by complexity analysis
        Module composition covers all identified requirements
        Session decision appropriate for task complexity and tracking needs
      </validation>
    </phase>
    
    <phase name="execution_handoff" order="3">
      <requirements>
        Selected command receives comprehensive context and module configuration
        Legacy commands properly migrated to modern equivalents with user notification
        Execution tracking established for complex multi-component work
      </requirements>
      <actions>
        Hand off execution to selected command with full context transfer
        Handle legacy command migration with deprecation timeline notification
        Establish session tracking for multi-agent or complex work
        Monitor execution and provide routing feedback for continuous improvement
      </actions>
      <validation>
        Command execution begins with complete context and configuration
        Legacy migration completed with appropriate user guidance
        Session tracking active for qualifying work complexity
      </validation>
    </phase>
    
  </implementation>
  
  <routing_decision_matrix>
    <swarm_triggers>
      3+ system components affected by task scope
      System architecture changes requiring specialized expertise
      Complex integration with multiple external services
      Distributed systems or microservice development work
    </swarm_triggers>
    <task_triggers>
      Single component modifications with clear scope
      Well-defined feature implementation within existing patterns
      Bug fixes and issue resolution with targeted changes
      Code refactoring and improvement within component boundaries
    </task_triggers>
    <query_triggers>
      Research-only analysis without system modifications
      Codebase exploration and understanding requirements
      Problem diagnosis and investigation without implementation
      Architecture and design planning without immediate execution
    </query_triggers>
  </routing_decision_matrix>
  
  <module_selection_rules>
    <security_modules>
      Triggers: audit, compliance, vulnerability, authentication, authorization
      Modules: security/threat-modeling.md, security/financial-compliance.md
      Conditions: Always include for security-related work
    </security_modules>
    <quality_modules>
      Triggers: test, tdd, coverage, quality, production
      Modules: quality/tdd.md, quality/production-standards.md
      Conditions: Required for production deployments
    </quality_modules>
    <development_modules>
      Triggers: feature, implement, build, create
      Modules: development/task-management.md, development/protocol-enforcement.md
      Conditions: Standard development workflow modules
    </development_modules>
    <patterns_modules>
      Triggers: api, microservice, architecture, integration
      Modules: patterns/api-development.md, patterns/session-management.md
      Conditions: Architectural and integration patterns
    </patterns_modules>
  </module_selection_rules>
  
  <legacy_command_migration>
    <multi_agent_commands>
      lead_agent → /swarm with Task() patterns (90 day deprecation)
      batch → /swarm with Batch() patterns (90 day deprecation)
    </multi_agent_commands>
    <quality_commands>
      project:tdd → /task with TDD module (60 day deprecation)
    </quality_commands>
    <security_commands>
      project:code-audit → /task with security audit module (90 day deprecation)
    </security_commands>
    <deployment_commands>
      project:commit-and-push → /task with git operations module (60 day deprecation)
    </deployment_commands>
  </legacy_command_migration>
  
  <session_decision_logic>
    <mandatory_creation>
      Multi-component work affecting 3+ system components
      System architecture modifications requiring coordination
      Compliance work requiring comprehensive audit trail
      Multi-agent coordination through /swarm command execution
    </mandatory_creation>
    <conditional_creation>
      Medium complexity tasks benefiting from progress tracking
      API development projects with architectural implications
      Large refactoring efforts with broad system impact
    </conditional_creation>
    <optional_creation>
      Simple single-file modifications with minimal scope
      Bug fixes isolated to specific component functionality
      Research queries focused on immediate development decisions
    </optional_creation>
  </session_decision_logic>
  
  <integration_points>
    <depends_on>
      All other modules for dynamic composition based on requirements
      quality/critical-thinking.md for rigorous analysis methodology
    </depends_on>
    <provides_to>
      All commands for intelligent routing and module composition decisions
      patterns/session-management.md for automatic session creation logic
    </provides_to>
  </integration_points>
  
</module>