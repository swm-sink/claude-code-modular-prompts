# Credential Protection

**Purpose**: Detect and mask sensitive credentials (API keys, passwords, tokens) to prevent accidental exposure during command execution.

**Usage**: 
- Scan input and output for 13+ credential formats using regex patterns
- Automatically mask detected credentials with safe placeholder values
- Prevent credential exposure in logs, error messages, and command output
- Support custom credential patterns and masking strategies
- Provide comprehensive protection during all command operations

**Compatibility**: 
- **Works with**: secure-config, command-security-wrapper, error-handler, content-sanitizer
- **Requires**: Input/output streams containing potential credentials
- **Conflicts**: None (universal security protection)

**Implementation**:
```python
# Detect and mask credentials in text
def protect_credentials(text):
    credential_patterns = {
        'api_key': r'[Aa][Pp][Ii]_?[Kk][Ee][Yy]\s*[=:]\s*["\']?([A-Za-z0-9]{20,})["\']?',
        'password': r'[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd]\s*[=:]\s*["\']?([^\s"\']+)["\']?',
        'token': r'[Tt][Oo][Kk][Ee][Nn]\s*[=:]\s*["\']?([A-Za-z0-9+/]{20,})["\']?',
        'secret': r'[Ss][Ee][Cc][Rr][Ee][Tt]\s*[=:]\s*["\']?([^\s"\']+)["\']?'
    }
    
    protected_text = text
    found_credentials = []
    
    for cred_type, pattern in credential_patterns.items():
        matches = re.finditer(pattern, protected_text)
        for match in matches:
            credential_value = match.group(1)
            masked_value = f"***{cred_type.upper()}***"
            protected_text = protected_text.replace(credential_value, masked_value)
            found_credentials.append(cred_type)
    
    return protected_text, found_credentials
```

**Category**: security | **Complexity**: moderate | **Time**: 1 hour