# Claude Code Modular Prompts - Master Project Memory

## 🚨 MANDATORY TDD ENFORCEMENT - NO EXCEPTIONS

### **ABSOLUTE RULES - VIOLATE AT PERIL**

**🔥 HARSH TDD ENFORCEMENT - ZERO TOLERANCE:**

1. **NO CODE WITHOUT TESTS FIRST** 
   - Every single line of code must have a test written BEFORE implementation
   - No exceptions, no excuses, no "quick fixes"
   - Test-first is not optional - it's mandatory

2. **90% MINIMUM TEST COVERAGE**
   - Below 90% coverage = IMMEDIATE FAILURE
   - Tests must cover all code paths, edge cases, and error conditions
   - Coverage reports run automatically on every commit

3. **SECURITY TESTS MANDATORY**
   - Every command must have security validation tests
   - Input sanitization tests required
   - Output validation tests required
   - No security vulnerabilities tolerated

4. **PERFORMANCE BENCHMARKS REQUIRED**
   - Every command must have performance baseline tests
   - Commands exceeding 100ms response time = FAILURE
   - Memory usage monitoring required
   - Performance regression = automatic rollback

5. **INTEGRATION TESTS NON-NEGOTIABLE**
   - Every command must integrate properly with Claude Code
   - End-to-end workflow tests required
   - Tool interaction tests mandatory

### **🛡️ QUALITY GATES - ALL MUST PASS**

**Pre-commit Hooks (ENFORCED):**
```bash
# These hooks BLOCK commits automatically
- pytest --cov=. --cov-fail-under=90
- security-audit --strict
- performance-benchmark --max-time=100ms
- integration-test --claude-code
- code-review --auto-approve=false
```

**Automated Validation Pipeline:**
```bash
# Every file change triggers full validation
1. Unit tests (must pass 100%)
2. Integration tests (must pass 100%) 
3. Security scanning (zero vulnerabilities)
4. Performance benchmarking (sub-100ms)
5. Code quality metrics (A+ grade required)
```

## 📁 Project Structure & Context

### **Current State**
- **Foundation**: 147 Claude Code compliant commands from `tallinn/.claude/commands`
- **Strategy**: Branch 3 - Hybrid Evolutionary (89.75% optimal score)
- **Approach**: Build on proven foundation, systematic TDD implementation

### **Directory Structure**
```
/
├── CLAUDE.md                    # THIS FILE - Master TDD enforcement
├── .claude/                     # Claude Code configuration
│   ├── settings.json           # Tool permissions & config
│   ├── commands/               # 50-70 curated, tested commands
│   │   ├── core/               # Essential commands (query, task, auto)
│   │   ├── development/        # Dev workflow commands
│   │   ├── security/           # Security audit commands
│   │   ├── testing/            # Test automation commands
│   │   ├── analysis/           # Code analysis commands
│   │   ├── utilities/          # Utility commands
│   │   └── workflow/           # Process automation
│   ├── docs/                   # Context documentation
│   └── templates/              # Command templates
├── tests/                      # COMPREHENSIVE test suite
│   ├── unit/                   # Unit tests for each command
│   ├── integration/            # Integration tests
│   ├── security/               # Security validation tests
│   └── performance/            # Performance benchmark tests
├── README.md                   # User-facing documentation
└── archived/                   # Legacy code (post-cleanup)
```

### **Source of Truth (Established)**
- **Commands**: `tallinn/.claude/commands` (147 commands - Claude Code compliant)
- **Components**: `tallinn/claude_prompt_factory/components` (comprehensive)
- **Tests**: `tallinn/tests/` (27 test files - foundation)
- **Scripts**: `tallinn/scripts/` (utility collection)

## 🧪 TDD FRAMEWORK - ULTRATHINK IMPLEMENTATION

### **Test-Driven Development Process**

**Phase 1: RED (Write Failing Test)**
```python
# MANDATORY: Write test BEFORE any implementation
def test_command_functionality():
    """Test must fail initially - no implementation exists yet"""
    result = execute_command("/example-command", "test-input")
    assert result.success == True
    assert result.output == "expected-output"
    assert result.performance < 100  # milliseconds
    assert result.security_validated == True
```

**Phase 2: GREEN (Minimal Implementation)**
```markdown
# Command implementation ONLY after test exists
---
name: /example-command
description: Brief description
usage: /example-command [arguments]
tools: Read, Write, Edit
tests: test_example_command.py
---

# Implementation that makes test pass
```

**Phase 3: REFACTOR (Improve Code Quality)**
```python
# Refactor with tests protecting against regression
def test_command_refactored():
    """Tests ensure refactoring doesn't break functionality"""
    # All previous tests must still pass
    # New tests for improved functionality
```

