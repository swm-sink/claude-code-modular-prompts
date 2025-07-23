---
name: /docs-generate
description: Automated documentation generation with intelligent content creation and validation
usage: /docs-generate [doc_type] [output_format]
tools: Read, Write, Edit, Bash, Grep
---

# Automated documentation generation with intelligent content creation and validation

**Usage**: `/docs-generate $TARGET`

## Key Arguments

- **$TARGET** (optional): The source directory to scan for code to document.

## Examples

```bash
/docs generate
```
*Generate documentation for all code in the default 'src' directory.*

```bash
/docs generate target="./src/components"
```
*Generate documentation for a specific component directory.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/actions/apply-code-changes.md
 components/analysis/codebase-discovery.md
 components/context/find-relevant-code.md
 components/documentation/content-generation.md
 components/documentation/example-generation.md
 
 You are a technical writer. The user wants to automatically generate documentation from their source code.

 1. **Analyze Code**: Scan the `target` directory to analyze the code. Extract information such as:
 * Class and function signatures.
 * Docstrings and comments.
 * Dependencies and relationships between modules.
 2. **Generate Content**:
 * For each major class or module, create a clear explanation of its purpose.
 * For each public function, document its parameters, return value, and purpose.
 * Intelligently generate clear usage examples based on the code's structure and any associated tests.
 3. **Assemble Documentation**:
 * Format the generated content into a well-structured Markdown file.
 * Apply the documentation style guide defined in `PROJECT_CONFIG.xml`.
 * Propose the new documentation file to the user.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

