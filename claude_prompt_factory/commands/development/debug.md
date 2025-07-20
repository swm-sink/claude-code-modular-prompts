# /debug - AI-Assisted Debugging Command

**Purpose**: Perform an advanced, AI-assisted debugging session to diagnose and fix issues in the codebase.

## Usage
```bash
/debug [issue] [--interactive]
```

## Workflow

The `/debug` command follows a systematic process to diagnose and fix issues.

```xml
<debugging_workflow>
  <step name="Gather Context">
    <description>Gather all relevant context about the issue, including error symptoms, recent changes, system state, and steps to reproduce.</description>
  </step>
  
  <step name="Analyze & Hypothesize">
    <description>Perform an intelligent analysis of the gathered context to generate a set of hypotheses about the root cause of the issue.</description>
  </step>
  
  <step name="Execute Debugging Strategy">
    <description>Systematically test each hypothesis using a variety of debugging techniques, such as setting strategic breakpoints, tracing execution flow, and monitoring variables.</description>
  </step>
  
  <step name="Provide Solution">
    <description>Once the root cause has been identified, provide a detailed solution, including the necessary code changes, verification steps, and recommendations for preventing the issue from recurring.</description>
    <output>A comprehensive debugging report with the root cause analysis and a complete solution.</output>
  </step>
</debugging_workflow>
```

## Debugging Techniques
- **Print Debugging**: Strategic log placement
- **Breakpoint Analysis**: Pause at critical points
- **State Inspection**: Variable and memory analysis
- **Flow Tracing**: Execution path tracking
- **Binary Search**: Isolate problem area
- **Differential Debugging**: Compare working/broken

## Output Format
```
DEBUG SESSION: User Login Fails
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HYPOTHESIS 1: Authentication token expired
Testing... ✗ Token is valid

HYPOTHESIS 2: Database connection issue
Testing... ✗ DB responding normally

HYPOTHESIS 3: Session middleware conflict
Testing... ✓ FOUND ISSUE

ROOT CAUSE:
Session middleware executing after auth check
- Location: middleware/auth.js:15
- Impact: All authenticated routes fail

EXECUTION TRACE:
1. Request arrives
2. Auth middleware checks session (empty)
3. Session middleware initializes (too late)
4. Auth fails

FIX:
Move session middleware before auth:
```javascript
app.use(session(config))  // Move this
app.use(authenticate)     // Before this
```

VERIFICATION:
- Test login flow
- Check session persistence
- Verify no side effects
```

## Options
- `--interactive`: Step-by-step debugging
- `--breakpoint`: Set breakpoints
- `--trace`: Execution tracing
- `--watch`: Monitor variables

## Related Commands
- `/error diagnose` - Error analysis
- `/fix bug` - Apply bug fixes
- `/test debug` - Debug test failures