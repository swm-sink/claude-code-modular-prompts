# /test - Testing Workflows

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Execute comprehensive testing workflows including test creation, execution, analysis, and improvement. Supports TDD practices, test automation, and quality assurance through systematic testing approaches.

**Note**: This is a simplified version that focuses on core testing functionality without complex TDD enforcement frameworks.

---

## How It Works

### 1. Test Planning
- **Test Strategy**: Define testing approach and scope
- **Test Cases**: Identify test scenarios and cases
- **Test Data**: Prepare test data and fixtures
- **Test Environment**: Set up testing environment and tools

### 2. Test Creation
- **Unit Tests**: Create unit tests for individual components
- **Integration Tests**: Build integration tests for component interactions
- **End-to-End Tests**: Develop comprehensive workflow tests
- **Test Automation**: Set up automated testing infrastructure

### 3. Test Execution
- **Test Running**: Execute tests systematically
- **Coverage Analysis**: Measure test coverage and effectiveness
- **Performance Testing**: Conduct performance and load testing
- **Regression Testing**: Ensure existing functionality remains intact

### 4. Test Analysis & Improvement
- **Results Analysis**: Analyze test results and failures
- **Coverage Improvement**: Identify and address coverage gaps
- **Test Optimization**: Improve test performance and reliability
- **Documentation**: Document testing procedures and findings

---

## Usage Examples

```bash
# Run all tests
/test --run-all

# Create tests for specific component
/test --create "user authentication module"

# Run specific test suite
/test --run-suite "integration tests"

# Analyze test coverage
/test --coverage-analysis

# Performance testing
/test --performance "api endpoints"

# TDD workflow
/test --tdd "new feature implementation"
```

---

## What It Does

### Test Creation
- Creates comprehensive unit tests
- Builds integration test suites
- Develops end-to-end test scenarios
- Sets up test automation infrastructure

### Test Execution
- Runs tests systematically and efficiently
- Measures coverage and effectiveness
- Conducts performance and load testing
- Provides detailed test reporting

### Test Analysis
- Analyzes test results and failures
- Identifies coverage gaps and improvements
- Optimizes test performance and reliability
- Provides actionable recommendations

### Test Improvement
- Enhances test coverage and quality
- Improves test maintainability
- Optimizes test execution performance
- Updates testing procedures and standards

---

## Testing Types

### Unit Testing
```
PURPOSE: Test individual components and functions
APPROACH: Isolated testing, mocking dependencies
OUTPUT: Unit test suite, coverage report, component validation
```

### Integration Testing
```
PURPOSE: Test component interactions and interfaces
APPROACH: Interface testing, dependency testing
OUTPUT: Integration test suite, interaction validation, interface coverage
```

### End-to-End Testing
```
PURPOSE: Test complete workflows and user scenarios
APPROACH: Full system testing, user journey validation
OUTPUT: E2E test suite, workflow validation, user experience testing
```

### Performance Testing
```
PURPOSE: Test system performance and scalability
APPROACH: Load testing, stress testing, performance profiling
OUTPUT: Performance metrics, bottleneck identification, optimization recommendations
```

---

## Output Format

### Test Summary
```
TEST_TYPE: [unit/integration/e2e/performance]
SCOPE: [components-or-features-tested]
COVERAGE: [coverage-percentage-or-metrics]
STATUS: [passed/failed/partial]
```

### Test Results
```
TESTS_RUN: [number-of-tests-executed]
TESTS_PASSED: [number-of-tests-passed]
TESTS_FAILED: [number-of-tests-failed]
EXECUTION_TIME: [total-execution-time]
```

### Coverage Analysis
```
COVERAGE_PERCENTAGE: [overall-coverage-percentage]
COVERAGE_GAPS: [areas-with-insufficient-coverage]
CRITICAL_PATHS: [important-paths-coverage-status]
RECOMMENDATIONS: [coverage-improvement-suggestions]
```

### Performance Metrics
```
RESPONSE_TIME: [average-response-time]
THROUGHPUT: [requests-per-second]
RESOURCE_USAGE: [memory-cpu-usage]
BOTTLENECKS: [identified-performance-bottlenecks]
```

---

## Test Development Process

### 1. Test Planning
- Define testing strategy and approach
- Identify test scenarios and cases
- Plan test data and environment setup
- Set coverage and quality targets

### 2. Test Implementation
- Write unit tests for components
- Create integration tests for interactions
- Build end-to-end test scenarios
- Set up test automation and CI/CD

### 3. Test Execution
- Run tests systematically
- Measure coverage and effectiveness
- Conduct performance testing
- Generate test reports

### 4. Test Analysis
- Analyze test results and failures
- Identify coverage gaps
- Optimize test performance
- Document findings and improvements

---

## Key Features

### ✅ Comprehensive Testing
- Unit, integration, and end-to-end testing
- Performance and load testing
- Automated test execution
- Detailed coverage analysis

### ✅ TDD Support
- Test-first development approach
- Red-Green-Refactor cycle support
- Continuous testing integration
- Quality-driven development

### ✅ Test Automation
- Automated test execution
- CI/CD integration
- Test reporting and analytics
- Continuous testing feedback

