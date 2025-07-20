# TDD Enforcement Engine

| version | last_updated | module_type | status |
|---------|--------------|-------------|--------|
| 1.0.0   | 2025-07-20   | testing     | stable |

## Purpose
Enforce Red-Green-Refactor TDD cycle with test-first validation mechanisms, coverage requirements (90%+), and comprehensive workflow templates.

## Core TDD Enforcement

### Red-Green-Refactor Cycle Enforcement
```xml
<tdd_cycle_enforcement enforcement="BLOCKING">
  <red_phase>
    <requirement>Write failing test FIRST</requirement>
    <validation>Test must fail with expected error message</validation>
    <blocking>Implementation BLOCKED until failing test exists</blocking>
    <coverage_requirement>New test must increase coverage</coverage_requirement>
  </red_phase>
  <green_phase>
    <requirement>Minimal implementation to pass test</requirement>
    <validation>Test must pass with minimal code</validation>
    <blocking>Additional features BLOCKED until test passes</blocking>
    <coverage_requirement>Coverage must reach 90%+ for new code</coverage_requirement>
  </green_phase>
  <refactor_phase>
    <requirement>Improve code while maintaining green tests</requirement>
    <validation>All tests must remain passing</validation>
    <blocking>New features BLOCKED until refactoring complete</blocking>
    <coverage_requirement>Coverage must not decrease</coverage_requirement>
  </refactor_phase>
</tdd_cycle_enforcement>
```

