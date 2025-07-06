# /test - Test-Driven Development Command

**Purpose**: Enforce pure TDD discipline with RED-GREEN-REFACTOR cycle for all development.

## When to Use

Use `/test` for:
- New feature development with TDD
- Adding test coverage
- Refactoring with test safety
- Bug fixes with regression tests
- Test-first development

## Session Management

- **Consider sessions** for complex TDD features
- **Links to active session** if one exists
- **Updates session** with TDD phase progress (RED/GREEN/REFACTOR)
- Use `/session start` for major test-driven features

## TDD Cycle Enforcement

### 1. RED Phase (Test First)
```python
# Write failing test that defines behavior
def test_user_can_login_with_valid_credentials():
    response = login("user@example.com", "password")
    assert response.status_code == 200
    assert response.token is not None
```

### 2. GREEN Phase (Minimal Code)
```python
# Write ONLY enough code to pass test
def login(email: str, password: str):
    # Minimal implementation
    if email and password:
        return Response(status_code=200, token="abc123")
```

### 3. REFACTOR Phase (Clean Code)
```python
# Improve code while keeping tests green
def login(email: str, password: str) -> Response:
    user = authenticate_user(email, password)
    if user:
        token = generate_jwt_token(user)
        return Response(status_code=200, token=token)
    raise AuthenticationError("Invalid credentials")
```

## Strict Rules

### Never Skip RED
- Test MUST fail first
- Defines expected behavior
- Prevents false positives
- Documents requirements

### Minimal GREEN  
- Simplest code that passes
- No premature optimization
- No extra features
- Focus on current test

### Safe REFACTOR
- Tests stay green
- Improve structure
- Enhance readability
- Add no new behavior

## Test Patterns

### Unit Tests
```python
# Test individual functions/methods
def test_calculate_discount():
    assert calculate_discount(100, 0.1) == 90
    assert calculate_discount(50, 0.2) == 40
```

### Integration Tests
```python
# Test component interactions
async def test_api_creates_user():
    async with AsyncClient(app=app) as client:
        response = await client.post("/users", json={...})
        assert response.status_code == 201
        assert User.objects.filter(email=email).exists()
```

### Edge Cases
```python
# Test boundaries and errors
def test_handles_invalid_input():
    with pytest.raises(ValueError):
        process_payment(-100)  # Negative amount
    with pytest.raises(ValueError):
        process_payment(None)  # None input
```

## Coverage Standards

### Minimum Requirements
- Line coverage: 90%
- Branch coverage: 85%
- Critical paths: 100%
- Error handling: 100%

### Quality Over Quantity
```python
# Bad: Testing getters/setters
def test_user_name():
    user = User(name="John")
    assert user.name == "John"  # Low value

# Good: Testing behavior
def test_user_full_name():
    user = User(first="John", last="Doe")
    assert user.full_name == "John Doe"
    assert User(first="Jane").full_name == "Jane"  # Edge case
```

## Common Workflows

### New Feature
```bash
/test "Add password reset functionality"

# 1. Writes test for password reset request
# 2. Implements minimal endpoint
# 3. Writes test for email sending
# 4. Implements email logic
# 5. Writes test for token validation
# 6. Implements token handling
# 7. Refactors for clarity
```

### Bug Fix
```bash
/test "Fix user logout not clearing session"

# 1. Writes failing test reproducing bug
# 2. Fixes bug minimally
# 3. Adds regression tests
# 4. Refactors if needed
```

### Refactoring
```bash
/test "Refactor payment processing for clarity"

# 1. Ensures full test coverage exists
# 2. Refactors in small steps
# 3. Runs tests after each change
# 4. Commits working state frequently
```

## Test Organization

### Structure
```
tests/
├── unit/          # Fast, isolated tests
├── integration/   # Component interaction tests
├── e2e/          # End-to-end user flows
└── fixtures/     # Test data and mocks
```

### Naming Convention
```python
# Clear test names describing behavior
def test_expired_token_returns_401_unauthorized():
def test_admin_can_delete_any_user():
def test_concurrent_updates_handle_race_condition():
```

## Mocking Strategy

### Mock External Services
```python
@patch('services.email.send')
def test_sends_welcome_email(mock_send):
    create_user("new@example.com")
    mock_send.assert_called_once()
```

### Don't Mock What You Own
```python
# Bad: Mocking your own code
@patch('models.User.save')  # Don't do this

# Good: Test real behavior
def test_user_saves_to_database():
    user = User.create(email="test@example.com")
    assert User.objects.get(id=user.id).email == "test@example.com"
```

## Examples

### Simple TDD
```bash
/test "Add age validation to User model"
# RED: Test age must be positive
# GREEN: Add validation
# REFACTOR: Extract validation logic
```

### Complex Feature
```bash
/test "Implement shopping cart with discounts"
# Prompts: "This is complex. Create session? (y/n)"
# If yes: Creates session #125 "TDD: Shopping Cart"
# Builds incrementally:
# - Test add item → Updates session: "RED: Add item test"
# - Test remove item → Updates session: "GREEN: Item management"
# - Test calculate total → Updates session: "REFACTOR: Calculation logic"
# - Test apply discount → Updates session: "RED: Discount tests"
# - Test multiple discounts → Updates session: "Complete: All tests passing"
```

## Token Optimization
- Focused on test scenarios
- Minimal implementation code
- Clear test descriptions
- Max 8k tokens per cycle