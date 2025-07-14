# /task - Do ONE Thing Well

You are executing a focused development task. Follow this simple workflow:

## PHASE 1: UNDERSTAND (2 minutes max)
1. Read the task requirements
2. Find related files using: `find . -name "*.py" -o -name "*.js" -o -name "*.md" | head -20`
3. Read the most relevant files

## PHASE 2: PLAN (1 minute max)
1. Write 1-3 failing tests that define success
2. Run tests to confirm they fail
3. Commit: `git add -A && git commit -m "TDD RED: [task] - failing tests"`

## PHASE 3: IMPLEMENT (5 minutes max)
1. Write minimal code to pass tests
2. Run tests until they pass
3. Commit: `git add -A && git commit -m "TDD GREEN: [task] - tests passing"`

## PHASE 4: VALIDATE (1 minute max)
1. Run coverage: `pytest --cov=. --cov-report=term-missing` (Python) or `npm test -- --coverage` (JS)
2. Ensure 90%+ coverage
3. Commit: `git add -A && git commit -m "TASK COMPLETE: [task] - validated with coverage"`

## RULES:
- ONE task only (single file/component)
- Tests first, always
- 90%+ coverage required
- Commit each phase
- 10 minutes total max

## EXAMPLE:
`/task "Add email validation to user registration"`

---

**NOW EXECUTE THE TASK: $ARGUMENTS**