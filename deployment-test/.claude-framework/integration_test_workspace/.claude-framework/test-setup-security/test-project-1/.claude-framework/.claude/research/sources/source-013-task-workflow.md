# Source #13: Claude Task Workflow

### Metadata
- **URL**: https://gist.github.com/mtimbs/db987628c5b3d39f23d5d4b01241ef7b
- **Author/Organization**: mtimbs (Community)
- **Date**: 2025 (Current)
- **Type**: Community/Workflow

### Verification Status
- ✅ Complete task workflow
- ✅ Git integration patterns
- ✅ Quality gate implementation
- ✅ Incremental development
- ✅ Autonomous execution design

### Rating: 5/5

### Key Patterns Observed

1. **Isolated Development Pattern**:
   ```bash
   git worktree add ".trees/worktree-${ISSUE_ID}" -b "feature/${ISSUE_ID}"
   ```
   - Separate worktree per issue
   - Clean environment isolation
   - Parallel development support

2. **Incremental Milestone Structure**:
   ```
   Milestone 1: Setup & Types
   Milestone 2: Core Logic
   Milestone 3: Testing
   Milestone 4: Polish & Validation
   ```

3. **Quality Gates at Each Stage**:
   ```bash
   npm run lint
   npm run typecheck
   npm run test:unit
   npm run build
   ```

### Code Examples

```markdown
# Issue Template
## Requirements
- High-level description
- Success criteria
- Technical constraints

## Complexity: [0-15 points]
- 0-4: Simple (1-2 hours)
- 5-9: Medium (2-6 hours)  
- 10+: Complex (break into sub-issues)

## Implementation Plan
1. [Specific technical steps]
2. [Quality checks]
3. [Validation criteria]
```

### Insights & Innovations

- Complexity scoring matrix
- Autonomous execution capability
- Structured milestone progression
- Integrated quality validation
- Comprehensive error handling

### Practical Applications

- Feature development workflow
- Bug fix process
- Refactoring projects
- Team collaboration
- CI/CD integration

### Unique Features

- Worktree-based isolation
- Milestone-driven progress
- Built-in quality enforcement
- Clear complexity assessment
- Documentation-first approach