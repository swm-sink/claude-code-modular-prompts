# /quality/tdd - Test-Driven Development Module

**Purpose**: Enforce disciplined TDD with RED-GREEN-REFACTOR cycle and comprehensive coverage standards.

## Module Interface
- **Trigger**: Any development task requiring new functionality
- **Dependencies**: Uses patterns/tool-usage.md for parallel test execution
- **Session**: Tracks TDD progress in development sessions
- **Output**: Verified TDD implementation with coverage reports

## Mandatory TDD Cycle

### RED Phase - Write Failing Test
```python
# 1. Understand requirements deeply
# 2. Write the simplest failing test
# 3. Verify test fails for the right reason
# 4. No implementation code yet!

def test_user_authentication_should_fail_with_invalid_password():
    user = User("john@example.com")
    result = user.authenticate("wrong_password")
    assert result.is_failure()
    assert result.error == "Invalid credentials"
```

### GREEN Phase - Minimal Implementation
```python
# 1. Write minimal code to make test pass
# 2. No optimization, no extra features
# 3. Just enough to pass the test
# 4. Verify test passes

def authenticate(self, password):
    if password != self.stored_password:
        return AuthResult.failure("Invalid credentials")
    return AuthResult.success()
```

### REFACTOR Phase - Improve Design
```python
# 1. Improve code quality while keeping tests green
# 2. Extract methods, improve naming
# 3. Remove duplication
# 4. Run tests after each change

def authenticate(self, password):
    if not self._is_valid_password(password):
        return self._create_auth_failure()
    return self._create_auth_success()
```

## Coverage Requirements

### Minimum Standards
- **Line Coverage**: 90% minimum
- **Branch Coverage**: 85% minimum  
- **Critical Paths**: 100% coverage required
- **Error Handling**: 100% coverage required

### Coverage Analysis
```python
# Automated coverage reporting
Bash("pytest --cov=src --cov-report=html --cov-fail-under=90")
Bash("pytest --cov=src --cov-branch --cov-report=term-missing")
```

## TDD Quality Gates

### Pre-Implementation Checklist
- [ ] Requirements clearly understood
- [ ] Test case scenarios identified
- [ ] Edge cases and error conditions mapped
- [ ] Test structure planned (Arrange-Act-Assert)

### During Implementation
- [ ] RED: Test fails for correct reason
- [ ] GREEN: Minimal implementation passes
- [ ] REFACTOR: Code quality improved
- [ ] Coverage thresholds maintained

### Post-Implementation
- [ ] All tests passing
- [ ] Coverage requirements met
- [ ] Code review completed
- [ ] TDD compliance documented

## Advanced TDD Patterns

### Test Categories
1. **Unit Tests**: Single responsibility, fast execution
2. **Integration Tests**: Component interaction validation
3. **Contract Tests**: API/interface verification
4. **Property-Based Tests**: Generative testing for edge cases

### Test Organization
```python
tests/
├── unit/           # Fast, isolated tests
├── integration/    # Component interaction tests
├── contract/       # API/interface tests
└── fixtures/       # Shared test data
```

## Session Integration
- TDD progress tracked in development sessions
- Test failures and fixes documented
- Coverage reports linked to GitHub issues
- TDD compliance verification required for completion

## Usage Examples
```bash
/quality/tdd "Implement user authentication with JWT tokens"
/quality/tdd "Add payment processing with Stripe integration"
```

**Token Budget**: <5k tokens (focused TDD enforcement)