#!/usr/bin/env python3
"""
Prompt Validation Tool
Validates prompt files against the JSON schema and naming conventions
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import argparse
from jsonschema import validate, ValidationError, Draft7Validator

class PromptValidator:
    """Validates prompt files for the Claude Code framework"""
    
    def __init__(self, schema_path: Path):
        """Initialize with schema"""
        with open(schema_path, 'r') as f:
            self.schema = json.load(f)
        self.validator = Draft7Validator(self.schema)
        
        # Naming patterns
        self.filename_pattern = re.compile(
            r'^[a-z]+(-[a-z0-9]+)*-v\d+\.\d+\.\d+\.json$'
        )
        self.id_pattern = re.compile(r'^[a-z0-9-]+$')
        self.version_pattern = re.compile(r'^\d+\.\d+\.\d+$')
        self.tag_pattern = re.compile(r'^[a-z0-9-]+$')
        
        # Valid categories
        self.valid_categories = {'queries', 'features', 'reviews', 'patterns', 'templates'}
    
    def validate_prompt(self, prompt_path: Path) -> Tuple[bool, List[str]]:
        """Validate a single prompt file"""
        errors = []
        
        # Check file exists
        if not prompt_path.exists():
            return False, [f"File not found: {prompt_path}"]
        
        # Check filename
        filename_errors = self._validate_filename(prompt_path)
        errors.extend(filename_errors)
        
        # Load and validate JSON
        try:
            with open(prompt_path, 'r') as f:
                prompt_data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON: {e}")
            return False, errors
        
        # Validate against schema
        schema_errors = self._validate_schema(prompt_data)
        errors.extend(schema_errors)
        
        # Additional validations
        if not errors:  # Only if schema valid
            content_errors = self._validate_content(prompt_data, prompt_path)
            errors.extend(content_errors)
        
        return len(errors) == 0, errors
    
    def _validate_filename(self, path: Path) -> List[str]:
        """Validate filename follows conventions"""
        errors = []
        filename = path.name
        
        if not self.filename_pattern.match(filename):
            errors.append(
                f"Invalid filename format: {filename}. "
                f"Expected: <subcategory>-<name>-v<version>.json"
            )
        
        # Check that file is in a valid category directory
        parent_dir = path.parent.name
        if parent_dir not in self.valid_categories and parent_dir != 'prompts':
            # Only check if not in root prompts dir
            if path.parent.parent.name == 'prompts':
                if parent_dir not in self.valid_categories:
                    errors.append(
                        f"File must be in a valid category directory. "
                        f"Found in '{parent_dir}', expected one of: {', '.join(self.valid_categories)}"
                    )
        
        return errors
    
    def _validate_schema(self, data: Dict) -> List[str]:
        """Validate against JSON schema"""
        errors = []
        
        try:
            validate(instance=data, schema=self.schema)
        except ValidationError as e:
            errors.append(f"Schema validation error: {e.message}")
            # Get all errors
            for error in self.validator.iter_errors(data):
                path = ' -> '.join(str(p) for p in error.path)
                if path:
                    errors.append(f"  At {path}: {error.message}")
        
        return errors
    
    def _validate_content(self, data: Dict, path: Path) -> List[str]:
        """Additional content validations"""
        errors = []
        
        # Validate ID format
        if not self.id_pattern.match(data.get('id', '')):
            errors.append(
                f"Invalid ID format: {data.get('id')}. "
                f"Must be lowercase alphanumeric with hyphens"
            )
        
        # Validate version
        if not self.version_pattern.match(data.get('version', '')):
            errors.append(
                f"Invalid version format: {data.get('version')}. "
                f"Must follow semantic versioning (X.Y.Z)"
            )
        
        # Validate category matches directory
        parent_dir = path.parent.name
        if parent_dir != 'prompts':  # Only validate if in a category subdirectory
            if data.get('category') != parent_dir:
                errors.append(
                    f"Category mismatch: File is in '{parent_dir}' directory "
                    f"but content category is '{data.get('category')}'"
                )
        
        # Validate tags
        tags = data.get('metadata', {}).get('tags', [])
        for tag in tags:
            if not self.tag_pattern.match(tag):
                errors.append(f"Invalid tag format: {tag}")
        
        # Validate template variables
        template_errors = self._validate_template_variables(data)
        errors.extend(template_errors)
        
        # Validate dates
        date_errors = self._validate_dates(data)
        errors.extend(date_errors)
        
        return errors
    
    def _validate_template_variables(self, data: Dict) -> List[str]:
        """Validate template variables match definition"""
        errors = []
        
        template = data.get('prompt', {}).get('template', '')
        variables = data.get('prompt', {}).get('variables', [])
        
        # Extract variable names from template, excluding Handlebars helpers
        # Match simple variables: {{variable}} or {{variable|default:value}}
        simple_vars = re.findall(r'\{\{([^}|#/@]+?)(?:\|[^}]+)?\}\}', template)
        
        # Match conditionals: {{#if variable}} {{#each variable}}
        conditional_vars = re.findall(r'\{\{#(?:if|each|unless)\s+([^}]+?)\}\}', template)
        
        # Combine and clean up
        template_vars = set()
        for var in simple_vars + conditional_vars:
            # Remove 'this.' prefix and other Handlebars context variables
            if var and not var.startswith(('this', '@', '/')):
                # Clean up whitespace
                var = var.strip()
                if var:
                    template_vars.add(var)
        
        # Get defined variable names
        defined_vars = {var['name'] for var in variables}
        
        # Check for undefined variables
        undefined = template_vars - defined_vars
        if undefined:
            errors.append(
                f"Undefined variables in template: {', '.join(sorted(undefined))}"
            )
        
        # Check for unused variables (optional warning)
        unused = defined_vars - template_vars
        if unused and len(unused) < len(defined_vars):  # Only warn if some are used
            # This is just a warning, not an error
            pass  # Could add warning system later
        
        return errors
    
    def _validate_dates(self, data: Dict) -> List[str]:
        """Validate date formats"""
        errors = []
        
        metadata = data.get('metadata', {})
        
        # Check created date
        created = metadata.get('created')
        if created:
            try:
                datetime.fromisoformat(created.replace('Z', '+00:00'))
            except ValueError:
                errors.append(f"Invalid created date format: {created}")
        
        # Check updated date
        updated = metadata.get('updated')
        if updated:
            try:
                datetime.fromisoformat(updated.replace('Z', '+00:00'))
            except ValueError:
                errors.append(f"Invalid updated date format: {updated}")
        
        return errors
    
    def validate_directory(self, directory: Path) -> Dict[str, Tuple[bool, List[str]]]:
        """Validate all prompts in a directory"""
        results = {}
        
        for prompt_file in directory.glob('**/*.json'):
            if 'archived' in prompt_file.parts:
                continue  # Skip archived files
            if prompt_file.name == 'prompt-schema.json':
                continue  # Skip schema file
            
            valid, errors = self.validate_prompt(prompt_file)
            results[str(prompt_file)] = (valid, errors)
        
        return results


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Validate Claude Code prompt files'
    )
    parser.add_argument(
        'path',
        type=Path,
        help='Path to prompt file or directory'
    )
    parser.add_argument(
        '--schema',
        type=Path,
        default=Path(__file__).parent.parent / 'prompts' / 'prompt-schema.json',
        help='Path to JSON schema'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show all validation details'
    )
    
    args = parser.parse_args()
    
    # Initialize validator
    validator = PromptValidator(args.schema)
    
    # Validate based on path type
    if args.path.is_file():
        # Single file validation
        valid, errors = validator.validate_prompt(args.path)
        
        if valid:
            print(f"✅ {args.path.name} is valid")
            return 0
        else:
            print(f"❌ {args.path.name} has errors:")
            for error in errors:
                print(f"   - {error}")
            return 1
    
    elif args.path.is_dir():
        # Directory validation
        results = validator.validate_directory(args.path)
        
        total = len(results)
        valid_count = sum(1 for _, (valid, _) in results.items() if valid)
        
        print(f"\nValidation Results: {valid_count}/{total} valid\n")
        
        # Show invalid files
        invalid_files = [
            (path, errors) 
            for path, (valid, errors) in results.items() 
            if not valid
        ]
        
        if invalid_files:
            print("❌ Invalid files:")
            for path, errors in invalid_files:
                print(f"\n  {Path(path).name}:")
                for error in errors[:3]:  # Show first 3 errors
                    print(f"    - {error}")
                if len(errors) > 3:
                    print(f"    ... and {len(errors) - 3} more errors")
        
        # Show valid files if verbose
        if args.verbose:
            valid_files = [
                path for path, (valid, _) in results.items() if valid
            ]
            if valid_files:
                print("\n✅ Valid files:")
                for path in valid_files:
                    print(f"  - {Path(path).name}")
        
        return 0 if valid_count == total else 1
    
    else:
        print(f"Error: {args.path} is neither a file nor directory")
        return 2


if __name__ == '__main__':
    sys.exit(main())