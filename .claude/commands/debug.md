---
name: debug
description: Advanced debugging with parallel root cause analysis and predictive fixes
usage: "/debug [error-message|file:line] [--mode quick|thorough|forensic]"
allowed-tools: [Read, Grep, WebSearch, Edit, Task, Bash]
---

# Advanced Debugging with Root Cause Analysis

I'll use parallel investigation and causal reasoning to find and fix your issue quickly.

## Phase 1: Parallel Investigation (5 Concurrent Agents)

**Agent 1: Error Pattern Analysis**
- Parse error message/stack trace with regex
- Identify error type and severity
- Extract relevant file paths and line numbers
- Classify error category (syntax/runtime/logic/performance)

**Agent 2: Historical Analysis**
- Git blame to find when code was introduced
- Check recent commits for related changes
- Identify if this is a regression
- Find similar past issues and their fixes

**Agent 3: Dependency Investigation**
- Check for version mismatches
- Identify breaking changes in dependencies
- Scan for circular dependencies
- Verify environment consistency

**Agent 4: Similar Issues Research**
- WebSearch for exact error message
- Search GitHub issues for your dependencies
- Check Stack Overflow for solutions
- Find patches or workarounds

**Agent 5: Code Flow Analysis**
- Trace execution path to error
- Identify all code paths leading to failure
- Map data flow and transformations
- Detect race conditions or deadlocks

## Phase 2: Root Cause Determination

**Causal Chain Analysis:**
1. Immediate cause (what broke)
2. Proximate cause (why it broke)
3. Root cause (what allowed it to break)
4. Systemic cause (process failure that enabled it)

**Hypothesis Testing:**
- Generate 3-5 potential causes
- Rank by probability
- Create minimal reproduction
- Test each hypothesis

## Phase 3: Solution Generation

**Multi-Strategy Fix Approach:**

**Quick Fix** (Immediate relief):
- Patch the symptom
- Add error handling
- Implement workaround

**Proper Fix** (Address root cause):
- Refactor problematic code
- Fix architectural issues
- Update dependencies

**Preventive Fix** (Avoid recurrence):
- Add tests to catch this
- Improve error messages
- Add validation/guards
- Document the issue

## Phase 4: Verification Protocol

**Automated Testing:**
```bash
# Test the fix works
# Test it doesn't break other things
# Test edge cases are handled
# Performance benchmark if relevant
```

## Phase 5: Learning Integration

**Documentation Updates:**
- Add to troubleshooting guide
- Update error handling patterns
- Create knowledge base entry
- Share team postmortem

## Debugging Modes

**Quick Mode**: Fast diagnosis, immediate patch
**Thorough Mode**: Complete root cause analysis
**Forensic Mode**: Deep investigation with full history

Starting parallel debugging investigation...