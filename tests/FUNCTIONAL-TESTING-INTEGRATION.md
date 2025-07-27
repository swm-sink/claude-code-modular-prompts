# Functional Testing Framework Integration Guide

## Overview

This document provides complete integration instructions for the Claude Code Modular Prompts functional testing framework. The system extends the existing structural validation with comprehensive functional behavior testing, security validation, and LLM-graded evaluation.

## Architecture Overview

### Testing Pipeline Flow
```
Command Files → Structural Validation → Functional Testing → Security Testing → LLM Evaluation → Comprehensive Report
```

### Framework Components

#### 1. Mock Tool Environment (`mock_environment.py`)
- **Purpose**: Safe testing environment without real file system operations
- **Components**: MockFileSystem, MockBashEnvironment, MockSearchTools
- **Features**: Tool call logging, state export, resource tracking

#### 2. Security Testing Framework (`security_testing.py`)
- **Purpose**: Comprehensive security validation and vulnerability detection
- **Components**: InputSanitizationTester, OutputSanitizationTester, PermissionBoundaryTester
- **Features**: Injection prevention, information disclosure detection, access control validation

#### 3. LLM Evaluation System (`llm_evaluation.py`)
- **Purpose**: Quality assessment using LLM-graded metrics
- **Components**: CommandEvaluator, MockDeepEvalMetrics (production ready for DeepEval integration)
- **Features**: Multi-metric evaluation, automated grading, insight generation

#### 4. Functional Testing Orchestrator (`functional_testing.py`)
- **Purpose**: Comprehensive test execution and coordination
- **Components**: CommandLoader, FunctionalTestGenerator, FunctionalTestExecutor
- **Features**: Parallel execution, comprehensive reporting, test case generation

#### 5. Validation Pipeline (`validation-pipeline.sh`)
- **Purpose**: Integrated command-line interface for complete validation
- **Features**: Phase-by-phase execution, comprehensive reporting, flexible configuration

## Installation and Setup

### Prerequisites
```bash
# Python 3.8+ required
python3 --version

# Optional: Install production dependencies for enhanced evaluation
pip install pyyaml  # For YAML parsing
pip install deepeval  # For production LLM evaluation (optional)
pip install promptfoo  # For standardized prompt testing (optional)
```

### Directory Structure
```
tests/
├── FUNCTIONAL-TESTING-PLAN.md          # Implementation plan and architecture
├── FUNCTIONAL-TESTING-INTEGRATION.md   # This integration guide
├── TESTING-METHODOLOGY.md              # Original structural testing methodology
├── mock_environment.py                 # Mock tool environment
├── security_testing.py                 # Security testing framework
├── llm_evaluation.py                   # LLM evaluation system
├── functional_testing.py               # Main functional testing orchestrator
├── promptfoo-config.yaml               # PromptFoo configuration template
├── validate-command.sh                 # Original structural validation
├── validation-pipeline.sh              # Integrated validation pipeline
└── results/                            # Test results and reports (auto-created)
```

## Usage Instructions

### Quick Start

#### 1. Run Complete Validation Pipeline
```bash
# Run all validation phases
./tests/validation-pipeline.sh

# View results
ls tests/results/
```

#### 2. Run Individual Phases
```bash
# Structural validation only
./tests/validation-pipeline.sh --structural-only

# Functional testing only  
./tests/validation-pipeline.sh --functional-only

# Security testing only
./tests/validation-pipeline.sh --security-only

# LLM evaluation only
./tests/validation-pipeline.sh --llm-only
```

#### 3. Test Specific Commands
```bash
# Test individual command
python3 tests/functional_testing.py

# From Python
from tests.functional_testing import run_command_tests
results = run_command_tests('path/to/commands', 'task')
```

### Advanced Usage

#### Custom Test Configuration
```python
# Create custom test executor
from tests.functional_testing import FunctionalTestExecutor

executor = FunctionalTestExecutor('/path/to/commands', parallel_execution=True)

# Generate custom test cases
test_cases = executor.test_generator.generate_basic_tests(command_data)

# Execute with custom validation criteria
results = executor.execute_test_suite('command_name')
```

#### Security Testing Integration
```python
from tests.security_testing import create_security_test_suite

# Create security test suite
suite = create_security_test_suite()

# Run comprehensive security tests
def mock_command(input_text):
    return f"Processed: {input_text}"

report = suite.run_comprehensive_security_tests(mock_command, 'command_name')
print(f"Security Score: {report['security_score']}%")
```

#### LLM Evaluation
```python
from tests.llm_evaluation import create_llm_evaluator

# Create evaluator (use_mock=False for production DeepEval)
evaluator = create_llm_evaluator(use_mock=True)

# Evaluate command output
report = evaluator.evaluate_command(
    command_name='task',
    input_text='create a hello world function',
    output_text='def hello(): print("Hello, World!")',
    expected_output='A simple hello world function'
)

print(f"Overall Score: {report.overall_score:.2f} (Grade: {report.grade})")
```

## Integration with Existing Workflow

### 1. Extend Current Testing Methodology

The functional testing framework builds on the existing structural validation:

```bash
# Original workflow
./tests/validate-command.sh command.md

# Extended workflow  
./tests/validation-pipeline.sh --commands-dir .claude/commands
```

### 2. CI/CD Integration

