# Decision Artifact Schema v1.0.0

## Core Architecture

Every decision made during Claude Code execution is preserved as an immutable artifact with a unique ID. These artifacts survive context compression and provide full audit trails.

## Artifact Structure

```yaml
artifact:
  id: "{timestamp}-{type}-{hash}"  # Immutable unique identifier
  version: "1.0.0"
  type: "routing|task|architecture|implementation|error"
  timestamp: "2025-07-08T12:00:00Z"
  session_id: "session-{uuid}"
  
  metadata:
    priority: "critical|high|medium|low"
    preserve_until: "2025-12-31T23:59:59Z"  # Retention policy
    compression_safe: true  # Survives context window compression
    cross_references: ["artifact-id-1", "artifact-id-2"]
    tags: ["routing", "swarm", "complexity"]
    
  context:
    user_request: "Original user request"
    current_state:
      files_modified: []
      tests_status: "passing|failing|none"
      active_issues: []
    environment:
      working_directory: "/path/to/project"
      git_branch: "main"
      framework_version: "2.3.0"
      
  decision:
    type: "command_selection|implementation_approach|error_recovery"
    rationale: "Explicit reasoning for the decision"
    components_analyzed:
      file_count: 0
      line_count: 0
      dependency_count: 0
      test_count: 0
      complexity_factors: []
    chosen_path: "Selected approach/command"
    alternatives_considered:
      - path: "Alternative 1"
        reason_rejected: "Why not chosen"
      - path: "Alternative 2"
        reason_rejected: "Why not chosen"
    confidence_level: 0.95
    
  execution:
    command_used: "/swarm|/task|/feature|/query|/auto"
    modules_invoked: ["module1", "module2"]
    start_time: "2025-07-08T12:00:00Z"
    end_time: "2025-07-08T12:05:00Z"
    status: "success|partial|failed"
    
  outcomes:
    files_created: []
    files_modified: []
    tests_added: 0
    tests_passing: 0
    issues_resolved: []
    errors_encountered: []
    recovery_actions: []
    
  audit_trail:
    - timestamp: "2025-07-08T12:00:00Z"
      action: "Decision made"
      details: "Initial routing decision"
    - timestamp: "2025-07-08T12:01:00Z"
      action: "Execution started"
      details: "Command invoked"
    - timestamp: "2025-07-08T12:05:00Z"
      action: "Execution completed"
      details: "All tests passing"
```

## Immutability Rules

1. **Never Modify**: Once created, artifacts are read-only
2. **Always Append**: New decisions create new artifacts
3. **Cross-Reference**: Link related artifacts instead of modifying
4. **Version Evolution**: New schema versions in new artifacts

## Compression Survival

Artifacts are designed to survive context window compression:

1. **Compact Format**: Essential information only
2. **ID-Based References**: Use IDs instead of content duplication
3. **Priority Preservation**: Critical artifacts protected from pruning
4. **Summary Generation**: Auto-generate summaries for quick access

## Query Interface

```yaml
query_patterns:
  by_id: "artifact-2025-07-08-routing-abc123"
  by_type: "type:routing"
  by_session: "session:session-uuid"
  by_date_range: "date:2025-07-08..2025-07-09"
  by_command: "command:/swarm"
  by_status: "status:failed"
  by_priority: "priority:critical"
  with_cross_refs: "refs:artifact-id"
```

## Storage Location

All artifacts stored in: `.claude/context/artifacts/`

Naming convention: `{date}/{type}/{id}.yaml`

Example: `.claude/context/artifacts/2025-07-08/routing/2025-07-08-routing-abc123.yaml`