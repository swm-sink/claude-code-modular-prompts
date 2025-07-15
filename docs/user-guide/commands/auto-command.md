# Auto Command Documentation

## Overview
The `/auto` command provides intelligent routing when you're uncertain about which command to use. It analyzes your request and automatically selects the most appropriate command and approach.

## When to Use `/auto`
- ✅ Unclear requirements or approach
- ✅ Complex decisions requiring analysis
- ✅ Route optimization between commands
- ✅ When you're unsure which command fits best

## When to Use Other Commands
- Use specific commands when you know exactly what you want
- Use `/query` when you only need research without modifications
- Use `/task` for clear single-component work
- Use `/feature` for clear multi-component features

## Usage Syntax
```bash
/auto "describe what you want to accomplish"
```

## How It Works
The framework will:
1. **Analyze request**: Understand the scope and complexity
2. **Evaluate options**: Consider all available commands
3. **Select optimal approach**: Choose the best command for the task
4. **Execute with reasoning**: Explain why this approach was chosen
5. **Adapt if needed**: Switch approaches if initial analysis was incorrect

## Decision Matrix

### Request Analysis Factors
- **Complexity**: Single component vs. multi-component
- **Scope**: Small change vs. new feature
- **Knowledge**: Understanding existing code vs. need research
- **Intent**: Research vs. implementation vs. documentation

### Routing Logic
```
Request Type → Command Selected
─────────────────────────────────────
"Fix bug in login" → /task
"Add user dashboard" → /feature  
"Understand auth flow" → /query
"Create shopping cart" → /feature
"Optimize database query" → /task
"How does payment work?" → /query
"Add social login" → /feature
"Write documentation" → /docs
```

## Example Walkthroughs

### Example 1: Unclear Scope
```bash
/auto "I need to improve the user experience for checkout"
```

**Analysis:**
```
🤔 ANALYZING REQUEST: "improve user experience for checkout"

📊 SCOPE ANALYSIS:
- Multiple components likely involved
- UX improvements suggest frontend + backend
- May require research into existing flow
- Could be enhancement or new feature

🎯 DECISION: /feature command selected
- Reason: UX improvements typically span multiple components
- Will start with PRD to define improvements
- Includes research, planning, and implementation

🚀 EXECUTING: /feature "improve user experience for checkout"
```

### Example 2: Technical Uncertainty
```bash
/auto "Something is wrong with the database queries in the product search"
```

**Analysis:**
```
🤔 ANALYZING REQUEST: "something wrong with database queries"

📊 SCOPE ANALYSIS:
- Problem identification needed first
- Could be single query or systemic issue
- Research required before solution
- Performance vs. correctness issue unclear

🎯 DECISION: /query command selected first
- Reason: Need to understand the problem before fixing
- Will analyze existing query patterns
- Then route to appropriate fix command

🚀 EXECUTING: /query "analyze database query performance in product search"
```

### Example 3: Clear Implementation
```bash
/auto "Add email validation to the registration form"
```

**Analysis:**
```
🤔 ANALYZING REQUEST: "add email validation to registration form"

📊 SCOPE ANALYSIS:
- Single component (validation function)
- Clear requirement (email validation)
- Focused change to existing feature
- Implementation task, not research

🎯 DECISION: /task command selected
- Reason: Single, focused implementation
- Clear requirements for TDD approach
- Small scope with specific outcome

🚀 EXECUTING: /task "add email validation to registration form"
```

### Example 4: Complex Integration
```bash
/auto "We need to integrate with a new payment provider"
```

**Analysis:**
```
🤔 ANALYZING REQUEST: "integrate with new payment provider"

📊 SCOPE ANALYSIS:
- Multiple integration points
- Likely affects multiple components
- May require understanding existing payment flow
- New functionality spanning frontend/backend

🎯 DECISION: Multi-step approach selected
- Step 1: /query "analyze existing payment system integration"
- Step 2: /feature "integrate new payment provider"
- Reason: Complex integration requires understanding first

🚀 EXECUTING: /query "how does the current payment system work?"
```

## Decision Tree Examples

### Research vs. Implementation
```
Need to understand? → /query
Ready to implement? → /task or /feature
Unsure about both? → /auto
```

