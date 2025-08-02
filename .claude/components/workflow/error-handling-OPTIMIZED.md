# Standardized Error Handling

**Purpose**: Implement consistent error handling, validation, and recovery patterns across all commands with clear user communication and graceful degradation.

**Usage**: 
- Classifies errors (system, user input, logic, external)
- Applies response patterns (immediate stop, graceful degradation, retry, fallback)
- Provides clear, actionable error messages with context
- Suggests resolution steps and recovery options
- Maintains helpful tone with partial functionality when possible

**Compatibility**: 
- **Works with**: All commands, error-handler, command-execution
- **Requires**: error_classification, recovery_strategies, user_communication
- **Conflicts**: None (universal error handling)

**Implementation**:
```markdown
🚨 Error Detected: [description]
📍 Context: [what was attempted]
🔍 Cause: [specific reason]
🛠️ Suggested Actions: [steps]
🔄 Recovery Options: [alternatives]
```

**Category**: workflow | **Complexity**: simple | **Time**: 30 minutes