---
name: generate-test-[TARGET_TYPE]
description: Generate comprehensive test suite for [TARGET_TYPE] following project patterns
usage: "generate-test-[TARGET_TYPE] <target> [options]"
allowed-tools: [Read, Write, Edit, Glob, Bash]
category: test-generation
---

# Generate Test for [TARGET_TYPE]

## Purpose
Automatically generate test suites that follow your project's testing patterns, coverage requirements, and assertion styles discovered during deep discovery consultation.

## Discovered Testing Configuration

### Testing Framework
- **Runner**: [TEST_RUNNER]
- **Assertion Library**: [ASSERTION_LIBRARY]
- **Mocking Framework**: [MOCK_FRAMEWORK]
- **Coverage Tool**: [COVERAGE_TOOL]
- **Coverage Target**: [COVERAGE_TARGET]%

### Testing Patterns
- **Test Structure**: [TEST_STRUCTURE_PATTERN]
- **Naming Convention**: [TEST_NAMING_PATTERN]
- **File Location**: [TEST_FILE_LOCATION]
- **Fixture Strategy**: [FIXTURE_PATTERN]

## Generation Workflow

### Step 1: Analyze Target

```yaml
analysis:
  - Parse target code structure
  - Identify public interfaces
  - Detect dependencies for mocking
  - Determine test scenarios
  - Calculate complexity for test cases
```

### Step 2: Generate Test Structure

```[TEST_LANGUAGE]
[TEST_IMPORTS]

[TEST_SETUP_PATTERN]

[TEST_SUITE_PATTERN] {
  
  [BEFORE_EACH_PATTERN]
  
  [TEST_CASE_PATTERN]('should [BEHAVIOR]', [ASYNC_PATTERN] => {
    // Arrange
    [ARRANGE_PATTERN]
    
    // Act
    [ACT_PATTERN]
    
    // Assert
    [ASSERT_PATTERN]
  });
  
  [AFTER_EACH_PATTERN]
}
```

### Step 3: Generate Test Cases

#### Happy Path Tests
- Normal input validation
- Expected output verification
- State changes confirmation

#### Edge Cases
- Boundary conditions
- Empty/null inputs
- Maximum values
- Special characters

#### Error Scenarios
- Invalid inputs
- Exception handling
- Timeout scenarios
- Network failures

#### Integration Points
- Mock external dependencies
- Verify integrations
- Contract testing

### Step 4: Setup Test Data

```[TEST_LANGUAGE]
// Test Data Factory
[TEST_DATA_FACTORY_PATTERN]

// Fixtures
[FIXTURE_DEFINITION_PATTERN]

// Mocks
[MOCK_DEFINITION_PATTERN]
```

### Step 5: Configure Coverage

- Set up coverage collection
- Define coverage thresholds
- Configure reporting format
- Integrate with CI/CD

## Options

- `--type <type>`: Test type (unit|integration|e2e)
- `--coverage`: Include coverage configuration
- `--watch`: Set up test watching
- `--only <pattern>`: Test specific methods/functions
- `--skip-mocks`: Don't generate mock setups
- `--snapshot`: Include snapshot testing

## Test Categories

### Unit Tests
- Isolated component testing
- Mock all dependencies
- Fast execution
- High coverage target

### Integration Tests
- Component interaction testing
- Selective mocking
- Database/API testing
- Medium execution time

### E2E Tests
- Full workflow testing
- No mocking
- Browser/API testing
- Slower execution

## Success Metrics

- [ ] All public methods have tests
- [ ] Coverage meets project threshold
- [ ] Tests are fast (<[MAX_TIME]ms)
- [ ] Clear test descriptions
- [ ] No flaky tests
- [ ] Proper cleanup

## Generated Test Example

```[TEST_LANGUAGE]
[EXAMPLE_TEST_CODE]
```

## Error Handling

- **Missing dependencies**: Suggest installation commands
- **Complex logic**: Break into smaller test cases
- **Async handling**: Proper promise/callback testing
- **Flaky tests**: Add retry logic or stabilization

## Post-Generation Tasks

1. Run generated tests
2. Check coverage report
3. Review test quality
4. Add to CI/CD pipeline
5. Document test scenarios

## Related Commands

- `/run-tests`: Execute test suites
- `/coverage-report`: Generate coverage reports
- `/test-watch`: Run tests in watch mode
- `/update-snapshots`: Update test snapshots

---

*Test generation patterns discovered on [DISCOVERY_DATE] with [CONFIDENCE]% confidence*