# GREEN: Minimal implementation to pass tests
import re
from dataclasses import dataclass
from typing import List


@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str]


class LoginValidator:
    """
    Login validation with email format and password strength requirements.
    TDD implementation following RED-GREEN-REFACTOR cycle.
    """
    
    def validate(self, username: str, password: str) -> ValidationResult:
        errors = []
        
        # Email format validation
        if not username:
            errors.append("Username is required")
        elif not self._is_valid_email(username):
            errors.append("Invalid email format")
        
        # Password validation
        if not password:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("Password must be at least 8 characters")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors
        )
    
    def _is_valid_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None


# This implementation makes tests PASS - TDD GREEN phase ✅