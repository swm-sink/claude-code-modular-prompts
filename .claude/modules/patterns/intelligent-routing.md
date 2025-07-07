---
version: 2.0.0
last_updated: 2025-01-07
status: stable
performance: optimized
---

<module name="intelligent_routing" category="patterns">
  
  <purpose>
    High-performance intelligent routing engine that analyzes requests, learns from patterns, and dynamically composes optimal command and module combinations with minimal latency.
  </purpose>
  
  <performance_optimizations>
    <lazy_loading>
      Command handlers loaded only when selected, not at startup
      Module content fetched on-demand with 50ms timeout
      Pattern matchers compiled once and cached for reuse
    </lazy_loading>
    <caching_strategy>
      Request pattern cache: 100 recent patterns, LRU eviction
      Decision cache: 20 recent routing decisions, 5min TTL
      Module dependency graph: Pre-computed at startup
    </caching_strategy>
    <benchmarks>
      Cold start routing: &lt;100ms p95
      Cached pattern match: &lt;10ms p95
      Full request analysis: &lt;200ms p95
      Module composition: &lt;50ms p95
    </benchmarks>
  </performance_optimizations>
  
  <trigger_conditions>
    <condition type="automatic">Complex requests requiring optimal approach selection, legacy command migration</condition>
    <condition type="explicit">User requests /auto command or multi-faceted problems</condition>
  </trigger_conditions>
  
  <smart_request_analysis>
    <pattern_learning>
      Track request patterns: command frequency, module combinations, success rates
      Identify user preferences: command shortcuts, module preferences, workflow patterns
      Learn from failures: routing mismatches, session requirements, performance issues
    </pattern_learning>
    <analysis_logic>
      Keyword extraction with weighted scoring (security:3, test:2, feature:1)
      Context analysis from file paths, recent changes, git status
      Complexity scoring: file count × integration points × security requirements
      Historical pattern matching with 80% confidence threshold
    </analysis_logic>
    <adaptation_rules>
      Promote frequently paired modules to automatic inclusion
      Adjust complexity thresholds based on session success rates
      Cache personalized routing preferences per project context
    </adaptation_rules>
  </smart_request_analysis>
  
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
    <swarm_triggers score="10+">
      3+ system components affected by task scope (score: 5 per component)
      System architecture changes requiring specialized expertise (score: 8)
      Complex integration with multiple external services (score: 4 per service)
      Distributed systems or microservice development work (score: 10)
      Performance: Use when complexity score exceeds 10 points
    </swarm_triggers>
    <task_triggers score="3-9">
      Single component modifications with clear scope (score: 2)
      Well-defined feature implementation within existing patterns (score: 3)
      Bug fixes and issue resolution with targeted changes (score: 1)
      Code refactoring and improvement within component boundaries (score: 2)
      Performance: Default for most development work, 90% of requests
    </task_triggers>
    <query_triggers score="0-2">
      Research-only analysis without system modifications (score: 0)
      Codebase exploration and understanding requirements (score: 1)
      Problem diagnosis and investigation without implementation (score: 1)
      Architecture and design planning without immediate execution (score: 2)
      Performance: Fastest path, no implementation overhead
    </query_triggers>
    <feature_triggers score="5-8">
      New feature development with PRD requirements (score: 5)
      API endpoint creation with documentation (score: 6)
      Database schema changes with migrations (score: 7)
      UI component development with testing (score: 4)
      Performance: Autonomous development with progress tracking
    </feature_triggers>
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
  
  <optimization_tips>
    <performance>
      Pre-warm cache with common patterns during idle time
      Use request batching for parallel module analysis
      Implement circuit breaker for slow module loads (50ms timeout)
      Monitor cache hit rates, target 80%+ for common requests
    </performance>
    <accuracy>
      Track routing success metrics, retrain patterns weekly
      A/B test new routing algorithms with 10% traffic
      Maintain fallback to manual command selection
      Log routing decisions for continuous improvement
    </accuracy>
    <scalability>
      Shard pattern cache by project context
      Use bloom filters for quick negative pattern matches
      Implement request coalescing for duplicate analysis
      Maintain separate caches for different project types
    </scalability>
  </optimization_tips>
  
</module>