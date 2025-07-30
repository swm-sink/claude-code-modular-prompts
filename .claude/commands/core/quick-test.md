---
name: /quick-test
description: "Universal testing assistance - works with any testing framework"
usage: /quick-test [--generate | --run | --fix | --strategy] [test-target]
category: core
tools: Read, Write, Edit, Bash, Grep, Glob
---

# 🧪 Universal Testing Assistance

**Instant testing help - works with any language, framework, or testing approach!**

## Quick Testing Actions

### Generate Tests
```
/quick-test --generate src/auth/login.js
/quick-test --generate "tests for user registration"
/quick-test --generate components/PaymentForm.tsx
```

### Run Tests
```
/quick-test --run
/quick-test --run auth
/quick-test --run --coverage
```

### Fix Failing Tests
```
/quick-test --fix "failing authentication tests"
/quick-test --fix tests/user.test.js
```

### Testing Strategy
```
/quick-test --strategy
/quick-test --strategy "microservices testing approach"
```

## Universal Framework Support

**Automatically detects and works with:**

**JavaScript/TypeScript**: Jest, Mocha, Cypress, Playwright, Vitest
**Python**: pytest, unittest, nose2, Robot Framework
**Java**: JUnit, TestNG, Mockito, Spring Test
**Go**: go test, Testify, Ginkgo
**Rust**: cargo test, quickcheck
**C#**: NUnit, xUnit, MSTest
**PHP**: PHPUnit, Codeception
**Ruby**: RSpec, MiniTest

## Smart Test Generation

**🎯 What I'll create:**
- Unit tests for individual functions/methods
- Integration tests for component interactions  
- End-to-end tests for user workflows
- Mock objects and test data
- Edge case and error handling tests

**🧠 Context-Aware Testing:**
- Follows your existing test patterns
- Uses your project's testing framework
- Maintains consistent test structure
- Applies testing best practices for your stack

## Example Test Generation

```
👤 /quick-test --generate src/utils/validateEmail.js

🤖 Analyzing validateEmail function...
🤖 Generating comprehensive test suite:

✅ Generated tests/utils/validateEmail.test.js:
• Valid email formats (12 test cases)
• Invalid email formats (8 test cases)  
• Edge cases (empty, null, undefined)
• Internationalization (unicode domains)
• Performance test (large input handling)

🤖 Test coverage: 100% lines, 95% branches
🤖 Ready to run: npm test tests/utils/validateEmail.test.js
```

## Testing Strategy Guidance

**I'll help you design:**
- **Test Pyramid**: Unit → Integration → E2E ratios
- **Coverage Goals**: Realistic targets for your project
- **CI/CD Integration**: Automated testing pipelines
- **Test Data Management**: Fixtures, mocks, factories
- **Performance Testing**: Load and stress testing approaches

## Test Execution & Debugging

**Run tests with smart analysis:**
- Execute existing test suites
- Analyze test failures and provide fixes
- Optimize slow tests
- Improve test reliability
- Generate coverage reports

**Debug failing tests:**
- Identify root causes of test failures
- Suggest fixes for broken tests
- Help with flaky test issues
- Optimize test performance

## Multi-Language Test Management

**Polyglot project support:**
- Consistent testing approach across languages
- Shared testing utilities and patterns
- Cross-service integration testing
- Unified reporting and metrics

## Example Testing Session

```
👤 /quick-test --run --coverage

🤖 Running test suite with coverage analysis...
🤖 Detected Jest configuration

📊 Test Results:
✅ 47 tests passing
❌ 3 tests failing  
⏱️  Total time: 12.3s

📈 Coverage Report:
• Lines: 78% (target: 80%)
• Branches: 72% (target: 75%)  
• Functions: 85% (target: 80%)

🔍 Failing Tests:
1. auth.test.js:45 - Token expiration handling
2. payment.test.js:89 - Credit card validation
3. user.test.js:123 - Profile update edge case

🤖 Want me to fix these failures? Run: /quick-test --fix
```

## Test Quality Metrics

**I'll analyze:**
- Test coverage gaps
- Test execution speed
- Test reliability (flakiness)
- Test maintainability
- Test documentation quality

## When to Use Test Commands

- **`/quick-test`**: Immediate testing help *(this command)*
- **`/test`**: Enhanced testing after `/adapt-to-project`
- **`/test-unit`**, `/test-integration`**, `/test-e2e`**: Specific test types (after customization)

## Start Testing

Choose your testing action:

```
/quick-test --generate [file-or-component]     # Create tests
/quick-test --run [test-pattern]               # Execute tests  
/quick-test --fix [failing-test]               # Fix test issues
/quick-test --strategy                         # Testing approach guidance
```

Ready to improve your test coverage and quality?