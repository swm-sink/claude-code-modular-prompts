# Command Validation Checklist

## Command Information
- **Command Name**: `/command-name`
- **File Path**: `.claude/commands/[category]/[name].md`
- **Category**: [core/specialized/development/quality]
- **Purpose**: [What problem does this command solve?]
- **Target Users**: [Who should use this command?]

## Structural Validation

### ✅ YAML Front Matter
- [ ] Contains required `name` field with slash prefix (e.g., `name: /command-name`)
- [ ] Contains required `description` field (concise, under 100 chars)
- [ ] Contains `argument-hint` field with clear parameter guidance
- [ ] Contains `allowed-tools` field with appropriate Claude Code tools
- [ ] Optional fields present: `usage`, `category`, `examples`

### ✅ Markdown Structure  
- [ ] Has clear H1 title matching command name
- [ ] Has concise purpose statement after title
- [ ] Has Usage section with bash code examples
- [ ] Has Arguments/Parameters section (if applicable)
- [ ] Has Examples section with realistic use cases

### ✅ XML Command Structure
- [ ] Has proper `<command_file>` root element
- [ ] Contains `<metadata>` section with name, purpose, usage
- [ ] Contains `<arguments>` section for parameter definitions
- [ ] Contains `<examples>` section with usage demonstrations
- [ ] Contains `<claude_prompt>` section with actual implementation

## Content Validation

### ✅ Command Implementation
- [ ] Claude prompt is clear and actionable
- [ ] Process steps are logical and complete
- [ ] Implementation strategy is well-defined
- [ ] Command solves a real problem efficiently

### ✅ Component Integration
- [ ] Uses appropriate standard components (validation, error handling)
- [ ] Component includes are valid and exist
- [ ] Component usage enhances command functionality
- [ ] No unnecessary or redundant component includes

### ✅ Tool Usage
- [ ] Lists only required Claude Code tools in allowed-tools
- [ ] Tool usage is appropriate for command purpose
- [ ] Tool permissions match command functionality
- [ ] No excessive or unnecessary tool permissions

## Functional Validation

### ✅ Command Execution Testing
```bash
# Test 1: Basic Command Loading
echo "Testing command loads without errors..."
# Load command in Claude Code and verify no syntax errors

# Test 2: Parameter Validation  
echo "Testing command with various parameters..."
# Test with valid parameters
# Test with invalid parameters
# Test with edge cases

# Test 3: Tool Integration
echo "Testing tool usage..."
# Verify command can access required tools
# Test tool operations work as expected
```

### ✅ Integration Testing
- [ ] Command works with other commands in workflows
- [ ] Command doesn't conflict with existing commands
- [ ] Command integrates properly with Claude Code session management
- [ ] Command respects Claude Code configuration and settings

### ✅ Error Handling
- [ ] Command handles invalid input gracefully
- [ ] Command provides clear error messages
- [ ] Command fails safely without corrupting state
- [ ] Command recovery options are available

## Quality Standards

### ✅ User Experience
- [ ] Command purpose is immediately clear
- [ ] Command arguments are intuitive and well-documented
- [ ] Command provides helpful feedback during execution
- [ ] Command output is clear and actionable

### ✅ Performance Standards
- [ ] Command loads quickly (< 2 seconds)
- [ ] Command execution completes in reasonable time
- [ ] Command doesn't consume excessive resources
- [ ] Command prompt size is optimized (< 10k tokens recommended)

### ✅ Documentation Quality
- [ ] Examples are realistic and helpful
- [ ] Usage instructions are complete and accurate
- [ ] Parameter documentation is clear and comprehensive
- [ ] Command benefits and use cases are well-explained

## Security Validation

### ✅ Security Review
- [ ] Command doesn't expose sensitive information
- [ ] Command input validation prevents injection attacks
- [ ] Command follows principle of least privilege (minimal tools)
- [ ] Command doesn't create security vulnerabilities

### ✅ Safety Validation
- [ ] Command doesn't perform destructive operations without confirmation
- [ ] Command has appropriate safeguards for dangerous operations
- [ ] Command validates file paths and permissions appropriately
- [ ] Command handles concurrent access safely

## Compatibility Testing

### ✅ Claude Code Integration
- [ ] Command works with current Claude Code version
- [ ] Command respects Claude Code hooks and configuration
- [ ] Command integrates with Claude Code memory management
- [ ] Command works in different operating environments

### ✅ Component Compatibility
| Component | Used | Compatible | Issues | Notes |
|-----------|------|------------|--------|-------|
| validation-framework.md | ✅/❌ | ✅/❌ | [list] | [notes] |
| error-handling.md | ✅/❌ | ✅/❌ | [list] | [notes] |
| progress-reporting.md | ✅/❌ | ✅/❌ | [list] | [notes] |

## Performance Metrics

### ✅ Benchmarking Results
- **Load Time**: [X.X seconds]
- **Execution Time**: [X.X seconds for typical usage]
- **Memory Usage**: [XXX MB peak]
- **Prompt Size**: [XXXX tokens]
- **Component Count**: [X components included]

### ✅ Optimization Opportunities
- [ ] Prompt can be shortened without losing functionality
- [ ] Component usage can be optimized
- [ ] Tool usage can be minimized
- [ ] Performance bottlenecks identified and addressed

## Real-World Testing

### ✅ User Acceptance Testing
- [ ] Command tested by intended user types
- [ ] Command solves real problems effectively
- [ ] Command is intuitive for new users
- [ ] Command integrates well into typical workflows

### ✅ Edge Case Testing
- [ ] Command handles empty/null inputs appropriately
- [ ] Command works with very large inputs
- [ ] Command handles network/resource failures gracefully
- [ ] Command works across different project types

## Validation Results

### Issues Found
1. **Critical Issues**: [List critical issues that block approval]
2. **High Priority Issues**: [List important issues needing fixes]
3. **Medium Priority Issues**: [List moderate issues for improvement]
4. **Low Priority Issues**: [List minor enhancement opportunities]

### Recommendations
- [List specific recommendations for improvement]
- [Include priority levels and estimated effort]
- [Suggest alternative approaches if needed]

### Final Assessment
- [ ] **APPROVED FOR PRODUCTION** - Command meets all quality standards
- [ ] **CONDITIONAL APPROVAL** - Command approved with minor fixes required
- [ ] **NEEDS REWORK** - Command requires significant improvements before approval
- [ ] **DEPRECATED** - Command should be removed or replaced

### Validation Details
- **Validation Date**: [YYYY-MM-DD]
- **Validator**: [Name/Role]
- **Claude Code Version**: [Version tested with]
- **Test Environment**: [OS, setup details]
- **Next Review Date**: [YYYY-MM-DD]

### Sign-off
- [ ] Technical Review Complete
- [ ] Security Review Complete
- [ ] User Experience Review Complete
- [ ] Performance Review Complete
- [ ] Documentation Review Complete