---
name: /test-unit
description: Run unit tests for [INSERT_PROJECT_NAME] using [INSERT_TESTING_FRAMEWORK] (v1.0)
version: "1.0"
usage: '/test-unit [file-pattern] [--coverage] [--watch] [--parallel] [--debug]'
category: testing
allowed-tools:
- Bash
- Read
- Write
- Grep
- LS
dependencies:
- /test-integration
- /test-e2e
- /quick-test
validation:
  pre-execution: Validate test framework installation and configuration
  during-execution: Monitor test execution with timeout protection
  post-execution: Verify coverage thresholds and generate reports
progressive-disclosure:
  layer-integration: Layer 1 via /quick-test, Layer 2 with customizable coverage, Layer 3 with advanced parallel execution
  layer-1-experience: Simple test execution with smart defaults
  layer-2-experience: Customizable coverage targets and watch mode
  layer-3-experience: Advanced parallel execution and debugging options
safety-features:
  input-validation: Test file patterns and coverage thresholds
  error-recovery: Graceful handling of test failures with clear reporting
  security-checks: Path traversal prevention and command injection protection
performance:
  optimization: Parallel test execution and smart test discovery
  caching: Test result caching for unchanged files
  resource-limits: Memory and CPU limits for test processes
---

# Unit Testing for [INSERT_PROJECT_NAME]

<!-- SECURITY: Include command security wrapper for injection prevention -->
<include>components/security/command-security-wrapper.md</include>

**SECURITY NOTICE**: This command executes test frameworks with potential file system access. ALL inputs are validated to prevent command injection and path traversal attacks.

I'll help you run and manage unit tests for **[INSERT_PROJECT_NAME]** using **[INSERT_TESTING_FRAMEWORK]** with patterns optimized for **[INSERT_PRIMARY_LANGUAGE]**.

## Test Configuration

- **Framework**: [INSERT_TESTING_FRAMEWORK]
- **Language**: [INSERT_PRIMARY_LANGUAGE]
- **Coverage Target**: Based on [INSERT_SECURITY_LEVEL] requirements
- **Tech Stack**: [INSERT_TECH_STACK]

## Running Tests

### All Unit Tests
```bash
/test-unit
# SECURITY: Default execution with security wrapper validation
# SECURITY: Test commands validated against TEST_ALLOWED_COMMANDS allowlist
```

### Specific Test Files
For [INSERT_PRIMARY_LANGUAGE] test patterns:
```bash
/test-unit src/**/*.test.[ext]
# SECURITY: File patterns validated using validateFilePath() with extension checking
# SECURITY: Path traversal prevention applied to all file patterns
/test-unit tests/unit/
# SECURITY: Directory paths validated against project boundaries
```

### Watch Mode
For [INSERT_WORKFLOW_TYPE] development:
```bash
/test-unit --watch
# SECURITY: Watch mode validated, file monitoring secured
# SECURITY: Continuous monitoring with sanitized output
```

## Coverage Requirements

Based on [INSERT_SECURITY_LEVEL] requirements:
- **Basic**: 60% minimum coverage
- **Standard**: 80% minimum coverage
- **High**: 90% minimum coverage with branch coverage
- Coverage thresholds validated
- Coverage reports properly formatted

## Test Patterns for [INSERT_DOMAIN]

Domain-specific testing patterns:
- Component isolation with test boundaries
- Mock strategies with input validation
- Test data factories with clean test data
- Assertion patterns with proper comparisons
- Test execution patterns
- File discovery patterns
- Clean test output and error handling

## Integration with [INSERT_CI_CD_PLATFORM]

Your CI pipeline configuration:
- Pre-commit hooks
- PR validation
- Coverage reporting
- Test result artifacts

## Performance Considerations

For [INSERT_PERFORMANCE_PRIORITY] requirements:
- Test execution optimization
- Parallel test runners
- Test suite splitting
- Resource management

## Team Collaboration

For [INSERT_TEAM_SIZE] teams:
- Test naming conventions
- Shared test utilities
- Test documentation
- Review processes

**TEST EXECUTION PROCESS:**

1. **Input Validation**: All test parameters validated
2. **File Pattern Validation**: Test file patterns validated
3. **Command Validation**: Test framework commands validated against allowlist
4. **Path Validation**: All test paths validated for boundary compliance
5. **Execution**: Tests executed using framework wrapper
6. **Output Processing**: All test results and coverage reports processed
7. **Error Handling**: Test failures handled with clean error messages
8. **Logging**: Complete audit trail maintained

**ALLOWED TEST FRAMEWORKS**: pytest, jest, mocha, jasmine, karma, go test, cargo test, mvn test, gradle test, phpunit, rspec, minitest
**VALIDATIONS**: 
- File patterns: Extension validation, path boundary checking
- Coverage values: Numeric validation, range checking
- Framework parameters: Parameter validation
- Test execution: Resource limits and timeout controls

What would you like to test? (All inputs will be validated)