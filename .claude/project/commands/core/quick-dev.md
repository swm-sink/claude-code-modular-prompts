---
name: quick-dev
description: Universal development assistance with instant analysis - works with any codebase and technology stack
category: core
parameters: 
  - name: ACTION
    type: string
    required: false
    description: Development action (--review, --debug, --optimize, --explain)
  - name: TARGET
    type: string
    required: false
    description: File path, directory, or description of the problem/area to analyze
usage_examples:
  - "/quick-dev --review src/components/UserForm.js"
  - "/quick-dev --debug 'users cannot log in'"
  - "/quick-dev --optimize 'slow database queries'"
  - "/quick-dev --explain src/auth/middleware.py"
prerequisites: 
  - "Codebase accessible for analysis"
  - "Target files readable"
output_format: structured
tags: [development, code-review, debugging, optimization, universal, v2-enhanced]
version: "1.0"
author: "template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Edit
- Bash
- Grep
- Glob
---

# 🛠️ Universal Development Assistance v1.0

<context type="project">
Instant development assistance system for context engineering system with universal language support and multi-mode analysis. Supports code review, debugging, optimization, and explanation across all technology stacks with smart context detection and framework-specific guidance.
</context>

<instructions>
Provide immediate development assistance using $ACTION parameter to determine analysis type and $TARGET for focus area. Support universal language detection, framework-specific guidance, and comprehensive code analysis with actionable recommendations.
</instructions>

## Usage Examples

<examples>
<example>
<input>/quick-dev --review src/components/UserForm.js</input>
<expected_output>Comprehensive code review with quality issues, security vulnerabilities, and improvement suggestions</expected_output>
</example>
<example>
<input>/quick-dev --debug "users cannot log in"</input>
<expected_output>Systematic debugging analysis with authentication flow examination and specific fix recommendations</expected_output>
</example>
<example>
<input>/quick-dev --optimize database/queries.sql</input>
<expected_output>Performance analysis with bottleneck identification, query optimization, and indexing recommendations</expected_output>
</example>
<example>
<input>/quick-dev --explain src/auth/middleware.py</input>
<expected_output>Code explanation with architecture analysis, pattern identification, and functionality breakdown</expected_output>
</example>
</examples>

## Development Assistance Workflow

<workflow type="conditional">
<task priority="high">
**Action Detection & Context Loading**: Determine development assistance mode
- Parse $ACTION for operation type: review, debug, optimize, explain
- Identify $TARGET scope: file, directory, or problem description
- Load relevant codebase context and detect technology stack
- Initialize framework-specific analysis patterns
</task>

<task priority="high">
**Code Review Mode** ($ACTION = --review): Quality and security analysis
- Comprehensive code quality assessment
- Security vulnerability scanning and risk analysis
- Best practices compliance checking
- Architecture pattern evaluation and recommendations
</task>

<task priority="high">
**Debug Mode** ($ACTION = --debug): Problem diagnosis and resolution
- Systematic problem analysis and root cause identification
- Code flow tracing and dependency mapping
- Error pattern recognition and resolution strategies
- Testing recommendations and validation approaches
</task>

<task priority="high">
**Optimize Mode** ($ACTION = --optimize): Performance enhancement
- Performance bottleneck identification and analysis
- Database query optimization and indexing recommendations
- Caching strategy evaluation and implementation guidance
- Scaling considerations and architectural improvements
</task>

<task priority="medium">
**Explain Mode** ($ACTION = --explain): Code understanding and documentation
- Comprehensive code explanation with architectural context
- Design pattern identification and implementation analysis
- Functionality breakdown with usage examples
- Documentation generation and improvement suggestions
</task>

<task priority="medium">
**Universal Language Support**: Framework-specific guidance
- Automatic language and framework detection
- Technology-specific best practices application
- Framework-appropriate solution recommendations
- Integration pattern suggestions and compatibility analysis
</task>
</workflow>

## 🚀 Multi-Mode Analysis Capabilities

### **Code Review (--review):**
- Code quality and maintainability assessment
- Security vulnerability identification and remediation
- Performance impact analysis and optimization opportunities
- Architecture pattern evaluation and improvement recommendations

### **Debugging (--debug):**
- Root cause analysis with systematic problem breakdown
- Error flow tracing and dependency impact assessment
- Resolution strategy development with implementation guidance
- Prevention recommendations and testing improvements

### **Optimization (--optimize):**
- Performance bottleneck identification with metrics analysis
- Database optimization with query improvement recommendations
- Caching strategy evaluation and implementation guidance
- Scalability assessment with architectural enhancement suggestions

### **Explanation (--explain):**
- Comprehensive code breakdown with architectural context
- Design pattern identification and implementation analysis
- Functionality documentation with usage examples
- Learning resources and best practice guidance

## 🌍 Universal Technology Support

### **Language Agnostic Analysis:**
- **Frontend**: React, Vue, Angular, Svelte, vanilla JavaScript, TypeScript
- **Backend**: Python, Node.js, Java, Go, Rust, C#, PHP, Ruby
- **Mobile**: React Native, Flutter, Swift, Kotlin, Xamarin
- **Databases**: PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch
- **DevOps**: Docker, Kubernetes, AWS, Azure, GCP, CI/CD pipelines

### **Smart Context Detection:**
- Automatic programming language and framework identification
- Project structure analysis and convention recognition
- Dependency mapping and integration pattern detection
- Best practice application based on detected technology stack

<automation trigger="completion">
- Generate comprehensive analysis report with actionable recommendations
- Provide specific code examples and implementation guidance
- Suggest related development areas for further improvement
- Update development assistance patterns based on technology detection
</automation>