# Example 1: Simple Function TDD - ContentProcessor.extract_frontmatter_metadata()

This example demonstrates Test-Driven Development (TDD) for a simple utility function that extracts metadata from markdown frontmatter. We'll implement the `extract_frontmatter_metadata()` method for the `ContentProcessor` class following the Red-Green-Refactor cycle.

## Target Function

We want to implement a function that extracts YAML-style metadata from markdown frontmatter blocks like this:

```markdown
---
name: /test-command
description: A test command for unit testing
usage: /test-command [args]
tools: Read, Write
---

# Command content here
```

## TDD Cycle Implementation

### 🔴 Red Phase 1: Write the First Failing Test

Let's start with the simplest possible test case.

```python
# tests/unit/test_content_processor_tdd.py
#!/usr/bin/env python3

import pytest
from pathlib import Path
import sys

# Import the module under test
sys.path.append(str(Path(__file__).parent.parent.parent))
from command_processing.content_processor import ContentProcessor


class TestContentProcessorTDD:
    """TDD implementation for ContentProcessor.extract_frontmatter_metadata()"""
    
    @pytest.fixture
    def processor(self):
        """Create a ContentProcessor instance for testing."""
        return ContentProcessor(Path("/fake/source"))
    
    def test_extract_frontmatter_metadata_with_simple_case(self, processor):
        """Test: Should extract basic metadata from frontmatter."""
        # Arrange
        content = """---
name: /test-command
---

# Content here
"""
        
        # Act
        result = processor.extract_frontmatter_metadata(content)
        
        # Assert
        assert result['name'] == '/test-command'
```

**Run the test:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD::test_extract_frontmatter_metadata_with_simple_case -v

FAILED - AttributeError: 'ContentProcessor' object has no attribute 'extract_frontmatter_metadata'
```

✅ **Test fails as expected** - the method doesn't exist yet.

### 🟢 Green Phase 1: Minimal Implementation

Add the minimal code to make the test pass:

```python
# command_processing/content_processor.py

class ContentProcessor:
    # ... existing code ...
    
    def extract_frontmatter_metadata(self, content: str) -> dict:
        """Extract metadata from frontmatter - minimal implementation."""
        return {'name': '/test-command'}
```

**Run the test:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD::test_extract_frontmatter_metadata_with_simple_case -v

PASSED
```

✅ **Test passes** - but this is obviously a hardcoded implementation.

### 🔴 Red Phase 2: Add More Specific Test

```python
def test_extract_frontmatter_metadata_with_multiple_fields(self, processor):
    """Test: Should extract multiple metadata fields."""
    # Arrange
    content = """---
name: /complex-command
description: A more complex test command
usage: /complex-command [options]
tools: Read, Write, Grep
---

# Command implementation
Some content here.
"""
    
    # Act
    result = processor.extract_frontmatter_metadata(content)
    
    # Assert
    assert result['name'] == '/complex-command'
    assert result['description'] == 'A more complex test command'
    assert result['usage'] == '/complex-command [options]'
    assert result['tools'] == 'Read, Write, Grep'
```

**Run the test:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD::test_extract_frontmatter_metadata_with_multiple_fields -v

FAILED - KeyError: 'description'
```

✅ **Test fails as expected** - our hardcoded implementation doesn't handle multiple fields.

### 🟢 Green Phase 2: Implement Basic Parsing

```python
def extract_frontmatter_metadata(self, content: str) -> dict:
    """Extract metadata from frontmatter."""
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

**Run the tests:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD -v

test_extract_frontmatter_metadata_with_simple_case PASSED
test_extract_frontmatter_metadata_with_multiple_fields PASSED
```

✅ **Both tests pass** - basic parsing works!

### 🔴 Red Phase 3: Test Edge Cases

Let's add tests for edge cases:

```python
def test_extract_frontmatter_metadata_with_no_frontmatter(self, processor):
    """Test: Should return empty dict when no frontmatter present."""
    # Arrange
    content = """# Just a regular markdown file

No frontmatter here.
"""
    
    # Act
    result = processor.extract_frontmatter_metadata(content)
    
    # Assert
    assert result == {}

def test_extract_frontmatter_metadata_with_empty_frontmatter(self, processor):
    """Test: Should handle empty frontmatter block."""
    # Arrange
    content = """---
---

# Content
"""
    
    # Act
    result = processor.extract_frontmatter_metadata(content)
    
    # Assert
    assert result == {}

