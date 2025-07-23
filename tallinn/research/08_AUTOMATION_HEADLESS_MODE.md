# Automation and Headless Mode

## Overview

Claude Code's headless mode enables non-interactive operation for CI/CD, automation scripts, pre-commit hooks, and build processes. It follows Unix philosophy principles, making it composable and scriptable.

## Basic Headless Mode Usage

### Command Structure

```bash
# Basic syntax
claude -p "Your prompt here"

# With output format
claude -p "Analyze this code" --output-format json

# With streaming JSON
claude -p "Generate report" --output-format stream-json
```

### Simple Examples

```bash
# Analyze CSV data
cat data.csv | claude -p "Who won the most games?"

# Monitor logs
tail -f app.log | claude -p "Alert me if you see any anomalies"

# Quick code review
git diff | claude -p "Review these changes for bugs"
```

## Unix Philosophy Integration

### Composability

Claude Code works seamlessly with Unix pipes and tools:

```bash
# Chain with grep
find . -name "*.js" | claude -p "List files that might have security issues" | grep -i "vulnerable"

# Process and filter
cat package.json | claude -p "List production dependencies" | jq '.dependencies'

# Multi-stage pipeline
git log --oneline -10 | claude -p "Summarize recent changes" | mail -s "Daily Summary" team@company.com
```

### Input Methods

1. **Pipe Input**
   ```bash
   echo "Hello World" | claude -p "Translate to Spanish"
   ```

2. **File Redirection**
   ```bash
   claude -p "Summarize this document" < report.md
   ```

3. **Command Substitution**
   ```bash
   claude -p "Explain this error: $(npm test 2>&1)"
   ```

## Advanced Non-Interactive Features

### Tool Whitelisting

Control which tools Claude can use in headless mode:

```bash
# Allow specific tools
claude -p "Fix the bug in main.js" --allowed-tools Read,Write,Edit

# Deny dangerous tools
claude -p "Analyze codebase" --denied-tools Bash

# Full permission list
claude -p "Deploy application" \
  --allowed-tools Read,Write,Edit,Grep,Glob \
  --denied-tools Bash
```

### Output Formatting

```bash
# JSON output for parsing
claude -p "List all functions" --output-format json > functions.json

# Streaming for real-time processing
claude -p "Monitor deployment" --output-format stream-json | \
  jq -r '.content' | tee deployment.log

# Verbose mode for debugging
claude -p "Debug issue" --verbose --output-format json
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Claude Code Analysis
on: [push, pull_request]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code
      
      - name: Security Analysis
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "Analyze code for security vulnerabilities" \
            --output-format json > security-report.json
      
      - name: Upload Report
        uses: actions/upload-artifact@v3
        with:
          name: security-report
          path: security-report.json
```

### GitLab CI

```yaml
claude-analysis:
  image: node:18
  before_script:
    - npm install -g @anthropic-ai/claude-code
  script:
    - |
      claude -p "Review merge request changes" \
        --allowed-tools Read,Grep \
        --output-format json
  artifacts:
    reports:
      junit: claude-report.xml
```

### Jenkins Pipeline

```groovy
pipeline {
    agent any
    
    stages {
        stage('Claude Analysis') {
            steps {
                script {
                    def analysis = sh(
                        script: '''claude -p "Analyze build artifacts" \
                                  --output-format json''',
                        returnStdout: true
                    )
                    def json = readJSON text: analysis
                    if (json.issues) {
                        error "Claude found issues: ${json.issues}"
                    }
                }
            }
        }
    }
}
```

## Automation Scripts

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check for security issues
ISSUES=$(git diff --cached --name-only | \
  xargs claude -p "Check these files for security vulnerabilities" \
  --output-format json | \
  jq -r '.vulnerabilities[]?')

if [ -n "$ISSUES" ]; then
  echo "Security issues found:"
  echo "$ISSUES"
  exit 1
fi
```

### Automated Documentation

```bash
#!/bin/bash
# generate-docs.sh

# Generate API documentation
find src -name "*.js" -type f | while read file; do
  claude -p "Generate JSDoc comments for functions without documentation" \
    --allowed-tools Read,Write \
    < "$file"
done

# Update README
claude -p "Update README.md with current project structure" \
  --allowed-tools Read,Write,Glob
