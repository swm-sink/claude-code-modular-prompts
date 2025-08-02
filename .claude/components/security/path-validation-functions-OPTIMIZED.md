# Path Validation Functions

**Purpose**: Critical security functions for preventing path traversal attacks and enforcing directory boundaries with comprehensive validation and sanitization.

**Usage**: 
- Sanitizes path traversal sequences (../, ..\, unicode attacks)
- Validates and canonicalizes paths to prevent directory escapes
- Enforces project boundary restrictions and allowlist directories
- Provides <5ms performance for real-time validation
- Returns specific security error messages for blocked operations

**Compatibility**: 
- **Works with**: path-validation, input-validation-framework, file-reader, file-writer, command-security-wrapper
- **Requires**: project_root, allowlist_directories, security_error_handlers
- **Conflicts**: user-confirmation (security bypass risk)

**Implementation**:
```python
path_validator = PathValidationFunctions(
    project_root=get_project_root(),
    allowlist=[".claude", "src", "docs", "tests"],
    sanitize=True,
    canonicalize=True
)
safe_path = path_validator.validate(user_input_path)
```

**Category**: security | **Complexity**: moderate | **Time**: 1 hour