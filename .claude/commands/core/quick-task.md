---
name: quick-task
description: Universal task execution with intelligent project analysis - works with any project or language without setup
category: core
parameters: 
  - name: TASK_DESCRIPTION
    type: string
    required: true
    description: Clear description of the task you want to accomplish
usage_examples:
  - "/quick-task 'add user authentication to my app'"
  - "/quick-task 'refactor this component to use TypeScript'"
  - "/quick-task 'optimize database queries in the user service'"
  - "/quick-task 'add unit tests for the payment module'"
prerequisites: 
  - "Project files accessible for analysis"
  - "Basic project structure identifiable"
output_format: structured
tags: [universal-task, language-agnostic, framework-flexible, zero-setup, v2-enhanced]
version: "1.0"
author: "template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Write
- Edit
- MultiEdit
- Bash
- Glob
- Grep
---

# 🎯 Universal Task Execution v1.0

<context type="project">
Universal task execution system for template library with intelligent project analysis, language-agnostic implementation, and framework-flexible approach. Works immediately with any project structure without setup or configuration requirements.
</context>

<instructions>
Execute $TASK_DESCRIPTION using comprehensive project analysis, intelligent tech stack detection, and adaptive implementation strategies. Provide structured approach with analysis, planning, execution, and validation phases for universal compatibility.
</instructions>

## Usage Examples

<examples>
<example>
<input>/quick-task "add user authentication to my app"</input>
<expected_output>Complete authentication system implementation with middleware, endpoints, tests, and documentation</expected_output>
</example>
<example>
<input>/quick-task "refactor this component to use TypeScript"</input>
<expected_output>Component conversion to TypeScript with proper typing, interface definitions, and compilation validation</expected_output>
</example>
<example>
<input>/quick-task "optimize database queries in the user service"</input>
<expected_output>Query optimization with performance analysis, indexing recommendations, and implementation improvements</expected_output>
</example>
<example>
<input>/quick-task "add unit tests for the payment module"</input>
<expected_output>Comprehensive test suite with edge cases, mocking strategies, and coverage validation</expected_output>
</example>
</examples>

## Universal Task Execution Workflow

<workflow type="sequential">
<task priority="high">
**Project Analysis & Tech Stack Detection**: Intelligent codebase examination
- Analyze project structure and file organization
- Detect programming languages, frameworks, and dependencies
- Identify existing patterns, conventions, and architectural decisions
- Assess testing setup, build tools, and development environment
</task>

<task priority="high">
**Task Planning & Strategy Development**: Adaptive approach formulation
- Parse $TASK_DESCRIPTION for specific requirements and scope
- Develop implementation strategy based on detected tech stack
- Create step-by-step execution plan with validation checkpoints
- Identify potential challenges and mitigation strategies
</task>

<task priority="high">
**Implementation Execution**: Best practices application
- Execute planned implementation using framework-appropriate patterns
- Follow detected coding conventions and architectural styles
- Implement comprehensive error handling and edge case coverage
- Ensure code quality and maintainability standards
</task>

<task priority="medium">
**Testing & Validation**: Quality assurance and verification
- Create appropriate tests based on detected testing framework
- Validate implementation against requirements and edge cases
- Perform integration testing and compatibility verification
- Update documentation and provide usage examples
</task>
</workflow>

## 🌍 Universal Compatibility Features

### **Language Agnostic Support:**
- **Frontend**: JavaScript, TypeScript, React, Vue, Angular, Svelte
- **Backend**: Python, Node.js, Java, Go, Rust, C#, PHP, Ruby
- **Mobile**: React Native, Flutter, Swift, Kotlin
- **DevOps**: Docker, Kubernetes, CI/CD pipelines, infrastructure

### **Framework Flexible Adaptation:**
- **Web Frameworks**: Express, Django, Spring Boot, Rails, Laravel, ASP.NET
- **Frontend Libraries**: React, Vue.js, Angular, Svelte, jQuery
- **Testing Frameworks**: Jest, Pytest, JUnit, Go Test, RSpec
- **Build Tools**: Webpack, Vite, Rollup, Maven, Gradle, Cargo

### **Intelligent Context Awareness:**
- Automatic project structure analysis and convention detection
- Dependency mapping and integration pattern recognition
- Testing strategy identification and implementation approach
- Documentation style analysis and consistency maintenance

## 🚀 Task Categories & Capabilities

### **Development Tasks:**
- Feature implementation and enhancement
- Code refactoring and optimization
- Bug fixing and debugging assistance
- Architecture improvements and modernization

### **Quality Assurance:**
- Test suite creation and enhancement
- Code review and quality assessment
- Security vulnerability analysis and fixes
- Performance optimization and profiling

### **DevOps & Infrastructure:**
- CI/CD pipeline setup and configuration
- Deployment automation and optimization
- Monitoring and logging implementation
- Security hardening and compliance

### **Documentation & Maintenance:**
- Code documentation and commenting
- API documentation generation
- README and guide creation
- Dependency updates and maintenance

## 📊 Task Command Comparison

**Quick Task Hierarchy:**
- **`/quick-task`**: Universal execution, zero setup *(this command)*
- **`/task`**: Enhanced features with v1.0 metadata and XML workflow
- **`/project-task`**: Complex multi-file operations with orchestration

**When to Use `/quick-task`:**
- Immediate execution without configuration
- Universal project compatibility required
- Simple to moderate complexity tasks
- First-time project interaction

<automation trigger="completion">
- Generate comprehensive implementation report with code examples
- Provide testing validation and quality assurance results
- Suggest related improvements and optimization opportunities
- Update task execution patterns for future universal compatibility
</automation>