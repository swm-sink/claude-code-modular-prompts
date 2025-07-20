| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-19   | production |

# TDD Anti-Pattern Enforcement
**Agent 11 - Hard Restrictions and Enforcement Mechanisms**

## Purpose

**CRITICAL ENFORCEMENT**: Hard restrictions and blocking mechanisms to prevent TDD anti-patterns that undermine test quality and development effectiveness.

## Anti-Pattern Categories & Enforcement

### 1. God Object Detection & Prevention

#### Detection Criteria
```xml
<god_object_detection enforcement="BLOCKING">
  <size_limits>
    <lines_of_code>500 maximum per class/file</lines_of_code>
    <method_count>20 maximum methods per class</method_count>
    <parameter_count>5 maximum parameters per method</parameter_count>
    <cyclomatic_complexity>10 maximum per method</cyclomatic_complexity>
  </size_limits>
  
  <responsibility_detection>
    <multiple_concerns>Class handling >3 distinct responsibilities</multiple_concerns>
    <excessive_dependencies>Class depending on >10 other classes</excessive_dependencies>
    <data_manipulation>Class directly manipulating >5 different data structures</data_manipulation>
  </responsibility_detection>
  
  <enforcement_actions>
    <block_commit>Prevent commit with clear refactoring requirements</block_commit>
    <refactoring_guidance>Provide specific decomposition recommendations</refactoring_guidance>
    <rollback_trigger>git reset --hard HEAD~1 if god object detected</rollback_trigger>
  </enforcement_actions>
</god_object_detection>
```

#### Enforcement Messages
```
ERROR: God Object Detected
- File: user_service.py (847 lines, 34 methods)
- BLOCKING: Commit prevented until refactored
- REQUIRED: Break into UserService, UserValidator, UserRepository
- GUIDANCE: Each class should handle ONE responsibility
- COMMAND: git reset --hard HEAD~1 (rollback)
```

### 2. Fake Test Prevention

#### Fake Test Detection
```xml
<fake_test_prevention enforcement="BLOCKING">
  <empty_assertions>
    <detection>Tests with no assert statements</detection>
    <detection>Tests with only assert True or assert False</detection>
    <detection>Tests with placeholder assertions</detection>
    <action>BLOCK with requirement for meaningful assertions</action>
  </empty_assertions>
  
  <meaningless_assertions>
    <detection>assert 1 == 1 (always true)</detection>
    <detection>assert len(result) (existence check only)</detection>
    <detection>Mock assertions without behavior verification</detection>
    <action>BLOCK with requirement for real behavior testing</action>
  </meaningless_assertions>
  
  <behavior_verification>
    <required>assert_called_with() with specific parameters</required>
    <required>assertEquals() with expected vs actual values</required>
    <required>Behavior verification, not just existence checks</required>
    <required>Edge case and error condition testing</required>
  </behavior_verification>
</fake_test_prevention>
```

#### Real Test Requirements
```python
# ❌ BLOCKED - Fake Test
def test_user_creation():
    user = create_user("test")
    assert user  # Empty assertion

# ✅ ALLOWED - Real Test  
def test_user_creation_sets_correct_attributes():
    user = create_user("john_doe", "john@example.com")
    assert user.username == "john_doe"
    assert user.email == "john@example.com"
    assert user.created_at is not None
    assert user.id is not None
```

### 3. Excessive Mocking Limits

#### Mocking Restrictions
```xml
<excessive_mocking_prevention enforcement="BLOCKING">
  <mock_limits>
    <max_mocks_per_test>3</max_mocks_per_test>
    <integration_test_ratio>30% minimum (no mocks)</integration_test_ratio>
    <real_dependency_tests>Required for database, API, file operations</real_dependency_tests>
  </mock_limits>
  
  <mock_quality_requirements>
    <specific_assertions>Mock calls must verify specific parameters</specific_assertions>
    <behavior_verification>Verify interactions, not just call counts</behavior_verification>
    <state_verification>Verify state changes, not just method calls</state_verification>
  </mock_quality_requirements>
  
  <integration_requirements>
    <database_tests>Real database tests for data persistence</database_tests>
    <api_tests>Real API tests for external integrations</api_tests>
    <end_to_end_tests>Complete workflow tests without mocks</end_to_end_tests>
  </integration_requirements>
</excessive_mocking_prevention>
```

