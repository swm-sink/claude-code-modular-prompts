# /review - Code Review & Quality Analysis

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Conduct comprehensive code review and quality analysis to ensure code meets project standards, is maintainable, secure, and performs well. Ideal for reviewing changes, analyzing code quality, and providing improvement suggestions.

**Note**: This is a simplified version that focuses on core review functionality without complex quality gate enforcement.

---

## How It Works

### 1. Code Analysis
- **Structure Review**: Analyze code organization and architecture
- **Quality Assessment**: Evaluate code quality and maintainability
- **Pattern Recognition**: Identify design patterns and anti-patterns
- **Convention Compliance**: Check adherence to coding standards

### 2. Security & Performance
- **Security Analysis**: Identify potential security vulnerabilities
- **Performance Review**: Assess performance implications
- **Resource Usage**: Evaluate memory and computational efficiency
- **Error Handling**: Review error handling and edge cases

### 3. Testing & Documentation
- **Test Coverage**: Analyze test coverage and quality
- **Documentation Review**: Evaluate code documentation
- **API Design**: Review API design and usability
- **Maintainability**: Assess long-term maintainability

### 4. Recommendations
- **Improvement Suggestions**: Provide actionable recommendations
- **Best Practices**: Suggest industry best practices
- **Refactoring Opportunities**: Identify refactoring opportunities
- **Risk Assessment**: Highlight potential risks and mitigation

---

## Usage Examples

```bash
# Review specific files
/review "src/auth.js" "src/user.js"

# Review recent changes
/review --recent-changes

# Review pull request
/review --pr 123

# Security-focused review
/review --focus security "src/payment/"

# Performance review
/review --focus performance "src/database/"

# Full codebase review
/review --full-review
```

---

## What It Does

### Code Quality Analysis
- Evaluates code structure and organization
- Identifies code smells and anti-patterns
- Checks coding standards compliance
- Assesses maintainability and readability

### Security Assessment
- Identifies security vulnerabilities
- Reviews authentication and authorization
- Checks input validation and sanitization
- Evaluates data protection measures

### Performance Review
- Analyzes algorithmic complexity
- Identifies performance bottlenecks
- Reviews resource usage patterns
- Suggests optimization opportunities

### Testing Analysis
- Evaluates test coverage and quality
- Reviews test structure and organization
- Identifies gaps in testing
- Suggests testing improvements

---

## Review Types

### Code Quality Review
```
PURPOSE: Assess overall code quality and maintainability
FOCUS: Structure, patterns, conventions, readability
OUTPUT: Quality score, improvement suggestions, refactoring opportunities
```

### Security Review
```
PURPOSE: Identify security vulnerabilities and risks
FOCUS: Authentication, authorization, input validation, data protection
OUTPUT: Security assessment, vulnerability report, mitigation strategies
```

### Performance Review
```
PURPOSE: Analyze performance and optimization opportunities
FOCUS: Algorithms, resource usage, bottlenecks, efficiency
OUTPUT: Performance analysis, optimization suggestions, benchmarking
```

### Architecture Review
```
PURPOSE: Evaluate system design and architecture
FOCUS: Design patterns, modularity, scalability, maintainability
OUTPUT: Architecture assessment, design recommendations, improvement plan
```

---

## Output Format

### Review Summary
```
REVIEW_TYPE: [code-quality/security/performance/architecture]
SCOPE: [files-or-components-reviewed]
OVERALL_SCORE: [score-or-rating]
CRITICAL_ISSUES: [number-of-critical-issues]
```

### Quality Analysis
```
CODE_QUALITY: [quality-assessment-and-score]
MAINTAINABILITY: [maintainability-evaluation]
PATTERNS: [design-patterns-and-anti-patterns]
CONVENTIONS: [coding-standards-compliance]
```

### Security Assessment
```
SECURITY_SCORE: [security-assessment-score]
VULNERABILITIES: [identified-vulnerabilities]
RISKS: [security-risks-and-threats]
MITIGATIONS: [recommended-security-measures]
```

### Performance Analysis
```
PERFORMANCE_SCORE: [performance-assessment-score]
BOTTLENECKS: [identified-performance-bottlenecks]
OPTIMIZATIONS: [optimization-opportunities]
RECOMMENDATIONS: [performance-improvement-suggestions]
```

### Recommendations
```
IMMEDIATE_ACTIONS: [urgent-issues-to-address]
IMPROVEMENTS: [suggested-improvements]
BEST_PRACTICES: [recommended-best-practices]
REFACTORING: [refactoring-opportunities]
```

---

## Review Categories

### Critical Issues
- **Security Vulnerabilities**: High-risk security issues
- **Performance Bottlenecks**: Severe performance problems
- **Logic Errors**: Incorrect or dangerous logic
- **Data Integrity**: Data corruption or loss risks

### Major Issues
- **Code Smells**: Significant code quality problems
- **Design Problems**: Poor architectural decisions
- **Resource Leaks**: Memory or resource management issues
- **Error Handling**: Inadequate error handling