#### GitHub Actions Example
```yaml
name: Claude Code Command Validation

on:
  push:
    paths:
      - '.claude/commands/**'
  pull_request:
    paths:
      - '.claude/commands/**'

jobs:
  validate-commands:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
          
      - name: Install dependencies
        run: |
          pip install pyyaml
          
      - name: Run validation pipeline
        run: |
          ./tests/validation-pipeline.sh
          
      - name: Upload test results
        uses: actions/upload-artifact@v2
        with:
          name: test-results
          path: tests/results/
```

### 3. Development Workflow Integration

#### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running Claude Code command validation..."

# Run validation on staged command files
staged_commands=$(git diff --cached --name-only --diff-filter=ACM | grep '\.claude/commands/.*\.md$')

if [ -n "$staged_commands" ]; then
    echo "Validating staged command files..."
    
    # Run quick validation
    if ! ./tests/validation-pipeline.sh --structural-only --functional-only; then
        echo "❌ Command validation failed. Commit aborted."
        echo "Run ./tests/validation-pipeline.sh for detailed results."
        exit 1
    fi
    
    echo "✅ Command validation passed."
fi

exit 0
```

## Configuration Options

### Environment Variables
```bash
# Set custom commands directory
export CLAUDE_COMMANDS_DIR="/path/to/commands"

# Enable debug mode
export CLAUDE_TESTING_DEBUG=true

# Configure parallel execution
export CLAUDE_TESTING_PARALLEL_WORKERS=4

# Set security testing level
export CLAUDE_SECURITY_TESTING_LEVEL=strict
```

### PromptFoo Integration
```yaml
# tests/promptfoo-config.yaml
providers:
  - claude-3-5-sonnet-20241022

tests:
  - description: "Test command functionality"
    vars:
      command: "/task"
      input: "create hello world function"
    assert:
      - type: llm-rubric
        value: "Output includes proper function definition"
```

### DeepEval Configuration (Production)
```python
# For production use with actual DeepEval
from deepeval import evaluate
from deepeval.metrics import CorrectnessMetric, RelevanceMetric

# Configure evaluator for production
evaluator = create_llm_evaluator(use_mock=False)
```

## Performance Considerations

### Test Execution Performance
- **Parallel Execution**: Enabled by default for functional tests
- **Mock Environment**: Zero file system overhead
- **Incremental Testing**: Test only changed commands
- **Caching**: Mock environment state caching for repeated tests

### Resource Usage
- **Memory**: ~50MB per test execution
- **CPU**: Optimized for multi-core systems
- **Storage**: Minimal - mock environment only
- **Network**: None required for mock testing

## Monitoring and Reporting

### Real-time Monitoring
```bash
# Watch test execution
tail -f tests/results/validation_log_*.csv

# Monitor specific phase
./tests/validation-pipeline.sh --functional-only 2>&1 | tee functional_tests.log
```

### Report Analysis
```python
# Analyze test results programmatically
import json
from pathlib import Path

results_dir = Path('tests/results')
latest_report = max(results_dir.glob('comprehensive_report_*.md'))

# Parse and analyze results
with open(latest_report) as f:
    report_content = f.read()
    
# Extract metrics and trends
```

### Metrics Dashboard
The comprehensive report includes:
- **Test Coverage**: Percentage of commands tested
- **Success Rates**: Pass/fail rates by category
- **Security Scores**: Security compliance percentages
- **Quality Metrics**: LLM evaluation scores and grades
- **Performance Data**: Execution times and resource usage

## Troubleshooting

### Common Issues

#### 1. Python Dependencies
```bash
# Error: ModuleNotFoundError
pip install pyyaml

# For production LLM evaluation
pip install deepeval promptfoo
```

#### 2. File Permissions
```bash
# Make scripts executable
chmod +x tests/validation-pipeline.sh
chmod +x tests/validate-command.sh
```

#### 3. Path Issues
```bash
# Verify commands directory
ls .claude/commands/

# Check test scripts
ls -la tests/
```

#### 4. Mock Environment Issues
```python
# Reset mock environment
from tests.mock_environment import create_test_environment
env = create_test_environment()
env.reset_environment()
```

### Debug Mode
```bash
# Enable verbose output
./tests/validation-pipeline.sh --functional-only 2>&1 | tee debug.log

# Python debug mode
python3 -c "
import sys
sys.path.append('tests')
from functional_testing import create_functional_test_executor
executor = create_functional_test_executor('path/to/commands')
# Debug execution here
"
```

## Future Enhancements

### Planned Improvements
1. **Real DeepEval Integration**: Production LLM evaluation
2. **PromptFoo Integration**: Standardized prompt testing
3. **Performance Benchmarking**: Response time measurement
4. **Regression Testing**: Compare results over time
5. **User Acceptance Testing**: Real user interaction simulation

### Extensibility Points
- **Custom Metrics**: Add domain-specific evaluation criteria
- **Tool Extensions**: Support for additional Claude Code tools
- **Security Rules**: Custom security validation rules
- **Report Formats**: Additional output formats (XML, HTML, etc.)

## Support and Maintenance

### Getting Help
1. **Documentation**: Refer to implementation plan and architecture docs
2. **Test Results**: Check `tests/results/` for detailed execution logs
3. **Debug Logs**: Enable debug mode for detailed troubleshooting
4. **Framework Status**: Check comprehensive reports for system health

### Maintenance Schedule
- **Daily**: Monitor test execution and results
- **Weekly**: Review security and quality metrics
- **Monthly**: Update test cases and validation criteria
- **Quarterly**: Framework enhancement and optimization

---

*Functional Testing Framework Integration Guide v1.0*  
*Claude Code Modular Prompts - Experimental Framework*  
*Generated: 2025-07-27*