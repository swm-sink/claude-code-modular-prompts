---
name: /test
description: "Generate tests, run test suites, and improve test coverage"
usage: /test [--generate | --run | --fix] [target]
category: core
tools: Read, Write, Edit, Bash, Grep, Glob
---

# Universal Testing Assistant

**Generate, run, and improve tests for any codebase or testing framework.**

## Testing Actions

### Generate Tests
```
/test --generate src/auth/login.js
/test --generate "tests for user registration flow"
/test --generate components/PaymentForm.tsx
```

### Run Tests
```
/test --run
/test --run auth
/test --run --coverage
/test --run tests/integration/
```

### Fix Failing Tests
```
/test --fix "authentication tests are failing"
/test --fix tests/user.test.js
/test --fix "flaky integration tests"
```

## Test Generation

### Automatic Test Creation
**I'll generate:**
- **Unit tests** for functions and methods
- **Component tests** for UI elements
- **Integration tests** for system interactions
- **End-to-end tests** for user workflows
- **Edge case tests** for error conditions

### Smart Test Design
**Tests include:**
- **Happy path** scenarios
- **Error handling** validation
- **Edge cases** and boundary conditions
- **Mock objects** and test data
- **Proper setup/teardown**

## Example Test Generation

### JavaScript Function Testing
```
👤 /test --generate src/utils/validateEmail.js

🤖 Analyzing validateEmail function...
🤖 Generating comprehensive test suite...

✅ Generated tests/utils/validateEmail.test.js:

```javascript
const { validateEmail } = require('../src/utils/validateEmail');

describe('validateEmail', () => {
  describe('valid emails', () => {
    test('accepts standard email format', () => {
      expect(validateEmail('user@example.com')).toBe(true);
    });
    
    test('accepts email with subdomain', () => {
      expect(validateEmail('user@mail.example.com')).toBe(true);
    });
    
    test('accepts email with plus addressing', () => {
      expect(validateEmail('user+tag@example.com')).toBe(true);
    });
  });

  describe('invalid emails', () => {
    test('rejects email without @', () => {
      expect(validateEmail('invalid-email')).toBe(false);
    });
    
    test('rejects email without domain', () => {
      expect(validateEmail('user@')).toBe(false);
    });
    
    test('rejects empty string', () => {
      expect(validateEmail('')).toBe(false);
    });
  });

  describe('edge cases', () => {
    test('handles null input', () => {
      expect(validateEmail(null)).toBe(false);
    });
    
    test('handles undefined input', () => {
      expect(validateEmail(undefined)).toBe(false);
    });
  });
});
```

📊 Test Coverage: 100% lines, 95% branches
🎯 Run with: npm test tests/utils/validateEmail.test.js
```

### React Component Testing
```
👤 /test --generate components/LoginForm.jsx

🤖 Generating React component tests...
🤖 Including user interaction and form validation tests...

✅ Generated components/__tests__/LoginForm.test.jsx:

```jsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import LoginForm from '../LoginForm';

// Mock the auth API
jest.mock('../../services/auth', () => ({
  login: jest.fn()
}));

describe('LoginForm', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders login form elements', () => {
    render(<LoginForm onLogin={jest.fn()} />);
    
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
  });

  test('validates required fields', async () => {
    const user = userEvent.setup();
    render(<LoginForm onLogin={jest.fn()} />);
    
    const loginButton = screen.getByRole('button', { name: /login/i });
    await user.click(loginButton);
    
    expect(screen.getByText(/email is required/i)).toBeInTheDocument();
    expect(screen.getByText(/password is required/i)).toBeInTheDocument();
  });

  test('submits form with valid data', async () => {
    const mockLogin = jest.fn().mockResolvedValue({ success: true });
    const user = userEvent.setup();
    
    render(<LoginForm onLogin={mockLogin} />);
    
    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /login/i }));
    
    await waitFor(() => {
      expect(mockLogin).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123'
      });
    });
  });
});
```

🧪 Tests cover: Rendering, validation, user interaction, API calls
```

