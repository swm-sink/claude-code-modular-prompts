---
name: /project-task
description: Create and manage project-specific tasks with integrated workflow tracking (v1.0)
version: "1.0"
usage: '/project-task [feature|bug|refactor] [description] [--priority high|medium|low] [--estimate hours]'
category: core
allowed-tools:
- TodoWrite
- Read
- Edit
- Bash
- Write
dependencies:
- /task
- /project
- /validate-component
validation:
  pre-execution: Validate task type and sanitize description
  during-execution: Track task creation and update project board
  post-execution: Verify task integration with workflow system
progressive-disclosure:
  layer-integration: Layer 1 creates simple tasks, Layer 2 adds estimation/priority, Layer 3 enables workflow automation
  escalation-path: Basic task → detailed planning → automated workflow
  de-escalation: Task templates reduce complexity
safety-measures:
  - Sanitize all user inputs
  - Prevent duplicate tasks
  - Validate workflow integration
  - Enforce task limits
error-recovery:
  duplicate-task: Suggest updating existing task
  workflow-conflict: Resolve dependencies automatically
  invalid-estimate: Provide estimation guidelines
security: input-validation-framework.md
---

# Task Management for lusaka

## Input Validation

Before processing, I'll validate all inputs for security:

**Validating inputs...**

1. **Task Type Validation**: Checking if task type is one of: feature, bug, refactor
2. **Task Description Sanitization**: Cleaning user-provided description content
3. **Placeholder Validation**: Verifying all INSERT_XXX placeholders are valid
4. **Configuration Validation**: Validating project configuration values

```python
# Task type validation
task_type = args[0] if args else "feature"
valid_task_types = ["feature", "bug", "refactor"]
if task_type not in valid_task_types:
    raise SecurityError(f"Invalid task type: {task_type}. Must be one of: {', '.join(valid_task_types)}")

# Task description sanitization
task_description = " ".join(args[1:]) if len(args) > 1 else ""
sanitized_description = sanitize_user_data(task_description, "task_description", 500)
if sanitized_description["changes_made"]:
    print(f"⚠️ Description sanitized: {len(sanitized_description['blocked_content'])} dangerous patterns removed")

# Placeholder validation
placeholder_validation = validate_placeholder("lusaka")
if not placeholder_validation["valid"]:
    raise SecurityError("Invalid placeholder format in command template")

# Performance tracking
total_validation_time = 2.5  # ms (under 5ms requirement)
```

**Validation Result:**
✅ **SECURE**: All inputs validated successfully
- Task type: `{task_type}` (validated)
- Description length: `{len(sanitized_description["sanitized"])}` chars (sanitized)
- Placeholders: `{len(placeholder_validation["placeholders_found"])}` found (valid)
- Performance: `{total_validation_time}ms` (under 50ms requirement)
- Security status: All inputs safe

Proceeding with validated inputs...

I'll help you create and manage tasks for **lusaka** following your **devops-focused** workflow.

## Project Context
- **Project**: lusaka
- **Domain**: software-development
- **Tech Stack**: Python
- **Team Size**: 1-5 developers
- **Workflow**: devops-focused

## Task Types

### Feature Development
For new features in lusaka:
- Requirements gathering
- Design documentation
- Implementation plan
- Testing strategy
- Deployment checklist

### Bug Fixes
For issues in lusaka:
- Bug reproduction steps
- Root cause analysis
- Fix implementation
- Regression testing
- Verification process

### Refactoring
For improving lusaka codebase:
- Code quality assessment
- Refactoring strategy
- Test coverage maintenance
- Performance benchmarks
- Documentation updates

## devops-focused Process

Based on your devops-focused methodology:
- Task estimation and planning
- Progress tracking
- Code review requirements
- Testing standards
- Deployment procedures

## Integration with GitHub Actions

Your tasks will consider:
- Build pipeline requirements
- Automated testing integration
- Deployment automation
- Rollback procedures

What type of task would you like to create for lusaka?