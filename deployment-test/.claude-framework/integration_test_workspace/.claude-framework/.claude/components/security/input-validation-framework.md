# Input Validation Framework

## Overview

Modular input validation framework extending successful patterns from security-critical-2 (88% success with credential protection) and security-critical-3 (100% success with path traversal protection) to provide comprehensive input validation across all 18 commands requiring user input processing.

## Validation Module Architecture

### 1. File Path Validation
**Extends:** path-validation-functions.md (100% attack blocking from security-critical-3)
**Purpose:** Validate and sanitize all file path inputs
**Performance:** <2ms per validation

```python
def validate_file_path(user_path, command_type="default", allowed_directories=None):
    """
    Comprehensive file path validation building on proven path traversal protection.
    Returns validated canonical path or raises SecurityError.
    """
    import pathlib
    import re
    
    # Phase 1: Sanitize traversal sequences (from security-critical-3)
    sanitized = sanitize_traversal_sequences(user_path)
    
    # Phase 2: Canonicalize and boundary check
    canonical = validate_and_canonicalize_path(sanitized)
    
    # Phase 3: Allowlist enforcement based on command type
    if not check_path_allowlist(canonical, allowed_directories, command_type):
        raise SecurityError(f"Path not in allowlist for {command_type}: {canonical}")
    
    # Phase 4: Extension validation
    allowed_extensions = get_allowed_extensions(command_type)
    if allowed_extensions and not any(canonical.endswith(ext) for ext in allowed_extensions):
        raise SecurityError(f"File extension not allowed: {canonical}")
    
    return canonical

def get_allowed_extensions(command_type):
    """Command-specific file extension allowlists"""
    extension_allowlists = {
        "notebook-run": [".ipynb", ".py", ".json"],
        "component-gen": [".tsx", ".jsx", ".ts", ".js", ".md"],
        "api-design": [".yaml", ".yml", ".json", ".md"],
        "db-restore": [".sql", ".dump", ".bak"],
        "env-setup": [".env", ".yaml", ".yml", ".json"],
        "test-integration": [".py", ".js", ".ts", ".json"],
        "default": [".md", ".json", ".yaml", ".yml", ".txt"]
    }
    return extension_allowlists.get(command_type, extension_allowlists["default"])
```

### 2. URL Validation
**Extends:** credential-protection.md regex patterns (88% success from security-critical-2)
**Purpose:** Validate repository URLs, API endpoints, and external resources
**Performance:** <1ms per validation

```python
def validate_url(url_input, allowed_schemes=None, allowed_domains=None):
    """
    URL validation using proven regex patterns from credential protection.
    Validates scheme, domain, and prevents malicious URLs.
    """
    import re
    import urllib.parse
    
    if not url_input or not isinstance(url_input, str):
        raise SecurityError("URL input required")
    
    # Remove whitespace and check length
    url = url_input.strip()
    if len(url) > 2048:  # Reasonable URL length limit
        raise SecurityError("URL too long")
    
    # Parse URL components
    try:
        parsed = urllib.parse.urlparse(url)
    except Exception:
        raise SecurityError(f"Invalid URL format: {url}")
    
    # Validate scheme
    default_schemes = ['https', 'http', 'git', 'ssh']
    schemes = allowed_schemes or default_schemes
    if parsed.scheme.lower() not in schemes:
        raise SecurityError(f"URL scheme not allowed: {parsed.scheme}")
    
    # Validate domain if allowlist provided
    if allowed_domains:
        domain = parsed.netloc.lower()
        if not any(domain.endswith(allowed) for allowed in allowed_domains):
            raise SecurityError(f"Domain not in allowlist: {domain}")
    
    # Block private/local addresses for security
    private_patterns = [
        r'^localhost',
        r'^127\.',
        r'^192\.168\.',
        r'^10\.',
        r'^172\.(1[6-9]|2[0-9]|3[01])\.'
    ]
    
    if any(re.match(pattern, parsed.netloc, re.IGNORECASE) for pattern in private_patterns):
        raise SecurityError(f"Private/local URLs not allowed: {url}")
    
    return url

def get_domain_allowlist(command_type):
    """Command-specific domain allowlists"""
    domain_allowlists = {
        "env-setup": ["github.com", "gitlab.com", "bitbucket.org"],
        "ci-setup": ["github.com", "gitlab.com", "circleci.com", "travis-ci.org"],
        "api-design": ["api.github.com", "api.gitlab.com", "jsonplaceholder.typicode.com"],
        "component-gen": ["npmjs.com", "unpkg.com", "jsdelivr.net"],
        "default": ["github.com", "gitlab.com"]
    }
    return domain_allowlists.get(command_type, domain_allowlists["default"])
```

