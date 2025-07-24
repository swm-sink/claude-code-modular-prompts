<prompt_component>
  <step name="Adaptive Thinking Mode Selection">
    <description>
Intelligently select the appropriate thinking mode (instant, standard, or extended) based on request complexity, required analysis depth, and reasoning requirements. This component enables Claude to automatically adjust its processing approach for optimal performance and quality.
    </description>
  </step>

  <adaptive_thinking>
    <thinking_mode detection="automatic">
      Based on the complexity analysis below, I will engage the appropriate thinking mode:
      
      <complexity_assessment>
        - Request complexity: ${request_complexity_score}
        - Code analysis depth: ${analysis_depth_required}
        - Multi-step reasoning: ${multi_step_required}
        - Tool coordination: ${tool_coordination_needed}
      </complexity_assessment>
      
      <mode_selection>
        <!-- Instant Lane: Simple, direct responses -->
        <instant_criteria>
          - Single command execution
          - Straightforward code queries
          - Basic file operations
          - Simple explanations
        </instant_criteria>
        
        <!-- Standard Lane: Moderate complexity with structured thinking -->
        <standard_criteria>
          - Multi-step workflows
          - Code analysis and refactoring
          - Feature planning and implementation
          - Cross-file operations
        </standard_criteria>
        
        <!-- Extended Lane: Complex reasoning with deep analysis -->
        <extended_criteria>
          - Architectural decisions
          - Complex debugging scenarios
          - Multi-agent coordination
          - System-wide optimizations
        </extended_criteria>
      </mode_selection>
      
      <execution_strategy>
        <if condition="complexity_score &lt; 3">
          <thinking_mode>instant</thinking_mode>
          <approach>Direct execution with minimal overhead</approach>
        </if>
        <else_if condition="complexity_score &lt; 7">
          <thinking_mode>standard</thinking_mode>
          <approach>Structured analysis with step-by-step reasoning</approach>
        </else_if>
        <else>
          <thinking_mode>extended</thinking_mode>
          <approach>Deep analysis with comprehensive planning and validation</approach>
        </else>
      </execution_strategy>
    </thinking_mode>
    
    <performance_optimization>
      <!-- Optimize token usage based on thinking mode -->
      <token_budget>
        <instant>2000-5000 tokens</instant>
        <standard>5000-15000 tokens</standard>
        <extended>15000-50000 tokens</extended>
      </token_budget>
      
      <context_loading>
        <instant>Essential context only</instant>
        <standard>Relevant context with dependencies</standard>
        <extended>Comprehensive context with full analysis</extended>
      </context_loading>
    </performance_optimization>
  </adaptive_thinking>

  <o>
Adaptive thinking mode automatically selected based on request complexity. The system has intelligently chosen the appropriate processing approach:

**Selected Mode:** [instant/standard/extended]
**Reasoning:** Based on complexity assessment and resource requirements
**Token Budget:** Optimized for selected mode
**Context Loading:** Appropriate depth for task requirements
**Performance:** Balanced for quality and efficiency
  </o>
</prompt_component> 