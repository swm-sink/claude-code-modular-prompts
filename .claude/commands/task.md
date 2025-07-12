# Task Command

Research-first focused development with mandatory TDD cycle.

## Instructions

Execute the following workflow for the task: $ARGUMENTS

1. **Research First**: Analyze the requirements, existing code, and patterns before any implementation.

2. **TDD Red Phase**: Write failing tests that define the expected behavior. Tests must fail initially.

3. **TDD Green Phase**: Implement the minimal code to make tests pass. Measure test coverage and ensure ≥90% threshold.

4. **TDD Refactor Phase**: Improve code quality while keeping tests green.

5. **Quality Gates**: Validate against production standards and ensure comprehensive coverage.

## Critical Rules

- ALWAYS write failing tests BEFORE implementation
- NEVER write code without test coverage
- Research existing patterns and architecture first
- Maintain 90%+ test coverage
- Use appropriate testing framework (pytest for Python, Jest for JavaScript, etc.)

## Coverage Commands

- Python: `pytest --cov=. --cov-report=term-missing --cov-fail-under=90`
- JavaScript: `npm test -- --coverage --coverageThreshold='{"global":{"lines":90}}'`

## Examples

- `/task "Add email validation"` - Creates email validation with tests
- `/task "Fix memory leak in component"` - Creates regression test first
- `/task "Optimize database query"` - Creates performance test first