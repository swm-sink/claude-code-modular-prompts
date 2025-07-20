# Security Validation Guide

*Version: 1.0.0*
*Purpose: Practical security for a personal developer workflow tool*
*Scope: Prevent common vulnerabilities, not defend against nation-states*

## 🎯 Security Philosophy

This is a **personal workflow tool**, not enterprise software. Our security goals:
1. **Prevent accidents** - Stop unintended damage
2. **Block obvious attacks** - No command injection
3. **Protect local system** - Don't expose secrets
4. **Maintain usability** - Security shouldn't hinder productivity

## 🚫 Input Sanitization

### Command Injection Prevention
```python
import shlex
import re

def sanitize_shell_input(user_input: str) -> str:
    """
    Prevent command injection in shell operations.
    
    Args:
        user_input: Raw user input
        
    Returns:
        Sanitized input safe for shell use
        
    Raises:
        ValueError: If input contains dangerous patterns
    """
    # Absolute blocklist - these should never appear
    dangerous_patterns = [
        r'[;&|]',           # Command chaining
        r'[$`]',            # Variable/command substitution  
        r'[<>]',            # Redirection
        r'\.\.',           # Directory traversal
        r'~/',             # Home directory expansion
        r'/etc/',          # System files
        r'/usr/',          # System binaries
        r'\brm\s+-rf',     # Dangerous commands
        r'\bsudo\b',       # Privilege escalation
        r'\beval\b',       # Code execution
        r'\bexec\b',       # Code execution
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, user_input):
            raise ValueError(
                f"Input contains potentially dangerous pattern: {pattern}\n"
                f"This is blocked for safety. Please modify your input."
            )
    
    # Use shlex to properly quote
    return shlex.quote(user_input)
```

### Path Validation
```python
from pathlib import Path
import os

def validate_safe_path(file_path: str) -> Path:
    """
    Ensure file paths are safe and within project bounds.
    
    Args:
        file_path: Path to validate
        
    Returns:
        Validated Path object
        
    Raises:
        ValueError: If path is unsafe
    """
    # Convert to Path object
    path = Path(file_path)
    
    # Block obvious traversal attempts
    if '..' in path.parts:
        raise ValueError("Path traversal (..) not allowed")
    
    # Block absolute paths
    if path.is_absolute():
        raise ValueError(
            "Absolute paths not allowed. Use relative paths from project root."
        )
    
    # Block access to sensitive directories
    sensitive_dirs = ['.git', '.env', 'node_modules', '__pycache__', '.ssh']
    for part in path.parts:
        if part in sensitive_dirs:
            raise ValueError(f"Access to {part} directory not allowed")
    
    # Resolve and ensure within project
    project_root = Path.cwd()
    resolved = (project_root / path).resolve()
    
    try:
        resolved.relative_to(project_root)
    except ValueError:
        raise ValueError(
            f"Path must be within project directory: {project_root}"
        )
    
    return resolved
```

### Configuration Validation
```python
import json
import xml.etree.ElementTree as ET
from typing import Dict, Any

def validate_config_file(config_path: str, file_type: str = 'json') -> Dict[str, Any]:
    """
    Safely parse configuration files.
    
    Args:
        config_path: Path to config file
        file_type: Type of config file (json, xml)
        
    Returns:
        Parsed configuration
        
    Raises:
        ValueError: If config is invalid or unsafe
    """
    # Validate path first
    path = validate_safe_path(config_path)
    
    # Check file size (prevent memory DoS)
    if path.stat().st_size > 1024 * 1024:  # 1MB limit
        raise ValueError("Config file too large (max 1MB)")
    
    if file_type == 'json':
        with open(path, 'r') as f:
            # Safe JSON parsing (no code execution)
            return json.load(f)
    
    elif file_type == 'xml':
        # Parse safely (prevent XXE attacks)
        parser = ET.XMLParser(resolve_entities=False)
        tree = ET.parse(path, parser)
        # Convert to dict (simplified)
        return {elem.tag: elem.text for elem in tree.getroot()}
    
    else:
        raise ValueError(f"Unsupported config type: {file_type}")
