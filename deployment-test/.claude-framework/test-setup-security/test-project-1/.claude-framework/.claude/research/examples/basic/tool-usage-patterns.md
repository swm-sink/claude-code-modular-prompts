# Basic Tool Usage Patterns

## Overview
This example demonstrates effective patterns for using Claude Code's tools in common development scenarios.

## Scenario 1: Finding and Updating Configuration

### Task: Update all API endpoints from HTTP to HTTPS

#### Inefficient Approach ❌
```python
# Bad: Sequential operations, broad search
files = LS("/")
files2 = LS("/src")  
files3 = LS("/src/config")
config = Read("/src/config/api.js")
config2 = Read("/src/config/endpoints.js")
# ... many more reads
```

#### Efficient Approach ✅
```python
# Good: Targeted search, parallel operations
# First, find all files containing API endpoints
api_files = Grep("http://api\\.", pattern="*.js", path="src/")

# Read relevant files in parallel
configs = parallel_read([
    "src/config/api.js",
    "src/config/endpoints.js",
    "src/services/api-client.js"
])

# Update all at once using MultiEdit
for file in api_files:
    MultiEdit(
        file_path=file,
        edits=[
            {
                "old_string": "http://api.example.com",
                "new_string": "https://api.example.com"
            },
            {
                "old_string": "http://staging-api.example.com",  
                "new_string": "https://staging-api.example.com"
            }
        ]
    )

# Verify changes
Bash("npm run test:api", description="Verify API connections work")
```

## Scenario 2: Implementing a New Feature

### Task: Add user profile image upload

#### Using TodoWrite for Planning
```python
TodoWrite(todos=[
    {
        "id": "profile-1",
        "content": "Create image upload component",
        "status": "in_progress",
        "priority": "high"
    },
    {
        "id": "profile-2", 
        "content": "Add API endpoint for image processing",
        "status": "pending",
        "priority": "high"
    },
    {
        "id": "profile-3",
        "content": "Update user model with avatar field",
        "status": "pending", 
        "priority": "medium"
    },
    {
        "id": "profile-4",
        "content": "Add image validation and security checks",
        "status": "pending",
        "priority": "high"
    },
    {
        "id": "profile-5",
        "content": "Write tests for upload flow",
        "status": "pending",
        "priority": "medium"
    }
])
```

#### Implementation Flow
```python
# Step 1: Research existing patterns
existing_uploads = Grep("upload|file|image", type="jsx")
upload_examples = Read("src/components/FileUpload.jsx", limit=50)

# Step 2: Create component
Write(
    file_path="src/components/ProfileImageUpload.jsx",
    content=profile_upload_component
)

# Step 3: Update in progress
TodoWrite(todos=[
    {"id": "profile-1", "status": "completed", ...},
    {"id": "profile-2", "status": "in_progress", ...}
])

# Step 4: Add API endpoint
Write(
    file_path="src/api/profile/upload.js",
    content=upload_endpoint_code
)

# Step 5: Run security checks
Bash("npm run security:scan src/api/profile/upload.js")
```

## Scenario 3: Debugging an Issue

### Task: Fix "Cannot read property 'user' of undefined" error

#### Smart Debugging Approach
```python
# 1. Find error location
error_files = Grep("Cannot read property.*user.*undefined", path="src/")

# 2. Search for the actual error pattern
potential_issues = Grep("\\.user(?!\\?)", path="src/", type="js")

# 3. Check specific patterns that might cause this
problems = [
    Grep("props\\.user\\.", path="src/components/"),
    Grep("state\\.user\\.", path="src/"),  
    Grep("data\\.user\\.", path="src/api/")
]

# 4. Read context around problematic code
for file in potential_issues[:3]:  # Limit initial investigation
    context = Read(file, limit=20, offset=problem_line - 10)
    analyze_context(context)

# 5. Fix with optional chaining
MultiEdit(
    file_path="src/components/UserProfile.jsx",
    edits=[
        {
            "old_string": "props.user.name",
            "new_string": "props.user?.name"
        },
        {
            "old_string": "props.user.email",
            "new_string": "props.user?.email"
        }
    ]
)

# 6. Verify fix
Bash("npm run test -- UserProfile", description="Test the fix")
```

## Scenario 4: Code Review Preparation

### Task: Ensure code meets standards before PR

#### Comprehensive Review Workflow
```python
# 1. Get list of changed files
changed = Bash("git diff --name-only main", description="Get changed files")

# 2. Run quality checks in parallel
quality_checks = parallel_execute([
    Bash("npm run lint", description="Check code style"),
    Bash("npm run typecheck", description="Verify types"),
    Bash("npm run test:changed", description="Run affected tests"),
    Grep("console\\.log", path=changed, description="Find debug logs")
])

# 3. Check for common issues
security_issues = Grep("api_key|password|secret", path=changed)
todos_left = Grep("TODO|FIXME|HACK", path=changed)

# 4. Generate summary
if any([security_issues, todos_left, quality_checks.failed]):
    create_fix_list()
else:
    Bash("git commit -m 'feat: add profile image upload'")
```

## Scenario 5: Performance Investigation

### Task: Find why the app is loading slowly

#### Performance Analysis Pattern
```python
# 1. Check bundle size
Bash("npm run build:analyze", description="Generate bundle report")

# 2. Find large imports
large_imports = Grep("import.*from", path="src/", head_limit=100)

# 3. Look for problematic patterns
performance_issues = parallel_search([
    Grep("JSON\\.parse.*JSON\\.stringify", description="Expensive operations"),
    Grep("map.*map.*map", description="Nested iterations"),
    Grep("useState.*\\[\\].*map", description="Re-renders on array ops"),
    Grep("useEffect.*\\[\\]", description="Missing dependencies")
])

# 4. Check lazy loading
lazy_loaded = Grep("React\\.lazy|dynamic", path="src/")

# 5. Measure specific components
Bash("npm run lighthouse -- --only-categories=performance")
```

## Best Practices Demonstrated

### 1. **Tool Selection**
- Use Grep for content search
- Use Glob for file patterns
- Use LS only for directory exploration
- Use Bash for system commands

### 2. **Parallel Execution**
- Batch independent operations
- Read multiple files at once
- Run multiple checks simultaneously

### 3. **Targeted Operations**
- Limit search scope
- Use file type filters
- Specify head_limit for large results

### 4. **Error Handling**
- Check before destructive operations
- Validate tool outputs
- Have fallback strategies

### 5. **Progress Tracking**
- Update TodoWrite frequently
- Mark completed items immediately
- Keep descriptions concise

## Common Patterns

### Finding Files
```python
# By name pattern
Glob("**/*test*.js")

# By content
Grep("className", type="jsx")

# By location
LS("/src/components/")
```

### Reading Efficiently
```python
# Read just what you need
Read(file, limit=50)  # First 50 lines
Read(file, offset=100, limit=20)  # Lines 100-120

# Parallel reads
files = ["a.js", "b.js", "c.js"]
contents = parallel_read(files)
```

### Editing Safely
```python
# Single precise edit
Edit(file, old_string, new_string)

# Multiple edits atomically  
MultiEdit(file, edits=[...])

# Bulk operations
Edit(file, old_string, new_string, replace_all=True)
```

### System Operations
```python
# Always describe what you're doing
Bash("npm test", description="Run test suite")

# Check before destructive operations
if Bash("ls dist/").success:
    Bash("rm -rf dist/", description="Clean build directory")
```

This example provides practical patterns for common development tasks using Claude Code's tools effectively.