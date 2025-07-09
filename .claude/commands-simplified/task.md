# /task - Single Task Execution

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Execute focused single tasks with a research-first approach and basic TDD support. Ideal for implementing specific features, fixing bugs, or making targeted improvements.

**Note**: This is a simplified version that focuses on core functionality without complex framework enforcement.

---

## How It Works

### 1. Research Phase
- **Understand Requirements**: Analyze what needs to be done
- **Explore Codebase**: Research existing code and patterns
- **Identify Dependencies**: Find related components and integrations
- **Plan Approach**: Determine the best implementation strategy

### 2. Test Design Phase
- **Write Tests First**: Create failing tests for the requirements
- **Cover Edge Cases**: Consider normal, edge, and error scenarios
- **Validate Approach**: Ensure tests accurately reflect requirements
- **Establish Success Criteria**: Define what "done" looks like

### 3. Implementation Phase
- **Make Tests Pass**: Implement minimal code to pass tests
- **Follow Patterns**: Use existing project conventions and patterns
- **Maintain Quality**: Write clean, readable code
- **Handle Errors**: Include appropriate error handling

### 4. Refinement Phase
- **Refactor Code**: Improve design while keeping tests green
- **Optimize Performance**: Address any performance concerns
- **Update Documentation**: Document the changes made
- **Verify Quality**: Ensure code meets project standards

---

## Usage Examples

```bash
# Basic task execution
/task "Add email validation to user registration"

# Bug fix task
/task "Fix memory leak in data processing" --type bug

# Feature enhancement
/task "Add dark mode toggle to settings" --type feature

# Refactoring task
/task "Extract common validation logic into utility" --type refactor

# With specific focus
/task "Optimize database query performance" --focus performance
```

---

## What It Does

### Research & Analysis
- Analyzes existing code and patterns
- Identifies related components and dependencies
- Researches best practices and approaches
- Plans implementation strategy

### Test-Driven Development
- Creates failing tests before implementation
- Ensures good test coverage
- Uses tests to drive design decisions
- Validates requirements through tests

### Clean Implementation
- Follows project conventions and patterns
- Implements minimal code to pass tests
- Maintains code quality and readability
- Includes appropriate error handling

### Quality Assurance
- Refactors code for better design
- Verifies tests pass consistently
- Updates relevant documentation
- Ensures code meets project standards

---

## Workflow Steps

### 1. Research Requirements
```
ANALYZE: What exactly needs to be implemented?
EXPLORE: What existing code is relevant?
IDENTIFY: What dependencies and integrations exist?
PLAN: What's the best approach?
```

### 2. Design Tests
```
WRITE: Create failing tests for requirements
COVER: Include normal, edge, and error cases
VALIDATE: Ensure tests match requirements
CONFIRM: Tests fail as expected
```

### 3. Implement Solution
```
CODE: Write minimal code to pass tests
FOLLOW: Use existing patterns and conventions
MAINTAIN: Keep code clean and readable
HANDLE: Include error handling and edge cases
```

### 4. Refine & Validate
```
REFACTOR: Improve design while keeping tests green
OPTIMIZE: Address performance concerns
DOCUMENT: Update relevant documentation
VERIFY: Ensure quality standards met
```

---

## Output Format

### Task Summary
```
TASK: [task-description]
TYPE: [feature/bug/refactor/enhancement]
SCOPE: [files-affected]
COMPLEXITY: [low/medium/high]
```

### Research Findings
```
EXISTING_CODE: [relevant-code-analysis]
DEPENDENCIES: [related-components]
PATTERNS: [project-conventions-to-follow]
APPROACH: [implementation-strategy]
```

### Test Results
```
TESTS_CREATED: [number-of-tests]
COVERAGE: [percentage-or-description]
SCENARIOS: [normal/edge/error-cases]
STATUS: [failing-as-expected/ready-for-implementation]
```

### Implementation Results
```
FILES_MODIFIED: [list-of-changed-files]
TESTS_PASSING: [test-results]
QUALITY_CHECKS: [code-quality-status]
DOCUMENTATION: [updates-made]
```

---

## Key Features

### ✅ Research-First Approach
- Understands requirements before coding
- Explores existing codebase patterns
- Identifies dependencies and integrations
- Plans optimal implementation strategy

### ✅ TDD Support
- Writes tests before implementation
- Ensures good test coverage
- Uses tests to drive design
- Validates requirements through testing

### ✅ Quality Focus
- Follows project conventions
- Maintains code quality standards
- Includes proper error handling
- Updates documentation

### ✅ Self-Contained
- No external module dependencies
- Built-in error handling
- Comprehensive workflow
- Clear output format

---

## Task Types

### Feature Tasks
- **New Functionality**: Adding new features
- **Enhancements**: Improving existing features
- **Integrations**: Adding external integrations
- **UI/UX**: User interface improvements

### Bug Fix Tasks
- **Error Handling**: Fixing error conditions
- **Performance**: Addressing performance issues
- **Security**: Fixing security vulnerabilities
- **Compatibility**: Resolving compatibility issues

### Refactoring Tasks
- **Code Cleanup**: Improving code structure
- **Pattern Implementation**: Applying design patterns
- **Optimization**: Performance improvements
- **Modernization**: Updating to newer practices

---

## Best Practices

### When to Use
- **Single File Changes**: Tasks affecting 1-3 files
- **Focused Work**: Clear, specific requirements
- **Bug Fixes**: Targeted problem resolution
- **Small Features**: Contained functionality

### Optimization Tips
- Start with research to understand the problem
- Write tests before any implementation
- Keep changes focused and minimal
- Refactor in small, safe steps

### Quality Guidelines
- Follow existing project patterns
- Maintain or improve test coverage
- Include appropriate error handling
- Update documentation when needed

---

## Error Handling

### Common Issues
- **Unclear Requirements**: Asks for clarification
- **Complex Dependencies**: Suggests breaking into smaller tasks
- **Test Failures**: Provides debugging guidance
- **Quality Issues**: Suggests improvements

### Graceful Degradation
- Provides partial implementation if full solution complex
- Suggests alternative approaches when blocked
- Maintains working state even with incomplete features
- Documents limitations and next steps

---

## Integration

### Works Well With
- `/context-prime` - For project context before starting
- `/research` - For deeper analysis of complex problems
- `/review` - For code review after implementation
- `/test` - For comprehensive testing

### Escalation Paths
- **Complex Tasks**: Escalate to `/feature` for multi-component work
- **Large Changes**: Consider `/refactor` for significant restructuring
- **Research Needs**: Use `/research` for investigation-heavy tasks
- **Multi-file Changes**: Consider `/feature` for broader scope

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple workflow steps
- **No Mandatory Enforcement**: Supportive TDD guidance
- **No Module Dependencies**: Self-contained logic
- **No Advanced Frameworks**: Basic TDD and quality practices

### Core Focus
- **Essential TDD**: Test-first development without complex enforcement
- **Practical Quality**: Basic quality checks without blocking gates
- **Fast Execution**: Minimal overhead for quick tasks
- **Clear Results**: Actionable output and next steps

---

**Note**: This simplified command provides core task execution functionality with basic TDD support. For advanced features like RISE framework integration, complex quality gates, or multi-agent coordination, use the full framework commands.