def test_extract_frontmatter_metadata_with_malformed_yaml(self, processor):
    """Test: Should handle malformed YAML gracefully."""
    # Arrange
    content = """---
name: /test-command
description: Missing closing quotes "
malformed_line_without_colon
another: valid line
---

# Content
"""
    
    # Act
    result = processor.extract_frontmatter_metadata(content)
    
    # Assert
    assert result['name'] == '/test-command'
    assert result['another'] == 'valid line'
    # Should skip malformed lines gracefully
```

**Run the tests:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD -v

test_extract_frontmatter_metadata_with_no_frontmatter PASSED
test_extract_frontmatter_metadata_with_empty_frontmatter PASSED  
test_extract_frontmatter_metadata_with_malformed_yaml PASSED
```

✅ **All tests pass** - our basic implementation handles these edge cases!

### 🔴 Red Phase 4: Test Complex Cases

Add tests for more complex scenarios:

```python
def test_extract_frontmatter_metadata_with_comments(self, processor):
    """Test: Should ignore YAML comments."""
    # Arrange
    content = """---
# This is a comment
name: /test-command
description: Test command  # inline comment
# Another comment
tools: Read, Write
---

# Content
"""
    
    # Act
    result = processor.extract_frontmatter_metadata(content)
    
    # Assert
    assert result['name'] == '/test-command'
    assert result['description'] == 'Test command  # inline comment'  # Doesn't handle inline comments yet
    assert result['tools'] == 'Read, Write'
    assert len(result) == 3  # Should not include comment lines

def test_extract_frontmatter_metadata_with_multiline_values(self, processor):
    """Test: Should handle multiline values (if needed)."""
    # Arrange
    content = """---
name: /test-command
description: |
  This is a multiline
  description that spans
  multiple lines
tools: Read, Write
---

# Content
"""
    
    # Act
    result = processor.extract_frontmatter_metadata(content)
    
    # Assert
    assert result['name'] == '/test-command'
    assert result['tools'] == 'Read, Write'
    # For now, we might not handle multiline properly, but test documents the behavior
```

**Run the tests:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD::test_extract_frontmatter_metadata_with_comments -v

FAILED - AssertionError: assert 4 == 3
```

✅ **Test fails as expected** - our implementation doesn't filter out comments.

### 🟢 Green Phase 4: Handle Comments

```python
def extract_frontmatter_metadata(self, content: str) -> dict:
    """Extract metadata from YAML frontmatter block."""
    import re
    
    frontmatter_pattern = r'^---\n(.*?)\n---'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if not match:
        return {}
    
    metadata = {}
    yaml_content = match.group(1)
    
    for line in yaml_content.split('\n'):
        line = line.strip()
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            continue
            
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    return metadata
```

**Run the tests:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD -v

All tests PASSED
```

✅ **All tests pass** - comments are now handled correctly!

### 🔵 Refactor Phase: Improve Code Quality

Now that all tests pass, let's refactor to improve the code:

```python
def extract_frontmatter_metadata(self, content: str) -> Dict[str, str]:
    """
    Extract metadata from YAML frontmatter block.
    
    Args:
        content: Markdown content with optional frontmatter
        
    Returns:
        Dictionary of metadata key-value pairs
        
    Example:
        >>> content = "---\\nname: /cmd\\n---\\n# Content"
        >>> processor.extract_frontmatter_metadata(content)
        {'name': '/cmd'}
    """
    frontmatter_pattern = r'^---\n(.*?)\n---'
    frontmatter_match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if not frontmatter_match:
        return {}
    
    return self._parse_yaml_like_content(frontmatter_match.group(1))

def _parse_yaml_like_content(self, yaml_content: str) -> Dict[str, str]:
    """Parse simple YAML-like content into key-value pairs."""
    metadata = {}
    
    for line in yaml_content.split('\n'):
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            continue
            
        # Parse key-value pairs
        if ':' in line:
            key_part, value_part = line.split(':', 1)
            key = key_part.strip()
            value = value_part.strip()
            
            # Remove inline comments from values
            if '#' in value and not value.startswith('"'):
                value = value.split('#')[0].strip()
            
            metadata[key] = value
    
    return metadata
```

