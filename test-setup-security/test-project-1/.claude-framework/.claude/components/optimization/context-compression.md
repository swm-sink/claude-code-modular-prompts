<prompt_component>
  <step name="Context Compression and Optimization">
    <description>
Intelligent context compression system that reduces token usage while preserving critical information. Uses semantic analysis, hierarchical summarization, and adaptive compression techniques to maintain quality while optimizing for performance and cost.
    </description>
  </step>

  <context_compression>
    <semantic_analysis>
      <priority_scoring>
        <!-- Analyze content importance based on semantic relevance -->
        <relevance_factors>
          - Direct relationship to current task
          - Frequency of reference in session
          - Recency of usage and modification
          - Cross-reference density with other content
          - User-specified importance markers
        </relevance_factors>
        
        <scoring_algorithm>
          Calculate semantic importance score (0-100):
          - Task relevance: 40% weight
          - Usage frequency: 25% weight  
          - Recency: 20% weight
          - Cross-references: 10% weight
          - User markers: 5% weight
        </scoring_algorithm>
      </priority_scoring>
    </semantic_analysis>
    
    <compression_strategies>
      <hierarchical_compression>
        <!-- Multi-level compression preserving structure -->
        <level_1_essential>
          Preserve critical information:
          - Current task context and objectives
          - Active file contents and recent changes
          - User preferences and project configuration
          - Error states and debugging information
        </level_1_essential>
        
        <level_2_important>
          Compress but maintain:
          - Recent conversation history (summarized)
          - Relevant code patterns and examples
          - Project structure and dependencies
          - Configuration and environment details
        </level_2_important>
        
        <level_3_background>
          Heavily compress or archive:
          - Historical conversation context
          - Unused code sections and files
          - General documentation and references
          - Completed task artifacts
        </level_3_background>
      </hierarchical_compression>
      
      <adaptive_compression>
        <!-- Dynamic compression based on available context window -->
        <token_budget_management>
          Monitor and adapt compression based on:
          - Available context window space
          - Anticipated task complexity
          - User interaction patterns
          - Performance requirements
        </token_budget_management>
        
        <compression_techniques>
          - Abstract summarization for code blocks
          - Symbol-based referencing for repeated patterns
          - Contextual abbreviation with expansion markers
          - Semantic clustering of related information
        </compression_techniques>
      </adaptive_compression>
    </compression_strategies>
    
    <quality_preservation>
      <critical_preservation>
        <!-- Ensure no loss of essential information -->
        <preservation_rules>
          - Never compress active debugging context
          - Preserve all user-specified critical information
          - Maintain error reproduction context
          - Keep configuration and environment details intact
        </preservation_rules>
        
        <validation_checks>
          - Verify compressed context maintains task viability
          - Ensure no loss of user preferences or settings
          - Validate preservation of project structure understanding
          - Confirm debugging and error context retention
        </validation_checks>
      </critical_preservation>
    </quality_preservation>
  </context_compression>

  <o>
Context compression completed with intelligent preservation of critical information:

**Compression Ratio:** [percentage]% space saved while maintaining quality
**Critical Information:** 100% preserved (task context, user preferences, active files)
**Important Information:** [percentage]% preserved with smart summarization
**Background Information:** Archived with retrieval markers for future access
**Performance Impact:** [timing] faster processing with reduced token usage
**Quality Score:** [0-100] compression effectiveness rating
  </o>
</prompt_component> 