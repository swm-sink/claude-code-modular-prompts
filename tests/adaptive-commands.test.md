# Adaptive Commands Test Specifications

## Test Framework for Adaptive Behavior

### `/start` Command Tests

#### Test 1: Minimal Mode (New Empty Project)
**Given**: Empty directory with no .claude folder
**When**: User runs `/start`
**Then**: 
- Should NOT ask questions
- Should create basic .claude/commands/ structure
- Should generate minimal settings.json
- Should create simple CLAUDE.md
- Execution time < 30 seconds
- No parallel agents used

#### Test 2: Standard Mode (Existing Project)
**Given**: Project with package.json or requirements.txt
**When**: User runs `/start`  
**Then**:
- Should detect project type automatically
- Should ask 0-1 clarifying questions max
- Should create tailored commands
- Should generate comprehensive CLAUDE.md
- Execution time < 2 minutes
- Max 1-2 agents if needed

#### Test 3: Comprehensive Mode (Complex Project)
**Given**: Large project (>100 files, multiple technologies)
**When**: User runs `/start --mode full`
**Then**:
- Should perform deep analysis
- Should ask 1-3 essential questions
- Should create custom commands
- Should detect team conventions
- Execution time < 5 minutes
- Can use 3-4 parallel agents

#### Test 4: User Control Override
**Given**: Any project
**When**: User runs `/start --mode minimal`
**Then**:
- Should skip all detection
- Should use minimal mode regardless of project complexity
- Should complete in < 30 seconds

### `/analyze` Command Tests

#### Test 5: Quick Analysis (Small Project)
**Given**: Project with < 10 files
**When**: User runs `/analyze`
**Then**:
- Should provide basic metrics only
- Should NOT use parallel agents
- Should complete in < 30 seconds
- Output should be concise (< 20 lines)

#### Test 6: Standard Analysis (Medium Project)
**Given**: Project with 10-100 files
**When**: User runs `/analyze`
**Then**:
- Should detect patterns
- Should provide code metrics
- Should identify key dependencies
- Should complete in < 2 minutes
- Can use 1-2 agents if beneficial

#### Test 7: Deep Analysis (Large Project)
**Given**: Project with > 100 files
**When**: User runs `/analyze --depth deep`
**Then**:
- Should perform comprehensive analysis
- Should identify architecture patterns
- Should detect technical debt
- Should find performance bottlenecks
- Execution time < 5 minutes
- Can use 3-4 parallel agents

### `/build` Command Tests

#### Test 8: Simple Feature (Single File)
**Given**: Request to add simple function
**When**: User runs `/build add-validation-function`
**Then**:
- Should NOT ask about approach
- Should detect existing patterns
- Should implement directly
- No TDD ceremony for simple function
- Complete in < 1 minute

#### Test 9: Medium Feature (Multiple Files)
**Given**: Request to add API endpoint
**When**: User runs `/build user-profile-endpoint`
**Then**:
- Should ask 1 question about requirements
- Should follow existing API patterns
- Should include basic tests
- Should update related files
- Complete in < 3 minutes

#### Test 10: Complex Feature (System-wide)
**Given**: Request to add authentication system
**When**: User runs `/build authentication-system`
**Then**:
- Should ask 2-3 key questions (auth type, storage, etc.)
- Should create implementation plan
- Should use TDD approach
- Should coordinate multiple files
- Can use parallel agents
- Complete in < 10 minutes

### `/test` Command Tests  

#### Test 11: Basic Test Generation
**Given**: Simple function with < 10 lines
**When**: User runs `/test utils.js`
**Then**:
- Should generate 3-5 basic tests
- Should cover happy path
- Should NOT over-test simple logic
- Complete in < 30 seconds

#### Test 12: Thorough Test Generation
**Given**: Complex module with business logic
**When**: User runs `/test payment-processor.js`
**Then**:
- Should detect complexity automatically
- Should generate 10-15 tests
- Should cover edge cases
- Should test error scenarios
- Complete in < 2 minutes

#### Test 13: Adaptive Coverage
**Given**: Mixed complexity codebase
**When**: User runs `/test --coverage adaptive`
**Then**:
- Should assess each function's complexity
- Should generate appropriate test density
- Simple functions: 2-3 tests
- Complex functions: 10+ tests
- Should explain coverage decisions

### Progressive Questioning Tests

#### Test 14: Zero Questions (Clear Context)
**Given**: Clear, unambiguous request with detectable context
**When**: User runs any adaptive command
**Then**:
- Should NOT ask any questions
- Should state assumptions clearly
- Should proceed with confidence

#### Test 15: Single Question (Ambiguous Goal)
**Given**: Request with unclear primary objective
**When**: User runs adaptive command
**Then**:
- Should ask ONE clarifying question
- Should provide sensible options
- Should make assumptions for everything else

#### Test 16: Progressive Questions (Complex Unknown)
**Given**: Complex request with many unknowns
**When**: User runs adaptive command
**Then**:
- Should ask most important question first
- Follow-up questions based on answer
- Maximum 3-5 questions total
- Should explain why each question matters

### Performance Tests

#### Test 17: Token Usage Optimization
**Given**: Same task complexity
**When**: Comparing old vs new adaptive commands
**Then**:
- Simple tasks: 40% fewer tokens
- Medium tasks: 20% fewer tokens
- Complex tasks: Similar token usage
- Better token/value ratio

#### Test 18: Execution Time
**Given**: Standard project operations
**When**: Running adaptive commands
**Then**:
- Simple operations: < 30 seconds
- Medium operations: < 2 minutes
- Complex operations: < 5 minutes
- No unnecessary waiting

#### Test 19: Agent Usage Efficiency
**Given**: Various task complexities
**When**: Executing adaptive commands
**Then**:
- Simple tasks: 0 parallel agents
- Medium tasks: 0-2 agents (only if beneficial)
- Complex tasks: 3-5 agents maximum
- Total agents reduced by 70% overall

### Error Handling Tests

#### Test 20: Graceful Degradation
**Given**: Complexity detection fails
**When**: Running adaptive command
**Then**:
- Should fall back to safe defaults
- Should ask user for guidance
- Should not crash or hang
- Should explain the issue

## Test Execution Plan

### Phase 1: Unit Tests
- Test individual complexity detection functions
- Test question decision logic
- Test mode selection algorithms

### Phase 2: Integration Tests  
- Test full command execution paths
- Test interaction between commands
- Test state management

### Phase 3: User Experience Tests
- Test with real projects of varying sizes
- Measure actual question counts
- Validate assumption accuracy
- Check execution times

## Success Criteria

### Quantitative Metrics
- ✅ 90% of simple tasks require 0 questions
- ✅ 80% of medium tasks require ≤ 1 question
- ✅ Average execution time reduced by 30%
- ✅ Token usage reduced by 40% for simple tasks
- ✅ Parallel agent usage reduced by 70%

### Qualitative Metrics
- ✅ Users report fewer interruptions
- ✅ Commands feel more intelligent
- ✅ Appropriate effort for task complexity
- ✅ Clear and helpful when questions are asked

## Test Implementation Notes

Since Claude Code commands are prompts, not executable code, testing involves:
1. **Manual validation**: Running commands with different inputs
2. **Scenario testing**: Documenting behavior in various contexts
3. **Metric tracking**: Measuring tokens, time, and questions
4. **User feedback**: Gathering experience reports

The test specifications above serve as acceptance criteria for the adaptive command implementation.