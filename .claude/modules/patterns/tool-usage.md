# /patterns/tool-usage - Claude Code Native Tool Optimization

**Purpose**: Comprehensive patterns for optimal Claude Code native tool usage, based on 2025 best practices and proven performance optimization.

## Module Interface
- **Trigger**: All commands use these optimization patterns
- **Dependencies**: None (foundational pattern)
- **Session**: N/A (tool optimization is universal)
- **Output**: Maximum efficiency Claude Code tool execution

## 2025 Tool Optimization Principles

### Parallel Execution (Critical Performance Pattern)
```python
# MANDATORY: All tool calls in single message for maximum efficiency
# Claude 4 models excel at parallel tool execution with 100% success rate

# ✅ CORRECT: True parallelism
Read("src/config.py")      # All execute in parallel
Read("src/database.py")    # Not sequentially
Read("src/models.py")      # Maximum efficiency
Grep("class User", "**/*.py")
Bash("git status")

# ❌ INCORRECT: Sequential execution (massive performance loss)
Read("src/config.py")
# Wait for response...
Read("src/database.py")
# Wait for response...
```

### Read-Before-Write Pattern (Mandatory Safety)
```python
# ALWAYS read files before any modifications
# Understanding context prevents errors and improves quality

# ✅ CORRECT: Safe modification pattern
current_content = Read("target_file.py")
# Analyze current state, understand patterns
# Make informed changes based on actual content
Edit("target_file.py", old_pattern, new_pattern)

# ❌ INCORRECT: Blind modification (high error rate)
Edit("target_file.py", assumed_old, new_code)
```

### Efficient Search Strategies
```python
# PREFER: Specific targeted searches (token efficient)
Glob("**/*.py")                    # Find Python files
Grep("class.*Service", "src/")     # Find service classes
Grep(r"def \w+_api\(", "src/api/") # Find API functions

# AVOID: Broad unfocused searches (token waste)
Grep("function", "**/*")           # Too generic
Grep("User", "**/*")              # Too broad scope
```

## Advanced Tool Patterns

### Multi-Edit Optimization
```python
# ✅ OPTIMAL: Single MultiEdit for multiple changes
MultiEdit("config.py", [
    {"old": "DEBUG = True", "new": "DEBUG = False"},
    {"old": "PORT = 8000", "new": "PORT = 8080"},
    {"old": "LOG_LEVEL = 'DEBUG'", "new": "LOG_LEVEL = 'INFO'"}
])

# ❌ INEFFICIENT: Multiple Edit calls
Edit("config.py", "DEBUG = True", "DEBUG = False")
Edit("config.py", "PORT = 8000", "PORT = 8080")
Edit("config.py", "LOG_LEVEL = 'DEBUG'", "LOG_LEVEL = 'INFO'")
```

### Smart Batching Strategies
```python
# ✅ OPTIMAL: Group related operations
# Git status batch
Bash("git status")
Bash("git diff --stat")
Bash("git log --oneline -5")

# File analysis batch  
Read("src/main.py")
Read("src/config.py")
Read("tests/test_main.py")

# Search and locate batch
Glob("**/*test*.py")
Grep("pytest", "**/*.py")
Grep("unittest", "**/*.py")

# ❌ INEFFICIENT: Interleaved unrelated operations
Bash("git status")
Read("random_file.py")
Bash("git diff")
Write("other_file.py", content)
```

## Error Handling and Resilience

### Graceful File Operations
```python
# Check directory existence before file operations
def safe_file_operations(directory_path, file_name):
    try:
        # Verify directory exists
        dir_contents = LS(directory_path)
        if file_name in [f.name for f in dir_contents]:
            content = Read(f"{directory_path}/{file_name}")
            return process_content(content)
        else:
            # File doesn't exist, create or skip
            return handle_missing_file(directory_path, file_name)
    except Exception as e:
        # Graceful degradation with clear user communication
        return f"File operation failed: {e}. Continuing with alternative approach."
```

### Command Execution Resilience
```python
# Handle command failures gracefully
def resilient_bash_execution(command, timeout_ms=30000):
    try:
        result = Bash(command, timeout=timeout_ms)
        if "error" in result.lower() or "failed" in result.lower():
            # Command succeeded but output indicates issues
            return handle_command_warnings(result)
        return result
    except TimeoutError:
        return f"Command timed out after {timeout_ms}ms. Consider breaking into smaller operations."
    except Exception as e:
        return f"Command execution failed: {e}. Attempting alternative approach."
```

## Multi-Agent Tool Coordination

### Task() Pattern Tool Usage
```python
# Each agent uses tools independently but efficiently
Task("Frontend Architect", """
TOOLS TO USE:
- Read() to examine React components and understand current architecture
- Glob() to find all frontend test files and component structure  
- MultiEdit() to update component interfaces consistently
- Bash() to run frontend tests and verify changes
""")

Task("Backend Engineer", """
TOOLS TO USE:
- Grep() to find all API endpoints and understand routing patterns
- Read() to examine existing API handlers and middleware
- Edit() to add new endpoints following established patterns
- Bash() to run API tests and verify integration
""")

# Agents coordinate through session but use tools independently
```

### Batch() Pattern Efficiency
```python
# Each batch item uses tools optimally
Batch([
    "Use Glob() to find all test files, then MultiEdit() to update import statements consistently",
    "Use Grep() to locate deprecated API calls, then Edit() each file to use modern equivalents", 
    "Use Read() to examine configuration files, then Write() updated configs with new settings"
])

# Each batch operation follows tool optimization patterns
```

## Command-Specific Tool Integration

