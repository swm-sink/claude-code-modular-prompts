# Source #8: Claude Code Tools and System Prompt

### Metadata
- **URL**: https://gist.github.com/wong2/e0f34aac66caf890a332f7b6f9e2ba8f
- **Author/Organization**: wong2 (Community)
- **Date**: 2025 (Current)
- **Type**: Community/Research

### Verification Status
- ✅ Shows complete tool list
- ✅ Demonstrates TodoWrite patterns
- ✅ System prompt revealed
- ✅ Multi-tool workflow guidance
- ✅ Actual Claude Code internals

### Rating: 5/5

### Key Patterns Observed

1. **Complete Tool Suite**:
   - File operations: Read, Write, Edit, MultiEdit
   - Search: Glob, Grep, LS
   - System: Bash
   - Web: WebSearch, WebFetch
   - Task management: TodoRead, TodoWrite
   - Notebooks: NotebookRead, NotebookEdit
   - Planning: exit_plan_mode

2. **TodoWrite Usage Rules**:
   ```
   - Use for tasks with 3+ steps
   - Only one task in_progress at a time
   - Mark complete immediately after finishing
   - Break complex tasks into actionable items
   - Task states: pending, in_progress, completed
   ```

3. **System Prompt Patterns**:
   - Concise responses (1-3 sentences)
   - Minimize output tokens
   - Be proactive only when asked
   - Follow existing conventions
   - No comments unless requested

### Code Examples

```python
# TodoWrite structure
todos = [
    {
        "id": "unique-id",
        "content": "Task description",
        "status": "pending|in_progress|completed",
        "priority": "high|medium|low"
    }
]
```

### Insights & Innovations

- Tool batching for performance
- Task tool for context reduction
- Strict output minimization
- Security-first approach
- Clear task management workflow

### Practical Applications

- Multi-tool parallel execution
- Structured task tracking
- Efficient context usage
- Security-conscious development

### Limitations/Caveats

- TodoWrite overwrites entire list (Issue #2250)
- Updates in Task tool not visible (Issue #1173)
- One task at a time limitation