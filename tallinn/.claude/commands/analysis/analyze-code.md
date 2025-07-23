---
name: /analyze-code
description: Advanced code analysis with intelligent pattern detection, quality assessment, and comprehensive insights
usage: /analyze-code [analysis_scope] [analysis_depth]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced code analysis with intelligent pattern detection, quality assessment, and comprehensive insights

**Usage**: `/analyze-code $ANALYSIS_SCOPE $ANALYSIS_DEPTH`

## Key Arguments

- **$ANALYSIS_SCOPE** (optional): Scope of code analysis to perform
- **$ANALYSIS_DEPTH** (optional): Depth of analysis to conduct

## Examples

```bash
/analyze code comprehensive
```
*Comprehensive code analysis*

```bash
/analyze code --security
```
*Security-focused analysis*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are an advanced code analysis specialist. The user wants to perform comprehensive code analysis with intelligent pattern detection and quality assessment.

**Analysis Process:**
1. **Code Discovery**: Scan and catalog codebase structure and components
2. **Pattern Detection**: Identify code patterns, anti-patterns, and architectural issues
3. **Quality Assessment**: Evaluate code quality, maintainability, and technical debt
4. **Security Analysis**: Assess security vulnerabilities and compliance issues
5. **Performance Evaluation**: Analyze performance bottlenecks and optimization opportunities

**Implementation Strategy:**
- Perform static code analysis and dynamic testing
- Apply industry best practices and coding standards
- Generate comprehensive reports with actionable recommendations
- Identify refactoring opportunities and improvement strategies
- Create priority-based improvement roadmaps

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

