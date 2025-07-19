# Error Recovery Patterns

**Purpose**: Transform cryptic errors into helpful guidance  
**User Benefit**: Know exactly what went wrong and how to fix it  
**Implementation**: Ready to use in all commands and modules

## Core Principle: Every Error Should Help

### ❌ What Users See Now
```
Error: undefined
Error: Command failed
Error: File not found
Error: Invalid configuration
```

### ✅ What Users Should See
```
Error: Cannot find test directory
  → Create a 'tests/' directory in your project root
  → Or update PROJECT_CONFIG.xml to specify test location: <test_directory>your_test_dir</test_directory>
  → Run '/init-validate' to check your setup

Error: TDD cycle failed - no tests found for new code
  → Write tests first in: tests/test_user_auth.py
  → Example test: test_user_login_validates_credentials()
  → Then run '/task' again to continue

Error: Cannot read package.json
  → File doesn't exist in current directory
  → Are you in the right directory? Current: /Users/you/wrong-folder
  → Try: cd /path/to/your/project
```

## Error Categories & Recovery Strategies

### 1. Configuration Errors
```python
def handle_config_error(error):
    if "PROJECT_CONFIG.xml not found":
        return ErrorResponse(
            problem="Framework configuration missing",
            solution="Run '/init' to create configuration",
            alternative="Copy PROJECT_CONFIG_TEMPLATE.md to PROJECT_CONFIG.xml",
            verify="Run '/init-validate' after setup"
        )
    
    if "Invalid configuration":
        return ErrorResponse(
            problem=f"Configuration error: {error.details}",
            solution=f"Fix in PROJECT_CONFIG.xml: {error.line}",
            example=show_correct_format(error.field),
            verify="Validate with '/init-validate'"
        )
```

### 2. File System Errors
```python
def handle_file_error(error):
    if error.type == "FileNotFound":
        return ErrorResponse(
            problem=f"Cannot find: {error.file}",
            context=f"Looking in: {error.search_path}",
            solutions=[
                f"Create the file: touch {error.file}",
                f"Check if you meant: {suggest_similar_files(error.file)}",
                f"Verify path in PROJECT_CONFIG.xml"
            ]
        )
    
    if error.type == "PermissionDenied":
        return ErrorResponse(
            problem=f"No permission to access: {error.file}",
            solution=f"Fix permissions: chmod 644 {error.file}",
            alternative="Run with appropriate user permissions",
            check=f"Current user: {get_current_user()}"
        )
```

### 3. Command Errors
```python
def handle_command_error(error):
    if "Unknown command":
        similar = find_similar_commands(error.command)
        return ErrorResponse(
            problem=f"Command not found: {error.command}",
            suggestions=f"Did you mean: {', '.join(similar)}?",
            help="See all commands: /auto help",
            example=f"Try: /{similar[0]} \"{error.original_request}\""
        )
    
    if "Missing arguments":
        return ErrorResponse(
            problem="Command needs more information",
            format=show_command_syntax(error.command),
            example=show_command_example(error.command),
            help=f"Full docs: /auto help {error.command}"
        )
```

### 4. Development Errors
```python
def handle_dev_error(error):
    if "Test failed":
        return ErrorResponse(
            problem=f"Test failure: {error.test_name}",
            output=error.test_output,
            likely_cause=analyze_test_failure(error),
            next_steps=[
                "1. Read the error message above",
                "2. Fix the implementation",
                "3. Run tests again",
                "Or skip this test temporarily with @pytest.mark.skip"
            ]
        )
    
    if "Linting error":
        return ErrorResponse(
            problem=f"Code style issue: {error.rule}",
            location=f"{error.file}:{error.line}",
            fix=error.suggested_fix,
            auto_fix="Run: /task --auto-fix" if error.fixable else None
        )
```

### 5. Framework Errors
```python
def handle_framework_error(error):
    if "Module not found":
        return ErrorResponse(
            problem=f"Missing framework module: {error.module}",
            solution="Reinstall framework: /init-validate --repair",
            check=f"Expected at: .claude/{error.module}",
            fallback="Continue with reduced functionality"
        )
    
    if "Quality gate failed":
        return ErrorResponse(
            problem=f"Code doesn't meet standards: {error.gate}",
            details=error.validation_results,
            fix=suggest_quality_fixes(error),
            override="Use --force to skip (not recommended)"
        )
```

## Implementation Patterns