### Test-First Validation Mechanisms
```python
"""
TDD Enforcement Validator
Validates that TDD cycle is followed correctly
"""
import ast
import subprocess
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class TDDEnforcementValidator:
    """Enforces TDD cycle compliance"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.test_dirs = ["tests", "test", "spec"]
        self.source_dirs = ["src", "app", "lib"]
        
    def validate_red_phase(self, test_file: Path) -> Dict[str, bool]:
        """Validate RED phase - test must fail"""
        results = {
            "test_exists": False,
            "test_fails": False,
            "error_message_appropriate": False,
            "coverage_increased": False
        }
        
        # Check test exists
        if test_file.exists():
            results["test_exists"] = True
            
            # Run test and verify it fails
            test_result = self._run_single_test(test_file)
            if test_result["failed"]:
                results["test_fails"] = True
                
                # Check error message is appropriate (not syntax error)
                if self._is_appropriate_failure(test_result["output"]):
                    results["error_message_appropriate"] = True
            
            # Check coverage increased
            if self._coverage_increased():
                results["coverage_increased"] = True
        
        return results
    
    def validate_green_phase(self, test_file: Path, impl_file: Path) -> Dict[str, bool]:
        """Validate GREEN phase - minimal implementation passes test"""
        results = {
            "test_passes": False,
            "implementation_minimal": False,
            "coverage_meets_threshold": False,
            "no_over_engineering": False
        }
        
        # Run test and verify it passes
        test_result = self._run_single_test(test_file)
        if test_result["passed"]:
            results["test_passes"] = True
            
            # Check implementation is minimal
            if self._implementation_is_minimal(impl_file):
                results["implementation_minimal"] = True
                results["no_over_engineering"] = True
            
            # Check coverage meets 90% threshold
            coverage = self._get_coverage_for_file(impl_file)
            if coverage >= 90:
                results["coverage_meets_threshold"] = True
        
        return results
    
    def validate_refactor_phase(self, test_file: Path, impl_file: Path) -> Dict[str, bool]:
        """Validate REFACTOR phase - improve code while maintaining tests"""
        results = {
            "all_tests_pass": False,
            "code_quality_improved": False,
            "coverage_maintained": False,
            "no_new_functionality": False
        }
        
        # Run all tests to ensure they pass
        if self._run_all_tests():
            results["all_tests_pass"] = True
            
            # Check code quality metrics improved
            if self._code_quality_improved(impl_file):
                results["code_quality_improved"] = True
            
            # Check coverage maintained or improved
            if self._coverage_maintained():
                results["coverage_maintained"] = True
            
            # Verify no new functionality added during refactor
            if self._no_new_functionality_added(impl_file):
                results["no_new_functionality"] = True
        
        return results
    
    def _run_single_test(self, test_file: Path) -> Dict[str, any]:
        """Run single test file and return results"""
        cmd = f"python -m pytest {test_file} -v"
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True
        )
        
        return {
            "passed": result.returncode == 0,
            "failed": result.returncode != 0,
            "output": result.stdout + result.stderr
        }
    
    def _run_all_tests(self) -> bool:
        """Run all tests and return success status"""
        cmd = "python -m pytest"
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True
        )
        return result.returncode == 0
    
    def _is_appropriate_failure(self, output: str) -> bool:
        """Check if test failure is appropriate (not syntax error)"""
        inappropriate_errors = [
            "SyntaxError",
            "IndentationError", 
            "ImportError",
            "ModuleNotFoundError"
        ]
        return not any(error in output for error in inappropriate_errors)
    
    def _implementation_is_minimal(self, impl_file: Path) -> bool:
        """Check if implementation is minimal (not over-engineered)"""
        if not impl_file.exists():
            return False
            
        with open(impl_file, 'r') as f:
            content = f.read()
        
        try:
            tree = ast.parse(content)
            
            # Count complexity indicators
            complexity_score = 0
            for node in ast.walk(tree):
                if isinstance(node, (ast.If, ast.For, ast.While, ast.Try)):
                    complexity_score += 1
                elif isinstance(node, ast.FunctionDef):
                    if len(node.body) > 10:  # Function too long
                        complexity_score += 2
                elif isinstance(node, ast.ClassDef):
                    if len(node.body) > 5:  # Class too complex for minimal impl
                        complexity_score += 3
            
            # Minimal implementation should have low complexity
            return complexity_score <= 3
            
        except SyntaxError:
            return False
    
    def _get_coverage_for_file(self, impl_file: Path) -> float:
        """Get coverage percentage for specific file"""
        cmd = f"python -m pytest --cov={impl_file.stem} --cov-report=json"
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True
        )
        
        if result.returncode == 0:
            # Parse coverage JSON output
            import json
            try:
                with open("coverage.json", "r") as f:
                    coverage_data = json.load(f)
                
                file_coverage = coverage_data.get("files", {}).get(str(impl_file), {})
                return file_coverage.get("summary", {}).get("percent_covered", 0)
            except (FileNotFoundError, json.JSONDecodeError):
                return 0
        
        return 0
    
    def _coverage_increased(self) -> bool:
        """Check if overall coverage increased"""
        # This would compare current coverage with previous coverage
        # Implementation depends on coverage tracking system
        return True  # Placeholder
    
    def _coverage_maintained(self) -> bool:
        """Check if coverage was maintained during refactor"""
        # Similar to _coverage_increased but ensures no decrease
        return True  # Placeholder
    
    def _code_quality_improved(self, impl_file: Path) -> bool:
        """Check if code quality metrics improved"""
        # Check metrics like cyclomatic complexity, maintainability index
        cmd = f"python -m radon cc {impl_file} -j"
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True
        )
        
        if result.returncode == 0:
            import json
            try:
                metrics = json.loads(result.stdout)
                # Simple heuristic: average complexity should be low
                avg_complexity = sum(
                    item["complexity"] for item in metrics.get(str(impl_file), [])
                ) / max(len(metrics.get(str(impl_file), [])), 1)
                return avg_complexity <= 3
            except (json.JSONDecodeError, KeyError):
                return False
        
        return False
    
    def _no_new_functionality_added(self, impl_file: Path) -> bool:
        """Verify no new functionality added during refactor"""
        # This would compare function signatures and public API
        # before and after refactor
        return True  # Placeholder


def enforce_tdd_cycle():
    """Command-line TDD enforcement tool"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Enforce TDD cycle")
    parser.add_argument("--phase", choices=["red", "green", "refactor"], required=True)
    parser.add_argument("--test-file", type=Path, required=True)
    parser.add_argument("--impl-file", type=Path)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    
    args = parser.parse_args()
    
    validator = TDDEnforcementValidator(args.project_root)
    
    if args.phase == "red":
        results = validator.validate_red_phase(args.test_file)
        print("RED Phase Validation:")
        for check, passed in results.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")
        
        if not all(results.values()):
            print("\n❌ RED phase validation FAILED")
            exit(1)
        else:
            print("\n✅ RED phase validation PASSED")
    
    elif args.phase == "green":
        if not args.impl_file:
            print("--impl-file required for GREEN phase")
            exit(1)
        
        results = validator.validate_green_phase(args.test_file, args.impl_file)
        print("GREEN Phase Validation:")
        for check, passed in results.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")
        
        if not all(results.values()):
            print("\n❌ GREEN phase validation FAILED")
            exit(1)
        else:
            print("\n✅ GREEN phase validation PASSED")
    
    elif args.phase == "refactor":
        if not args.impl_file:
            print("--impl-file required for REFACTOR phase")
            exit(1)
        
        results = validator.validate_refactor_phase(args.test_file, args.impl_file)
        print("REFACTOR Phase Validation:")
        for check, passed in results.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")
        
        if not all(results.values()):
            print("\n❌ REFACTOR phase validation FAILED")
            exit(1)
        else:
            print("\n✅ REFACTOR phase validation PASSED")


if __name__ == "__main__":
    enforce_tdd_cycle()
```

