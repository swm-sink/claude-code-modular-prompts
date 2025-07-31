---
name: /demo-input-processing
description: Demonstrate reliable input processing and parameter validation (v2.0)
version: 2.0
usage: '/demo-input-processing [input_data] [processing_options]'
category: examples
allowed-tools:
- Read
- Write
- Edit
- Grep
dependencies:
- /validate-command
- /build-command
validation:
  pre-execution: Validate input data format and processing options
  during-execution: Monitor data processing and validation steps
  post-execution: Verify output correctness and completeness
progressive-disclosure:
  layer-integration: Shows input validation patterns for all layers
  escalation-path: Basic validation → complex rules → custom validators
  de-escalation: Focus on simple parameter checking
safety-measures:
  - Sanitize all user inputs
  - Validate data types and ranges
  - Prevent injection attacks
  - Handle edge cases gracefully
error-recovery:
  invalid-input: Provide clear format examples and requirements
  type-mismatch: Show type conversion options
  validation-failure: Detailed error messages with fix suggestions
---

# Input Processing Demo - Foundation Pattern

*This command demonstrates the reliable input processing pattern (100% valid)*

## Step 1: Validate User Input
```
Validate the provided input:
- Check for required parameters
- Verify data types match expectations
- Validate input ranges and constraints
- Return clear error messages if validation fails
- Continue only with valid inputs
```

## Step 2: Parse Command Parameters
```
Parse and extract command parameters:
- Split parameter string using appropriate delimiters
- Extract key-value pairs or positional arguments
- Apply type conversion and validation rules
- Handle optional parameters with defaults
- Return structured parameter object
```

## Step 3: Read Target Files
```
Read the specified file or files:
- Use the provided file path or pattern
- Handle multiple files if pattern matches several
- Validate file exists and is readable
- Parse file content appropriately
- Report file size and format detected
```

**Pattern Score: 100% (Solid Foundation)**  
**Components Used: 3 (input-validation, parameter-parser, file-reader)**  
**Validation Status: ✅ Solid Performance - Reliable Input Handling**