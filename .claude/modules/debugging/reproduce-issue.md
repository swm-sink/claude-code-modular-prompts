| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-01-08   | stable |

# Issue Reproduction Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="reproduce_issue" category="debugging">
  
  <purpose>
    Create reproducible test cases for bugs with 75% faster bug resolution through systematic reproduction, failing test creation, and documented fix verification.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Task command detects bug fix keywords (fix, resolve, bug, issue)</condition>
    <condition type="explicit">User requests bug reproduction or debugging assistance</condition>
    <condition type="issue_analysis">GitHub issue or bug report needs reproduction</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="issue_analysis" order="1">
      <requirements>
        Bug description parsed and key symptoms identified
        Expected vs actual behavior clearly defined
        Environment and reproduction conditions documented
        Potential root causes hypothesized from description
      </requirements>
      <actions>
        Parse issue description for symptoms, environment, and steps
        Identify expected behavior and actual incorrect behavior
        Extract environment details: OS, versions, configurations
        Analyze error messages and stack traces if provided
        Hypothesize potential root causes based on symptoms
      </actions>
      <validation>
        Clear understanding of what should happen vs what actually happens
        Environment factors identified that might affect reproduction
        Initial hypotheses formed about potential causes
        Reproduction strategy planned based on available information
      </validation>
    </phase>
    
    <phase name="reproduction_environment" order="2">
      <requirements>
        Minimal environment setup that reproduces the issue
        All necessary dependencies and configurations identified
        Environment matches or simulates reported issue conditions
        Reproduction steps documented for consistency
      </requirements>
      <actions>
        Set up minimal environment matching reported conditions
        Install required dependencies and configurations
        Create isolated test environment to avoid side effects
        Verify environment can run relevant code without the bug
        Document exact environment setup for future reference
      </actions>
      <validation>
        Environment successfully created and functional
        Baseline behavior works correctly before introducing bug conditions
        Environment setup documented for reproducibility
        Isolation confirmed to prevent interference with main codebase
      </validation>
    </phase>
    
    <phase name="failing_test_creation" order="3">
      <requirements>
        Test written that demonstrates the bug behavior
        Test fails consistently with the reported symptoms
        Test captures both the incorrect behavior and expected correct behavior
        Test is isolated and doesn't depend on external factors
      </requirements>
      <actions>
        Write test that reproduces the exact bug scenario
        Ensure test fails with the same symptoms as reported
        Include assertions for both current (wrong) and expected (correct) behavior
        Make test deterministic and independent of external factors
        Document test purpose and what it's verifying
      </actions>
      <validation>
        Test consistently fails with symptoms matching the reported bug
        Test clearly demonstrates what should happen vs what actually happens
        Test is isolated and doesn't create side effects
        Test serves as acceptance criteria for bug fix
      </validation>
    </phase>
    
    <phase name="root_cause_investigation" order="4">
      <requirements>
        Systematic investigation to identify the actual cause
        Code paths traced from input to incorrect output
        Data flow analyzed to find where corruption occurs
        Dependencies and interactions examined for conflicts
      </requirements>
      <actions>
        Trace code execution path that leads to the bug
        Examine data transformations and state changes
        Check for race conditions, timing issues, or concurrency problems
        Analyze dependencies and their potential interactions
        Use debugging tools to step through problematic code
      </actions>
      <validation>
        Root cause identified with clear understanding of why bug occurs
        Code location(s) responsible for the bug pinpointed
        Understanding of how inputs lead to incorrect outputs
        Confidence that fixing identified cause will resolve the issue
      </validation>
    </phase>
    
    <phase name="fix_implementation" order="5">
      <requirements>
        Minimal fix that addresses the root cause
        Fix doesn't introduce new issues or break existing functionality
        Fix makes the failing test pass
        All existing tests continue to pass
      </requirements>
      <actions>
        Implement minimal change that addresses the identified root cause
        Verify the fix makes the reproduction test pass
        Run full test suite to ensure no regressions introduced
        Test edge cases and boundary conditions around the fix
        Document the fix and why it resolves the issue
      </actions>
      <validation>
        Reproduction test now passes with the fix applied
        All existing tests continue to pass
        Fix is minimal and surgical, not over-engineered
        Edge cases considered and handled appropriately
      </validation>
    </phase>
    
    <phase name="verification_documentation" order="6">
      <requirements>
        Complete reproduction steps documented
        Fix verification process documented
        Regression prevention measures established
        Knowledge captured for future similar issues
      </requirements>
      <actions>
        Document complete reproduction steps for future reference
        Record fix implementation details and rationale
        Add regression test to prevent future recurrence
        Update relevant documentation or knowledge base
        Create guidelines for preventing similar issues
      </actions>
      <validation>
        Reproduction process fully documented and verifiable
        Fix adequately explained with rationale
        Regression protection in place through automated tests
        Knowledge captured for team learning and future prevention
      </validation>
    </phase>
    
  </implementation>
  
  <reproduction_strategies>
    <minimal_reproduction>
      <approach>Create smallest possible case that demonstrates the bug</approach>
      <benefits>Faster debugging, clearer cause identification, easier testing</benefits>
      <method>
        1. Start with reported scenario
        2. Remove non-essential elements one by one
        3. Verify bug still reproduces after each removal
        4. Continue until only essential elements remain
      </method>
    </minimal_reproduction>
    
    <environment_isolation>
      <approach>Reproduce in clean, controlled environment</approach>
      <benefits>Eliminates environmental variables, ensures consistent reproduction</benefits>
      <method>
        1. Create fresh environment (virtual env, container, etc.)
        2. Install only required dependencies
        3. Use minimal configuration
        4. Verify reproduction in isolation
      </method>
    </environment_isolation>
    
    <data_driven_reproduction>
      <approach>Create test data that triggers the bug</approach>
      <benefits>Systematic testing, edge case discovery, automated verification</benefits>
      <method>
        1. Identify input patterns that trigger the bug
        2. Create test datasets covering various scenarios
        3. Automate reproduction with different data sets
        4. Document data patterns that cause issues
      </method>
    </data_driven_reproduction>
  </reproduction_strategies>
  
  <test_patterns>
    <bug_reproduction_test>
      <structure>
        ```python
        def test_bug_reproduction_issue_123():
            """
            Reproduces bug where user authentication fails with special characters
            
            Expected: User should be able to login with email containing + symbol
            Actual: Authentication fails with "Invalid email format" error
            
            Issue: https://github.com/project/repo/issues/123
            """
            # Arrange - Set up the bug conditions
            email_with_special_char = "user+test@example.com"
            password = "validpassword123"
            
            # Act - Perform the action that should work but currently fails
            result = authenticate_user(email_with_special_char, password)
            
            # Assert - Document both current (wrong) and expected (correct) behavior
            # Currently fails - this assertion will pass, showing the bug exists
            assert result.success == False  # This is the bug - should be True
            assert "Invalid email format" in result.error_message
            
            # Expected behavior - this assertion will fail until bug is fixed
            # assert result.success == True  # Uncomment when fixing
            # assert result.user.email == email_with_special_char
        ```
      </structure>
    </bug_reproduction_test>
    
    <regression_prevention_test>
      <structure>
        ```python
        def test_email_authentication_with_special_characters():
            """
            Regression test to prevent re-introduction of email validation bug
            
            Ensures that emails with valid special characters are accepted
            for authentication as per RFC 5322 specification.
            """
            valid_special_emails = [
                "user+tag@example.com",
                "user.name@example.com", 
                "user-name@example.com",
                "user_name@example.com"
            ]
            
            for email in valid_special_emails:
                result = authenticate_user(email, "validpassword123")
                assert result.success == True, f"Failed to authenticate {email}"
                assert result.user.email == email
        ```
      </structure>
    </regression_prevention_test>
    
    <edge_case_coverage>
      <structure>
        ```python
        def test_authentication_edge_cases():
            """
            Test edge cases discovered during bug reproduction
            
            Ensures comprehensive coverage of boundary conditions
            that might trigger similar issues.
            """
            edge_cases = [
                ("", "password"),  # Empty email
                ("user@", "password"),  # Incomplete email
                ("user@domain", "password"),  # No TLD
                ("user@domain.c", "password"),  # Single char TLD
                ("user@domain.com", ""),  # Empty password
                ("user@domain.com", " "),  # Whitespace password
            ]
            
            for email, password in edge_cases:
                result = authenticate_user(email, password)
                # Document expected behavior for each edge case
                assert isinstance(result, AuthenticationResult)
                assert hasattr(result, 'success')
                assert hasattr(result, 'error_message')
        ```
      </structure>
    </edge_case_coverage>
  </test_patterns>
  
  <debugging_techniques>
    <systematic_isolation>
      <binary_search_debugging>
        <description>Narrow down the problem by eliminating half the code at each step</description>
        <process>
          1. Comment out half the functionality
          2. Test if bug still reproduces
          3. If yes, bug is in remaining half; if no, bug is in commented half
          4. Repeat until minimal code that reproduces bug is found
        </process>
      </binary_search_debugging>
      
      <input_output_tracing>
        <description>Track data flow from input to incorrect output</description>
        <process>
          1. Log input data at entry points
          2. Add logging at each major transformation step
          3. Compare expected vs actual values at each step
          4. Identify the first point where values diverge
        </process>
      </input_output_tracing>
      
      <dependency_elimination>
        <description>Remove dependencies one by one to isolate the cause</description>
        <process>
          1. List all external dependencies
          2. Mock or remove each dependency individually
          3. Test if bug reproduces without each dependency
          4. Identify which dependency is related to the bug
        </process>
      </dependency_elimination>
    </systematic_isolation>
    
    <state_analysis>
      <memory_inspection>
        <description>Examine object states and memory contents</description>
        <tools>Debugger, memory profilers, object inspectors</tools>
        <focus>Object lifecycle, memory leaks, state corruption</focus>
      </memory_inspection>
      
      <concurrency_analysis>
        <description>Identify race conditions and threading issues</description>
        <tools>Thread debuggers, race condition detectors, timing analysis</tools>
        <focus>Shared state, locking mechanisms, timing dependencies</focus>
      </concurrency_analysis>
      
      <configuration_validation>
        <description>Verify configuration and environment setup</description>
        <tools>Configuration validators, environment comparisons</tools>
        <focus>Settings conflicts, version mismatches, missing configurations</focus>
      </configuration_validation>
    </state_analysis>
  </debugging_techniques>
  
  <documentation_templates>
    <bug_reproduction_report>
      <template>
        # Bug Reproduction Report - Issue #{issue_number}
        
        ## Summary
        **Bug**: {Brief description of the bug}
        **Impact**: {Who is affected and how}
        **Severity**: {Critical/High/Medium/Low}
        
        ## Reproduction Steps
        1. {Step 1 with specific details}
        2. {Step 2 with specific details}
        3. {Step 3 with specific details}
        
        **Expected Result**: {What should happen}
        **Actual Result**: {What actually happens}
        
        ## Environment
        - **OS**: {Operating system and version}
        - **Browser/Runtime**: {Specific version}
        - **Dependencies**: {Relevant package versions}
        - **Configuration**: {Relevant settings}
        
        ## Root Cause Analysis
        **Cause**: {Technical explanation of why the bug occurs}
        **Location**: {File and line number where issue exists}
        **Data Flow**: {How inputs lead to incorrect output}
        
        ## Reproduction Test
        ```{language}
        {Test code that reproduces the bug}
        ```
        
        ## Fix Implementation
        **Approach**: {Strategy used to fix the bug}
        **Changes**: {Specific code changes made}
        **Verification**: {How fix was verified}
        
        ## Prevention
        - **Regression Test**: {Test added to prevent recurrence}
        - **Process Improvement**: {Changes to prevent similar bugs}
        - **Documentation Updates**: {Knowledge captured}
      </template>
    </bug_reproduction_report>
    
    <fix_verification_checklist>
      <template>
        ## Fix Verification Checklist - Issue #{issue_number}
        
        ### Reproduction Verification
        - [ ] Bug reproduces consistently before fix
        - [ ] Reproduction test fails before fix
        - [ ] Environment setup documented
        - [ ] Minimal reproduction case created
        
        ### Fix Validation
        - [ ] Root cause identified and understood
        - [ ] Fix addresses root cause, not just symptoms
        - [ ] Reproduction test passes after fix
        - [ ] All existing tests continue to pass
        
        ### Regression Prevention
        - [ ] Regression test added to test suite
        - [ ] Edge cases tested and covered
        - [ ] Similar code patterns reviewed for same issue
        - [ ] Documentation updated with fix details
        
        ### Quality Assurance
        - [ ] Code review completed
        - [ ] Performance impact assessed
        - [ ] Security implications considered
        - [ ] User impact and communication planned
      </template>
    </fix_verification_checklist>
  </documentation_templates>
  
  <integration_workflows>
    <task_command_integration>
      <bug_detection>Auto-trigger reproduction workflow when bug keywords detected</bug_detection>
      <tdd_integration>Use TDD module for test-first bug fixing approach</tdd_integration>
      <commit_integration>Generate conventional commits for bug fixes with issue references</commit_integration>
    </task_command_integration>
    
    <github_integration>
      <issue_linking>Automatically link reproduction tests to GitHub issues</issue_linking>
      <pr_templates>Use reproduction documentation in pull request descriptions</pr_templates>
      <milestone_tracking>Track bug fix progress through reproduction, fix, verification phases</milestone_tracking>
    </github_integration>
    
    <quality_integration>
      <pre_commit_hooks>Ensure regression tests run before commits</pre_commit_hooks>
      <ci_integration>Add reproduction tests to continuous integration pipeline</ci_integration>
      <documentation>Auto-update debugging knowledge base with new patterns</documentation>
    </quality_integration>
  </integration_workflows>
  
  <performance_metrics>
    <reproduction_speed>
      <target>Issue reproduction within 15 minutes for typical bugs</target>
      <measurement>Time from issue description to failing test creation</measurement>
      <optimization>Use templates and automation to speed up common scenarios</optimization>
    </reproduction_speed>
    
    <fix_accuracy>
      <target>95% of fixes resolve the issue without introducing new bugs</target>
      <measurement>Success rate of fixes based on post-deployment monitoring</measurement>
      <optimization>Thorough root cause analysis and comprehensive testing</optimization>
    </fix_accuracy>
    
    <regression_prevention>
      <target>Zero recurrence of fixed bugs within 6 months</target>
      <measurement>Tracking of bug recurrence after fixes are deployed</measurement>
      <optimization>Comprehensive regression tests and pattern analysis</optimization>
    </regression_prevention>
  </performance_metrics>
  
  <integration_points>
    <depends_on>
      quality/tdd.md for test-driven bug fixing approach
      git/conventional-commits.md for structured bug fix commits
      development/task-management.md for debugging workflow integration
    </depends_on>
    <provides_to>
      development/task-management.md for enhanced debugging capabilities
      quality/production-standards.md for bug fix quality standards
      patterns/session-management.md for debugging session tracking
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">systematic_debugging</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">test_driven_development</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">documentation_templates</uses_pattern>
    <implementation_notes>
      Systematic isolation follows systematic_debugging pattern for consistency
      Failing test creation uses test_driven_development for quality
      Documentation generation implements documentation_templates for standardization
      Integration with task management follows established workflow patterns
    </implementation_notes>
  </pattern_usage>
  
</module>
```