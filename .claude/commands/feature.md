# Feature Command

PRD-driven autonomous feature development with comprehensive planning and atomic commits.

## Instructions

Execute feature development workflow for: $ARGUMENTS

1. **PRD Analysis**: Understand product requirements and acceptance criteria.
   - **Atomic Checkpoint**: `git add -A && git commit -m "FEATURE PLAN: [feature_name] - requirements analyzed and PRD validated"`
   - **Validation**: Ensure acceptance criteria are clearly defined before proceeding

2. **Feature Planning**: Break down feature into components and dependencies.
   - **Atomic Checkpoint**: `git add -A && git commit -m "FEATURE DESIGN: [feature_name] - components planned and dependencies mapped"`
   - **Architecture Safety**: Validate design against existing system architecture

3. **TDD Implementation**: Implement feature with test-driven development.
   - **Per-Component Atomic Checkpoints**: `git add -A && git commit -m "FEATURE IMPL: [component] - functionality added with tests"`
   - **TDD Compliance**: Each component follows RED→GREEN→REFACTOR with atomic commits
   - **Rollback Safety**: Failed components can be rolled back without affecting completed ones

4. **Integration Testing**: Ensure feature integrates properly with existing system.
   - **Atomic Checkpoint**: `git add -A && git commit -m "FEATURE INTEGRATION: [feature_name] - system integrated and tested"`
   - **Integration Validation**: Run full integration test suite before commit

5. **Quality Validation**: Comprehensive testing and production readiness.
   - **Final Atomic Checkpoint**: `git add -A && git commit -m "FEATURE VALIDATED: [feature_name] - production ready with quality gates passed"`

## Feature Development Process

- Product requirements analysis
- Technical specification creation
- Component identification and planning
- Test-driven implementation
- Integration and validation
- Production readiness assessment

## Examples

- `/feature "User profile management"` - Complete user profile feature
- `/feature "Payment processing integration"` - Payment feature development
- `/feature "Real-time notifications"` - Notification system feature