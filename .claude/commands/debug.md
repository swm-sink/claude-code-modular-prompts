---
name: debug
description: Interactive debugging assistant for finding and fixing issues
usage: "/debug [error-message|file:line]"
allowed-tools: [Read, Grep, WebSearch, Edit]
---

# Debug Assistant

I'll help you troubleshoot and fix issues in your code.

## What I Can Debug

- **Runtime errors**: Stack traces, error messages
- **Logic bugs**: Unexpected behavior, wrong outputs  
- **Performance issues**: Slow code, memory leaks
- **Integration problems**: API failures, dependency conflicts

## My Debugging Process

1. **Analyze the Error**
   - Parse error message or stack trace
   - Identify the failing component
   - Trace execution path

2. **Investigate Root Cause**
   - Read relevant code sections
   - Check recent changes
   - Search for known issues

3. **Provide Solutions**
   - Specific fix with code
   - Alternative approaches
   - Prevention strategies

## Interactive Mode

I'll ask clarifying questions:
- What were you trying to do?
- When did this start happening?
- What have you already tried?

## Output

- Root cause analysis
- Step-by-step fix
- Code corrections
- Test to verify fix

Share your error or issue to begin...