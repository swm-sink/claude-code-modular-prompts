# Context Preservation & Deterministic Routing Integration Guide

## Overview

This guide explains how the Context Preservation system (Phase 1) and Deterministic Routing system (Phase 2) work together to create a robust, auditable, and predictable command routing framework.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Request                             │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Component Counter (Deterministic)               │
│  - Count files, functions, dependencies                      │
│  - No estimates, only actual counts                          │
│  - Parallel analysis for speed                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Threshold Evaluator (Deterministic)             │
│  - Apply fixed thresholds per command                        │
│  - Evaluate in deterministic order                           │
│  - Generate routing decision                                 │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│           Decision Artifact Creator (Preservation)           │
│  - Create immutable artifact with unique ID                  │
│  - Record all counts and decisions                           │
│  - Establish cross-references                                │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Transparency Protocol (User-Facing)             │
│  - Explain decision in clear language                        │
│  - Show component counts                                     │
│  - Present alternatives considered                           │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    Command Execution                         │
│  - Execute selected command                                  │
│  - Update artifact with outcomes                             │
│  - Create child artifacts as needed                          │
└─────────────────────────────────────────────────────────────┘
```

## Integration Example

### Step 1: User Request
```
User: "Add authentication to the API endpoints"
```

### Step 2: Component Counting
```python
counts = {
    'files_to_create': 4,    # auth.py, middleware.py, etc.
    'files_to_modify': 2,    # api.py, config.py
    'tests_required': 6,     # unit and integration tests
    'cross_module_deps': 1,  # api depends on new auth module
    'architecture_decisions': 2  # auth flow, token strategy
}
```

### Step 3: Threshold Evaluation
```python
# Check /task thresholds
if counts['files_to_create'] + counts['files_to_modify'] <= 3:
    # 6 > 3, so /task is not suitable
    
# Check /feature thresholds  
if 2 <= total_files <= 10 and architecture_decisions > 0:
    # 6 files and 2 architecture decisions, so /feature is suitable
    selected = '/feature'
```

### Step 4: Create Decision Artifact
```yaml
artifact:
  id: "2025-07-08-routing-auth123"
  type: "routing"
  decision:
    selected_command: "/feature"
    rationale: "6 files with architecture decisions"
    counts:
      files_total: 6
      architecture_decisions: 2
    alternatives:
      "/task": "Exceeds 3 file limit"
      "/swarm": "Not complex enough"
```

### Step 5: User Transparency
```
I'll use /feature for this task because:
✓ It's a complete feature (authentication system)
✓ Affects 6 files (within feature range of 2-10)
✓ Requires 2 architecture decisions
✓ Needs proper design documentation

Component Analysis:
- Files to create: 4 (auth.py, middleware.py, tokens.py, permissions.py)
- Files to modify: 2 (api.py, config.py)  
- Tests required: 6
- Cross-module dependencies: 1

This will create a PRD first, then implement with TDD approach.
```

### Step 6: Execution & Child Artifacts
```yaml
# Feature execution creates child artifacts
child_artifacts:
  - id: "2025-07-08-task-auth-impl1"
    type: "task"
    parent: "2025-07-08-routing-auth123"
    
  - id: "2025-07-08-task-auth-tests"
    type: "task"
    parent: "2025-07-08-routing-auth123"
```

## Key Integration Points

### 1. Deterministic → Preservation
- Every routing decision creates an artifact
- All component counts are preserved
- Decision rationale is immutable

### 2. Preservation → Transparency
- Artifacts provide full audit trail
- Decisions can be explained from history
- Patterns emerge from artifact analysis

### 3. Transparency → Trust
- Users understand every decision
- Routing is predictable and consistent
- Failures are traceable and learnable

## Query Examples

### Find All Feature Routings
```python
artifacts = query.find_by_type('routing')
             .filter(decision__selected_command='/feature')
             .sort_by('timestamp')
```

### Analyze Routing Patterns
```python
patterns = analyze_routing_patterns(last_30_days)
# Shows: 60% /task, 25% /feature, 10% /swarm, 5% /query
```

### Trace Decision Lineage
```python
lineage = query.trace_lineage('2025-07-08-error-fix123')
# Returns: routing → task → error → recovery → success
```

## Benefits of Integration

1. **Predictability**: Deterministic routing ensures consistency
2. **Auditability**: Every decision is preserved and queryable  
3. **Transparency**: Users understand the "why" behind routing
4. **Learning**: Historical patterns improve future routing
5. **Recovery**: Failed decisions provide learning opportunities
6. **Compliance**: Full audit trail for all decisions

## Next Steps

1. Implement component counting functions
2. Create artifact storage system
3. Build query interface
4. Integrate with existing commands
5. Add transparency layer to all routing decisions