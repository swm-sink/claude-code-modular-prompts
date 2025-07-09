| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-08   | stable |

# /task - Research-first single-component development with RISE framework

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Execute research-first focused development tasks with RISE framework and MANDATORY TDD cycle">
  
  <delegation target="modules/development/task-management.md">
    RISE framework → Research deeply → Write FAILING test → Implement → Make test PASS → Refactor → Quality gates
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/research-analysis-pattern.md">Research-first methodology</uses_pattern>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Role definition and decision-making</uses_pattern>
    <uses_pattern from="patterns/tdd-cycle-pattern.md">Test-driven development cycle</uses_pattern>
    <uses_pattern from="patterns/implementation-pattern.md">Code development and creation</uses_pattern>
    <uses_pattern from="patterns/quality-validation-pattern.md">Comprehensive quality gates</uses_pattern>
    <uses_pattern from="patterns/error-recovery-pattern.md">Failure handling and recovery</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply RISE framework - Define Role and expertise level</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What role definition is needed for optimal task execution?
          - What context and constraints apply to this development task?
          - How does role selection connect to quality standards and TDD approach?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Role Question: What role should I take for this task (senior developer, expert, specialist)?]
          - [Expertise Question: What level of technical expertise is required?]
          - [Domain Question: What domain knowledge is needed for optimal execution?]
          - [Standards Question: How does my role affect the approach and quality standards?]
          - [TDD Question: How does role selection impact TDD methodology and test design?]
          - [Context Question: What existing patterns align with this role and expertise level?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this role optimal for the task characteristics and complexity?
          - What evidence supports this expertise level selection?
          - How will this role definition guide TDD approach and quality standards?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can role analysis be combined with initial requirement research?</tool_optimization>
        <context_efficiency>How can role definition optimize token usage for development?</context_efficiency>
        <dependency_analysis>What role analysis is sequential vs parallel for TDD setup?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>ROLE_DEFINITION: [role] with [expertise_level] for [domain] requiring [standards]</output_format>
      <validation>Role clearly defined with appropriate expertise level and enhanced reasoning</validation>
      <enforcement>BLOCK if role unclear or insufficient for task complexity</enforcement>
      <context_transfer>Role definition and expertise level for input analysis</context_transfer>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply RISE framework - Analyze Input and research thoroughly</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What input analysis and research is needed for optimal TDD approach?
          - What existing patterns and architecture need understanding?
          - How does research connect to role-appropriate test design?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Requirement Question: What exactly needs to be implemented/fixed based on requirements?]
          - [Architecture Question: What existing code, patterns, or architecture should I understand first?]
          - [Constraints Question: What are the constraints, dependencies, and integration points?]
          - [Research Question: What research is needed to ensure optimal approach?]
          - [TDD Question: How does research inform test design and implementation strategy?]
          - [Parallel Question: Can research operations be batched for 70% performance improvement?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this research approach optimal for the role and complexity?
          - What evidence supports the requirement analysis?
          - How will research findings guide TDD implementation success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can research operations be batched (Read, Grep, analysis) for 70% improvement?</tool_optimization>
        <context_efficiency>How can research optimize context window usage for development?</context_efficiency>
        <dependency_analysis>What research can be done in parallel vs sequential for TDD setup?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>INPUT_ANALYSIS: [requirement] affecting [components] requiring [research_findings]</output_format>
      <validation>Requirements analyzed with research-based understanding and enhanced reasoning</validation>
      <enforcement>BLOCK until comprehensive research and analysis completed</enforcement>
      <context_transfer>Research findings and requirements for TDD test design</context_transfer>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply RISE framework - Define Steps with TDD RED phase</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What step definition and test design is needed for TDD RED phase?
          - What comprehensive test scenarios need coverage?
          - How do steps align with RISE framework expectations and TDD methodology?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Steps Question: What are the specific steps for implementation?]
          - [Tests Question: What tests should I write to verify correctness?]
          - [TDD Question: How do steps align with TDD methodology?]
          - [Coverage Question: Are test scenarios comprehensive (normal, edge, error cases)?]
          - [Quality Question: Do tests meet role-appropriate standards and expectations?]
          - [Parallel Question: Can test design and step planning be optimized for efficiency?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this step sequence optimal for the role and requirement?
          - What evidence supports the test design approach?
          - How will these tests ensure quality and correctness?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can test writing and step definition be optimized for parallel execution?</tool_optimization>
        <context_efficiency>How can TDD setup optimize context window usage?</context_efficiency>
        <dependency_analysis>What test design can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>STEPS_WITH_TESTS: [step_sequence] with [failing_tests_created]</output_format>
      <validation>Steps defined and failing tests written for all acceptance criteria with enhanced reasoning</validation>
      <enforcement>BLOCK implementation until tests properly fail - use quality/tdd.md#red_phase</enforcement>
      <context_transfer>Test design and step sequence for GREEN phase implementation</context_transfer>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="standard">
      <action>Execute TDD GREEN phase - minimal implementation aligned with RISE expectations</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What minimal implementation approach will make tests pass?
          - How does implementation align with role expectations and TDD methodology?
          - What systematic approach ensures quality and efficiency?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Implementation Question: What's the simplest code that makes tests pass?]
          - [Role Question: Does implementation align with defined role and expertise level?]
          - [Steps Question: Am I following the defined steps systematically?]
          - [Testing Question: Are all tests now passing with focused implementation?]
          - [Quality Question: Does implementation meet role-appropriate standards?]
          - [Efficiency Question: Can implementation be optimized for performance?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this implementation approach optimal for the role and requirements?
          - What evidence supports the minimal implementation strategy?
          - How will this implementation ensure test success and quality?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can implementation and testing be optimized for parallel execution?</tool_optimization>
        <context_efficiency>How can GREEN phase optimize context window usage?</context_efficiency>
        <dependency_analysis>What implementation tasks can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>MINIMAL_IMPLEMENTATION: Code aligned with RISE framework and passing tests</output_format>
      <validation>All tests pass with role-appropriate, step-aligned implementation and enhanced reasoning</validation>
      <enforcement>BLOCK refactoring until GREEN achieved - use quality/tdd.md#green_phase</enforcement>
      <context_transfer>GREEN implementation for refactoring phase</context_transfer>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Execute TDD REFACTOR phase with RISE Expectations validation</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What refactoring approach will improve code to role standards?
          - How does refactoring align with RISE expectations and TDD methodology?
          - What design improvements maintain test integrity?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Improvement Question: How can I improve code to meet role expectations and standards?]
          - [Design Question: What design patterns align with defined expertise level?]
          - [Quality Question: Does refactored code meet the quality standards for my role?]
          - [Testing Question: Do tests remain green while achieving RISE expectations?]
          - [Standards Question: Does refactoring meet production-level quality requirements?]
          - [Efficiency Question: Can refactoring be optimized for maintainability and performance?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this refactoring approach optimal for the role and quality standards?
          - What evidence supports the design improvement strategy?
          - How will refactoring enhance long-term maintainability and quality?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can refactoring and testing be optimized for parallel execution?</tool_optimization>
        <context_efficiency>How can REFACTOR phase optimize context window usage?</context_efficiency>
        <dependency_analysis>What refactoring tasks can be parallelized safely?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>REFACTORED_CODE: Design improved to role standards with green tests</output_format>
      <validation>Code meets role expectations, quality improved, tests remain green with enhanced reasoning</validation>
      <enforcement>ROLLBACK if tests fail or quality below role standards</enforcement>
      <context_transfer>Refactored implementation for final validation</context_transfer>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply RISE framework - Validate Expectations and quality gates</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What final validation ensures RISE expectations and quality standards?
          - How do quality gates ensure production-level delivery?
          - What comprehensive validation confirms role-appropriate implementation?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Expectations Question: Does final deliverable meet all RISE framework expectations?]
          - [Coverage Question: Is test coverage ≥90% with role-appropriate quality?]
          - [Quality Question: Do all quality gates pass per production-standards.md?]
          - [Standards Question: Is implementation worthy of the defined expertise level?]
          - [Completeness Question: Are all requirements satisfied with appropriate quality?]
          - [Performance Question: Does implementation meet performance and efficiency standards?]
        </critical_thinking>
        <decision_reasoning>
          - Why does this validation approach ensure comprehensive quality?
          - What evidence supports the expectation fulfillment?
          - How will this validation confirm production readiness?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can validation operations be batched for 70% improvement?</tool_optimization>
        <context_efficiency>How can validation optimize context window usage?</context_efficiency>
        <dependency_analysis>What validation checks can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>EXPECTATION_VALIDATION: RISE expectations met, coverage [%], quality gates [status]</output_format>
      <validation>RISE expectations fulfilled, quality gates passed, role standards met with enhanced reasoning</validation>
      <enforcement>BLOCK completion until RISE expectations and quality standards achieved</enforcement>
      <context_transfer>Complete validation with quality confirmation</context_transfer>
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
    
    <checkpoint_enforcement>
      <checkpoint_3_red_phase>
        <tdd_validation>BLOCK unless failing tests exist for ALL acceptance criteria</tdd_validation>
        <test_execution>VERIFY tests fail with expected error messages</test_execution>
        <coverage_requirement>ENSURE edge cases and error conditions included</coverage_requirement>
        <quality_gate>Reference quality/tdd.md#red_phase_validation</quality_gate>
      </checkpoint_3_red_phase>
      
      <checkpoint_4_green_phase>
        <tdd_validation>BLOCK unless ALL tests pass with minimal implementation</tdd_validation>
        <implementation_scope>VERIFY no features beyond test requirements</implementation_scope>
        <test_execution>CONFIRM all tests green with current implementation</test_execution>
        <quality_gate>Reference quality/tdd.md#green_phase_validation</quality_gate>
      </checkpoint_4_green_phase>
      
      <checkpoint_5_refactor_phase>
        <tdd_validation>BLOCK unless tests remain green during refactoring</tdd_validation>
        <design_improvement>VERIFY code quality enhanced while maintaining functionality</design_improvement>
        <test_integrity>ENSURE no test modifications during refactoring</test_integrity>
        <quality_gate>Reference quality/tdd.md#refactor_phase_validation</quality_gate>
      </checkpoint_5_refactor_phase>
      
      <checkpoint_6_final_validation>
        <tdd_validation>BLOCK unless 90%+ test coverage achieved</tdd_validation>
        <quality_standards>VERIFY production-ready quality with comprehensive testing</quality_standards>
        <integration_testing>CONFIRM integration tests pass for external dependencies</integration_testing>
        <quality_gate>Reference quality/tdd.md#final_validation</quality_gate>
      </checkpoint_6_final_validation>
    </checkpoint_enforcement>
    
    <blocking_conditions>
      <condition>Implementation attempted before RISE framework application</condition>
      <condition>Research skipped before requirement analysis</condition>
      <condition>Implementation attempted before tests written</condition>
      <condition>Tests pass when they should fail (incorrect tests)</condition>
      <condition>Implementation exceeds test requirements (over-engineering)</condition>
      <condition>Refactoring breaks any existing tests</condition>
      <condition>Final deliverable below role-appropriate quality standards</condition>
      <condition>TDD cycle skipped or bypassed for expedited delivery</condition>
      <condition>Test coverage below 90% for new code</condition>
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
  
  <claude_4_module_execution enforcement="MANDATORY" thinking_mode="interleaved">
    <core_stack order="advanced_sequential" optimization="context_hierarchical">
      <module thinking="enabled" cache="predictive">quality/critical-thinking.md - Claude 4 enhanced 30-second analysis before any action</module>
      <module thinking="enabled" cache="predictive">quality/tdd.md - Strict RED-GREEN-REFACTOR enforcement with Claude 4 optimization</module>
      <module thinking="enabled" cache="predictive">development/task-management.md - Task execution workflow with RISE framework integration</module>
      <module thinking="enabled" cache="predictive">quality/production-standards.md - Quality gate validation with enhanced reasoning</module>
    </core_stack>
    <contextual_modules evaluation="intelligent_conditional" analysis="claude_4_enhanced">
      <conditional module="patterns/session-management.md" condition="complex_task OR multiple_files" thinking="adaptive" fallback="quality/critical-thinking.md"/>
      <conditional module="git/conventional-commits.md" condition="task_complete" thinking="adaptive" fallback="quality/production-standards.md"/>
      <conditional module="quality/pre-commit.md" condition="code_changes" thinking="adaptive" fallback="quality/tdd.md"/>
      <conditional module="frameworks/rise.md" condition="framework_optimization_needed" thinking="adaptive" fallback="development/task-management.md"/>
    </contextual_modules>
    <support_modules order="optimized_parallel" batching="mandatory" speedup="70_percent">
      <module batch_group="analysis" tools="Read,Grep">patterns/pattern-library.md - Parallel pattern analysis</module>
      <module batch_group="validation" tools="quality_gates">quality/universal-quality-gates.md - Concurrent quality validation</module>
    </support_modules>
    <performance_monitoring>
      <metric name="execution_time" target="70_percent_improvement"/>
      <metric name="context_efficiency" target="token_optimization"/>
      <metric name="thinking_quality" target="enhanced_reasoning"/>
      <metric name="tdd_compliance" target="100_percent_enforcement"/>
    </performance_monitoring>
  </claude_4_module_execution>
  
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