<prompt_component>
  <step name="Persistent Memory Management">
    <description>
Cross-session memory management system that leverages Claude 4's persistent memory capabilities to maintain project context, learned patterns, and development history across sessions. Provides seamless continuity and knowledge preservation.
    </description>
  </step>

  <persistent_memory>
    <session_continuity>
      <!-- Leverage Claude 4's persistent memory for cross-session context -->
      <memory_initialization>
        <project_context>
          Project: ${project.name}
          Tech Stack: ${tech_stack.primary_language}, ${tech_stack.framework}
          Last Session: ${memory.last_session_date}
          Session Count: ${memory.session_count}
        </project_context>
        
        <development_history>
          <recent_changes>
            ${memory.recent_changes || "No recent changes in memory"}
          </recent_changes>
          <ongoing_tasks>
            ${memory.ongoing_tasks || "No ongoing tasks tracked"}
          </ongoing_tasks>
          <learned_patterns>
            ${memory.learned_patterns || "Building pattern knowledge..."}
          </learned_patterns>
        </development_history>
      </memory_initialization>
      
      <context_preservation>
        <!-- Save important context for future sessions -->
        <session_summary>
          At the end of this session, I will update the persistent memory with:
          - Key decisions made and rationale
          - Patterns discovered in the codebase
          - Architectural insights gained
          - Ongoing work that needs continuation
          - User preferences and workflow patterns
        </session_summary>
        
        <learning_accumulation>
          - Code style preferences identified
          - Architectural patterns in use
          - Testing strategies employed
          - Development workflow preferences
          - Common problem areas and solutions
        </learning_accumulation>
      </context_preservation>
    </session_continuity>
    
    <adaptive_context>
      <!-- Use accumulated knowledge to improve responses -->
      <pattern_recognition>
        <if condition="memory.contains_pattern">
          Based on previous sessions, I recognize this pattern: ${memory.pattern_match}
          Applying learned optimizations: ${memory.pattern_optimizations}
        </if>
        <else>
          This appears to be a new pattern. I'll analyze and add to memory for future sessions.
        </else>
      </pattern_recognition>
      
      <preference_adaptation>
        <code_style>
          Previous sessions indicate preference for: ${memory.code_style_preferences}
        </code_style>
        <workflow_style>
          Observed workflow patterns: ${memory.workflow_preferences}
        </workflow_style>
        <communication_style>
          Preferred explanation style: ${memory.communication_preferences}
        </communication_style>
      </preference_adaptation>
    </adaptive_context>
    
    <memory_management>
      <!-- Intelligent memory organization -->
      <retention_strategy>
        <high_priority>
          - Architectural decisions and rationale
          - Custom patterns and conventions
          - Complex problem solutions
          - User workflow preferences
        </high_priority>
        <medium_priority>
          - Code style preferences
          - Common operations and shortcuts
          - Project-specific knowledge
        </medium_priority>
        <low_priority>
          - Routine task details
          - Temporary debugging information
        </low_priority>
      </retention_strategy>
      
      <memory_optimization>
        <!-- Compress and optimize memory for efficiency -->
        <compression_rules>
          - Merge similar patterns and insights
          - Abstract specific examples to general principles
          - Remove redundant or outdated information
          - Prioritize actionable insights over historical details
        </compression_rules>
      </memory_optimization>
    </memory_management>
  </persistent_memory>

  <o>
Persistent memory management completed with cross-session continuity:

**Memory Status:** [active/initialized/restored] persistent memory state
**Session Context:** [count] sessions tracked with [count] preserved patterns
**Knowledge Base:** [count] learned patterns and insights maintained
**Continuity Score:** [percentage]% session context preservation achieved
**Memory Optimization:** [percentage]% memory compression efficiency
**Learning Progress:** [0-100] knowledge accumulation and pattern development rating
  </o>
</prompt_component> 