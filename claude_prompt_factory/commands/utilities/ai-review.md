---
description: Advanced AI code review with intelligent assessment, quality metrics, and automated improvement suggestions
argument-hint: "[review_scope] [quality_focus]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /ai review - Advanced AI Code Review

Sophisticated AI code review system with intelligent assessment, comprehensive quality metrics, and automated improvement suggestions.

## Usage
```bash
/ai review comprehensive                     # Comprehensive code review
/ai review --security                        # Security-focused review
/ai review --performance                     # Performance optimization review
/ai review --quality                         # Code quality assessment
```

## Examples
- `/ai review src/component.py` - Review single file
- `/ai review api/ --depth=thorough` - Deep API review
- `/ai review --depth=comprehensive --fix` - Full review with fixes
- `/ai review feature/ --score` - Review with quality scores

## Process

Based on enterprise AI review patterns:
1. Analyze code structure and patterns
2. Check adherence to best practices
3. Identify performance optimizations
4. Review error handling and edge cases
5. Assess maintainability and readability
6. Generate scored recommendations

## Review Areas
- **Code Quality**: Structure, naming, complexity
- **Best Practices**: Language-specific conventions
- **Performance**: Bottlenecks and optimizations
- **Security**: Vulnerability patterns
- **Maintainability**: Documentation, modularity
- **Testing**: Coverage and test quality

## Output Format
```
AI CODE REVIEW: component.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Score: 8.2/10

QUALITY BREAKDOWN:
Structure:      9/10  ✓ Well organized
Performance:    7/10  ⚠ Optimization opportunities
Security:       9/10  ✓ No vulnerabilities found
Maintainability: 8/10  ✓ Good documentation

IMPROVEMENTS IDENTIFIED:
[HIGH] Line 45: Extract complex condition to method
  Impact: Readability +2, Maintainability +1
  
[MEDIUM] Line 78: Add input validation
  Impact: Security +1, Robustness +1
```

## Options
- `--depth`: Review thoroughness (quick/thorough/comprehensive)
- `--fix`: Apply suggested improvements
- `--score`: Include numerical quality scores
- `--focus`: Target specific aspects (performance/security/style)

## Related Commands
- `/analyze quality` - Quality metrics analysis
- `/refactor suggest` - Refactoring suggestions
- `/security scan` - Security-focused review