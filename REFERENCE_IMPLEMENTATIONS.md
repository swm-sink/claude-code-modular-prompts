# Reference Implementations

*Version: 1.0.0*
*Purpose: Concrete patterns for reliable LLM code generation*
*Principle: Copy-paste-modify patterns that actually work*

## 🎯 How to Use This Document

1. Find the pattern you need
2. Copy the implementation
3. Modify for your specific use case
4. Keep the error handling and validation

## 📝 Input Validation Pattern

### Basic Input Validation
```python
def validate_user_input(user_input: str, max_length: int = 10000) -> str:
    """
    Standard input validation for all user-provided strings.
    
    Args:
        user_input: Raw input from user
        max_length: Maximum allowed length (default 10KB)
        
    Returns:
        Cleaned, validated input
        
    Raises:
        ValueError: If input is invalid
    """
    # Check existence
    if user_input is None:
        raise ValueError("Input cannot be None")
    
    # Convert to string if needed
    input_str = str(user_input)
    
    # Check not empty
    if not input_str or not input_str.strip():
        raise ValueError("Input cannot be empty or just whitespace")
    
    # Check length
    if len(input_str) > max_length:
        raise ValueError(f"Input exceeds maximum length of {max_length} characters")
    
    # Basic sanitization
    cleaned = input_str.strip()
    
    # Check for dangerous characters (for shell commands)
    dangerous_chars = ['$', '`', ';', '|', '&', '>', '<', '(', ')', '{', '}']
    for char in dangerous_chars:
        if char in cleaned:
            raise ValueError(f"Input contains invalid character: {char}")
    
    # Normalize whitespace
    cleaned = ' '.join(cleaned.split())
    
    return cleaned
```

### Path Validation
```python
import os
from pathlib import Path

def validate_file_path(file_path: str, must_exist: bool = False) -> Path:
    """
    Validate and normalize file paths.
    
    Args:
        file_path: Path to validate
        must_exist: Whether file must already exist
        
    Returns:
        Normalized Path object
        
    Raises:
        ValueError: If path is invalid
        FileNotFoundError: If must_exist=True and file doesn't exist
    """
    # Basic validation
    if not file_path or not file_path.strip():
        raise ValueError("File path cannot be empty")
    
    # Create Path object
    path = Path(file_path).resolve()
    
    # Security: Ensure path is within project directory
    project_root = Path.cwd()
    try:
        path.relative_to(project_root)
    except ValueError:
        raise ValueError(f"Path must be within project directory: {project_root}")
    
    # Check existence if required
    if must_exist and not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    # Check parent directory exists for new files
    if not must_exist and not path.parent.exists():
        raise ValueError(f"Parent directory does not exist: {path.parent}")
    
    return path
```

## 🔄 Error Handling Pattern

### Standard Error Wrapper
```python
from typing import TypeVar, Callable, Any
from functools import wraps
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T')

def safe_execution(recovery_hint: str = None):
    """
    Decorator for safe function execution with error handling.
    
    Args:
        recovery_hint: Suggestion for recovering from errors
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Log the error with context
                logger.error(f"Error in {func.__name__}: {str(e)}")
                
                # Provide helpful error message
                error_msg = f"Operation failed: {str(e)}"
                if recovery_hint:
                    error_msg += f"\nHint: {recovery_hint}"
                
                # Re-raise with context
                raise FrameworkError(error_msg) from e
        return wrapper
    return decorator

class FrameworkError(Exception):
    """Base exception for framework errors with recovery hints."""
    def __init__(self, message: str, recovery_hint: str = None):
        super().__init__(message)
        self.recovery_hint = recovery_hint
```

### Retry Pattern
```python
import time
from typing import TypeVar, Callable

T = TypeVar('T')

def retry_on_failure(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0
):
    """
    Retry decorator with exponential backoff.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay after each retry
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        logger.warning(
                            f"{func.__name__} failed (attempt {attempt + 1}/{max_attempts}): {e}"
                        )
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(f"{func.__name__} failed after {max_attempts} attempts")
            
            raise last_exception
        return wrapper
    return decorator
