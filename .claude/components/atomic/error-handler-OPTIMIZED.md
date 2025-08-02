# Error Handler Component

**Purpose**: Handle errors gracefully with clear messages and recovery guidance for any component that might fail.

**Usage**: 
- Identify error type (user input, system, logic)
- Provide clear, actionable error messages to users
- Suggest specific next steps to resolve issues
- Log errors for debugging and pattern analysis

**Compatibility**: 
- **Works with**: api-caller, file-reader, data-transformer, response-validator
- **Requires**: Error input from any component
- **Conflicts**: user-confirmation (overlapping interaction patterns)

**Implementation**:
```pseudocode
if error_occurs:
    error_type = categorize_error(error)
    user_message = create_clear_message(error_type)
    recovery_steps = suggest_resolution(error_type)
    log_error(error, context)
    return {message: user_message, steps: recovery_steps}
```

**Category**: atomic | **Complexity**: simple | **Time**: 15 minutes