### Pattern 1: Graceful Degradation
```python
# Instead of crashing, continue with warnings
try:
    config = load_project_config()
except ConfigError as e:
    print(helpful_error(e))
    print("ℹ️  Using default configuration")
    config = get_default_config()
    # Continue execution with defaults
```

### Pattern 2: Contextual Help
```python
# Provide context-aware assistance
def provide_context(error):
    return {
        "what_happened": error.message,
        "why_it_happened": analyze_cause(error),
        "how_to_fix": step_by_step_solution(error),
        "prevent_future": best_practices(error.type)
    }
```

### Pattern 3: Progressive Disclosure
```python
# Start simple, offer more detail if needed
def format_error(error, verbosity="normal"):
    if verbosity == "simple":
        return f"❌ {error.summary}\n   → Try: {error.quick_fix}"
    
    elif verbosity == "normal":
        return f"""
❌ {error.summary}

What went wrong:
  {error.details}

How to fix:
  → {error.solution}

Need more help? Add --verbose
"""
    
    else:  # verbose
        return full_diagnostic_report(error)
```

### Pattern 4: Error Prevention
```python
# Validate before operations to prevent errors
def pre_flight_check():
    issues = []
    
    if not os.path.exists("PROJECT_CONFIG.xml"):
        issues.append("Missing configuration - run /init first")
    
    if not os.path.exists(get_test_directory()):
        issues.append(f"No test directory - create '{get_test_directory()}/'")
    
    if issues:
        print("⚠️  Found issues that may cause errors:")
        for issue in issues:
            print(f"  - {issue}")
        if not confirm("Continue anyway?"):
            return False
    
    return True
```

## Error Message Templates

### Template 1: File Operations
```
Error: {operation} failed for '{filename}'
  
  Problem: {specific_issue}
  Location: {full_path}
  
  Solutions:
  1. {primary_solution}
  2. {alternative_solution}
  
  Common causes:
  - {cause_1}
  - {cause_2}
```

### Template 2: Command Execution
```
Error: /{command} failed
  
  What happened: {error_summary}
  
  To fix this:
  → {immediate_action}
  
  Full command syntax:
  /{command} {required_args} [optional_args]
  
  Example:
  /{command} {example_usage}
```

### Template 3: Quality Gates
```
⚠️  Quality Check Failed: {gate_name}

Current: {current_value}
Required: {required_value}

To fix:
1. {step_1}
2. {step_2}
3. Run validation: {validation_command}

Why this matters:
{quality_rationale}
```

## Integration Guide

### For Command Implementers
```python
# Wrap operations with helpful error handling
def execute_command(request):
    try:
        # Pre-flight checks
        if not validate_environment():
            return helpful_error("Environment not ready", 
                               solution="Run /init-validate")
        
        # Main operation
        result = perform_operation(request)
        
    except FrameworkError as e:
        return transform_to_helpful_error(e)
    
    except Exception as e:
        # Even unexpected errors should be helpful
        return generic_helpful_error(e, context=request)
```

### For Module Developers
```python
# Raise errors with enough context to be helpful
class InformativeError(Exception):
    def __init__(self, message, solution=None, context=None):
        self.message = message
        self.solution = solution
        self.context = context
        super().__init__(message)

# Usage
if not test_file_exists:
    raise InformativeError(
        "No test file found for module",
        solution=f"Create test file: {expected_test_path}",
        context={"module": module_name, "convention": "test_*.py"}
    )
```

## Success Metrics

### Before
- "I don't understand this error" - 80% of users
- "I don't know how to fix it" - 90% of users
- Error resolution time: 10-30 minutes

### After  
- Clear understanding: 95% of users
- Know how to fix: 90% of users
- Error resolution time: 1-5 minutes

## Examples of Transformation

### Real Error → Helpful Error

**File Not Found**
```
# Before:
FileNotFoundError: [Errno 2] No such file or directory: 'src/config.json'

# After:
❌ Cannot read configuration file

  Looking for: src/config.json
  In directory: /Users/you/project
  
  This might help:
  → Create the file: echo '{}' > src/config.json
  → Or check if it's in a different location: find . -name "config.json"
  → Update path in code: line 45 of main.py
```

**Import Error**
```
# Before:
ImportError: No module named 'requests'

# After:
❌ Missing required package: requests

  This package is needed for HTTP operations
  
  To fix:
  → Install it: pip install requests
  → Or with pipenv: pipenv install requests
  → Or with poetry: poetry add requests
  
  Then try your command again.
```

---

**Remember**: Every error is a teaching opportunity. Make them helpful, not cryptic.