#### Enforcement Examples
```python
# ❌ BLOCKED - Too Many Mocks
@patch('module.database')
@patch('module.cache')  
@patch('module.logger')
@patch('module.validator')  # 4 mocks - BLOCKED
def test_user_service():
    pass

# ✅ ALLOWED - Balanced Testing
def test_user_service_with_real_database():
    # Integration test with real database
    user = UserService().create_user("test")
    saved_user = UserService().get_user(user.id)
    assert saved_user.username == "test"

@patch('module.external_api')  # 1 mock for external dependency
def test_user_service_api_failure():
    # Test error handling with mocked external API
    pass
```

### 4. Test Quality Enforcement

#### Quality Requirements
```xml
<test_quality_enforcement enforcement="BLOCKING">
  <assertion_requirements>
    <minimum_assertions>1 meaningful assertion per test</minimum_assertions>
    <assertion_specificity>Assertions must test specific behavior</assertion_specificity>
    <edge_case_coverage>Tests must cover error conditions</edge_case_coverage>
  </assertion_requirements>
  
  <test_independence>
    <no_order_dependency>Tests must run in any order</no_order_dependency>
    <clean_state>Each test must set up and clean up its state</clean_state>
    <isolation>No shared state between tests</isolation>
  </test_independence>
  
  <naming_requirements>
    <descriptive_names>test_when_condition_then_expected_behavior</descriptive_names>
    <behavior_focus>Names describe what behavior is being tested</behavior_focus>
    <clear_intent>Anyone can understand what test validates</clear_intent>
  </naming_requirements>
</test_quality_enforcement>
```

#### Test Quality Examples
```python
# ❌ BLOCKED - Poor Test Quality
def test_user():  # Unclear name
    u = User()   # No clear setup
    assert u     # Meaningless assertion

# ✅ ALLOWED - High Quality Test
def test_user_email_validation_rejects_invalid_format():
    user = User(username="test", email="invalid-email")
    
    with pytest.raises(ValidationError) as exc:
        user.validate()
    
    assert "Invalid email format" in str(exc.value)
    assert user.is_valid is False
```

## TDD Cycle Enforcement

### RED Phase Enforcement
```xml
<red_phase_enforcement enforcement="MANDATORY">
  <failing_test_validation>
    <requirement>Tests MUST fail for correct reasons</requirement>
    <verification>Test failure message must match expected error</verification>
    <blocking>No implementation allowed until tests fail correctly</blocking>
  </failing_test_validation>
  
  <atomic_commit_red>
    <message_format>"TDD RED: [test_description] - failing tests created"</message_format>
    <validation>Commit blocked if tests don't fail</validation>
    <rollback>"git reset --hard HEAD~1" if tests pass without implementation</rollback>
  </atomic_commit_red>
</red_phase_enforcement>
```

### GREEN Phase Enforcement
```xml
<green_phase_enforcement enforcement="MANDATORY">
  <minimal_implementation>
    <requirement>Only code necessary to make tests pass</requirement>
    <detection>Block implementation beyond test requirements</detection>
    <guidance>Implement simplest solution first</guidance>
  </minimal_implementation>
  
  <coverage_validation>
    <threshold>90% minimum coverage required</threshold>
    <blocking>Commit blocked if coverage insufficient</blocking>
    <tools>pytest --cov, jest --coverage, etc.</tools>
  </coverage_validation>
  
  <atomic_commit_green>
    <message_format>"TDD GREEN: [implementation] - tests passing with minimal code"</message_format>
    <validation>All tests must pass before commit</validation>
    <rollback>"git reset --hard HEAD~1" if tests fail or coverage low</rollback>
  </atomic_commit_green>
</green_phase_enforcement>
```