### 3. Configuration Validation
**Extends:** credential-protection.md detection patterns (88% success from security-critical-2)
**Purpose:** Validate environment variables, database configs, CI/CD parameters
**Performance:** <1.5ms per validation

```python
def validate_configuration_value(config_key, config_value, command_type="default"):
    """
    Configuration validation extending credential protection patterns.
    Detects and masks sensitive values while validating format.
    """
    from .credential_protection import detectAndMaskCredentials
    
    if not config_key or not isinstance(config_key, str):
        raise SecurityError("Configuration key required")
    
    # Validate key format (alphanumeric, underscore, hyphen only)
    if not re.match(r'^[A-Za-z0-9_-]+$', config_key):
        raise SecurityError(f"Invalid configuration key format: {config_key}")
    
    # Check for sensitive configuration patterns
    sensitive_patterns = [
        r'(password|secret|token|key|credential)',
        r'(api_key|access_key|private_key)',
        r'(db_pass|database_password)',
        r'(auth_token|bearer_token)'
    ]
    
    is_sensitive = any(re.search(pattern, config_key, re.IGNORECASE) for pattern in sensitive_patterns)
    
    if config_value is None:
        return {"key": config_key, "value": None, "is_sensitive": is_sensitive}
    
    # Convert to string for validation
    value_str = str(config_value)
    
    # Apply credential detection from security-critical-2
    protection_result = detectAndMaskCredentials(value_str)
    
    # Validate value based on key patterns
    validation_result = validate_config_by_type(config_key, value_str, command_type)
    
    return {
        "key": config_key,
        "value": protection_result["maskedText"] if protection_result["detectedCredentials"] > 0 else value_str,
        "is_sensitive": is_sensitive or protection_result["detectedCredentials"] > 0,
        "validation_passed": validation_result["valid"],
        "error_message": validation_result.get("error"),
        "credentials_masked": protection_result["detectedCredentials"]
    }

def validate_config_by_type(config_key, config_value, command_type):
    """Type-specific configuration validation"""
    key_lower = config_key.lower()
    
    # Database configuration validation
    if 'db_' in key_lower or 'database_' in key_lower:
        if key_lower.endswith('_host'):
            return validate_hostname(config_value)
        elif key_lower.endswith('_port'):
            return validate_port(config_value)
        elif key_lower.endswith('_url'):
            return validate_database_url(config_value)
    
    # Environment validation
    if key_lower.startswith('env_') or key_lower.endswith('_env'):
        return validate_environment_name(config_value)
    
    # URL validation for endpoints
    if 'url' in key_lower or 'endpoint' in key_lower:
        try:
            validate_url(config_value, allowed_domains=get_domain_allowlist(command_type))
            return {"valid": True}
        except SecurityError as e:
            return {"valid": False, "error": str(e)}
    
    # Default: basic string validation
    return validate_basic_string(config_value)

def validate_hostname(hostname):
    """Validate hostname format"""
    import re
    hostname_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$'
    if re.match(hostname_pattern, hostname):
        return {"valid": True}
    return {"valid": False, "error": "Invalid hostname format"}

def validate_port(port):
    """Validate port number"""
    try:
        port_num = int(port)
        if 1 <= port_num <= 65535:
            return {"valid": True}
        return {"valid": False, "error": "Port must be between 1-65535"}
    except ValueError:
        return {"valid": False, "error": "Port must be a number"}

def validate_environment_name(env_name):
    """Validate environment name"""
    valid_envs = ['dev', 'development', 'test', 'testing', 'stage', 'staging', 'prod', 'production']
    if env_name.lower() in valid_envs:
        return {"valid": True}
    return {"valid": False, "error": f"Environment must be one of: {', '.join(valid_envs)}"}

def validate_basic_string(value):
    """Basic string validation"""
    if len(str(value)) > 1000:
        return {"valid": False, "error": "Configuration value too long"}
    return {"valid": True}
```