```

## 🔐 Secret Protection

### Environment Variable Safety
```python
import os
import re

def get_env_safely(key: str, default: str = None, mask_in_logs: bool = True) -> str:
    """
    Safely retrieve environment variables.
    
    Args:
        key: Environment variable name
        default: Default value if not found
        mask_in_logs: Whether to mask value in logs
        
    Returns:
        Environment variable value
    """
    # Validate key name
    if not re.match(r'^[A-Z_][A-Z0-9_]*$', key):
        raise ValueError(f"Invalid environment variable name: {key}")
    
    value = os.environ.get(key, default)
    
    if value and mask_in_logs:
        # Log that we accessed it, but not the value
        logger.info(f"Accessed environment variable: {key}")
    
    return value

def check_for_secrets(content: str) -> List[str]:
    """
    Scan content for potential secrets.
    
    Args:
        content: Text to scan
        
    Returns:
        List of potential secret patterns found
    """
    secret_patterns = [
        (r'api[_-]?key\s*[:=]\s*["\']?\w{20,}', 'API key'),
        (r'password\s*[:=]\s*["\']?.+["\']?', 'Password'),
        (r'token\s*[:=]\s*["\']?\w{20,}', 'Token'),
        (r'secret\s*[:=]\s*["\']?\w{10,}', 'Secret'),
        (r'private[_-]?key', 'Private key'),
        (r'-----BEGIN (RSA |DSA |EC )?PRIVATE KEY-----', 'Private key'),
    ]
    
    findings = []
    for pattern, name in secret_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            findings.append(name)
    
    return findings
```

### Safe Credential Storage
```python
import keyring
import getpass

class CredentialManager:
    """Manage credentials safely using system keyring."""
    
    def __init__(self, service_name: str = "claude-framework"):
        self.service = service_name
    
    def store_credential(self, key: str, prompt: str = None) -> None:
        """Store credential securely."""
        if not prompt:
            prompt = f"Enter value for {key}: "
        
        # Get value securely (hidden input)
        value = getpass.getpass(prompt)
        
        # Store in system keyring
        try:
            keyring.set_password(self.service, key, value)
            print(f"✓ Stored {key} securely")
        except Exception as e:
            logger.error(f"Failed to store credential: {e}")
            raise
    
    def get_credential(self, key: str) -> str:
        """Retrieve credential securely."""
        try:
            value = keyring.get_password(self.service, key)
            if not value:
                raise ValueError(f"No credential found for: {key}")
            return value
        except Exception as e:
            logger.error(f"Failed to retrieve credential: {e}")
            raise
```

## 🛡️ File Operation Security

### Safe File Writing
```python
import tempfile
import os

def write_file_securely(file_path: str, content: str) -> None:
    """
    Write file with security considerations.
    
    Args:
        file_path: Target file path
        content: Content to write
    """
    # Validate path
    path = validate_safe_path(file_path)
    
    # Check for secrets in content
    secrets = check_for_secrets(content)
    if secrets:
        logger.warning(f"Potential secrets detected: {secrets}")
        response = input("Continue writing file with potential secrets? (y/N): ")
        if response.lower() != 'y':
            raise ValueError("Aborted due to potential secrets")
    
    # Create parent directory if needed
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write atomically using temp file
    with tempfile.NamedTemporaryFile(
        mode='w',
        dir=path.parent,
        delete=False
    ) as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    
    # Set secure permissions (owner read/write only)
    os.chmod(tmp_path, 0o600)
    
    # Atomic rename
    os.rename(tmp_path, path)
```

### Safe Command Execution
```python
import subprocess
import shlex
from typing import List, Tuple