### REFACTOR Phase Enforcement
```xml
<refactor_phase_enforcement enforcement="MANDATORY">
  <quality_improvement>
    <requirement>Measurable code quality improvement</requirement>
    <metrics>Complexity reduction, duplication removal, readability</metrics>
    <validation>Quality metrics must improve</validation>
  </quality_improvement>
  
  <test_preservation>
    <requirement>All tests must remain green throughout refactoring</requirement>
    <continuous_validation>Run tests after each refactoring step</continuous_validation>
    <rollback>Immediate rollback if any test breaks</rollback>
  </test_preservation>
  
  <atomic_commit_refactor>
    <message_format>"TDD REFACTOR: [improvement] - quality enhanced while keeping tests green"</message_format>
    <validation>Tests green AND quality improved</validation>
    <rollback>"git reset --hard HEAD~1" if tests break or quality degrades</rollback>
  </atomic_commit_refactor>
</refactor_phase_enforcement>
```

## Enforcement Tools & Integration

### Coverage Tool Requirements
```bash
# Python - MANDATORY
pytest --cov=. --cov-report=term-missing --cov-fail-under=90

# JavaScript - MANDATORY  
npm test -- --coverage --coverageThreshold='{"global":{"lines":90}}'

# TypeScript - MANDATORY
nyc --check-coverage --lines 90 --functions 90 --branches 90
```

### Git Hook Integration
```bash
#!/bin/bash
# pre-commit hook for TDD enforcement

# Check for god objects
if grep -r "class.*{" . | while read line; do
  lines=$(wc -l < $(echo $line | cut -d: -f1))
  if [ $lines -gt 500 ]; then
    echo "ERROR: God object detected - $line"
    exit 1
  fi
done

# Check test coverage
coverage_result=$(pytest --cov=. --cov-fail-under=90 2>&1)
if [ $? -ne 0 ]; then
  echo "ERROR: Coverage below 90% - commit blocked"
  echo "$coverage_result"
  exit 1
fi

# Validate TDD cycle
if ! git log -1 --pretty=%B | grep -E "TDD (RED|GREEN|REFACTOR):"; then
  echo "ERROR: Commit must follow TDD cycle pattern"
  exit 1
fi
```

## Error Codes & Messages

### Anti-Pattern Error Codes
```xml
<error_codes>
  <code id="AP001" severity="CRITICAL">
    <name>God Object Detected</name>
    <message>Class exceeds size limits - refactor required</message>
    <action>Block commit until refactored</action>
  </code>
  
  <code id="AP002" severity="CRITICAL">
    <name>Fake Test Detected</name>
    <message>Test lacks meaningful assertions - real tests required</message>
    <action>Block commit until tests improved</action>
  </code>
  
  <code id="AP003" severity="CRITICAL">
    <name>Excessive Mocking</name>
    <message>Too many mocks - add integration tests</message>
    <action>Block commit until mocking reduced</action>
  </code>
  
  <code id="AP004" severity="CRITICAL">
    <name>TDD Cycle Violation</name>
    <message>Implementation without failing tests - follow RED phase</message>
    <action>Rollback and restart TDD cycle</action>
  </code>
  
  <code id="AP005" severity="WARNING">
    <name>Test Quality Issues</name>
    <message>Test quality below standards - improvements recommended</message>
    <action>Review and enhance test quality</action>
  </code>
</error_codes>
```

## Success Metrics

### Anti-Pattern Prevention Success
- **100% God Object Prevention**: Zero god objects in codebase
- **Fake Test Elimination**: All tests have meaningful assertions
- **Balanced Testing**: 70% unit tests with mocks, 30% integration tests
- **TDD Compliance**: 100% adherence to RED→GREEN→REFACTOR cycle

### Quality Improvements
- **90%+ Test Coverage**: Enforced through tooling
- **Real Behavior Testing**: Verified through assertion analysis
- **Test Independence**: Validated through random order execution
- **Clear Test Intent**: Enforced through naming conventions

## Implementation Status

✅ **God Object Detection**: Size limits and complexity detection implemented
✅ **Fake Test Prevention**: Assertion requirements and validation implemented  
✅ **Mocking Limits**: Mock count restrictions and integration test requirements implemented
✅ **TDD Cycle Enforcement**: Mandatory RED→GREEN→REFACTOR with atomic commits implemented
✅ **Quality Gates**: Coverage tools and quality metrics enforcement implemented
✅ **Git Integration**: Pre-commit hooks and rollback mechanisms implemented

**RESULT**: Comprehensive anti-pattern enforcement that maintains high TDD quality while preventing common development pitfalls that undermine test effectiveness.