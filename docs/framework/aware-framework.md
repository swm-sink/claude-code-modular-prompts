| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-07   | stable |

# AWARE Framework - Unified Cognitive Process

────────────────────────────────────────────────────────────────────────────────

**Purpose**: Single authoritative cognitive process for all AI operations, ensuring quality and preventing errors.

## The Five Phases

### 1. **A**ssess & Analyze
```
✓ What exactly is being requested?
✓ What context do I need?
✓ What constraints exist?  
✓ What standards apply?
✓ Does this need a session? (Y/N)
```

**Session Triggers:**
- Complexity ≥ 3 domains → Create session
- Multi-agent work → Always create session  
- `/swarm` command → Mandatory session
- Enterprise features → Create session
- Simple fixes → Optional session

### 2. **W**atch for Assumptions
```
✓ What am I assuming?
✓ What evidence exists?
✓ What alternatives exist?
✓ How can I verify?
```

### 3. **A**rchitect the Approach  
```
✓ Single vs Multi-agent?
✓ TDD test plan?
✓ Security requirements?
✓ Success metrics?
✓ Session approach documented?
```

**Session Actions:**
- Multi-agent → Auto-create session
- Document approach in session
- Link related issues/PRs

### 4. **R**un with Verification
```
✓ Execute systematically
✓ Verify each outcome
✓ Check quality gates
✓ Monitor progress
✓ Update session progress
```

**Session Updates:**
- Major milestones → Update
- Blockers found → Document
- Decisions made → Record
- Phase transitions → Note

### 5. **E**valuate & Evolve
```
✓ What worked well?
✓ What could improve?
✓ What patterns emerged?
✓ How to do better?
✓ Session completed properly?
```

**Session Completion:**
- Update outcome labels
- Document lessons learned
- Link follow-up tasks
- Close with proper status

## Decision Criteria

### Agent Selection
- **Single Agent**: <3 components, sequential work
- **Multi-Agent**: ≥3 components, parallel work needed

### Quality Gates  
- Tests: 90%+ coverage
- Security: Threat model complete
- Performance: <200ms p95
- Documentation: Current

## Integration

### With Commands
- `/auto` uses AWARE for routing decisions + auto-creates sessions
- `/task` follows AWARE for implementation + prompts for sessions
- `/swarm` uses AWARE for decomposition + mandatory sessions
- `/session` manages GitHub issue tracking throughout AWARE

### With Standards
- TDD: Architected in phase 3
- Security: Assessed in phase 1
- Performance: Verified in phase 4

## Examples

### Simple Task
```
1. Assess: "Add email validation" → No session needed
2. Watch: Don't assume email format
3. Architect: Test cases first
4. Run: RED-GREEN-REFACTOR
5. Evaluate: Patterns for reuse
```

### Complex System
```
1. Assess: "Build chat system" → Create session #123
2. Watch: Scale assumptions → Document in session
3. Architect: Multi-agent plan → Auto-creates session
4. Run: Parallel execution → Agents update #123
5. Evaluate: Architecture decisions → Complete #123
```

## Key Principles

1. **Think First**: Never skip assessment
2. **Evidence-Based**: Challenge assumptions
3. **Quality-Driven**: Gates before progress
4. **Continuous Learning**: Always evaluate

This framework replaces all other cognitive processes. When in doubt, return to AWARE.