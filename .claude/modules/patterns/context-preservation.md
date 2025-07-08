| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | active |

# Context Preservation Module

## Purpose
Create immutable decision artifacts that survive context window compression and enable full decision traceability.

## Core Architecture

### 1. Artifact Management
```python
class ArtifactManager:
    def create_artifact(self, type, decision_data):
        """Create immutable decision artifact"""
        artifact = {
            'id': self._generate_id(type),
            'version': '1.0.0',
            'type': type,
            'timestamp': datetime.utcnow().isoformat(),
            'session_id': self.current_session,
            'metadata': {
                'priority': self._determine_priority(type),
                'preserve_until': self._retention_date(type),
                'compression_safe': True,
                'cross_references': []
            },
            'decision': decision_data,
            'audit_trail': [{
                'timestamp': datetime.utcnow().isoformat(),
                'action': 'Created',
                'details': f'{type} artifact initialized'
            }]
        }
        
        self._save_artifact(artifact)
        self._update_index(artifact)
        return artifact['id']
```

### 2. Compression Survival
```python
class CompressionManager:
    def compress_context(self, threshold_reached):
        """Compress artifacts while preserving critical decisions"""
        
        if threshold_reached >= 0.8:
            # Summarize low priority artifacts
            self._summarize_old_artifacts('low', days=1)
            
        if threshold_reached >= 0.9:
            # Archive medium priority artifacts
            self._archive_artifacts('medium', days=7)
            
        if threshold_reached >= 0.95:
            # Emergency compression
            self._emergency_compress()
            
        # Never touch critical artifacts
        self._verify_critical_preserved()
```

### 3. Cross-Reference System
```python
class ReferenceManager:
    def link_artifacts(self, parent_id, child_id, relationship):
        """Create bidirectional references between artifacts"""
        
        # Update parent
        parent = self.get_artifact(parent_id)
        parent['metadata']['cross_references'].append({
            'artifact_id': child_id,
            'relationship': relationship,
            'type': 'child'
        })
        
        # Update child
        child = self.get_artifact(child_id)
        child['metadata']['cross_references'].append({
            'artifact_id': parent_id,
            'relationship': relationship,
            'type': 'parent'
        })
        
        # Update reference index
        self._update_reference_index(parent_id, child_id, relationship)
```

### 4. Query Interface
```python
class ArtifactQuery:
    def find_by_session(self, session_id):
        """Find all artifacts for a session"""
        return self._query_index('session', session_id)
        
    def find_by_type(self, artifact_type):
        """Find all artifacts of a specific type"""
        return self._query_index('type', artifact_type)
        
    def trace_lineage(self, artifact_id):
        """Trace complete decision lineage"""
        lineage = []
        current = self.get_artifact(artifact_id)
        
        # Traverse up to root
        while current.get('parent_ref'):
            parent = self.get_artifact(current['parent_ref'])
            lineage.append(parent)
            current = parent
            
        return lineage
```

## Thinking Pattern

```xml
<thinking_pattern>
  <step>Identify decision type (routing/task/error)</step>
  <step>Capture all decision factors</step>
  <step>Create immutable artifact with unique ID</step>
  <step>Establish cross-references to related artifacts</step>
  <step>Set retention priority based on importance</step>
  <step>Update indexes for fast querying</step>
</thinking_pattern>
```

## Artifact Templates

### Routing Decision
```yaml
type: routing
priority: high
preserve_days: 30
fields:
  - user_request
  - component_counts
  - selected_command
  - alternatives_considered
  - confidence_level
```

### Task Implementation
```yaml
type: task
priority: medium
preserve_days: 7
fields:
  - implementation_approach
  - files_affected
  - tests_written
  - outcome_status
```

### Error Recovery
```yaml
type: error
priority: critical
preserve_days: 90
fields:
  - error_details
  - root_cause
  - recovery_actions
  - final_resolution
```

## Integration Points

### With Deterministic Routing
- Every routing decision creates an artifact
- Component counts are preserved
- Routing patterns emerge from history

### With Commands
- All commands create decision artifacts
- Failed executions trigger error artifacts
- Success patterns guide future decisions

## Usage Example

```python
# In any command or module
def make_decision(request, analysis):
    # Create decision artifact
    artifact_id = artifact_manager.create_artifact('routing', {
        'request': request,
        'analysis': analysis,
        'components': count_components(request),
        'decision': select_command(analysis),
        'rationale': explain_decision(analysis)
    })
    
    # Link to parent if exists
    if parent_artifact:
        reference_manager.link_artifacts(
            parent_artifact, 
            artifact_id,
            'spawned_from'
        )
    
    # Execute with artifact reference
    return execute_with_artifact(artifact_id)
```

## Benefits

1. **Persistent**: Decisions survive context compression
2. **Traceable**: Complete decision lineage available
3. **Queryable**: Fast artifact retrieval and analysis
4. **Learnable**: Patterns emerge from history
5. **Recoverable**: Failed decisions fully documented