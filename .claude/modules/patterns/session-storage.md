| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Session Storage Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="session_storage" category="patterns">
  
  <purpose>
    Hybrid local/GitHub storage system for session management with intelligent compression and artifact preservation
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Assess session storage requirements (size, artifacts, compression)</step>
    <step>2. Determine optimal storage strategy (GitHub, local, hybrid)</step>
    <step>3. Apply intelligent compression while preserving critical artifacts</step>
    <step>4. Implement storage with automatic fallback mechanisms</step>
    <step>5. Verify storage integrity and recoverability</step>
    <step>6. Monitor storage health and performance metrics</step>
  </thinking_pattern>
  
  <implementation>
    
    <phase name="storage_strategy_selection" order="1">
      <requirements>
        Storage strategy selected based on content size and type
        GitHub API limits (65KB) respected with automatic fallback
        Critical artifacts identified for preservation during compression
      </requirements>
      <actions>
        Calculate session content size and complexity
        Identify critical artifacts (code, decisions, configurations)
        Select appropriate storage tier (GitHub-only, local-only, hybrid)
        Plan compression strategy to preserve essential information
      </actions>
      <validation>
        Storage strategy appropriate for content size and type
        Critical artifacts identified and protected from compression
        Fallback mechanisms configured for reliability
      </validation>
    </phase>
    
    <phase name="intelligent_compression" order="2">
      <requirements>
        Session content compressed intelligently while preserving artifacts
        Compression maintains 95%+ information value
        Code blocks, configurations, and decisions remain intact
      </requirements>
      <actions>
        Apply hierarchical compression based on content importance
        Preserve all code artifacts and technical decisions
        Compress verbose descriptions and repetitive content
        Generate compressed summaries with links to full content
      </actions>
      <validation>
        Compressed content fits within storage limits
        Critical artifacts remain uncompressed and accessible
        Information value retention exceeds 95% threshold
      </validation>
    </phase>
    
    <phase name="hybrid_storage_implementation" order="3">
      <requirements>
        GitHub stores compressed summaries and references
        Local storage maintains full session context
        Synchronization ensures consistency between stores
      </requirements>
      <actions>
        Store compressed summary in GitHub issue/comment
        Save full context to local session storage
        Create bidirectional links between storage locations
        Implement automatic synchronization on updates
      </actions>
      <validation>
        Both storage locations accessible and synchronized
        Full context recoverable from either location
        Storage redundancy provides reliability
      </validation>
    </phase>
    
  </implementation>
  
  <storage_tiers>
    <github_only_tier threshold="45KB">
      <description>Small sessions stored entirely in GitHub</description>
      <compression>Minimal compression, focus on formatting</compression>
      <artifacts>All artifacts inline in issue/comment</artifacts>
      <recovery>Direct recovery from GitHub API</recovery>
    </github_only_tier>
    
    <hybrid_tier threshold="45KB-200KB">
      <description>Medium sessions use GitHub + local storage</description>
      <compression>Intelligent compression for GitHub, full in local</compression>
      <artifacts>Critical artifacts in GitHub, full set local</artifacts>
      <recovery>Primary from local, fallback to GitHub</recovery>
    </hybrid_tier>
    
    <local_primary_tier threshold=">200KB">
      <description>Large sessions primarily use local storage</description>
      <compression>GitHub gets executive summary only</compression>
      <artifacts>All artifacts in local storage</artifacts>
      <recovery>Local required, GitHub provides index</recovery>
    </local_primary_tier>
  </storage_tiers>
  
  <compression_strategies>
    <artifact_preservation priority="HIGHEST">
      <code_blocks>Never compress code blocks or snippets</code_blocks>
      <configurations>Preserve all configuration in full</configurations>
      <api_contracts>Maintain complete API definitions</api_contracts>
      <decisions>Keep architectural decisions intact</decisions>
    </artifact_preservation>
    
    <intelligent_summarization>
      <verbose_descriptions>Compress to bullet points</verbose_descriptions>
      <progress_updates>Aggregate into milestone summaries</progress_updates>
      <discussion_threads>Extract key decisions only</discussion_threads>
      <repetitive_content>Replace with references</repetitive_content>
    </intelligent_summarization>
    
    <compression_metadata>
      <original_size>Track pre-compression size</original_size>
      <compressed_size>Track post-compression size</compressed_size>
      <information_retention>Calculate information value preserved</information_retention>
      <artifact_inventory>List all preserved artifacts</artifact_inventory>
    </compression_metadata>
  </compression_strategies>
  
  <local_storage_implementation>
    <directory_structure>
      ```
      .claude/sessions/
      ├── active/                    # Currently active sessions
      │   ├── {session-id}/
      │   │   ├── metadata.json      # Session metadata
      │   │   ├── context.md         # Full session context
      │   │   ├── artifacts/         # Code and config artifacts
      │   │   ├── decisions/         # Architectural decisions
      │   │   └── checkpoints/       # Progress checkpoints
      ├── completed/                 # Finished sessions
      ├── archived/                  # Long-term storage
      └── recovery/                  # Recovery snapshots
      ```
    </directory_structure>
    
    <storage_operations>
      <create_session>Initialize directory structure with metadata</create_session>
      <update_session>Append to context, update checkpoints</update_session>
      <save_artifacts>Store code/config in artifacts directory</save_artifacts>
      <create_checkpoint>Snapshot current state for recovery</create_checkpoint>
      <archive_session>Move completed sessions with compression</archive_session>
    </storage_operations>
    
    <synchronization>
      <github_sync>Bidirectional sync with GitHub issues</github_sync>
      <conflict_resolution>Local takes precedence, GitHub for backup</conflict_resolution>
      <update_triggers>Auto-sync on significant changes</update_triggers>
      <consistency_checks>Verify sync status periodically</consistency_checks>
    </synchronization>
  </local_storage_implementation>
  
  <recovery_mechanisms>
    <local_recovery priority="1">
      <full_context>Complete session restoration from local storage</full_context>
      <checkpoint_rollback>Restore to previous checkpoint states</checkpoint_rollback>
      <artifact_recovery>Direct access to all preserved artifacts</artifact_recovery>
    </local_recovery>
    
    <github_recovery priority="2">
      <compressed_context>Restore from GitHub summaries</compressed_context>
      <artifact_references>Follow links to critical artifacts</artifact_references>
      <partial_reconstruction>Rebuild context from available data</partial_reconstruction>
    </github_recovery>
    
    <hybrid_recovery priority="3">
      <merge_sources>Combine GitHub and local data</merge_sources>
      <validation>Cross-verify between sources</validation>
      <completeness_check>Ensure full context restoration</completeness_check>
    </hybrid_recovery>
  </recovery_mechanisms>
  
  <monitoring_and_metrics>
    <storage_health>
      <github_availability>Monitor GitHub API accessibility</github_availability>
      <local_disk_usage>Track local storage consumption</local_disk_usage>
      <sync_status>Monitor synchronization health</sync_status>
      <compression_efficiency>Track compression ratios</compression_efficiency>
    </storage_health>
    
    <performance_metrics>
      <storage_latency>Time to save session updates</storage_latency>
      <retrieval_speed>Time to recover full context</retrieval_speed>
      <compression_time>Processing time for compression</compression_time>
      <sync_duration>Time for full synchronization</sync_duration>
    </performance_metrics>
    
    <reliability_metrics>
      <recovery_success_rate>Percentage of successful recoveries</recovery_success_rate>
      <data_integrity>Verification of stored data accuracy</data_integrity>
      <artifact_preservation>Percentage of artifacts preserved</artifact_preservation>
      <information_retention>Value of information preserved</information_retention>
    </reliability_metrics>
  </monitoring_and_metrics>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for session lifecycle hooks
      quality/error-recovery.md for failure handling
    </depends_on>
    <provides_to>
      patterns/session-management.md for storage backend
      patterns/multi-agent.md for agent session storage
      quality/production-standards.md for audit trail storage
    </provides_to>
  </integration_points>
  
</module>
```