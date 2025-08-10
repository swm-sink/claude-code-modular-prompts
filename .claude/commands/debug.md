---
name: debug
description: Adaptive debugging based on issue complexity
usage: "/debug [error-message|file:line]"
allowed-tools: [Read, Grep, WebSearch, Edit]
---

# Adaptive Debugging

Looking at: **[error/issue]**

Assessing complexity...

<simple-mode>
<!-- Syntax errors, typos -->
## Quick Fix
**Found**: [issue] at `file:line`
**Cause**: [immediate cause]
**Fixing**: [applying solution]
</simple-mode>

<standard-mode>
<!-- Runtime errors, logic bugs -->
## Systematic Debug
1. **What broke**: [error analysis]
2. **Root cause**: [investigation]
3. **Solution**: [fix description]

Implementing fix now...
</standard-mode>

<complex-mode>
<!-- System issues, race conditions -->
## Deep Investigation
- Researching similar issues
- Checking dependencies
- Analyzing recent changes

**Root cause chain**:
Symptom → Cause → Root

**Fix approach**:
- Immediate: [patch]
- Proper: [solution]
- Prevention: [tests]

*Need external research? (Y/n)*
</complex-mode>

## Resolution
✅ **Fixed**: [what]
📍 **Location**: [where]

**Verify**: `[test command]`
**Prevent**: Add [test/validation]