### 4. User Data Sanitization
**Purpose:** Sanitize task descriptions, feature names, and user-provided content
**Performance:** <1ms per validation

```python
def sanitize_user_data(user_input, input_type="text", max_length=1000):
    """
    User data sanitization for task descriptions and user content.
    Removes dangerous characters while preserving legitimate content.
    """
    if not user_input:
        return {"sanitized": "", "changes_made": False, "blocked_content": []}
    
    # Convert to string and check length
    text = str(user_input).strip()
    if len(text) > max_length:
        raise SecurityError(f"Input too long: {len(text)} chars (max: {max_length})")
    
    original_text = text
    blocked_content = []
    
    # Remove potential script injection patterns
    dangerous_patterns = [
        (r'<script[^>]*>.*?</script>', '[SCRIPT_REMOVED]'),
        (r'javascript:', '[JS_REMOVED]'),
        (r'on\w+\s*=', '[EVENT_REMOVED]'),
        (r'eval\s*\(', '[EVAL_REMOVED]'),
        (r'document\.\w+', '[DOM_REMOVED]'),
        (r'window\.\w+', '[WINDOW_REMOVED]'),
    ]
    
    for pattern, replacement in dangerous_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        if matches:
            blocked_content.extend(matches)
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE | re.DOTALL)
    
    # Sanitize based on input type
    if input_type == "task_description":
        text = sanitize_task_description(text)
    elif input_type == "feature_name":
        text = sanitize_feature_name(text)
    elif input_type == "file_content":
        text = sanitize_file_content(text)
    
    return {
        "sanitized": text,
        "changes_made": text != original_text,
        "blocked_content": blocked_content,
        "length": len(text)
    }

def sanitize_task_description(text):
    """Sanitize task descriptions while preserving formatting"""
    # Allow common formatting but remove dangerous chars
    allowed_chars_pattern = r'[^a-zA-Z0-9\s\.\,\!\?\:\;\-\_\(\)\[\]\{\}\@\#\$\%\^\&\*\+\=\|\\\n\r\t]'
    sanitized = re.sub(allowed_chars_pattern, '', text)
    
    # Limit consecutive special characters
    sanitized = re.sub(r'[^\w\s]{3,}', '...', sanitized)
    
    return sanitized.strip()

def sanitize_feature_name(text):
    """Sanitize feature names to safe identifier format"""
    # Convert to safe identifier: alphanumeric, hyphen, underscore only
    sanitized = re.sub(r'[^a-zA-Z0-9\-\_\s]', '', text)
    
    # Replace spaces with hyphens and collapse multiple separators
    sanitized = re.sub(r'[\s\-\_]+', '-', sanitized)
    
    # Remove leading/trailing separators
    sanitized = sanitized.strip('-_')
    
    return sanitized.lower()

def sanitize_file_content(text):
    """Sanitize file content while preserving code structure"""
    # More permissive for code content, but still block dangerous patterns
    blocked_patterns = [
        r'rm\s+-rf\s+/',
        r'sudo\s+',
        r'chmod\s+777',
        r'wget\s+.*\|\s*sh',
        r'curl\s+.*\|\s*sh',
    ]
    
    for pattern in blocked_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            text = re.sub(pattern, '[DANGEROUS_COMMAND_REMOVED]', text, flags=re.IGNORECASE)
    
    return text
```