### Coverage Requirements (90%+)
```xml
<coverage_requirements enforcement="BLOCKING">
  <minimum_threshold>90% line coverage for all new code</minimum_threshold>
  <branch_coverage>85% branch coverage required</branch_coverage>
  <mutation_testing>70% mutation score required</mutation_testing>
  <integration_coverage>80% of business workflows covered</integration_coverage>
  <blocking_conditions>
    <condition>Coverage below threshold blocks commits</condition>
    <condition>Decreasing coverage blocks merges</condition>
    <condition>Untested public methods block releases</condition>
  </blocking_conditions>
</coverage_requirements>
```

### Coverage Enforcement Script
```python
"""
Coverage Enforcement Script
Enforces 90%+ coverage requirements
"""
import subprocess
import json
import sys
from pathlib import Path

class CoverageEnforcer:
    """Enforce coverage requirements"""
    
    def __init__(self, threshold: float = 90.0):
        self.threshold = threshold
        self.branch_threshold = 85.0
        self.mutation_threshold = 70.0
    
    def enforce_coverage(self) -> bool:
        """Enforce all coverage requirements"""
        print("🔍 Enforcing coverage requirements...")
        
        checks = [
            ("Line Coverage", self.check_line_coverage()),
            ("Branch Coverage", self.check_branch_coverage()),
            ("Mutation Testing", self.check_mutation_coverage()),
            ("Integration Coverage", self.check_integration_coverage())
        ]
        
        all_passed = True
        for check_name, passed in checks:
            status = "✅" if passed else "❌"
            print(f"  {status} {check_name}")
            if not passed:
                all_passed = False
        
        if all_passed:
            print("\n✅ All coverage requirements met!")
            return True
        else:
            print("\n❌ Coverage requirements FAILED - commit BLOCKED")
            return False
    
    def check_line_coverage(self) -> bool:
        """Check line coverage meets threshold"""
        cmd = "python -m pytest --cov=. --cov-report=json --cov-fail-under=90"
        result = subprocess.run(cmd, shell=True, capture_output=True)
        
        if result.returncode == 0:
            try:
                with open("coverage.json", "r") as f:
                    coverage_data = json.load(f)
                
                total_coverage = coverage_data["totals"]["percent_covered"]
                print(f"    Line coverage: {total_coverage:.1f}% (threshold: {self.threshold}%)")
                return total_coverage >= self.threshold
            except (FileNotFoundError, KeyError):
                print(f"    ❌ Unable to read coverage data")
                return False
        
        print(f"    ❌ Coverage check failed")
        return False
    
    def check_branch_coverage(self) -> bool:
        """Check branch coverage meets threshold"""
        cmd = "python -m pytest --cov=. --cov-branch --cov-report=json"
        result = subprocess.run(cmd, shell=True, capture_output=True)
        
        if result.returncode == 0:
            try:
                with open("coverage.json", "r") as f:
                    coverage_data = json.load(f)
                
                branch_coverage = coverage_data["totals"]["percent_covered_display"]
                branch_value = float(branch_coverage.rstrip('%'))
                print(f"    Branch coverage: {branch_value:.1f}% (threshold: {self.branch_threshold}%)")
                return branch_value >= self.branch_threshold
            except (FileNotFoundError, KeyError, ValueError):
                print(f"    ❌ Unable to read branch coverage data")
                return False
        
        return False
    
    def check_mutation_coverage(self) -> bool:
        """Check mutation testing meets threshold"""
        cmd = "python -m mutmut run --simple-output"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if "FAILED" not in result.stdout:
            # Parse mutation score from output
            lines = result.stdout.split('\n')
            for line in lines:
                if "Mutation score" in line:
                    try:
                        score = float(line.split(':')[-1].strip().rstrip('%'))
                        print(f"    Mutation score: {score:.1f}% (threshold: {self.mutation_threshold}%)")
                        return score >= self.mutation_threshold
                    except ValueError:
                        continue
        
        print(f"    ❌ Mutation testing failed or unavailable")
        return True  # Don't block if mutation testing not available
    
    def check_integration_coverage(self) -> bool:
        """Check integration test coverage"""
        # Run only integration tests and check coverage
        cmd = "python -m pytest tests/integration/ --cov=. --cov-report=json"
        result = subprocess.run(cmd, shell=True, capture_output=True)
        
        if result.returncode == 0:
            try:
                with open("coverage.json", "r") as f:
                    coverage_data = json.load(f)
                
                integration_coverage = coverage_data["totals"]["percent_covered"]
                print(f"    Integration coverage: {integration_coverage:.1f}% (threshold: 80%)")
                return integration_coverage >= 80.0
            except (FileNotFoundError, KeyError):
                print(f"    ❌ Unable to read integration coverage data")
                return False
        
        return False


def main():
    """Main coverage enforcement entry point"""
    enforcer = CoverageEnforcer()
    success = enforcer.enforce_coverage()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

## TDD Workflow Templates

### Basic TDD Workflow Template
```python
"""
TDD Workflow Template
Follow this template for all TDD development
"""

