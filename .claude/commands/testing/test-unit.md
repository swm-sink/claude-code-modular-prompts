---
name: /test-unit
description: Run unit tests for [INSERT_PROJECT_NAME] using [INSERT_TESTING_FRAMEWORK]
usage: /test-unit [file-pattern] [--coverage] [--watch]
category: testing
tools: Bash, Read, Write
security_level: HIGH
---

# Unit Testing for [INSERT_PROJECT_NAME]

<!-- SECURITY: Include command security wrapper for injection prevention -->
<include>components/security/command-security-wrapper.md</include>

**SECURITY NOTICE**: This command executes test frameworks with potential file system access. ALL inputs are validated to prevent command injection and path traversal attacks.

I'll help you run and manage unit tests for **[INSERT_PROJECT_NAME]** using **[INSERT_TESTING_FRAMEWORK]** with patterns optimized for **[INSERT_PRIMARY_LANGUAGE]** and comprehensive security validation.

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
For [INSERT_PRIMARY_LANGUAGE] test patterns (with security validation):
```bash
/test-unit src/**/*.test.[ext]
# SECURITY: File patterns validated using validateFilePath() with extension checking
# SECURITY: Path traversal prevention applied to all file patterns
/test-unit tests/unit/
# SECURITY: Directory paths validated against project boundaries
```

### Watch Mode
For [INSERT_WORKFLOW_TYPE] development (with security monitoring):
```bash
/test-unit --watch
# SECURITY: Watch mode validated, file monitoring secured
# SECURITY: Continuous monitoring with sanitized output
```

## Coverage Requirements - SECURITY ENHANCED

Based on [INSERT_SECURITY_LEVEL] security:
- **Basic**: 60% minimum coverage with security test validation
- **Standard**: 80% minimum coverage with security test validation
- **High**: 90% minimum coverage with branch coverage and mandatory security tests
- **SECURITY REQUIREMENT**: All coverage thresholds validated against injection attacks
- **MANDATORY**: Coverage reports sanitized to prevent information disclosure

## Test Patterns for [INSERT_DOMAIN] - SECURITY ENHANCED

Domain-specific testing patterns with security validation:
- Component isolation with secure test boundaries
- Mock strategies with input validation
- Test data factories with sanitized test data
- Assertion patterns with secure comparisons
- **SECURITY PATTERNS**: Command injection prevention in test execution
- **SECURITY PATTERNS**: Path traversal prevention in test file discovery
- **SECURITY PATTERNS**: Sanitized test output and error handling

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

**SECURITY EXECUTION PROCESS:**

1. **Input Validation**: All test parameters validated using security wrapper
2. **File Pattern Validation**: Test file patterns validated using validateFilePath()
3. **Command Validation**: Test framework commands validated against TEST_ALLOWED_COMMANDS
4. **Path Security**: All test paths validated for boundary compliance and traversal prevention
5. **Secure Execution**: Tests executed using executeSecureCommand() wrapper
6. **Output Sanitization**: All test results and coverage reports sanitized
7. **Error Handling**: Test failures handled with sanitized error messages
8. **Audit Logging**: Complete security audit trail maintained

**ALLOWED TEST FRAMEWORKS**: pytest, jest, mocha, jasmine, karma, go test, cargo test, mvn test, gradle test, phpunit, rspec, minitest
**SECURITY VALIDATIONS**: 
- File patterns: Extension validation, path boundary checking
- Coverage values: Numeric validation, range checking
- Framework parameters: Command injection prevention
- Test execution: Resource limits and timeout controls

What would you like to test? (All inputs will be validated for security compliance)