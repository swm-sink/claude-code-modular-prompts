---
version: 2.0.0
last_updated: 2025-01-07
status: minimal
---

# /task - Single-component development with quality gates

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
  
</command>