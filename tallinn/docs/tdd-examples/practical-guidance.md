# Practical TDD Guidance for the Tallinn Project

This document provides concrete, actionable guidance for applying Test-Driven Development (TDD) effectively within the Claude Code Modular Prompts Tallinn project. It focuses on real-world scenarios, common challenges, and project-specific best practices.

## Writing Testable Code

### Design Principles for Testability

#### 1. Single Responsibility Principle
Each function/class should have one clear responsibility.

```python
# ❌ BAD: Multiple responsibilities
class CommandProcessor:
    def process_command(self, file_path):
        # File reading
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Parsing
        metadata = self.parse_frontmatter(content)
        
        # Validation
        if not metadata.get('name'):
            raise ValueError("Missing name")
        
        # Formatting
        formatted = self.format_output(metadata)
        
        # File writing
        with open(f"output_{file_path}", 'w') as f:
            f.write(formatted)
        
        return formatted

# ✅ GOOD: Separated responsibilities
class FileReader:
    def read_file(self, file_path: str) -> str:
        with open(file_path, 'r') as f:
            return f.read()

class FrontmatterParser:
    def parse_frontmatter(self, content: str) -> Dict[str, str]:
        # Parsing logic only
        pass

class MetadataValidator:
    def validate_metadata(self, metadata: Dict[str, str]) -> None:
        if not metadata.get('name'):
            raise ValueError("Missing name")

class OutputFormatter:
    def format_output(self, metadata: Dict[str, str]) -> str:
        # Formatting logic only
        pass

class CommandProcessor:
    def __init__(self, reader, parser, validator, formatter):
        self.reader = reader
        self.parser = parser
        self.validator = validator
        self.formatter = formatter
    
    def process_command(self, file_path: str) -> str:
        content = self.reader.read_file(file_path)
        metadata = self.parser.parse_frontmatter(content)
        self.validator.validate_metadata(metadata)
        return self.formatter.format_output(metadata)
```

#### 2. Dependency Injection
Make dependencies explicit and injectable.

```python
# ❌ BAD: Hard-coded dependencies
class SecureAPIKeyManager:
    def __init__(self):
        self.cipher = Fernet(self._generate_key())  # Hard to test
        self.file_path = "encrypted_keys.json"      # Hard to test
    
    def _generate_key(self):
        return Fernet.generate_key()  # Random, non-deterministic

# ✅ GOOD: Injectable dependencies
class SecureAPIKeyManager:
    def __init__(self, cipher=None, file_path=None, key_generator=None):
        self.cipher = cipher or self._default_cipher()
        self.file_path = file_path or "encrypted_keys.json"
        self.key_generator = key_generator or Fernet.generate_key
    
    def _default_cipher(self):
        return Fernet(self.key_generator())
```

#### 3. Pure Functions Where Possible
Functions without side effects are easiest to test.

```python
# ✅ GOOD: Pure function
def extract_command_name(frontmatter_content: str) -> Optional[str]:
    """Extract command name from frontmatter content."""
    for line in frontmatter_content.split('\n'):
        if line.strip().startswith('name:'):
            return line.split(':', 1)[1].strip()
    return None

# Test is simple
def test_extract_command_name():
    content = "name: /test-command\ndescription: Test"
    assert extract_command_name(content) == "/test-command"
```

### Project-Specific Testable Patterns

#### Pattern 1: Command Processing
```python
# Testable command processing structure
class CommandMetadataExtractor:
    """Extracts metadata from command files."""
    
    def extract_from_file(self, file_path: Path) -> Dict[str, str]:
        content = self._read_file(file_path)
        return self.extract_from_content(content)
    
    def extract_from_content(self, content: str) -> Dict[str, str]:
        """Pure function - easy to test."""
        return self._parse_frontmatter(content)
    
    def _read_file(self, file_path: Path) -> str:
        """Separate file I/O - can be mocked."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _parse_frontmatter(self, content: str) -> Dict[str, str]:
        """Pure parsing logic."""
        # Implementation here
        pass

# Testing becomes straightforward
def test_extract_from_content():
    extractor = CommandMetadataExtractor()
    content = """---
name: /test
description: Test command
---
# Content"""
    
    result = extractor.extract_from_content(content)
    assert result['name'] == '/test'
    assert result['description'] == 'Test command'

@patch.object(CommandMetadataExtractor, '_read_file', return_value="mocked content")
def test_extract_from_file(mock_read):
    extractor = CommandMetadataExtractor()
    
    with patch.object(extractor, 'extract_from_content', return_value={'name': '/test'}) as mock_extract:
        result = extractor.extract_from_file(Path("/fake/path"))
        
        mock_read.assert_called_once_with(Path("/fake/path"))
        mock_extract.assert_called_once_with("mocked content")
        assert result == {'name': '/test'}
```

