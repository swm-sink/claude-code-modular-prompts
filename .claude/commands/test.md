---
name: test
description: Generate tests for code with appropriate complexity
usage: "/test <target> [type]"
tools: [Read, Write, Grep]
---

# Generate Tests

I'll analyze your code and create appropriate tests.

## Quick Analysis

First, let me examine the target to determine:
- Code complexity level
- Existing test framework
- Current test coverage

## Test Generation Process

1. **Read the target file** to understand structure and dependencies
2. **Check existing tests** to maintain consistency
3. **Identify test framework** (Jest, pytest, etc.) from project config
4. **Create comprehensive tests** covering:
   - Main functionality (happy path)
   - Edge cases and boundary conditions
   - Error handling
   - Input validation

## Adaptive Approach

**For simple functions**: Basic unit tests with key scenarios
**For complex logic**: Thorough testing with mocking and integration tests
**For critical systems**: Comprehensive test suite with performance checks

What would you like me to test?