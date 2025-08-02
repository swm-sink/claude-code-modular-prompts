# User Confirmation Component

**Purpose**: Request explicit user confirmation before destructive actions with clear impact explanation.

**Usage**: 
- Clearly explain what action will be performed and its consequences
- List all affected files, resources, and potential risks
- Ask for explicit user confirmation with clear yes/no prompt
- Handle user responses and cancellation gracefully
- Provide undo information when possible for destructive actions

**Compatibility**: 
- **Works with**: error-handler, file-writer, git-operations (for destructive operations)
- **Requires**: Action description and list of affected resources
- **Conflicts**: completion-tracker, data-transformer (automated processing conflicts)

**Implementation**:
```pseudocode
action = describe_destructive_action()
affected = list_affected_resources()
risk_level = assess_action_risk_level()
display_confirmation_prompt(action, affected, risk_level)
response = wait_for_explicit_user_confirmation()
return {confirmed: boolean, user_response: response, proceed: boolean}
```

**Category**: atomic | **Complexity**: simple | **Time**: 30 minutes