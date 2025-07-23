# Test Coverage Improvement Plan - 90% Target

**Current State**: 23.8% coverage (down from 30% due to test failures)  
**Goal**: 90% coverage with robust, real tests  
**Gap**: 66.2% coverage increase needed

## Critical Issues to Fix First

### 1. Import Errors in Test Files (BLOCKING - 74 errors)
- **Issue**: Missing `os` import in test files causing fixture failures
- **Impact**: 74 test errors preventing coverage calculation
- **Fix**: Add missing imports to all test files

### 2. Module Import Path Issues
- **Issue**: Test modules can't find the modules they're testing
- **Impact**: 0% coverage on most modules
- **Fix**: Ensure correct Python path setup in tests

### 3. Test Quality Issues
- **Issue**: Some tests are too shallow or mock too much
- **Impact**: Low effective coverage even when tests pass
- **Fix**: Write tests that exercise real code paths

## Coverage Gap Analysis

### Modules with 0% Coverage (High Priority)
1. **mcp_server.py** (280 statements) - Core functionality
2. **secure_api_key_manager.py** (190 statements) - Security critical
3. **performance/benchmarker.py** (184 statements) - Performance module
4. **performance/context_optimizer.py** (227 statements) - Complex algorithms
5. **performance/monitor.py** (212 statements) - Monitoring functionality
6. **run_comprehensive_tests.py** (338 statements) - Test runner
7. **test_data_management.py** (313 statements) - Test utilities
8. **command_processing/** modules (430+ statements) - Core processing

### Modules with Low Coverage (15-20%)
1. **security/audit_checkers.py** (15% - 162/191 missed)
2. **security/key_rotation.py** (16% - 98/117 missed)
3. **security/report_generator.py** (19% - 75/93 missed)

## Implementation Strategy (DAG Approach)

### Phase 1: Fix Foundation Issues (Day 1 - Morning)
```
Task 1.1: Fix import errors in all test files
├── Add missing os import
├── Fix other missing imports
└── Verify all tests can at least start

Task 1.2: Fix Python path issues
├── Update test __init__.py files
├── Add proper sys.path configuration
└── Ensure modules can be imported

Task 1.3: Run tests and verify baseline
├── All tests should at least run (pass/fail)
├── No more import errors
└── Establish true baseline coverage
```

### Phase 2: Core Module Testing (Day 1 - Afternoon)
```
Task 2.1: MCP Server Testing (Target: 80% coverage)
├── Server initialization tests
├── Resource discovery tests
├── Command execution tests
├── Error handling tests
└── Integration tests

Task 2.2: Secure API Key Manager (Target: 85% coverage)
├── Encryption/decryption tests
├── Key storage/retrieval tests
├── Master key management tests
├── Security edge cases
└── Thread safety tests

Task 2.3: Command Processing Modules (Target: 75% coverage)
├── XML parser tests
├── Component extractor tests
├── Content processor tests
└── Markdown generator tests
```

### Phase 3: Performance Module Testing (Day 2 - Morning)
```
Task 3.1: Performance Monitor (Target: 70% coverage)
├── Metric collection tests
├── Resource tracking tests
├── Report generation tests
└── Alert threshold tests

Task 3.2: Performance Benchmarker (Target: 70% coverage)
├── Benchmark execution tests
├── Result analysis tests
├── Comparison tests
└── Report generation tests

Task 3.3: Context Optimizer (Target: 60% coverage)
├── Token optimization tests
├── Context window tests
├── Strategy selection tests
└── Performance validation tests
```

### Phase 4: Security & Utility Testing (Day 2 - Afternoon)
```
Task 4.1: Security Modules (Target: 80% coverage)
├── Audit checker enhancements
├── Key rotation improvements
├── Report generator tests
└── OWASP compliance tests

Task 4.2: Utility Scripts (Target: 70% coverage)
├── Test data management
├── Comprehensive test runner
├── XML fixers and validators
└── Script utilities
```

### Phase 5: Integration & E2E Testing (Day 3)
```
Task 5.1: Integration Tests (Target: 85% coverage)
├── Module interaction tests
├── Workflow orchestration tests
├── Error propagation tests
└── Configuration validation

Task 5.2: End-to-End Tests (Target: 90% coverage)
├── Complete workflow tests
├── User scenario tests
├── Performance benchmarks
└── Security audit workflows
```

## Test Types Distribution

### Unit Tests (60% of total tests)
- Isolated function testing
- Mock external dependencies
- Fast execution
- High code coverage

### Integration Tests (25% of total tests)
- Module interaction testing
- Partial mocking
- Real data flow
- Error propagation

### Contract Tests (10% of total tests)
- API contracts
- Interface validation
- Schema testing
- Version compatibility

### E2E Tests (5% of total tests)
- Full workflow testing
- No mocking
- Real environment
- User scenarios

## TDD Implementation Process

For each module:
1. **Red**: Write failing test for expected behavior
2. **Green**: Implement minimal code to pass
3. **Refactor**: Improve code while keeping tests green
4. **Repeat**: Add more test cases

### Example TDD Cycle for mcp_server.py
```python
# Test 1: Server initialization
def test_server_initializes_with_default_config():
    # Red: Test fails - no implementation
    server = MCPServer()
    assert server.project_root == Path.cwd()
    
# Implement minimal code to pass
# Green: Test passes

# Test 2: Resource discovery
def test_server_discovers_command_resources():
    # Red: Test fails
    server = MCPServer(test_dir)
    resources = server.discover_resources()
    assert len(resources) > 0
    
# Implement discovery logic
# Green: Test passes

# Continue with more complex scenarios...
```

## Success Metrics

### Coverage Targets by Module Type
- **Core Modules**: 85-90% coverage
- **Security Modules**: 90-95% coverage
- **Utility Modules**: 70-80% coverage
- **Scripts**: 60-70% coverage
- **Test Files**: Excluded from coverage

### Quality Metrics
- **Branch Coverage**: >80%
- **Function Coverage**: >90%
- **Line Coverage**: >90%
- **Mutation Score**: >70% (stretch goal)

## Risk Mitigation

### Risk 1: Complex Module Testing
- **Mitigation**: Start with simple cases, gradually add complexity
- **Fallback**: Accept lower coverage on most complex parts

### Risk 2: External Dependencies
- **Mitigation**: Use mocking strategically, not excessively
- **Fallback**: Create test doubles for complex dependencies

### Risk 3: Time Constraints
- **Mitigation**: Prioritize high-value modules first
- **Fallback**: Focus on critical path coverage

## Tooling & Configuration

### pytest Configuration Enhancement
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short --strict-markers --cov=. --cov-report=term-missing --cov-report=html --cov-report=json

[coverage:run]
source = .
omit = 
    */tests/*
    */test_*
    */__pycache__/*
    */venv/*
    */env/*
    setup.py
    conftest.py

[coverage:report]
exclude_lines = 
    pragma: no cover
    def __repr__
    if __name__ == .__main__.:
    raise AssertionError
    raise NotImplementedError
precision = 2
show_missing = True
skip_empty = True
```

### Test Fixtures & Utilities
- Centralized test data factories
- Reusable mock objects
- Performance benchmarking fixtures
- Security testing utilities

## Timeline & Milestones

### Day 1 (8 hours)
- **Morning**: Fix all import issues, establish baseline (4 hours)
- **Afternoon**: Core module testing - mcp_server, secure_api_key_manager (4 hours)
- **Target**: 45% coverage

### Day 2 (8 hours)
- **Morning**: Performance modules, command processing (4 hours)
- **Afternoon**: Security modules, utilities (4 hours)
- **Target**: 70% coverage

### Day 3 (4-6 hours)
- **Morning**: Integration tests, E2E tests (3 hours)
- **Afternoon**: Gap filling, edge cases (2-3 hours)
- **Target**: 90%+ coverage

## Commit Strategy

### Atomic Commits
- One commit per module tested
- Clear commit messages
- Include coverage metrics in commit message

### Example Commit Messages
```
test: Add comprehensive tests for mcp_server.py (0% → 85% coverage)
test: Fix import errors in all test files - restore test execution
test: Add security tests for api_key_manager (0% → 90% coverage)
test: Implement integration tests for command processing pipeline
```

## Next Steps

1. Fix all import errors (Task 1.1)
2. Verify tests can run without errors
3. Begin TDD implementation for mcp_server.py
4. Track progress using todo list
5. Commit after each module completion

---

**Created**: 2025-07-23  
**Version**: 1.0  
**Target Completion**: 2.5 days