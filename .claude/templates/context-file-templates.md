# Context File Templates for Claude Code
*Research-based templates optimized for Claude Code's 200K token window*

## 📁 Template 1: Essential Project Context (00-essential.md)
*Keep under 100 lines for instant loading*

```markdown
# Project: [PROJECT_NAME] Essential Context

## 🎯 Project Overview
**Vision**: [One-line vision statement]
**Type**: [web-app|cli-tool|library|api|mobile]
**Stage**: [prototype|development|production]

## 🔧 Tech Stack
- **Language**: [Primary language and version]
- **Framework**: [Main framework and version]
- **Database**: [Database type if applicable]
- **Key Dependencies**: [Critical 3-5 dependencies]

## 📂 Project Structure
\`\`\`
src/
├── [main-module]/     # [Purpose]
├── [core-module]/     # [Purpose]
└── [utils]/           # [Purpose]
\`\`\`

## 🚀 Critical Commands
\`\`\`bash
# Development
npm run dev          # Start development server

# Testing
npm test             # Run test suite

# Build
npm run build        # Production build
\`\`\`

## ⚠️ Project-Specific Rules
1. **NEVER** [Critical prohibition]
2. **ALWAYS** [Critical requirement]
3. **Pattern**: [Key pattern to follow]

## 🔍 Current Focus
**Active Feature**: [What's being worked on]
**Known Issues**: [Critical bugs/blockers]
**Next Steps**: [Immediate priorities]

## 📚 Quick References
- Architecture: @docs/architecture.md
- Patterns: @docs/patterns.md
- API Docs: @docs/api.md
```

## 📁 Template 2: Architecture Context (01-architecture.md)

```markdown
# [PROJECT_NAME] Architecture Context

## 🏗️ System Architecture

### High-Level Design
\`\`\`
[User] → [Frontend] → [API Gateway] → [Services] → [Database]
\`\`\`

### Core Components

#### 1. [Component Name]
- **Purpose**: [What it does]
- **Location**: `src/[path]`
- **Dependencies**: [Key dependencies]
- **Patterns**: [Design patterns used]

#### 2. [Component Name]
- **Purpose**: [What it does]
- **Location**: `src/[path]`
- **Dependencies**: [Key dependencies]
- **Patterns**: [Design patterns used]

## 🔄 Data Flow

### Request Lifecycle
1. **Entry**: [How requests enter]
2. **Validation**: [How validated]
3. **Processing**: [Core processing]
4. **Response**: [How responses formed]

### State Management
- **Pattern**: [Redux|Context|MobX|etc]
- **Store Location**: `src/store`
- **Key Slices**: [Main state sections]

## 🔌 Integration Points

### External Services
| Service | Purpose | Authentication |
|---------|---------|---------------|
| [API] | [Purpose] | [Auth type] |
| [Service] | [Purpose] | [Auth type] |

### Internal APIs
\`\`\`typescript
// Core API patterns
interface [EntityAPI] {
  get(id: string): Promise<Entity>
  list(filters: Filters): Promise<Entity[]>
  create(data: CreateDTO): Promise<Entity>
  update(id: string, data: UpdateDTO): Promise<Entity>
  delete(id: string): Promise<void>
}
\`\`\`

## 📊 Performance Considerations
- **Bottlenecks**: [Known performance issues]
- **Optimization**: [Current optimizations]
- **Monitoring**: [How performance tracked]

## 🛡️ Security Architecture
- **Authentication**: [Auth method]
- **Authorization**: [Permission system]
- **Data Protection**: [Encryption/security measures]
```

## 📁 Template 3: Domain Context (02-domain.md)

```markdown
# [PROJECT_NAME] Domain Context

## 🎯 Business Domain

### Core Concepts
1. **[Entity]**: [Business definition and rules]
2. **[Entity]**: [Business definition and rules]
3. **[Process]**: [Business workflow description]

### Domain Terminology
| Term | Definition | Code Reference |
|------|------------|----------------|
| [Term] | [Business meaning] | `src/domain/[file]` |
| [Term] | [Business meaning] | `src/domain/[file]` |

## 📋 Business Rules

### Critical Rules
1. **Rule**: [Description]
   - Implementation: `src/rules/[file]`
   - Validation: [How validated]

2. **Rule**: [Description]
   - Implementation: `src/rules/[file]`
   - Validation: [How validated]

### Workflows

#### [Workflow Name]
\`\`\`mermaid
graph LR
    A[Start] --> B[Step 1]
    B --> C{Decision}
    C -->|Yes| D[Action]
    C -->|No| E[Alternative]
    D --> F[End]
    E --> F
\`\`\`

## 👥 User Personas

### [Persona Name]
- **Role**: [User role]
- **Goals**: [What they want]
- **Pain Points**: [Problems they face]
- **Features Used**: [Key features]

## 📊 Data Models

### Core Entities
\`\`\`typescript
interface [Entity] {
  id: string
  [field]: [type]
  // Business rules enforced
  validate(): ValidationResult
  // Domain operations
  [operation](): [ReturnType]
}
\`\`\`

### Relationships
- [Entity] has many [Entity]
- [Entity] belongs to [Entity]
- [Entity] has and belongs to many [Entity]

## 🔄 Business Processes

### [Process Name]
**Trigger**: [What starts it]
**Steps**:
1. [Step description]
2. [Step description]
3. [Step description]
**Output**: [What it produces]
**SLA**: [Time requirements]
```

