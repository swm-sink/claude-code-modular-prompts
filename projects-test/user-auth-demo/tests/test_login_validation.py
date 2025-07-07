# RED: Write failing tests first (TDD enforcement)
import pytest
from auth.login_validator import LoginValidator


class TestLoginValidation:
    def setup_method(self):
        self.validator = LoginValidator()
    
    def test_valid_username_password_returns_true(self):
        # Acceptance criteria: valid format should pass
        result = self.validator.validate("user@example.com", "SecurePass123!")
        assert result.is_valid is True
        assert result.errors == []
    
    def test_invalid_email_format_returns_false(self):
        # Email validation required
        result = self.validator.validate("invalid-email", "SecurePass123!")
        assert result.is_valid is False
        assert "Invalid email format" in result.errors
    
    def test_weak_password_returns_false(self):
        # Password strength requirements
        result = self.validator.validate("user@example.com", "weak")
        assert result.is_valid is False
        assert "Password must be at least 8 characters" in result.errors
    
    def test_empty_credentials_returns_false(self):
        # Handle edge cases
        result = self.validator.validate("", "")
        assert result.is_valid is False
        assert len(result.errors) >= 2


# This test will FAIL initially - TDD RED phase ✅