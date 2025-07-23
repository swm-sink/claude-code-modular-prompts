# CLAUDE.md Best Practices

## Overview

CLAUDE.md is a special Markdown file that Claude Code automatically ingests to gain project-specific context. It serves as the "constitution" for your AI assistant, transforming it from a generic tool to a specialized, project-aware developer.

## Core Principles

1. **Conciseness**: Keep it human-readable and under 500 lines
2. **Specificity**: Be explicit about conventions and preferences
3. **Hierarchy**: Layer files from global to project-specific
4. **Maintenance**: Update regularly as project evolves

## File Location Hierarchy

Claude Code searches for CLAUDE.md files in this order:

1. **Global** (`~/.claude/CLAUDE.md`)
   - Personal preferences
   - Global coding standards
   - Common tools/commands

2. **Project Root** (`/project/CLAUDE.md`)
   - Project-specific rules
   - Team conventions
   - Shared with version control

3. **Subdirectory** (`/project/subdir/CLAUDE.md`)
   - Module-specific rules
   - Overrides parent settings
   - Useful for monorepos

4. **Local** (`/project/CLAUDE.local.md`)
   - Personal project overrides
   - Add to .gitignore
   - Developer-specific settings

## Essential Sections

### 1. Tech Stack & Environment

```markdown
# Tech Stack
- Framework: Next.js 14 with App Router
- Language: TypeScript 5.2 (strict mode)
- Runtime: Node.js 20 LTS
- Package Manager: pnpm (not npm!)
- Styling: Tailwind CSS 3.4 + CSS Modules
- Database: PostgreSQL 15 with Prisma ORM
- Testing: Jest + React Testing Library

# Environment Setup
- Node version: Use .nvmrc (v20.11.0)
- Environment files: .env.local (never .env)
- Required: NEXT_PUBLIC_* for client vars
```

### 2. Project Structure

```markdown
# Project Structure
- `src/app/`: Next.js 14 App Router pages
- `src/components/`: Reusable React components
  - `ui/`: Base UI components (Button, Card, etc.)
  - `features/`: Feature-specific components
- `src/lib/`: Core utilities and business logic
  - `api/`: API client functions
  - `db/`: Database queries and models
  - `utils/`: Helper functions
- `src/styles/`: Global styles and Tailwind config
- `src/types/`: TypeScript type definitions
- `tests/`: Test files mirroring src structure
```

### 3. Commands & Scripts

```markdown
# Commands
- `pnpm dev`: Start development server (port 3000)
- `pnpm build`: Build for production
- `pnpm test`: Run all tests
- `pnpm test:watch`: Run tests in watch mode
- `pnpm lint`: Run ESLint
- `pnpm typecheck`: Run TypeScript compiler
- `pnpm db:migrate`: Run database migrations
- `pnpm db:seed`: Seed development database

# Git Hooks (via Husky)
- Pre-commit: Runs lint and typecheck
- Pre-push: Runs full test suite
```

### 4. Code Style & Conventions

```markdown
# Code Style
- Use ES modules (import/export), never CommonJS
- Prefer named exports over default exports
- Use arrow functions for components
- Destructure props in function signature
- Sort imports: react → next → third-party → local

# Naming Conventions
- Components: PascalCase (UserProfile.tsx)
- Utilities: camelCase (formatDate.ts)
- Constants: UPPER_SNAKE_CASE
- Types/Interfaces: PascalCase with 'I' prefix for interfaces
- API routes: kebab-case

# TypeScript Rules
- No 'any' types (use 'unknown' if needed)
- Explicit return types for functions
- Interface over type for object shapes
- Strict null checks enabled
```

### 5. Testing Requirements

```markdown
# Testing Standards
- Minimum 80% code coverage
- Test file naming: *.test.ts(x) or *.spec.ts(x)
- Use React Testing Library (no enzyme)
- Mock external dependencies
- Test user behavior, not implementation

# Test Structure
describe('ComponentName', () => {
  it('should handle user interaction', () => {
    // Arrange, Act, Assert pattern
  });
});
```

### 6. Git Workflow

```markdown
# Git Workflow
- Branch naming: feature/JIRA-123-description
- Commit format: type(scope): message
  - Types: feat, fix, docs, style, refactor, test, chore
- PR titles: [JIRA-123] Brief description
- Squash and merge (no merge commits)
- Delete branches after merge

# Protected Branches
- main: Requires PR + 2 approvals + passing CI
- staging: Requires PR + 1 approval
```

### 7. API & Database Patterns

```markdown
# API Patterns
- RESTful endpoints: /api/v1/resources
- Use API routes in src/app/api/
- Return consistent error format:
  { error: { message: string, code: string } }
- Always validate request body with zod

# Database Patterns
- Use Prisma for all queries (no raw SQL)
- Transactions for multi-table updates
- Soft deletes (deletedAt timestamp)
- UUID primary keys, not auto-increment
```

### 8. Security & Performance

```markdown
# Security Rules
- Never commit .env files
- Use environment variables for secrets
- Validate all user inputs
- Sanitize data before rendering
- Use HTTPS in production
- Implement rate limiting

# Performance Guidelines
- Lazy load components with dynamic imports
- Optimize images with next/image
- Use React.memo for expensive components
- Implement pagination (limit: 20 items)
- Cache API responses appropriately
```

