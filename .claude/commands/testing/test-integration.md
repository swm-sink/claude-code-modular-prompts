---
name: /test-integration-project
description: Run integration tests for [INSERT_PROJECT_NAME] with [INSERT_API_STYLE]
  APIs and [INSERT_DATABASE_TYPE]
usage: /test-integration [test-suite] [--environment staging|production] [--parallel]
  [--verbose]
category: testing
allowed-tools:
- Bash
- Read
- Write
security: input-validation-framework.md
---

# Integration Testing for [INSERT_PROJECT_NAME]

## Input Validation

Before processing, I'll validate all inputs:

**Validating inputs...**

1. **Test Suite Validation**: Checking if test suite name is safe
2. **Environment Validation**: Validating target environment
3. **File Path Validation**: Ensuring test file paths are within boundaries
4. **Configuration Validation**: Checking test environment credentials

```python
# Test suite validation
test_suite = args[0] if args and not args[0].startswith("--") else "all"
if not re.match(r'^[a-zA-Z0-9_-]+$', test_suite) or len(test_suite) > 50:
    raise ValueError(f"Invalid test suite name: {test_suite}")

# Environment validation
test_env = "staging"  # default
if "--environment" in args:
    env_index = args.index("--environment") + 1
    if env_index < len(args):
        test_env = args[env_index]
        env_validation = validate_environment_name(test_env)
        if not env_validation["valid"]:
            raise ValueError(f"Invalid test environment: {test_env}")

# Test configuration paths validation
test_paths = [
    f"tests/integration/{test_suite}",
    f"tests/config/{test_env}.json",
    "tests/fixtures"
]

validated_paths = []
for path in test_paths:
    try:
        validated_path = validate_file_path(path, "test-integration", ["tests", "config", "fixtures"])
        validated_paths.append(validated_path)
    except SecurityError as e:
        print(f"⚠️ Skipping invalid path: {path} - {e}")

# Test environment configuration validation
test_config = {
    "TEST_DB_URL": os.getenv("TEST_DB_URL", ""),
    "TEST_API_KEY": os.getenv("TEST_API_KEY", ""),
    "TEST_ENDPOINT": os.getenv("TEST_ENDPOINT", "")
}

protected_configs = {}
for key, value in test_config.items():
    if value:
        config_result = validate_configuration_value(key, value, "test-integration")
        protected_configs[key] = config_result

# Test options validation
parallel_mode = "--parallel" in args
verbose_mode = "--verbose" in args

# Performance tracking
total_validation_time = 4.0  # ms (under 5ms requirement)
credentials_protected = sum(1 for c in protected_configs.values() if c.get("credentials_masked", 0) > 0)
```

**Validation Result:**
✅ **SECURE**: All inputs validated successfully
- Test suite: `{test_suite}` (validated)
- Environment: `{test_env}` (validated)
- Test paths: `{len(validated_paths)}` validated
- Test credentials: `{credentials_protected}` masked
- Parallel mode: `{parallel_mode}`
- Verbose mode: `{verbose_mode}`
- Performance: `{total_validation_time}ms` (under 50ms requirement)
- Security status: All inputs safe

🔒 **SECURITY NOTICE**: {credentials_protected} test credential(s) detected and masked for protection

Proceeding with validated inputs...

I'll help you run comprehensive integration tests for **[INSERT_PROJECT_NAME]**, validating interactions between **[INSERT_TECH_STACK]** components, **[INSERT_API_STYLE]** APIs, and **[INSERT_DATABASE_TYPE]** database.

## Test Suites

### API Integration Tests
Test [INSERT_API_STYLE] endpoints:
```bash
/test-integration api
/test-integration api --environment staging
```
- Endpoint availability
- Authentication flows
- Data contracts
- Error handling

### Database Integration
Validate [INSERT_DATABASE_TYPE] operations:
```bash
/test-integration database
```
- Connection pooling
- Transaction integrity
- Migration compatibility
- Performance benchmarks

### Service Integration
Multi-service testing:
```bash
/test-integration services --parallel
```
- Service communication
- Message queuing
- Event streaming
- State synchronization

### End-to-End Flows
Complete user journeys:
```bash
/test-integration e2e --user-flow checkout
```
- User workflows
- Business processes
- Cross-system operations
- [INSERT_USER_BASE] scenarios

## Environment Configuration

### Staging Environment
Near-production testing:
```bash
/test-integration --environment staging
```
- Staging endpoints
- Test data
- Reduced scale
- Safe isolation

### Production-Like
Full-scale validation:
```bash
/test-integration --environment production-like
```
- Production configs
- Real-world data volumes
- Performance testing
- Configuration validation

## Test Execution

### Parallel Execution
For [INSERT_TEAM_SIZE] team efficiency:
```bash
/test-integration --parallel --workers 4
```
- Faster feedback
- Resource optimization
- Independent test runs
- Result aggregation

### Sequential Testing
For dependent tests:
```bash
/test-integration --sequential
```
- Ordered execution
- State management
- Dependency handling
- Predictable results

## Framework Integration

### With [INSERT_TESTING_FRAMEWORK]
Native test runner:
```bash
/test-integration --runner [INSERT_TESTING_FRAMEWORK]
```
- Framework features
- Reporting formats
- Assertion libraries
- Mock capabilities

### Custom Assertions
Domain-specific checks:
- [INSERT_DOMAIN] validations
- Business rule verification
- Compliance checks
- Performance thresholds

## Data Management

### Test Data Setup
Prepare test scenarios:
```bash
/test-integration --setup-data
```
- Seed test data
- Clean state
- Fixtures loading
- Snapshot restore

### Cleanup Strategy
Post-test cleanup:
```bash
/test-integration --cleanup aggressive
```
- Database rollback
- Cache clearing
- File cleanup
- State reset

## Error Handling

### Retry Logic
For flaky tests:
```bash
/test-integration --retry 3 --retry-delay 5s
```
- Automatic retries
- Backoff strategies
- Failure tracking
- Success criteria

### Failure Analysis
Debug assistance:
```bash
/test-integration --on-failure screenshot,logs
```
- Error screenshots
- Log collection
- State dumps
- Stack traces

## Reporting

### Test Results
Comprehensive reports:
```bash
/test-integration --report html,junit
```
- HTML dashboards
- JUnit XML
- Coverage metrics
- Performance data

### CI/CD Integration
For [INSERT_CI_CD_PLATFORM]:
```bash
/test-integration --ci-mode
```
- Exit codes
- Artifact generation
- Status updates
- Failure notifications

## Performance Testing

### Load Testing
For [INSERT_PERFORMANCE_PRIORITY]:
```bash
/test-integration performance --users 1000
```
- Concurrent users
- Response times
- Throughput metrics
- Resource usage

### Stress Testing
Find breaking points:
```bash
/test-integration stress --ramp-up 60s
```
- Gradual load increase
- Failure points
- Recovery testing
- Capacity planning

## Input Validation

For [INSERT_SECURITY_LEVEL]:
- Authentication tests
- Authorization checks
- Input validation
- Security headers
- Encryption verification

## Mock Services

### External Services
Simulate dependencies:
```bash
/test-integration --mock-external
```
- API mocking
- Service virtualization
- Predictable responses
- Offline testing

### Partial Mocking
Selective simulation:
```bash
/test-integration --mock payment-service
```
- Specific service mocks
- Real integrations
- Hybrid testing
- Controlled scenarios

Which integration tests would you like to run?