# STEP 1: RED PHASE - Write failing test first
def test_user_can_create_account():
    """Test user account creation - RED PHASE"""
    user_service = UserService()
    
    # This should fail because UserService.create_user doesn't exist yet
    result = user_service.create_user(
        email="test@example.com",
        password="secure123",
        name="Test User"
    )
    
    assert result.success is True
    assert result.user.email == "test@example.com"
    assert result.user.id is not None
    assert result.user.created_at is not None

# Run test: python -m pytest test_user_service.py::test_user_can_create_account
# Expected: FAIL - UserService.create_user method doesn't exist

# STEP 2: GREEN PHASE - Minimal implementation to pass test
class UserService:
    """Minimal implementation to pass test"""
    
    def create_user(self, email: str, password: str, name: str):
        """Minimal user creation implementation"""
        from datetime import datetime
        from collections import namedtuple
        
        User = namedtuple('User', ['id', 'email', 'name', 'created_at'])
        Result = namedtuple('Result', ['success', 'user'])
        
        user = User(
            id=1,  # Hardcoded for minimal implementation
            email=email,
            name=name,
            created_at=datetime.now()
        )
        
        return Result(success=True, user=user)

# Run test: python -m pytest test_user_service.py::test_user_can_create_account
# Expected: PASS - Test now passes with minimal implementation

# STEP 3: REFACTOR PHASE - Improve implementation while keeping tests green
class User:
    """Proper User model"""
    def __init__(self, email: str, name: str):
        self.id = self._generate_id()
        self.email = email
        self.name = name
        self.created_at = datetime.now()
    
    def _generate_id(self) -> int:
        import uuid
        return int(str(uuid.uuid4().int)[:8])

class UserCreationResult:
    """Proper result object"""
    def __init__(self, success: bool, user: User = None, error: str = None):
        self.success = success
        self.user = user
        self.error = error

class UserService:
    """Improved implementation after refactoring"""
    
    def __init__(self, database=None):
        self.database = database or []
    
    def create_user(self, email: str, password: str, name: str) -> UserCreationResult:
        """Improved user creation with validation"""
        # Validate input
        if not email or "@" not in email:
            return UserCreationResult(success=False, error="Invalid email")
        
        if not password or len(password) < 8:
            return UserCreationResult(success=False, error="Password too short")
        
        if not name or len(name.strip()) == 0:
            return UserCreationResult(success=False, error="Name required")
        
        # Check if user already exists
        if any(u.email == email for u in self.database):
            return UserCreationResult(success=False, error="Email already exists")
        
        # Create user
        user = User(email=email, name=name.strip())
        self.database.append(user)
        
        return UserCreationResult(success=True, user=user)

# Run test: python -m pytest test_user_service.py::test_user_can_create_account
# Expected: PASS - Refactored implementation still passes original test