### 9. The "Do Not" Section

```markdown
# DO NOT
- Edit files in src/legacy/ (migration in progress)
- Use console.log (use logger utility)
- Commit directly to main or staging
- Use !important in CSS
- Create files larger than 300 lines
- Ignore TypeScript errors
- Skip writing tests
- Use var (use const/let)
- Install packages without team discussion
```

### 10. Error Handling

```markdown
# Error Handling
- Use custom AppError class for known errors
- Log errors with context (user, action, timestamp)
- Show user-friendly error messages
- Implement error boundaries for React
- Report to Sentry in production
- Never expose stack traces to users
```

## Advanced Patterns

### Monorepo Configuration

```markdown
# Monorepo Structure
/packages/
  /web: Next.js frontend (this CLAUDE.md)
  /api: Express backend (see ./api/CLAUDE.md)
  /shared: Shared utilities

# Workspace Commands
- Run from root: pnpm --filter web dev
- Install in package: pnpm --filter web add package
```

### Dynamic Sections

```markdown
# Current Sprint Focus
> Updated: 2025-07-22
- Implementing new authentication flow
- Migrating from REST to GraphQL
- Performance optimization priority

# Known Issues
- Memory leak in Dashboard component (#123)
- Flaky test in user.test.ts (#124)
```

### Integration Points

```markdown
# External Services
- Auth: Auth0 (see lib/auth/config.ts)
- Payments: Stripe (webhook: /api/webhooks/stripe)
- Email: SendGrid (templates in /emails)
- Storage: AWS S3 (use lib/storage helpers)

# API Keys Location
- Development: .env.local
- Staging: Vercel environment variables
- Production: AWS Secrets Manager
```

## Real-World Examples

### Example 1: Full-Stack Application

```markdown
# Claude Code Assistant Configuration

## Project Overview
E-commerce platform built with Next.js, focusing on performance and SEO.

## Tech Stack
- Next.js 14 (App Router)
- TypeScript 5.2
- PostgreSQL + Prisma
- Redis for caching
- Stripe for payments

## Key Files
- `/src/app/api/checkout/route.ts`: Payment processing
- `/src/lib/cart.ts`: Cart management logic
- `/src/components/ProductCard.tsx`: Main product display

## Coding Standards
- Mobile-first responsive design
- Accessibility: WCAG 2.1 AA compliance
- Performance: Core Web Vitals targets
  - LCP < 2.5s
  - FID < 100ms
  - CLS < 0.1

## Current Tasks
Working on cart abandonment recovery feature.
Reference: /docs/cart-recovery-spec.md

## Testing Requirements
- Unit tests for all utilities
- Integration tests for API routes
- E2E tests for critical user paths
```

### Example 2: Microservices

```markdown
# Service: User Authentication API

## Architecture
Microservice handling authentication and authorization.
Part of larger microservices ecosystem.

## Communication
- Internal: gRPC (port 50051)
- External: REST API (port 3001)
- Message Queue: RabbitMQ

## Development Workflow
1. Make changes
2. Run `make test` (includes integration tests)
3. Run `make proto` if protobuf changes
4. Deploy with `kubectl apply -f k8s/`

## Service Dependencies
- PostgreSQL: User data
- Redis: Session storage
- Vault: Secret management

## Monitoring
- Logs: Structured JSON to stdout
- Metrics: Prometheus (port 9090)
- Traces: Jaeger integration

## Do Not
- Store passwords (use bcrypt hashes)
- Log sensitive data (PII, tokens)
- Skip rate limiting
```

## Tips for Effectiveness

### 1. Keep It Updated
```bash
# Add update script
echo "Review and update CLAUDE.md" >> .git/hooks/pre-push
```

### 2. Version Control
```bash
# Track changes
git add CLAUDE.md
git commit -m "docs: Update CLAUDE.md with new API patterns"
```

### 3. Team Collaboration
- Review CLAUDE.md in onboarding
- Update during sprint planning
- Include in PR reviews

### 4. Measure Impact
- Track reduction in repeated mistakes
- Monitor consistency improvements
- Gather team feedback

## Common Pitfalls to Avoid

1. **Too Verbose**: Keep under 500 lines
2. **Too Generic**: Be specific to your project
3. **Outdated Information**: Regular updates essential
4. **Conflicting Rules**: Ensure consistency
5. **Missing Context**: Include "why" not just "what"

## Integration with Other Tools

### With Custom Commands

```markdown
# Custom Commands Available
- /project:lint - Run linting with auto-fix
- /project:test-feature - Test current feature branch
- /project:deploy-staging - Deploy to staging
See .claude/commands/ for all available commands
```

### With MCP Servers

```markdown
# MCP Integrations
- GitHub: PR management, issue tracking
- Slack: Notifications, alerts
- Jira: Task updates
Configuration in .mcp.json
```

## Conclusion

A well-crafted CLAUDE.md file:
- Reduces repetitive corrections
- Improves code consistency
- Accelerates development
- Facilitates team collaboration
- Serves as living documentation

Investment in maintaining this file pays dividends in productivity and code quality.