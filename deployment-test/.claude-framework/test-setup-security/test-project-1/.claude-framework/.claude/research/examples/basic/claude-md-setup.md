# Basic CLAUDE.md Setup Example

## Overview
This example demonstrates how to create an effective CLAUDE.md file for a typical web development project.

## Example: E-commerce Platform

### File: `/project/CLAUDE.md`

```markdown
# ShopFlow E-commerce Platform

## Project Overview
Modern e-commerce platform built with Next.js, PostgreSQL, and Stripe.

## Quick Commands
- `npm run dev` - Start development server (port 3000)
- `npm run test:watch` - Run tests in watch mode
- `npm run db:migrate` - Run pending migrations
- `npm run build:prod` - Production build with optimizations

## Architecture Decisions
- **Frontend**: Next.js 14 with App Router
- **State**: Zustand for client state
- **Database**: PostgreSQL with Prisma ORM
- **Payments**: Stripe (test mode in dev)
- **Auth**: NextAuth with JWT

## Code Standards
- TypeScript strict mode enabled
- Functional components only (no class components)
- Named exports preferred over default
- Tests required for all new features
- Accessibility: WCAG 2.1 AA compliance

## Database
- Local: PostgreSQL in Docker (`docker-compose up -d`)
- Migrations: `prisma/migrations/`
- Seed data: `npm run db:seed`
- Reset: `npm run db:reset` (⚠️ deletes all data)

## Testing Strategy
- Unit tests: Vitest for components/utilities
- Integration: Playwright for user flows
- Coverage target: 80% for new code
- Run single test: `npm run test -- auth.test.ts`

## Common Tasks
### Add new product page
1. Create page in `app/products/[slug]/page.tsx`
2. Add to `lib/products/types.ts`
3. Update `components/ProductCard.tsx`
4. Add tests in `__tests__/products/`

### Update payment flow
- Webhook handler: `app/api/webhooks/stripe/route.ts`
- Test cards: See `.env.example`
- Logs: `stripe listen --forward-to localhost:3000/api/webhooks/stripe`

## Environment Variables
- Copy `.env.example` to `.env.local`
- Required: DATABASE_URL, STRIPE_SECRET_KEY, NEXTAUTH_SECRET
- Optional: ANALYTICS_ID, SENTRY_DSN

## Known Issues
- Hot reload sometimes fails on Windows - restart dev server
- Stripe webhooks require `stripe listen` running locally
- Database connection pool limited to 5 in dev

## Performance Notes
- Images: Use next/image with sizes prop
- Fonts: Preloaded in app/layout.tsx
- API routes: Cache with `revalidate` when possible

## Deployment
- Staging: Vercel preview on PRs
- Production: Manual deploy via GitHub Actions
- Database migrations run automatically

## Getting Help
- Tech lead: @alice (frontend), @bob (backend)
- Docs: `/docs` folder
- Design system: Storybook on port 6006
```

### File: `/project/CLAUDE.local.md`

```markdown
# Personal Development Notes

## My Setup
- Using VSCode with Prettier extension
- Database GUI: TablePlus
- API testing: Insomnia

## Local Shortcuts
- Skip pre-commit hooks: `git commit --no-verify`
- Fast DB reset: `./scripts/quick-reset.sh`
- My test user: test@example.com / password123

## WIP Features
- Working on: New checkout flow
- Branch: feature/checkout-v2
- Related PR: #234

## Personal TODOs
- [ ] Fix flaky test in checkout.test.ts
- [ ] Review Alice's PR on product search
- [ ] Update my local Stripe webhooks
```

## Key Principles Demonstrated

### 1. **Conciseness**
- Information is scannable
- Bullet points over paragraphs
- Links to detailed docs

### 2. **Specificity**
- Exact commands provided
- Specific file paths
- Clear version numbers

### 3. **Practicality**
- Common tasks documented
- Known issues listed
- Quick reference section

### 4. **Team Enablement**
- Shared via git
- Contact information
- Architecture decisions

### 5. **Personal Efficiency**
- Local overrides
- Personal shortcuts
- WIP tracking

## Usage Tips

### Adding New Information
```bash
# During development, press # to add instruction
# "Remember: The payment webhook needs ngrok in development"

# Or ask Claude directly
"Update CLAUDE.md to note that tests require TEST_MODE=true"
```

### Maintaining Relevance
- Review monthly
- Remove outdated info
- Update after major changes
- Date temporal information

### Token Optimization
- This example: ~450 tokens
- Optimal range: 200-500 tokens
- Monitor with: `wc -w CLAUDE.md`

## Benefits

1. **Faster Onboarding**: New developers productive quickly
2. **Fewer Interruptions**: Common questions answered
3. **Consistency**: Team follows same patterns
4. **Context Preservation**: Knowledge isn't lost
5. **Efficiency**: Claude provides better assistance

## Anti-Patterns to Avoid

❌ Including entire API documentation
❌ Duplicating README content
❌ Personal passwords/tokens
❌ Outdated information
❌ Generic best practices

✅ Project-specific information
✅ Frequently used commands
✅ Current architecture decisions
✅ Active known issues
✅ Quick task guides

This example provides a foundation for creating your own effective CLAUDE.md file. Adapt based on your project's specific needs and team conventions.