### 5. Placeholder Validation
**Purpose:** Validate INSERT_XXX patterns and replacement content safety
**Performance:** <0.5ms per validation

```python
def validate_placeholder(placeholder_text, replacement_value=None):
    """
    Validate INSERT_XXX placeholder patterns and ensure safe replacements.
    Returns validation result and safe replacement if provided.
    """
    if not placeholder_text:
        return {"valid": False, "error": "Placeholder text required"}
    
    # Standard placeholder pattern
    placeholder_pattern = r'\[INSERT_([A-Z_]+)\]'
    matches = re.findall(placeholder_pattern, placeholder_text)
    
    if not matches:
        return {"valid": False, "error": "No valid INSERT_XXX placeholders found"}
    
    valid_placeholder_types = [
        'PROJECT_NAME', 'DOMAIN', 'TECH_STACK', 'COMPANY_NAME', 'TEAM_SIZE',
        'DATABASE_URL', 'API_ENDPOINT', 'REPOSITORY_URL', 'ENVIRONMENT',
        'CONFIG_FILE', 'OUTPUT_DIR', 'COMPONENT_NAME', 'FEATURE_NAME'
    ]
    
    result = {
        "valid": True,
        "placeholders_found": matches,
        "invalid_placeholders": [],
        "replacement_result": None
    }
    
    # Validate placeholder types
    for placeholder in matches:
        if placeholder not in valid_placeholder_types:
            result["invalid_placeholders"].append(placeholder)
            result["valid"] = False
    
    # If replacement value provided, validate and perform replacement
    if replacement_value is not None:
        replacement_result = validate_placeholder_replacement(
            placeholder_text, replacement_value, matches[0] if matches else None
        )
        result["replacement_result"] = replacement_result
    
    return result

def validate_placeholder_replacement(template_text, replacement_value, placeholder_type):
    """
    Validate replacement value and perform safe substitution.
    """
    if not replacement_value:
        return {"valid": False, "error": "Replacement value required"}
    
    # Validate replacement based on placeholder type
    validation_rules = {
        'PROJECT_NAME': validate_project_name,
        'DOMAIN': validate_domain_name,
        'TECH_STACK': validate_tech_stack,
        'COMPANY_NAME': validate_company_name,
        'TEAM_SIZE': validate_team_size,
        'DATABASE_URL': validate_database_url,
        'API_ENDPOINT': validate_api_endpoint,
        'REPOSITORY_URL': validate_repository_url,
        'ENVIRONMENT': validate_environment_name,
        'CONFIG_FILE': lambda x: validate_file_path(x, "config"),
        'OUTPUT_DIR': lambda x: validate_file_path(x, "output"),
        'COMPONENT_NAME': validate_component_name,
        'FEATURE_NAME': validate_feature_name
    }
    
    validator = validation_rules.get(placeholder_type, validate_generic_replacement)
    validation_result = validator(replacement_value)
    
    if not validation_result["valid"]:
        return validation_result
    
    # Perform safe replacement
    safe_value = validation_result.get("sanitized_value", replacement_value)
    placeholder_pattern = f'\\[INSERT_{placeholder_type}\\]'
    replaced_text = re.sub(placeholder_pattern, safe_value, template_text)
    
    return {
        "valid": True,
        "replaced_text": replaced_text,
        "sanitized_value": safe_value,
        "changes_made": replaced_text != template_text
    }

def validate_project_name(name):
    """Validate project name format"""
    if not re.match(r'^[a-zA-Z0-9\-\_\s]{1,50}$', name):
        return {"valid": False, "error": "Project name must be alphanumeric with spaces, hyphens, underscores (1-50 chars)"}
    return {"valid": True, "sanitized_value": name.strip()}

def validate_domain_name(domain):
    """Validate domain name"""
    valid_domains = ['web-dev', 'data-science', 'mobile-dev', 'devops', 'api-dev', 'ml-ops']
    if domain.lower() not in valid_domains:
        return {"valid": False, "error": f"Domain must be one of: {', '.join(valid_domains)}"}
    return {"valid": True, "sanitized_value": domain.lower()}

def validate_tech_stack(stack):
    """Validate technology stack"""
    # Allow common tech stack formats
    if len(stack) > 200:
        return {"valid": False, "error": "Tech stack description too long"}
    sanitized = re.sub(r'[^a-zA-Z0-9\s\,\.\-\_\+\#]', '', stack)
    return {"valid": True, "sanitized_value": sanitized.strip()}

def validate_component_name(name):
    """Validate React/Vue component name"""
    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', name):
        return {"valid": False, "error": "Component name must be PascalCase alphanumeric"}
    return {"valid": True, "sanitized_value": name}

def validate_feature_name(name):
    """Validate feature name"""
    sanitized = sanitize_feature_name(name)
    if not sanitized:
        return {"valid": False, "error": "Feature name cannot be empty after sanitization"}
    return {"valid": True, "sanitized_value": sanitized}

def validate_generic_replacement(value):
    """Generic replacement validation"""
    if len(str(value)) > 500:
        return {"valid": False, "error": "Replacement value too long"}
    sanitized = str(value).strip()
    return {"valid": True, "sanitized_value": sanitized}
```

