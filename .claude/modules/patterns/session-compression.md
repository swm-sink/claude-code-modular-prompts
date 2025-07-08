| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Session Compression Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="session_compression" category="patterns">
  
  <purpose>
    Intelligent session content compression that preserves critical artifacts while optimizing storage
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze session content structure and identify artifact types</step>
    <step>2. Classify content by importance (critical/important/verbose)</step>
    <step>3. Apply appropriate compression strategy per content type</step>
    <step>4. Preserve all code, configs, and technical decisions</step>
    <step>5. Generate compressed output with artifact inventory</step>
    <step>6. Validate information retention meets 95% threshold</step>
  </thinking_pattern>
  
  <implementation>
    
    <phase name="content_analysis" order="1">
      <requirements>
        Session content parsed and categorized by type
        Critical artifacts identified for preservation
        Compression opportunities quantified
      </requirements>
      <actions>
        Parse session content into structured components
        Identify code blocks, configurations, API definitions
        Mark architectural decisions and technical choices
        Calculate potential compression ratios
      </actions>
      <validation>
        All content categorized with importance levels
        Critical artifacts properly identified
        Compression strategy appropriate for content
      </validation>
    </phase>
    
    <phase name="artifact_preservation" order="2">
      <requirements>
        All code artifacts preserved without modification
        Technical decisions maintained in full
        Configurations and schemas kept intact
      </requirements>
      <actions>
        Extract and preserve all code blocks
        Maintain technical decision documentation
        Keep API contracts and configurations complete
        Create artifact inventory with references
      </actions>
      <validation>
        100% of code artifacts preserved
        All technical decisions accessible
        Configuration integrity maintained
      </validation>
    </phase>
    
    <phase name="intelligent_compression" order="3">
      <requirements>
        Non-critical content compressed intelligently
        Information value retention exceeds 95%
        Compressed format remains readable and useful
      </requirements>
      <actions>
        Compress verbose descriptions to summaries
        Aggregate repetitive updates into milestones
        Replace redundant content with references
        Generate executive summaries for long sections
      </actions>
      <validation>
        Compression achieves target reduction
        Information value preserved above threshold
        Output remains actionable and clear
      </validation>
    </phase>
    
  </implementation>
  
  <compression_rules>
    <never_compress priority="CRITICAL">
      <code_blocks>
        ```language
        // All code blocks preserved exactly as-is
        function example() { return true; }
        ```
      </code_blocks>
      <configurations>
        All JSON, YAML, TOML, XML configurations
        Environment variables and settings
        Build configurations and dependencies
      </configurations>
      <api_definitions>
        OpenAPI/Swagger specifications
        GraphQL schemas
        REST endpoint definitions
        Message formats and protocols
      </api_definitions>
      <architectural_decisions>
        Technology choices with rationale
        Design patterns and their justification
        Security decisions and threat models
        Performance optimization choices
      </architectural_decisions>
    </never_compress>
    
    <intelligent_compression>
      <verbose_descriptions>
        Original: "The user authentication system was implemented using JWT tokens with a Redis-backed session store..."
        Compressed: "• Auth: JWT + Redis session store"
      </verbose_descriptions>
      <progress_updates>
        Original: Multiple detailed progress comments
        Compressed: "✓ Milestones: API complete, UI 80%, Tests passing"
      </progress_updates>
      <discussion_threads>
        Original: Long discussion about approach
        Compressed: "Decision: Chose PostgreSQL over MongoDB for ACID compliance"
      </discussion_threads>
    </intelligent_compression>
    
    <compression_patterns>
      <summary_generation>
        Extract key points from verbose text
        Maintain technical accuracy
        Preserve decision rationale
      </summary_generation>
      <reference_replacement>
        Replace repeated content with links
        Use anchors for cross-references
        Maintain navigability
      </reference_replacement>
      <milestone_aggregation>
        Combine related updates
        Group by logical phases
        Preserve completion status
      </milestone_aggregation>
    </compression_patterns>
  </compression_rules>
  
  <compression_algorithms>
    <hierarchical_compression>
      <level_1_critical>
        No compression - full preservation
        Applies to: code, configs, decisions
        Information retention: 100%
      </level_1_critical>
      
      <level_2_important>
        Light compression - key point extraction
        Applies to: technical discussions, plans
        Information retention: 95-98%
      </level_2_important>
      
      <level_3_verbose>
        Heavy compression - summary only
        Applies to: progress updates, redundant content
        Information retention: 85-90%
      </level_3_verbose>
    </hierarchical_compression>
    
    <semantic_compression>
      <technique>Natural language summarization</technique>
      <preservation>Technical terms and values</preservation>
      <validation>Meaning equivalence check</validation>
    </semantic_compression>
    
    <structural_compression>
      <technique>Hierarchical outline format</technique>
      <preservation>Logical relationships</preservation>
      <validation>Structure integrity check</validation>
    </structural_compression>
  </compression_algorithms>
  
  <compression_metrics>
    <size_reduction>
      <target>60-80% size reduction</target>
      <minimum>40% for artifact-heavy sessions</minimum>
      <maximum>90% for verbose sessions</maximum>
    </size_reduction>
    
    <information_retention>
      <critical_artifacts>100% retention required</critical_artifacts>
      <technical_decisions>100% retention required</technical_decisions>
      <overall_value>95% minimum retention</overall_value>
    </information_retention>
    
    <quality_measures>
      <readability_score>Compressed content readability</readability_score>
      <artifact_accessibility>Direct artifact access maintained</artifact_accessibility>
      <recovery_completeness>Full context recoverable</recovery_completeness>
    </quality_measures>
  </compression_metrics>
  
  <output_format>
    ```markdown
    ## Session Summary [Compressed from XXkb to YYkb - ZZ% reduction]
    
    ### 📎 Preserved Artifacts (100% retention)
    - `/path/to/code/file.js` - Authentication implementation
    - `/configs/api.yaml` - API configuration
    - `#decision-001` - Database selection rationale
    
    ### 🎯 Key Decisions & Outcomes
    • Architecture: Microservices with event-driven communication
    • Database: PostgreSQL for ACID, Redis for caching
    • Security: JWT + OAuth2 with refresh tokens
    
    ### 📊 Progress Summary
    ✓ Phase 1: Backend API (100%) - All endpoints tested
    ✓ Phase 2: Frontend UI (80%) - Auth flow complete
    ⏳ Phase 3: Integration (40%) - In progress
    
    ### 🔗 Full Context
    Local storage: `.claude/sessions/active/{session-id}/`
    Information retention: 96% of original value
    ```
  </output_format>
  
  <validation_rules>
    <pre_compression>
      Verify all artifacts identified
      Calculate expected retention rate
      Confirm compression strategy
    </pre_compression>
    
    <post_compression>
      Validate all artifacts accessible
      Verify information retention > 95%
      Test recovery completeness
      Ensure readability maintained
    </post_compression>
    
    <continuous_monitoring>
      Track compression effectiveness
      Monitor artifact preservation rate
      Measure recovery success rate
      Gather usage feedback
    </continuous_monitoring>
  </validation_rules>
  
  <integration_points>
    <depends_on>
      patterns/session-storage.md for storage integration
      patterns/session-management.md for session lifecycle
    </depends_on>
    <provides_to>
      patterns/session-storage.md for compression service
      patterns/session-management.md for GitHub storage
      patterns/multi-agent.md for agent session compression
    </provides_to>
  </integration_points>
  
</module>
```