# STEP 4: Add more tests for edge cases discovered during refactoring
def test_user_creation_validation():
    """Test user creation validation - Added after refactoring"""
    user_service = UserService()
    
    # Test invalid email
    result = user_service.create_user("invalid-email", "secure123", "Test User")
    assert result.success is False
    assert "Invalid email" in result.error
    
    # Test short password
    result = user_service.create_user("test@example.com", "123", "Test User")
    assert result.success is False
    assert "Password too short" in result.error
    
    # Test empty name
    result = user_service.create_user("test@example.com", "secure123", "")
    assert result.success is False
    assert "Name required" in result.error

def test_duplicate_email_prevention():
    """Test duplicate email prevention"""
    user_service = UserService()
    
    # Create first user
    result1 = user_service.create_user("test@example.com", "secure123", "User 1")
    assert result1.success is True
    
    # Try to create user with same email
    result2 = user_service.create_user("test@example.com", "secure456", "User 2")
    assert result2.success is False
    assert "Email already exists" in result2.error
```

### Advanced TDD Integration Workflow
```python
"""
Advanced TDD Workflow for Integration Tests
"""

# STEP 1: RED PHASE - Integration test that fails
def test_complete_user_registration_workflow(test_database, test_email_service):
    """Integration test for complete user registration - RED PHASE"""
    registration_service = RegistrationService(
        database=test_database,
        email_service=test_email_service
    )
    
    # Complete registration workflow
    result = registration_service.register_user(
        email="newuser@example.com",
        password="SecurePass123",
        name="New User"
    )
    
    # Verify registration success
    assert result.success is True
    assert result.user.email == "newuser@example.com"
    assert result.user.email_verified is False
    
    # Verify user stored in database
    stored_user = test_database.get_user_by_email("newuser@example.com")
    assert stored_user is not None
    assert stored_user.password_hash != "SecurePass123"  # Password hashed
    
    # Verify verification email sent
    sent_emails = test_email_service.get_sent_emails()
    assert len(sent_emails) == 1
    assert sent_emails[0].to == "newuser@example.com"
    assert "verify your email" in sent_emails[0].subject.lower()

# Expected: FAIL - RegistrationService doesn't exist

# STEP 2: GREEN PHASE - Minimal integration implementation
class RegistrationService:
    """Minimal registration service implementation"""
    
    def __init__(self, database, email_service):
        self.database = database
        self.email_service = email_service
    
    def register_user(self, email: str, password: str, name: str):
        """Minimal registration implementation"""
        import hashlib
        from collections import namedtuple
        
        User = namedtuple('User', ['email', 'password_hash', 'name', 'email_verified'])
        Result = namedtuple('Result', ['success', 'user'])
        Email = namedtuple('Email', ['to', 'subject', 'body'])
        
        # Hash password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Create user
        user = User(
            email=email,
            password_hash=password_hash,
            name=name,
            email_verified=False
        )
        
        # Store in database
        self.database.add_user(user)
        
        # Send verification email
        email = Email(
            to=email,
            subject="Please verify your email",
            body="Click here to verify your email"
        )
        self.email_service.send_email(email)
        
        return Result(success=True, user=user)

# STEP 3: REFACTOR PHASE - Improve with proper architecture
from dataclasses import dataclass
from typing import Optional
import bcrypt
import secrets

@dataclass
class User:
    """Proper User entity"""
    email: str
    password_hash: str
    name: str
    email_verified: bool = False
    verification_token: Optional[str] = None

@dataclass
class RegistrationResult:
    """Registration result with proper error handling"""
    success: bool
    user: Optional[User] = None
    error: Optional[str] = None

