# Edge Cases Handling Guide

*Version: 1.0.0*
*Purpose: Practical patterns for handling real-world edge cases*
*Philosophy: Expect the unexpected, handle it gracefully*

## 🎯 Core Principle

Every edge case should be:
1. **Detected** early
2. **Handled** gracefully  
3. **Reported** clearly
4. **Recoverable** when possible

## 📝 Input Edge Cases

### Empty and Whitespace Input
```python
def handle_empty_input(user_input: str) -> str:
    """Handle various forms of 'empty' input."""
    
    # Case 1: None
    if user_input is None:
        raise ValueError("Input cannot be None. Please provide a value.")
    
    # Case 2: Empty string
    if user_input == "":
        raise ValueError("Input cannot be empty. Please provide a value.")
    
    # Case 3: Only whitespace
    if user_input.strip() == "":
        raise ValueError("Input cannot be only whitespace. Please provide actual content.")
    
    # Case 4: Only special whitespace (tabs, newlines)
    if user_input.replace('\t', '').replace('\n', '').replace('\r', '').strip() == "":
        raise ValueError("Input contains only whitespace characters. Please provide actual content.")
    
    # Return cleaned input
    return user_input.strip()
```

### Unicode and Special Characters
```python
import unicodedata
import re

def handle_unicode_input(user_input: str) -> str:
    """Safely handle Unicode and special characters."""
    
    # Normalize Unicode (handles different representations of same character)
    normalized = unicodedata.normalize('NFKC', user_input)
    
    # Handle zero-width characters (often invisible)
    zero_width_chars = ['\u200b', '\u200c', '\u200d', '\ufeff']
    for char in zero_width_chars:
        normalized = normalized.replace(char, '')
    
    # Handle emoji in code contexts
    if any(ord(char) > 127 for char in normalized):
        # Check if it's in a code block
        if '```' in normalized or 'def ' in normalized or 'function ' in normalized:
            logger.warning("Unicode characters detected in code context")
            # Optionally strip or warn
    
    # Handle RTL/LTR markers
    normalized = normalized.replace('\u200e', '').replace('\u200f', '')
    
    # Validate result isn't empty after cleaning
    if not normalized.strip():
        raise ValueError("Input became empty after Unicode normalization")
    
    return normalized
```

### Extremely Large Input
```python
def handle_large_input(user_input: str, max_size: int = 100000) -> str:
    """Handle inputs that might overflow buffers or context windows."""
    
    input_size = len(user_input)
    
    # Check absolute size
    if input_size > max_size:
        raise ValueError(
            f"Input too large: {input_size:,} characters (max: {max_size:,}). "
            f"Consider splitting into smaller chunks."
        )
    
    # Check token estimate (rough: 1 token ≈ 4 chars)
    estimated_tokens = input_size // 4
    if estimated_tokens > 20000:  # Leave room in context
        logger.warning(
            f"Input may consume {estimated_tokens:,} tokens. "
            f"This could limit available context for processing."
        )
    
    # Check line count (might indicate generated content)
    line_count = user_input.count('\n')
    if line_count > 10000:
        raise ValueError(
            f"Input has {line_count:,} lines. This might be generated content. "
            f"Please provide focused input."
        )
    
    return user_input
```

## 📁 File System Edge Cases

### Path Traversal and Security
```python
from pathlib import Path
import os

def handle_file_path_securely(file_path: str) -> Path:
    """Handle various path edge cases and security issues."""
    
    # Case 1: Path traversal attempts
    if '..' in file_path:
        raise ValueError("Path traversal (..) not allowed")
    
    # Case 2: Absolute paths
    if os.path.isabs(file_path):
        raise ValueError("Absolute paths not allowed. Use relative paths from project root.")
    
    # Case 3: Hidden files (might be unintentional)
    path = Path(file_path)
    if any(part.startswith('.') for part in path.parts):
        logger.warning(f"Accessing hidden file/directory: {file_path}")
    
    # Case 4: Symbolic links (security risk)
    if path.exists() and path.is_symlink():
        raise ValueError("Symbolic links not allowed for security reasons")
    
    # Case 5: Special file names
    dangerous_names = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'LPT1']  # Windows reserved
    if path.stem.upper() in dangerous_names:
        raise ValueError(f"Reserved filename not allowed: {path.stem}")
    
    # Case 6: Non-ASCII in paths
    try:
        file_path.encode('ascii')
    except UnicodeEncodeError:
        logger.warning("Non-ASCII characters in path. May cause issues on some systems.")
    
    # Resolve and validate within project
    resolved = path.resolve()
    project_root = Path.cwd()
    try:
        resolved.relative_to(project_root)
    except ValueError:
        raise ValueError(f"Path must be within project directory: {project_root}")
    
    return resolved