```

### Continuous Monitoring

```bash
#!/bin/bash
# monitor.sh

while true; do
  # Check error logs
  tail -n 100 /var/log/app/error.log | \
    claude -p "Identify critical errors and suggest fixes" \
    --output-format json | \
    jq -r '.critical_errors[]?' | \
    while read error; do
      # Send alert
      curl -X POST https://alerts.company.com/webhook \
        -d "{\"error\": \"$error\"}"
    done
  
  sleep 300  # Check every 5 minutes
done
```

## Current Limitations

### Authentication Issues

```bash
# Problem: Non-interactive mode still requires login
claude -p "Test command" 
# Error: "Invalid API key · Please run /login"

# Workaround: Ensure API key is set
export ANTHROPIC_API_KEY="sk-ant-..."
```

### Slash Commands

Currently not supported in headless mode:
```bash
# This doesn't work
claude -p "/auto fix the bug"

# Use direct prompts instead
claude -p "Analyze and fix the bug in the codebase"
```

### Tool Permissions

Some permission configurations may not work correctly:
```bash
# May not respect tool restrictions
claude -p "Build project" --allowed-tools Bash
```

## Best Practices

### 1. Error Handling

```bash
#!/bin/bash
set -e  # Exit on error

# Capture exit code
if ! OUTPUT=$(claude -p "Validate code" 2>&1); then
  echo "Claude failed: $OUTPUT" >&2
  exit 1
fi
```

### 2. Timeout Management

```bash
# Use timeout to prevent hanging
timeout 300 claude -p "Complex analysis" || {
  echo "Analysis timed out after 5 minutes"
  exit 1
}
```

### 3. Resource Limits

```bash
# Limit memory usage
ulimit -m 2097152  # 2GB limit
claude -p "Process large file" < bigfile.txt
```

### 4. Logging

```bash
# Comprehensive logging
claude -p "Deploy application" \
  --verbose \
  --output-format json \
  2>&1 | tee -a deployment.log
```

## Advanced Patterns

### Parallel Processing

```bash
# Process multiple files in parallel
find . -name "*.py" -type f | \
  parallel -j 4 'claude -p "Add type hints" --allowed-tools Read,Write < {}'
```

### Conditional Execution

```bash
# Only proceed if analysis passes
if claude -p "Is this code production ready?" | grep -q "YES"; then
  ./deploy.sh
else
  echo "Code not ready for production"
  exit 1
fi
```

### Template Processing

```bash
# Generate from template
VARS=$(cat config.json)
claude -p "Generate Dockerfile using these variables: $VARS" \
  > Dockerfile
```

## Security Considerations

### 1. API Key Management

```bash
# Never hardcode keys
# Bad:
claude -p "task" --api-key "sk-ant-12345"

# Good:
export ANTHROPIC_API_KEY="${SECRET_API_KEY}"
claude -p "task"
```

### 2. Input Sanitization

```bash
# Sanitize user input
USER_INPUT=$(echo "$1" | sed 's/[^a-zA-Z0-9 ]//g')
claude -p "Process: $USER_INPUT"
```

### 3. Output Validation

```bash
# Validate JSON output
OUTPUT=$(claude -p "Generate config" --output-format json)
if ! echo "$OUTPUT" | jq empty 2>/dev/null; then
  echo "Invalid JSON output"
  exit 1
fi
```

## Performance Optimization

### Caching Results

```bash
# Simple file-based cache
CACHE_FILE="/tmp/claude-cache-$(echo "$PROMPT" | md5sum | cut -d' ' -f1)"
if [ -f "$CACHE_FILE" ] && [ $(find "$CACHE_FILE" -mmin -60) ]; then
  cat "$CACHE_FILE"
else
  claude -p "$PROMPT" | tee "$CACHE_FILE"
fi
```

### Batch Processing

```bash
# Process in batches to reduce API calls
find . -name "*.md" -type f | \
  xargs -n 10 claude -p "Summarize these documents"
```

## Future Enhancements

### Planned Features

1. Native slash command support in headless mode
2. Better authentication handling for CI/CD
3. Improved tool permission system
4. Session persistence across calls
5. Built-in caching mechanisms

### Community Requests

- Webhook support for async operations
- Better integration with container orchestration
- Native parallelization support
- Structured output schemas