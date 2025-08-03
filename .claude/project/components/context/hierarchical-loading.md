<prompt_component>
  <step name="Hierarchical Context Loading">
    <description>
Multi-tier context loading system that intelligently prioritizes and organizes context information across multiple layers. Provides optimal context utilization through strategic loading, caching, and adaptive context management for maximum effectiveness.
    </description>
  </step>

  <hierarchical_loading>
    <context_architecture>
      <!-- Multi-tier context loading with intelligent prioritization -->
      <loading_strategy>
        <tier_1_immediate priority="critical" cache_duration="session">
          <!-- Essential context loaded immediately -->
          <core_project_info>
            - project-config.yaml configuration
            - Current working directory and file structure
            - Active command context and parameters
            - Immediate user request and intent
          </core_project_info>
          
          <session_context>
            - Recent conversation history (last 5 exchanges)
            - Active files and modifications in session
            - Current task state and progress
            - User preferences from session behavior
          </session_context>
        </tier_1_immediate>
        
        <tier_2_relevant priority="high" cache_duration="command">
          <!-- Context relevant to current command -->
          <command_specific>
            - Related files and dependencies for current task
            - Relevant documentation sections
            - Applied patterns and components
            - Similar previous solutions and patterns
          </command_specific>
          
          <project_patterns>
            - Established architecture patterns
            - Code style and convention examples
            - Common integration approaches
            - Testing strategies and frameworks
          </project_patterns>
        </tier_2_relevant>
        
        <tier_3_extended priority="medium" cache_duration="adaptive">
          <!-- Extended context for complex operations -->
          <broader_codebase>
            - Additional related modules and files
            - Cross-cutting concerns and shared utilities
            - API definitions and interfaces
            - Configuration and environment files
          </broader_codebase>
          
          <historical_context>
            - Previous architectural decisions
            - Resolved issues and their solutions
            - Performance optimization history
            - Refactoring patterns and outcomes
          </historical_context>
        </tier_3_extended>
        
        <tier_4_comprehensive priority="low" cache_duration="persistent">
          <!-- Full context for deep analysis -->
          <complete_project>
            - Full project structure and all files
            - Complete documentation set
            - All patterns and examples
            - External dependencies and their usage
          </complete_project>
          
          <knowledge_base>
            - Best practices and design patterns
            - Framework-specific patterns and conventions
            - Security patterns and considerations
            - Performance optimization techniques
          </knowledge_base>
        </tier_4_comprehensive>
      </loading_strategy>
      
      <intelligent_caching>
        <!-- Smart caching based on usage patterns and relevance -->
        <cache_management>
          <session_cache>
            Keep frequently accessed context in session memory:
            - Core project configuration and structure
            - Recently modified files and their content
            - Active development patterns and decisions
            - User workflow preferences and shortcuts
          </session_cache>
          
          <command_cache>
            Cache context specific to command types:
            - `/task` commands: TDD patterns, test frameworks, related code
            - `/feature` commands: Architecture patterns, integration examples
            - `/query` commands: Analysis patterns, documentation, project structure
            - `/protocol` commands: Safety patterns, rollback procedures, validation
          </command_cache>
          
          <adaptive_cache>
            Dynamically adjust cache based on usage:
            - Promote frequently accessed items to higher tiers
            - Compress rarely used context to save memory
            - Preload context based on predicted next actions
            - Expire stale context based on file modification times
          </adaptive_cache>
        </cache_management>
        
        <cache_optimization>
          <relevance_scoring>
            Score context elements for intelligent loading:
            - Direct relevance to current task: Score 8-10
            - Indirect but related: Score 5-7
            - Background context: Score 2-4
            - Historical reference: Score 1
          </relevance_scoring>
          
          <memory_efficiency>
            Optimize memory usage through:
            - Semantic compression of similar patterns
            - Reference-based loading for large files
            - Lazy loading of detailed content
            - Intelligent summarization of verbose context
          </memory_efficiency>
        </cache_optimization>
      </intelligent_caching>
    </context_architecture>
    
    <dynamic_loading>
      <!-- Adapt loading strategy based on command requirements -->
      <command_specific_loading>
        <task_focused_loading>
          For `/task` commands, prioritize:
          - Test framework patterns and examples
          - Related code files and their tests
          - TDD cycle patterns and validation
          - Error handling and edge case examples
        </task_focused_loading>
        
        <feature_comprehensive_loading>
          For `/feature` commands, load:
          - Full architectural context and patterns
          - Integration examples and API patterns
          - Database schema and migration patterns
          - UI/UX patterns and component examples
        </feature_comprehensive_loading>
        
        <query_analytical_loading>
          For `/query` commands, include:
          - Complete project structure and relationships
          - Documentation and architecture decisions
          - Historical context and evolution patterns
          - Cross-cutting concerns and dependencies
        </query_analytical_loading>
        
        <protocol_safety_loading>
          For `/protocol` commands, emphasize:
          - Safety patterns and validation procedures
          - Rollback and recovery mechanisms
          - Testing and verification approaches
          - Risk assessment and mitigation strategies
        </protocol_safety_loading>
      </command_specific_loading>
      
      <predictive_loading>
        <usage_pattern_analysis>
          Analyze usage patterns to predict context needs:
          - Common command sequences and their context requirements
          - User workflow patterns and typical progression
          - Project phase patterns (development, testing, deployment)
          - Time-based patterns (morning setup, afternoon debugging)
        </usage_pattern_analysis>
        
        <preemptive_caching>
          Load context before it's explicitly needed:
          - When `/query` is used, prepare for likely `/task` or `/feature`
          - When files are analyzed, cache related files and dependencies
          - When patterns are identified, cache similar pattern examples
          - When errors occur, cache debugging and solution patterns
        </preemptive_caching>
      </predictive_loading>
    </dynamic_loading>
    
    <performance_optimization>
      <!-- Achieve optimal loading performance -->
      <loading_efficiency>
        <parallel_loading>
          Load context tiers in parallel when possible:
          - Tier 1 loads immediately while Tier 2 loads in background
          - Independent context elements load simultaneously
          - File reads and analysis operations execute concurrently
          - Cache warming happens during idle periods
        </parallel_loading>
        
        <incremental_loading>
          Load context incrementally based on need:
          - Start with minimal context for simple operations
          - Expand context as complexity requirements become clear
          - Load additional tiers only when explicitly needed
          - Stream context as it becomes available rather than waiting for completion
        </incremental_loading>
      </loading_efficiency>
      
      <resource_management>
        <memory_budgeting>
          Manage memory allocation intelligently:
          - Reserve memory for active development context
          - Compress historical context to save space
          - Unload unused context when memory pressure increases
          - Balance between comprehensive context and performance
        </memory_budgeting>
        
        <performance_monitoring>
          Track and optimize loading performance:
          - Measure context loading times and optimize bottlenecks
          - Monitor cache hit rates and adjust strategies
          - Track memory usage and compression effectiveness
          - Identify and optimize frequently loaded context patterns
        </performance_monitoring>
      </resource_management>
    </performance_optimization>
  </hierarchical_loading>

  <o>
Hierarchical context loading completed with optimized multi-tier strategy:

**Loading Tiers:** [count] tiers configured with intelligent priority management
**Context Organization:** [count] context elements organized across priority levels
**Loading Performance:** [timing] average context loading time per tier
**Cache Efficiency:** [percentage]% cache hit rate for frequently accessed content
**Memory Usage:** [size] optimized memory allocation with [percentage]% efficiency
**Loading Score:** [0-100] hierarchical loading effectiveness rating
  </o>
</prompt_component> 