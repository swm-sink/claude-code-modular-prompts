| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Session Storage Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

**PURPOSE**: Hybrid storage strategy for GitHub sessions with local fallback

────────────────────────────────────────────────────────────────────────────────

```xml
<module purpose="Realistic session storage with GitHub API limits and local fallback">
  
  <github_api_reality>
    <documented_limit>1MB per issue comment</documented_limit>
    <actual_limit>65KB (65,536 bytes)</actual_limit>
    <safe_limit>45KB for practical use</safe_limit>
    <discovery>Empirical testing revealed significant discrepancy</discovery>
  </github_api_reality>
  
  <storage_strategy>
    <tier name="github_only" threshold="<45KB">
      <description>Small sessions fit entirely in GitHub</description>
      <approach>Direct storage in issue comments</approach>
      <benefits>Fully cloud-based, team accessible</benefits>
    </tier>
    
    <tier name="hybrid" threshold="45KB-200KB">
      <description>Medium sessions need split storage</description>
      <approach>Critical data in GitHub, full context local</approach>
      <benefits>Team visibility with complete local backup</benefits>
    </tier>
    
    <tier name="local_primary" threshold=">200KB">
      <description>Large sessions primarily local</description>
      <approach>Summary in GitHub, full data local only</approach>
      <benefits>No size limits, GitHub tracks existence</benefits>
    </tier>
  </storage_strategy>
  
  <implementation>
    <local_storage>
      <path>.claude/sessions/{session_id}/</path>
      <structure>
        - context.json (full session data)
        - artifacts/ (decision artifacts)
        - checkpoints/ (progress tracking)
        - metrics.json (quality scores)
      </structure>
    </local_storage>
    
    <github_storage>
      <format>
        ```json
        {
          "session_id": "uuid",
          "tier": "github_only|hybrid|local_primary",
          "size": "bytes",
          "critical_data": {
            "decisions": [],
            "checkpoints": [],
            "current_phase": ""
          },
          "local_path": "./claude/sessions/{id}"
        }
        ```
      </format>
    </github_storage>
    
    <synchronization>
      <bidirectional>true</bidirectional>
      <conflict_resolution>Local wins with GitHub notification</conflict_resolution>
      <sync_frequency>On checkpoint completion</sync_frequency>
    </synchronization>
  </implementation>
  
  <api_optimization>
    <compression>Use session-compression.md strategies</compression>
    <chunking>Split large updates across comments</chunking>
    <rate_limiting>Respect GitHub API rate limits</rate_limiting>
    <retry_logic>Exponential backoff on failures</retry_logic>
  </api_optimization>
  
  <recovery_mechanisms>
    <github_failure>Fall back to local-only mode</github_failure>
    <local_corruption>Restore from GitHub if available</local_corruption>
    <sync_conflicts>Manual resolution with clear options</sync_conflicts>
  </recovery_mechanisms>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Integration with Runtime Engine

This module implements the context preservation requirements of the Module Runtime Engine:
- State management across module boundaries
- Error isolation and recovery
- Performance optimization through smart storage tiers

────────────────────────────────────────────────────────────────────────────────

*Realistic storage that acknowledges actual constraints.*