#### Pattern 2: Async Resource Management
```python
# Testable async resource management
class ResourceDiscoveryService:
    """Manages async resource discovery with testable structure."""
    
    def __init__(self, file_scanner=None, metadata_extractor=None):
        self.file_scanner = file_scanner or DefaultFileScanner()
        self.metadata_extractor = metadata_extractor or MetadataExtractor()
        self._cache = {}
    
    async def discover_resources(self, root_path: Path) -> List[Resource]:
        """Main entry point - coordinates other methods."""
        if root_path in self._cache:
            return self._cache[root_path]
        
        files = await self.file_scanner.scan_directory(root_path)
        resources = await self._process_files(files)
        
        self._cache[root_path] = resources
        return resources
    
    async def _process_files(self, files: List[Path]) -> List[Resource]:
        """Process files - can be tested with mock files."""
        resources = []
        for file_path in files:
            try:
                metadata = await self.metadata_extractor.extract_async(file_path)
                resource = self._create_resource(file_path, metadata)
                resources.append(resource)
            except Exception as e:
                # Log error but continue processing
                logger.warning(f"Failed to process {file_path}: {e}")
        return resources
    
    def _create_resource(self, file_path: Path, metadata: Dict) -> Resource:
        """Pure function - easy to test."""
        return Resource(
            uri=f"file://{file_path}",
            name=metadata.get('name', file_path.stem),
            description=metadata.get('description', ''),
            metadata=metadata
        )

# Testing async components
@pytest.mark.asyncio
async def test_discover_resources_with_mocked_dependencies():
    # Mock dependencies
    mock_scanner = AsyncMock()
    mock_scanner.scan_directory.return_value = [Path("test1.md"), Path("test2.md")]
    
    mock_extractor = AsyncMock()
    mock_extractor.extract_async.side_effect = [
        {'name': '/test1', 'description': 'First test'},
        {'name': '/test2', 'description': 'Second test'}
    ]
    
    service = ResourceDiscoveryService(
        file_scanner=mock_scanner,
        metadata_extractor=mock_extractor
    )
    
    # Act
    resources = await service.discover_resources(Path("/fake/root"))
    
    # Assert
    assert len(resources) == 2
    assert resources[0].name == '/test1'
    assert resources[1].name == '/test2'
    
    # Verify dependencies were called correctly
    mock_scanner.scan_directory.assert_called_once_with(Path("/fake/root"))
    assert mock_extractor.extract_async.call_count == 2
```

## Mocking Strategies for Our Specific Dependencies

### 1. File System Operations

#### Basic File Mocking
```python
from unittest.mock import mock_open, patch

# Mock file reading
@patch('builtins.open', new_callable=mock_open, read_data='file content')
def test_file_reading(mock_file):
    result = read_command_file('/fake/path')
    assert result == 'file content'
    mock_file.assert_called_once_with('/fake/path', 'r', encoding='utf-8')

# Mock Path operations
@patch('pathlib.Path.exists', return_value=True)
@patch('pathlib.Path.is_file', return_value=True)
def test_path_operations(mock_is_file, mock_exists):
    processor = CommandProcessor()
    result = processor.validate_file_path(Path('/fake/file'))
    assert result is True
```

