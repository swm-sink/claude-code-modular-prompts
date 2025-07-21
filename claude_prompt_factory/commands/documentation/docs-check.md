---
description: Comprehensive documentation validation with quality checks, consistency analysis, and improvement recommendations
argument-hint: "[check_scope] [output_format]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /docs check - Documentation Quality Validator

Advanced documentation validation system with quality assessment, consistency checking, and automated improvement recommendations.

## Usage
```bash
/docs check all                              # Complete documentation validation
/docs check quality                          # Focus on quality and consistency
/docs check links                            # Validate internal and external links
/docs check --format json                    # Output detailed JSON report
```

## Arguments
```bash
/docs check <target_directory="./docs">
```

## Examples
```bash
/docs check                              # Check all documentation in the default 'docs' directory.
/docs check target="./docs/guides"      # Check documentation within the 'guides' subdirectory.
```

## Dependencies
```bash
/docs check                              # Check all documentation in the default 'docs' directory.
/docs check target="./docs/guides"      # Check documentation within the 'guides' subdirectory.
```