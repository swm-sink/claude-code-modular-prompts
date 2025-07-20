# Architectural Constraints

*Version: 1.0.0*
*Purpose: Practical constraints for reliable LLM autonomous coding*
*Scope: Personal workflow tool, not enterprise software*

## 🎯 Core Principles

1. **Simplicity First** - Constraints should guide, not restrict
2. **Developer Experience** - Fast feedback, clear errors
3. **Token Efficiency** - Every constraint must justify its token cost
4. **Practical Security** - Protect against common issues, not nation-states

## 📁 Module Structure

### Size Limits
- **Maximum module size**: 15KB (prevents context overflow)
- **Preferred module size**: 5-10KB (optimal for LLM processing)
- **Maximum complexity**: Cyclomatic complexity < 15
- **Maximum nesting**: 4 levels deep

### Required Sections
Every module MUST contain:
```markdown
# Module Name
Purpose: [One sentence description]
Dependencies: [List @ links]

## Interface
[Clear input/output specification]

## Implementation
[Core logic]

## Error Handling
[How errors are handled]

## Example Usage
[Practical example]
```

### Naming Conventions
- **Modules**: `{domain}-{function}-{type}.md` (e.g., `tdd-cycle-pattern.md`)
- **Commands**: `/command-name` (lowercase, hyphenated)
- **Variables**: `snake_case` for configs, `camelCase` for code
- **Files**: Use `.md` extension for all framework files

## 🔗 Dependency Management

### Allowed Dependencies
- **Internal**: Via @ links only (e.g., `@modules/patterns/tdd-cycle.md`)
- **External**: Must be in approved list (see below)
- **Depth**: Maximum 3 levels of dependency
- **Circular**: Strictly prohibited - will cause infinite loops

### Approved External Dependencies
```yaml
claude-code-cli: "*"  # Core dependency
python: ">=3.8"       # Scripting
nodejs: ">=18"        # If using JS
git: "*"              # Version control
```

### @ Link Rules
1. Always use relative paths from `.claude/`
2. Verify target exists before creating link
3. Document what the dependency provides
4. Maximum 5 @ links per module

## 🛡️ Security Constraints

### Input Validation
All user inputs MUST be validated:
```python
# Required pattern for all inputs
def process_input(user_input: str) -> str:
    # 1. Check not empty
    if not user_input or not user_input.strip():
        raise ValueError("Input cannot be empty")
    
    # 2. Check length
    if len(user_input) > 10000:
        raise ValueError("Input too large")
    
    # 3. Basic sanitization
    cleaned = user_input.strip()
    
    # 4. No shell metacharacters
    if any(char in cleaned for char in ['$', '`', ';', '|', '&']):
        raise ValueError("Invalid characters in input")
    
    return cleaned
```

### File Operations
- **Read**: Always verify file exists first
- **Write**: Never overwrite without confirmation
- **Paths**: Validate all paths are within project directory
- **Execution**: Never use `shell=True` or `eval()`

## ⚡ Performance Constraints

### Token Limits
- **Per module**: Max 4K tokens (leaving room for context)
- **Total framework**: Target <80K tokens loaded
- **Per operation**: Warn if >20K tokens used
- **Context reserve**: Always keep 50K tokens for work

### Response Times
- **Simple commands**: <2 seconds
- **Complex operations**: <10 seconds
- **Timeout**: 30 seconds maximum
- **Progress**: Show indicator after 3 seconds

### Resource Usage
- **Memory**: Warn at 500MB usage
- **CPU**: Single-threaded by default
- **Files**: Max 100 open simultaneously
- **Connections**: Pool with max 10

## 🧩 Integration Patterns

### Command-Module Integration
Commands MUST:
1. Validate inputs before module delegation
2. Handle module errors gracefully
3. Provide user-friendly error messages
4. Track operation progress

### Module Interfaces
Modules MUST:
1. Define clear input/output contracts
2. Validate their own inputs
3. Return structured responses
4. Handle their own errors

### Error Propagation
```python
# Standard error pattern
class FrameworkError(Exception):
    def __init__(self, message: str, recovery_hint: str = None):
        super().__init__(message)
        self.recovery_hint = recovery_hint

# Usage
raise FrameworkError(
    "Module not found: @modules/missing.md",
    recovery_hint="Check if module exists or fix @ link"
)
```

## 🔄 State Management

### Global State
- **Prohibited**: No global mutable state
- **Configuration**: Read-only after initialization
- **Sessions**: Isolated per command execution

### Concurrency
- **Default**: Single-threaded execution
- **Parallel**: Only for independent read operations
- **Locks**: Required for any shared resource access
- **Atomicity**: All operations must be atomic

## 📊 Quality Requirements

### Code Quality
- **Linting**: Must pass basic linting
- **Type hints**: Recommended for Python
- **Comments**: Required for complex logic
- **Documentation**: Required for public interfaces

### Testing
- **Unit tests**: Recommended for complex modules
- **Integration tests**: Required for new commands
- **Edge cases**: Document handled scenarios
- **Coverage**: Target 60% (not 90% - be realistic)

## 🚀 Development Workflow

### Adding New Modules
1. Check if functionality exists
2. Create module following template
3. Add @ links in commands
4. Test with edge cases
5. Document in CLAUDE.md

### Modifying Framework
1. Understand impact via dependency graph
2. Test changes locally first
3. Update documentation
4. Verify no regressions
5. Commit with clear message

## ⚠️ Anti-Patterns to Avoid

### LLM-Specific Pitfalls
1. **Hallucinated Imports**: Always verify modules exist
2. **Infinite Loops**: Check for circular dependencies
3. **Context Overflow**: Monitor token usage
4. **Over-Engineering**: Keep it simple
5. **Perfect Abstraction**: Practical > Perfect

### Common Mistakes
1. Creating files without checking existence
2. Assuming error handling exists
3. Ignoring token limits
4. Making changes without understanding impact
5. Adding complexity without clear benefit

## 📋 Validation Checklist

Before deploying any change:
- [ ] Module size <15KB?
- [ ] All @ links valid?
- [ ] Input validation present?
- [ ] Error handling implemented?
- [ ] Token usage reasonable?
- [ ] Documentation updated?
- [ ] No circular dependencies?
- [ ] Security patterns followed?

## 🎯 Success Metrics

A well-architected module:
- Loads in <100ms
- Uses <4K tokens
- Handles edge cases gracefully
- Provides clear error messages
- Has obvious purpose
- Can be understood in 5 minutes

---

Remember: These constraints exist to make the framework **more reliable**, not more complex. When in doubt, choose simplicity.