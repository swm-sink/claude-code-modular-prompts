# Persistent Memory

**Purpose**: Cross-session memory management leveraging Claude's persistent memory capabilities to maintain project context, learned patterns, and development history.

**Usage**: 
- Initialize session with project context (name, tech stack, session history)
- Track development history including recent changes and ongoing tasks
- Preserve learned patterns and knowledge across sessions
- Provide seamless continuity for long-term project development
- Manage memory updates and context synchronization

**Compatibility**: 
- **Works with**: session-management, intelligent-summarization, context-optimization
- **Requires**: Claude persistent memory capabilities and project context
- **Conflicts**: None (foundational memory management)

**Implementation**:
```python
# Persistent memory management
class PersistentMemory:
    def __init__(self, project_name):
        self.project_name = project_name
        self.memory_store = {}
        
    def initialize_session(self):
        # Load persistent memory from Claude's memory system
        project_context = self.load_project_context()
        development_history = self.load_development_history()
        learned_patterns = self.load_learned_patterns()
        
        return SessionContext(
            project=project_context,
            history=development_history,
            patterns=learned_patterns,
            session_count=self.increment_session_count()
        )
    
    def update_memory(self, session_data):
        # Update persistent memory with new session data
        self.store_recent_changes(session_data.changes)
        self.update_ongoing_tasks(session_data.tasks)
        self.learn_new_patterns(session_data.patterns)
        self.update_last_session_timestamp()
        
        # Sync with Claude's persistent memory
        self.sync_to_persistent_memory()
    
    def load_project_context(self):
        return {
            'name': self.project_name,
            'tech_stack': self.memory_store.get('tech_stack', {}),
            'last_session': self.memory_store.get('last_session_date'),
            'session_count': self.memory_store.get('session_count', 0)
        }
    
    def load_development_history(self):
        return {
            'recent_changes': self.memory_store.get('recent_changes', []),
            'ongoing_tasks': self.memory_store.get('ongoing_tasks', []),
            'completed_milestones': self.memory_store.get('milestones', [])
        }
    
    def load_learned_patterns(self):
        return {
            'coding_patterns': self.memory_store.get('coding_patterns', []),
            'workflow_preferences': self.memory_store.get('workflow_prefs', {}),
            'common_issues': self.memory_store.get('common_issues', []),
            'solution_strategies': self.memory_store.get('solutions', [])
        }
    
    def learn_new_patterns(self, session_patterns):
        # Extract and store new patterns from current session
        for pattern in session_patterns:
            if pattern['confidence'] > 0.8:  # High confidence patterns only
                existing_patterns = self.memory_store.get('coding_patterns', [])
                if not self.pattern_exists(pattern, existing_patterns):
                    existing_patterns.append(pattern)
                    self.memory_store['coding_patterns'] = existing_patterns

# Memory-driven session initialization
def start_memory_aware_session(project_name):
    memory = PersistentMemory(project_name)
    session_context = memory.initialize_session()
    
    return f"""
    Resuming work on {session_context.project['name']}
    
    **Project Context**:
    - Tech Stack: {session_context.project.get('tech_stack', 'Not specified')}
    - Session #{session_context.session_count}
    - Last Active: {session_context.project.get('last_session', 'First session')}
    
    **Ongoing Work**:
    - Recent Changes: {len(session_context.history['recent_changes'])} tracked
    - Active Tasks: {len(session_context.history['ongoing_tasks'])} in progress
    - Learned Patterns: {len(session_context.patterns['coding_patterns'])} available
    
    Ready to continue development with full context awareness.
    """
```

**Category**: context | **Complexity**: moderate | **Time**: 2 hours