## 📁 Template 4: Patterns & Anti-Patterns (03-patterns.md)

```markdown
# [PROJECT_NAME] Patterns & Anti-Patterns

## ✅ Established Patterns

### Code Patterns

#### [Pattern Name]
\`\`\`typescript
// Good: Follow this pattern
class [Example] {
  constructor(private readonly deps: Dependencies) {}
  
  async execute(input: Input): Promise<Output> {
    // Validate
    const validated = this.validate(input);
    // Process
    const result = await this.process(validated);
    // Return
    return this.format(result);
  }
}
\`\`\`

### Testing Patterns
\`\`\`typescript
// Standard test structure
describe('[Component]', () => {
  let sut: SystemUnderTest;
  
  beforeEach(() => {
    sut = createTestSubject();
  });
  
  describe('[method]', () => {
    it('should [expected behavior]', async () => {
      // Arrange
      const input = createTestInput();
      
      // Act
      const result = await sut.method(input);
      
      // Assert
      expect(result).toMatchExpectation();
    });
  });
});
\`\`\`

## ❌ Anti-Patterns to Avoid

### Code Anti-Patterns

#### [Anti-Pattern Name]
\`\`\`typescript
// BAD: Never do this
class [BadExample] {
  async execute(input: any): Promise<any> {
    // No validation
    // Direct database access
    const result = await db.query('SELECT * FROM...');
    // No error handling
    return result;
  }
}

// GOOD: Do this instead
class [GoodExample] {
  constructor(private repository: Repository) {}
  
  async execute(input: ValidatedInput): Promise<Result> {
    try {
      return await this.repository.find(input);
    } catch (error) {
      throw new DomainError('Operation failed', error);
    }
  }
}
\`\`\`

## 🎯 Project-Specific Conventions

### Naming Conventions
- **Files**: kebab-case.ts
- **Classes**: PascalCase
- **Functions**: camelCase
- **Constants**: UPPER_SNAKE_CASE
- **Interfaces**: IPrefixedName

### File Organization
\`\`\`
[feature]/
├── [feature].controller.ts    # HTTP layer
├── [feature].service.ts       # Business logic
├── [feature].repository.ts    # Data access
├── [feature].dto.ts          # Data transfer objects
├── [feature].entity.ts       # Domain model
└── [feature].spec.ts         # Tests
\`\`\`

### Error Handling
\`\`\`typescript
// Always use typed errors
class DomainError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly context?: unknown
  ) {
    super(message);
  }
}

// Never use generic catch
try {
  await riskyOperation();
} catch (error) {
  if (error instanceof SpecificError) {
    // Handle specific case
  }
  throw new DomainError('Operation failed', 'OP_001', error);
}
\`\`\`

## 📝 Code Review Checklist
- [ ] Follows established patterns
- [ ] No anti-patterns present
- [ ] Proper error handling
- [ ] Tests included
- [ ] Documentation updated
- [ ] Performance considered
- [ ] Security validated
```

## 📁 Template 5: Testing Context (04-testing.md)

