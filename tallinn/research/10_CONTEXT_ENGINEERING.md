# Context Engineering and Token Optimization

## Overview

Context engineering is "the new vibe coding" - the practice of optimizing how AI coding assistants understand and work with your codebase. It's about maximizing effectiveness while minimizing token usage and costs.

## Context Window Fundamentals

### Model Capacities

| Model | Context Window | Effective Usage | Best For |
|-------|----------------|-----------------|----------|
| Claude Opus 4 | 200k tokens | Full capacity | Complex analysis, large codebases |
| Claude Sonnet 4 | 200k tokens | Full capacity | Balanced tasks |
| Claude Haiku 3.5 | 200k tokens | Full capacity | Quick tasks |
| Enterprise Plans | 500k tokens | With Sonnet 4 | Massive codebases |

### Token Equivalents
- 1 token ≈ 4 characters
- 200k tokens ≈ 500 pages of text
- 500k tokens ≈ 1,250 pages of text

## Context Optimization Strategies

### 1. File Structure Optimization

**Principle**: Keep files lean and focused

```markdown
# Bad: Large monolithic file (1000+ lines)
src/components/Dashboard.tsx  # Everything in one file

# Good: Modular structure
src/
  components/
    Dashboard/
      index.tsx         # Main component (50 lines)
      DashboardHeader.tsx  # Sub-component (30 lines)
      DashboardStats.tsx   # Sub-component (40 lines)
      useDashboard.ts      # Hook (25 lines)
      types.ts             # Types (20 lines)
```

### 2. Direct Reading Instructions

**In CLAUDE.md:**
```markdown
# File Boundaries
Read files in this order for features:
1. Feature specification: /docs/features/
2. Implementation: /src/features/
3. Tests: /tests/features/

# Ignore These Directories
- node_modules/
- build/
- dist/
- .next/
- coverage/
```

### 3. Context Window Management

```bash
# Clear context between distinct tasks
/clear

# Use specific file references
@src/specific-file.ts  # Instead of "check the files"

# Batch related operations
"Update all API endpoints in src/api/ to use new auth"
# Instead of multiple separate requests
```

### 4. Strategic Information Loading

**Hierarchical Context Loading:**
```markdown
# Level 1: Project Overview (always loaded)
Project type, tech stack, key conventions

# Level 2: Current Task Context
Relevant files, specifications, examples

# Level 3: Supporting Information
Related tests, documentation, dependencies
```

## Extended Thinking Optimization

### Thinking Keywords and Budgets

| Keyword | Thinking Budget | Use Case |
|---------|-----------------|----------|
| "think" | Low | Simple analysis |
| "think hard" | Medium | Complex problems |
| "think harder" | High | Critical decisions |
| "ultrathink" | Maximum | Architecture design |

### Usage Examples

```bash
# Simple task - minimal thinking
"Fix the typo in the error message"

# Complex task - extended thinking
"Think hard about the security implications of this auth flow"

# Critical task - maximum thinking
"Ultrathink: Design a scalable microservices architecture"
```

## Cost Optimization Techniques

### 1. Token Usage Calculation

```python
# Estimate tokens before sending
def estimate_tokens(text):
    # Rough estimate: 1 token ≈ 4 characters
    return len(text) / 4

# Example usage
prompt = "Analyze this code..."
file_content = open("large_file.js").read()
total_tokens = estimate_tokens(prompt + file_content)
print(f"Estimated tokens: {total_tokens}")
```

### 2. Prompt Compression

**Before:**
```
Please analyze the following JavaScript code and identify any potential 
performance issues, security vulnerabilities, or code quality problems. 
Also suggest improvements and best practices that should be followed.
```

**After:**
```
Analyze JS code for: performance, security, quality issues. Suggest fixes.
```

### 3. Context Caching Patterns

```bash
# Cache analysis results
CACHE_KEY="analysis_$(echo "$FILE" | md5sum)"
if [ -f "/tmp/claude_cache/$CACHE_KEY" ]; then
  cat "/tmp/claude_cache/$CACHE_KEY"
else
  claude -p "Analyze $FILE" | tee "/tmp/claude_cache/$CACHE_KEY"
fi
```

## Advanced Context Engineering

### 1. Context Layering

```markdown
# Base Context (CLAUDE.md) - 500 tokens
Essential project info

# Task Context (.claude/contexts/feature-x.md) - 1000 tokens
Feature-specific information

# Dynamic Context (generated) - 2000 tokens
Current file contents, recent changes
```

### 2. Smart Context Selection

```python
# context_selector.py
def select_relevant_files(task_description, codebase):
    """Select only relevant files for the task."""
    keywords = extract_keywords(task_description)
    relevant_files = []
    
    for file in codebase:
        if any(keyword in file.content for keyword in keywords):
            relevant_files.append(file)
    
    # Sort by relevance
    return sorted(relevant_files, key=lambda f: f.relevance_score)
```

### 3. Context Templates

**Bug Fix Template:**
```markdown
# Bug Fix Context
## Issue
$ISSUE_DESCRIPTION

## Affected Files
$FILE_LIST

## Recent Changes
$GIT_DIFF

## Related Tests
$TEST_FILES
```