#### Complex File System Mocking
```python
# Mock directory traversal
def create_mock_file_structure():
    """Create a mock file structure for testing."""
    mock_files = {
        'commands/core/auto.md': """---
name: /auto
description: Auto command
---
# Auto Command""",
        'commands/dev/debug.md': """---
name: /debug
description: Debug command
---
# Debug Command""",
        'components/validation/input.md': '<metadata><name>input-validation</name></metadata>'
    }
    return mock_files

@pytest.fixture
def mock_file_system():
    """Fixture providing mocked file system."""
    mock_files = create_mock_file_structure()
    
    def mock_open_func(file_path, mode='r', **kwargs):
        str_path = str(file_path)
        # Find matching file in mock structure
        for mock_path, content in mock_files.items():
            if mock_path in str_path:
                return mock_open(read_data=content).return_value
        raise FileNotFoundError(f"Mocked file not found: {file_path}")
    
    def mock_glob(pattern):
        """Mock pathlib glob operations."""
        matching_files = []
        for file_path in mock_files.keys():
            if pattern.replace('**/', '') in file_path:
                matching_files.append(Path(file_path))
        return matching_files
    
    with patch('builtins.open', side_effect=mock_open_func), \
         patch('pathlib.Path.glob', side_effect=mock_glob), \
         patch('pathlib.Path.rglob', side_effect=mock_glob), \
         patch('pathlib.Path.exists', return_value=True):
        yield mock_files

def test_complex_file_operations(mock_file_system):
    processor = CommandProcessor()
    commands = processor.discover_commands(Path('/fake/commands'))
    
    assert len(commands) == 2
    assert commands[0]['name'] == '/auto'
    assert commands[1]['name'] == '/debug'
```

### 2. Cryptographic Operations

```python
# Mock encryption operations
@pytest.fixture
def mock_crypto():
    """Mock cryptographic operations."""
    mock_cipher = Mock()
    mock_cipher.encrypt.return_value = b'encrypted_data_123'
    mock_cipher.decrypt.return_value = b'{"api_key": "secret", "name": "test"}'
    
    with patch('cryptography.fernet.Fernet', return_value=mock_cipher), \
         patch('cryptography.fernet.Fernet.generate_key', return_value=b'test_key_32_bytes_long_12345678'), \
         patch('secrets.token_urlsafe', return_value='deterministic_token'):
        yield mock_cipher

def test_api_key_encryption(mock_crypto):
    manager = SecureAPIKeyManager(master_key="test_key")
    
    key_id = manager.encrypt_api_key("test_key", "secret_value")
    
    assert key_id.startswith("key_")
    mock_crypto.encrypt.assert_called_once()
```

### 3. Date/Time Operations

```python
# Mock datetime for deterministic tests
@pytest.fixture
def fixed_datetime():
    """Provide fixed datetime for consistent testing."""
    fixed_time = datetime(2024, 1, 15, 12, 0, 0)
    
    with patch('secure_api_key_manager.datetime') as mock_dt:
        mock_dt.now.return_value = fixed_time
        mock_dt.fromisoformat.side_effect = datetime.fromisoformat
        yield mock_dt

def test_key_expiration_with_fixed_time(fixed_datetime):
    manager = SecureAPIKeyManager()
    
    # Encrypt key (should use fixed time)
    key_id = manager.encrypt_api_key("test", "secret")
    
    # Verify created time
    key_data = manager.decrypt_api_key(key_id)
    assert key_data['created'] == '2024-01-15T12:00:00'
```

### 4. Environment Variables

```python
# Mock environment variables
@pytest.fixture
def mock_environment():
    """Mock environment variables."""
    env_vars = {
        'CLAUDE_MASTER_KEY': 'test_master_key_123',
        'PROJECT_ROOT': '/fake/project/root'
    }
    
    with patch.dict(os.environ, env_vars, clear=True):
        yield env_vars

def test_master_key_from_environment(mock_environment):
    manager = SecureAPIKeyManager()  # Should use env var
    
    # Should not generate new key since env var exists
    assert 'Generated new master key' not in captured_output
```

### 5. Network Operations (for MCP)

```python
# Mock network/MCP operations
@pytest.fixture
def mock_mcp_client():
    """Mock MCP client operations."""
    mock_client = AsyncMock()
    
    # Mock typical MCP responses
    mock_client.list_resources.return_value = [
        {'uri': 'file://cmd1.md', 'name': '/cmd1'},
        {'uri': 'file://cmd2.md', 'name': '/cmd2'}
    ]
    
    mock_client.read_resource.return_value = "command content"
    
    yield mock_client

@pytest.mark.asyncio
async def test_mcp_resource_listing(mock_mcp_client):
    server = ClaudeCodeMCPServer("/fake/project")
    server.client = mock_mcp_client
    
    resources = await server.list_resources()
    
    assert len(resources) == 2
    mock_mcp_client.list_resources.assert_called_once()
```

