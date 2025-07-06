# /auto - Intelligent Autonomous Routing with Module Composition

**Purpose**: Research deeply, analyze complexity, then intelligently route to optimal commands with dynamic module composition.

**Foundation**: Inherits universal principles from CLAUDE.md (AWARE framework, critical thinking, tool patterns)

## When to Use

Use `/auto` when:
- **Unsure which approach is optimal** - Let intelligence decide
- **Complex multi-faceted requests** - Automatic decomposition  
- **Legacy command syntax** - Seamless migration support
- **Want research-first execution** - Always investigates before acting

## Revolutionary Modular Composition

### Intelligent Module Loading
```python
# Auto analyzes request and dynamically composes modules:

# Security-focused task → Loads security modules
/auto "Audit authentication system for SOX compliance"
# → Routes to /task + loads modules/security/audit.md + modules/security/compliance.md

# Multi-component system → Routes to /swarm + loads multi-agent patterns  
/auto "Build e-commerce platform with microservices"
# → Routes to /swarm + loads modules/patterns/multi-agent.md + creates session

# Quality-focused work → Loads quality modules
/auto "Implement payment processing with TDD"  
# → Routes to /task + loads modules/quality/tdd.md + modules/deploy/protocol.md
```

### Dynamic Decision Engine

```python
def intelligent_routing(request):
    # 1. RESEARCH PHASE - Deep analysis before action
    context = analyze_codebase(request)
    requirements = extract_requirements(request) 
    complexity = assess_complexity(context, requirements)
    
    # 2. MODULE SELECTION - Compose optimal capability set
    modules = []
    if has_security_keywords(request):
        modules.extend(["security/audit", "security/compliance"])
    if requires_testing(request):
        modules.append("quality/tdd")
    if is_multi_component(complexity):
        modules.append("patterns/multi-agent")
    
    # 3. ROUTING DECISION - Select primary command + modules
    if complexity.components >= 3:
        return route("swarm", modules, auto_session=True)
    elif is_research_only(request):
        return route("query", modules, auto_session=False)
    else:
        return route("task", modules, auto_session=prompt_user)
```

## Research-First Execution

### Mandatory Investigation Phase
Before any routing decision:

1. **Web Search**: Current best practices for the domain
2. **Codebase Analysis**: Understand existing patterns and constraints  
3. **Requirement Clarification**: Surface hidden complexities and assumptions
4. **Alternative Assessment**: Consider multiple approaches before selecting optimal

### Evidence-Based Routing
```python
# Research findings influence routing:
research_results = web_search(f"{request_domain} best practices 2025")
codebase_patterns = analyze_existing_implementation(request)
constraints = identify_technical_constraints(codebase_patterns)

# Route based on evidence, not assumptions
optimal_approach = select_approach(research_results, constraints, complexity)
```

## Legacy Command Migration (Zero Breaking Changes)

### Seamless Backward Compatibility
```python
LEGACY_MAPPINGS = {
    # Multi-agent → Modern modular patterns
    "lead_agent": {
        "route": "swarm", 
        "modules": ["patterns/multi-agent"],
        "message": "⚠️ Migrated to /swarm with Task() patterns"
    },
    "batch": {
        "route": "swarm",
        "modules": ["patterns/multi-agent"], 
        "message": "⚠️ Migrated to /swarm with Batch() patterns"
    },
    
    # Quality → Modern quality modules
    "project:tdd": {
        "route": "task",
        "modules": ["quality/tdd"],
        "message": "⚠️ Migrated to /task with TDD module"
    },
    
    # Security → Modern security modules  
    "project:code-audit": {
        "route": "task",
        "modules": ["security/audit"],
        "message": "⚠️ Migrated to /task with security audit module"
    },
    
    # Deploy → Modern deployment modules
    "project:commit-and-push": {
        "route": "task", 
        "modules": ["deploy/commit"],
        "message": "⚠️ Migrated to /task with commit module"
    }
}
```

## Intelligent Session Management

### Auto-Creation Rules
```python
def session_decision(complexity, components, request_type):
    if components >= 3:
        return "auto_create"  # Complex multi-component work
    elif "system" in request or "architecture" in request:
        return "auto_create"  # System-level changes
    elif complexity == "medium":
        return "prompt_user"  # Ask user preference
    else:
        return "optional"     # Simple tasks don't need sessions
```

### Session Integration with Modules
- **Security modules** → Always create compliance tracking session
- **Multi-agent patterns** → Mandatory session for coordination
- **Quality modules** → Session tracks TDD progress and coverage
- **Deploy modules** → Session tracks deployment pipeline and rollback

## Advanced Routing Examples

### Complex System Development
```bash
/auto "Build real-time notification system with WebSockets, Redis, and mobile push"

# Analysis Phase:
# → Web search: "WebSocket Redis notification system best practices 2025"
# → Codebase analysis: Existing messaging infrastructure
# → Complexity assessment: 4 components (WebSocket, Redis, API, Mobile)

# Routing Decision:
# → Primary: /swarm (multi-component complexity)
# → Modules: patterns/multi-agent.md, deploy/protocol.md, security/audit.md
# → Session: Auto-created #125 "Real-time Notification System"
# → Execution: Task() pattern with security and deployment standards
```

### Security Compliance Task
```bash
/auto "Make our payment processing SOX compliant"

# Analysis Phase:  
# → Web search: "SOX compliance payment processing requirements 2025"
# → Codebase analysis: Current payment flow and data handling
# → Security assessment: PCI DSS current state

# Routing Decision:
# → Primary: /task (focused compliance work)
# → Modules: security/compliance.md, security/audit.md, quality/review.md  
# → Session: Auto-created #126 "SOX Compliance Implementation"
# → Execution: Comprehensive compliance implementation with auditing
```

### Research-Only Request
```bash
/auto "Understand how our current caching system works"

# Analysis Phase:
# → Detects research-only intent ("understand", no action verbs)
# → Codebase analysis: Locate caching implementation
# → No modification requirements identified

# Routing Decision:
# → Primary: /query (research-only, zero modifications)
# → Modules: patterns/tool-usage.md (optimal search patterns)
# → Session: None (research doesn't need tracking)
# → Execution: Deep analysis with comprehensive report
```

## Quality Enforcement Integration

### Automatic Quality Module Loading
- **New features** → Loads quality/tdd.md automatically
- **API development** → Loads deploy/fastapi.md + security/audit.md
- **Data handling** → Loads security/compliance.md + quality/performance.md
- **Production changes** → Loads deploy/protocol.md + quality/review.md

### Evidence-Based Decision Documentation
All routing decisions include:
- Research findings that influenced the choice
- Alternative approaches considered and why they were rejected
- Module selection rationale
- Success metrics and evaluation criteria

## Performance Optimization

### Token Budget Management
- **Routing analysis**: <2k tokens (fast decision making)
- **Module composition**: <3k tokens (efficient loading)
- **Execution delegation**: Immediate handoff to specialized commands
- **Total /auto overhead**: <5k tokens (minimal resource usage)

### Caching and Learning
- **Pattern recognition**: Learn from successful routing decisions
- **Context awareness**: Remember project-specific preferences
- **Module effectiveness**: Track which module combinations work best
- **User feedback integration**: Adapt routing based on outcomes

**Foundation**: Built on CLAUDE.md universal principles - inherits AWARE framework, critical thinking, and tool optimization patterns.