---
name: /deps-update
description: Intelligent dependency updates with automated vulnerability scanning, compatibility validation, and rollback safety
usage: /deps-update [update_scope] [validation_level]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent dependency updates with automated vulnerability scanning, compatibility validation, and rollback safety

**Usage**: `/deps-update $UPDATE_SCOPE $VALIDATION_LEVEL`

## Key Arguments

- **$UPDATE_SCOPE** (optional): Scope of dependency updates to perform
- **$VALIDATION_LEVEL** (optional): Level of validation and safety checks

## Examples

```bash
/deps update security
```
*Security-focused dependency updates*

```bash
/deps update --automated
```
*Fully automated dependency management*

## Core Logic

You are an advanced dependency management specialist. The user wants to implement intelligent updates with vulnerability scanning and comprehensive safety validation.

**Update Process:**
1. **Dependency Analysis**: Analyze current dependencies and identify update candidates
2. **Security Scanning**: Perform comprehensive vulnerability and security scanning
3. **Compatibility Testing**: Validate compatibility and breaking change detection
4. **Automated Updates**: Execute intelligent updates with rollback mechanisms
5. **Validation & Monitoring**: Monitor updates and validate system stability

**Implementation Strategy:**
- Analyze dependency trees for security vulnerabilities and outdated packages
- Implement automated security scanning with vulnerability databases
- Apply intelligent compatibility testing and breaking change detection
- Create comprehensive rollback mechanisms and safety nets
- Establish continuous monitoring for dependency health and security

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

