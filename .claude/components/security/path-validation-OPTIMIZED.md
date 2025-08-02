# Path Validation Security

**Purpose**: Comprehensive path validation preventing directory traversal attacks, enforcing security boundaries, and ensuring safe file operations across all commands.

**Usage**: 
- Blocks path traversal attempts (../, ..\, unicode attacks)
- Validates paths stay within project boundaries
- Canonicalizes paths to prevent bypass attempts
- Enforces directory allowlists for high-risk operations
- Provides command-specific security boundaries (notebook sandboxing, component restrictions)

**Compatibility**: 
- **Works with**: input-validation-framework, file-reader, file-writer, credential-protection, owasp-compliance
- **Requires**: project_root, security_boundaries, allowlist_directories
- **Conflicts**: user-confirmation (path security bypass risk)

**Implementation**:
```markdown
{{validate_and_canonicalize_path(user_input)}}
{{#if_path_valid}}
✅ Path validated: {canonical_path}
{{else}}
❌ Invalid path: {validation_error}
{{/if_path_valid}}
```

**Category**: security | **Complexity**: moderate | **Time**: 1 hour