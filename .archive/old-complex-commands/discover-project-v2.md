---
name: discover-project
description: Analyze current project and create PROJECT-DNA.md with discovered patterns
usage: "discover-project"
allowed-tools: [Read, Write, Glob, Grep, LS, Bash]
category: core
version: "2.0"
---

# Discover Project DNA - Functional Version

## Purpose
Analyze the current project directory and create PROJECT-DNA.md with discovered patterns. This version provides specific, executable instructions for consistent results.

## Execution Instructions

### Step 1: Create PROJECT-DNA.md Header

Use Write to create PROJECT-DNA.md with this initial content:
```markdown
# Project DNA Analysis
*Generated: [current timestamp]*
*Analysis Version: 2.0*

## Technology Stack
```

### Step 2: Detect Technology Stack

#### For JavaScript/TypeScript Projects:
1. Use Read to check if `package.json` exists
2. If it exists:
   - Extract the `dependencies` object
   - Extract the `devDependencies` object
   - Look for these frameworks in dependencies:
     - "react" → Framework: React
     - "vue" → Framework: Vue
     - "@angular/core" → Framework: Angular
     - "express" → Framework: Express
     - "next" → Framework: Next.js
     - "svelte" → Framework: Svelte
   - Look for these in devDependencies:
     - "typescript" → Language: TypeScript
     - "jest" → Testing: Jest
     - "mocha" → Testing: Mocha
     - "@testing-library/react" → Testing: React Testing Library
     - "vitest" → Testing: Vitest
3. Check for lock files:
   - If `package-lock.json` exists → Package Manager: npm
   - If `yarn.lock` exists → Package Manager: yarn
   - If `pnpm-lock.yaml` exists → Package Manager: pnpm

Add to PROJECT-DNA.md:
```markdown
- **Language**: JavaScript/TypeScript
- **Framework**: [detected]
- **Testing**: [detected]
- **Package Manager**: [detected]
```

#### For Python Projects:
1. Use Read to check if `requirements.txt` exists
2. If it exists, read each line and detect:
   - Line contains "django" → Framework: Django
   - Line contains "flask" → Framework: Flask
   - Line contains "fastapi" → Framework: FastAPI
   - Line contains "pytest" → Testing: pytest
   - Line contains "unittest" → Testing: unittest
3. Use Read to check if `pyproject.toml` exists
   - If exists, check for [tool.poetry] → Package Manager: Poetry
   - Otherwise → Package Manager: pip

Add to PROJECT-DNA.md:
```markdown
- **Language**: Python
- **Framework**: [detected]
- **Testing**: [detected]
- **Package Manager**: [detected]
```

#### For Ruby Projects:
1. Use Read to check if `Gemfile` exists
2. If it exists, read and detect:
   - Line contains "gem 'rails'" → Framework: Rails
   - Line contains "gem 'sinatra'" → Framework: Sinatra
   - Line contains "gem 'rspec'" → Testing: RSpec

#### For Go Projects:
1. Use Read to check if `go.mod` exists
2. If it exists → Language: Go

### Step 3: Analyze Project Structure

Use LS to check the root directory, then check for these common directories:

```bash
# Check which source directories exist
src/     → Source directory: src
lib/     → Source directory: lib  
app/     → Source directory: app
pkg/     → Source directory: pkg

# Check organization pattern
features/   → Organization: Feature-based
components/ → Organization: Component-based
controllers/ + models/ + views/ → Organization: MVC
pages/ + components/ → Organization: Page-based
```

Add to PROJECT-DNA.md:
```markdown

## Project Structure
- **Organization**: [detected pattern]
- **Source Directory**: [detected directory]
```

### Step 4: Detect File Patterns

Use Glob to find example files:

For JavaScript/TypeScript:
```bash
# Find component files
Glob pattern: **/*.{jsx,tsx}
# Take first 5 results
# Check naming: PascalCase.tsx, kebab-case.tsx, or camelCase.tsx
```

For Python:
```bash
# Find Python files
Glob pattern: **/*.py
# Take first 5 results  
# Check naming: snake_case.py expected
```

Add to PROJECT-DNA.md:
```markdown
- **File Naming**: [detected pattern]
```

### Step 5: Detect Test Patterns

Use Glob to find test files:
```bash
# JavaScript/TypeScript
Glob pattern: **/*.test.{js,jsx,ts,tsx}
Glob pattern: **/*.spec.{js,jsx,ts,tsx}

# Python
Glob pattern: **/test_*.py
Glob pattern: **/*_test.py

# Check if tests are:
# - In same directory as source (colocated)
# - In __tests__ directories
# - In separate test/ directory
```

Add to PROJECT-DNA.md:
```markdown
- **Test Pattern**: [.test.js / .spec.js / test_*.py]
- **Test Location**: [colocated / separate / __tests__]
```