```markdown
# [PROJECT_NAME] Testing Context

## 🧪 Testing Strategy

### Test Pyramid
\`\`\`
         /\\
        /  \\  E2E (10%)
       /    \\
      /------\\ Integration (30%)
     /        \\
    /__________\\ Unit (60%)
\`\`\`

### Coverage Requirements
- **Overall**: >= 80%
- **Critical Paths**: >= 95%
- **New Code**: >= 90%

## 🔧 Testing Setup

### Test Runner Configuration
\`\`\`javascript
// jest.config.js or vitest.config.js
module.exports = {
  preset: '[preset]',
  testEnvironment: '[environment]',
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
\`\`\`

### Test Commands
\`\`\`bash
npm test              # Run all tests
npm test:unit         # Unit tests only
npm test:integration  # Integration tests
npm test:e2e         # End-to-end tests
npm test:coverage    # With coverage report
\`\`\`

## 📋 Test Patterns

### Unit Test Template
\`\`\`typescript
describe('[Component]', () => {
  describe('[method]', () => {
    it('should [behavior] when [condition]', () => {
      // Arrange
      const input = createInput();
      const expected = createExpected();
      
      // Act
      const result = component.method(input);
      
      // Assert
      expect(result).toEqual(expected);
    });
    
    it('should throw when [invalid condition]', () => {
      // Arrange
      const invalidInput = createInvalidInput();
      
      // Act & Assert
      expect(() => component.method(invalidInput))
        .toThrow(ExpectedError);
    });
  });
});
\`\`\`

### Integration Test Template
\`\`\`typescript
describe('[Feature] Integration', () => {
  let app: TestApp;
  
  beforeAll(async () => {
    app = await createTestApp();
  });
  
  afterAll(async () => {
    await app.cleanup();
  });
  
  it('should [complete workflow]', async () => {
    // Step 1: Setup
    const user = await app.createUser();
    
    // Step 2: Execute
    const response = await app.request()
      .post('/endpoint')
      .send({ data: 'test' })
      .expect(200);
    
    // Step 3: Verify
    expect(response.body).toMatchSnapshot();
    const dbRecord = await app.db.find(response.body.id);
    expect(dbRecord).toBeDefined();
  });
});
\`\`\`

## 🎯 Critical Test Scenarios

### Must-Test Scenarios
1. **Authentication Flow**: User login/logout
2. **Authorization**: Permission checks
3. **Data Validation**: Input validation
4. **Error Handling**: Error responses
5. **Edge Cases**: Boundary conditions

### Test Data Management
\`\`\`typescript
// Test fixtures
export const fixtures = {
  validUser: () => ({
    id: 'test-id',
    email: 'test@example.com',
    role: 'user'
  }),
  
  invalidUser: () => ({
    id: null,
    email: 'invalid',
    role: 'unknown'
  })
};

// Test factories
export const factories = {
  user: Factory.define<User>(() => ({
    id: faker.uuid(),
    email: faker.internet.email(),
    createdAt: new Date()
  }))
};
\`\`\`

## ⚠️ Common Testing Pitfalls
1. **Avoid**: Testing implementation details
2. **Avoid**: Brittle selectors in E2E tests
3. **Avoid**: Shared state between tests
4. **Avoid**: Time-dependent tests
5. **Avoid**: Network calls in unit tests
```

## 📁 Template 6: Session Management (05-session.md)

```markdown
# [PROJECT_NAME] Session Context

## 📊 Current Session State

### Active Work
**Branch**: [current-branch]
**Feature**: [feature-name]
**Started**: [timestamp]
**Progress**: [percentage]%

### Session Goals
- [ ] [Goal 1]
- [ ] [Goal 2]
- [ ] [Goal 3]

## 🔄 Recent Changes

### Files Modified
\`\`\`bash
modified: src/[file1.ts]
modified: src/[file2.ts]
added: src/[newfile.ts]
\`\`\`

### Decisions Made
1. **Decision**: [What was decided]
   - **Rationale**: [Why]
   - **Impact**: [What changes]

2. **Decision**: [What was decided]
   - **Rationale**: [Why]
   - **Impact**: [What changes]

## ⚠️ Pending Issues

### Blockers
- **Issue**: [Description]
  - **Impact**: [What's blocked]
  - **Next Step**: [How to resolve]

### Technical Debt
- [ ] Refactor [component]
- [ ] Add tests for [feature]
- [ ] Update documentation for [module]

## 📝 Session Notes

### Key Discoveries
- [Important finding 1]
- [Important finding 2]

### Questions for Team
- [Question needing team input]
- [Architecture decision needed]

### Next Session Priorities
1. [Top priority for next session]
2. [Second priority]
3. [Third priority]

## 🔗 References
- Related PR: #[number]
- Issue: #[number]
- Discussion: [link]
```

## 🎯 Usage Guidelines

### When to Use Each Template

1. **00-essential.md**: Always loaded, keep minimal
2. **01-architecture.md**: Load for structural changes
3. **02-domain.md**: Load for business logic work
4. **03-patterns.md**: Load for new feature development
5. **04-testing.md**: Load for test writing/debugging
6. **05-session.md**: Update at session start/end

### Token Optimization Strategy

```yaml
Initial Load:
  - 00-essential.md (500 tokens)
  
On-Demand Load:
  - @docs/01-architecture.md (2000 tokens)
  - @docs/02-domain.md (1500 tokens)
  - @docs/03-patterns.md (1000 tokens)
  - @docs/04-testing.md (1000 tokens)
  
Session Tracking:
  - 05-session.md (300 tokens, updated frequently)
  
Total Maximum: ~6300 tokens (well under 200K limit)
```

### Progressive Loading Example

```markdown
# In your conversation with Claude:

"I need to refactor the user authentication system"

# Claude automatically loads:
- 00-essential.md (always)
- @docs/01-architecture.md (for system structure)
- @docs/03-patterns.md (for coding patterns)

# Not loaded (saving tokens):
- 02-domain.md (not needed for auth)
- 04-testing.md (not testing yet)
```

---
*These templates are based on 75+ research sources and proven patterns from enterprise Claude Code implementations.*