---
name: build
description: Adaptive development from simple edits to complex features
usage: "/build <what-to-build> [--approach auto|quick|tdd|architect]"
allowed-tools: [Read, Write, Edit, MultiEdit, Grep, Task]
---

# Adaptive Feature Building

I'll build your feature with the right approach based on complexity.

## Understanding the Request

Building: **[what-to-build]**

Let me assess the scope:
- Checking existing patterns...
- Estimating complexity...
- Identifying dependencies...

<simple-build>
<!-- For single-file changes, simple functions -->

## Quick Implementation (< 2 minutes)

This is straightforward. I'll:
1. Follow your existing patterns in [detected file/pattern]
2. Add the [feature type] directly
3. Include basic validation

*Creating now with smart defaults...*

[Direct implementation - no over-engineering]
</simple-build>

<standard-build>
<!-- For multi-file features, moderate complexity -->

## Standard Development (3-5 minutes)

This involves [detected scope]. 

**One quick question**: [Most important clarification]
- Option A: [Common approach with trade-offs]
- Option B: [Alternative approach with trade-offs]

*I'll handle everything else based on your patterns.*

### Implementation Plan
1. **Core logic**: [where and what]
2. **Integration**: [how it connects]
3. **Testing**: [test approach]
4. **Documentation**: [what to update]

*Proceeding with [selected approach]...*

[Implementation with progress updates]
</standard-build>

<complex-build>
<!-- For system-wide changes, high complexity -->

## Comprehensive Development (5-10 minutes)

This is a substantial feature affecting multiple areas.

### Essential Clarifications

**Architecture question**: [Key structural decision]
> Your answer: 

**Requirements question**: [Core functionality scope]
> Your answer:

*Making intelligent assumptions for:*
- Code style (detected from your codebase)
- Testing approach (using your framework)
- Error handling (following your patterns)

### Multi-Phase Implementation

**Phase 1: Foundation** (Task agent)
- Core data structures
- Basic interfaces
- Initial validation

**Phase 2: Business Logic** (Task agent)
- Main functionality
- Edge case handling
- Error management

**Phase 3: Integration** (Task agent)
- Connect to existing system
- Update dependent modules
- Migration if needed

**Phase 4: Quality** (Standard execution)
- Comprehensive tests
- Documentation
- Performance optimization

### Execution with TDD

1. **RED**: Writing failing tests first
2. **GREEN**: Implementing minimal solution
3. **REFACTOR**: Optimizing for your patterns

*Starting implementation...*

[Detailed progress with checkpoints]
</complex-build>

<architect-mode>
<!-- For --approach architect or major system design -->

## Architecture-First Development

This requires careful design. Let me create a plan:

### System Design
- Component breakdown
- Interface definitions
- Data flow design

### Risk Assessment
- Breaking changes: [identified]
- Performance impact: [estimated]
- Security considerations: [analyzed]

**Proceed with full implementation?** (Y/n)

[If yes, execute complex-build flow]
</architect-mode>

## Build Progress

[Real-time updates based on mode]
- ✅ Pattern detection complete
- ⏳ Creating [current file/component]
- ⏳ Writing tests
- ⏳ Updating documentation

## Build Complete!

Successfully built: **[what was built]**

### What I Created/Modified:
- [List of files and changes]

### Assumptions Made:
- [List key decisions]

### Next Steps:
- Run tests: `[test command]`
- Review changes: `git diff`
- Commit: `/commit`

*Used [mode] approach based on complexity assessment.*