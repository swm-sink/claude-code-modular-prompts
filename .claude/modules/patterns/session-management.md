# /patterns/session-management - GitHub Issue Session Integration

**Purpose**: Intelligent GitHub issue-based session management for AI development context tracking and coordination.

## Module Interface
- **Trigger**: Multi-agent work, complex tasks (≥3 components), enterprise features
- **Dependencies**: None (foundational pattern)
- **Session**: Creates and manages GitHub issues as coordination hubs
- **Output**: Structured session tracking with automatic linking and progress updates

## Session Decision Logic (from AWARE Framework)

### Automatic Session Triggers
```python
def should_create_session(complexity, components, command):
    # MANDATORY session creation
    if command == "swarm":
        return "mandatory"  # Multi-agent always needs coordination
    if components >= 3:
        return "mandatory"  # Complex multi-component work
    if "system" in request or "architecture" in request:
        return "mandatory"  # System-level changes
    
    # OPTIONAL session creation
    if complexity == "medium":
        return "prompt_user"  # Ask user preference
    if "enterprise" in request or "compliance" in request:
        return "recommended"  # Enterprise features benefit from tracking
    
    # NO SESSION needed
    return "optional"  # Simple fixes don't require sessions
```

### Session Integration with AWARE Framework
```python
# AWARE Phase 1: Assess & Analyze
session_needed = assess_session_requirements(request, complexity)

# AWARE Phase 3: Architect the Approach  
if session_needed in ["mandatory", "recommended"]:
    session = create_github_session(request_summary)
    document_approach_in_session(session, architecture_plan)

# AWARE Phase 4: Run with Verification
update_session_progress(session, milestones, decisions, blockers)

# AWARE Phase 5: Evaluate & Evolve
complete_session(session, outcome, lessons_learned, follow_ups)
```

## GitHub Issue Session Patterns

### Session Creation
```python
def create_github_session(title, session_type="general"):
    session = gh.issues.create({
        "title": f"{title} - AI Session",
        "labels": ["ai-session", "active", f"type:{session_type}"],
        "template": select_template(session_type),
        "auto_assign": True,
        "milestone": detect_milestone(title)
    })
    
    # Session types:
    # - "multi-agent" for /swarm commands
    # - "development" for /task commands  
    # - "research" for /query commands
    # - "security" for security-focused work
    # - "enterprise" for compliance/production work
    
    return session
```

### Session Lifecycle Management

#### During Development - Progress Tracking
```python
def update_session_progress(session, update_type, content):
    session_updates = {
        "milestone": f"🎯 **Milestone Reached**: {content}",
        "decision": f"🧠 **Decision Made**: {content}",
        "blocker": f"🚫 **Blocker Found**: {content}",
        "architecture": f"🏗️ **Architecture**: {content}",
        "quality_gate": f"✅ **Quality Gate**: {content}",
        "integration": f"🔗 **Integration**: {content}"
    }
    
    session.add_comment(session_updates[update_type])
    session.update_labels_if_needed(update_type)
```

#### Session Completion
```python
def complete_session(session, outcome, details=""):
    # Update labels
    session.remove_label("active")
    session.add_label("completed")
    session.add_label(f"outcome:{outcome}")  # successful, partial, blocked
    
    # Final summary comment
    completion_summary = f"""
## 🏁 Session Complete

**Outcome**: {outcome}
**Details**: {details}
**Completion Date**: {datetime.now().isoformat()}

### Summary
- Total commits linked: {count_linked_commits(session)}
- PRs created: {count_linked_prs(session)}
- Key decisions: {count_decisions(session)}
- Quality gates passed: {count_quality_gates(session)}

### Follow-up Actions
{generate_follow_up_actions(session)}
"""
    
    session.add_comment(completion_summary)
    session.close()
```

## Advanced Session Patterns

### Multi-Agent Session Coordination
```python
class MultiAgentSession:
    def __init__(self, session_issue):
        self.session = session_issue
        self.agents = {}
        self.coordination_log = []
        
    def register_agent(self, agent_role, task_description):
        agent_id = f"agent_{len(self.agents)}"
        self.agents[agent_id] = {
            "role": agent_role,
            "task": task_description,
            "status": "assigned",
            "progress": []
        }
        
        self.session.add_comment(f"""
### 🤖 Agent Assigned: {agent_role}
**Task**: {task_description}
**Agent ID**: {agent_id}
**Status**: Assigned
        """)
        
    def log_agent_progress(self, agent_id, progress_update):
        self.agents[agent_id]["progress"].append({
            "timestamp": datetime.now(),
            "update": progress_update
        })
        
        self.session.add_comment(f"""
### 📈 Progress Update - {self.agents[agent_id]["role"]}
{progress_update}
        """)
```

