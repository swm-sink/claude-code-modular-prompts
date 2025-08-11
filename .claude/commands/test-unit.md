---
name: test-unit
description: Adaptive unit test generation with complexity-aware strategies
usage: "/test-unit <file-path> [--coverage minimal|standard|exhaustive]"
tools: [Read, Write, Grep, WebSearch, Task, Bash]
---

# Adaptive Unit Test Generation

I'll analyze your code complexity and generate appropriate test strategies using parallel analysis.

## Phase 1: Complexity Assessment

**Parallel Analysis via Sub-Agents:**

**Agent 1: Code Complexity Analysis**
- Calculate cyclomatic complexity per function
- Identify branching paths and conditionals
- Detect state mutations and side effects
- Measure coupling with external dependencies

**Agent 2: Risk Assessment**
- Identify critical business logic
- Find security-sensitive operations
- Detect data transformation logic
- Locate error-prone patterns

**Agent 3: Coverage Research**
- WebSearch for testing patterns specific to your tech
- Find industry standards for similar code
- Research known bugs in similar implementations
- Identify framework-specific best practices

## Phase 2: Adaptive Test Strategy

Based on complexity score (0-100):

**Simple Code (0-30):**
- Basic input/output tests
- Null/undefined handling
- Type validation
- 3-5 tests per function

**Moderate Complexity (31-70):**
- Comprehensive branch coverage
- Edge case exploration
- Mock external dependencies
- Property-based testing where applicable
- 10-15 tests per function

**High Complexity (71-100):**
- Exhaustive path coverage
- Mutation testing approach
- Fuzz testing for inputs
- State machine verification
- Performance benchmarks
- 20+ tests per function

## Phase 3: Test Generation Techniques

**Pattern Recognition:**
- Detect common patterns (getter/setter, factory, observer)
- Apply pattern-specific test templates
- Generate parameterized tests for similar functions

**Invariant Testing:**
- Identify code invariants
- Generate tests that verify invariants hold
- Create property-based tests

**Boundary Analysis:**
- Automatically detect boundary conditions
- Generate tests for limits and edge cases
- Include overflow/underflow scenarios

## Phase 4: Test Quality Assurance

**Generated Test Verification:**
- Ensure tests actually fail without implementation
- Verify tests catch common bugs
- Check test independence and isolation
- Validate test performance (<100ms per test)

## Phase 5: Framework Integration

Automatically detect and use your testing framework:
- **JavaScript**: Jest, Mocha, Vitest, Jasmine
- **Python**: pytest, unittest, nose2
- **Go**: native testing, testify, ginkgo
- **Rust**: native tests, proptest
- **Java**: JUnit, TestNG, Mockito

## Output Structure

```
1. Test Setup & Fixtures
2. Unit Tests (organized by complexity)
3. Integration Points (marked for later)
4. Performance Benchmarks (if applicable)
5. Test Coverage Report
```

Initiating adaptive test generation...