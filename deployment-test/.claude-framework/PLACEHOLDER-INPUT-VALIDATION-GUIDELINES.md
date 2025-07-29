# Placeholder Input Validation Guidelines

**Purpose**: Comprehensive input validation framework for safe placeholder replacement in Claude Code command templates.

## Validation Framework Overview

### Security Objectives
1. **Prevent injection attacks** - No command, script, or HTML injection
2. **Block path traversal** - No filesystem access outside intended scope  
3. **Sanitize special characters** - Remove or escape dangerous characters
4. **Enforce reasonable limits** - Prevent excessively long or empty inputs
5. **Validate domain-specific values** - Ensure values make sense for their context

## Input Validation Rules

### 1. Character Whitelist Validation

**Basic Rule**: Only allow safe characters
```regex
^[a-zA-Z0-9\s\-_.]+$
```

**Allowed Characters:**
- ✅ Letters: `a-z`, `A-Z`
- ✅ Numbers: `0-9`
- ✅ Spaces: ` ` (single spaces only)
- ✅ Hyphens: `-`
- ✅ Underscores: `_`
- ✅ Periods: `.`

**Forbidden Characters:**
- ❌ Quotes: `'`, `"`, `` ` ``
- ❌ Command separators: `;`, `&`, `|`, `&&`, `||`
- ❌ Special symbols: `@`, `#`, `$`, `%`, `^`, `*`, `+`, `=`
- ❌ Brackets: `()`, `[]`, `{}`
- ❌ Slashes: `/`, `\`
- ❌ HTML/XML: `<`, `>`

### 2. Length Validation

**Standard Limits:**
```yaml
minimum_length: 1        # No empty values
maximum_length: 100      # Reasonable limit for most contexts
```

**Placeholder-Specific Limits:**
```yaml
INSERT_PROJECT_NAME:
  min: 2
  max: 50
  
INSERT_DOMAIN:
  min: 3
  max: 20
  
INSERT_TECH_STACK:
  min: 3
  max: 80
  
INSERT_COMPANY_NAME:
  min: 2
  max: 60
