# Task Command Documentation

## Overview
The `/task` command is designed for focused, single-component development with automatic TDD enforcement. Use it for bug fixes, small enhancements, and individual functions or classes.

## When to Use `/task`
- ✅ Single function or class
- ✅ Bug fixes
- ✅ Small enhancements (< 50 lines)
- ✅ Utility functions
- ✅ Test additions

## When to Use Other Commands
- `/feature` for complete features (user registration system)
- `/query` for understanding existing code
- `/auto` when unsure which command to use

## Usage Syntax
```bash
/task "clear, specific description of what needs to be implemented"
```

## How It Works
The framework will:
1. **Analyze context**: Understand your project structure and existing code
2. **Plan TDD approach**: Outline test cases before implementation
3. **Create failing tests**: Write comprehensive test cases that fail initially
4. **Implement minimal code**: Create the minimum code to pass tests
5. **Verify tests pass**: Ensure all tests pass after implementation
6. **Suggest improvements**: Recommend code quality enhancements

## Example Walkthrough

### Scenario: Password Validation Function
```bash
/task "add password validation function that checks for length, uppercase, lowercase, and special characters"
```

### Expected Output
```
🔍 ANALYZING PROJECT CONTEXT...
- Language: Python (Django project detected)
- Existing auth module: src/auth/models.py
- Test directory: tests/auth/

📋 TDD PLAN:
1. Create test_password_validation.py with test cases
2. Test for minimum length (8 characters)
3. Test for uppercase requirement
4. Test for lowercase requirement  
5. Test for special character requirement
6. Test for invalid inputs and edge cases

🔴 RED PHASE - Creating failing tests...
```

### Generated Test File
`tests/auth/test_password_validation.py`:
```python
import pytest
from auth.validators import validate_password

def test_password_minimum_length():
    """Test password must be at least 8 characters"""
    assert validate_password("short") == False
    assert validate_password("longenough") == True

def test_password_uppercase_requirement():
    """Test password must contain uppercase letter"""
    assert validate_password("lowercase123!") == False
    assert validate_password("Uppercase123!") == True

def test_password_lowercase_requirement():
    """Test password must contain lowercase letter"""
    assert validate_password("UPPERCASE123!") == False
    assert validate_password("Uppercase123!") == True

def test_password_special_character_requirement():
    """Test password must contain special character"""
    assert validate_password("Uppercase123") == False
    assert validate_password("Uppercase123!") == True

def test_password_all_requirements():
    """Test password with all requirements passes"""
    assert validate_password("ValidPass123!") == True
    assert validate_password("AnotherValid1@") == True
```

### Generated Implementation
`src/auth/validators.py`:
```python
import re

def validate_password(password):
    """
    Validate password meets security requirements:
    - At least 8 characters long
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains special character
    
    Args:
        password (str): Password to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True
```

### Integration Example
```python
# In your user model or form validation
from auth.validators import validate_password

def create_user(email, password):
    if not validate_password(password):
        raise ValueError("Password does not meet security requirements")
    # ... rest of user creation
```

## Key Learning Points

### ✅ What the Framework Does Well
- **TDD Enforcement**: Always creates tests before implementation
- **Context Awareness**: Understands your project structure and language
- **Code Quality**: Follows best practices and naming conventions
- **Integration Ready**: Provides usage examples and integration guidance

### 📚 Best Practices Demonstrated
1. **Clear Requirements**: Specific, testable requirements in the command
2. **Comprehensive Testing**: Multiple test cases covering edge cases
3. **Minimal Implementation**: Just enough code to pass tests
4. **Documentation**: Clear docstrings and comments
5. **Integration Guidance**: Shows how to use the new functionality

## Command Variations

### More Specific Requirements
```bash
/task "add password validation with configurable complexity rules"
```

### Error Handling Focus
```bash
/task "add password validation with detailed error messages"
```

### Performance Focus
```bash
/task "add password validation optimized for high-volume usage"
```

## Testing the Results

### Run Tests
```bash
pytest tests/auth/test_password_validation.py -v

# Expected output:
# ✅ test_password_minimum_length PASSED
# ✅ test_password_uppercase_requirement PASSED  
# ✅ test_password_lowercase_requirement PASSED
# ✅ test_password_special_character_requirement PASSED
# ✅ test_password_all_requirements PASSED
```

### Integration Testing
1. **Test the function**: Run the generated tests to verify functionality
2. **Integrate**: Add the validator to your authentication flow
3. **Extend**: Use `/task` for related functionality like password strength meters
4. **Iterate**: Refine based on user feedback and security requirements

## Next Steps
- **For related functionality**: Use `/task` for additional components
- **For complete features**: Use `/feature` for full feature development
- **For research**: Use `/query` to understand existing implementations
- **For deployment**: Use `/protocol` for production-ready deployment

## Related Documentation
- [Feature Command](feature-command.md) - For complete feature development
- [Query Command](query-command.md) - For code research
- [Auto Command](auto-command.md) - For intelligent command selection