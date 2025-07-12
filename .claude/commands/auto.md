# Auto Command

Intelligent routing with framework selection and optimal command routing.

## Instructions

Analyze the request and route to the optimal command for: $ARGUMENTS

1. **Request Analysis**: Understand the intent, scope, and complexity of the request.

2. **Framework Selection**: Choose the most appropriate framework (RISE, TRACE, CARE, etc.).

3. **Command Routing**: Route to the optimal command based on analysis:
   - Simple tasks → /task
   - Multi-component → /swarm  
   - Research needed → /query
   - Documentation → /docs
   - Sessions → /session

4. **Execution**: Execute the selected command with framework integration.

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