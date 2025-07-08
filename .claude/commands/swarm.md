| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /swarm - Multi-agent parallel execution with git worktree isolation

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Complex systems via Task() and Batch() patterns with worktree isolation">
  
  <delegation target="modules/patterns/multi-agent.md">
    Create session → Setup worktrees → Decompose work → Execute Task() calls → Merge results
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Create GitHub session for coordination tracking</step>
    <step>2. Analyze components and assign specialized agents</step>
    <step>3. Create git worktrees: ../worktrees/swarm-{session}-{agent}</step>
    <step>4. Execute ALL Task() calls in ONE message for parallelism</step>
    <step>5. Each agent works in isolated environment with TDD</step>
    <step>6. Apply 4-tier error recovery if failures occur</step>
    <step>7. Merge all agent work and clean up worktrees</step>
  </thinking_pattern>
  
  <critical_features>
    <git_worktree_isolation enforcement="MANDATORY">
      ALWAYS create worktrees BEFORE Task() execution
      Each agent MUST have isolated workspace
      Pattern: ../worktrees/swarm-{session}-{agent}
      Clean merge process after completion
    </git_worktree_isolation>
    <parallel_execution>
      ALL Task() calls in SINGLE message - 70% faster
      True parallelism with native Claude Code patterns
      Example: Task("frontend", {...}), Task("backend", {...}), Task("database", {...})
    </parallel_execution>
  </critical_features>
  
  <depends_on>
    patterns/multi-agent.md for Task() and Batch() coordination with worktrees
    patterns/git-operations.md for git worktree management patterns
    patterns/pattern-library.md for proven execution patterns
    patterns/session-management.md for automatic session creation
    quality/error-recovery.md for 4-tier recovery hierarchy
    docs/framework/native-patterns.md for Task()/Batch() documentation
  </depends_on>
  
  <examples>
    /swarm "Build e-commerce platform"     # Multi-service system with isolated worktrees
    /swarm "Optimize for 10x scale"        # Performance across layers in parallel
    /swarm "Migrate monolith to microservices" # Architecture shift with clean isolation
  </examples>
  
  <rules>
    • AUTO-creates GitHub session for coordination
    • AUTO-creates git worktrees for each agent
    • For ≥3 component systems requiring isolation
    • Native Task() and Batch() patterns with error recovery
    • Worktree cleanup after successful merge
  </rules>
  
  <pattern_usage>
    • Uses parallel_execution pattern from pattern-library.md
    • Implements batch_operations for homogeneous work
    • Applies issue_tracking pattern for GitHub sessions
    • Leverages three_x_rule for planning agent assignments
    • Integrates git_worktree_patterns from git-operations.md
    • Implements error_recovery patterns for resilience
    
    See modules/patterns/multi-agent.md for full implementation
    See modules/patterns/git-operations.md for worktree patterns
  </pattern_usage>
  
</command>
```
