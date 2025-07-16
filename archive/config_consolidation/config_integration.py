#!/usr/bin/env python3
"""
Configuration Integration Tool for Claude Code Modular Prompts Framework

Integrates PROJECT_CONFIG.xml loading and template resolution into existing
commands and modules, enabling dynamic configuration without modifying core files.

Author: Claude Code Framework
Version: 1.0.0
Date: 2025-07-11
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging
from template_resolver import TemplateResolver


class ConfigIntegrator:
    """
    Integrates configuration loading capabilities into framework commands and modules.
    """
    
    def __init__(self, framework_root: Optional[str] = None):
        """
        Initialize configuration integrator.
        
        Args:
            framework_root: Path to framework root directory (default: detected automatically)
        """
        if framework_root:
            self.framework_root = Path(framework_root)
        else:
            # Auto-detect framework root by looking for .claude directory
            current = Path.cwd()
            while current != current.parent:
                if (current / '.claude').exists():
                    self.framework_root = current
                    break
                current = current.parent
            else:
                self.framework_root = Path.cwd()
        
        self.claude_dir = self.framework_root / '.claude'
        self.commands_dir = self.claude_dir / 'prompt_eng' / 'commands'
        self.modules_dir = self.claude_dir / 'modules'
        
        self.logger = logging.getLogger(__name__)
        
        # Configuration sections that commonly need integration
        self.config_integration_points = {
            'commands': {
                'placeholders': [
                    '[PROJECT_CONFIG: commands.test | DEFAULT: npm test]',
                    '[PROJECT_CONFIG: commands.lint | DEFAULT: npm run lint]',
                    '[PROJECT_CONFIG: commands.build | DEFAULT: npm run build]',
                    '[PROJECT_CONFIG: source_directory | DEFAULT: src]',
                    '[PROJECT_CONFIG: test_directory | DEFAULT: tests]',
                    '[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]'
                ]
            },
            'modules': {
                'placeholders': [
                    '[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]',
                    '[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]',
                    '[PROJECT_CONFIG: quality_standards.enforcement | DEFAULT: BLOCKING]'
                ]
            }
        }
    
    def scan_files_for_hardcoded_values(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Scan framework files for hardcoded values that should be configurable.
        
        Returns:
            Dictionary of files and their hardcoded values
        """
        results = {}
        
        # Patterns to look for that indicate hardcoded values
        hardcoded_patterns = [
            (r'\b90%?\b', 'test coverage threshold'),
            (r'\b200ms\b', 'response time threshold'),
            (r'\bsrc\b(?=\s*(directory|folder))', 'source directory'),
            (r'\btests?\b(?=\s*(directory|folder))', 'test directory'),
            (r'\bnpm\s+test\b', 'test command'),
            (r'\bnpm\s+run\s+lint\b', 'lint command'),
            (r'\bnpm\s+run\s+build\b', 'build command')
        ]
        
        # Scan command files
        if self.commands_dir.exists():
            for file_path in self.commands_dir.rglob('*.md'):
                matches = self._scan_file_for_patterns(file_path, hardcoded_patterns)
                if matches:
                    results[str(file_path)] = matches
        
        # Scan module files
        if self.modules_dir.exists():
            for file_path in self.modules_dir.rglob('*.md'):
                matches = self._scan_file_for_patterns(file_path, hardcoded_patterns)
                if matches:
                    results[str(file_path)] = matches
        
        return results
    
    def _scan_file_for_patterns(self, file_path: Path, patterns: List[tuple]) -> List[Dict[str, Any]]:
        """Scan a single file for hardcoded patterns."""
        matches = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                for pattern, description in patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        matches.append({
                            'line': line_num,
                            'content': line.strip(),
                            'pattern': pattern,
                            'description': description,
                            'suggested_replacement': self._suggest_replacement(pattern, description)
                        })
        
        except Exception as e:
            self.logger.warning(f"Error scanning {file_path}: {e}")
        
        return matches
    
    def _suggest_replacement(self, pattern: str, description: str) -> str:
        """Suggest a configuration placeholder replacement."""
        replacements = {
            'test coverage threshold': '[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%',
            'response time threshold': '[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]',
            'source directory': '[PROJECT_CONFIG: source_directory | DEFAULT: src]',
            'test directory': '[PROJECT_CONFIG: test_directory | DEFAULT: tests]',
            'test command': '[PROJECT_CONFIG: commands.test | DEFAULT: npm test]',
            'lint command': '[PROJECT_CONFIG: commands.lint | DEFAULT: npm run lint]',
            'build command': '[PROJECT_CONFIG: commands.build | DEFAULT: npm run build]'
        }
        
        return replacements.get(description, f'[PROJECT_CONFIG: {description.replace(" ", "_")} | DEFAULT: original_value]')
    
    def generate_integration_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive integration report.
        
        Returns:
            Report dictionary with integration opportunities and recommendations
        """
        report = {
            'framework_root': str(self.framework_root),
            'scan_timestamp': '2025-07-11',
            'hardcoded_values': {},
            'integration_opportunities': [],
            'priority_files': [],
            'recommendations': []
        }
        
        # Scan for hardcoded values
        hardcoded_results = self.scan_files_for_hardcoded_values()
        report['hardcoded_values'] = hardcoded_results
        
        # Analyze integration opportunities
        for file_path, matches in hardcoded_results.items():
            if len(matches) >= 3:  # Files with many hardcoded values are high priority
                report['priority_files'].append({
                    'file': file_path,
                    'match_count': len(matches),
                    'reason': 'Multiple hardcoded values found'
                })
        
        # Generate recommendations
        if hardcoded_results:
            report['recommendations'].extend([
                "Replace hardcoded values with PROJECT_CONFIG placeholders",
                "Create PROJECT_CONFIG.xml template for this project type",
                "Test configuration resolution with different project setups",
                "Document configuration options for users"
            ])
        
        # Check for existing configuration integration
        resolver = TemplateResolver(project_root=str(self.framework_root))
        validation_result = resolver.validate_configuration()
        
        if not validation_result['config_found']:
            report['recommendations'].append("Create PROJECT_CONFIG.xml to enable configuration features")
        
        return report
    
    def apply_integration_to_file(self, file_path: str, replacements: List[Dict[str, str]]) -> bool:
        """
        Apply configuration integration to a specific file.
        
        Args:
            file_path: Path to file to modify
            replacements: List of replacement dictionaries with 'from' and 'to' keys
            
        Returns:
            True if modifications were made successfully
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            self.logger.error(f"File not found: {file_path}")
            return False
        
        try:
            # Read original content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply replacements
            for replacement in replacements:
                content = content.replace(replacement['from'], replacement['to'])
            
            # Only write if changes were made
            if content != original_content:
                # Create backup
                backup_path = file_path.with_suffix(file_path.suffix + '.backup')
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
                
                # Write modified content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.logger.info(f"Applied configuration integration to {file_path}")
                self.logger.info(f"Backup created at {backup_path}")
                return True
            else:
                self.logger.info(f"No changes needed for {file_path}")
                return False
        
        except Exception as e:
            self.logger.error(f"Error applying integration to {file_path}: {e}")
            return False
    
    def create_integration_guide(self) -> str:
        """
        Create a comprehensive integration guide.
        
        Returns:
            Markdown content for integration guide
        """
        guide = """# Configuration Integration Guide

This guide explains how to integrate PROJECT_CONFIG.xml loading into Claude Code Framework commands and modules.

## Overview

The configuration integration system allows commands and modules to dynamically load project-specific settings without modifying core framework files.

## Placeholder Syntax

Use this syntax in commands and modules:
```
[PROJECT_CONFIG: path.to.value | DEFAULT: fallback_value]
```

### Examples

```markdown
# Test Coverage
Coverage must be [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% or higher

# Commands  
Run tests with [PROJECT_CONFIG: commands.test | DEFAULT: npm test]

# Directories
Source files in [PROJECT_CONFIG: source_directory | DEFAULT: src]
```

## Common Integration Points

### Commands
- Test commands: `[PROJECT_CONFIG: commands.test | DEFAULT: npm test]`
- Build commands: `[PROJECT_CONFIG: commands.build | DEFAULT: npm run build]`
- Lint commands: `[PROJECT_CONFIG: commands.lint | DEFAULT: npm run lint]`

### Quality Gates
- Test coverage: `[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]`
- Performance: `[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]`
- Enforcement: `[PROJECT_CONFIG: quality_standards.enforcement | DEFAULT: BLOCKING]`

### Project Structure
- Source directory: `[PROJECT_CONFIG: source_directory | DEFAULT: src]`
- Test directory: `[PROJECT_CONFIG: test_directory | DEFAULT: tests]`
- Docs directory: `[PROJECT_CONFIG: docs_directory | DEFAULT: docs]`

## Integration Process

1. **Scan for hardcoded values**
   ```bash
   python scripts/framework/config_integration.py --scan
   ```

2. **Generate integration report**
   ```bash
   python scripts/framework/config_integration.py --report
   ```

3. **Apply integration to specific files**
   ```bash
   python scripts/framework/config_integration.py --integrate file.md
   ```

## Best Practices

1. **Always provide defaults** - Ensure framework works without configuration
2. **Use descriptive paths** - Make configuration paths self-documenting
3. **Test with different configs** - Verify integration works across project types
4. **Document new placeholders** - Update this guide when adding new integration points

## Validation

Use the template resolver to validate integration:
```bash
python scripts/framework/template_resolver.py --validate
```

## Troubleshooting

### Placeholder not resolving
- Check placeholder syntax
- Verify PROJECT_CONFIG.xml exists
- Confirm configuration path is correct

### Default values not working
- Ensure proper DEFAULT syntax
- Check for typos in placeholder

### Performance issues
- Template resolver includes caching
- Avoid excessive placeholder nesting
"""
        return guide