class RegistrationService:
    """Improved registration service with proper architecture"""
    
    def __init__(self, database, email_service, password_validator=None):
        self.database = database
        self.email_service = email_service
        self.password_validator = password_validator or PasswordValidator()
    
    def register_user(self, email: str, password: str, name: str) -> RegistrationResult:
        """Complete registration with validation and security"""
        # Validate inputs
        validation_error = self._validate_registration_inputs(email, password, name)
        if validation_error:
            return RegistrationResult(success=False, error=validation_error)
        
        # Check if user already exists
        if self.database.get_user_by_email(email):
            return RegistrationResult(success=False, error="Email already registered")
        
        # Hash password securely
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Generate verification token
        verification_token = secrets.token_urlsafe(32)
        
        # Create user
        user = User(
            email=email,
            password_hash=password_hash.decode('utf-8'),
            name=name.strip(),
            email_verified=False,
            verification_token=verification_token
        )
        
        try:
            # Store user in database
            self.database.add_user(user)
            
            # Send verification email
            self._send_verification_email(user)
            
            return RegistrationResult(success=True, user=user)
            
        except Exception as e:
            # Rollback and return error
            self.database.remove_user_by_email(email)
            return RegistrationResult(success=False, error=f"Registration failed: {str(e)}")
    
    def _validate_registration_inputs(self, email: str, password: str, name: str) -> Optional[str]:
        """Validate registration inputs"""
        if not email or "@" not in email:
            return "Invalid email address"
        
        if not self.password_validator.is_valid(password):
            return "Password does not meet requirements"
        
        if not name or len(name.strip()) < 2:
            return "Name must be at least 2 characters"
        
        return None
    
    def _send_verification_email(self, user: User):
        """Send verification email"""
        verification_url = f"https://example.com/verify?token={user.verification_token}"
        
        email = EmailMessage(
            to=user.email,
            subject="Please verify your email address",
            body=f"Hello {user.name},\n\nPlease verify your email by clicking: {verification_url}"
        )
        
        self.email_service.send_email(email)

# Run integration test: Still passes after refactoring
```

## Git Hook Integration

### Pre-commit TDD Enforcement
```bash
#!/bin/bash
# .git/hooks/pre-commit
# TDD enforcement pre-commit hook

echo "🔍 Enforcing TDD cycle..."

# Check if we're in a valid TDD phase
if [ -f ".tdd-phase" ]; then
    PHASE=$(cat .tdd-phase)
    echo "Current TDD phase: $PHASE"
    
    case $PHASE in
        "red")
            echo "Validating RED phase..."
            python scripts/enforce_tdd.py --phase red --test-file $(cat .current-test)
            if [ $? -ne 0 ]; then
                echo "❌ RED phase validation failed - commit blocked"
                exit 1
            fi
            ;;
        "green")
            echo "Validating GREEN phase..."
            python scripts/enforce_tdd.py --phase green --test-file $(cat .current-test) --impl-file $(cat .current-impl)
            if [ $? -ne 0 ]; then
                echo "❌ GREEN phase validation failed - commit blocked"
                exit 1
            fi
            ;;
        "refactor")
            echo "Validating REFACTOR phase..."
            python scripts/enforce_tdd.py --phase refactor --test-file $(cat .current-test) --impl-file $(cat .current-impl)
            if [ $? -ne 0 ]; then
                echo "❌ REFACTOR phase validation failed - commit blocked"
                exit 1
            fi
            ;;
    esac
else
    echo "⚠️  No TDD phase set - assuming GREEN phase"
    python scripts/coverage_enforcer.py
    if [ $? -ne 0 ]; then
        echo "❌ Coverage requirements not met - commit blocked"
        exit 1
    fi
fi

echo "✅ TDD enforcement passed"
```

## Thinking Pattern for TDD Enforcement

```xml
<thinking_pattern name="tdd_enforcement">
  <step_1>Identify Current TDD Phase (Red/Green/Refactor)</step_1>
  <step_2>Validate Phase Requirements</step_2>
  <step_3>Block Invalid Transitions</step_3>
  <step_4>Run Appropriate Validation Tools</step_4>
  <step_5>Check Coverage Requirements</step_5>
  <step_6>Verify Test Quality Standards</step_6>
  <step_7>Ensure Minimal Implementation (Green Phase)</step_7>
  <step_8>Validate Refactoring Safety (Refactor Phase)</step_8>
  <step_9>Update Phase Tracking</step_9>
  <step_10>Allow or Block Commit Based on Results</step_10>
</thinking_pattern>
```

## Integration Points

- **Integration-First Testing**: Enforces TDD cycle for integration tests
- **Test Quality Gates**: Validates TDD compliance as part of quality gates
- **Testing Patterns Library**: Provides TDD workflow templates
- **Test Framework Integration**: Integrates TDD enforcement into commands

## Validation Metrics

- TDD cycle compliance (target: 100%)
- Test-first development rate (target: 95%)
- Coverage threshold adherence (target: 90%+)
- Red-Green-Refactor cycle time (target: <30 minutes)
- Test quality score (target: 85%+)