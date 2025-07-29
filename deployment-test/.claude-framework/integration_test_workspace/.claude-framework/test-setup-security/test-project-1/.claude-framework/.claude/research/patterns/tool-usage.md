# Tool Usage Patterns for Claude Code

## Overview
Claude Code provides 15+ tools for file operations, search, web access, task management, and more. Effective usage patterns maximize efficiency and minimize token consumption.

## Core Tools Available

From official sources:
1. **File Operations**: Read, Write, Edit, MultiEdit
2. **Search Tools**: Glob, Grep, LS
3. **System**: Bash
4. **Web Tools**: WebSearch, WebFetch
5. **Task Management**: TodoRead, TodoWrite
6. **Notebooks**: NotebookRead, NotebookEdit
7. **Planning**: exit_plan_mode

## Essential Tool Patterns

### 1. Parallel Tool Execution

**Pattern**: Execute multiple independent tools simultaneously.

**Example**:
```python
# Inefficient: Sequential
result1 = Read("file1.js")
result2 = Read("file2.js")
result3 = Grep("pattern", "src/")

# Efficient: Parallel
results = parallel_execute([
    Read("file1.js"),
    Read("file2.js"),
    Grep("pattern", "src/")
])
```

**From System Prompt**: "When multiple independent pieces of information are requested, batch your tool calls together for optimal performance."

### 2. Tool Selection Strategy

**Pattern**: Choose the right tool for the task.

**Decision Tree**:
```
Need to find files?
├── Know exact path → Read
├── Know pattern → Glob
└── Search content → Grep

Need to modify files?
├── Single change → Edit
├── Multiple changes → MultiEdit
└── New file → Write

Need system info?
├── File listing → LS
├── Run command → Bash
└── Complex search → Task tool
```

### 3. TodoWrite Task Management

**Pattern**: Use TodoWrite for complex, multi-step tasks.

**When to Use** (from system prompt):
- Tasks with 3+ steps
- Complex operations requiring planning
- When tracking progress is important
- Team visibility needed

**Implementation**:
```python
# Structure
todos = [
    {
        "id": "unique-id",
        "content": "Task description",
        "status": "pending|in_progress|completed",
        "priority": "high|medium|low"
    }
]

# Rules
- Only one task "in_progress" at a time
- Mark complete immediately after finishing
- Update frequently for visibility
```

### 4. Search Optimization

**Pattern**: Use appropriate search tools to minimize context usage.

**Grep Best Practices**:
```bash
# Include context lines
Grep("pattern", path, -A=2, -B=2)

# Search specific file types
Grep("TODO", path, type="py")

# Limit results
Grep("error", path, head_limit=10)
```

**From Verification**: "Use Task tool for open-ended searches requiring multiple rounds"

### 5. Edit vs MultiEdit

**Pattern**: Choose editing approach based on scope.

**Single Edit**:
```python
# For one specific change
Edit(
    file_path="src/index.js",
    old_string="console.log",
    new_string="logger.debug"
)
```

**MultiEdit**:
```python
# For multiple changes in same file
MultiEdit(
    file_path="src/index.js",
    edits=[
        {"old_string": "var", "new_string": "const"},
        {"old_string": "require", "new_string": "import"},
        {"old_string": "module.exports", "new_string": "export default"}
    ]
)
```

### 6. Web Tool Usage

**Pattern**: Use web tools for current information and research.

**WebSearch**:
```python
# Domain-specific search
WebSearch(
    query="Claude Code GitHub examples 2025",
    allowed_domains=["github.com"]
)
```

**WebFetch**:
```python
# Extract specific information
WebFetch(
    url="https://docs.anthropic.com/claude-code",
    prompt="Extract tool usage examples and patterns"
)
```

### 7. Bash Command Patterns

**Pattern**: Use Bash for system operations with safety checks.

**Safe Execution**:
```bash
# Verify before destructive operations
Bash("ls target/", description="Check directory exists")
Bash("rm -rf target/", description="Clean build directory")

# Use descriptions for clarity
Bash("npm test", description="Run test suite")
```

**From System Prompt**: "Be concise, direct, and explain what commands do"

### 8. File Discovery Patterns

**Pattern**: Efficient file location strategies.

```python
# Pattern 1: Known location
if know_exact_path:
    Read("/src/components/Button.js")

# Pattern 2: Pattern matching
elif know_naming_pattern:
    Glob("**/Button*.js")

# Pattern 3: Content search
elif searching_for_content:
    Grep("class Button", type="js")

# Pattern 4: Exploration
else:
    LS("/src/components/")
```

## Advanced Tool Patterns

### 1. Tool Chaining

**Pattern**: Use output from one tool as input to another.

```python
# Find files, then read them
files = Glob("**/*test*.js")
for file in files[:5]:  # Limit to prevent overload
    content = Read(file)
    analyze(content)
```

### 2. Conditional Tool Usage

**Pattern**: Select tools based on context.

```python
# From hooks configuration
if file_type == "notebook":
    NotebookRead(path)
else:
    Read(path)
```

### 3. Error Recovery

**Pattern**: Handle tool failures gracefully.

```python
try:
    Edit(file, old, new)
except EditFailed:
    # Fall back to Write if edit fails
    content = Read(file)
    new_content = content.replace(old, new)
    Write(file, new_content)
```

### 4. Performance Optimization

**Pattern**: Minimize tool calls and token usage.

```python
# Bad: Multiple reads
header = Read("component.js", limit=10)
footer = Read("component.js", offset=90)

# Good: Single read with processing
content = Read("component.js")
header = content[:10]
footer = content[-10:]
```

## Tool-Specific Best Practices

### TodoWrite
- Update after each task completion
- Keep descriptions concise
- Use meaningful IDs
- Batch updates when possible

### Grep
- Use type filters for faster searches
- Include line numbers with -n
- Limit results with head_limit
- Use multiline mode for complex patterns

### Edit/MultiEdit
- Verify unique strings before editing
- Use replace_all for bulk changes
- Preserve exact whitespace
- Test with small changes first

### Bash
- Always include descriptions
- Avoid interactive commands
- Use absolute paths
- Check command success

## Anti-Patterns to Avoid

### 1. Tool Overuse
❌ Reading entire codebase into context
✅ Targeted reads of specific files

### 2. Sequential Operations
❌ Multiple sequential edits
✅ Single MultiEdit call

### 3. Unsafe Commands
❌ `rm -rf /` without checks
✅ Verify paths before deletion

### 4. Ignoring Tool Errors
❌ Continuing after tool failure
✅ Handle errors appropriately

## Real-World Examples

### From Claude Code Action
- Analyzes PR context before acting
- Creates progress tracking comments
- Manages branches automatically

### From ClaudeFlow
- Separates planning and execution tools
- Uses memory tools for persistence
- Implements phase-based workflows

### From Task Workflow
- Git worktree for isolation
- Quality gates between phases
- Systematic tool usage

## Performance Guidelines

### Token Optimization
1. Batch parallel operations
2. Use search before read
3. Limit file read sizes
4. Cache frequently accessed content

### Speed Optimization
1. Prefer Glob over LS for patterns
2. Use specific file types in Grep
3. Minimize Bash calls
4. Batch related operations

## Conclusion

Effective tool usage in Claude Code requires:
- Understanding each tool's strengths
- Batching operations for efficiency
- Appropriate error handling
- Token and performance awareness
- Following established patterns

The key is selecting the right tool for each task and using it efficiently.