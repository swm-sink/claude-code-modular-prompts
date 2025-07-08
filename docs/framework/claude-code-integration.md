| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-08   | stable |

# Claude Code Integration - Native Tool Usage

────────────────────────────────────────────────────────────────────────────────

**Purpose**: Define proper usage of Claude Code's native tools and capabilities for optimal performance.

## Available Tools

### File Operations
```python
# Reading
Read(file_path)           # Read any file
Grep(pattern, path)       # Search content
Glob(pattern, path)       # Find files
LS(path)                 # List directory

# Writing
Write(file_path, content) # Create/overwrite
Edit(file_path, old, new) # Replace content
MultiEdit(file_path, edits) # Multiple edits
```

### Development Tools
```python
# Execution
Bash(command)            # Run shell commands
TodoWrite(todos)         # Task management
TodoRead()              # Check task status

# Research
WebSearch(query)         # Search the web
WebFetch(url, prompt)    # Analyze web content
```

## Tool Best Practices

### Batch Operations
```python
# Good: Single message, multiple tools
Read("src/config.py")
Read("src/database.py")
Read("src/models.py")

# Bad: Sequential messages
Read("src/config.py")
# Wait...
Read("src/database.py")
```

### Efficient Searching
```python
# Good: Targeted search
Grep("class User", "**/*.py")

# Better: Specific path
Grep("class User", "src/models/*.py")

# Bad: Too broad
Grep("User", "**/*")
```

### Smart Editing
```python
# Good: MultiEdit for multiple changes
MultiEdit("config.py", [
    {"old": "DEBUG = True", "new": "DEBUG = False"},
    {"old": "PORT = 8000", "new": "PORT = 8080"}
])

# Bad: Multiple Edit calls
Edit("config.py", "DEBUG = True", "DEBUG = False")
Edit("config.py", "PORT = 8000", "PORT = 8080")
```

## Integration Patterns

### Research Before Modify
```python
# Always read before writing
file_content = Read("src/app.py")
# Understand structure
# Make informed changes
Edit("src/app.py", old_code, new_code)
```

### Comprehensive Search
```python
# Find all occurrences
files = Glob("**/*.py")
matches = Grep("deprecated_function", "src/")
# Plan refactoring
# Execute systematically
```

### Progress Tracking
```python
# Start with plan
TodoWrite([
    {"task": "Research current implementation"},
    {"task": "Design improvements"},
    {"task": "Implement changes"},
    {"task": "Add tests"}
])
# Update as you progress
```

## Multi-Agent Integration

### Task() with Tools
```python
Task("Frontend Dev", """
Use Read() to examine components
Use MultiEdit() to update styles
Use Bash() to run tests
""")

Task("Backend Dev", """
Use Grep() to find API endpoints
Use Edit() to add new routes
Use Bash() to verify
""")
```

### Batch() Efficiency
```python
Batch([
    "Use Glob() to find all test files and update imports",
    "Use Grep() to find deprecated APIs and modernize",
    "Use MultiEdit() to apply consistent formatting"
])
```

## Command Integration

### /query Command
- Uses Read, Grep, Glob extensively
- Never uses Write or Edit
- Combines findings intelligently

### /task Command
- Reads first, understands context
- Edits systematically
- Verifies with Bash

### /swarm Command
- Each agent uses appropriate tools
- Coordinates file access
- Avoids conflicts

## Performance Tips

### Minimize File Reads
```python
# Good: Read once, use multiple times
content = Read("large_file.py")
# Process content...

# Bad: Multiple reads
Read("large_file.py")  # First time
# Later...
Read("large_file.py")  # Again
```

### Efficient Searches
```python
# Good: Specific patterns
Grep(r"def \w+_api\(", "src/api/")

# Bad: Generic patterns
Grep("def", "**/*")
```

### Smart Batching
```python
# Good: Related operations together
Bash("git status")
Bash("git diff")
Bash("git log -5")

# Bad: Interleaved operations
Bash("git status")
Read("file.py")
Bash("git diff")
```

## Error Handling

### File Operations
```python
# Check existence
if LS("/path/to/dir"):
    Read("/path/to/dir/file.py")

# Handle missing files gracefully
try:
    content = Read("maybe_missing.py")
except FileNotFoundError:
    # Create or skip
```

### Command Execution
```python
# Capture errors
result = Bash("npm test")
if "FAILED" in result:
    # Handle test failures

# Use appropriate timeouts
Bash("long_running_command", timeout=60000)
```

## Tool Limitations

### Be Aware Of
- File size limits for Read
- Search depth limits for Grep
- Execution timeouts for Bash
- Rate limits for WebSearch

### Work Within Constraints
- Split large files if needed
- Use specific paths for searches
- Break long operations into steps
- Cache web results when possible

## Best Practices Summary

1. **Read before Write** - Understand first
2. **Batch operations** - Single message efficiency
3. **Specific patterns** - Targeted searches
4. **Progress tracking** - Use todos
5. **Error handling** - Graceful failures

These native tools are powerful when used correctly.