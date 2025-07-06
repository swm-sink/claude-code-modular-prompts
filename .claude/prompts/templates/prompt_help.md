# /prompt Command Help

## Synopsis
`/prompt <subcommand> [arguments] [options]`

## Description
The `/prompt` command provides systematic AI prompt engineering workflows for creating, evaluating, testing, and improving prompts with evidence-based methodology.

## Subcommands

### create
Create new prompts with best practices and patterns
```
/prompt create <name> [--type TYPE] [--framework FRAMEWORK] [--style STYLE]
```

### evaluate  
Analyze prompt effectiveness and identify improvements
```
/prompt evaluate <prompt_file> [--metrics METRICS] [--comprehensive]
```

### test
Test prompts against various scenarios and edge cases
```
/prompt test <prompt_file> [--scenarios SCENARIOS] [--output OUTPUT]
```

### improve
Iteratively enhance prompts based on evaluation results
```
/prompt improve <prompt_file> [--iterations N] [--target METRIC] [--based-on RESULTS]
```

## Options

### Global Options
- `--help`: Show this help message
- `--version`: Show command version
- `--verbose`: Enable detailed output

### create Options
- `--type`: Prompt type (system|user|assistant|hybrid) [default: system]
- `--framework`: Target AI framework (claude|gpt|general) [default: claude]
- `--style`: Communication style (directive|conversational|structured|narrative) [default: directive]
- `--template`: Use specific template from library

### evaluate Options
- `--metrics`: Evaluation metrics (clarity|specificity|robustness|effectiveness|all) [default: all]
- `--comprehensive`: Generate detailed evaluation report
- `--compare-with`: Compare against another prompt file
- `--output`: Save results to file

### test Options
- `--scenarios`: Test scenarios (basic|edge-cases|adversarial|all) [default: basic]
- `--iterations`: Number of test iterations [default: 1]
- `--output`: Output format (console|file|both) [default: console]
- `--timeout`: Test timeout in seconds [default: 30]

### improve Options
- `--iterations`: Number of improvement cycles [default: 1]
- `--target`: Target metric to optimize
- `--based-on`: Use specific test/evaluation results
- `--preserve`: Elements to keep unchanged

## Examples

### Basic Usage
```bash
# Create a new system prompt
/prompt create "code-reviewer"

# Evaluate an existing prompt
/prompt evaluate "my-prompt.md"

# Test with edge cases
/prompt test "api-prompt.md" --scenarios edge-cases

# Improve based on test results
/prompt improve "api-prompt.md" --based-on test-results.json
```

### Advanced Workflows
```bash
# Complete development cycle
/prompt create "assistant" && /prompt test && /prompt improve

# Claude-specific optimization
/prompt create "claude-assistant" --framework claude --style conversational

# Production validation
/prompt test "prod-prompt.md" --scenarios all --output validation-report.md
```

## File Structure

### Input Files
- Prompts: `.md` files with structured content
- Templates: `.claude/prompts/templates/*.md`
- Test scenarios: `.claude/prompts/tests/*.json`

### Output Files  
- Created prompts: `prompts/{name}_{version}.md`
- Evaluation reports: `evaluation_{name}_{timestamp}.md`
- Test results: `test_results_{name}_{timestamp}.json`
- Improvement logs: `CHANGELOG_{name}.md`

## Integration

### With Other Commands
- `/swarm`: For complex multi-prompt systems
- `/session`: For tracked improvement workflows
- `/auto`: For intelligent prompt development
- `/protocol`: For production deployment validation

### With Framework Modules
- `patterns/research-analysis.md`: Research best practices
- `quality/critical-thinking.md`: Validate assumptions
- `patterns/session-management.md`: Track complex workflows

## Best Practices

1. **Research First**: Always research current best practices
2. **Test Thoroughly**: Use all scenario types before production
3. **Version Control**: Leverage automatic versioning
4. **Metric-Driven**: Let data guide improvements
5. **Document Changes**: Maintain clear changelogs

## Troubleshooting

### Common Errors
- `Invalid subcommand`: Check spelling (create|evaluate|test|improve)
- `File not found`: Verify file path and extension
- `Test failure`: Review prompt syntax and structure
- `Missing parameters`: Check required arguments

### Debug Mode
```bash
# Enable verbose output
/prompt create "debug-test" --verbose

# Check command version
/prompt --version
```

## See Also
- `.claude/examples/prompt_command_usage.md`: Detailed usage examples
- `.claude/modules/development/prompt-engineering.md`: Implementation details
- `.claude/prompts/templates/`: Prompt templates library

## Version
1.0.0 - Initial implementation with core functionality