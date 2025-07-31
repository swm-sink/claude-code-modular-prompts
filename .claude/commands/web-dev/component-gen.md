---
name: /component-gen
description: Generate modern web components with tests, styles, and framework integration (v2.0)
version: 2.0
usage: '/component-gen [component-name] [--type functional|class|page] [--with-tests] [--with-styles] [--framework react|vue|angular] [--accessibility]'
category: web-dev
allowed-tools:
- Write
- Read
- Edit
- Bash
- Glob
dependencies:
- /validate-component
- /quick-command
- /test
validation:
  pre-execution: Validate component name and check for naming conflicts
  during-execution: Ensure all generated files follow conventions
  post-execution: Run tests and verify component integration
progressive-disclosure:
  layer-integration: Layer 1 generates basic components, Layer 2 adds testing/styling, Layer 3 enables full framework features
  escalation-path: Simple component → styled with tests → full feature integration
  de-escalation: Component templates reduce generation complexity
safety-measures:
  - Prevent overwriting existing components
  - Validate naming conventions
  - Check import paths
  - Ensure accessibility compliance
error-recovery:
  name-conflict: Suggest alternative names or versioning
  framework-mismatch: Auto-detect project framework
  style-conflict: Merge with existing style system
---

# Component Generator for [INSERT_PROJECT_NAME]

I'll help you generate **[INSERT_TECH_STACK]** components following your team's conventions and best practices for **[INSERT_PROJECT_NAME]**.

## Component Types

### Functional Components
Modern [INSERT_TECH_STACK] components:
```bash
# SECURITY: Component name 'Button' validated → 'src/components/Button/' ✅
/component-gen Button --type functional

# SECURITY: Component name 'UserCard' validated → 'src/components/UserCard/' ✅ 
/component-gen UserCard --with-hooks
```

### Page Components
Full page layouts:
```bash
/component-gen Dashboard --type page
/component-gen ProfilePage --with-routing
```

### Shared Components
Reusable UI elements:
```bash
/component-gen Modal --shared
/component-gen DataTable --with-props
```

## Framework Support

### For React Projects
```bash
/component-gen Header --react --typescript
```
- Functional components with hooks
- TypeScript interfaces
- Styled-components or CSS modules
- React Testing Library tests

### For Vue Projects
```bash
/component-gen NavigationBar --vue --composition-api
```
- Composition API by default
- Single File Components
- Scoped styles
- Vue Test Utils

### For Angular Projects
```bash
/component-gen UserList --angular --standalone
```
- Standalone components
- TypeScript strict mode
- Angular Material integration
- Jasmine/Karma tests

## Generation Options

### With Tests
Generate [INSERT_TESTING_FRAMEWORK] tests:
```bash
/component-gen ProductCard --with-tests
```
- Unit tests
- Integration tests
- Accessibility tests
- Snapshot tests

### With Styles
Include styling setup:
```bash
/component-gen Hero --with-styles
```
- CSS modules
- Styled-components
- SCSS/SASS
- Tailwind classes

### With State Management
Connect to state:
```bash
/component-gen TodoList --with-state
```
- Redux/Zustand/Pinia
- Context API
- Local state hooks

## Team Conventions

Following [INSERT_TEAM_SIZE] team standards:
- File naming: [ComponentName].[ext]
- Folder structure: features/components/
- Export patterns: named/default
- Props validation: TypeScript/PropTypes

## Accessibility Features

For [INSERT_USER_BASE] users:
- ARIA labels
- Keyboard navigation
- Screen reader support
- Focus management

## Performance Optimization

For [INSERT_PERFORMANCE_PRIORITY] requirements:
- Lazy loading setup
- Memo optimization
- Bundle splitting
- Virtual scrolling

## Component Structure

Generated with:
```
ComponentName/
├── index.ts                 # Barrel export
├── ComponentName.tsx        # Component logic
├── ComponentName.styles.ts  # Styled components
├── ComponentName.test.tsx   # Tests
├── ComponentName.stories.tsx # Storybook
└── types.ts                # TypeScript types
```

## Integration

### With [INSERT_API_STYLE]
Data fetching setup:
- API hooks
- Loading states
- Error handling
- Data caching

### With [INSERT_CI_CD_PLATFORM]
CI/CD ready:
- Test coverage
- Linting passes
- Build optimization
- Documentation

## Examples

### Basic Component
```bash
/component-gen Avatar
```

### Full-Featured Component
```bash
/component-gen DataGrid \
  --with-tests \
  --with-styles \
  --with-storybook \
  --with-docs
```

### Domain Component
```bash
/component-gen [INSERT_DOMAIN]Widget \
  --with-api \
  --with-state
```

---

What component would you like to generate for [INSERT_PROJECT_NAME]?