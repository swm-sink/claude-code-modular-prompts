---
name: generate-commands-simple
description: Generate custom commands based on PROJECT-DNA.md (simplified, functional version)
usage: "generate-commands-simple"
allowed-tools: [Read, Write, Edit]
category: core
---

# Generate Commands - Simple & Functional

## Purpose
Read PROJECT-DNA.md and generate 5-10 custom commands specifically for your project. Actually creates working commands, not theoretical ones.

## What This Actually Does

1. Reads your PROJECT-DNA.md
2. Identifies what commands would be useful
3. Creates actual command files in `.claude/commands/generated/`
4. Commands that work immediately

## Generation Logic

### For React Projects
Generate these commands:
- `/create-component [name]` - Creates component with your patterns
- `/add-test [component]` - Adds test file with your test framework
- `/create-hook [name]` - Creates custom React hook
- `/add-route [path]` - Adds new route to your router
- `/create-context [name]` - Creates React context

### For Python/Django Projects
Generate these commands:
- `/create-model [name]` - Creates Django model
- `/add-view [name]` - Creates view with your patterns
- `/create-api-endpoint [path]` - Creates API endpoint
- `/add-test [module]` - Creates test file
- `/create-migration [description]` - Creates migration

### For Node.js/Express Projects
Generate these commands:
- `/create-route [path]` - Creates Express route
- `/add-middleware [name]` - Creates middleware
- `/create-controller [name]` - Creates controller
- `/add-validation [route]` - Adds validation
- `/create-service [name]` - Creates service layer

## Template Example

Here's what a generated command looks like:

```markdown
# Example command template (not an actual command):
# ---
# name: create-component-example
# description: Create a React component with project patterns
# usage: "create-component [ComponentName] [type:functional|class]"
# allowed-tools: [Write, Edit]
# category: generated
# ---

# Create Component - Project Specific

Creates a new React component following YOUR patterns:
- Uses TypeScript (detected from your project)
- Functional components with hooks (your pattern)
- CSS Modules for styling (your pattern)
- Colocated tests (your structure)

## Usage
/create-component Button
/create-component UserCard functional

## What Gets Created

For `/create-component Button`:

### 1. Component File: src/components/Button/Button.tsx
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
    <button 
      className={styles[variant]}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
\```

### 2. Test File: src/components/Button/Button.test.tsx
\```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders children', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('handles click events', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});
\```

### 3. Style File: src/components/Button/Button.module.css
\```css
.primary {
  background-color: #007bff;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.secondary {
  background-color: transparent;
  color: #007bff;
  padding: 8px 16px;
  border: 1px solid #007bff;
  border-radius: 4px;
  cursor: pointer;
}
\```

### 4. Index File: src/components/Button/index.ts
\```typescript
export { Button } from './Button';
\```
```

## How Generation Works

### Step 1: Read PROJECT-DNA.md
```
Claude reads PROJECT-DNA.md to understand:
- Technology stack (React, TypeScript, Jest)
- File structure (components folder pattern)
- Naming conventions (PascalCase components)
- Test patterns (Testing Library, colocated)
```

### Step 2: Select Appropriate Commands
```
Based on stack, generate commands for:
- Component creation (for React)
- Model creation (for Django)
- Route creation (for Express)
- Test creation (universal)
```

### Step 3: Customize Templates
```
Adjust templates to match:
- Your file naming (Button.tsx vs button.tsx)
- Your test framework (Jest vs Mocha)
- Your style approach (CSS Modules vs styled-components)
- Your structure (flat vs nested)
```

### Step 4: Write Command Files
```
Create files in .claude/commands/generated/:
- create-component.md
- add-test.md
- create-hook.md
- [3-7 more based on your stack]
```

## Output Structure

After running this command:
```
.claude/commands/generated/
├── create-component.md
├── add-test.md
├── create-hook.md
├── add-route.md
├── create-context.md
└── README.md (explains the generated commands)
```

## Success Criteria

The generated commands will:
- ✅ Match your project's actual patterns
- ✅ Use your testing framework
- ✅ Follow your naming conventions
- ✅ Work immediately when run
- ✅ Create files in the right locations

## After Generation

1. Review generated commands in `.claude/commands/generated/`
2. Try a command: `/create-component TestButton`
3. Check that files were created correctly
4. Adjust if needed

## Important Notes

- Generates 5-10 commands based on your stack
- Commands are immediately usable
- No complex configuration needed
- Simple templates that work
- Can be edited/customized after generation

---
*This is the simplified, actually functional version of command generation*