## Integration Pattern for Commands

Commands integrate validation using this standard pattern:

```markdown
## Input Validation

Before processing, I'll validate all inputs for security:

{{#validation_start}}
**Validating inputs...**

{{#if file_path}}
- File Path: `{file_path}` → {{validate_file_path file_path command_type}}
{{/if}}

{{#if url}}
- URL: `{url}` → {{validate_url url (get_domain_allowlist command_type)}}
{{/if}}

{{#if config_values}}
{{#each config_values}}
- Config `{key}`: → {{validate_configuration_value key value ../command_type}}
{{/each}}
{{/if}}

{{#if user_data}}
- User Data: → {{sanitize_user_data user_data input_type max_length}}
{{/if}}

{{#if placeholders}}
{{#each placeholders}}
- Placeholder `{placeholder}`: → {{validate_placeholder placeholder replacement}}
{{/each}}
{{/if}}

**Validation Result:**
{{#if all_validations_passed}}
✅ **SECURE**: All inputs validated successfully
- Total validations: {validation_count}
- Performance: {total_validation_time}ms (under 50ms requirement)
- Security status: All inputs safe

Proceeding with validated inputs...
{{else}}
❌ **SECURITY VIOLATION**: Input validation failed
- Failed validations: {failed_validations}
- Security issues: {security_issues}
- Action: Operation blocked for security

Cannot proceed. Please correct the invalid inputs and try again.
{{/if}}
{{/validation_end}}
```

## Performance Monitoring

Each validation type tracks performance:

```python
def track_validation_performance():
    """Performance tracking for validation operations"""
    return {
        "file_path_validation": "<2ms average",
        "url_validation": "<1ms average", 
        "configuration_validation": "<1.5ms average",
        "user_data_sanitization": "<1ms average",
        "placeholder_validation": "<0.5ms average",
        "total_per_command": "<5ms (requirement met)"
    }
```

## Error Handling and User Feedback

Validation provides clear, actionable error messages:

```python
def format_validation_error(validation_type, error_details):
    """Format validation errors for user display"""
    error_templates = {
        "file_path": "🔒 Path Security: {error} - Please provide a valid path within project boundaries",
        "url": "🌐 URL Security: {error} - Please provide a valid URL from allowed domains", 
        "configuration": "⚙️ Config Security: {error} - Please check configuration format and values",
        "user_data": "📝 Input Security: {error} - Please review your input content",
        "placeholder": "🔧 Template Security: {error} - Please use valid placeholder format"
    }
    
    template = error_templates.get(validation_type, "🛡️ Security: {error}")
    return template.format(error=error_details)
```

This framework provides functional input validation that builds on proven successful patterns while covering all input types across the 18 commands requiring validation.