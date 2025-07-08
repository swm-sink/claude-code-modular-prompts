| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /task - Single-component development with quality gates

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Execute focused development tasks with MANDATORY TDD cycle">
  
  <delegation target="modules/development/task-management.md">
    Research → Write FAILING test → Implement → Make test PASS → Refactor → Quality gates
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Understand the requirement completely</step>
    <step>2. Write a FAILING test FIRST (RED phase)</step>
    <step>3. Implement MINIMAL code to pass (GREEN phase)</step>
    <step>4. REFACTOR for quality while keeping tests green</step>
    <step>5. Verify 90%+ coverage and quality gates</step>
    <step>6. Check if multi-component (escalate to /swarm if yes)</step>
  </thinking_pattern>
  
  <examples>
    /task "Add email validation"      # Creates test_email_validation.py FIRST
    /task "Fix memory leak" --fix     # Creates regression test FIRST
    /task "Refactor to SOLID" --refactor # Ensures tests exist FIRST
    /task "Optimize database query"   # Creates performance test FIRST
  </examples>
  
  <rules enforcement="STRICT">
    <rule priority="CRITICAL">ALWAYS write failing test BEFORE implementation</rule>
    <rule priority="CRITICAL">NEVER write code without test coverage</rule>
    <rule priority="HIGH">90%+ test coverage MANDATORY</rule>
    <rule priority="HIGH">Quality gates from production-standards.md</rule>
    <rule priority="MEDIUM">Escalate to /swarm if touches 3+ files</rule>
  </rules>
  
  <pattern_usage>
    • Implements tdd_cycle pattern EXPLICITLY (RED→GREEN→REFACTOR)
    • Uses parallel_execution for file operations
    • Applies single_responsibility pattern
    • Leverages explicit_validation for error handling
    • Uses three_x_rule for implementation planning
    • Integrates quality gates from production-standards.md
    • Uses error-recovery.md for resilient development
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/task-management.md for full implementation
    See modules/quality/tdd.md for TDD enforcement
  </pattern_usage>
  
</command>
```