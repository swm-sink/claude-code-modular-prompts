---
name: /docs-check
description: Advanced documentation validation with intelligent analysis, consistency checking, and quality assurance
usage: /docs-check [check_scope] [validation_level]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced documentation validation with intelligent analysis, consistency checking, and quality assurance

**Usage**: `/docs-check $CHECK_SCOPE $VALIDATION_LEVEL`

## Key Arguments

- **$CHECK_SCOPE** (optional): Scope of documentation to validate
- **$VALIDATION_LEVEL** (optional): Level of validation thoroughness

## Examples

```bash
/docs check all
```
*Check all documentation*

```bash
/docs check --consistency
```
*Consistency validation*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/quality/framework-validation.md
 components/reporting/generate-structured-report.md
 components/documentation/link-validation.md
 components/quality/readability-assessment.md
 components/documentation/consistency-checking.md
 
You are an advanced documentation validation specialist. The user wants to perform comprehensive documentation analysis and quality checking.

**Validation Process:**
1. **Content Analysis**: Analyze documentation content for accuracy and completeness
2. **Consistency Checking**: Verify consistency across documentation sections
3. **Quality Assessment**: Evaluate documentation quality and readability
4. **Link Validation**: Check internal and external links for validity
5. **Standards Compliance**: Ensure compliance with documentation standards

**Implementation Strategy:**
- Scan all documentation files for completeness and accuracy
- Validate cross-references and internal links
- Check code examples and technical accuracy
- Assess documentation structure and organization
- Generate comprehensive validation reports

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

