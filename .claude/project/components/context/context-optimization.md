<prompt_component>
  <step name="Context Optimization and Token Management">
    <description>
Advanced context optimization system that maximizes Claude 4's 200K token window through intelligent hierarchical loading, dynamic context management, and adaptive compression. Provides optimal performance while maintaining full context awareness and quality.
    </description>
  </step>

  <context_optimization>
    <token_management>
      <!-- Optimize for Claude 4's full 200K token context window -->
      <context_capacity>
        <total_budget>200000</total_budget>
        <working_reserve>50000</working_reserve>
        <available_context>150000</available_context>
      </context_capacity>
      
      <hierarchical_loading>
        <!-- Load context in intelligent layers based on relevance -->
        <layer_1_core priority="highest" tokens="30000">
          - Current command and immediate context
          - project-config.yaml settings
          - Essential project structure
          - Active file being worked on
        </layer_1_core>
        
        <layer_2_relevant priority="high" tokens="50000">
          - Related files and dependencies
          - Recent conversation history
          - Relevant documentation sections
          - Applied patterns and components
        </layer_2_relevant>
        
        <layer_3_extended priority="medium" tokens="40000">
          - Broader project context
          - Additional related files
          - Extended documentation
          - Historical patterns and decisions
        </layer_3_extended>
        
        <layer_4_comprehensive priority="low" tokens="30000">
          - Full project analysis when needed
          - Complete documentation set
          - All available patterns and examples
          - Deep architectural context
        </layer_4_comprehensive>
      </hierarchical_loading>
    </token_management>
    
    <intelligent_context_assembly>
      <!-- Dynamic context insertion based on query type and complexity -->
      <context_determination>
        <query_analysis>
          Analyze the user's request to determine optimal context loading:
          - Simple queries: Layer 1-2 (80K tokens)
          - Complex analysis: Layer 1-3 (120K tokens)
          - Architectural work: All layers (150K tokens)
          - Emergency debugging: All layers + extra working space
        </query_analysis>
        
        <relevance_scoring>
          Score context elements by relevance to current task:
          - Direct relevance: Score 10 (always include)
          - High relevance: Score 7-9 (include if space)
          - Medium relevance: Score 4-6 (include in extended context)
          - Low relevance: Score 1-3 (include only in comprehensive mode)
        </relevance_scoring>
      </context_determination>
      
      <semantic_chunking>
        <!-- Optimize context through semantic compression -->
        <compression_strategies>
          <information_density>
            - Summarize repetitive patterns
            - Abstract common concepts
            - Reference rather than repeat
            - Use symbolic representations for complex structures
          </information_density>
          
          <priority_preservation>
            - Keep critical information in full
            - Compress auxiliary information
            - Maintain essential relationships
            - Preserve actionable insights
          </priority_preservation>
        </compression_strategies>
      </semantic_chunking>
    </intelligent_context_assembly>
    
    <performance_optimization>
      <!-- Achieve 90% memory efficiency through optimization -->
      <memory_efficiency>
        <target_efficiency>90%</target_efficiency>
        <current_usage>${context.current_tokens}/200000</current_usage>
        <efficiency_score>${context.efficiency_percentage}%</efficiency_score>
      </memory_efficiency>
      
      <adaptive_loading>
        <real_time_adjustment>
          Monitor context usage during execution and adapt:
          - If approaching token limit, compress lower priority context
          - If more context needed, load next layer intelligently
          - If context underutilized, include additional relevant information
        </real_time_adjustment>
        
        <predictive_loading>
          Anticipate context needs based on command type:
          - `/feature` commands: Load architectural context early
          - `/debug` commands: Load error patterns and related code
          - `/query` commands: Load comprehensive project context
          - `/task` commands: Load focused, relevant context only
        </predictive_loading>
      </adaptive_loading>
    </performance_optimization>
    
    <context_continuity>
      <!-- Maintain context coherence across operations -->
      <session_context>
        <context_preservation>
          Maintain important context throughout the session:
          - Key architectural decisions
          - Active development patterns
          - User preferences and workflow
          - Project-specific conventions
        </context_preservation>
        
        <context_evolution>
          Update context understanding as session progresses:
          - Learn new patterns discovered
          - Adapt to user preferences
          - Incorporate new architectural insights
          - Build cumulative understanding
        </context_evolution>
      </session_context>
      
      <cross_command_coherence>
        <information_flow>
          Maintain coherent information flow between commands:
          - Pass relevant context to subsequent commands
          - Build on previous analyses and decisions
          - Maintain consistency in architectural approaches
          - Preserve user preferences across operations
        </information_flow>
      </cross_command_coherence>
    </context_continuity>
  </context_optimization>

  <o>
Context optimization completed with intelligent token management and hierarchical loading:

**Context Capacity:** 200K tokens optimally allocated across priority levels
**Loading Strategy:** Multi-tier hierarchical loading with intelligent prioritization
**Token Efficiency:** [percentage]% token utilization optimization achieved
**Performance:** [timing] context loading time with adaptive compression
**Cache Effectiveness:** [percentage]% cache hit rate for frequently accessed context
**Optimization Score:** [0-100] overall context management effectiveness rating
  </o>
</prompt_component> 