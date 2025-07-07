# /prompt Command Usage Examples

## Overview
The `/prompt` command provides systematic AI prompt engineering workflows for creating, evaluating, testing, and improving prompts.

## Basic Usage

### 1. Creating a New Prompt
```bash
# Create a system prompt for code review
/prompt create "code review assistant" --type system --style directive

# Create a user prompt template
/prompt create "bug report template" --type user --format structured

# Create a Claude-optimized prompt
/prompt create "feature generator" --framework claude --style conversational
```

### 2. Evaluating Existing Prompts
```bash
# Evaluate all metrics
/prompt evaluate "my-prompt.md"

# Focus on specific metrics
/prompt evaluate "api-design.md" --metrics clarity,specificity

# Comprehensive evaluation with report
/prompt evaluate ".claude/prompts/system-prompt.md" --comprehensive
```

### 3. Testing Prompts
```bash
# Basic testing
/prompt test "refactoring-prompt.md"

# Test with edge cases
/prompt test "validation-prompt.md" --scenarios edge-cases

# Full test suite with report
/prompt test "critical-prompt.md" --scenarios all --output report.md
```

### 4. Improving Prompts
```bash
# Basic improvement
/prompt improve "current-prompt.md"

# Iterative improvement
/prompt improve "assistant-prompt.md" --iterations 3

# Targeted improvement
/prompt improve "system-prompt.md" --target clarity --based-on test-results.json
```

## Advanced Workflows

### Complete Development Cycle
```bash
# Create, test, and improve in one workflow
/prompt create "feature generator" && /prompt test && /prompt improve
```

### A/B Testing
```bash
# Create variations
/prompt create "assistant-v1" --style directive
/prompt create "assistant-v2" --style conversational

# Test both versions
/prompt test "assistant-v1.md" --output v1-results.json
/prompt test "assistant-v2.md" --output v2-results.json

# Compare and improve winner
/prompt evaluate "assistant-v1.md" --compare-with "assistant-v2.md"
```

### Production Deployment
```bash
# Full validation before deployment
/prompt test "production-prompt.md" --scenarios all
/prompt evaluate "production-prompt.md" --metrics all
/protocol validate "production-prompt.md"  # Requires production standards
```

## Parameter Reference

### --type
- `system`: System-level prompts (default)
- `user`: User input templates
- `assistant`: Assistant response patterns
- `hybrid`: Combined prompt types

### --framework
- `claude`: Claude-specific optimizations (default)
- `gpt`: GPT-compatible format
- `general`: Framework-agnostic

### --style
- `directive`: Clear instructions (default)
- `conversational`: Natural dialogue
- `structured`: Formal templates
- `narrative`: Story-like flow

### --metrics
- `clarity`: Language clarity and unambiguity
- `specificity`: Detail and precision
- `robustness`: Error handling capability
- `effectiveness`: Goal achievement likelihood
- `all`: All metrics (default)

### --scenarios
- `basic`: Standard use cases (default)
- `edge-cases`: Boundary conditions
- `adversarial`: Security testing
- `all`: Complete test suite

## Integration with Other Commands

### With /swarm for Complex Prompt Systems
```bash
# Design multi-prompt system
/swarm "Design conversational AI prompt system with context management"
```

### With /session for Tracking
```bash
# Create tracked improvement session
/session start "Prompt Optimization Sprint"
/prompt evaluate "all-prompts/*.md" --output baseline.json
/prompt improve "all-prompts/*.md" --iterations 5
/session complete
```

### With /auto for Intelligent Routing
```bash
# Let auto determine best approach
/auto "Help me create better prompts for my documentation generator"
```

## Best Practices

1. **Always Test Before Production**: Use comprehensive test scenarios
2. **Version Control**: All prompts are automatically versioned
3. **Metric-Driven**: Use evaluation metrics to guide improvements
4. **Document Changes**: Changelog automatically maintained
5. **Framework-Specific**: Optimize for your target AI system

## Common Patterns

### Research-First Prompt Development
```bash
# Research best practices first
/query "current best practices for Claude system prompts"
# Then create based on findings
/prompt create "optimized-system" --framework claude
```

### Continuous Improvement
```bash
# Regular optimization cycle
/prompt evaluate "production/*.md" --output monthly-report.md
/prompt improve "production/*.md" --based-on monthly-report.md
```

### Error Recovery
```bash
# If prompt fails testing
/prompt test "failing-prompt.md" --scenarios all --output failures.json
/prompt improve "failing-prompt.md" --based-on failures.json --focus error-handling
```

## Output Examples

### Evaluation Report
```markdown
# Prompt Evaluation Report
Generated: 2024-01-15 10:30:00

## Metrics Summary
- Clarity: 8.5/10
- Specificity: 7.2/10
- Robustness: 6.8/10
- Effectiveness: 8.0/10

## Recommendations
1. Add edge case handling for null inputs
2. Clarify ambiguous terms in section 3
3. Include more concrete examples
```

### Test Results
```json
{
  "test_suite": "refactoring-prompt",
  "timestamp": "2024-01-15T10:35:00Z",
  "summary": {
    "total_tests": 25,
    "passed": 22,
    "failed": 3,
    "success_rate": 0.88
  },
  "failures": [
    {
      "scenario": "empty_input",
      "error": "No fallback behavior defined"
    }
  ]
}
```

## Troubleshooting

### Common Issues

1. **"Prompt file not found"**
   - Ensure file path is correct
   - Check file extension (.md expected)

2. **"Invalid subcommand"**
   - Use: create, evaluate, test, or improve
   - Check spelling and syntax

3. **"Test execution failed"**
   - Review prompt syntax
   - Check for XML/JSON formatting issues
   - Ensure all required sections present

### Getting Help
```bash
# Display command help
/prompt --help

# Show examples
/prompt --examples

# Check version
/prompt --version
```