---
name: /onboard-team
description: Team-focused setup ensuring consistency across all developers
usage: "/onboard-team [--size small|medium|large]"
allowed-tools: [Read, Glob, Grep, LS, Write, MultiEdit, Bash]
---

# 👥 Team Onboarding - Consistency Across Your Entire Team

Configure Claude Code with team-wide standards, shared conventions, and collaborative workflows. This ensures every developer on your team gets the same Claude experience with consistent code generation.

## Team Size Detection

I'll auto-detect your team size from:
- Git contributors count
- Commit frequency patterns  
- Branch naming conventions
- PR/MR workflow complexity
- Directory ownership patterns

Or specify directly:
- **--size small** (1-5 developers)
- **--size medium** (5-20 developers)
- **--size large** (20+ developers)

## What Gets Configured

### 1. Shared Team Configuration
```yaml
# Created in git-tracked CLAUDE.md
team_config:
  name: "Your Team Name"
  size: "auto-detected"
  conventions:
    - Component naming patterns
    - File organization rules
    - Import conventions
    - Testing requirements
  workflows:
    - PR review process
    - Branch naming
    - Commit format
    - Release process
```

### 2. Team-Specific Commands

#### For Small Teams (1-5 devs)
Simple, direct collaboration:
- `/review` - Quick code review helper
- `/sync` - Sync with team conventions
- `/document` - Consistent documentation

#### For Medium Teams (5-20 devs)
Structured coordination:
- `/feature` - Feature branch workflow
- `/review-checklist` - Standardized reviews
- `/team-component` - Shared components
- `/api-contract` - API consistency
- `/migrate` - Database migrations

#### For Large Teams (20+ devs)
Enterprise coordination:
- `/module-owner` - Ownership assignment
- `/cross-team` - Cross-team integration
- `/architecture-review` - ADR creation
- `/breaking-change` - Impact analysis
- `/deprecate` - Deprecation workflow

### 3. Convention Extraction

I analyze your codebase to extract:

```javascript
// From actual code patterns:
teamConventions = {
  components: {
    location: "src/components/",
    naming: "PascalCase",
    structure: "atomic|domain|feature",
    testing: "colocated|separate",
    storybook: true|false
  },
  
  imports: {
    style: "absolute|relative",
    aliases: {"@": "src/"},
    ordering: "builtin|external|internal|parent|sibling"
  },
  
  api: {
    style: "REST|GraphQL|gRPC",
    versioning: "url|header|none",
    authentication: "JWT|OAuth|Basic",
    errorFormat: "standard format detected"
  },
  
  testing: {
    framework: "jest|mocha|pytest",
    coverage: "80%|required|optional",
    structure: "__tests__|*.test.ts|spec/",
    required: "pre-commit|pre-push|PR"
  }
}
```

### 4. Workflow Enforcement

Based on your git history:
- **Branch patterns**: feature/*, bugfix/*, hotfix/*
- **Commit format**: Conventional, Jira-linked, or custom
- **Review requirements**: Approvals needed, required checks
- **Merge strategy**: Squash, rebase, or merge commits

### 5. Knowledge Sharing System

```markdown
# Team Knowledge Base (auto-generated)
.claude/
├── team/
│   ├── conventions.md      # Extracted patterns
│   ├── architecture.md     # System design
│   ├── decisions/          # ADRs
│   ├── patterns/           # Code patterns
│   └── onboarding.md       # New dev guide
```

## Smart Team Detection

### Analyzing Collaboration Patterns
```javascript
detectTeamDynamics() {
  // Commit patterns
  const commitFrequency = analyzeCommitRate()
  const activeContributors = countActiveDevs(30) // Last 30 days
  
  // Code ownership
  const codeOwners = parseCodeOwners()
  const moduleOwnership = analyzeDirectoryOwnership()
  
  // Review patterns
  const prReviewers = extractReviewPatterns()
  const reviewTurnaround = calculateReviewSpeed()
  
  // Communication style
  const prDescriptions = analyzePRDescriptions()
  const commitMessages = analyzeCommitDetail()
  
  return synthesizeTeamProfile()
}
```

### Team Profiles

#### Startup Team Profile
- Rapid iteration
- Flexible conventions
- Direct communication
- Shared ownership

Generated commands focus on speed:
- `/prototype` - Quick experiments
- `/pivot` - Refactoring helpers
- `/ship` - Fast deployment

#### Enterprise Team Profile
- Strict conventions
- Detailed documentation
- Formal reviews
- Clear ownership

Generated commands focus on process:
- `/rfc` - Request for comments
- `/compliance` - Compliance checks
- `/audit` - Audit trails

#### Open Source Profile
- Contributor-friendly
- Extensive documentation
- Clear guidelines
- Public communication

Generated commands focus on collaboration:
- `/contribute` - Contribution helper
- `/issue` - Issue templates
- `/release` - Release management

## Example Team Onboarding

```bash
$ /onboard-team

👥 Team Analysis Starting...

🔍 Analyzing Team Dynamics... (15s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contributors : 8 active (last 30 days)
Team Size    : Medium (5-20 developers)
Code Style   : Highly consistent (92% similarity)
Review Style : Thorough (avg 3.2 comments/PR)
Workflow     : GitFlow with PR reviews
Conventions  : Strong, well-established

📊 Extracted Conventions... (10s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Components: Atomic design pattern
✓ Testing: Required (87% coverage)
✓ Commits: Conventional with JIRA-XXX
✓ Reviews: 2 approvals required
✓ Imports: Absolute with @ alias
✓ API: RESTful with versioning

🤝 Team Configuration... (5s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
? Team name: Engineering Team
? Enforce conventions strictly? [Y/n]: Y
? Share configuration via git? [Y/n]: Y

🚀 Generating Team Setup... (10s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Created: team-CLAUDE.md (git-tracked)
✓ Generated: 18 team commands
✓ Configured: Review workflows
✓ Enabled: Convention enforcement
✓ Setup: Knowledge sharing system

✨ Team Setup Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Shared commands for your team:
  /feature user-auth  → Creates feature/user-auth branch
  /component Button   → Follows team patterns exactly
  /review            → Uses team checklist
  /api users         → Matches your API style
  /test             → Runs team test suite

Git-tracked configuration:
  CLAUDE.md          → Team conventions (commit this)
  .claude/team/      → Shared knowledge base

Next: Commit CLAUDE.md and have team run:
  git pull && /sync-team
```

## Team Synchronization

After initial setup, team members can:

### Join the Team Setup
```bash
/sync-team
# Pulls latest CLAUDE.md
# Updates local commands
# Syncs conventions
```

### Update Team Config
```bash
/team-update
# Propose convention changes
# Update shared commands
# Document decisions
```

### Check Compliance
```bash
/team-check
# Verify following conventions
# Flag deviations
# Suggest corrections
```

## Benefits

### Consistency
- Everyone generates the same patterns
- Reduces review friction
- Maintains codebase coherence

### Onboarding
- New developers productive immediately
- Conventions are enforced automatically
- Knowledge is embedded in commands

### Evolution
- Conventions evolve with your code
- Team decides changes together
- History is preserved

## The Team Promise

**One setup. Whole team aligned. Conventions enforced.**

Your team's way becomes Claude's way. For everyone.