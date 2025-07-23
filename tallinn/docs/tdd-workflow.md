# Test-Driven Development (TDD) Workflow

## Overview

This document provides a comprehensive guide to implementing Test-Driven Development (TDD) within the Claude Code Modular Prompts Tallinn project. TDD is a software development practice where tests are written before the actual implementation code, following the Red-Green-Refactor cycle.

## The Red-Green-Refactor Cycle

### 🔴 Red Phase: Write a Failing Test
1. **Write the smallest possible test** that expresses the desired behavior
2. **Run the test** - it should fail because the feature doesn't exist yet
3. **Verify the failure** - make sure the test fails for the right reason

### 🟢 Green Phase: Make it Pass
1. **Write the minimal code** to make the test pass
2. **Don't worry about code quality** - focus on making it work
3. **Run all tests** to ensure nothing is broken

### 🔵 Refactor Phase: Improve the Code
1. **Clean up the code** while keeping all tests passing
2. **Remove duplication** and improve design
3. **Run tests frequently** during refactoring

## TDD Process for This Project

### Step-by-Step Implementation

#### 1. Set Up Test Environment
```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-mock pytest-cov

# Run tests to verify setup
python -m pytest tests/ -v
```

#### 2. Identify What to Test
- **Unit Functions**: Individual functions with clear inputs/outputs
- **Class Methods**: Methods with specific behaviors
- **Integration Points**: Where modules interact
- **Error Conditions**: Edge cases and failure scenarios

#### 3. Write Test First (Red)
```python
# Example: Testing a utility function
def test_extract_metadata_from_frontmatter():
    """Test extraction of metadata from markdown frontmatter."""
    # Arrange
    content = """---
name: /test-command
description: Test command
usage: /test-command [args]
---

# Command content
"""
    processor = ContentProcessor(Path("/fake/path"))
    
    # Act & Assert - this will fail initially
    result = processor.extract_frontmatter_metadata(content)
    
    assert result['name'] == '/test-command'
    assert result['description'] == 'Test command'
    assert result['usage'] == '/test-command [args]'
```

#### 4. Implement Minimal Code (Green)
```python
def extract_frontmatter_metadata(self, content: str) -> Dict[str, str]:
    """Extract metadata from frontmatter - minimal implementation."""
    import re
    
    # Find frontmatter block
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    # Parse YAML-like structure
    metadata = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    return metadata
```

#### 5. Refactor and Improve (Blue)
```python
def extract_frontmatter_metadata(self, content: str) -> Dict[str, str]:
    """Extract metadata from YAML frontmatter block."""
    frontmatter_pattern = r'^---\n(.*?)\n---'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if not match:
        return {}
    
    metadata = {}
    yaml_content = match.group(1)
    
    for line in yaml_content.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    return metadata
```

## Common TDD Patterns and Best Practices

### 1. Test Naming Convention
```python
def test_[method_name]_[scenario]_[expected_behavior]():
    """
    Examples:
    - test_encrypt_api_key_with_valid_input_returns_key_id()
    - test_discover_resources_with_empty_directory_returns_empty_list()
    - test_extract_metadata_with_malformed_yaml_handles_gracefully()
    """
```

### 2. Arrange-Act-Assert Pattern
```python
def test_example():
    # Arrange: Set up test data and conditions
    input_data = "test input"
    expected_result = "expected output"
    
    # Act: Execute the code under test
    actual_result = function_under_test(input_data)
    
    # Assert: Verify the results
    assert actual_result == expected_result
```

### 3. Test Isolation and Independence
```python
@pytest.fixture
def temp_project():
    """Create isolated test environment."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)

def test_function_a(temp_project):
    # This test won't affect other tests
    pass

def test_function_b(temp_project):
    # Fresh environment for each test
    pass
```

## Mocking Strategies for Our Dependencies

### 1. File System Operations
```python
from unittest.mock import patch, mock_open

@patch('builtins.open', new_callable=mock_open, read_data='file content')
@patch('pathlib.Path.exists', return_value=True)
def test_load_component(mock_exists, mock_file):
    processor = ContentProcessor(Path("/fake"))
    result = processor.load_component("component.md")
    assert result == 'file content'
```

### 2. Async Operations
```python
@pytest.mark.asyncio
async def test_async_function():
    with patch('module.async_dependency') as mock_async:
        mock_async.return_value = AsyncMock(return_value="async result")
        
        result = await function_under_test()
        assert result == "async result"
```

### 3. External Dependencies
```python
@patch('secure_api_key_manager.os.environ.get')
@patch('secure_api_key_manager.secrets.token_urlsafe')
def test_generate_master_key(mock_token, mock_env):
    mock_env.return_value = None  # No env var
    mock_token.return_value = "secure_token_123"
    
    manager = SecureAPIKeyManager()
    # Test behavior when no master key exists
```

## Testing Different Module Types

### 1. Pure Functions (Easiest to Test)
```python
# Function: extract_examples_from_content()
def test_extract_examples_simple_case():
    content = """
    ## Examples
    ```bash
    /command arg1 arg2
    ```
    """
    result = extract_examples_from_content(content)
    assert len(result) == 1
    assert result[0]['code'] == '/command arg1 arg2'
```

