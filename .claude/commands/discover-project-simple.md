---
name: discover-project-simple
description: Analyze current project and extract patterns (simplified, functional version)
usage: "discover-project-simple"
allowed-tools: [Read, Write, Glob, Grep, LS]
category: core
---

# Discover Project - Simple & Functional

## Purpose
Analyze the current project directory to understand its technology stack, patterns, and conventions. Creates PROJECT-DNA.md with discovered patterns.

## What This Actually Does

Using Claude's native tools, this command:
1. Detects your technology stack
2. Identifies project structure
3. Finds naming conventions
4. Discovers test patterns
5. Creates PROJECT-DNA.md

## Execution Steps

### Step 1: Detect Technology Stack

Check for package.json (JavaScript/TypeScript):
```bash
Read package.json
Extract: dependencies, devDependencies, scripts
Identify: React/Vue/Angular, Jest/Mocha, TypeScript
```

Check for requirements.txt or pyproject.toml (Python):
```bash
Read requirements.txt or pyproject.toml
Identify: Django/Flask/FastAPI, pytest/unittest
```

Check for Gemfile (Ruby):
```bash
Read Gemfile
Identify: Rails, RSpec
```

Check for go.mod (Go):
```bash
Read go.mod
Identify: Go version, dependencies
```

### Step 2: Analyze Project Structure

```bash
Use LS to explore:
- src/ or lib/ or app/
- tests/ or test/ or spec/
- components/ or views/ or models/
- public/ or static/
```

Identify patterns:
- Flat vs nested structure
- Feature-based vs type-based organization
- Test colocation vs separate directory

### Step 3: Detect Naming Conventions

```bash
Use Glob to find files:
- *.js, *.jsx, *.ts, *.tsx
- *.py
- *.rb
- *.go
```

Analyze naming:
- kebab-case vs camelCase vs PascalCase
- File suffixes (.test.js vs .spec.js)
- Component naming patterns

### Step 4: Find Test Patterns

```bash
Use Grep to search for:
- "describe(" or "test(" or "it(" (JavaScript)
- "def test_" or "class Test" (Python)
- "RSpec.describe" (Ruby)
```

Identify:
- Testing framework
- Test file locations
- Test naming conventions

### Step 5: Generate PROJECT-DNA.md

Create a structured output:

```markdown
# Project DNA Analysis
*Generated: [timestamp]*

## Technology Stack
- **Language**: [detected]
- **Framework**: [detected]
- **Testing**: [detected]
- **Package Manager**: [detected]

## Project Structure
- **Organization**: [feature-based/type-based]
- **Source Directory**: [src/lib/app]
- **Test Location**: [colocated/separate]

## Conventions
- **File Naming**: [kebab-case/camelCase/PascalCase]
- **Component Pattern**: [functional/class]
- **Test Pattern**: [.test.js/.spec.js]

## Discovered Patterns

### Component Structure
[Example of discovered component pattern]

### Test Structure
[Example of discovered test pattern]

### API/Route Structure
[Example of discovered API pattern]

## Recommendations for Generation

Based on this analysis, generate:
1. Component generators matching [pattern]
2. Test generators using [framework]
3. API endpoint creators following [structure]
4. Utility commands for [common tasks]

## Confidence Score
- High confidence: [list]
- Medium confidence: [list]
- Low confidence: [list]
```

## Example Usage

When you run this command, Claude will:

1. **Check your package.json**:
```json
{
  "dependencies": {
    "react": "^18.0.0",
    "axios": "^1.0.0"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "@types/react": "^18.0.0"
  }
}
```
Result: Detects React + TypeScript + Jest

2. **Scan your file structure**:
```
src/
  components/
    Button/
      Button.tsx
      Button.test.tsx
      Button.module.css
```
Result: Component folder pattern with colocated tests

3. **Create PROJECT-DNA.md** with your specific patterns

## Important Notes

- This analyzes YOUR current directory
- Works with any language/framework
- Creates actionable PROJECT-DNA.md
- No complex backend needed
- Simple, direct, functional

## After Running This

Run `/generate-commands-simple` to create custom commands based on your PROJECT-DNA.md

---
*This is the simplified, actually functional version of project discovery*