## Integration with pytest and Our Test Infrastructure

### 1. Custom Fixtures for the Project

```python
# conftest.py - Shared fixtures for the entire project
import pytest
from pathlib import Path
import tempfile
import shutil
from unittest.mock import Mock, patch

@pytest.fixture(scope="session")
def project_root():
    """Get the actual project root for integration tests."""
    return Path(__file__).parent.parent

@pytest.fixture
def temp_project_structure():
    """Create a realistic temporary project structure."""
    temp_dir = Path(tempfile.mkdtemp())
    
    # Create directory structure
    (temp_dir / ".claude" / "commands" / "core").mkdir(parents=True)
    (temp_dir / ".claude" / "commands" / "development").mkdir(parents=True)
    (temp_dir / "claude_prompt_factory" / "components").mkdir(parents=True)
    
    # Create sample files
    sample_command = temp_dir / ".claude" / "commands" / "core" / "test.md"
    sample_command.write_text("""---
name: /test
description: Test command
usage: /test [args]
tools: Read, Write
---

# Test Command
This is a test command.
""")
    
    sample_component = temp_dir / "claude_prompt_factory" / "components" / "test.md"
    sample_component.write_text("""<metadata>
<name>test-component</name>
<description>Test component</description>
</metadata>

# Test Component
This is a test component.
""")
    
    yield temp_dir
    
    # Cleanup
    shutil.rmtree(temp_dir)

@pytest.fixture
def isolated_api_key_manager():
    """Create API key manager with isolated storage."""
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as temp_file:
        manager = SecureAPIKeyManager(
            master_key="test_master_key_for_testing",
            key_store_path=temp_file.name
        )
        yield manager
        
        # Cleanup
        Path(temp_file.name).unlink(missing_ok=True)

@pytest.fixture
def mock_all_external_deps():
    """Mock all external dependencies for unit testing."""
    patches = [
        patch('builtins.open', create=True),
        patch('pathlib.Path.exists', return_value=True),
        patch('os.chmod'),
        patch('secrets.token_urlsafe', return_value='deterministic_token'),
        patch('cryptography.fernet.Fernet.generate_key', return_value=b'x' * 32)
    ]
    
    mocks = {}
    for p in patches:
        mock_obj = p.start()
        mocks[p.attribute] = mock_obj
    
    yield mocks
    
    for p in patches:
        p.stop()
```

### 2. Test Categories and Markers

```python
# pytest.ini
[tool:pytest]
markers =
    unit: Unit tests that don't require external resources
    integration: Integration tests that test component interaction
    slow: Tests that take more than 1 second
    network: Tests that require network access
    filesystem: Tests that require real file system access
    crypto: Tests that use cryptographic operations

# Use markers in tests
@pytest.mark.unit
def test_parse_frontmatter():
    """Unit test - fast, isolated."""
    pass

@pytest.mark.integration
@pytest.mark.filesystem
def test_full_command_discovery():
    """Integration test - uses real file system."""
    pass

@pytest.mark.slow
@pytest.mark.crypto
def test_key_encryption_performance():
    """Performance test with real crypto."""
    pass
```

### 3. Test Running Strategies

```bash
# Run different test categories
pytest -m unit                    # Only unit tests (fast)
pytest -m "not slow"             # Skip slow tests
pytest -m "integration or unit"   # Integration and unit tests
pytest -m "not (network or slow)" # Skip network and slow tests

# Run with different levels of output
pytest -v                        # Verbose output
pytest -s                        # Show print statements
pytest --tb=short                # Short traceback format
pytest --tb=no                   # No traceback

# Coverage with exclusions
pytest --cov=. --cov-exclude="*/tests/*" --cov-report=html

# Run specific test patterns
pytest -k "test_api_key"         # Tests matching pattern
pytest tests/unit/               # Specific directory
pytest tests/unit/test_*.py      # Specific file pattern
```