def execute_command_safely(
    command: List[str],
    timeout: int = 30,
    allow_shell: bool = False
) -> Tuple[str, str]:
    """
    Execute commands with security restrictions.
    
    Args:
        command: Command as list of arguments
        timeout: Maximum execution time
        allow_shell: Whether to allow shell execution (default: False)
        
    Returns:
        Tuple of (stdout, stderr)
    """
    # Never allow shell by default
    if allow_shell:
        logger.warning("Shell execution enabled - use with caution")
    
    # Validate command arguments
    for arg in command:
        if not isinstance(arg, str):
            raise ValueError(f"Command argument must be string: {arg}")
        
        # Check for shell metacharacters if shell is disabled
        if not allow_shell and any(c in arg for c in ';|&$`'):
            raise ValueError(
                f"Shell metacharacters not allowed without shell=True: {arg}"
            )
    
    # Set secure environment
    env = os.environ.copy()
    # Remove potentially dangerous variables
    for key in ['LD_PRELOAD', 'LD_LIBRARY_PATH', 'PYTHONPATH']:
        env.pop(key, None)
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            shell=allow_shell,
            env=env
        )
        
        return result.stdout, result.stderr
        
    except subprocess.TimeoutExpired:
        raise TimeoutError(f"Command timed out after {timeout} seconds")
    except Exception as e:
        raise RuntimeError(f"Command execution failed: {e}")
```

## 🔍 Audit and Logging

### Security Event Logging
```python
import logging
from datetime import datetime
from pathlib import Path

class SecurityLogger:
    """Log security-relevant events."""
    
    def __init__(self, log_file: str = ".claude/logs/security.log"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Configure logger
        self.logger = logging.getLogger('security')
        handler = logging.FileHandler(self.log_file)
        handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        )
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def log_file_access(self, file_path: str, operation: str) -> None:
        """Log file access operations."""
        self.logger.info(f"FILE_ACCESS: {operation} on {file_path}")
    
    def log_command_execution(self, command: List[str]) -> None:
        """Log command executions."""
        self.logger.info(f"COMMAND_EXEC: {' '.join(command)}")
    
    def log_validation_failure(self, input_type: str, reason: str) -> None:
        """Log validation failures."""
        self.logger.warning(f"VALIDATION_FAIL: {input_type} - {reason}")
    
    def log_security_event(self, event_type: str, details: str) -> None:
        """Log general security events."""
        self.logger.warning(f"SECURITY_EVENT: {event_type} - {details}")
```

## 🚀 Security Checklist

### Before Processing User Input
- [ ] Validate against whitelist if possible
- [ ] Check for command injection patterns
- [ ] Validate path boundaries
- [ ] Check input size limits
- [ ] Sanitize special characters

### Before File Operations
- [ ] Validate file path is within project
- [ ] Check file permissions
- [ ] Scan for secrets in content
- [ ] Use atomic operations
- [ ] Set appropriate permissions

### Before Command Execution
- [ ] Use argument list, not shell strings
- [ ] Validate all arguments
- [ ] Set timeout limits
- [ ] Use minimal environment
- [ ] Log execution

### Configuration Security
- [ ] Validate config file paths
- [ ] Limit config file size
- [ ] Use safe parsers (no eval)
- [ ] Validate config values
- [ ] Don't store secrets in configs

## 🎯 Quick Security Patterns

### Pattern 1: User Input to File Path
```python
# SAFE
user_path = get_user_input()
safe_path = validate_safe_path(user_path)
content = read_file_safely(safe_path)

# UNSAFE - DON'T DO THIS
user_path = get_user_input()
content = open(user_path).read()  # No validation!
```

### Pattern 2: User Input to Command
```python
# SAFE
user_arg = get_user_input()
safe_arg = sanitize_shell_input(user_arg)
output = execute_command_safely(['git', 'status', safe_arg])

# UNSAFE - DON'T DO THIS
user_arg = get_user_input()
output = os.system(f"git status {user_arg}")  # Command injection!
```

### Pattern 3: Configuration Loading
```python
# SAFE
config = validate_config_file('config.json', 'json')

# UNSAFE - DON'T DO THIS
config = eval(open('config.txt').read())  # Code execution!
```

## 💡 Security Principles

1. **Validate Everything** - Never trust user input
2. **Fail Securely** - Errors shouldn't expose info
3. **Least Privilege** - Only access what's needed
4. **Log Security Events** - Know what happened
5. **Keep It Simple** - Complex = vulnerable

---

Remember: This is security for a personal tool. Focus on preventing accidents and obvious attacks, not building Fort Knox.