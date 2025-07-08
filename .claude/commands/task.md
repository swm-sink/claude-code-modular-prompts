| version | last_updated | status |
|---------|--------------|--------|
| 2.6.0   | 2025-07-08   | stable |

# /task - Research-first single-component development with RISE framework

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Execute research-first focused development tasks with RISE framework and MANDATORY TDD cycle">
  
  <delegation target="modules/development/task-management.md">
    RISE framework → Research deeply → Write FAILING test → Implement → Make test PASS → Refactor → Quality gates
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Apply RISE framework - Define Role and expertise level</action>
      <critical_thinking>
        - What role should I take for this task (senior developer, expert, specialist)?
        - What level of technical expertise is required?
        - What domain knowledge is needed for optimal execution?
        - How does my role affect the approach and quality standards?
      </critical_thinking>
      <output_format>ROLE_DEFINITION: [role] with [expertise_level] for [domain] requiring [standards]</output_format>
      <validation>Role clearly defined with appropriate expertise level</validation>
      <enforcement>BLOCK if role unclear or insufficient for task complexity</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Apply RISE framework - Analyze Input and research thoroughly</action>
      <critical_thinking>
        - What exactly needs to be implemented/fixed based on requirements?
        - What existing code, patterns, or architecture should I understand first?
        - What are the constraints, dependencies, and integration points?
        - What research is needed to ensure optimal approach?
      </critical_thinking>
      <output_format>INPUT_ANALYSIS: [requirement] affecting [components] requiring [research_findings]</output_format>
      <validation>Requirements analyzed with research-based understanding</validation>
      <enforcement>BLOCK until comprehensive research and analysis completed</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Apply RISE framework - Define Steps with TDD RED phase</action>
      <critical_thinking>
        - What are the specific steps for implementation?
        - What tests should I write to verify correctness?
        - How do steps align with TDD methodology?
        - Are test scenarios comprehensive (normal, edge, error cases)?
      </critical_thinking>
      <output_format>STEPS_WITH_TESTS: [step_sequence] with [failing_tests_created]</output_format>
      <validation>Steps defined and failing tests written for all acceptance criteria</validation>
      <enforcement>BLOCK implementation until tests properly fail - use quality/tdd.md#red_phase</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Execute TDD GREEN phase - minimal implementation aligned with RISE expectations</action>
      <critical_thinking>
        - What's the simplest code that makes tests pass?
        - Does implementation align with defined role and expertise level?
        - Am I following the defined steps systematically?
        - Are all tests now passing with focused implementation?
      </critical_thinking>
      <output_format>MINIMAL_IMPLEMENTATION: Code aligned with RISE framework and passing tests</output_format>
      <validation>All tests pass with role-appropriate, step-aligned implementation</validation>
      <enforcement>BLOCK refactoring until GREEN achieved - use quality/tdd.md#green_phase</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Execute TDD REFACTOR phase with RISE Expectations validation</action>
      <critical_thinking>
        - How can I improve code to meet role expectations and standards?
        - What design patterns align with defined expertise level?
        - Does refactored code meet the quality standards for my role?
        - Do tests remain green while achieving RISE expectations?
      </critical_thinking>
      <output_format>REFACTORED_CODE: Design improved to role standards with green tests</output_format>
      <validation>Code meets role expectations, quality improved, tests remain green</validation>
      <enforcement>ROLLBACK if tests fail or quality below role standards</enforcement>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING">
      <action>Apply RISE framework - Validate Expectations and quality gates</action>
      <critical_thinking>
        - Does final deliverable meet all RISE framework expectations?
        - Is test coverage ≥90% with role-appropriate quality?
        - Do all quality gates pass per production-standards.md?
        - Is implementation worthy of the defined expertise level?
      </critical_thinking>
      <output_format>EXPECTATION_VALIDATION: RISE expectations met, coverage [%], quality gates [status]</output_format>
      <validation>RISE expectations fulfilled, quality gates passed, role standards met</validation>
      <enforcement>BLOCK completion until RISE expectations and quality standards achieved</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <rise_framework_integration enforcement="MANDATORY">
    <role_definition>Define expertise level and domain knowledge for appropriate quality standards</role_definition>
    <input_analysis>Comprehensive research and requirement analysis before any implementation</input_analysis>
    <steps_methodology>Systematic approach with clear sequential steps and TDD integration</steps_methodology>
    <expectation_validation>Deliverable must meet role-appropriate quality and expertise standards</expectation_validation>
    <research_first>ALWAYS research existing patterns, architecture, and constraints before coding</research_first>
    <validation>Reference frameworks/rise.md for complete RISE framework implementation</validation>
  </rise_framework_integration>
  
  <tdd_integration enforcement="MANDATORY">
    <red_phase>Write failing tests for all acceptance criteria using quality/tdd.md#red_phase_compliance</red_phase>
    <green_phase>Implement minimal solution to make tests pass using quality/tdd.md#green_phase_compliance</green_phase>
    <refactor_phase>Improve design while maintaining green tests using quality/tdd.md#refactor_phase_compliance</refactor_phase>
    <rise_alignment>TDD cycle must align with RISE framework role expectations and standards</rise_alignment>
    <validation>Reference quality/tdd.md#quality_gates for strict enforcement</validation>
    <blocking_conditions>
      <condition>Implementation attempted before RISE framework application</condition>
      <condition>Research skipped before requirement analysis</condition>
      <condition>Implementation attempted before tests written</condition>
      <condition>Tests pass when they should fail (incorrect tests)</condition>
      <condition>Implementation exceeds test requirements (over-engineering)</condition>
      <condition>Refactoring breaks any existing tests</condition>
      <condition>Final deliverable below role-appropriate quality standards</condition>
    </blocking_conditions>
  </tdd_integration>
  
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
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before any action</module>
      <module>quality/tdd.md - Strict RED-GREEN-REFACTOR enforcement</module>
      <module>development/task-management.md - Task execution workflow</module>
      <module>quality/production-standards.md - Quality gate validation</module>
    </core_stack>
    <contextual_modules>
      <conditional module="patterns/session-management.md" condition="complex_task OR multiple_files"/>
      <conditional module="git/conventional-commits.md" condition="task_complete"/>
      <conditional module="quality/pre-commit.md" condition="code_changes"/>
    </contextual_modules>
  </module_execution>
  
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
  
  <prompt_construction>
    <assembly_preview>
      WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. Critical     │ → 30s requirement analysis
      │    Thinking     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. TDD RED      │ → Write failing tests
      │    Phase        │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. TDD GREEN    │ → Minimal implementation
      │    Phase        │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. TDD REFACTOR │ → Design improvement
      │    Phase        │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. Quality      │ → Coverage & standards
      │    Gates        │
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~12,000
      - Critical thinking: 2,000
      - TDD cycle execution: 7,000
      - Quality validation: 2,000
      - Output formatting: 1,000
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /task "Add email validation"
      [00:30] ✓ Critical thinking: Email validation requirements analyzed
      [00:31] 📝 RED: Writing failing tests for email validation...
      [00:45] 🔴 RED: Tests failing as expected - test_email_validation.py
      [00:46] 💚 GREEN: Implementing minimal email validation...
      [01:15] ✅ GREEN: All tests passing with regex validation
      [01:16] 🔧 REFACTOR: Improving validation class design...
      [01:25] ✨ REFACTOR: Clean validation with builder pattern
      [01:26] 🎯 QUALITY: Running coverage and quality gates...
      [01:35] ✅ COMPLETE: 95% coverage, all gates passed
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Reads 5 checkpoint structure sequentially
      2. Executes critical_thinking questions for each checkpoint
      3. Enforces BLOCKING conditions strictly per TDD methodology
      4. Validates against quality gates from production-standards.md
      5. Formats output according to specified patterns
    </parsing_behavior>

    <decision_points>
      - Checkpoint failures trigger enforcement actions (BLOCK)
      - TDD violations prevent progression to next phase
      - Quality gate failures block task completion
      - Multi-component detection escalates to /swarm
      - Parallel execution for file operations when beneficial
    </decision_points>
  </claude_4_interpretation>

</command>
```