### /query Command Tool Patterns
```python
# Research-only operations with maximum efficiency
def query_tool_strategy(research_topic):
    # Phase 1: Broad discovery (parallel execution)
    files = Glob(f"**/*{research_topic}*")
    classes = Grep(f"class.*{research_topic}", "**/*.py")
    functions = Grep(f"def.*{research_topic}", "**/*.py")
    configs = Grep(research_topic, "**/*.json", "**/*.yaml", "**/*.toml")
    
    # Phase 2: Deep analysis (parallel file reads)
    relevant_files = select_most_relevant(files)
    Read(relevant_files[0])
    Read(relevant_files[1]) 
    Read(relevant_files[2])
    
    # Phase 3: Web research for context
    WebSearch(f"{research_topic} best practices 2025")
    
    # NEVER uses Write, Edit, or destructive operations
```

### /task Command Tool Patterns  
```python
# Development execution with safety-first approach
def task_tool_strategy(development_task):
    # Phase 1: Understanding (read-first pattern)
    current_state = Read(target_files)
    related_tests = Glob("**/test*" + task_scope + "*")
    dependencies = Grep("import.*" + task_scope, "**/*.py")
    
    # Phase 2: Planning (analyze before acting)
    plan = analyze_changes_needed(current_state, dependencies)
    
    # Phase 3: Implementation (systematic modification)
    for change in plan.changes:
        if change.type == "multi_file":
            MultiEdit(change.file, change.edits)
        else:
            Edit(change.file, change.old, change.new)
    
    # Phase 4: Verification (test and validate)
    Bash("run_tests_for_" + task_scope)
    Bash("lint_check")
```

### /swarm Command Tool Coordination
```python
# Multi-agent tool usage with conflict prevention
def swarm_tool_coordination(agents):
    # Tool access coordination to prevent conflicts
    file_locks = {}
    
    for agent in agents:
        agent.assigned_files = assign_non_overlapping_files(agent.role)
        agent.tool_strategy = optimize_for_agent_type(agent.role)
        
        # Agents use tools within their assigned scope
        if agent.role == "Security":
            agent.tools = ["Grep", "Read", "WebSearch"]  # Analysis focused
        elif agent.role == "Implementation":
            agent.tools = ["Read", "Edit", "MultiEdit", "Bash"]  # Modification focused
        elif agent.role == "Testing":
            agent.tools = ["Glob", "Read", "Write", "Bash"]  # Test creation focused
```

## Performance Optimization Patterns

### Token Efficiency
```python
# Minimize file read operations
def efficient_code_analysis(file_pattern):
    # Read all relevant files in parallel (not sequential)
    relevant_files = Glob(file_pattern)[:10]  # Limit scope
    
    # Batch read operations
    file_contents = {}
    for file in relevant_files:
        file_contents[file] = Read(file)
    
    # Process all content together (avoid re-reading)
    return analyze_patterns(file_contents)

# Optimize search patterns for speed
def smart_search_strategy(search_term):
    # Start specific, broaden if needed
    matches = Grep(search_term, "src/")
    if not matches:
        matches = Grep(search_term, "**/*.py")
    if not matches:
        matches = Grep(search_term, "**/*")
    
    return matches
```

### Memory and Resource Management
```python
# Handle large operations efficiently
def large_file_operations(large_file_path):
    # Check file size implications
    file_info = LS(os.path.dirname(large_file_path))
    target_file = next(f for f in file_info if f.name == os.path.basename(large_file_path))
    
    if target_file.size > 100000:  # Large file threshold
        # Use targeted searches instead of full read
        specific_content = Grep("critical_pattern", large_file_path)
        return process_specific_content(specific_content)
    else:
        # Safe to read entire file
        return Read(large_file_path)
```

## Tool Integration with Session Management

### Progress Tracking Integration
```python
# TodoWrite/TodoRead integration with tool operations
def track_tool_operations(operation_plan):
    # Initialize progress tracking
    TodoWrite([
        {"task": "Phase 1: File discovery and analysis", "status": "pending"},
        {"task": "Phase 2: Code modification", "status": "pending"},
        {"task": "Phase 3: Testing and validation", "status": "pending"}
    ])
    
    # Phase 1: Discovery
    files = Glob(operation_plan.pattern)
    analysis = Grep(operation_plan.search_term, operation_plan.scope)
    TodoWrite([...])  # Update first task to completed
    
    # Phase 2: Modification (only after analysis complete)
    for change in operation_plan.changes:
        Edit(change.file, change.old, change.new)
    TodoWrite([...])  # Update second task to completed
    
    # Phase 3: Validation
    test_results = Bash(operation_plan.test_command)
    TodoWrite([...])  # Update final task to completed
```

## Best Practices Summary (2025 Standards)

### Universal Principles
1. **Parallel Execution**: All tool calls in single message (100% success rate)
2. **Read-Before-Write**: Always understand before modifying (safety first)
3. **Specific Searches**: Targeted patterns over broad searches (efficiency)
4. **Error Resilience**: Graceful handling of all failure modes
5. **Progress Tracking**: TodoWrite/TodoRead for complex operations

### Performance Optimization
- **Batch related operations** together
- **Minimize file re-reads** through smart caching
- **Use specific search patterns** to reduce token usage
- **Handle large files** with targeted operations
- **Coordinate multi-agent** tool access to prevent conflicts

### Quality Assurance
- **Verify tool results** before proceeding to next step
- **Validate modifications** with appropriate testing
- **Document tool usage** in session tracking
- **Monitor resource usage** and optimize accordingly

**Token Budget**: <3k tokens (foundational efficiency patterns for all commands)