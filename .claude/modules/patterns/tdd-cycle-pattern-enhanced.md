| version | last_updated | status |
|---------|--------------|--------|
| 1.1.0   | 2025-07-19   | enhanced |

# TDD Cycle Pattern Module (Enhanced with Helpful Errors)

────────────────────────────────────────────────────────────────────────────────

**Enhancement**: This version implements helpful error messages that guide users to solutions

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="tdd_cycle_pattern_enhanced" category="patterns">
  
  <purpose>
    Test-driven development workflow with Red-Green-Refactor cycle, now with helpful error messages that guide users through common issues and provide actionable solutions.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Any code implementation task</condition>
    <condition type="explicit">Bug fixes requiring regression tests</condition>
    <condition type="explicit">Feature development work</condition>
    <condition type="explicit">Refactoring existing code</condition>
    <condition type="explicit">Code quality improvement</condition>
  </trigger_conditions>
  
  <pre_flight_checks>
    <check name="environment_validation">
      <validation>
        <!-- Check test directory exists -->
        if not exists(test_directory):
          return HelpfulError(
            "❌ Cannot create test file - test directory not found",
            context=f"Looking for: {expected_test_dirs}",
            solutions=[
              f"Create test directory: mkdir {default_test_dir}",
              "Or specify custom location in PROJECT_CONFIG.xml",
              "<test_directory>my_custom_tests</test_directory>"
            ],
            why="TDD requires tests to be written first. We need a place to put them!"
          )
        
        <!-- Check test framework available -->
        if not command_exists(test_command):
          return HelpfulError(
            "❌ Test framework not available",
            context=f"Tried to run: {test_command}",
            solutions=[
              f"Install {suggested_framework}: {install_command}",
              "Or specify your test command in PROJECT_CONFIG.xml:",
              f"<test_command>{alternative_command}</test_command>"
            ],
            next_step="Then run /task again"
          )
        
        <!-- Check coverage tool available -->
        if not command_exists(coverage_command):
          return Warning(
            "⚠️  Coverage tool not found",
            context="Continuing without coverage measurement",
            solution=f"To enable: {coverage_install_command}",
            impact="Won't be able to verify 90% coverage requirement"
          )
      </validation>
    </check>
  </pre_flight_checks>
  
  <implementation>
    
    <phase name="red_phase_write_failing_test" order="1">
      <requirements>
        Requirements must be clearly defined
        Test framework must be available
        Test structure must be planned
        No implementation code should exist yet
      </requirements>
      
      <helpful_validations>
        <!-- Check for existing implementation -->
        if implementation_exists_without_test():
          return HelpfulError(
            "⚠️  TDD Violation: Implementation exists without test",
            found=f"{implementation_file} (modified)",
            missing=f"{expected_test_file}",
            tdd_process=[
              "1. Write a failing test that describes the behavior",
              "2. Run test (see it fail - RED)",
              "3. Write minimal code to pass (GREEN)",
              "4. Refactor while keeping tests passing"
            ],
            to_fix=[
              f"Create test first: /task \"create test for {feature_name}\"",
              "Or acknowledge violation: /task --skip-tdd (not recommended)"
            ]
          )
        
        <!-- Guide test creation -->
        if unsure_how_to_test():
          return Guidance(
            "💡 Need help writing tests?",
            examples=[
              f"For {feature_type}: {test_example}",
              f"Test structure: {test_template}",
              f"Edge cases to consider: {edge_case_list}"
            ],
            resources=[
              "See existing tests: {similar_test_file}",
              "Testing patterns: .claude/patterns/testing-patterns.md"
            ]
          )
      </helpful_validations>
      
      <actions>
        Create tests that define the desired behavior
        Write tests that specify exactly what the code should do
        Make sure tests fail for the right reasons
        Cover normal cases, edge cases, and error conditions
        Use clear, descriptive test names
        Verify tests fail with expected error messages
      </actions>
      
      <atomic_commit_integration>
        <checkpoint>git add -A && git commit -m "TDD RED: [test_description] - failing tests created"</checkpoint>
        <validation_before_commit>
          <!-- Helpful validation messages -->
          if tests_not_failing():
            return HelpfulError(
              "❌ Tests must fail in RED phase",
              problem="Your tests are passing without implementation",
              likely_causes=[
                "Test might not be testing the right thing",
                "Feature might already be implemented",
                "Test might have a bug"
              ],
              to_fix=[
                "Review test logic",
                "Ensure test actually calls the code to be implemented",
                "Check test assertions are correct"
              ]
            )
        </validation_before_commit>
      </atomic_commit_integration>
    </phase>
    
    <phase name="green_phase_make_tests_pass" order="2">
      <requirements>
        Failing tests from red phase must exist
        Tests must be running and failing correctly
        Implementation environment must be ready
      </requirements>
      
      <helpful_validations>
        <!-- Guide minimal implementation -->
        if implementation_too_complex():
          return Warning(
            "⚠️  Implementation might be too complex",
            observed="Adding features beyond test requirements",
            reminder="Write MINIMAL code to make tests pass",
            examples=[
              "❌ Bad: Full validation framework for one test",
              "✅ Good: Simple if statement that satisfies test"
            ],
            why="Complex code without tests is risky"
          )
        
        <!-- Help with test failures -->
        if tests_still_failing():
          return HelpfulError(
            "❌ Tests still failing after implementation",
            failures=test_failure_summary,
            likely_issues=[
              "Implementation doesn't match test expectations",
              "Missing edge case handling",
              "Incorrect return values"
            ],
            debugging_tips=[
              f"Run single test: {run_single_test_command}",
              f"Add debug output: {debug_suggestion}",
              f"Check test vs implementation: {comparison_tip}"
            ]
          )
      </helpful_validations>
      
      <actions>
        Write minimal code to make tests pass
        Focus only on making the current tests green
        Avoid premature optimization
        Run tests frequently to ensure they pass
      </actions>
      
      <coverage_validation>
        if coverage_below_threshold():
          return HelpfulError(
            "❌ Test coverage too low",
            current=f"{current_coverage}%",
            required="90%",
            uncovered_code=[
              f"{file}:{lines} ({description})"
              for file, lines, description in uncovered_areas
            ],
            to_fix=[
              "Add tests for error scenarios",
              "Test edge cases",
              f"Run: {coverage_report_command}"
            ],
            example_test=generate_test_for_uncovered_code()
          )
      </coverage_validation>
    </phase>
    
    <phase name="refactor_phase_improve_code_quality" order="3">
      <requirements>
        All tests must be passing (green)
        Code quality issues must be identified
        Refactoring plan must be established
      </requirements>
      
      <helpful_validations>
        <!-- Prevent refactoring with broken tests -->
        if any_test_failing():
          return HelpfulError(
            "❌ Cannot refactor with failing tests",
            failing_tests=list_failing_tests(),
            rule="All tests must be GREEN before refactoring",
            to_fix=[
              "Fix failing tests first",
              f"Run: {test_command}",
              "Or revert changes: git checkout ."
            ],
            why="Refactoring requires a safety net of passing tests"
          )
        
        <!-- Guide safe refactoring -->
        if refactoring_breaks_tests():
          return HelpfulError(
            "❌ Refactoring broke tests",
            broken_tests=newly_failing_tests(),
            advice="Refactoring should NOT change behavior",
            to_fix=[
              "Revert last change: git checkout .",
              "Make smaller refactoring steps",
              "Run tests after each small change"
            ],
            safe_refactorings=[
              "Extract method",
              "Rename variable",
              "Remove duplication"
            ]
          )
      </helpful_validations>
      
      <actions>
        Improve code structure while keeping tests green
        Remove duplication and apply design patterns
        Run tests after each refactoring step
        Make small, incremental improvements
      </actions>
    </phase>
    
  </implementation>
  
  <quality_gates>
    <gate name="test_first_enforcement" severity="blocking">
      <validation>
        if no_failing_tests_exist():
          return HelpfulError(
            "🚫 Quality Gate Failed: Test-First Development",
            violation="Writing code before tests",
            required_process=[
              "1. Write failing test (RED)",
              "2. Write code to pass (GREEN)", 
              "3. Improve code (REFACTOR)"
            ],
            bypass="Use --skip-tdd flag (not recommended)",
            learn_more=".claude/system/quality/tdd.md"
          )
      </validation>
    </gate>
    
    <gate name="coverage_requirements" severity="blocking">
      <validation>
        if coverage < 90:
          return HelpfulError(
            "🚫 Quality Gate Failed: Insufficient Coverage",
            metric=f"Coverage: {coverage}% (Required: 90%)",
            gaps=show_uncovered_lines_with_context(),
            quick_wins=suggest_easy_tests_to_add(),
            commands=[
              coverage_report_command,
              coverage_html_command
            ]
          )
      </validation>
    </gate>
  </quality_gates>
  
  <error_handling>
    <error code="TDD001" severity="critical">
      <old_message>Implementation attempted without failing tests - enforce red phase</old_message>
      <helpful_message>
        ❌ TDD Violation: Cannot write code without tests
        
        You're trying to implement before writing tests.
        
        TDD Process:
        1. Write a test that fails (describes what you want)
        2. See it fail (confirms test is correct)
        3. Write code to make it pass
        4. Refactor while keeping tests green
        
        To fix:
        → Write your test first in: {suggested_test_file}
        → Example: {test_example_for_feature}
        → Then implement the feature
        
        Why this matters:
        Tests written after code often miss edge cases and
        don't properly define the intended behavior.
      </helpful_message>
    </error>
    
    <error code="TDD002" severity="critical">
      <old_message>Tests passing without implementation - review test quality</old_message>
      <helpful_message>
        ⚠️  Test Quality Issue: Tests passing without code
        
        Your test is passing but you haven't written the implementation yet.
        This means the test isn't actually testing your new feature.
        
        Common causes:
        - Test is checking existing functionality
        - Test assertions are incorrect
        - Test isn't calling the right code
        
        To fix:
        → Review your test: {test_file}
        → Ensure it calls: {expected_function}
        → Check assertions test new behavior
        → The test should fail until you implement
        
        Example of a good failing test:
        {contextual_test_example}
      </helpful_message>
    </error>
    
    <error code="TDD003" severity="critical">
      <old_message>Refactoring attempted with failing tests - ensure green phase</old_message>
      <helpful_message>
        ❌ Cannot refactor with failing tests
        
        Failing tests: {list_of_failing_tests}
        
        The refactoring phase requires all tests to be passing.
        This ensures your refactoring doesn't break functionality.
        
        To fix:
        1. Get all tests passing first
           Run: {test_command}
        
        2. Fix any failures:
           {specific_failure_hints}
        
        3. Once all tests are green, then refactor
        
        If you're stuck:
        → Revert recent changes: git checkout .
        → Start with smaller implementation
        → Ask for help with specific test failures
      </helpful_message>
    </error>
    
    <error code="TDD004" severity="warning">
      <old_message>Coverage below minimum threshold - improve test coverage</old_message>
      <helpful_message>
        ⚠️  Coverage Below Requirements
        
        Current: {current_coverage}%
        Required: 90%
        Gap: {coverage_gap}%
        
        Uncovered areas:
        {uncovered_report_with_line_numbers}
        
        Quick fixes - Add tests for:
        {prioritized_test_suggestions}
        
        Commands:
        → See coverage: {coverage_command}
        → HTML report: {coverage_html_command}
        → Run specific test: {test_single_command}
        
        Example test for uncovered code:
        {generated_test_example}
      </helpful_message>
    </error>
    
    <error code="TDD005" severity="warning">
      <old_message>Large refactoring step detected - break into smaller steps</old_message>
      <helpful_message>
        ⚠️  Refactoring Too Large
        
        Changed files: {count}
        Changed lines: {line_count}
        
        Large refactorings are risky and hard to debug if tests break.
        
        Better approach:
        1. Refactor one thing at a time
        2. Run tests after each change
        3. Commit working states
        
        Safe refactoring sequence:
        {suggested_refactoring_steps}
        
        If tests are broken now:
        → Revert: git checkout .
        → Start with smallest change
        → Test after each step
      </helpful_message>
    </error>
  </error_handling>
  
  <continuous_guidance>
    <progress_indicators>
      🔴 RED Phase: Writing failing tests...
      🟢 GREEN Phase: Making tests pass...
      🔵 REFACTOR Phase: Improving code quality...
      ✅ TDD Cycle Complete!
    </progress_indicators>
    
    <helpful_prompts>
      <!-- Context-aware suggestions during each phase -->
      <red_phase>
        "💡 Writing test for {feature}? Consider testing: {test_scenarios}"
      </red_phase>
      <green_phase>
        "💡 Stuck making tests pass? Try: {implementation_hint}"
      </green_phase>
      <refactor_phase>
        "💡 Code smell detected: {smell_type}. Consider: {refactoring_pattern}"
      </refactor_phase>
    </helpful_prompts>
  </continuous_guidance>
  
</module>
```

## Benefits of Enhanced Error Handling

### For Users
1. **Immediate Understanding**: Know exactly what went wrong
2. **Clear Next Steps**: Actionable solutions for every error
3. **Learning Opportunity**: Understand TDD principles through guidance
4. **Reduced Frustration**: No more cryptic error codes

### For Framework
1. **Higher Success Rate**: Users complete tasks successfully
2. **Better Adoption**: TDD principles taught through practice
3. **Fewer Support Issues**: Self-service error resolution
4. **Quality Improvement**: Users write better tests with guidance

## Implementation Strategy

1. **Phase 1**: Update error messages in this module
2. **Phase 2**: Test with real scenarios
3. **Phase 3**: Roll out to other modules
4. **Phase 4**: Measure user success improvement

## Measuring Success

- Error resolution time: 10-30 min → 1-5 min
- User frustration: High → Low
- TDD adoption: 60% → 90%
- Support requests: -70%

---

**Note**: This enhanced version maintains all existing functionality while adding helpful error messages throughout the TDD workflow.