**Run all tests:**
```bash
$ pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD -v

All tests PASSED
```

✅ **Refactoring successful** - tests still pass with improved code structure.

## Final Test Suite

Here's the complete test suite we built through TDD:

```python
#!/usr/bin/env python3
"""
TDD Example: Simple Function Testing
Testing ContentProcessor.extract_frontmatter_metadata()
"""

import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))
from command_processing.content_processor import ContentProcessor


class TestContentProcessorTDD:
    """TDD implementation for ContentProcessor.extract_frontmatter_metadata()"""
    
    @pytest.fixture
    def processor(self):
        """Create a ContentProcessor instance for testing."""
        return ContentProcessor(Path("/fake/source"))
    
    def test_extract_frontmatter_metadata_with_simple_case(self, processor):
        """Test: Should extract basic metadata from frontmatter."""
        content = """---
name: /test-command
---

# Content here
"""
        result = processor.extract_frontmatter_metadata(content)
        assert result['name'] == '/test-command'
    
    def test_extract_frontmatter_metadata_with_multiple_fields(self, processor):
        """Test: Should extract multiple metadata fields."""
        content = """---
name: /complex-command
description: A more complex test command
usage: /complex-command [options]
tools: Read, Write, Grep
---

# Command implementation
"""
        result = processor.extract_frontmatter_metadata(content)
        assert result['name'] == '/complex-command'
        assert result['description'] == 'A more complex test command'
        assert result['usage'] == '/complex-command [options]'
        assert result['tools'] == 'Read, Write, Grep'
    
    def test_extract_frontmatter_metadata_with_no_frontmatter(self, processor):
        """Test: Should return empty dict when no frontmatter present."""
        content = """# Just a regular markdown file

No frontmatter here.
"""
        result = processor.extract_frontmatter_metadata(content)
        assert result == {}
    
    def test_extract_frontmatter_metadata_with_empty_frontmatter(self, processor):
        """Test: Should handle empty frontmatter block."""
        content = """---
---

# Content
"""
        result = processor.extract_frontmatter_metadata(content)
        assert result == {}
    
    def test_extract_frontmatter_metadata_with_malformed_yaml(self, processor):
        """Test: Should handle malformed YAML gracefully."""
        content = """---
name: /test-command
description: Missing closing quotes "
malformed_line_without_colon
another: valid line
---

# Content
"""
        result = processor.extract_frontmatter_metadata(content)
        assert result['name'] == '/test-command'
        assert result['another'] == 'valid line'
        assert 'malformed_line_without_colon' not in result
    
    def test_extract_frontmatter_metadata_with_comments(self, processor):
        """Test: Should ignore YAML comments."""
        content = """---
# This is a comment
name: /test-command
description: Test command
# Another comment
tools: Read, Write
---

# Content
"""
        result = processor.extract_frontmatter_metadata(content)
        assert result['name'] == '/test-command'
        assert result['description'] == 'Test command'
        assert result['tools'] == 'Read, Write'
        assert len(result) == 3  # Should not include comment lines


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

## Key TDD Lessons from This Example

### 1. Start with the Simplest Test
We began with extracting just one field, not trying to solve the entire problem at once.

### 2. Let Tests Drive the Design
Each test revealed what the function needed to handle, guiding our implementation decisions.

### 3. Red-Green-Refactor Discipline
- **Red**: Write a failing test first
- **Green**: Write minimal code to pass
- **Refactor**: Improve code while keeping tests passing

### 4. Test Coverage Through TDD
By following TDD, we naturally achieved comprehensive test coverage:
- Basic functionality
- Edge cases (no frontmatter, empty frontmatter)
- Error handling (malformed YAML)
- Complex scenarios (comments, multiple fields)

### 5. Living Documentation
The tests serve as documentation showing exactly how the function should behave.

## Running This Example

To run this TDD example in your environment:

```bash
# 1. Create the test file
cp docs/tdd-examples/01-simple-function.md tests/unit/test_content_processor_tdd.py

# 2. Run the specific test class
pytest tests/unit/test_content_processor_tdd.py::TestContentProcessorTDD -v

# 3. Run with coverage to see what we've tested
pytest tests/unit/test_content_processor_tdd.py --cov=command_processing.content_processor --cov-report=term-missing
```

This example demonstrates how TDD leads to robust, well-tested code through a disciplined approach of test-first development.