### ✅ Quality Assurance
- Coverage measurement and analysis
- Performance benchmarking
- Regression testing
- Test quality assessment

---

## Testing Strategies

### Test-Driven Development (TDD)
- **Red Phase**: Write failing tests first
- **Green Phase**: Write minimal code to pass tests
- **Refactor Phase**: Improve code while keeping tests green
- **Continuous Cycle**: Repeat for each feature or change

### Behavior-Driven Development (BDD)
- **Specification**: Define behavior in business terms
- **Implementation**: Write tests based on specifications
- **Validation**: Ensure system meets specified behavior
- **Collaboration**: Involve stakeholders in test definition

### Risk-Based Testing
- **Risk Assessment**: Identify high-risk areas
- **Prioritization**: Focus testing on high-risk components
- **Coverage**: Ensure adequate coverage of critical paths
- **Mitigation**: Use testing to reduce identified risks

---

## Test Categories

### Functional Testing
- **Unit Tests**: Individual component testing
- **Integration Tests**: Component interaction testing
- **System Tests**: Full system functionality testing
- **Acceptance Tests**: User acceptance and business logic testing

### Non-Functional Testing
- **Performance Tests**: Speed and scalability testing
- **Security Tests**: Security vulnerability testing
- **Usability Tests**: User experience and interface testing
- **Reliability Tests**: System stability and reliability testing

### Maintenance Testing
- **Regression Tests**: Ensure existing functionality intact
- **Smoke Tests**: Basic functionality verification
- **Sanity Tests**: Focused testing after changes
- **Compatibility Tests**: Cross-platform and version testing

---

## Best Practices

### When to Use
- **Development**: During active development for TDD
- **Pre-deployment**: Before releasing to production
- **Continuous Integration**: As part of CI/CD pipeline
- **Quality Assurance**: For comprehensive quality validation

### Testing Tips
- Start with clear test requirements
- Use appropriate testing frameworks and tools
- Maintain test code quality and organization
- Run tests frequently and consistently
- Keep tests fast and reliable

### Quality Guidelines
- Aim for high test coverage (80%+)
- Focus on critical paths and edge cases
- Maintain test independence and isolation
- Use meaningful test names and descriptions
- Keep tests simple and focused

---

## Error Handling

### Common Issues
- **Flaky Tests**: Identifies and fixes unreliable tests
- **Slow Tests**: Optimizes test execution performance
- **Coverage Gaps**: Identifies missing test coverage
- **Test Failures**: Provides debugging and resolution guidance

### Graceful Degradation
- Provides partial test results when full suite fails
- Suggests workarounds for testing infrastructure issues
- Maintains test quality even with resource constraints
- Documents limitations and improvement needs

---

## Integration

### Works Well With
- `/context-prime` - For project context before testing
- `/task` - For implementing tests as part of development
- `/debug` - For investigating test failures
- `/review` - For reviewing test quality and coverage

### Typical Workflow
1. **Context**: `/context-prime` to understand project testing context
2. **Test Creation**: `/test` to create and implement tests
3. **Execution**: `/test` to run tests and analyze results
4. **Debug**: `/debug` to investigate and fix test failures

---

## Test Automation

### Automated Testing
- **Unit Test Automation**: Automated unit test execution
- **Integration Test Automation**: Automated integration testing
- **CI/CD Integration**: Continuous testing in deployment pipeline
- **Test Reporting**: Automated test result reporting

### Test Infrastructure
- **Test Frameworks**: Setup and configuration of testing frameworks
- **Test Environments**: Test environment management
- **Test Data**: Test data generation and management
- **Test Tools**: Testing tool selection and integration

---

## Performance Testing

### Load Testing
- **Normal Load**: Testing under expected load conditions
- **Peak Load**: Testing under high load scenarios
- **Stress Testing**: Testing beyond normal capacity
- **Endurance Testing**: Long-term performance validation

### Performance Metrics
- **Response Time**: Request processing time
- **Throughput**: Requests handled per unit time
- **Resource Usage**: CPU, memory, and disk usage
- **Scalability**: System scaling characteristics

---

## Test Maintenance

### Test Code Quality
- **Organization**: Well-structured test code
- **Readability**: Clear and understandable tests
- **Maintainability**: Easy to update and modify
- **Reusability**: Shared test utilities and fixtures

### Test Updates
- **Regression Prevention**: Update tests for new features
- **Coverage Improvement**: Add tests for uncovered areas
- **Performance Optimization**: Improve test execution speed
- **Framework Updates**: Keep testing frameworks current

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple testing workflow
- **No Module Dependencies**: Self-contained testing logic
- **No Advanced Frameworks**: Basic testing and TDD patterns
- **No Mandatory Enforcement**: Supportive testing guidance

### Core Focus
- **Essential Testing**: Core test creation, execution, and analysis
- **Practical TDD**: Basic test-driven development support
- **Fast Execution**: Minimal overhead for quick testing
- **Clear Results**: Well-structured test reports and metrics

---

**Note**: This simplified command provides core testing functionality without the complexity of the full framework. For advanced features like complex TDD enforcement, multi-agent testing coordination, or advanced quality gates, use the full framework commands.