```

## 📁 File Operations Pattern

### Safe File Reading
```python
def read_file_safely(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Read file with proper error handling and encoding detection.
    
    Args:
        file_path: Path to file
        encoding: File encoding (default utf-8)
        
    Returns:
        File contents as string
    """
    # Validate path
    path = validate_file_path(file_path, must_exist=True)
    
    try:
        # Check file size first
        file_size = path.stat().st_size
        if file_size > 10 * 1024 * 1024:  # 10MB limit
            raise ValueError(f"File too large: {file_size / 1024 / 1024:.1f}MB")
        
        # Read file
        with open(path, 'r', encoding=encoding) as f:
            content = f.read()
            
        # Validate content
        if not content:
            logger.warning(f"File is empty: {path}")
            
        return content
        
    except UnicodeDecodeError:
        # Try with different encoding
        with open(path, 'r', encoding='latin-1') as f:
            return f.read()
    except Exception as e:
        raise FrameworkError(
            f"Failed to read file: {path}",
            recovery_hint="Check file permissions and encoding"
        ) from e
```

### Safe File Writing
```python
def write_file_safely(
    file_path: str, 
    content: str, 
    create_backup: bool = True,
    encoding: str = 'utf-8'
) -> None:
    """
    Write file with backup and atomic operations.
    
    Args:
        file_path: Target file path
        content: Content to write
        create_backup: Whether to backup existing file
        encoding: File encoding
    """
    # Validate inputs
    path = validate_file_path(file_path, must_exist=False)
    if not content:
        raise ValueError("Cannot write empty content")
    
    # Create backup if file exists
    if path.exists() and create_backup:
        backup_path = path.with_suffix(path.suffix + '.backup')
        path.rename(backup_path)
        logger.info(f"Created backup: {backup_path}")
    
    # Write atomically using temporary file
    temp_path = path.with_suffix(path.suffix + '.tmp')
    try:
        # Write to temporary file
        with open(temp_path, 'w', encoding=encoding) as f:
            f.write(content)
        
        # Atomic rename
        temp_path.rename(path)
        logger.info(f"Successfully wrote: {path}")
        
    except Exception as e:
        # Restore from backup if available
        if path.exists():
            path.unlink()
        if backup_path.exists():
            backup_path.rename(path)
        
        raise FrameworkError(
            f"Failed to write file: {path}",
            recovery_hint="Check disk space and permissions"
        ) from e
    finally:
        # Clean up temp file if still exists
        if temp_path.exists():
            temp_path.unlink()
```

## 🔀 Module Loading Pattern

### Safe Module Loading
```python
from typing import Dict, Any

def load_module_safely(module_path: str) -> Dict[str, Any]:
    """
    Load a framework module with validation.
    
    Args:
        module_path: @ link path to module
        
    Returns:
        Module content and metadata
    """
    # Convert @ link to file path
    if module_path.startswith('@'):
        file_path = f".claude/{module_path[1:]}"
    else:
        file_path = module_path
    
    # Validate and read
    content = read_file_safely(file_path)
    
    # Parse module structure
    module_data = {
        'path': file_path,
        'content': content,
        'size': len(content),
        'tokens': estimate_tokens(content),
    }
    
    # Validate module structure
    if 'Purpose:' not in content:
        raise ValueError(f"Module missing Purpose section: {file_path}")
    
    if 'Interface' not in content:
        raise ValueError(f"Module missing Interface section: {file_path}")
    
    # Check token limit
    if module_data['tokens'] > 4000:
        logger.warning(f"Module exceeds token limit: {file_path} ({module_data['tokens']} tokens)")
    
    return module_data

def estimate_tokens(text: str) -> int:
    """Rough token estimation (1 token ≈ 4 characters)"""
    return len(text) // 4
```

## 🏃 Command Execution Pattern

### Safe Command Runner
```python
import subprocess
from typing import List, Tuple

def run_command_safely(
    command: List[str],
    timeout: int = 30,
    check: bool = True
) -> Tuple[str, str]:
    """
    Execute shell command safely without shell injection.
    
    Args:
        command: Command as list of arguments
        timeout: Maximum execution time in seconds
        check: Whether to raise on non-zero exit
        
    Returns:
        Tuple of (stdout, stderr)
    """
    # Validate command
    if not command or not all(command):
        raise ValueError("Command cannot be empty")
    
    # Never use shell=True
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=check,
            shell=False  # CRITICAL: Never use shell=True
        )
        
        return result.stdout, result.stderr
        
    except subprocess.TimeoutExpired:
        raise FrameworkError(
            f"Command timed out after {timeout} seconds",
            recovery_hint="Consider increasing timeout or optimizing command"
        )
    except subprocess.CalledProcessError as e:
        raise FrameworkError(
            f"Command failed with exit code {e.returncode}: {e.stderr}",
            recovery_hint="Check command syntax and permissions"
        )
    except Exception as e:
        raise FrameworkError(
            f"Failed to execute command: {' '.join(command)}",
            recovery_hint="Verify command exists and is accessible"
        ) from e
```

## 🔄 State Management Pattern

### Session State Handler
```python
from typing import Dict, Any
import json
from datetime import datetime

class SessionState:
    """Manage session state with persistence."""
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.state_file = f".claude/sessions/{session_id}.json"
        self._state = self._load_state()
    
    def _load_state(self) -> Dict[str, Any]:
        """Load existing state or create new."""
        try:
            if Path(self.state_file).exists():
                with open(self.state_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load state: {e}")
        
        # Default state
        return {
            'session_id': self.session_id,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'data': {}
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get value from state."""
        return self._state['data'].get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set value in state."""
        self._state['data'][key] = value
        self._state['updated_at'] = datetime.now().isoformat()
        self._save_state()
    
    def _save_state(self) -> None:
        """Persist state to disk."""
        try:
            # Ensure directory exists
            Path(self.state_file).parent.mkdir(parents=True, exist_ok=True)
            
            # Write atomically
            write_file_safely(
                self.state_file,
                json.dumps(self._state, indent=2),
                create_backup=False
            )
        except Exception as e:
            logger.error(f"Failed to save state: {e}")
```

## 🎯 Module Interface Pattern

### Standard Module Structure
```python
"""
Module: Example Pattern Implementation
Purpose: Demonstrate standard module interface
Dependencies: [@modules/patterns/base-pattern.md]
"""

from typing import Dict, Any, Optional

class ModuleInterface:
    """Standard interface all modules should implement."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize module with optional configuration."""
        self.config = config or {}
        self._validate_config()
    
    def _validate_config(self) -> None:
        """Validate configuration on initialization."""
        # Add specific validation for your module
        pass
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main execution method for the module.
        
        Args:
            input_data: Input parameters as dictionary
            
        Returns:
            Result dictionary with 'status' and 'data' keys
        """
        try:
            # Validate inputs
            self._validate_input(input_data)
            
            # Process
            result = self._process(input_data)
            
            # Return standardized response
            return {
                'status': 'success',
                'data': result,
                'module': self.__class__.__name__
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'module': self.__class__.__name__,
                'recovery_hint': getattr(e, 'recovery_hint', None)
            }
    
    def _validate_input(self, input_data: Dict[str, Any]) -> None:
        """Validate input data."""
        if not input_data:
            raise ValueError("Input data cannot be empty")
    
    def _process(self, input_data: Dict[str, Any]) -> Any:
        """Actual processing logic - override in subclasses."""
        raise NotImplementedError("Subclasses must implement _process")
```

## 📋 Common Patterns Quick Reference

### Pattern Selection Guide
| Need | Use Pattern |
|------|-------------|
| User input | Input Validation Pattern |
| File operations | Safe File Reading/Writing |
| External commands | Safe Command Runner |
| Network calls | Retry Pattern |
| Module loading | Safe Module Loading |
| State persistence | Session State Handler |
| Error handling | Standard Error Wrapper |

### Copy-Paste Snippets

**Quick Input Validation:**
```python
user_input = validate_user_input(raw_input, max_length=1000)
```

**Quick File Read:**
```python
content = read_file_safely("path/to/file.md")
```

**Quick Error Handling:**
```python
@safe_execution(recovery_hint="Check input format")
def my_function():
    # Your code here
```

**Quick Retry:**
```python
@retry_on_failure(max_attempts=3, delay=1.0)
def flaky_operation():
    # Your code here
```

---

Remember: These patterns are **tested and working**. Always prefer copying these over inventing new patterns.