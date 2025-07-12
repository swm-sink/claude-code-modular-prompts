# Auto Command

Intelligent routing with framework selection and optimal command routing.

## Instructions

Analyze the request and route to the optimal command for: $ARGUMENTS

1. **Request Analysis**: Understand the intent, scope, and complexity of the request.
   - **Atomic Checkpoint**: `git add -A && git commit -m "AUTO ANALYSIS: [request] - intent and complexity analyzed"`

2. **Framework Selection**: Choose the most appropriate framework (RISE, TRACE, CARE, etc.).
   - **Atomic Checkpoint**: `git add -A && git commit -m "AUTO FRAMEWORK: [selected_framework] - framework selection optimized"`

3. **Command Routing**: Route to the optimal command based on analysis:
   - Simple tasks → /task
   - Multi-component → /swarm  
   - Research needed → /query
   - Documentation → /docs
   - Sessions → /session
   - **Atomic Checkpoint**: `git add -A && git commit -m "AUTO ROUTING: [selected_command] - intelligent routing decision made"`

4. **Execution**: Execute the selected command with framework integration.
   - **Delegated Atomic Safety**: Selected command inherits atomic commit capabilities
   - **Final Checkpoint**: `git add -A && git commit -m "AUTO COMPLETE: [operation] - intelligent routing and execution successful"`

## Routing Logic

- **Single file/component + clear requirements** → /task
- **Multiple files/components** → /swarm
- **Need to understand codebase first** → /query
- **Generate documentation** → /docs
- **Long-running complex work** → /session

## Examples

- `/auto "Add user login"` - Analyzes scope, likely routes to /swarm
- `/auto "Fix this bug"` - Analyzes context, likely routes to /task
- `/auto "Understand the auth system"` - Routes to /query