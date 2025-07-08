# Artifact Preservation Rules v1.0.0

## Priority Levels

### Critical (Never Compress)
- Error recovery decisions
- Failed execution artifacts
- Active session routing decisions
- Incomplete task artifacts
- Cross-module dependency decisions

### High (Preserve 30 days minimum)
- Successful routing decisions
- Completed task implementations
- Architecture decisions
- Performance benchmarks
- Security-related decisions

### Medium (Preserve 7 days minimum)
- Research query results
- Documentation generation records
- Standard implementation decisions
- Test execution results

### Low (Preserve 24 hours minimum)
- Duplicate routing attempts
- Cancelled operations
- Superseded decisions
- Debug artifacts

## Compression Rules

### When Context Window Reaches 80%
1. Summarize low priority artifacts older than 24 hours
2. Archive medium priority artifacts older than 7 days
3. Create summary artifacts linking to archived items
4. Never touch critical or high priority recent artifacts

### When Context Window Reaches 90%
1. Generate executive summary of all non-critical artifacts
2. Preserve only artifact IDs and outcomes
3. Maintain full critical artifacts
4. Create recovery index for restoration

### When Context Window Reaches 95%
1. Emergency compression mode
2. Keep only critical artifacts and current session
3. Generate compressed session state
4. Alert user about context limitations

## Preservation Strategies

### 1. Artifact Chaining
```yaml
summary_artifact:
  id: "summary-${TIMESTAMP}-${HASH}"
  type: "summary"
  summarizes: ["artifact-1", "artifact-2", "artifact-3"]
  key_decisions:
    - artifact: "artifact-1"
      decision: "Used /swarm for multi-module refactor"
      outcome: "success"
    - artifact: "artifact-2"
      decision: "Error recovery via rollback"
      outcome: "recovered"
```

### 2. State Snapshots
```yaml
snapshot_artifact:
  id: "snapshot-${TIMESTAMP}-${HASH}"
  type: "state_snapshot"
  session_id: "${SESSION_ID}"
  active_artifacts: 45
  compressed_artifacts: 120
  total_decisions: 165
  success_rate: 0.94
  key_patterns:
    - pattern: "Complex tasks → /swarm"
      frequency: 12
    - pattern: "Single file → /task"
      frequency: 38
```

### 3. Cross-Reference Index
```yaml
index_artifact:
  id: "index-${TIMESTAMP}-${HASH}"
  type: "reference_index"
  artifact_map:
    by_session:
      "session-123": ["artifact-1", "artifact-2"]
    by_command:
      "/swarm": ["artifact-3", "artifact-4"]
    by_outcome:
      "failed": ["artifact-5", "artifact-6"]
```

## Restoration Protocol

### From Compressed State
1. Locate summary artifacts
2. Identify critical decisions
3. Restore execution context
4. Rebuild decision chain

### From Archive
1. Query by session ID
2. Load artifact chain
3. Reconstruct state
4. Resume operations

## Automatic Rules

### Always Preserve
- Last 10 routing decisions
- All error recovery artifacts
- Active session artifacts
- Incomplete task artifacts
- Cross-module dependencies

### Always Compress
- Duplicate decisions
- Successful simple tasks older than 24h
- Superseded routing decisions
- Debug/trace artifacts

### Smart Compression
- Group related artifacts
- Generate outcome summaries
- Maintain decision rationale
- Preserve audit trail

## Implementation

All preservation logic implemented in:
`.claude/context/preservation/rules.yaml`

Compression thresholds in:
`.claude/context/preservation/thresholds.yaml`