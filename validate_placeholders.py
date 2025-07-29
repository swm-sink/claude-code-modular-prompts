#!/usr/bin/env python3
"""
Placeholder Security Validation Script
Validates replacement values before placeholder substitution
"""

import re
import sys
from typing import Dict, List, Tuple

class PlaceholderValidator:
    def __init__(self):
        self.validation_rules = {
            '[INSERT_PROJECT_NAME]': {
                'pattern': r'^[a-zA-Z][a-zA-Z0-9\-_]{1,49}$',
                'max_length': 50,
                'min_length': 2,
                'description': 'Must start with letter, alphanumeric + hyphens/underscores'
            },
            '[INSERT_DOMAIN]': {
                'type': 'enum',
                'allowed_values': ['web-dev', 'data-science', 'devops', 'enterprise', 'mobile', 'ai-ml', 'blockchain', 'iot'],
                'description': 'Must be from predefined domain list'
            },
            '[INSERT_TECH_STACK]': {
                'pattern': r'^[a-zA-Z0-9\s\+\-_\.]{3,80}$',
                'max_length': 80,
                'min_length': 3,
                'description': 'Tech stack with + separators allowed'
            },
            '[INSERT_TEAM_SIZE]': {
                'type': 'enum',
                'allowed_values': ['solo', 'small', 'medium', 'large', 'enterprise'],
                'description': 'Must be from predefined team size categories'
            },
            '[INSERT_CI_CD_PLATFORM]': {
                'type': 'enum',
                'allowed_values': ['GitHub Actions', 'Jenkins', 'GitLab CI', 'Azure DevOps', 'CircleCI', 'Travis CI', 'Bitbucket Pipelines'],
                'description': 'Must be from supported CI/CD platforms'
            }
        }
        
        self.dangerous_patterns = [
            (r'(cmd|bash|sh|exec|eval|system)\s*[\(\[]', 'Command execution patterns'),
            (r'<script[^>]*>|javascript:|on\w+\s*=', 'Script injection patterns'),
            (r'\.\./|\.\.\\|\\\\\.\.|%2e%2e', 'Path traversal patterns'),
            (r'\$\{|\$\(|%\w+%|`[^`]*`', 'Variable expansion patterns'),
            (r'<[^>]+>|&\w+;', 'HTML/XML injection patterns'),
            (r'[\'"`;|&]', 'Dangerous special characters')
        ]
    
    def validate_value(self, placeholder: str, value: str) -> Tuple[bool, List[str]]:
        errors = []
        
        # Basic validation
        if not value or not value.strip():
            errors.append('Value cannot be empty')
            return False, errors
            
        # Length validation  
        if len(value) > 100:
            errors.append('Value exceeds maximum length of 100 characters')
            
        # Character whitelist validation
        if not re.match(r'^[a-zA-Z0-9\s\-_.+]+$', value):
            errors.append('Value contains forbidden characters (only alphanumeric, space, -, _, ., + allowed)')
            
        # Dangerous pattern detection
        for pattern, description in self.dangerous_patterns:
            if re.search(pattern, value, re.IGNORECASE):
                errors.append(f'Value contains {description.lower()}')
                
        # Placeholder-specific validation
        if placeholder in self.validation_rules:
            rule = self.validation_rules[placeholder]
            
            if rule.get('type') == 'enum':
                if value not in rule['allowed_values']:
                    errors.append(f'Value must be one of: {", ".join(rule["allowed_values"])}')
                    
            elif 'pattern' in rule:
                if not re.match(rule['pattern'], value):
                    errors.append(f'Value does not match required pattern: {rule["description"]}')
                    
            if 'min_length' in rule and len(value) < rule['min_length']:
                errors.append(f'Value must be at least {rule["min_length"]} characters')
                
            if 'max_length' in rule and len(value) > rule['max_length']:
                errors.append(f'Value must be at most {rule["max_length"]} characters')
        
        return len(errors) == 0, errors

def main():
    if len(sys.argv) < 3:
        print('Usage: python3 validate_placeholders.py <placeholder> <value>')
        print('Example: python3 validate_placeholders.py "[INSERT_PROJECT_NAME]" "MyApp"')
        sys.exit(1)
        
    placeholder = sys.argv[1]
    value = sys.argv[2]
    
    validator = PlaceholderValidator()
    is_valid, errors = validator.validate_value(placeholder, value)
    
    if is_valid:
        print(f'✅ VALID: {placeholder} = "{value}"')
        sys.exit(0)
    else:
        print(f'❌ INVALID: {placeholder} = "{value}"')
        for error in errors:
            print(f'   - {error}')
        sys.exit(1)

if __name__ == '__main__':
    main()