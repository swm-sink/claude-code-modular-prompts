# Cross-Reference System v1.0.0

## Overview

The cross-reference system enables artifacts to maintain relationships across the entire decision history, creating a traceable graph of all decisions and their dependencies.

## Reference Types

### 1. Parent-Child References
```yaml
parent_ref:
  type: "parent"
  artifact_id: "2025-07-08-routing-abc123"
  relationship: "spawned_from"
  
child_refs:
  - type: "child"
    artifact_id: "2025-07-08-task-def456"
    relationship: "implementation_of"
  - type: "child"
    artifact_id: "2025-07-08-task-ghi789"
    relationship: "parallel_task"
```

### 2. Dependency References
```yaml
depends_on:
  - artifact_id: "2025-07-08-architecture-xxx"
    dependency_type: "requires_completion"
    status: "satisfied"
    
required_by:
  - artifact_id: "2025-07-08-feature-yyy"
    dependency_type: "blocks"
    status: "waiting"
```

### 3. Error Chain References
```yaml
error_chain:
  caused_by: "2025-07-08-task-failed"
  recovery_attempt: "2025-07-08-error-recovery1"
  final_resolution: "2025-07-08-error-recovery2"
  
related_errors:
  - artifact_id: "2025-07-08-similar-error"
    similarity: 0.85
    resolution_reused: true
```

### 4. Session References
```yaml
session_refs:
  previous_session: "session-uuid-1"
  next_session: "session-uuid-3"
  related_sessions:
    - session_id: "session-uuid-4"
      relationship: "similar_task"
    - session_id: "session-uuid-5"
      relationship: "continuation"
```

## Reference Query System

### Query by Relationship
```python
# Find all children of a routing decision
query: "refs:children:2025-07-08-routing-abc123"

# Find all artifacts that depend on this one
query: "refs:required_by:2025-07-08-architecture-xxx"

# Find error recovery chain
query: "refs:error_chain:2025-07-08-task-failed"
```

### Query by Pattern
```python
# Find all artifacts with similar decisions
query: "refs:similar:decision_pattern:/swarm"

# Find all artifacts in the same session family
query: "refs:session_family:session-uuid-1"

# Find all artifacts with specific outcomes
query: "refs:outcome:partial_success"
```

### Graph Traversal
```python
# Traverse from routing to all implementations
traverse:
  start: "2025-07-08-routing-abc123"
  direction: "children"
  depth: 3
  filter: "type:task"

# Trace error propagation
traverse:
  start: "2025-07-08-error-initial"
  follow: ["caused_by", "recovery_attempt"]
  until: "status:resolved"
```

## Reference Integrity

### Validation Rules
1. All referenced artifacts must exist
2. Circular references are detected and prevented
3. Reference types must be valid
4. Bi-directional references auto-maintained

### Automatic References
```yaml
auto_refs:
  # When task created from routing decision
  on_task_creation:
    - add_parent_ref: routing_artifact
    - add_child_ref: to_routing_artifact
    
  # When error occurs
  on_error:
    - add_caused_by: failing_artifact
    - add_error_chain: previous_errors
    
  # When session continues
  on_session_continuation:
    - link_previous_session
    - inherit_context_refs
```

## Reference Index Structure

### Primary Index
```yaml
# .claude/context/indexes/reference_index.yaml
reference_index:
  by_artifact:
    "artifact-id-1":
      parents: ["parent-1"]
      children: ["child-1", "child-2"]
      dependencies: ["dep-1"]
      errors: []
      
  by_relationship:
    "spawned_from":
      - from: "parent-1"
        to: "child-1"
      - from: "parent-2"
        to: "child-3"
        
  by_session:
    "session-uuid-1":
      artifacts: ["artifact-1", "artifact-2"]
      references: ["ref-1", "ref-2"]
```

### Graph Cache
```yaml
# .claude/context/indexes/graph_cache.yaml
graph_cache:
  decision_trees:
    "session-uuid-1":
      root: "routing-decision-1"
      branches:
        - path: ["task-1", "task-2"]
          outcome: "success"
        - path: ["task-3", "error-1", "recovery-1"]
          outcome: "recovered"
          
  dependency_graphs:
    "feature-implementation-1":
      nodes: ["arch-1", "task-1", "task-2", "test-1"]
      edges:
        - from: "arch-1"
          to: ["task-1", "task-2"]
          type: "requires"
```

## Usage Examples

### Creating Cross-References
```yaml
# In a task artifact
artifact:
  id: "2025-07-08-task-impl123"
  cross_references:
    - ref_type: "parent"
      artifact_id: "2025-07-08-routing-abc"
      relationship: "implements"
    - ref_type: "dependency"
      artifact_id: "2025-07-08-arch-design"
      relationship: "follows_design"
    - ref_type: "related"
      artifact_id: "2025-07-07-similar-task"
      relationship: "similar_approach"
```

### Querying References
```python
# Find all implementations of a design
GET /context/refs/children/2025-07-08-arch-design

# Find decision lineage
GET /context/refs/lineage/2025-07-08-task-final

# Find similar errors
GET /context/refs/similar/2025-07-08-error-type
```

## Benefits

1. **Complete Traceability**: Every decision linked to its origin
2. **Pattern Recognition**: Identify repeated decision patterns
3. **Error Learning**: Link errors to resolutions
4. **Context Preservation**: Maintain relationships through compression
5. **Audit Compliance**: Full decision graph for review