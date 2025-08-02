# Request User Confirmation

**Purpose**: Ensure explicit user confirmation before proceeding with plans or actions, preventing unwanted changes and maintaining user control.

**Usage**: 
- Present clear plans or findings before requesting confirmation
- Ask direct yes/no questions about proceeding with next actions
- Stop execution and wait for positive user confirmation
- Clearly state what specific action will be taken next
- Provide opportunity for user to modify or reject proposed actions

**Compatibility**: 
- **Works with**: create-step-by-step-plan, workflow execution, user-confirmation (atomic)
- **Requires**: User interaction capability and clear action proposals
- **Conflicts**: automated-execution (breaks automation flow)

**Implementation**:
```python
# User confirmation request system
def request_confirmation(action_description, plan_summary=None):
    confirmation_request = UserConfirmationRequest()
    
    # Present the plan or findings clearly
    if plan_summary:
        confirmation_request.add_context("Plan Summary", plan_summary)
    
    # State the specific action to be taken
    confirmation_request.add_proposed_action(action_description)
    
    # Ask direct yes/no question
    confirmation_text = f"""
Based on the analysis above, I'm ready to proceed with the following action:

**Proposed Action**: {action_description}

Are you happy with this plan? Shall I proceed with the implementation?

Please respond with:
- "Yes" or "Proceed" to continue
- "No" or "Stop" to halt
- "Modify" to suggest changes
"""
    
    return confirmation_request.present_to_user(confirmation_text)

# Confirmation processing
def process_user_response(user_response):
    response = user_response.lower().strip()
    
    positive_responses = ['yes', 'y', 'proceed', 'continue', 'go ahead', 'ok', 'confirm']
    negative_responses = ['no', 'n', 'stop', 'halt', 'cancel', 'abort']
    modify_responses = ['modify', 'change', 'edit', 'update', 'revise']
    
    if any(pos in response for pos in positive_responses):
        return ConfirmationResult(action='proceed', confirmed=True)
    elif any(neg in response for neg in negative_responses):
        return ConfirmationResult(action='stop', confirmed=False, reason='User declined')
    elif any(mod in response for mod in modify_responses):
        return ConfirmationResult(action='modify', confirmed=False, reason='User requested modifications')
    else:
        # Ambiguous response - ask for clarification
        return ConfirmationResult(
            action='clarify', 
            confirmed=False, 
            reason='Response unclear, please respond with Yes/No/Modify'
        )

# Safety wrapper for actions requiring confirmation
def require_confirmation(action_description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Request confirmation before execution
            confirmation = request_confirmation(action_description)
            
            if not confirmation.confirmed:
                return ConfirmationResult(
                    action='cancelled',
                    message=f"Action cancelled: {confirmation.reason}"
                )
            
            # Proceed with action if confirmed
            try:
                result = func(*args, **kwargs)
                return ActionResult(success=True, result=result)
            except Exception as e:
                return ActionResult(success=False, error=str(e))
                
        return wrapper
    return decorator

# Example usage
@require_confirmation("Delete all temporary files and rebuild project")
def clean_and_rebuild_project():
    # Implementation would go here
    clean_temp_files()
    rebuild_project()
    return "Project cleaned and rebuilt successfully"
```

**Category**: interaction | **Complexity**: simple | **Time**: 30 minutes