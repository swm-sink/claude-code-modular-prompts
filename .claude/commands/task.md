| version | last_updated | status |
|---------|--------------|--------|
| 2.3.0   | 2025-07-07   | stable |

# /task - Single-component development with quality gates

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Execute focused development tasks with TDD and quality enforcement">
  
  <delegation target="modules/development/task-management.md">
    Research → TDD cycle → Implement → Quality gates → Complete
  </delegation>
  
  <examples>
    /task "Add email validation"      # Feature development
    /task "Fix memory leak" --fix     # Bug fixing
    /task "Refactor to SOLID" --refactor # Code improvement
    /task "Document API" --docs       # Documentation
  </examples>
  
  <rules>
    • TDD mandatory (RED-GREEN-REFACTOR)
    • 90%+ test coverage required
    • Escalates to /swarm if multi-component
  </rules>
  
  <pattern_usage>
    • Implements tdd_cycle pattern from pattern-library.md
    • Uses parallel_execution for file operations
    • Applies single_responsibility pattern
    • Leverages explicit_validation for error handling
    • Uses three_x_rule for implementation planning
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/task-management.md for full implementation
  </pattern_usage>
  
</command>
```