**Feature Development Template:**
```markdown
# Feature Context
## Specification
$FEATURE_SPEC

## Architecture
$ARCHITECTURE_DIAGRAM

## Dependencies
$DEPENDENCY_LIST

## Examples
$SIMILAR_FEATURES
```

## Performance Patterns

### 1. Incremental Context Building

```bash
# Start with minimal context
claude "What files implement user authentication?"

# Build on response
claude "Show me the auth middleware in src/middleware/auth.ts"

# Deep dive as needed
claude "Explain the JWT validation in line 45-60"
```

### 2. Context Recycling

```markdown
# In CLAUDE.md
## Session Context
Reuse these findings from previous analysis:
- Authentication flow uses JWT with refresh tokens
- Database queries are optimized with indexes
- API rate limiting is 100 requests/minute
```

### 3. Parallel Context Processing

```bash
# Process multiple contexts in parallel
parallel -j 4 claude -p "Analyze security in {}" ::: \
  "src/auth/*" \
  "src/api/*" \
  "src/database/*" \
  "src/utils/*"
```

## Token Reduction Strategies

### 1. Code Summarization

```markdown
# Instead of full file content
## File: src/services/UserService.ts (2500 lines)
### Summary
- Main class: UserService
- Key methods: create, update, delete, find
- Dependencies: Database, Cache, Logger
- Patterns: Repository pattern with caching
```

### 2. Selective Inclusion

```python
def include_code_section(file_path, start_line, end_line):
    """Include only relevant code sections."""
    with open(file_path) as f:
        lines = f.readlines()
        return ''.join(lines[start_line-1:end_line])

# Usage
relevant_code = include_code_section("app.py", 100, 150)
```

### 3. Reference Compression

```markdown
# Instead of repeating code
See previous analysis of AuthService (message #3)

# Instead of full error stacks
Error: TypeError at UserController.create (line 45)
Key issue: undefined property 'email'
```

## Monitoring and Metrics

### Token Usage Tracking

```python
# track_usage.py
import json
from datetime import datetime

def track_token_usage(prompt, response, tokens_used):
    """Track token usage for optimization."""
    with open("token_usage.json", "a") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "prompt_length": len(prompt),
            "response_length": len(response),
            "tokens_used": tokens_used,
            "cost": tokens_used * 0.00002  # Example rate
        }, f)
        f.write("\n")
```

### Context Effectiveness Metrics

```markdown
# Measure context quality
## Good Context Indicators
- Single-attempt task completion: 85%+
- Relevant file identification: 95%+
- Accurate problem diagnosis: 90%+

## Poor Context Indicators
- Multiple clarification requests
- Incorrect file references
- Missed dependencies
```

## Best Practices Summary

### Do's
✅ Keep CLAUDE.md under 500 lines  
✅ Use hierarchical context loading  
✅ Clear context between unrelated tasks  
✅ Batch similar operations  
✅ Use specific file references  
✅ Monitor token usage  
✅ Cache expensive analyses  

### Don'ts
❌ Include entire codebases unnecessarily  
❌ Repeat large code blocks  
❌ Use vague references  
❌ Ignore token limits  
❌ Mix unrelated contexts  
❌ Forget to clear old context  

## Advanced Techniques

### 1. Dynamic Context Generation

```bash
# generate_context.sh
#!/bin/bash
TASK=$1
CONTEXT_FILE=".claude/contexts/dynamic.md"

echo "# Task Context: $TASK" > $CONTEXT_FILE
echo "## Recent Changes" >> $CONTEXT_FILE
git log --oneline -10 >> $CONTEXT_FILE
echo "## Modified Files" >> $CONTEXT_FILE
git status --short >> $CONTEXT_FILE
echo "## Related Issues" >> $CONTEXT_FILE
gh issue list --search "$TASK" >> $CONTEXT_FILE
```

### 2. Context Optimization Tools

```python
# optimize_context.py
class ContextOptimizer:
    def __init__(self, max_tokens=50000):
        self.max_tokens = max_tokens
    
    def optimize(self, files, priority_map):
        """Optimize file selection within token budget."""
        selected = []
        current_tokens = 0
        
        # Sort by priority
        sorted_files = sorted(files, 
            key=lambda f: priority_map.get(f.path, 0), 
            reverse=True)
        
        for file in sorted_files:
            file_tokens = self.estimate_tokens(file.content)
            if current_tokens + file_tokens <= self.max_tokens:
                selected.append(file)
                current_tokens += file_tokens
        
        return selected
```

### 3. Intelligent Summarization

```python
def summarize_for_context(code, max_lines=20):
    """Create intelligent code summary."""
    summary = []
    
    # Extract key elements
    summary.append(f"Classes: {extract_classes(code)}")
    summary.append(f"Functions: {extract_functions(code)}")
    summary.append(f"Imports: {extract_imports(code)}")
    summary.append(f"Exports: {extract_exports(code)}")
    
    # Add complexity metrics
    summary.append(f"Lines: {count_lines(code)}")
    summary.append(f"Complexity: {calculate_complexity(code)}")
    
    return "\n".join(summary[:max_lines])
```

## Conclusion

Effective context engineering:
- Reduces costs by 50-80%
- Improves response accuracy
- Speeds up development
- Enables larger codebases

The key is finding the balance between comprehensive context and token efficiency.