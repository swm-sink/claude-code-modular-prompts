# Project DNA Analysis
*Generated: 2025-01-09 10:30:00*

## Technology Stack
- **Language**: TypeScript
- **Framework**: React 18.2.0
- **Testing**: Jest + React Testing Library
- **Package Manager**: npm
- **Build Tool**: Vite
- **Styling**: CSS Modules

## Project Structure
- **Organization**: Feature-based with component folders
- **Source Directory**: src/
- **Test Location**: Colocated with components
- **Asset Management**: public/ for static assets

## Conventions
- **File Naming**: PascalCase for components (Button.tsx)
- **Component Pattern**: Functional components with hooks
- **Test Pattern**: Component.test.tsx
- **Export Pattern**: Named exports with index files

## Discovered Patterns

### Component Structure
```
src/components/Button/
├── Button.tsx          # Component implementation
├── Button.test.tsx     # Jest tests
├── Button.module.css   # CSS Module styles
└── index.ts           # Barrel export
```

### Test Structure
```typescript
import { render, screen, fireEvent } from '@testing-library/react';
describe('Component', () => {
  it('should render correctly', () => {
    // Arrange, Act, Assert pattern
  });
});
```

### API/Route Structure
```typescript
// React Router v6 pattern
<Route path="/users/:id" element={<UserDetail />} />
```

## Recommendations for Generation

Based on this analysis, generate:
1. Component generators matching folder structure
2. Test generators using React Testing Library
3. Hook creators following custom hook patterns
4. Route helpers for React Router v6
5. Context creators for state management

## Confidence Score
- High confidence: React, TypeScript, Jest, Component patterns
- Medium confidence: State management approach
- Low confidence: Backend API integration patterns