### Session Search and Analytics
```python
def find_sessions(filters):
    """
    Find sessions with various filters:
    - find_sessions({"status": "active"})
    - find_sessions({"type": "multi-agent", "since": "2025-01-01"})
    - find_sessions({"outcome": "successful", "contains": "authentication"})
    """
    
    query_parts = ["is:issue", "label:ai-session"]
    
    if filters.get("status"):
        query_parts.append(f"label:{filters['status']}")
    if filters.get("type"):
        query_parts.append(f"label:type:{filters['type']}")
    if filters.get("since"):
        query_parts.append(f"created:>={filters['since']}")
    if filters.get("contains"):
        query_parts.append(f'"{filters["contains"]}"')
        
    return gh.search.issues(" ".join(query_parts))

def session_analytics():
    """Generate session effectiveness metrics"""
    return {
        "total_sessions": count_sessions_all_time(),
        "success_rate": calculate_success_rate(),
        "avg_session_duration": calculate_avg_duration(),
        "most_effective_patterns": analyze_successful_patterns(),
        "common_blockers": analyze_common_blockers()
    }
```

## Integration with Command Patterns

### Command Session Integration
```python
# For /swarm commands - MANDATORY sessions
def swarm_session_integration(task_description):
    session = create_github_session(task_description, "multi-agent")
    return MultiAgentSession(session)

# For /task commands - CONDITIONAL sessions  
def task_session_integration(task_description, complexity):
    if complexity >= 3 or "system" in task_description:
        return create_github_session(task_description, "development")
    else:
        return prompt_user_for_session(task_description)

# For /query commands - OPTIONAL sessions
def query_session_integration(research_topic):
    if "architecture" in research_topic or "system" in research_topic:
        return create_github_session(research_topic, "research")
    return None  # Most queries don't need sessions
```

### Session-Command Communication
```python
def link_commit_to_session(session, commit_message):
    """Automatically link commits containing session reference"""
    if f"[#{session.number}]" in commit_message:
        session.add_timeline_event("commit", commit_message)
        
def link_pr_to_session(session, pr_number):
    """Link pull requests to session for tracking"""
    session.add_timeline_event("pr_created", pr_number)
    pr = gh.pulls.get(pr_number)
    pr.add_comment(f"Related to AI session #{session.number}")
```

## Performance and Optimization

### Session Efficiency
- **Lightweight creation**: <500ms session setup
- **Batch updates**: Combine multiple progress updates
- **Smart notifications**: Only notify on significant milestones
- **Auto-archiving**: Completed sessions auto-archive after 90 days

### Token Budget
- **Session overhead**: <1k tokens per session operation
- **Progress tracking**: <200 tokens per update
- **Completion summary**: <500 tokens
- **Search operations**: <300 tokens per query

## Usage Examples

### Complex System Development
```bash
# Automatically creates session for multi-agent work
/swarm "Build microservices e-commerce platform"
# → Session #127: "Microservices E-commerce Platform - AI Session"
# → Type: multi-agent
# → Auto-assigns agents and tracks progress

# Manual session for focused development
/session start "Implement OAuth2 authentication"
# → Session #128: "OAuth2 Authentication - AI Session"  
# → Type: development
# → Manual progress tracking
```

### Session Lifecycle Example
```bash
# 1. Session auto-created by /swarm
Session #129 created: "Real-time Trading Platform - AI Session"

# 2. Agents register and update progress
Agent "System Architect" → Milestone: "Architecture design complete"
Agent "Security Specialist" → Decision: "Using OAuth2 with JWT tokens"
Agent "Performance Engineer" → Quality Gate: "Latency benchmarks passed"

# 3. Session completion
Session #129 completed: outcome:successful
- 15 commits linked
- 3 PRs created  
- 8 key decisions documented
- All quality gates passed
```

**Token Budget**: <1k tokens (efficient session coordination patterns)