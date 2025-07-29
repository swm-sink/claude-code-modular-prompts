# Testing Methodology

## Overview

This testing framework provides structural validation for the Claude Code Modular Prompts experimental framework. The focus is on validating command structure, YAML front matter, and basic content requirements rather than functional testing.

## Scope

### What We Test
- **YAML Front Matter**: Validates presence and structure of required metadata
- **Required Fields**: Ensures name, description, and other essential fields exist
- **File Structure**: Verifies proper markdown format and basic content structure
- **Content Length**: Checks for reasonable command content (not empty files)

### What We Don't Test
- **Functional Behavior**: Commands are not executed or tested for functionality
- **Performance**: No performance benchmarks (experimental framework focus)
- **Integration**: No testing of command interaction with Claude Code runtime
- **Security**: No security validation (handled by Claude Code platform)

## Validation Approach

### Structural Validation
The validation script checks each command file for:
1. Valid YAML front matter delimited by `---`
2. Required fields: `name`, `description`
3. Optional fields: `usage`, `tools`, `category`
4. Minimum content length outside front matter
5. Basic markdown structure

### Command Categories
- **Active Commands**: Currently maintained and functional
- **Deprecated Commands**: Marked for archival but structurally validated
- **Core Commands**: Essential commands that receive priority validation

## Usage Examples

### Validate Single Command
```bash
./tests/validate-command.sh .claude/commands/core/query.md
```

### Validate Directory
```bash
find .claude/commands -name "*.md" -exec ./tests/validate-command.sh {} \;
```

### Validation Output
- ✅ PASS: File meets structural requirements
- ❌ FAIL: File fails validation with specific error details
- Summary statistics for batch validation

## Limitations

1. **No Functional Testing**: This framework validates structure only
2. **Experimental Focus**: Designed for prompt engineering research, not production validation
3. **Static Analysis**: No runtime or dynamic testing capabilities
4. **Basic Validation**: Checks essential structure but not complex content requirements

## Integration with UltraThink

This testing framework supports the UltraThink finalization process by:
- Providing baseline quality assurance for command structure
- Identifying structurally invalid commands that need attention
- Supporting the experimental framework's focus on prompt effectiveness
- Enabling systematic validation of the 102 total commands (64 active, 38 deprecated)

## Maintenance

The testing methodology should be updated as the experimental framework evolves:
- Add new required fields as they are defined
- Update validation rules for new command categories
- Expand scope as framework maturity increases
- Document validation results for quality tracking

---
*Testing Methodology v1.0*  
*UltraThink Finalization Framework*  
*Experimental Prompt Engineering Research*