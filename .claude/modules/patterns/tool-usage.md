<module name="tool_usage" category="patterns">
  
  <purpose>
    Comprehensive patterns for optimal Claude Code native tool usage with parallel execution and performance optimization.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">All commands use these optimization patterns universally</condition>
    <condition type="explicit">Tool usage optimization, performance improvement, efficiency enhancement</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="parallel_execution" order="1">
      <requirements>
        All tool calls executed in single message for maximum efficiency
        Read-before-write pattern enforced for safe modifications
        Efficient search strategies used to minimize token waste
      </requirements>
      <actions>
        Batch all related tool calls in single message for true parallelism
        Execute Read operations before any Write or Edit operations
        Use specific search patterns: Glob for files, Grep for content
        Group operations by type for optimal processing efficiency
      </actions>
      <validation>
        All tool calls executed in parallel batches without sequential delays
        Read operations completed before modification operations
        Search operations targeted and specific rather than broad
      </validation>
    </phase>
    
    <phase name="error_handling" order="2">
      <requirements>
        Graceful failure handling with clear user communication
        Command resilience with timeout management
        File operation safety with existence verification
      </requirements>
      <actions>
        Handle tool failures gracefully with informative error messages
        Implement timeout management for long-running operations
        Verify file and directory existence before operations
        Provide alternative approaches when primary methods fail
      </actions>
      <validation>
        Tool failures handled without breaking execution flow
        Timeouts managed appropriately for operation types
        File operations verified for safety before execution
      </validation>
    </phase>
    
    <phase name="optimization_patterns" order="3">
      <requirements>
        Multi-agent coordination with conflict prevention
        Progress tracking integration for complex operations
        Token efficiency maximized through smart batching
      </requirements>
      <actions>
        Coordinate tool access across agents to prevent conflicts
        Integrate TodoWrite/TodoRead for operation progress tracking
        Optimize token usage through intelligent operation batching
        Monitor resource usage and adjust strategies accordingly
      </actions>
      <validation>
        Multi-agent tool coordination prevents conflicts
        Progress tracking operational for complex operations
        Token efficiency optimized through strategic batching
      </validation>
    </phase>
    
  </implementation>
  
  <optimization_principles>
    <parallel_execution critical="true">All tool calls in single message - never sequential</parallel_execution>
    <read_before_write mandatory="true">Always Read before Edit/Write operations</read_before_write>
    <efficient_search>Targeted searches: Glob for files, Grep for content patterns</efficient_search>
    <smart_batching>Group related operations for parallel processing</smart_batching>
    <error_resilience>Graceful handling with clear communication</error_resilience>
  </optimization_principles>
  
  <tool_patterns>
    <file_operations>
      <read_pattern>Read multiple files in parallel batch</read_pattern>
      <write_pattern>MultiEdit for multiple changes, Edit for single changes</write_pattern>
      <safety_pattern>LS for verification, Read before modification</safety_pattern>
    </file_operations>
    <search_operations>
      <discovery>Glob("**/*.ext") for file discovery</discovery>
      <content>Grep("pattern", "scope") for content search</content>
      <progressive>Start specific, broaden scope if needed</progressive>
    </search_operations>
    <command_execution>
      <batch_git>git status, git diff, git log in parallel</batch_git>
      <resilient>Handle failures with fallback approaches</resilient>
      <timeout>Appropriate timeouts for operation complexity</timeout>
    </command_execution>
  </tool_patterns>
  
  <multi_agent_coordination>
    <conflict_prevention>Assign non-overlapping file scopes to agents</conflict_prevention>
    <tool_specialization>Different tool sets based on agent role</tool_specialization>
    <session_communication>Shared context through session documentation</session_communication>
  </multi_agent_coordination>
  
  <performance_metrics>
    <efficiency_gains>70% latency reduction through parallel execution</efficiency_gains>
    <token_optimization>Targeted searches reduce token waste</token_optimization>
    <error_reduction>Read-before-write prevents data loss</error_reduction>
    <scalability>Patterns work across single and multi-agent scenarios</scalability>
  </performance_metrics>
  
  <integration_points>
    <depends_on>
      None - foundational pattern for all tool usage
    </depends_on>
    <provides_to>
      ALL commands for optimal tool execution patterns
      patterns/multi-agent.md for agent coordination
      development/task-management.md for progress tracking integration
    </provides_to>
  </integration_points>
  
</module>