## Test Execution & Analysis

### Running Test Suites
```
👤 /test --run --coverage

🤖 Running test suite with coverage analysis...
🤖 Framework detected: Jest + React Testing Library

📊 Test Results:
✅ 47 tests passing
❌ 3 tests failing
⏱️ Runtime: 12.3 seconds

📈 Coverage Report:
• Statements: 78% (target: 80%)
• Branches: 72% (target: 75%)
• Functions: 85% (target: 80%)
• Lines: 76% (target: 80%)

🔍 Failing Tests:
1. auth.test.js:45 - Token expiration handling
   Expected: 401 status
   Received: 500 status

2. payment.test.js:89 - Credit card validation  
   Error: Invalid mock response format

3. user.test.js:123 - Profile update edge case
   Timeout: Async operation never resolved

🎯 Coverage Gaps:
• Error handling in src/api/users.js (lines 34-42)
• Edge cases in src/utils/validation.js
• Integration paths in src/services/payment.js

💡 Recommendations:
1. Fix failing authentication test (check error codes)
2. Update payment mocks to match API changes
3. Add timeout handling to async operations
4. Generate tests for uncovered code paths
```

### Test Fixing
```
👤 /test --fix "authentication tests are failing"

🤖 Analyzing failing authentication tests...
🤖 Examining test expectations vs actual implementation...

🔍 ISSUE IDENTIFIED:
❌ Test expects 401 for expired token
✅ API returns 500 (server error handling changed)

💡 ROOT CAUSE:
Recent API update changed error handling:
- Old: 401 Unauthorized for expired tokens
- New: 500 Internal Server Error (incorrect implementation)

🔧 FIX OPTIONS:

Option 1 - Fix the API (Recommended):
```javascript
// In src/middleware/auth.js
if (tokenExpired) {
  return res.status(401).json({ error: 'Token expired' });
  // Instead of letting it throw 500 error
}
```

Option 2 - Update the test:
```javascript
// In tests/auth.test.js
expect(response.status).toBe(500); // Update expectation
```

🎯 RECOMMENDATION: Fix the API (Option 1)
Reason: 401 is the correct HTTP status for expired tokens

🧪 VERIFICATION PLAN:
1. Update API error handling
2. Re-run authentication tests
3. Test with expired token manually
4. Update integration tests if needed
```

## Multi-Framework Support

**Automatic detection and adaptation:**

**JavaScript**: Jest, Mocha, Cypress, Playwright, Vitest
**Python**: pytest, unittest, nose2, Robot Framework  
**Java**: JUnit, TestNG, Mockito, Spring Test
**Go**: go test, Testify, Ginkgo
**Rust**: cargo test, quickcheck
**C#**: NUnit, xUnit, MSTest

## Testing Best Practices

**I'll ensure tests are:**
- **Fast**: Quick execution, minimal setup
- **Independent**: No test interdependencies
- **Repeatable**: Same results every run
- **Self-validating**: Clear pass/fail results
- **Timely**: Written alongside production code

**Testing Patterns:**
- **AAA Pattern**: Arrange, Act, Assert
- **Given-When-Then**: BDD style scenarios
- **Red-Green-Refactor**: TDD cycle
- **Test Pyramid**: Unit → Integration → E2E

## Integration with Development

**Workflow Integration:**
1. Write code → `/test --generate` for test creation
2. Run `/test --run` to verify functionality  
3. Use `/test --fix` to resolve test failures
4. Check coverage and add missing tests

**CI/CD Integration:**
- Test automation strategies
- Coverage reporting setup
- Flaky test identification
- Performance test integration

## Ready to Test?

Choose your testing action:

```
/test --generate [file-or-feature]    # Create new tests
/test --run [pattern]                 # Execute tests
/test --fix [failing-test]            # Fix test issues
/test --coverage                      # Coverage analysis
```

I'll help you build a robust testing strategy for your codebase!