### 4. Continuous Testing Setup

```python
# scripts/run_tests.py
#!/usr/bin/env python3
"""Continuous testing script for development."""

import subprocess
import sys
from pathlib import Path

def run_fast_tests():
    """Run fast unit tests during development."""
    cmd = [
        "pytest", 
        "-m", "unit",
        "--tb=short",
        "-x",  # Stop on first failure
        "--ff"  # Run failures first
    ]
    return subprocess.run(cmd).returncode

def run_full_test_suite():
    """Run complete test suite for CI/CD."""
    cmd = [
        "pytest",
        "--cov=.",
        "--cov-exclude=*/tests/*",
        "--cov-report=term-missing",
        "--cov-report=html:htmlcov",
        "--junitxml=test-results.xml"
    ]
    return subprocess.run(cmd).returncode

def run_integration_tests():
    """Run integration tests."""
    cmd = [
        "pytest",
        "-m", "integration",
        "-v"
    ]
    return subprocess.run(cmd).returncode

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_type = sys.argv[1]
        if test_type == "fast":
            exit_code = run_fast_tests()
        elif test_type == "full":
            exit_code = run_full_test_suite()
        elif test_type == "integration":
            exit_code = run_integration_tests()
        else:
            print(f"Unknown test type: {test_type}")
            sys.exit(1)
    else:
        exit_code = run_fast_tests()
    
    sys.exit(exit_code)

# Usage:
# python scripts/run_tests.py fast        # Quick feedback during development
# python scripts/run_tests.py full        # Complete test suite
# python scripts/run_tests.py integration # Integration tests only
```

### 5. Pre-commit Hooks for TDD

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: fast-tests
        name: Fast Tests
        entry: python scripts/run_tests.py fast
        language: system
        pass_filenames: false
        stages: [commit]
      
      - id: security-audit
        name: Security Audit
        entry: python scripts/security_audit.py
        language: system
        pass_filenames: false
        stages: [push]
      
      - id: full-tests
        name: Full Test Suite
        entry: python scripts/run_tests.py full
        language: system
        pass_filenames: false
        stages: [push]
```

## TDD Workflow Integration with Development

### 1. Feature Development Workflow

```bash
# 1. Start with failing test
git checkout -b feature/new-command-validator

# Write failing test first
cat > tests/unit/test_command_validator.py << 'EOF'
def test_validate_command_name_rejects_invalid_names():
    validator = CommandValidator()
    
    with pytest.raises(ValueError, match="Command name must start with /"):
        validator.validate_command_name("invalid-name")
EOF

# Run test - should fail
pytest tests/unit/test_command_validator.py::test_validate_command_name_rejects_invalid_names -v

# 2. Write minimal implementation
# ... implement CommandValidator.validate_command_name() ...

# 3. Run test - should pass
pytest tests/unit/test_command_validator.py::test_validate_command_name_rejects_invalid_names -v

# 4. Refactor and add more tests
# ... add more test cases and refine implementation ...

# 5. Commit with tests
git add tests/unit/test_command_validator.py command_validator.py
git commit -m "feat: Add command name validation with TDD"
```

### 2. Bug Fix Workflow

```bash
# 1. Reproduce bug with failing test
cat > tests/unit/test_bug_reproduction.py << 'EOF'
def test_api_key_decryption_handles_expired_keys():
    """Reproduce bug: expired keys should raise clear error."""
    manager = SecureAPIKeyManager()
    
    # Create key that expires immediately
    with patch('datetime.now') as mock_now:
        # Set time to past for creation
        mock_now.return_value = datetime(2024, 1, 1)
        key_id = manager.encrypt_api_key("test", "secret")
        
        # Set time to future for access
        mock_now.return_value = datetime(2024, 12, 31)
        
        with pytest.raises(ValueError, match="API key .* has expired"):
            manager.decrypt_api_key(key_id)
EOF

# Run test - should fail with the bug
pytest tests/unit/test_bug_reproduction.py -v

# 2. Fix the bug
# ... implement proper expiration checking ...

# 3. Test should pass
pytest tests/unit/test_bug_reproduction.py -v

# 4. Run all tests to ensure no regression
pytest

