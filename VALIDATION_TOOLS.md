# Framework Validation Tools

Three minimal Python scripts for validating and optimizing the Claude Code framework.

## Tools

### 1. validate.py
Automatically detects and reports common framework issues:
- Missing delegation blocks in commands
- Broken module references
- Missing version headers
- Files in wrong locations

```bash
./validate.py              # Check for issues
./validate.py --fix        # Auto-fix simple issues (coming soon)
```

### 2. optimize.py
Analyzes framework performance and suggests improvements:
- Token usage analysis
- Module complexity scoring
- Cache efficiency recommendations
- Execution path optimization

```bash
./optimize.py              # Run performance analysis
```

### 3. visualize.py
Generates visual representations of the framework:
- Command-module relationships tree
- Module category breakdown
- Dependency graph
- ASCII architecture diagram

```bash
./visualize.py             # Generate visualization
```

## Usage in CI/CD

```bash
# Run validation in CI pipeline
python3 validate.py || exit 1

# Generate performance report
python3 optimize.py > performance-report.txt

# Create framework diagram
python3 visualize.py > framework-structure.txt
```

## Design Principles
- Each tool is under 100 lines
- Clear, actionable output
- Proper exit codes for automation
- Minimal dependencies (stdlib only)
- Work together as cohesive suite