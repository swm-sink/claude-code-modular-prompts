# Task Command

Research-first focused development with mandatory TDD cycle and atomic commits.

## Instructions

Execute the following workflow for the task: $ARGUMENTS

1. **Research First**: Analyze the requirements, existing code, and patterns before any implementation.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TASK RESEARCH: [task_name] - requirements analyzed and patterns identified"`

2. **TDD Red Phase**: Write failing tests that define the expected behavior. Tests must fail initially.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TDD RED: [test_description] - failing tests created for [task_name]"`
   - **Rollback Safety**: If tests don't fail correctly, rollback with `git reset --hard HEAD~1`

3. **TDD Green Phase**: Implement the minimal code to make tests pass. Measure test coverage and ensure ≥90% threshold.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TDD GREEN: [implementation] - tests passing for [task_name]"`
   - **Coverage Validation**: Run coverage tools and validate ≥90% before commit
   - **Rollback Safety**: If coverage fails, rollback with `git reset --hard HEAD~1`

4. **TDD Refactor Phase**: Improve code quality while keeping tests green.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TDD REFACTOR: [refactoring] - quality improved for [task_name]"`
   - **Safety Check**: Ensure tests still pass after refactoring

5. **Quality Gates**: Validate against production standards and ensure comprehensive coverage.
   - **Final Atomic Checkpoint**: `git add -A && git commit -m "TASK COMPLETE: [task_name] - production ready with quality validation"`

## Critical Rules

- ALWAYS write failing tests BEFORE implementation
- NEVER write code without test coverage
- Research existing patterns and architecture first
- Maintain 90%+ test coverage with atomic commit validation
- Use appropriate testing framework (pytest for Python, Jest for JavaScript, etc.)
- **ATOMIC SAFETY**: Every TDD phase gets atomic commit with rollback capability
- **INSTANT ROLLBACK**: Use `git reset --hard HEAD~1` for immediate rollback to previous phase

## Coverage Commands

- Python: `pytest --cov=. --cov-report=term-missing --cov-fail-under=90`
- JavaScript: `npm test -- --coverage --coverageThreshold='{"global":{"lines":90}}'`

## Examples

- `/task "Add email validation"` - Creates email validation with tests
- `/task "Fix memory leak in component"` - Creates regression test first
- `/task "Optimize database query"` - Creates performance test first