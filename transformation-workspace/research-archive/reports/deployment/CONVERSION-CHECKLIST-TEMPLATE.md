# Manual Conversion Checklist Template - v1.0

## 📋 PRE-CONVERSION ANALYSIS

**Command File**: `________________________`  
**Category**: `________________________`  
**Original Purpose**: `________________________`

### Analysis Checklist:
- [ ] Read complete original command file
- [ ] Understand core functionality and workflow
- [ ] Identify existing parameters and usage patterns
- [ ] Note any special requirements or constraints
- [ ] Review existing examples or documentation
- [ ] Determine command complexity level (Simple/Medium/Complex)

## 🎯 CONVERSION EXECUTION

### Step 1: Enhanced YAML Frontmatter
```yaml
---
command: ________________________
description: ________________________ (enhanced with v1.0 capabilities)
category: ________________________
parameters: 
  - name: ________________________
    type: string/number/boolean
    required: true/false
    description: ________________________
usage_examples:
  - "/command ________________________"
  - "/command ________________________"
  - "/command ________________________"
prerequisites: 
  - "________________________"
  - "________________________"
output_format: structured/text/code/json
tags: [________________________, ________________________, v2-enhanced]
version: "1.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools: [________________________]
---
```

### Metadata Conversion Checklist:
- [ ] `command`: Extracted from original name field (removed leading /)
- [ ] `description`: Enhanced original description with v1.0 mention
- [ ] `category`: Determined from file location and purpose
- [ ] `parameters`: At least 1 parameter defined with type and description
- [ ] `usage_examples`: Minimum 3 realistic examples
- [ ] `prerequisites`: Environment and dependency requirements
- [ ] `output_format`: Appropriate for command purpose
- [ ] `tags`: Relevant categorization tags + "v2-enhanced"
- [ ] `version`: Set to "2.0"
- [ ] `author`: Set to "lusaka-template-library"
- [ ] `last_updated`: Today's date
- [ ] `allowed-tools`: Preserved from original

### Step 2: XML Structure Enhancement

#### Required XML Tags:
- [ ] `<context type="project">` - Project-specific context
- [ ] `<instructions>` - Procedural guidance with parameters
- [ ] `<examples>` - Structured input/output examples
- [ ] `<workflow type="sequential">` - Implementation phases
- [ ] `<automation trigger="completion">` - Post-execution steps

#### Content Structure:
```markdown
# [Original Title or Enhanced Title]

<context type="project">
[Command-specific context for lusaka template library - describe the domain/purpose]
</context>

<instructions>
[Procedural guidance using parameter substitution like $PARAMETER_NAME]
</instructions>

## Usage Examples

<examples>
<example>
<input>/command specific realistic input</input>
<expected_output>Detailed description of expected output</expected_output>
</example>
<example>
<input>/command different scenario</input>
<expected_output>Different expected output</expected_output>
</example>
<example>
<input>/command edge case or advanced usage</input>
<expected_output>Advanced output description</expected_output>
</example>
</examples>

## Implementation Workflow

<workflow type="sequential">
<task priority="high">
**[Phase Name]**: [Purpose of this phase]
- [Specific action 1]
- [Specific action 2]
- [Parameter usage: $PARAMETER_NAME]
</task>

<task priority="high/medium">
**[Phase Name]**: [Purpose of this phase]
- [Specific action 1]
- [Specific action 2]
</task>

<task priority="medium/low">
**[Phase Name]**: [Purpose of this phase]
- [Specific action 1]
- [Specific action 2]
</task>
</workflow>

<automation trigger="completion">
- [Command-specific validation steps]
- [Follow-up actions]
- [Documentation updates]
</automation>

## [Original Content Section if Valuable]

[Preserve original content that adds value]
```

### XML Structure Checklist:
- [ ] `<context>` provides project-specific background
- [ ] `<instructions>` uses parameter substitution ($PARAM)
- [ ] `<examples>` has 3 realistic input/output pairs
- [ ] `<workflow>` phases are logical and command-appropriate
- [ ] `<task>` priorities are assigned (high/medium/low)
- [ ] `<automation>` trigger is relevant to command
- [ ] All XML tags properly opened and closed
- [ ] XML syntax is valid (no parsing errors)

## ✅ POST-CONVERSION VALIDATION

### Quality Checks:
- [ ] YAML frontmatter syntax is valid
- [ ] All required v1.0 metadata fields present
- [ ] Parameters are referenced in instructions ($PARAM_NAME)
- [ ] Usage examples are realistic and varied
- [ ] XML structure is semantically meaningful
- [ ] Original functionality is preserved
- [ ] No broken references or missing content

### MCP Validator Check:
```bash
python scripts/mcp_template_validator.py validate_command [file_path]
```

### Validation Results:
- [ ] **Valid**: true/false
- [ ] **Version**: 2.0+ detected
- [ ] **Metadata Score**: ___/100 (target: 80+)
- [ ] **XML Tags**: ___ count (target: 5+)
- [ ] **Issues**: None or resolved
- [ ] **Warnings**: Addressed if critical

### Functional Testing:
- [ ] Command loads properly in Claude Code environment
- [ ] Parameters are recognized and processed
- [ ] Examples work as documented
- [ ] No error messages or failures
- [ ] Expected output format is produced

## 📊 CONVERSION METRICS

**Time Spent**: _______ minutes  
**Complexity Level**: Simple/Medium/Complex  
**Enhancements Added**: _____ v1.0 fields  
**XML Tags Added**: _____ semantic tags  
**Examples Created**: _____ usage examples  
**Issues Encountered**: _____________________  

## 📝 NOTES & LESSONS LEARNED

**Patterns That Worked**:
- _____________________
- _____________________

**Challenges Encountered**:
- _____________________
- _____________________

**Improvements for Next Conversion**:
- _____________________
- _____________________

## ✅ COMPLETION CHECKLIST

- [ ] All analysis completed
- [ ] Enhanced metadata implemented
- [ ] XML structure added and validated
- [ ] MCP validation passed
- [ ] Functional testing completed
- [ ] Metrics recorded
- [ ] Lessons documented
- [ ] File saved and backed up

**Conversion Status**: ⏳ In Progress / ✅ Complete / ❌ Issues Found  

---

*Conversion Checklist Template v1.0*  
*Use this template for every manual conversion to ensure consistency*