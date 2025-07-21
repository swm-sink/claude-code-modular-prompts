---
description: Intelligent session state persistence with compression, encryption, and cross-session continuity
argument-hint: "[session_name] [save_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /session save - Intelligent Session Persistence

Advanced session state management with intelligent compression, encryption, and seamless cross-session continuity.

## Usage
```bash
/session save project-state                  # Save current session state
/session save --auto                         # Automatic periodic saving
/session save --compress                     # Compressed state storage
/session save --encrypt                      # Encrypted session data
```

<command_file>
  <metadata>
    <n>/session save</n>
    <purpose>Intelligent session state persistence with compression, encryption, and cross-session continuity</purpose>
    <usage>
      <![CDATA[
      /session save [session_name] --strategy [save_strategy]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="session_name" type="string" required="true" default="current-session">
      <description>The name to save the session as</description>
    </argument>
    <argument name="save_strategy" type="string" required="false" default="standard">
      <description>The strategy for saving the session (e.g., standard, compress, encrypt)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Save the current session with a specific name</description>
      <usage>/session save "feature-x-development"</usage>
    </example>
    <example>
      <description>Save the session with encryption</description>
      <usage>/session save "secure-session" --strategy "encrypt"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced session management specialist. The user wants to save their current session state.

**Session Save Process:**
1. **Capture State**: Capture the current conversation state, context window, and file modifications.
2. **Compress Context**: Intelligently compress the conversation history and context to optimize storage.
3. **Encrypt Data**: If requested, encrypt the session data for security.
4. **Persist Session**: Save the session state to a persistent storage location.
5. **Generate Analytics**: Generate productivity analytics based on the session data.

**Implementation Strategy:**
- Capture all relevant session data, including conversation history, context, open files, and command history.
- Use intelligent summarization and compression techniques to reduce the size of the saved session.
- Apply strong encryption to the session data if the user requests it.
- Save the session state to a structured format (e.g., JSON, YAML) in a well-defined location.
- Analyze the session data to provide insights into productivity, efficiency, and areas for improvement.

<include component="components/context/persistent-memory.md" />
<include component="components/optimization/context-compression.md" />
<include component="components/analytics/session-tracking.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/persistent-memory.md</component>
      <component>components/optimization/context-compression.md</component>
      <component>components/analytics/session-tracking.md</component>
    </includes_components>
    <uses_config_values>
      <value>session.save.default_strategy</value>
      <value>session.encryption.key</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Purpose
**WORKING** command that saves current Claude Code session state with intelligent context compression, conversation preservation, and productivity analytics.

## Command
`/session-save`

## Functional Implementation

### XML Command Structure
```xml
<command>
  <name>session-save</name>
  <context>
    <status>active|paused|completed</status>
    <summary>Optional session summary</summary>
    <checkpoint_name>Optional checkpoint identifier</checkpoint_name>
    <compression_level>minimal|standard|aggressive</compression_level>
  </context>
  <components>
    <import>context/persistent-memory</import>
    <import>optimization/context-compression</import>
    <import>analytics/session-tracking</import>
  </components>
  <execution>
    <mode>state_preservation</mode>
    <include_context>true</include_context>
    <auto_compress>true</auto_compress>
  </execution>
</command>
```

## ACTUAL SAVE PROCESS

### Session State Capture
```
CLAUDE SESSION SAVE SEQUENCE:
1. Capture current conversation state and context window
2. Extract key decisions, insights, and progress markers
3. Compress conversation history using intelligent summarization
4. Save file modifications and code changes
5. Update session metadata with current progress
6. Create searchable index of session content
7. Generate productivity analytics report
8. Commit changes to git with session linkage
```

## WORKING EXAMPLES

### Example 1: Standard Session Save
**Input:**
```
/session-save --status active --summary "Completed database schema analysis, identified 3 major bottlenecks"
```

**ACTUAL CLAUDE EXECUTION:**
```xml
<session_save_execution>
  <context_capture>
    <current_context_usage>72%</current_context_usage>
    <conversation_messages>47</conversation_messages>
    <commands_executed>12</commands_executed>
    <files_analyzed>8</files_analyzed>
    <decisions_made>5</decisions_made>
  </context_capture>
  
  <conversation_compression>
    <original_length>45,000 tokens</original_length>
    <compression_method>intelligent_summarization</compression_method>
    <preserved_elements>
      <key_decisions>All architectural and implementation decisions preserved</key_decisions>
      <code_snippets>All code examples and snippets maintained</code_snippets>
      <error_solutions>All problem-solution pairs preserved</error_solutions>
      <insights>All important insights and discoveries preserved</insights>
    </preserved_elements>
    <compressed_length>12,000 tokens</compressed_length>
    <compression_ratio>73%</compression_ratio>
  </conversation_compression>
  
  <session_state_summary>
    <progress_overview>
      **Session: Database Performance Optimization**
      **Progress**: Schema analysis phase completed (40% of total project)
      
      **Key Accomplishments:**
      1. ✅ Analyzed current database schema structure
      2. ✅ Identified 3 major performance bottlenecks:
         - Missing index on user_activity.created_at (affects 60% of queries)
         - Inefficient JOIN in order_analytics view (2.3s avg query time)
         - Suboptimal pagination in product_search (memory intensive)
      3. ✅ Documented query patterns and usage statistics
      4. ✅ Created optimization priority matrix
      
      **Next Steps Identified:**
      1. Implement missing indexes (estimated 2 hours)
      2. Refactor order_analytics view (estimated 4 hours)
      3. Optimize product_search pagination (estimated 3 hours)
      4. Performance testing and validation (estimated 2 hours)
      
      **Files Modified:**
      - schema/analysis-report.md (created)
      - docs/performance-bottlenecks.md (created)
      - sql/index-optimization-plan.sql (created)
      
      **Decisions Made:**
      1. Use B-tree indexes for datetime columns (better for range queries)
      2. Implement cursor-based pagination instead of OFFSET (more efficient)
      3. Create materialized view for order_analytics (performance vs. complexity trade-off)
      4. Prioritize user_activity index (highest impact, lowest risk)
      5. Implement gradual rollout strategy (minimize production risk)
    </progress_overview>
    
    <context_preserved>
      <key_conversations>
        **Database Index Strategy Discussion**
        - User question: "Which indexing approach is best for our datetime queries?"
        - Claude analysis: Compared B-tree vs. Hash vs. GIN indexes
        - Decision: B-tree for range queries, documented reasoning
        - Impact: 60% of queries will benefit from this optimization
        
        **Pagination Performance Investigation**
        - Problem: OFFSET pagination causing memory issues at high page numbers
        - Solution: Cursor-based pagination using created_at timestamps
        - Trade-offs: More complex implementation vs. consistent performance
        - Implementation plan: Gradual migration starting with product_search
        
        **Order Analytics View Optimization**
        - Current issue: Complex JOIN taking 2.3s average
        - Analysis: Breaking down query components, identifying bottlenecks
        - Solution: Materialized view with scheduled refresh
        - Risk mitigation: Fallback to real-time view if materialization fails
      </key_conversations>
      
      <technical_context>
        **Database Environment:**
        - PostgreSQL 14.2
        - 50M+ records in main tables
        - Peak traffic: 1000 concurrent users
        - Average query response target: <200ms
        
        **Performance Baseline:**
        - Current avg response time: 850ms
        - Target improvement: 400ms (53% reduction)
        - Most problematic queries identified and prioritized
        
        **Optimization Constraints:**
        - Zero downtime deployment required
        - Backward compatibility for existing APIs
        - Memory usage must not increase
        - Implementation timeline: 2 weeks maximum
      </technical_context>
    </context_preserved>
  </session_state_summary>
  
  <metadata_update>
    {
      "session_id": "claude-session-20250119-db-performance-optimization",
      "last_saved": "2025-01-19T16:45:30Z",
      "status": "active",
      "summary": "Completed database schema analysis, identified 3 major bottlenecks",
      "progress_percentage": 40,
      "total_messages": 47,
      "commands_executed": 12,
      "files_modified": 8,
      "context_usage_peak": "72%",
      "session_duration": "2h 15m",
      "productivity_score": 8.5,
      "next_session_preparation": {
        "context_to_preload": ["schema analysis results", "optimization priority matrix"],
        "files_to_focus": ["sql/index-optimization-plan.sql", "schema/migration-scripts/"],
        "continuation_point": "Ready to implement index optimizations"
      },
      "checkpoints": [
        {
          "id": "checkpoint-schema-analysis",
          "timestamp": "2025-01-19T16:45:30Z",
          "description": "Schema analysis completed, bottlenecks identified",
          "progress": 40,
          "files_snapshot": ["schema/analysis-report.md", "docs/performance-bottlenecks.md"]
        }
      ]
    }
  </metadata_update>
  
  <git_integration>
    <commit_creation>
      <files_committed>
        - .claude/sessions/active/claude-session-20250119-db-performance-optimization/session-metadata.json
        - .claude/sessions/active/claude-session-20250119-db-performance-optimization/conversation-compressed.md
        - .claude/sessions/active/claude-session-20250119-db-performance-optimization/context-snapshot-16-45-30.json
        - schema/analysis-report.md
        - docs/performance-bottlenecks.md
        - sql/index-optimization-plan.sql
      </files_committed>
      
      <commit_message>feat: database schema analysis complete - 3 bottlenecks identified

- Added comprehensive schema analysis report
- Documented 3 major performance bottlenecks
- Created index optimization implementation plan  
- Established optimization priority matrix
- Session: claude-session-20250119-db-performance-optimization</commit_message>
    </commit_creation>
    
    <branch_status>
      <current_branch>feature/db-optimization</current_branch>
      <commits_total>4</commits_total>
      <ready_for_review>false</ready_for_review>
      <estimated_completion>60%</estimated_completion>
    </branch_status>
  </git_integration>
  
  <analytics_report>
    <session_productivity>
      <efficiency_score>8.5/10</efficiency_score>
      <goals_completed>2/5</goals_completed>
      <commands_per_hour>5.3</commands_per_hour>
      <context_utilization>optimal</context_utilization>
      <decision_quality>high</decision_quality>
    </session_productivity>
    
    <optimization_suggestions>
      <context_management>Consider creating checkpoint before analyzing large files</context_management>
      <workflow_efficiency>Batch similar analysis commands to reduce context switching</workflow_efficiency>
      <collaboration>Ready for stakeholder review of identified bottlenecks</collaboration>
    </optimization_suggestions>
  </analytics_report>
</session_save_execution>
```

**Session Save Result:**
```
✅ SESSION SAVED SUCCESSFULLY!

📊 **Save Summary:**
- **Session**: Database Performance Optimization
- **Progress**: 40% complete (schema analysis phase)
- **Duration**: 2h 15m
- **Messages**: 47 (compressed to 12k tokens - 73% reduction)
- **Files Modified**: 8
- **Productivity Score**: 8.5/10

🎯 **Key Accomplishments Preserved:**
- ✅ Identified 3 major database bottlenecks
- ✅ Created optimization priority matrix
- ✅ Documented implementation plan
- ✅ Established performance baselines

🔄 **Context Optimization:**
- Original conversation: 45k tokens
- Compressed to: 12k tokens (73% reduction)
- All key decisions and insights preserved
- Context ready for efficient session resumption

📁 **Files Saved:**
- schema/analysis-report.md ✅
- docs/performance-bottlenecks.md ✅
- sql/index-optimization-plan.sql ✅
- Session metadata and conversation history ✅

🚀 **Next Session Preparation:**
- Context preloaded: Schema analysis results
- Ready to start: Index implementation phase
- Estimated remaining work: 8-10 hours
- Priority: user_activity index (highest impact)

**Git Status:**
- Branch: feature/db-optimization
- Commits: 4 total
- Ready for: Implementation phase
```

### Example 2: Session Completion Save
**Input:**
```
/session-save --status completed --summary "Successfully optimized database performance - 67% improvement achieved" --compression_level aggressive
```

**ACTUAL CLAUDE EXECUTION:**
```xml
<session_completion_save>
  <final_analytics>
    <project_success_metrics>
      <performance_improvement>67%</performance_improvement>
      <target_achieved>Yes (target was 53%)</target_achieved>
      <implementation_time>1.8 weeks (target was 2 weeks)</implementation_time>
      <zero_downtime>True</zero_downtime>
      <backward_compatibility>Maintained</backward_compatibility>
    </project_success_metrics>
    
    <knowledge_extraction>
      <lessons_learned>
        1. B-tree indexes provided 40% improvement alone
        2. Cursor-based pagination eliminated memory issues
        3. Materialized views reduced complex query time by 85%
        4. Gradual rollout strategy prevented production issues
        5. Performance monitoring essential for validation
      </lessons_learned>
      
      <reusable_patterns>
        1. Database optimization methodology
        2. Performance bottleneck identification process
        3. Risk-free deployment strategy
        4. Index selection decision framework
        5. Query optimization techniques
      </reusable_patterns>
      
      <success_factors>
        1. Systematic analysis before implementation
        2. Clear success metrics and baselines
        3. Incremental implementation approach
        4. Continuous performance monitoring
        5. Stakeholder communication throughout
      </success_factors>
    </knowledge_extraction>
  </final_analytics>
  
  <aggressive_compression>
    <compression_strategy>
      <method>hierarchical_summarization</method>
      <preserve_outcomes>100%</preserve_outcomes>
      <preserve_decisions>100%</preserve_decisions>
      <preserve_code>key_snippets_only</preserve_code>
      <preserve_conversations>decision_points_only</preserve_conversations>
    </compression_strategy>
    
    <compression_results>
      <original_size>127,000 tokens</original_size>
      <compressed_size>8,500 tokens</compressed_size>
      <compression_ratio>93%</compression_ratio>
      <knowledge_preserved>All critical knowledge preserved</knowledge_preserved>
    </compression_results>
  </aggressive_compression>
  
  <session_archive>
    <archive_location>.claude/sessions/archived/claude-session-20250119-db-performance-optimization/</archive_location>
    <archive_contents>
      <session_summary>comprehensive_project_summary.md</session_summary>
      <knowledge_base>extracted_patterns_and_lessons.md</knowledge_base>
      <implementation_guide>reusable_optimization_methodology.md</implementation_guide>
      <performance_data>before_after_metrics.json</performance_data>
      <code_artifacts>key_optimizations_and_migrations.sql</code_artifacts>
    </archive_contents>
    
    <searchable_index>
      <tags>["database", "optimization", "postgresql", "performance", "indexes", "success"]</tags>
      <keywords>["bottleneck", "B-tree", "cursor pagination", "materialized view", "67% improvement"]</keywords>
      <outcomes>["performance_optimization", "zero_downtime", "exceeded_targets"]</outcomes>
    </searchable_index>
  </session_archive>
</session_completion_save>
```

## ADVANCED FEATURES

### Intelligent Compression
```
COMPRESSION STRATEGIES:
- Minimal: Preserve all context, light summarization (20-30% reduction)
- Standard: Smart summarization, preserve key decisions (60-75% reduction)  
- Aggressive: Extract essential knowledge only (85-95% reduction)
- Custom: User-defined compression rules and priorities
```

### Context Optimization
```
CONTEXT MANAGEMENT:
- Identify and preserve critical decision points
- Compress repetitive conversation patterns
- Extract reusable knowledge patterns
- Maintain searchable conversation index
- Prepare optimal context for session resumption
```

### Session Analytics
```
PRODUCTIVITY TRACKING:
- Commands per hour and efficiency metrics
- Goal completion and progress tracking
- Context window utilization patterns
- Collaboration effectiveness measures
- Knowledge retention and application
```

This `/session-save` command provides comprehensive state preservation that maintains all critical information while optimizing for future productivity and knowledge reuse. 