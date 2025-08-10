---
name: test
description: Adaptive test generation based on code complexity
usage: "/test <target> [--type auto|unit|integration|e2e] [--coverage basic|thorough]"
allowed-tools: [Read, Write, Grep, Task]
---

# Adaptive Test Generation

I'll create appropriate tests based on your code's complexity and needs.

## Analyzing Target

Target: **[target]**

Quick assessment:
- Code complexity: [detecting...]
- Test framework: [checking project...]
- Existing coverage: [analyzing...]

<basic-tests>
<!-- For simple functions, utilities -->

## Basic Test Suite (< 1 minute)

This is simple code. I'll create:
- **Happy path**: 2-3 core scenarios
- **Edge cases**: Null/empty handling
- **Basic validation**: Type checking

*Using [detected framework] with your conventions.*

[Generate 3-5 focused tests]
</basic-tests>

<standard-tests>
<!-- For business logic, moderate complexity -->

## Standard Test Coverage (2-3 minutes)

This code has moderate complexity (score: [calculated]).

### Test Strategy
- **Unit tests**: [number] for core functions
- **Edge cases**: [identified edge scenarios]
- **Error paths**: [error conditions to test]

*Quick check*: Should I mock external dependencies? (Y/n)

### Generating Tests
1. **Functionality tests**: Core behavior
2. **Boundary tests**: Edge values
3. **Error tests**: Failure scenarios
4. **Integration**: With connected modules

*Creating comprehensive test suite...*

[Generate 10-15 well-structured tests]
</standard-tests>

<comprehensive-tests>
<!-- For complex systems, critical paths -->

## Comprehensive Testing (5 minutes)

This is complex/critical code requiring thorough coverage.

### Coverage Planning

**Question**: What's most important to test?
- Performance under load
- Security and validation
- All edge cases
- Integration points

*I'll prioritize based on your answer.*

### Multi-Layer Test Strategy

**Layer 1: Unit Tests** (isolated functions)
- [Number] tests per function
- Mock all dependencies
- Cover all branches

**Layer 2: Integration Tests** (module interactions)
- Component integration
- Database/API interactions
- State management

**Layer 3: E2E Tests** (if applicable)
- User workflows
- Full system paths
- Performance benchmarks

### Execution Plan
Using parallel test generation for efficiency:
- Task 1: Generate unit tests
- Task 2: Create integration tests
- Task 3: Build test utilities

*Starting comprehensive test generation...*

[Generate 20+ tests with utilities]
</comprehensive-tests>

<e2e-mode>
<!-- For explicit E2E request -->

## End-to-End Test Suite

Creating realistic user scenarios:

### Test Scenarios
1. **Happy path**: [main workflow]
2. **Alternative paths**: [variations]
3. **Error recovery**: [failure handling]
4. **Performance**: [load conditions]

### Implementation
- Using [Cypress/Playwright/Selenium]
- Following your patterns in [test directory]
- Including data fixtures

[Generate E2E test suite]
</e2e-mode>

## Test Output

### Created Tests
- **File**: [test file path]
- **Tests**: [count] test cases
- **Coverage**: [estimated percentage]

### Test Organization
```
describe('[Component/Module]', () => {
  // Setup and teardown
  
  describe('[Feature 1]', () => {
    // Related tests
  });
  
  describe('[Feature 2]', () => {
    // Related tests
  });
});
```

### Key Test Cases
1. ✅ [Test name] - [what it validates]
2. ✅ [Test name] - [what it validates]
3. ✅ [Test name] - [what it validates]
[More based on complexity...]

## Running Tests

Execute with: `[test command for your framework]`

**Coverage report**: `[coverage command]`

*Generated [count] tests using [approach] strategy based on code complexity.*

**Next steps**:
- Review test quality
- Run test suite
- Add any domain-specific tests I might have missed