### Single vs. Multi-Component
```
Single file/function? → /task
Multiple components? → /feature
System-wide changes? → /swarm
```

### Documentation vs. Code
```
Need documentation? → /docs
Need code changes? → /task or /feature
Need both? → /auto (will orchestrate)
```

## Advanced Auto Behaviors

### Adaptive Routing
The auto command can change its approach based on discoveries:

```bash
/auto "Fix the slow API responses"
```

**Initial Analysis:**
```
🎯 STARTING: /query "identify API performance bottlenecks"

📊 FINDINGS: Multiple issues found
- Database N+1 queries in user endpoints
- Missing caching in product search
- Inefficient serialization in orders

🔄 ADAPTING: Switching to /swarm for coordination
- Multiple related but independent optimizations
- Can be worked on in parallel
- Requires coordination between components
```

### Context-Aware Decisions
```bash
/auto "The tests are failing after the recent changes"
```

**Analysis:**
```
🤔 ANALYZING CONTEXT:
- Recent changes detected in git history
- Test failures indicate regression
- Need to identify root cause first

🎯 DECISION: /query then /task sequence
- First: Understand what changed and why tests fail
- Then: Fix the specific issues found
```

## Key Learning Points

### ✅ What the Framework Does Well
- **Intelligent Analysis**: Understands request complexity and scope
- **Optimal Routing**: Selects the most appropriate command
- **Adaptive Behavior**: Changes approach based on discoveries
- **Clear Reasoning**: Explains why decisions were made
- **Multi-Step Orchestration**: Coordinates complex workflows

### 📚 Best Practices Demonstrated
1. **Think Before Acting**: Analyzes before selecting approach
2. **Scope Assessment**: Evaluates complexity and requirements
3. **Optimal Selection**: Chooses the best tool for the job
4. **Transparent Reasoning**: Explains decision-making process
5. **Adaptive Planning**: Adjusts approach based on findings

## Command Variations

### Specific Context
```bash
/auto "working on user authentication improvements"
```

### Problem-Focused
```bash
/auto "users are complaining about slow page loads"
```

### Feature-Focused
```bash
/auto "need to add real-time notifications"
```

### Research-Focused
```bash
/auto "need to understand how the caching system works"
```

## When Auto Might Choose Each Command

### Routes to /query
- "How does X work?"
- "What's causing the performance issue?"
- "Why are the tests failing?"
- "What's the architecture of Y?"

### Routes to /task
- "Fix the bug in X"
- "Add validation to Y"
- "Optimize the Z function"
- "Update the configuration"

### Routes to /feature
- "Add user dashboard"
- "Implement shopping cart"
- "Create notification system"
- "Build search functionality"

### Routes to /swarm
- "Optimize the entire application"
- "Refactor the architecture"
- "Implement microservices"
- "Add comprehensive testing"

### Routes to /docs
- "Create API documentation"
- "Write user guide"
- "Document the deployment process"
- "Update README"

## Advanced Usage Tips

### Provide Context
```bash
# Good: Specific context
/auto "add user authentication to the React frontend"

# Better: Include current state
/auto "add user authentication to React frontend - currently has basic forms but no backend integration"
```

### Specify Constraints
```bash
# Good: Clear constraint
/auto "optimize database queries but maintain existing API"

# Better: Multiple constraints
/auto "optimize database queries while maintaining API compatibility and not breaking existing tests"
```

### Indicate Uncertainty
```bash
# When unsure about approach
/auto "improve user experience but not sure if it's frontend, backend, or both"

# When unsure about scope
/auto "fix the login issues - could be validation, authentication, or database related"
```

## Next Steps After Auto

1. **Trust the Selection**: The auto command has analyzed your request thoroughly
2. **Provide Feedback**: If the selected approach doesn't feel right, explain why
3. **Learn the Pattern**: Notice why certain requests route to specific commands
4. **Use Direct Commands**: As you learn, use specific commands for faster execution

## Related Documentation
- [Task Command](task-command.md) - For focused single-component work
- [Feature Command](feature-command.md) - For complete feature development
- [Query Command](query-command.md) - For research and analysis
- [All Commands](README.md) - Complete command reference