### Minor Issues
- **Code Style**: Formatting and style inconsistencies
- **Documentation**: Missing or inadequate documentation
- **Test Coverage**: Insufficient test coverage
- **Naming**: Poor variable or function naming

### Improvements
- **Refactoring**: Code restructuring opportunities
- **Optimization**: Performance improvement opportunities
- **Best Practices**: Industry standard practices
- **Maintainability**: Long-term maintenance improvements

---

## Key Features

### ✅ Comprehensive Analysis
- Multi-faceted code review approach
- Security, performance, and quality analysis
- Pattern recognition and anti-pattern identification
- Comprehensive documentation review

### ✅ Actionable Feedback
- Clear, specific recommendations
- Prioritized issue identification
- Concrete improvement suggestions
- Best practice recommendations

### ✅ Flexible Scope
- Single file to full codebase review
- Focused reviews (security, performance, etc.)
- Pull request and change reviews
- Continuous integration support

### ✅ Quality Metrics
- Quantitative quality assessment
- Security and performance scoring
- Test coverage analysis
- Maintainability evaluation

---

## Review Process

### 1. Scope Definition
- Define review scope and focus areas
- Identify files and components to review
- Set review criteria and standards
- Plan review approach and timeline

### 2. Code Analysis
- Analyze code structure and organization
- Evaluate design patterns and architecture
- Check coding standards compliance
- Assess readability and maintainability

### 3. Quality Assessment
- Evaluate code quality metrics
- Identify code smells and anti-patterns
- Assess test coverage and quality
- Review documentation completeness

### 4. Security & Performance
- Conduct security vulnerability analysis
- Evaluate performance characteristics
- Identify optimization opportunities
- Assess resource usage patterns

### 5. Recommendations
- Compile findings and analysis results
- Prioritize issues and recommendations
- Provide actionable improvement suggestions
- Create improvement roadmap

---

## Best Practices

### When to Use
- **Pre-deployment**: Before releasing code to production
- **Pull Requests**: During code review process
- **Quality Audits**: Regular code quality assessments
- **Security Reviews**: Security-focused analysis

### Review Tips
- Focus on most critical issues first
- Provide specific, actionable feedback
- Consider long-term maintainability
- Balance thoroughness with practicality
- Include positive feedback and recognition

### Quality Guidelines
- Use consistent review criteria
- Document review findings clearly
- Provide examples and suggestions
- Follow up on recommendations
- Maintain review quality standards

---

## Error Handling

### Common Issues
- **Large Codebases**: Focuses on most critical areas
- **Complex Logic**: Breaks down into manageable components
- **Missing Context**: Requests additional information
- **Incomplete Code**: Reviews available code with limitations noted

### Graceful Degradation
- Provides partial review when full analysis not possible
- Focuses on most critical issues when time-constrained
- Suggests follow-up reviews for complex areas
- Documents limitations and recommendations

---

## Integration

### Works Well With
- `/context-prime` - For project context before review
- `/research` - For investigating complex issues found
- `/task` - For implementing review recommendations
- `/refactor` - For addressing code quality issues

### Typical Workflow
1. **Context**: `/context-prime` to understand project context
2. **Review**: `/review` to analyze code quality and issues
3. **Research**: `/research` to investigate complex issues
4. **Implementation**: `/task` or `/refactor` to address findings

---

## Review Metrics

### Quality Score
- **Code Quality**: Structure, patterns, conventions
- **Test Coverage**: Test completeness and quality
- **Documentation**: Code and API documentation
- **Maintainability**: Long-term maintenance ease

### Security Score
- **Vulnerability Count**: Number of security issues
- **Risk Level**: Severity of security risks
- **Compliance**: Security standard compliance
- **Best Practices**: Security best practice adherence

### Performance Score
- **Efficiency**: Algorithmic and resource efficiency
- **Bottlenecks**: Performance bottleneck identification
- **Optimization**: Optimization opportunity assessment
- **Scalability**: Scalability considerations

---

## Review Focus Areas

### Code Structure
- Organization and modularity
- Design patterns and architecture
- Coupling and cohesion
- Separation of concerns

### Security
- Authentication and authorization
- Input validation and sanitization
- Data protection and encryption
- Error handling and information disclosure

### Performance
- Algorithmic complexity
- Resource usage and optimization
- Caching and efficiency
- Scalability considerations

### Testing
- Test coverage and completeness
- Test quality and maintainability
- Integration and unit testing
- Test automation and CI/CD

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple review workflow
- **No Module Dependencies**: Self-contained review logic
- **No Advanced Frameworks**: Basic review and analysis patterns
- **No Mandatory Enforcement**: Supportive quality guidance

### Core Focus
- **Essential Review**: Core code quality, security, and performance analysis
- **Practical Recommendations**: Actionable feedback and suggestions
- **Fast Execution**: Minimal overhead for quick reviews
- **Clear Results**: Well-structured review reports

---

**Note**: This simplified command provides core code review functionality without the complexity of the full framework. For advanced features like complex quality gates, multi-agent review coordination, or advanced security analysis, use the full framework commands.