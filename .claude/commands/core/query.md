---
command: query
description: Intelligent codebase query and analysis with deep Python understanding and architectural insights
category: core
parameters: 
  - name: QUESTION
    type: string
    required: true
    description: Question about codebase architecture, implementation, patterns, or dependencies
usage_examples:
  - "/query 'How does authentication work in this system?'"
  - "/query 'What design patterns are used here?'"
  - "/query 'Where are the performance bottlenecks?'"
  - "/query 'How is the database accessed?'"
prerequisites: 
  - "Codebase accessible for analysis"
  - "Project files readable"
output_format: structured
tags: [codebase-analysis, architecture, query, patterns, dependencies, v2-enhanced]
version: "2.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Grep
- Glob
---

# /query - Intelligent Codebase Analysis v2.0

<context type="project">
Advanced codebase query system for lusaka template library with deep Python understanding, architectural analysis capabilities, dependency mapping, and performance insights. Supports comprehensive code exploration and pattern recognition.
</context>

<instructions>
Analyze codebase and provide intelligent responses to $QUESTION using comprehensive code exploration, pattern recognition, and architectural analysis. Deliver structured insights with code examples, file locations, and actionable recommendations.
</instructions>

## Usage Examples

<examples>
<example>
<input>/query "How does authentication work in this system?"</input>
<expected_output>Detailed explanation of authentication flow with code snippets, file locations, and security analysis</expected_output>
</example>
<example>
<input>/query "What design patterns are used here?"</input>
<expected_output>Comprehensive pattern analysis with examples of MVC, Repository, Factory patterns and their implementations</expected_output>
</example>
<example>
<input>/query "Where are the performance bottlenecks?"</input>
<expected_output>Performance analysis with specific bottleneck locations, metrics, and optimization recommendations</expected_output>
</example>
<example>
<input>/query "What are the external dependencies?"</input>
<expected_output>Complete dependency map with versions, usage patterns, and potential security considerations</expected_output>
</example>
</examples>

## Codebase Analysis Workflow

<workflow type="sequential">
<task priority="high">
**Query Processing**: Parse and understand the question context
- Analyze $QUESTION for specific technical focus areas
- Identify scope: architecture, implementation, patterns, performance, security
- Determine required analysis depth and exploration strategy
</task>

<task priority="high">
**Codebase Exploration**: Systematic code discovery and analysis
- Use Read, Grep, and Glob tools for comprehensive code search
- Identify relevant files, functions, and patterns
- Map relationships between components and dependencies
- Extract code examples and implementation details
</task>

<task priority="high">
**Pattern Recognition**: Identify architectural and design patterns
- Recognize common design patterns (MVC, Repository, Factory, Observer)
- Analyze architectural patterns and their implementation
- Identify best practices and anti-patterns
- Assess code quality and maintainability factors
</task>

<task priority="medium">
**Insight Generation**: Provide actionable analysis and recommendations
- Generate comprehensive explanations with context
- Provide specific file locations and code references
- Identify potential improvements and optimization opportunities
- Assess security considerations and compliance factors
</task>
</workflow>

## 🔍 Query Capabilities

### **Code Understanding:**
- Authentication and authorization flows
- Business logic implementation and organization
- Design patterns and architectural decisions
- Data models and database interactions

### **Architecture Analysis:**
- Overall system architecture and component relationships
- Service organization and API structure
- State management and data flow patterns
- Integration points and external dependencies

### **Performance Insights:**
- Performance bottlenecks and optimization opportunities
- Caching strategies and implementation
- Database query optimization
- Scaling considerations and architectural limits

### **Security Analysis:**
- Security vulnerabilities and risk assessment
- Authentication and authorization implementation
- Input validation and sanitization patterns
- Compliance with security best practices

### **Dependency Mapping:**
- External library usage and integration patterns
- Component dependencies and relationships
- Circular dependency detection
- Version compatibility and upgrade paths

<automation trigger="completion">
- Generate comprehensive analysis report with findings
- Provide file references and code examples for all insights
- Suggest related queries for deeper exploration
- Update analysis cache for improved performance on similar queries
</automation>