### **Test Categories (ALL MANDATORY)**

**1. Unit Tests**
```python
def test_command_unit():
    """Test individual command functionality"""
    # Input validation
    # Output format
    # Error handling
    # Edge cases
```

**2. Security Tests**
```python
def test_command_security():
    """Security validation - NO EXCEPTIONS"""
    # Input sanitization
    # Output validation
    # Permission checks
    # Vulnerability scanning
```

**3. Performance Tests**
```python
def test_command_performance():
    """Performance benchmarking - <100ms mandatory"""
    start_time = time.time()
    result = execute_command()
    execution_time = (time.time() - start_time) * 1000
    assert execution_time < 100  # HARD LIMIT
```

**4. Integration Tests**
```python
def test_command_integration():
    """Claude Code integration - must work seamlessly"""
    # Tool interaction
    # Context loading
    # Memory management
    # Error propagation
```

## 🔒 SECURITY ENFORCEMENT PATTERNS

### **Defensive Security Principles**
```python
# Every command must implement these patterns

def validate_input(user_input):
    """Mandatory input validation"""
    if not user_input or len(user_input) > MAX_INPUT_SIZE:
        raise SecurityError("Invalid input")
    
    # Sanitize against injection attacks
    sanitized = sanitize_input(user_input)
    return sanitized

def validate_output(output):
    """Mandatory output validation"""
    # Prevent information leakage
    # Sanitize sensitive data
    # Validate format
    return sanitized_output
```

### **Security Test Requirements**
```python
def test_security_comprehensive():
    """ALL commands must pass ALL security tests"""
    
    # Test 1: Input injection prevention
    malicious_input = "'; DROP TABLE commands; --"
    result = command_execute(malicious_input)
    assert not result.contains_injection()
    
    # Test 2: Output sanitization
    sensitive_data = "api_key=secret123"
    result = command_execute(sensitive_data)
    assert not result.contains_sensitive_data()
    
    # Test 3: Permission validation
    unauthorized_action = "/admin-command"
    result = command_execute(unauthorized_action)
    assert result.permission_denied()
```

## ⚡ PERFORMANCE OPTIMIZATION GUIDELINES

### **Performance Requirements (ENFORCED)**
- **Response Time**: <100ms per command (HARD LIMIT)
- **Memory Usage**: <50MB per command execution
- **Context Window**: Optimized loading, <5% waste
- **Caching**: Intelligent caching for repeated operations

### **Performance Test Framework**
```python
@performance_test(max_time=100)  # milliseconds
@memory_test(max_memory=50)      # megabytes
def test_command_performance():
    """Automatic performance validation"""
    with performance_monitor():
        result = execute_command()
        assert result.response_time < 100
        assert result.memory_usage < 50
```

## 🎯 QUALITY GATES & VALIDATION RULES

### **Commit Blocking Rules**
```yaml
# .pre-commit-config.yaml (ENFORCED)
quality_gates:
  - test_coverage: 90%        # Below 90% = BLOCKED
  - security_scan: zero       # Any vulnerabilities = BLOCKED  
  - performance: 100ms        # Slower than 100ms = BLOCKED
  - code_quality: A+          # Below A+ grade = BLOCKED
  - integration: pass         # Failed integration = BLOCKED
```

### **Continuous Validation Pipeline**
```bash
# Triggered on EVERY file change
pipeline:
  1. Pre-commit hooks (immediate blocking)
  2. Unit test execution (full suite)
  3. Security vulnerability scanning  
  4. Performance benchmark testing
  5. Integration test validation
  6. Code quality analysis
  7. Documentation completeness check
```

## 🧠 CONTEXT ENGINEERING HIERARCHY

### **Memory Import Patterns**
```markdown
# Hierarchical context loading
@import .claude/docs/claude-code-best-practices.md
@import .claude/docs/dependency-matrix.md  
@import .claude/docs/tree-of-thought-strategy.md
@import .claude/templates/command-template.md
@import tests/templates/test-template.py
```

### **Context Optimization**
- **Selective Loading**: Only load relevant context
- **Hierarchical Structure**: General → Specific context
- **Caching Strategy**: Cache frequently accessed patterns
- **Memory Management**: Efficient context window usage

## 🚀 COMMAND DEVELOPMENT WORKFLOW

### **MANDATORY Process (NO SHORTCUTS)**

1. **Analysis Phase**
   ```bash
   # Understand requirements thoroughly
   - Document command purpose
   - Define input/output specifications  
   - Identify security considerations
   - Plan performance requirements
   ```

