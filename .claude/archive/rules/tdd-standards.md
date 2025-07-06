# TDD Standards - Test-Driven Development

**Purpose**: Enforce disciplined TDD practice with RED-GREEN-REFACTOR cycle for all development.

## Core Cycle

### 🔴 RED Phase - Test First
```
1. Write failing test that defines behavior
2. Run test and confirm it fails
3. Commit the failing test
4. NO implementation code yet
5. Update session: "RED phase - Test written"
```

### 🟢 GREEN Phase - Minimal Pass
```
1. Write ONLY enough code to pass
2. No extra features or optimization
3. Run test and confirm it passes
4. Commit the passing code
5. Update session: "GREEN phase - Tests passing"
```

### 🔄 REFACTOR Phase - Clean Code
```
1. Improve code structure
2. Keep all tests passing
3. No behavior changes
4. Commit improvements
5. Update session: "REFACTOR complete"
```

## Test Quality Standards

### Coverage Requirements
- **Line Coverage**: 90% minimum
- **Branch Coverage**: 85% minimum  
- **Critical Paths**: 100% required
- **Error Handling**: 100% required

### Test Characteristics
```python
# Good Test Example
def test_user_cannot_login_with_invalid_password():
    """Test describes expected behavior clearly"""
    # Arrange
    user = create_test_user(email="test@example.com")
    
    # Act
    result = login(email="test@example.com", password="wrong")
    
    # Assert
    assert result.status_code == 401
    assert result.error == "Invalid credentials"
    assert not result.token
```

## Multi-Agent TDD

### When Using Task() Pattern
```python
# Each agent maintains TDD discipline
# Session auto-created for multi-agent work
Task("Frontend Dev", "Create login form with validation")
# → Writes failing component tests first
# → Updates session: "Frontend: RED phase"

Task("Backend Dev", "Create login endpoint") 
# → Writes failing API tests first
# → Updates session: "Backend: RED phase"

Task("Security Expert", "Add rate limiting")
# → Writes failing security tests first
# → Updates session: "Security: RED phase"
```

### Coordination Rules
1. Each agent completes full TDD cycle
2. Integration tests verify agent work
3. No skipping phases in any agent
4. All tests green before merge

## Common Patterns

### Feature Development
```
1. RED: Test the feature requirement
2. GREEN: Implement minimally
3. RED: Test edge case
4. GREEN: Handle edge case
5. REFACTOR: Clean up code
6. Repeat for each aspect
```

### Bug Fixing
```
1. RED: Test that reproduces bug
2. GREEN: Fix the bug minimally
3. RED: Test related edge cases
4. GREEN: Handle edge cases
5. REFACTOR: Improve solution
```

### Refactoring
```
1. Ensure tests exist and pass
2. Make small changes
3. Run tests after each change
4. Commit frequently
5. Never change behavior
```

## Anti-Patterns to Avoid

### ❌ Writing Code First
```python
# WRONG: Implementation before test
def calculate_tax(amount):
    return amount * 0.08

# Then writing test - NO!
```

### ❌ Testing Implementation
```python
# WRONG: Testing HOW not WHAT
def test_uses_multiplication():
    # Don't test internal implementation
```

### ❌ Skipping RED
```python
# WRONG: Writing passing test
def test_always_passes():
    assert True  # Useless test
```

## Enforcement

### Automatic Checks
- Pre-commit hooks verify test coverage
- CI/CD enforces TDD evidence
- Code review checks for TDD cycle
- Metrics track TDD compliance

### Evidence Requirements
```bash
# Each PR must show:
- Commit with failing test (RED)
- Commit with minimal pass (GREEN)
- Commit with refactoring (REFACTOR)
- All tests passing
- Coverage requirements met
- Session showing TDD cycle progress
```

### Session Integration
```bash
# TDD phases tracked in sessions:
- RED commits linked to session
- GREEN commits show progression
- REFACTOR commits complete cycle
- Session documents TDD compliance
```

## Benefits

1. **Design**: Tests drive better design
2. **Documentation**: Tests document behavior
3. **Confidence**: Safe refactoring
4. **Quality**: Fewer bugs in production
5. **Speed**: Faster long-term development

Remember: TDD is not optional. It's how we ensure quality.