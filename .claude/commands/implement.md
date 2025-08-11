---
name: implement
description: TDD implementation with Chain of Thought reasoning and verification
usage: "/implement <feature-description> [--approach careful|balanced|rapid]"
tools: [Read, Write, Edit, WebSearch, Grep, Task, Bash]
---

# Chain of Thought TDD Implementation

I'll implement your feature using systematic Chain of Thought reasoning with continuous verification.

## Step 1: Requirements Analysis (Extended Thinking)

Let me think through this systematically:
- What is the core problem we're solving?
- What are the success criteria?
- What edge cases must we handle?
- What are the performance requirements?
- How does this integrate with existing code?

## Step 2: Test Design (Chain of Thought)

**Reasoning through test scenarios:**
1. Happy path test → What's the ideal flow?
2. Edge case tests → What could go wrong?
3. Error handling → How should failures behave?
4. Performance tests → What are acceptable limits?
5. Integration tests → How does this affect other components?

**Test Implementation Order:**
- Red: Write failing test for core functionality
- Green: Minimal implementation to pass
- Refactor: Improve without breaking tests
- Repeat for each test scenario

## Step 3: Parallel Implementation Strategy

**Task Agent 1: Research Best Practices**
- WebSearch for latest patterns in your language/framework
- Find similar implementations in respected codebases
- Identify common pitfalls to avoid

**Task Agent 2: Dependency Analysis**
- Map all files that need modification
- Identify potential breaking changes
- Check for required refactoring

**Main Thread: Incremental Implementation**
- Implement smallest working piece
- Run tests after each change
- Commit at each green state
- Document decisions in code

## Step 4: Verification Loop

After each implementation step:
1. Run all tests (unit, integration, e2e if applicable)
2. Check performance metrics
3. Validate against requirements
4. Review for code smells
5. Ensure documentation is updated

## Step 5: Quality Assurance

**Final verification using sub-agent:**
- Code review against team standards
- Security vulnerability check
- Performance profiling
- Test coverage validation

## Adaptive Approach

**Careful**: More tests, smaller steps, frequent verification
**Balanced**: Standard TDD cycle with reasonable coverage
**Rapid**: Focus on core functionality, minimal viable tests

Starting Chain of Thought implementation process...