# Task Command - Build a single feature with tests (Enhanced)

**Description**: Build a single feature with tests - now with helpful error recovery

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.1.0   | 2025-07-19   | stable | 98%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/tdd-cycle-pattern.md</delegation_target>
  <orchestration_flow>
    1. Validate task scope (single component, <3 files)
    2. Delegate to TDD cycle pattern module
    3. Enforce quality gates and atomic commits
    4. Validate completion criteria
  </orchestration_flow>
  <error_handling>
    <strategy>helpful_errors</strategy>
    <pattern>@.claude/patterns/error-recovery-patterns.md</pattern>
  </error_handling>
</command_orchestration>
```

## Enhanced Error Handling

This version implements helpful error messages for common issues:

### Common Error Scenarios

**1. No Test Directory**
```
❌ Cannot create test file - test directory not found

  Looking for: tests/ or test/
  Current directory: /Users/you/myproject
  
  To fix this:
  → Create test directory: mkdir tests
  → Or specify custom location in PROJECT_CONFIG.xml:
    <test_directory>my_custom_tests</test_directory>
  → Then run /task again

  Why this matters:
  TDD requires tests to be written first. We need a place to put them!
```

**2. Test Framework Not Installed**
```
❌ Test framework not available

  Tried to run: pytest
  Error: Command not found
  
  To fix this:
  → Install pytest: pip install pytest
  → Or for JavaScript: npm install --save-dev jest
  → Or specify your test command in PROJECT_CONFIG.xml:
    <test_command>python -m unittest</test_command>
    
  Then run /task again
```

**3. TDD Cycle Violation**
```
⚠️  TDD Violation: Implementation exists without test

  Found: src/user_auth.py (modified)
  Missing: tests/test_user_auth.py
  
  TDD requires writing tests FIRST:
  1. Write a failing test that describes the behavior
  2. Run test (see it fail - RED)
  3. Write minimal code to pass (GREEN)
  4. Refactor while keeping tests passing
  
  To fix:
  → Create test first: /task "create test for user authentication"
  → Or acknowledge violation: /task --skip-tdd (not recommended)
```

**4. Coverage Below Threshold**
```
❌ Test coverage too low

  Current coverage: 72%
  Required: 90%
  
  Uncovered code:
  - src/user_auth.py: lines 45-52 (error handling)
  - src/user_auth.py: lines 78-81 (edge case)
  
  To fix:
  → Add tests for error scenarios
  → Test edge cases
  → Run: pytest --cov=src --cov-report=term-missing
  
  Example test to add:
  ```python
  def test_login_with_invalid_credentials():
      with pytest.raises(AuthenticationError):
          login("invalid@example.com", "wrong_password")
  ```
```

## Graceful Degradation

When non-critical issues occur, the command continues with warnings:

```
⚠️  Warning: Code formatter not found
  Continuing without auto-formatting
  To enable: pip install black

⚠️  Warning: Git repository not initialized  
  Continuing without version control
  To enable: git init

✓ Test created: tests/test_user_auth.py
✓ Implementation created: src/user_auth.py
✓ All tests passing!
```

## Pre-flight Checks

Before starting, the command validates the environment:

```
🔍 Checking environment...
  ✓ Project configuration found
  ✓ Test directory exists
  ✓ Test framework available
  ⚠️ Linter not configured (optional)
  ✓ Ready to start TDD cycle
```

## Smart Error Prevention

The command helps prevent errors before they happen:

```
📋 Task: "Add email validation"

Before we start:
- Will create: tests/test_email_validation.py
- Will modify: src/validators.py
- Test command: pytest tests/test_email_validation.py

Look good? (Y/n):
```

## Usage Improvements

**Original usage remains the same:**
```
/task "Add email validation to user registration"
```

**New helpful features:**
- Clear error messages with solutions
- Warnings for missing optional tools
- Pre-flight environment checks
- Smart suggestions for common issues
- Graceful degradation when possible

## Example Session with Error Recovery

```
> /task "Add password strength validation"

🔍 Checking environment...
  ❌ Test directory not found
  
  To fix this:
  → Create test directory: mkdir tests
  → Then run this command again
  
  Would you like me to create it for you? (Y/n): y
  
✓ Created: tests/

🔍 Rechecking environment...
  ✓ All checks passed!

📋 Starting TDD cycle for: Add password strength validation

Step 1: Creating failing test...
✓ Created: tests/test_password_validation.py

Step 2: Running test (expect failure)...
✓ Test fails as expected (RED phase)

Step 3: Implementing minimal code...
✓ Created: src/password_validation.py

Step 4: Running test again...
✓ All tests pass! (GREEN phase)

Step 5: Checking coverage...
✓ Coverage: 95% (exceeds 90% requirement)

✨ Task completed successfully!
```

## Benefits of Enhanced Error Handling

1. **Reduced Frustration**: Users know exactly what went wrong
2. **Faster Resolution**: Clear steps to fix issues
3. **Learning Opportunity**: Explains WHY things need to be certain ways
4. **Continued Productivity**: Graceful degradation keeps users moving

---

**Note**: This enhanced version maintains 100% backward compatibility while adding helpful error handling throughout the TDD workflow.