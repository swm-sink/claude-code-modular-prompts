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
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Create GitHub session for coordination tracking FIRST</action>
      <critical_thinking>
        - Why: Central coordination hub enables deterministic agent behavior
        - Challenge: Single session sufficient for complex multi-component work?
        - Alternative: Multiple linked sessions for component isolation
        - Decision: Single session with clear agent sections for traceability
      </critical_thinking>
      <output_format>SESSION_CREATED: #[number] - [title]</output_format>
      <validation>Must output session ID before proceeding</validation>
      <enforcement>BLOCK if session creation fails - no coordination without tracking</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Analyze components and assign specialized agents with TDD coordination</action>
      <critical_thinking>
        - What components need separate test suites and isolated development?
        - How will agents coordinate their TDD cycles without conflicts?
        - Which agent should establish shared interfaces first?
        - Are test dependencies between agents properly managed?
      </critical_thinking>
      <output_format>AGENT_ASSIGNMENTS:
        - [Agent1]: [responsibility] + TDD enforcement in [worktree]
        - [Agent2]: [responsibility] + TDD enforcement in [worktree]
        - [Agent3]: [responsibility] + TDD enforcement in [worktree]</output_format>
      <validation>Must list all agents with explicit responsibilities AND TDD requirements</validation>
      <enforcement>BLOCK if any agent lacks clear TDD responsibility</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Create git worktrees BEFORE agent execution</action>
      <critical_thinking>
        - Why: Isolated worktrees prevent TDD conflicts and enable true parallelism
        - Challenge: Worktree overhead vs benefit for small changes
        - Alternative: Shared workspace with file locking
        - Decision: Always use worktrees for conflict-free parallel TDD execution
      </critical_thinking>
      <output_format>WORKTREES_CREATED:
        - ../worktrees/swarm-[session]-[agent1] (TDD isolation confirmed)
        - ../worktrees/swarm-[session]-[agent2] (TDD isolation confirmed)</output_format>
      <validation>Must show worktree paths with TDD isolation confirmation</validation>
      <enforcement>VERIFY worktree creation success before proceeding to Task() execution</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Execute Task() calls with TDD coordination protocol</action>
      <critical_thinking>
        - How do agents coordinate shared interfaces without breaking TDD isolation?
        - What happens if one agent's tests depend on another's implementation?
        - Should integration tests be separate from component-level TDD?
        - How to ensure each agent follows RED-GREEN-REFACTOR independently?
      </critical_thinking>
      <output_format>TASK_EXECUTION_WITH_TDD:
        Task("[Agent1]", "Follow TDD: Write tests FIRST for [component] in [worktree]")
        Task("[Agent2]", "Follow TDD: Write tests FIRST for [component] in [worktree]")
        Task("[Agent3]", "Follow TDD: Write tests FIRST for [component] in [worktree]")</output_format>
      <validation>All Task() calls must include explicit TDD requirements</validation>
      <enforcement>VERIFY each Task() includes TDD cycle enforcement using quality/tdd.md</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Verify agent TDD compliance and integration readiness</action>
      <critical_thinking>
        - Did each agent complete full RED-GREEN-REFACTOR cycles?
        - Are component-level tests passing in all worktrees?
        - Do interfaces between agents work as expected?
        - Are integration points properly tested?
      </critical_thinking>
      <output_format>AGENT_TDD_COMPLETION:
        - [Agent1]: TDD COMPLETE - Tests passing: [count] - Coverage: [%]
        - [Agent2]: TDD COMPLETE - Tests passing: [count] - Coverage: [%]
        - [Agent3]: TDD COMPLETE - Tests passing: [count] - Coverage: [%]</output_format>
      <validation>Must confirm TDD compliance AND deliverable completion for all agents</validation>
      <enforcement>BLOCK merge if any agent has failing tests or coverage <90%</enforcement>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING">
      <action>Execute integration testing across agent boundaries</action>
      <critical_thinking>
        - Do components integrate correctly despite separate development?
        - Are there interface mismatches or contract violations?
        - Do end-to-end scenarios work with all components?
        - Are there performance issues in the integrated system?
      </critical_thinking>
      <output_format>INTEGRATION_TEST_STATUS:
        - Component Integration: [PASS/FAIL] - [details]
        - End-to-End Testing: [PASS/FAIL] - [details]
        - Performance Validation: [PASS/FAIL] - [details]</output_format>
      <validation>All integration tests must pass before merge</validation>
      <enforcement>BLOCK merge if integration tests fail - must resolve conflicts</enforcement>
    </checkpoint>
    <checkpoint id="7" verify="optional" enforcement="CONDITIONAL">
      <action>Apply 4-tier error recovery if failures occur</action>
      <critical_thinking>
        - What type of failure occurred and which tier is appropriate?
        - Can we recover while maintaining TDD integrity?
        - Should we restart individual agents or the entire swarm?
        - How to preserve completed TDD work during recovery?
      </critical_thinking>
      <output_format>RECOVERY_STATUS: [NONE|TIER_1|TIER_2|TIER_3|TIER_4]</output_format>
      <validation>Only required if errors detected</validation>
      <enforcement>ESCALATE to next tier if current tier fails</enforcement>
    </checkpoint>
    <checkpoint id="8" verify="true" enforcement="BLOCKING">
      <action>Merge agent work with TDD validation and cleanup</action>
      <critical_thinking>
        - Are all tests still passing after merge?
        - Is the integrated codebase properly tested and documented?
        - Have we maintained TDD discipline throughout the process?
        - Is the final system ready for production deployment?
      </critical_thinking>
      <output_format>MERGE_WITH_TDD_VALIDATION:
        - Merge Status: [SUCCESS/CONFLICTS]
        - Final Test Suite: [PASS/FAIL] - Total tests: [count]
        - Coverage: [%] (target: ≥90%)
        - Worktrees Cleaned: [count]</output_format>
      <validation>Must verify TDD compliance and test success before completion</validation>
      <enforcement>ROLLBACK if final tests fail or coverage drops below 90%</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <tdd_integration enforcement="MANDATORY">
    <multi_agent_tdd>Each agent follows independent TDD cycles in isolated worktrees using quality/tdd.md</multi_agent_tdd>
    <agent_coordination>Agents coordinate shared interfaces through tests-first contracts</agent_coordination>
    <integration_testing>Final integration testing validates all agent work together</integration_testing>
    <validation>Reference quality/tdd.md#quality_gates for per-agent enforcement</validation>
    <blocking_conditions>
      <condition>Any agent starts implementation before writing tests</condition>
      <condition>Integration attempted before all agents complete TDD cycles</condition>
      <condition>Final merge proceeds with failing tests or coverage <90%</condition>
      <condition>Agent worktrees have conflicting test requirements</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <critical_features>
    <git_worktree_isolation>
      <requirement>Create worktrees BEFORE Task() execution</requirement>
      <verification>Each agent must confirm isolated workspace access</verification>
      <pattern>../worktrees/swarm-{session}-{agent}</pattern>
      <cleanup>Clean merge process required for completion</cleanup>
      <output_format>WORKTREE_VERIFICATION: [agent] = [path] = [status]</output_format>
    </git_worktree_isolation>
    <parallel_execution>
      <requirement>ALL Task() calls in SINGLE message</requirement>
      <performance>True parallelism = 70% faster execution</performance>
      <verification>Must show all Task() calls in single tool invocation</verification>
      <example>Task("frontend", {...}), Task("backend", {...}), Task("database", {...})</example>
      <output_format>PARALLEL_CONFIRMED: [count] agents in single message</output_format>
    </parallel_execution>
  </critical_features>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before multi-agent coordination</module>
      <module>patterns/session-management.md - GitHub session creation for coordination tracking</module>
      <module>patterns/multi-agent.md - Task() and Batch() coordination with worktrees</module>
      <module>quality/tdd.md - Multi-agent TDD coordination and enforcement</module>
      <module>patterns/git-operations.md - Git worktree isolation and merge protocols</module>
      <module>quality/production-standards.md - Quality gate validation across all agents</module>
    </core_stack>
    <contextual_modules>
      <conditional module="quality/error-recovery.md" condition="agent_failures OR coordination_issues"/>
      <conditional module="git/conventional-commits.md" condition="merge_complete"/>
      <conditional module="quality/pre-commit.md" condition="final_integration"/>
      <conditional module="development/code-review.md" condition="complex_integration"/>
    </contextual_modules>
  </module_execution>
  
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