```

### File State Edge Cases
```python
def handle_file_operations(file_path: Path, operation: str = 'read') -> Any:
    """Handle edge cases during file operations."""
    
    # Case 1: File doesn't exist (for read)
    if operation == 'read' and not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}\n"
            f"Hint: Check if the path is correct or if the file was moved/deleted"
        )
    
    # Case 2: Directory instead of file
    if file_path.exists() and file_path.is_dir():
        raise ValueError(f"Expected file but found directory: {file_path}")
    
    # Case 3: No read permissions
    if operation == 'read' and file_path.exists() and not os.access(file_path, os.R_OK):
        raise PermissionError(f"No read permission for file: {file_path}")
    
    # Case 4: No write permissions (for write)
    if operation == 'write':
        # Check parent directory permissions
        parent = file_path.parent
        if not parent.exists():
            raise ValueError(f"Parent directory doesn't exist: {parent}")
        if not os.access(parent, os.W_OK):
            raise PermissionError(f"No write permission in directory: {parent}")
    
    # Case 5: File is locked (Windows)
    if operation == 'write' and file_path.exists():
        try:
            # Try to open for append (less intrusive than write)
            with open(file_path, 'a'):
                pass
        except IOError:
            raise IOError(f"File appears to be locked: {file_path}")
    
    # Case 6: Disk space (for write)
    if operation == 'write':
        # Get free space
        stat = os.statvfs(file_path.parent)
        free_bytes = stat.f_frsize * stat.f_bavail
        if free_bytes < 10 * 1024 * 1024:  # Less than 10MB
            raise IOError(f"Low disk space: only {free_bytes // 1024 // 1024}MB free")
```

## 🔄 Concurrency Edge Cases

### Race Conditions
```python
import fcntl
import time
from contextlib import contextmanager

@contextmanager
def file_lock(file_path: Path, timeout: float = 5.0):
    """Handle file locking to prevent race conditions."""
    
    lock_path = Path(str(file_path) + '.lock')
    lock_file = None
    start_time = time.time()
    
    try:
        # Try to acquire lock
        while True:
            try:
                lock_file = open(lock_path, 'x')  # Exclusive create
                break
            except FileExistsError:
                # Check timeout
                if time.time() - start_time > timeout:
                    raise TimeoutError(
                        f"Could not acquire lock for {file_path} after {timeout}s. "
                        f"Another process may be using it."
                    )
                time.sleep(0.1)
        
        yield
        
    finally:
        # Release lock
        if lock_file:
            lock_file.close()
            lock_path.unlink(missing_ok=True)
```

### Parallel Execution Issues
```python
import threading
from typing import Dict, Any

class ThreadSafeOperations:
    """Handle edge cases in multi-threaded environments."""
    
    def __init__(self):
        self._lock = threading.Lock()
        self._data: Dict[str, Any] = {}
    
    def update_safely(self, key: str, value: Any) -> None:
        """Thread-safe update operation."""
        
        with self._lock:
            # Case 1: Concurrent modifications
            old_value = self._data.get(key)
            if old_value is not None:
                logger.warning(f"Overwriting existing value for {key}")
            
            # Case 2: Memory pressure
            if len(self._data) > 10000:
                logger.warning("Large number of keys in storage. Consider cleanup.")
            
            self._data[key] = value
    
    def get_safely(self, key: str, default: Any = None) -> Any:
        """Thread-safe read operation."""
        
        with self._lock:
            return self._data.get(key, default)