### 2. Stateful Classes (Moderate Complexity)
```python
# Class: SecureAPIKeyManager
def test_encrypt_decrypt_roundtrip():
    manager = SecureAPIKeyManager(master_key="test_key_123")
    
    # Encrypt
    key_id = manager.encrypt_api_key("test", "secret_api_key")
    assert key_id.startswith("key_")
    
    # Decrypt
    decrypted = manager.decrypt_api_key(key_id)
    assert decrypted['api_key'] == "secret_api_key"
    assert decrypted['name'] == "test"
```

### 3. Async/Complex Modules (Highest Complexity)
```python
# Class: ClaudeCodeMCPServer
@pytest.mark.asyncio
async def test_discover_resources_integration():
    # Setup real-ish test environment
    temp_project = create_temp_project_structure()
    server = ClaudeCodeMCPServer(str(temp_project))
    
    # Test full discovery process
    resources = await server._discover_resources()
    
    assert len(resources) > 0
    assert any("commands" in r.uri for r in resources)
    assert any("components" in r.uri for r in resources)
```

## Integration with pytest and Our Test Infrastructure

### 1. Test Configuration (pytest.ini)
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --cov=.
    --cov-report=term-missing
    --cov-report=html:htmlcov
asyncio_mode = auto
```

### 2. Fixtures for Common Setup
```python
# tests/conftest.py
@pytest.fixture
def sample_command_content():
    return """---
name: /test-command
description: A test command
tools: Read, Write
---

# Test Command
This is a test.
"""

@pytest.fixture
def temp_project_structure():
    """Create standardized temp project for tests."""
    temp_path = create_temp_project()
    # Add standard directories and files
    yield temp_path
    shutil.rmtree(temp_path)
```

### 3. Test Categories and Markers
```python
# Mark slow tests
@pytest.mark.slow
def test_large_file_processing():
    pass

# Mark integration tests
@pytest.mark.integration
def test_full_workflow():
    pass

# Run specific categories
# pytest -m "not slow"  # Skip slow tests
# pytest -m integration  # Only integration tests
```

## Common TDD Antipatterns to Avoid

### ❌ Writing Tests After Implementation
```python
# WRONG: Implementation first, then test
def complex_function():
    # 50 lines of complex logic
    pass

def test_complex_function():
    # Test written to match existing behavior
    pass
```

### ❌ Testing Implementation Details
```python
# WRONG: Testing internal methods
def test_internal_method_calls():
    obj = MyClass()
    obj.public_method()
    assert obj._internal_counter == 5  # Testing internals
```

### ❌ Overly Complex Tests
```python
# WRONG: Test doing too much
def test_everything():
    # Tests multiple behaviors at once
    # Hard to understand what's being tested
    # Fails for multiple reasons
    pass
```

### ❌ Tests That Don't Add Value
```python
# WRONG: Testing trivial getters/setters
def test_get_name():
    obj = MyClass()
    obj.name = "test"
    assert obj.name == "test"  # No real logic tested
```

## Best Practices for This Project

### 1. Test File Organization
```
tests/
├── unit/                    # Unit tests for individual modules
│   ├── test_content_processor.py
│   ├── test_secure_api_key_manager.py
│   └── test_mcp_server.py
├── integration/             # Integration tests
│   ├── test_command_workflow.py
│   └── test_full_pipeline.py
├── fixtures/               # Test data and fixtures
│   ├── sample_commands/
│   └── test_configs/
└── conftest.py            # Shared fixtures
```

### 2. Continuous Testing Workflow
```bash
# Run tests continuously during development
pytest --watch

# Run with coverage
pytest --cov=. --cov-report=html

# Run only failed tests
pytest --lf

# Run specific test file
pytest tests/unit/test_content_processor.py -v
```

### 3. Pre-commit Testing
```bash
# Add to .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

## Measuring TDD Success

### 1. Test Coverage Metrics
```bash
# Generate coverage report
pytest --cov=. --cov-report=term-missing

# Aim for:
# - 80%+ line coverage for critical modules
# - 60%+ overall project coverage
# - 100% coverage for utility functions
```

### 2. Test Quality Indicators
- **Fast execution**: Unit tests should run in milliseconds
- **Clear failures**: Test failures should immediately indicate the problem
- **Independent**: Tests don't depend on each other
- **Repeatable**: Same results every time

### 3. Development Velocity
- **Fewer bugs**: TDD catches issues early
- **Confident refactoring**: Tests enable safe code changes
- **Living documentation**: Tests document expected behavior

## Real-World TDD Examples

See the `/docs/tdd-examples/` directory for detailed, step-by-step TDD implementations using actual modules from this codebase:

1. **[Simple Function TDD](tdd-examples/01-simple-function.md)**: Testing `ContentProcessor.extract_frontmatter_metadata()`
2. **[Class with Dependencies TDD](tdd-examples/02-class-dependencies.md)**: Testing `SecureAPIKeyManager`
3. **[Async/Complex Module TDD](tdd-examples/03-async-complex.md)**: Testing `ClaudeCodeMCPServer`

Each example shows the complete Red-Green-Refactor cycle with actual code from our project.

## Conclusion

TDD is a discipline that requires practice but pays dividends in code quality, maintainability, and developer confidence. By following the Red-Green-Refactor cycle and using the patterns described in this guide, you'll create robust, well-tested code that's easier to maintain and extend.

Remember: **The goal isn't perfect test coverage, but confident, maintainable code that serves its purpose reliably.**