def main():
    """CLI interface for configuration integration."""
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description="Configuration Integration Tool")
    parser.add_argument('--framework-root', help="Framework root directory")
    parser.add_argument('--scan', action='store_true', help="Scan for hardcoded values")
    parser.add_argument('--report', action='store_true', help="Generate integration report")
    parser.add_argument('--integrate', help="Apply integration to specific file")
    parser.add_argument('--guide', action='store_true', help="Generate integration guide")
    parser.add_argument('--output', help="Output file for report or guide")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    integrator = ConfigIntegrator(framework_root=args.framework_root)
    
    try:
        if args.scan:
            results = integrator.scan_files_for_hardcoded_values()
            if results:
                print("Hardcoded values found:")
                for file_path, matches in results.items():
                    print(f"\n{file_path}:")
                    for match in matches:
                        print(f"  Line {match['line']}: {match['description']}")
                        print(f"    Current: {match['content']}")
                        print(f"    Suggested: {match['suggested_replacement']}")
            else:
                print("No hardcoded values found")
        
        elif args.report:
            report = integrator.generate_integration_report()
            
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(report, f, indent=2)
                print(f"Integration report saved to {args.output}")
            else:
                print(json.dumps(report, indent=2))
        
        elif args.guide:
            guide = integrator.create_integration_guide()
            
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(guide)
                print(f"Integration guide saved to {args.output}")
            else:
                print(guide)
        
        elif args.integrate:
            print(f"Integration functionality for {args.integrate} requires manual review")
            print("Use --scan first to identify integration opportunities")
        
        else:
            parser.print_help()
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())