```

## 🌐 Network Edge Cases

### API Call Failures
```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def make_resilient_request(url: str, **kwargs) -> requests.Response:
    """Handle various network edge cases."""
    
    # Create session with retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    # Set reasonable timeout
    kwargs.setdefault('timeout', (5, 30))  # (connect, read)
    
    try:
        response = session.request('GET', url, **kwargs)
        
        # Case 1: Empty response
        if not response.content:
            raise ValueError("Received empty response from server")
        
        # Case 2: Unexpected content type
        content_type = response.headers.get('content-type', '')
        if 'application/json' in kwargs.get('headers', {}).get('Accept', ''):
            if 'json' not in content_type:
                logger.warning(f"Expected JSON but got: {content_type}")
        
        # Case 3: Large response
        content_length = len(response.content)
        if content_length > 10 * 1024 * 1024:  # 10MB
            logger.warning(f"Large response: {content_length // 1024 // 1024}MB")
        
        return response
        
    except requests.exceptions.ConnectTimeout:
        raise TimeoutError(f"Connection timeout to {url}. Check network connectivity.")
    except requests.exceptions.ReadTimeout:
        raise TimeoutError(f"Read timeout from {url}. Server may be slow.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError(f"Could not connect to {url}. Check if service is running.")
```

## 🧮 Computation Edge Cases

### Numeric Edge Cases
```python
import math
from decimal import Decimal, InvalidOperation

def handle_numeric_input(value: Any) -> float:
    """Handle various numeric edge cases."""
    
    # Case 1: None or empty
    if value is None or value == "":
        raise ValueError("Numeric value cannot be empty")
    
    # Case 2: String representation
    if isinstance(value, str):
        value = value.strip()
        
        # Scientific notation
        if 'e' in value.lower():
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Invalid scientific notation: {value}")
        
        # Percentage
        if value.endswith('%'):
            try:
                return float(value[:-1]) / 100
            except ValueError:
                raise ValueError(f"Invalid percentage: {value}")
    
    # Case 3: Special float values
    try:
        num = float(value)
        
        if math.isnan(num):
            raise ValueError("NaN (Not a Number) values not allowed")
        
        if math.isinf(num):
            raise ValueError("Infinite values not allowed")
        
        # Case 4: Precision issues
        if abs(num) > 1e308:
            raise ValueError(f"Number too large: {num}")
        
        if 0 < abs(num) < 1e-308:
            raise ValueError(f"Number too small (would underflow): {num}")
        
        return num
        
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid numeric value: {value}") from e
```

## 🎭 State Edge Cases

### Session State Corruption
```python
def validate_session_state(state: Dict[str, Any]) -> Dict[str, Any]:
    """Handle corrupted or invalid session state."""
    
    # Case 1: Not a dictionary
    if not isinstance(state, dict):
        logger.error(f"Invalid state type: {type(state)}")
        return {}  # Return empty state rather than crash
    
    # Case 2: Missing required fields
    required_fields = ['session_id', 'created_at']
    for field in required_fields:
        if field not in state:
            logger.warning(f"Missing required field: {field}")
            # Attempt recovery
            if field == 'session_id':
                state['session_id'] = 'recovered_' + str(time.time())
            elif field == 'created_at':
                state['created_at'] = datetime.now().isoformat()
    
    # Case 3: Invalid data types
    if 'data' in state and not isinstance(state['data'], dict):
        logger.warning("Invalid data field, resetting")
        state['data'] = {}
    
    # Case 4: Circular references
    try:
        json.dumps(state)  # Will fail if circular
    except (TypeError, ValueError):
        logger.error("Circular reference in state, clearing data")
        state['data'] = {}
    
    return state
```

## 📊 Quick Reference: Edge Case Patterns

### Input Validation Checklist
- [ ] Handle None
- [ ] Handle empty string
- [ ] Handle whitespace-only
- [ ] Handle Unicode/emoji
- [ ] Handle too large input
- [ ] Handle malicious input

### File Operation Checklist
- [ ] Check file exists
- [ ] Check permissions
- [ ] Handle locked files
- [ ] Check disk space
- [ ] Validate paths
- [ ] Handle symlinks

### Network Operation Checklist
- [ ] Set timeouts
- [ ] Handle connection errors
- [ ] Retry on failure
- [ ] Validate responses
- [ ] Handle large responses
- [ ] Check content types

### State Management Checklist
- [ ] Validate structure
- [ ] Handle corruption
- [ ] Check circular refs
- [ ] Handle concurrent access
- [ ] Validate data types
- [ ] Provide recovery

## 💡 Golden Rules

1. **Never assume** - Always validate
2. **Fail gracefully** - Provide helpful error messages
3. **Log warnings** - Help diagnose issues
4. **Provide recovery** - When possible
5. **Test edge cases** - They will happen

---

Remember: Edge cases aren't edge cases - they're Tuesday.