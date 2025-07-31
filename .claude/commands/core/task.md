---
command: task
description: Execute a focused development task with best practices and quality standards
category: workflow
parameters: 
  - name: TASK_DESCRIPTION
    type: string
    required: true
    description: Detailed description of the development task to be implemented
usage_examples:
  - "/task create email validation utility function"
  - "/task implement user authentication middleware"
  - "/task add pagination to the user listing component"
prerequisites: 
  - "Git repository initialized"
  - "Project dependencies installed"
  - "Development environment configured"
output_format: structured
tags: [development, implementation, testing, documentation, quality]
version: "2.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Write
- Edit
- Grep
- Glob
- Bash
---

# /task - Focused Development Workflow

<context type="project">
lusaka template library specializing in Claude Code command development with Python-focused implementation patterns, automated testing integration, and comprehensive documentation standards.
</context>

<instructions>
Execute a focused development task using industry best practices, quality standards, and systematic approach. Process $TASK_DESCRIPTION with comprehensive analysis, implementation, testing, and documentation.
</instructions>

## Usage Examples

<examples>
<example>
<input>/task "create email validation utility function"</input>
<expected_output>Complete utility function with regex validation, error handling, unit tests, and documentation</expected_output>
</example>
<example>
<input>/task "implement user authentication middleware"</input>
<expected_output>Middleware with JWT handling, error responses, security headers, and integration tests</expected_output>
</example>
<example>
<input>/task "add pagination to user listing component"</input>
<expected_output>Component with page controls, data fetching, loading states, and unit tests</expected_output>
</example>
</examples>

## Implementation Workflow

<workflow type="sequential">
<task priority="high">
**Analysis Phase**: Understand requirements, dependencies, and context
- Parse $TASK_DESCRIPTION for technical requirements
- Identify affected files and components  
- Determine testing strategy and documentation needs
</task>

<task priority="high">
**Design Phase**: Plan implementation approach and architecture
- Design API interfaces and data structures
- Plan error handling and edge cases
- Consider performance and security implications
</task>

<task priority="high">
**Implementation Phase**: Write clean, maintainable code
- Follow established coding standards and patterns
- Implement core functionality with proper error handling
- Add logging and monitoring where appropriate
</task>

<task priority="medium">
**Testing Phase**: Comprehensive test coverage
- Unit tests for individual functions/methods
- Integration tests for component interactions
- End-to-end tests for complete workflows
</task>

<task priority="medium">
**Documentation Phase**: Update relevant documentation
- Code comments and docstrings
- README updates for new features
- API documentation where applicable
</task>
</workflow>

<automation trigger="completion">
- Run test suite to verify functionality
- Check code quality and standards compliance
- Update project documentation and examples
</automation>
