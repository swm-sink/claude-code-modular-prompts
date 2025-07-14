| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Deterministic Routing Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

## Purpose
Replace fuzzy complexity scoring with deterministic component counting and transparent routing decisions.

## Core Components

### 1. Component Counter
```python
def count_components(request):
    """Count actual components without estimates or weights"""
    counts = {
        'files_to_read': 0,
        'files_to_modify': 0,
        'files_to_create': 0,
        'cross_module_deps': 0,
        'tests_required': 0,
        'breaking_changes': 0,
        'architecture_decisions': 0
    }
    
    # Use parallel tool calls for efficiency
    results = parallel_analyze(request)
    
    # Count files
    counts['files_to_read'] = len(results.files_to_read)
    counts['files_to_modify'] = len(results.files_to_modify)
    counts['files_to_create'] = len(results.new_files)
    
    # Analyze dependencies
    for file in results.files_to_modify:
        deps = analyze_dependencies(file)
        if deps.cross_module:
            counts['cross_module_deps'] += 1
            
    return counts
```

### 2. Threshold Evaluator
```python
def evaluate_thresholds(counts):
    """Apply deterministic thresholds for command selection"""
    
    # Check each command in order
    if can_use_task(counts):
        return '/task', 'Within single-component limits'
        
    if can_use_feature(counts):
        return '/feature', 'Feature-scoped with design needs'
        
    if should_use_swarm(counts):
        return '/swarm', 'Multi-component requiring isolation'
        
    if is_query_only(counts):
        return '/query', 'Read-only research request'
        
    return '/auto', 'Requirements need clarification'
```

### 3. Decision Artifact Creator
```python
def create_routing_artifact(request, counts, decision):
    """Create immutable decision artifact"""
    
    artifact = {
        'id': f"{timestamp}-routing-{hash}",
        'type': 'routing',
        'request': request,
        'counts': counts,
        'decision': decision,
        'timestamp': now(),
        'cross_references': []
    }
    
    # Save to context preservation system
    save_artifact(artifact)
    return artifact.id
```

## Thinking Pattern

```xml
<thinking_pattern>
  <step>Parse request to identify components</step>
  <step>Count files, functions, dependencies explicitly</step>
  <step>No estimates - only actual counts</step>
  <step>Apply thresholds in deterministic order</step>
  <step>Create immutable decision artifact</step>
  <step>Explain decision transparently</step>
</thinking_pattern>
```

## Integration Points

### With Context Preservation
- Every routing decision creates an artifact
- Artifacts survive context compression
- Cross-references link related decisions
- Query system enables decision analysis

### With Commands
- /auto uses this for intelligent routing
- All commands can query routing history
- Failed routings are recoverable
- Patterns emerge from artifact analysis

## Usage Example

```python
# In /auto command
def route_request(request):
    # Count components
    counts = count_components(request)
    
    # Evaluate thresholds
    command, reason = evaluate_thresholds(counts)
    
    # Create decision artifact
    artifact_id = create_routing_artifact(request, counts, {
        'command': command,
        'reason': reason,
        'confidence': calculate_confidence(counts)
    })
    
    # Explain to user
    explain_routing_decision(command, counts, reason)
    
    # Execute selected command
    return execute_command(command, request, artifact_id)
```

## Benefits

1. **Predictable**: Same input → same routing
2. **Transparent**: Every decision explained
3. **Auditable**: Complete decision history
4. **Learnable**: Patterns improve routing
5. **Recoverable**: Failed decisions traceable