# 5. Commit fix with test
git add .
git commit -m "fix: Handle expired API keys correctly"
```

### 3. Refactoring Workflow

```bash
# 1. Ensure all tests pass before refactoring
pytest

# 2. Run tests continuously during refactoring
pytest --watch  # or use pytest-watch

# 3. Refactor with confidence
# ... make structural changes ...

# 4. Tests should still pass
pytest

# 5. Add any new tests for new structure
# ... write tests for new interfaces ...

# 6. Commit refactoring
git commit -m "refactor: Extract metadata parsing into separate class"
```

## Common TDD Pitfalls and Solutions

### Pitfall 1: Writing Tests After Implementation
```python
# ❌ WRONG: Implementation first
def complex_function():
    # 50 lines of logic
    return result

def test_complex_function():
    # Test written to match existing behavior
    assert complex_function() == expected_result

# ✅ RIGHT: Test first
def test_complex_function_handles_edge_case():
    # Write this test first, watch it fail
    result = complex_function(edge_case_input)
    assert result == expected_edge_case_output

# Then implement complex_function to make the test pass
```

### Pitfall 2: Testing Implementation Details
```python
# ❌ WRONG: Testing internals
def test_api_key_manager_uses_correct_cipher():
    manager = SecureAPIKeyManager()
    manager.encrypt_api_key("test", "secret")
    
    # Testing that it uses Fernet specifically
    assert isinstance(manager.cipher_suite, Fernet)

# ✅ RIGHT: Testing behavior
def test_api_key_manager_encrypts_and_decrypts_correctly():
    manager = SecureAPIKeyManager()
    
    key_id = manager.encrypt_api_key("test", "secret_value")
    decrypted = manager.decrypt_api_key(key_id)
    
    assert decrypted['api_key'] == "secret_value"
```

### Pitfall 3: Overly Complex Test Setup
```python
# ❌ WRONG: Complex, hard-to-understand test
def test_command_processing():
    # 30 lines of setup
    with patch('os.path.exists') as mock_exists, \
         patch('builtins.open', mock_open()) as mock_file, \
         patch('json.loads') as mock_json, \
         patch('cryptography.fernet.Fernet') as mock_fernet, \
         patch('datetime.datetime.now') as mock_now:
        
        # Complex mock configuration
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = "complex data"
        # ... more complex setup ...
        
        # The actual test is lost in the setup
        result = process_command("test")
        assert result == "expected"

# ✅ RIGHT: Clear, focused test with helper
@pytest.fixture
def command_processing_environment():
    """Clear fixture that sets up test environment."""
    return MockCommandEnvironment(
        files={'test.md': 'test content'},
        crypto_key='test_key',
        current_time=datetime(2024, 1, 1)
    )

def test_command_processing_extracts_metadata(command_processing_environment):
    """Clear test name that describes what's being tested."""
    processor = CommandProcessor(command_processing_environment)
    
    result = processor.process_command("test.md")
    
    assert result.name == "/test"
    assert result.description == "Test command"
```

## Summary: TDD Success in This Project

### Key Success Factors

1. **Start Simple**: Begin with the simplest possible test
2. **Mock Thoughtfully**: Mock dependencies, not implementation details
3. **Test Behavior**: Focus on what the code should do, not how it does it
4. **Refactor Safely**: Use tests as a safety net for improvements
5. **Fail Fast**: Write tests that fail quickly and clearly

### Project-Specific Benefits

- **Command Processing**: TDD ensures reliable parsing of various command formats
- **Security Features**: TDD catches encryption/decryption issues early
- **Async Operations**: TDD helps manage complex async state and error handling
- **Integration Points**: TDD validates interactions between components
- **Performance**: TDD enables confident optimization with safety nets

### Measuring TDD Success

```bash
# Code coverage (aim for 80%+ on critical paths)
pytest --cov=. --cov-report=term-missing

# Test execution speed (unit tests should be fast)
pytest --durations=10

# Test reliability (tests should pass consistently)
for i in {1..10}; do pytest -x || break; done

# Code quality metrics
flake8 .
mypy .
```

By following these practical guidelines, TDD becomes a natural part of the development process in the Tallinn project, leading to more reliable, maintainable, and well-tested code.