2. **Test-First Implementation**
   ```bash
   # TDD Phase - TESTS BEFORE CODE
   - Write failing unit tests
   - Write security validation tests
   - Write performance benchmark tests
   - Write integration tests
   ```

3. **Minimal Implementation**
   ```bash
   # Make tests pass with minimal code
   - Implement core functionality
   - Ensure all tests pass
   - Validate security requirements
   - Confirm performance benchmarks
   ```

4. **Quality Validation**
   ```bash
   # MANDATORY quality gates
   - Run full test suite (90%+ coverage)
   - Security audit (zero vulnerabilities)
   - Performance validation (<100ms)
   - Integration testing (full compatibility)
   ```

5. **Documentation & Review**
   ```bash
   # Complete the development cycle
   - Update documentation
   - Code review (mandatory)
   - Final validation
   - Atomic commit with tests
   ```

## 📚 DOCUMENTATION STANDARDS

### **Command Documentation Template**
```markdown
# /command-name

## Purpose
Brief description of command functionality

## Usage
```
/command-name [arguments]
```

## Tests
- Unit tests: `tests/unit/test_command_name.py`
- Security tests: `tests/security/test_command_name_security.py`
- Performance tests: `tests/performance/test_command_name_perf.py`
- Integration tests: `tests/integration/test_command_name_integration.py`

## Performance Metrics
- Response time: <100ms
- Memory usage: <50MB
- Test coverage: >90%

## Security Considerations
- Input validation: [describe]
- Output sanitization: [describe]
- Permission requirements: [list]
```

## 🛠️ DEVELOPMENT TOOLS & AUTOMATION

### **Required Development Stack**
```bash
# Testing Framework
pytest>=7.0.0           # Unit testing
pytest-cov>=4.0.0       # Coverage reporting
pytest-security>=0.1.0  # Security testing
pytest-benchmark>=4.0.0 # Performance testing

# Security Tools  
bandit>=1.7.0           # Security linting
safety>=2.0.0           # Dependency scanning
semgrep>=1.0.0          # Static analysis

# Performance Tools
memory-profiler>=0.60.0 # Memory monitoring
py-spy>=0.3.0           # Performance profiling
```

### **Automation Scripts**
```bash
# Pre-commit automation (ENFORCED)
#!/bin/bash
# run-tdd-validation.sh

echo "🧪 Running TDD validation pipeline..."

# Phase 1: Unit tests with coverage
pytest --cov=. --cov-fail-under=90 --cov-report=html
if [ $? -ne 0 ]; then
    echo "❌ FAILED: Test coverage below 90%"
    exit 1
fi

# Phase 2: Security scanning
bandit -r . -f json -o security-report.json
if [ $? -ne 0 ]; then
    echo "❌ FAILED: Security vulnerabilities detected"
    exit 1
fi

# Phase 3: Performance benchmarking
pytest tests/performance/ --benchmark-max-time=0.1
if [ $? -ne 0 ]; then
    echo "❌ FAILED: Performance benchmarks exceeded 100ms"
    exit 1
fi

# Phase 4: Integration testing
pytest tests/integration/ -v
if [ $? -ne 0 ]; then
    echo "❌ FAILED: Integration tests failed"
    exit 1
fi

echo "✅ SUCCESS: All TDD validation gates passed"
```

## 🎯 SUCCESS METRICS & KPIs

### **Quality Metrics (MONITORED)**
- **Test Coverage**: 90%+ (ENFORCED)
- **Security Score**: Zero vulnerabilities (ENFORCED)
- **Performance**: <100ms response time (ENFORCED)
- **Code Quality**: A+ grade (ENFORCED)
- **Documentation**: 100% coverage (REQUIRED)

### **Project Health Dashboard**
```yaml
# Automated monitoring
metrics:
  test_coverage: 90%+
  security_vulnerabilities: 0
  performance_baseline: <100ms
  command_count: 50-70 (curated)
  documentation_completeness: 100%
  user_satisfaction: 9/10+
```

---

## ⚠️ FINAL WARNING - TDD ENFORCEMENT

**This project enforces TDD with ZERO tolerance for violations.**

- **No code without tests first**
- **No commits without passing all quality gates**  
- **No exceptions for "urgent" or "quick" fixes**
- **No compromises on security or performance**

**Violate TDD principles = Automatic rollback + mandatory rewrite**

*This is not negotiable. This is not optional. This is mandatory.*

---

*Generated: 2025-07-23*  
*Strategy: Branch 3 - Hybrid Evolutionary*  
*TDD Enforcement: MAXIMUM*  
*Quality Gates: UNCOMPROMISING*