### Step 6: Find Example Patterns

#### For React Projects:
Use Glob to find a component file: `**/*.{jsx,tsx}`
Use Read on the first result to check:
- Functional components (arrow functions or function keyword)
- Class components (class extends React.Component)
- TypeScript interfaces or PropTypes
- Hooks usage (useState, useEffect)

#### For Python Projects:
Use Glob to find a Python file: `**/*.py`
Use Read on the first result to check:
- Type hints usage
- Class-based or functional
- Docstring style

Add to PROJECT-DNA.md:
```markdown

## Conventions
- **Component Style**: [functional/class]
- **Type System**: [TypeScript/PropTypes/Python hints/none]
- **State Management**: [detected if evident]
```

### Step 7: Generate Recommendations

Based on detected technology, add specific recommendations:

For React + TypeScript:
```markdown

## Recommendations for Generation

Based on this analysis, generate:
1. `create-component` - React component with TypeScript
2. `add-test` - Test with Jest and React Testing Library
3. `create-hook` - Custom React hook
4. `create-context` - React Context provider
5. `add-route` - React Router route
```

For Python + Django:
```markdown

## Recommendations for Generation

Based on this analysis, generate:
1. `create-model` - Django model
2. `add-view` - Django view
3. `create-serializer` - DRF serializer
4. `add-test` - Python test with pytest
5. `create-migration` - Django migration
```

For Node.js + Express:
```markdown

## Recommendations for Generation

Based on this analysis, generate:
1. `create-route` - Express route
2. `add-middleware` - Express middleware
3. `create-controller` - Route controller
4. `add-test` - Test with Jest/Mocha
5. `create-model` - Database model
```

### Step 8: Add Confidence Scores

```markdown

## Analysis Confidence
- **High Confidence**: [Items directly detected from files]
- **Medium Confidence**: [Items inferred from patterns]
- **Low Confidence**: [Items that may need verification]
- **Not Detected**: [Common items not found]
```

### Step 9: Add Example Code Pattern

If a component/module file was found, include a snippet:
```markdown

## Example Code Pattern Found

\```[language]
[First 20 lines of an example file]
\```

This pattern will be used as a template for generation.
```

### Step 10: Finalize and Save

Add footer:
```markdown

---
*This PROJECT-DNA.md will be used by `/generate-commands` to create custom commands for your project.*
*To regenerate, run `/discover-project` again.*
```

Use Write to save the complete content to `PROJECT-DNA.md` in the current directory.

## Success Validation

After execution:
1. Verify PROJECT-DNA.md exists
2. Check it contains:
   - Technology stack section
   - Project structure section
   - Conventions section
   - Recommendations section
   - No placeholder text

## Error Handling

If no package.json, requirements.txt, Gemfile, or go.mod found:
1. Check for other indicators:
   - `.html` files → Likely web project
   - `Makefile` → Check for language hints
   - `.java` files → Java project
   - `.cs` files → C# project
2. Create minimal PROJECT-DNA.md with:
   - What was detected
   - Request for user guidance
   - Explanation of what files to add

## Example Final Output

```markdown
# Project DNA Analysis
*Generated: 2025-01-09T16:30:00Z*
*Analysis Version: 2.0*

## Technology Stack
- **Language**: TypeScript
- **Framework**: React 18.2.0
- **Testing**: Jest + React Testing Library
- **Package Manager**: npm

## Project Structure
- **Organization**: Component-based
- **Source Directory**: src
- **File Naming**: PascalCase for components
- **Test Pattern**: .test.tsx
- **Test Location**: colocated

## Conventions
- **Component Style**: functional
- **Type System**: TypeScript interfaces
- **State Management**: Context API + hooks

## Recommendations for Generation

Based on this analysis, generate:
1. `create-component` - React component with TypeScript
2. `add-test` - Test with Jest and React Testing Library
3. `create-hook` - Custom React hook
4. `create-context` - React Context provider
5. `add-route` - React Router route

## Analysis Confidence
- **High Confidence**: React, TypeScript, Jest detected from package.json
- **Medium Confidence**: Component organization from directory structure
- **Low Confidence**: State management approach (inferred from imports)
- **Not Detected**: API client library, CSS framework

## Example Code Pattern Found

\```typescript
import React from 'react';
import styles from './Button.module.css';

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  variant?: 'primary' | 'secondary';
}

export const Button: React.FC<ButtonProps> = ({ 
  children, 
  onClick,
  variant = 'primary'
}) => {
  return (
    <button className={styles[variant]} onClick={onClick}>
      {children}
    </button>
  );
};
\```

This pattern will be used as a template for generation.

---
*This PROJECT-DNA.md will be used by `/generate-commands` to create custom commands for your project.*
*To regenerate, run `/discover-project` again.*
```

---
*This command now provides specific, executable instructions that will produce consistent results.*