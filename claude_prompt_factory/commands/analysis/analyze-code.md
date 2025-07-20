# Analyze Code Command

## Overview
The `/analyze code` command provides comprehensive code analysis focusing on structure, patterns, complexity, and improvement opportunities across multiple languages.

## Usage
```bash
/analyze code [file_path] [focus_area]
```

## Focus Areas
- **structure** - Architecture patterns and organization
- **complexity** - Cyclomatic complexity and code metrics  
- **patterns** - Design patterns and anti-patterns
- **quality** - Code smells and maintainability
- **performance** - Performance bottlenecks and optimizations
- **security** - Security vulnerabilities and best practices

## Analysis Process
1. **Code Structure Review**
   - Component relationships and dependencies
   - Architectural patterns identification
   - Module cohesion and coupling analysis

2. **Complexity Analysis**
   - Cyclomatic complexity metrics
   - Function/method length assessment
   - Nesting depth evaluation

3. **Pattern Recognition**
   - Design patterns usage
   - Anti-pattern detection
   - Code duplication identification

4. **Quality Assessment**
   - Code smell detection
   - Maintainability scoring
   - Technical debt identification

5. **Improvement Recommendations**
   - Refactoring opportunities
   - Performance optimization suggestions
   - Best practice adherence

## Supported Languages
Python, JavaScript, TypeScript, Java, C#, Go, Rust, PHP, Ruby

## Output Format
- Executive summary with key findings
- Detailed analysis by category
- Code examples with specific issues
- Prioritized improvement recommendations
- Metrics dashboard with scores

## Example Usage
```bash
/analyze code src/auth/models.py security
/analyze code . complexity
/analyze code components/ patterns
```