```

### 3. Content Pattern Validation

**Dangerous Pattern Detection:**
```regex
# Command injection patterns
(cmd|bash|sh|exec|eval|system)\s*[\(\[]

# Script injection patterns  
<script[^>]*>|javascript:|on\w+\s*=

# Path traversal patterns
\.\./|\.\.\\|\\\\\.\.|%2e%2e

# Variable expansion patterns
\$\{|\$\(|%\w+%|\`[^`]*\`

# HTML/XML injection
<[^>]+>|&\w+;
```

**Validation Logic:**
```python
def is_dangerous_content(value):
    dangerous_patterns = [
        r'(cmd|bash|sh|exec|eval|system)\s*[\(\[]',
        r'<script[^>]*>|javascript:|on\w+\s*=',
        r'\.\./|\.\.\\|\\\\\.\.|%2e%2e',
        r'\$\{|\$\(|%\w+%|`[^`]*`',
        r'<[^>]+>|&\w+;'
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, value, re.IGNORECASE):
            return True
    return False
```

### 4. Domain-Specific Validation

**INSERT_PROJECT_NAME**
```yaml
validation:
  pattern: "^[a-zA-Z][a-zA-Z0-9\-_]{1,49}$"
  description: "Must start with letter, alphanumeric + hyphens/underscores"
  examples:
    valid: ["MyProject", "web-app", "data_pipeline"]
    invalid: ["123project", "my project", "app-"]
```

**INSERT_DOMAIN**
```yaml
validation:
  type: "enum"
  allowed_values: 
    - "web-dev"
    - "data-science" 
    - "devops"
    - "enterprise"
    - "mobile"
    - "ai-ml"
    - "blockchain"
    - "iot"
  case_sensitive: true
```

**INSERT_TECH_STACK**
```yaml
validation:
  pattern: "^[a-zA-Z0-9\s\+\-_\.]{3,80}$"
  description: "Tech names with + separators allowed"
  examples:
    valid: ["React+Node.js", "Python+FastAPI", "Go+PostgreSQL"]
    invalid: ["React & Node", "Python/FastAPI", "Go|PostgreSQL"]
```

**INSERT_TEAM_SIZE**
```yaml
validation:
  type: "enum"
  allowed_values: ["solo", "small", "medium", "large", "enterprise"]
  description: "Predefined team size categories"
```

**INSERT_CI_CD_PLATFORM**
```yaml
validation:
  type: "enum"
  allowed_values:
    - "GitHub Actions"
    - "Jenkins"  
    - "GitLab CI"
    - "Azure DevOps"
    - "CircleCI"
    - "Travis CI"
    - "Bitbucket Pipelines"
  description: "Common CI/CD platforms"
```

## Validation Implementation

### Python Validation Function

```python
import re
from typing import Dict, List, Tuple, Optional

class PlaceholderValidator:
    def __init__(self):
        self.validation_rules = {
            '[INSERT_PROJECT_NAME]': {
                'pattern': r'^[a-zA-Z][a-zA-Z0-9\-_]{1,49}$',
                'max_length': 50,
                'min_length': 2
            },
            '[INSERT_DOMAIN]': {
                'type': 'enum',
                'allowed_values': ['web-dev', 'data-science', 'devops', 
                                 'enterprise', 'mobile', 'ai-ml']
            },
            '[INSERT_TECH_STACK]': {
                'pattern': r'^[a-zA-Z0-9\s\+\-_\.]{3,80}$',
                'max_length': 80,
                'min_length': 3
            },
            '[INSERT_TEAM_SIZE]': {
                'type': 'enum', 
                'allowed_values': ['solo', 'small', 'medium', 'large', 'enterprise']
            }
        }
    
    def validate_value(self, placeholder: str, value: str) -> Tuple[bool, List[str]]:
        """Validate a replacement value for a specific placeholder."""
        errors = []
        
        # Basic validation
        if not value or not value.strip():
            errors.append("Value cannot be empty")
            return False, errors
            
        # Length validation
        if len(value) > 100:
            errors.append("Value exceeds maximum length of 100 characters")
            
        # Character whitelist validation
        if not re.match(r'^[a-zA-Z0-9\s\-_.]+$', value):
            errors.append("Value contains forbidden characters")
            
        # Dangerous pattern detection
        if self._is_dangerous_content(value):
            errors.append("Value contains potentially dangerous patterns")
            
        # Placeholder-specific validation
        if placeholder in self.validation_rules:
            rule = self.validation_rules[placeholder]
            
            if rule.get('type') == 'enum':
                if value not in rule['allowed_values']:
                    errors.append(f"Value must be one of: {', '.join(rule['allowed_values'])}")
                    
            elif 'pattern' in rule:
                if not re.match(rule['pattern'], value):
                    errors.append("Value does not match required pattern")
                    
            if 'min_length' in rule and len(value) < rule['min_length']:
                errors.append(f"Value must be at least {rule['min_length']} characters")
                
            if 'max_length' in rule and len(value) > rule['max_length']:
                errors.append(f"Value must be at most {rule['max_length']} characters")
        
        return len(errors) == 0, errors
    
    def _is_dangerous_content(self, value: str) -> bool:
        """Check for dangerous patterns in value."""
        dangerous_patterns = [
            r'(cmd|bash|sh|exec|eval|system)\s*[\(\[]',
            r'<script[^>]*>|javascript:|on\w+\s*=',
            r'\.\./|\.\.\\|\\\\\.\.|%2e%2e',
            r'\$\{|\$\(|%\w+%|`[^`]*`',
            r'<[^>]+>|&\w+;',
            r'[\'"`;|&]'
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, value, re.IGNORECASE):
                return True
        return False

# Usage example
validator = PlaceholderValidator()
is_valid, errors = validator.validate_value('[INSERT_PROJECT_NAME]', 'MyApp')
```

### Bash Validation Script

```bash
#!/bin/bash
# validate_placeholder_input.sh

validate_placeholder_value() {
    local placeholder="$1"
    local value="$2"
    local errors=()
    
    # Check if empty
    if [[ -z "$value" ]]; then
        errors+=("Value cannot be empty")
        return 1
    fi
    
    # Check length
    if [[ ${#value} -gt 100 ]]; then
        errors+=("Value exceeds maximum length of 100 characters")
    fi
    
    # Check for dangerous characters
    if [[ "$value" =~ [\'\"`;|&<>] ]]; then
        errors+=("Value contains forbidden characters")
    fi
    
    # Check for dangerous patterns
    if [[ "$value" =~ \.\./|\\\\ ]]; then
        errors+=("Value contains path traversal patterns")
    fi
    
    if [[ "$value" =~ \<script\>|javascript:|eval\( ]]; then
        errors+=("Value contains script injection patterns")
    fi
    
    # Print errors if any
    if [[ ${#errors[@]} -gt 0 ]]; then
        echo "❌ Validation failed for $placeholder:"
        printf "   - %s\n" "${errors[@]}"
        return 1
    else
        echo "✅ Valid: $placeholder = $value"
        return 0
    fi
}

# Example usage
validate_placeholder_value "[INSERT_PROJECT_NAME]" "MyApp"
validate_placeholder_value "[INSERT_DOMAIN]" "web-dev"
```

## User Validation Checklist

### Before Replacement
```markdown
□ Read all input validation guidelines
□ Prepare all replacement values in a secure text file
□ Validate each value against security rules
□ Test values with validation script if available
□ Backup .claude/ directory before making changes
```

### During Replacement
```markdown
□ Replace one placeholder type at a time
□ Double-check each replacement value before confirming
□ Use "Match Case" option in find/replace
□ Review each match before replacing
□ Save and test files incrementally
```

### After Replacement
```markdown
□ Search for any remaining [INSERT_ patterns
□ Run syntax validation on modified files
□ Test sample commands in safe environment
□ Verify no error messages or warnings
□ Commit changes with security validation confirmation
```

## Common Validation Errors

### Error: "Value contains forbidden characters"
**Cause**: Using quotes, semicolons, or special characters
**Fix**: Remove special characters, use only alphanumeric + `-_.`
```
❌ "My App!" → ✅ "My-App"
❌ "React & Vue" → ✅ "React+Vue" 
❌ "Team's Project" → ✅ "Team-Project"
```

### Error: "Value contains dangerous patterns"
**Cause**: Patterns that could enable injection attacks
**Fix**: Use safe descriptive names without system patterns
```
❌ "cmd-tools" → ✅ "command-tools"
❌ "script-runner" → ✅ "task-runner"
❌ "../config" → ✅ "app-config"
```

### Error: "Value must be one of: [list]"
**Cause**: Using custom value for enum-restricted placeholder
**Fix**: Choose from predefined options
```
❌ INSERT_DOMAIN: "webapp" → ✅ "web-dev"
❌ INSERT_TEAM_SIZE: "3-people" → ✅ "small"
```

### Error: "Value does not match required pattern"
**Cause**: Format doesn't meet placeholder-specific requirements
**Fix**: Adjust format to match expected pattern
```
❌ INSERT_PROJECT_NAME: "123project" → ✅ "project123"
❌ INSERT_TECH_STACK: "React/Node" → ✅ "React+Node"
```

## Security Testing Commands

### Validate All Replacement Values
```bash
# Test validation before replacement
./scripts/validate_inputs.sh my-values.txt

# Check for dangerous patterns
grep -E '[\'"`;|&<>]' replacement-values.txt

# Verify no path traversal
grep -E '\.\./|\\\\' replacement-values.txt
```

### Post-Replacement Security Check
```bash
# Search for remaining placeholders
grep -r "\[INSERT_" .claude/

# Check for dangerous patterns in replaced content
grep -r -E '[\'"`;|&]' .claude/commands/

# Validate file integrity
find .claude/ -name "*.md" -exec head -5 {} \;
```

---

**Implementation Priority**: CRITICAL - Must be implemented before any placeholder replacement

**Validation Scope**: All 597 placeholder instances across 102 command templates

**Security Level**: Production-ready with comprehensive threat protection