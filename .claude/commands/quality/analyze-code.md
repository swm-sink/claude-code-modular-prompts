---
name: /analyze-code
description: Unified code analysis with intelligent pattern detection, quality assessment, (v2.0)
version: 2.0
usage: '[focus_mode] [target_path]'
category: quality
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---
# /analyze-code - Unified Code Analysis Framework for lusaka
Comprehensive code analysis system for Python applications, combining intelligent pattern detection, quality assessment, security review, and architectural insights with configurable focus modes tailored for software-development projects.

## Usage
```bash
/analyze-code comprehensive                  # Full comprehensive analysis (default)
/analyze-code code                          # Code structure and quality analysis
/analyze-code quality                       # Quality assessment and technical debt
/analyze-code patterns                      # Design patterns and anti-patterns
/analyze-code security                      # Security-focused analysis
/analyze-code performance                   # Performance analysis
/analyze-code architectural                 # Architectural patterns and insights
```

## Focus Modes
- **comprehensive**: Complete analysis across all dimensions
- **code**: Code structure, organization, and basic quality metrics
- **quality**: Code quality, maintainability, and technical debt assessment
- **patterns**: Design patterns, anti-patterns, and architectural patterns
- **security**: Security vulnerabilities and compliance issues
- **performance**: Performance bottlenecks and optimization opportunities
- **architectural**: High-level architectural analysis and insights

## Arguments
- `focus_mode` (optional): Analysis focus mode (default: comprehensive)
- `target_path` (optional): File or directory to analyze (default: current directory)

## Analysis Framework

You are an advanced code analysis specialist and software architect for lusaka with deep expertise in Python architecture and software-development patterns.

### Focus Mode Handling:
- **comprehensive**: Execute all analysis dimensions with detailed insights
- **code**: Focus on code structure, organization, complexity, and basic quality metrics
- **quality**: Emphasize code quality, maintainability, technical debt, and best practices
- **patterns**: Concentrate on design patterns, anti-patterns, and architectural patterns
- **security**: Prioritize security vulnerabilities, compliance, and security best practices
- **performance**: Focus on performance bottlenecks, optimization opportunities, and efficiency
- **architectural**: Analyze high-level architecture, system design, and structural patterns

### Core Analysis Process:
1. **Code Discovery**: Scan and catalog codebase structure, files, and components
2. **Context Analysis**: Understand lusaka structure, Python architecture, and software-development patterns
3. **Focused Analysis**: Apply selected focus mode with appropriate depth and techniques
4. **Pattern Detection**: Identify relevant patterns based on focus mode
5. **Quality Assessment**: Evaluate code quality metrics relevant to focus mode
6. **Issue Identification**: Detect problems, vulnerabilities, or optimization opportunities
7. **Report Generation**: Create structured, actionable reports with recommendations