# Project DNA Analysis
*Generated: 2025-01-09T15:30:00Z*
*Project: example-react-app*

## Technology Stack
- **Language**: TypeScript 5.0
- **Framework**: React 18.2.0
- **Testing**: Jest 29.5, React Testing Library 14.0
- **Package Manager**: npm 9.0
- **Build Tool**: Vite 4.3
- **Styling**: CSS Modules

## Project Structure
- **Organization**: Feature-based with shared components
- **Source Directory**: src/
- **Test Location**: Colocated with components (.test.tsx files)
- **Component Pattern**: Folder per component with index export

Example structure discovered:
```
src/
├── components/          # Shared components
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.test.tsx
│   │   ├── Button.module.css
│   │   └── index.ts
│   └── Card/
│       ├── Card.tsx
│       ├── Card.test.tsx
│       ├── Card.module.css
│       └── index.ts
├── features/           # Feature modules
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── services/
│   └── dashboard/
│       ├── components/
│       ├── hooks/
│       └── services/
├── hooks/              # Shared hooks
├── services/           # API services
└── utils/              # Utilities
```

## Conventions
- **File Naming**: PascalCase for components, camelCase for utilities
- **Component Pattern**: Functional components with TypeScript interfaces
- **Test Pattern**: .test.tsx colocated with components
- **Export Pattern**: Named exports with index.ts barrel files
- **State Management**: React Context + useReducer for complex state
- **API Calls**: Axios with TypeScript interfaces

## Discovered Patterns

### Component Structure
```typescript
// Typical component pattern found
import React from 'react';
import styles from './ComponentName.module.css';

interface ComponentNameProps {
  // Props with TypeScript
}

export const ComponentName: React.FC<ComponentNameProps> = ({ ...props }) => {
  // Functional component with hooks
  return (
    <div className={styles.container}>
      {/* JSX */}
    </div>
  );
};
```

### Test Structure
```typescript
// Typical test pattern found
import { render, screen, fireEvent } from '@testing-library/react';
import { ComponentName } from './ComponentName';

describe('ComponentName', () => {
  it('should render correctly', () => {
    // Arrange → Act → Assert pattern
  });
});
```

### Hook Structure
```typescript
// Custom hook pattern found
import { useState, useEffect } from 'react';

export const useCustomHook = (param: ParamType) => {
  // Hook logic
  return { /* return values */ };
};
```

## Anti-Patterns Detected
- Some components missing TypeScript interfaces (3 instances)
- Inconsistent test coverage in features/ directory
- Mixed styling approaches (CSS Modules + inline styles)
- TODO comments found (7 instances)

## Recommendations for Generation

Based on this analysis, generate:

### High Priority Commands
1. **create-component** - Component with TypeScript, tests, and CSS Modules
2. **create-hook** - Custom React hook with TypeScript
3. **add-test** - Test file using React Testing Library
4. **create-feature** - New feature module with standard structure
5. **create-service** - API service with TypeScript interfaces

### Medium Priority Commands  
6. **add-context** - React Context provider and hook
7. **create-util** - Utility function with tests
8. **add-route** - React Router route configuration

### Customization Points
- Component template should include TypeScript interface
- Tests should use React Testing Library patterns
- CSS Modules for all component styling
- Index.ts barrel exports for all folders
- Follow discovered naming conventions

## Confidence Score

### High Confidence (90%+)
- React + TypeScript stack
- Component folder structure
- Testing with Jest + RTL
- CSS Modules for styling

### Medium Confidence (70-89%)
- Feature-based organization
- Custom hooks pattern
- API service structure

### Low Confidence (Below 70%)
- State management approach (Context vs Redux)
- Routing configuration (needs more analysis)
- Build optimization settings

## Generation Parameters

```json
{
  "language": "typescript",
  "framework": "react",
  "componentStyle": "functional",
  "testingFramework": "jest",
  "testingLibrary": "react-testing-library",
  "styling": "css-modules",
  "fileNaming": {
    "components": "PascalCase",
    "utilities": "camelCase",
    "tests": ".test.tsx"
  },
  "structure": {
    "componentsInFolders": true,
    "barrelExports": true,
    "colocatedTests": true
  }
}
```

---
*This DNA will be used to generate custom commands that match your exact patterns*