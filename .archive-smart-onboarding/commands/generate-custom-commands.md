---
name: /generate-custom-commands
description: Generate project-specific commands based on detected patterns and conventions
usage: "/generate-custom-commands [--category all|components|api|testing|workflow]"
allowed-tools: [Read, Write, MultiEdit, Glob, Grep]
---

# 🎯 Custom Command Generator

I create commands specifically tailored to YOUR project based on the patterns and conventions I've detected. These aren't generic templates - they're built to match exactly how YOUR team writes code.

## How It Works

### 1. Pattern Analysis
I analyze your existing code to understand:
- How you structure components
- How you name files and functions
- Where you put different types of code
- What testing approach you use
- Your API design patterns

### 2. Command Generation
Based on those patterns, I generate commands that:
- Follow YOUR naming conventions
- Use YOUR file structure
- Match YOUR coding style
- Integrate with YOUR tools
- Respect YOUR workflow

### 3. Progressive Enhancement
Commands evolve as I learn more:
- Start with detected patterns
- Learn from your corrections
- Adapt to new patterns
- Improve over time

## Generated Command Categories

### Component Commands
Based on your component patterns:

```javascript
// If I detect: src/components/atoms/Button/Button.tsx
// I generate: /create-atom command

// If I detect: features/user/components/UserProfile.tsx  
// I generate: /create-feature-component command

// If I detect: components/Button.tsx + Button.test.tsx + Button.stories.tsx
// I generate: /create-component with test and story files
```

Example generated command:
```markdown
---
name: /create-component
description: Create component following your atomic design pattern
usage: "/create-component <name> [atom|molecule|organism]"
---

Creates a component with your exact structure:
- src/components/{type}/{Name}/
  - {Name}.tsx (component)
  - {Name}.test.tsx (test)
  - {Name}.stories.tsx (storybook)
  - {Name}.module.css (styles)
  - index.ts (export)
```

### API Commands
Based on your API patterns:

```javascript
// If I detect: pages/api/v1/users/[id].ts
// I generate: /create-api with versioning

// If I detect: src/controllers/UserController.ts
// I generate: /create-controller command

// If I detect: GraphQL resolvers
// I generate: /create-resolver command
```

Example generated command:
```markdown
---
name: /create-endpoint
description: Create REST endpoint following your patterns
usage: "/create-endpoint <resource> [GET|POST|PUT|DELETE]"
---

Creates endpoint matching your style:
- Versioned paths (/api/v1/)
- JWT authentication
- Zod validation
- Prisma integration
- Error handling pattern
- OpenAPI documentation
```

### Testing Commands
Based on your testing approach:

```javascript
// If I detect: __tests__/ folders
// I generate: /test creating files there

// If I detect: *.spec.ts pattern
// I generate: /create-spec command

// If I detect: E2E tests with Playwright
// I generate: /create-e2e command
```

### Workflow Commands
Based on your team workflow:

```javascript
// If I detect: feature/* branch pattern
// I generate: /start-feature command

// If I detect: conventional commits
// I generate: /commit with formatting

// If I detect: PR templates
// I generate: /create-pr command
```

## Customization Examples

### Your Patterns Become Commands

#### Pattern Found: Barrel Exports
```typescript
// Detected: Every folder has index.ts with exports
// Generated command includes barrel file creation
/create-module UserAuth
  → Creates UserAuth/index.ts with exports
```

#### Pattern Found: DTOs and Entities
```typescript
// Detected: DTOs for API, Entities for database
// Generated commands for both
/create-dto User
  → Creates src/dtos/UserDto.ts
/create-entity User  
  → Creates src/entities/User.entity.ts
```

#### Pattern Found: Custom Hook Pattern
```typescript
// Detected: hooks/ folder with use* naming
// Generated command for hooks
/create-hook useUserData
  → Creates src/hooks/useUserData.ts
  → Includes test file
  → Adds to hooks/index.ts
```

## Real Example

### What I Detect in Your Project:
```
📁 Analysis Results:
- Components: Atomic design in src/components/
- State: Zustand stores in src/store/
- API: tRPC routers in src/server/api/
- Tests: Vitest with @testing-library
- Styles: Tailwind CSS with cn() helper
```

### Commands I Generate:
```yaml
/atom Button
  Creates: src/components/atoms/Button/
  - Button.tsx (with Tailwind classes)
  - Button.test.tsx (with Vitest)
  - index.ts (barrel export)

/store user
  Creates: src/store/userStore.ts
  - Zustand store with TypeScript
  - Following your naming pattern
  - Includes your middleware

/trpc users
  Creates: src/server/api/routers/users.ts
  - tRPC router structure
  - Your validation approach
  - Your error handling

/feature checkout
  Creates: src/features/checkout/
  - components/ (local components)
  - hooks/ (feature hooks)
  - store/ (feature state)
  - api/ (feature endpoints)
  - index.ts (public API)
```

## Smart Generation Features

### 1. Import Detection
```javascript
// I detect your import style and generate accordingly:
detectImportStyle() {
  if (uses('@/components')) generateWithAlias('@')
  if (uses('../../../')) generateWithRelative()
  if (uses('src/')) generateWithAbsolute()
}
```

### 2. Testing Integration
```javascript
// I detect your testing patterns:
detectTestingPattern() {
  const hasTestingLibrary = uses('@testing-library/react')
  const hasStoriesFiles = exists('*.stories.tsx')
  const hasE2E = exists('e2e/*.spec.ts')
  
  // Generate commands include appropriate tests
}
```

### 3. State Management
```javascript
// I detect what you use and generate accordingly:
if (uses('redux')) generateReduxCommands()
if (uses('zustand')) generateZustandCommands()
if (uses('mobx')) generateMobXCommands()
if (uses('context')) generateContextCommands()
```

## Generation Output

### Summary Mode (default)
```
🎯 Generated 12 Custom Commands:

Component Commands (4):
  /component    - Create atomic component
  /page        - Create Next.js page
  /layout      - Create layout component
  /hook        - Create custom hook

API Commands (3):
  /endpoint    - Create REST endpoint
  /middleware  - Create API middleware
  /validation  - Create Zod schema

Testing Commands (2):
  /test        - Create test file
  /e2e         - Create E2E test

Workflow Commands (3):
  /feature     - Start feature branch
  /commit      - Conventional commit
  /review      - Create PR with template
```

### Detailed Mode (--detailed)
Shows full command definitions with:
- Complete YAML frontmatter
- Full command documentation
- Usage examples
- Generated file structures

## Progressive Learning

The commands improve over time:

### Day 1: Basic Patterns
```javascript
// Initial: Detected basic structure
/component Button
  → Creates simple component file
```

### Week 1: Learned Preferences
```javascript
// Learned: You always add PropTypes
/component Button
  → Includes PropTypes automatically
```

### Month 1: Deep Understanding
```javascript
// Learned: Complex patterns
/component Button
  → Includes your animation library
  → Uses your theming system
  → Follows your accessibility patterns
  → Matches your documentation style
```

## The Magic

Your commands are yours alone. They:
- Match YOUR exact patterns
- Follow YOUR conventions
- Use YOUR tools
- Fit YOUR workflow

Not generic templates. YOUR templates.