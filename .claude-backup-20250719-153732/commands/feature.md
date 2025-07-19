# Feature Command - Build a complete feature from requirements

**Description**: Build a complete feature from requirements

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/workflow-orchestration-engine.md</delegation_target>
  <orchestration_flow>
    1. Generate Product Requirements Document (PRD)
    2. Delegate to workflow orchestration engine
    3. Coordinate multi-component development
    4. Enforce quality gates and integration testing
    5. Validate production readiness
  </orchestration_flow>
  <feature_lifecycle>
    <planning>PRD generation with acceptance criteria</planning>
    <development>Multi-component TDD development</development>
    <integration>System integration and testing</integration>
    <validation>Quality assurance and production readiness</validation>
  </feature_lifecycle>
</command_orchestration>
```

## Usage

**Complete feature development:**
```
/feature "User profile management system"
```

**Multi-component feature:**
```
/feature "Real-time notification system with email and SMS"
```

**Feature with complex requirements:**
```
/feature "Payment processing with multiple payment methods"
```

## What This Command Does

- **PRD-driven**: Creates comprehensive Product Requirements Document first
- **Multi-component**: Handles features spanning multiple files and systems
- **Quality gates**: Ensures comprehensive testing and production standards
- **Integration focus**: Coordinates component interactions and dependencies
- **Production ready**: Validates deployment readiness and system integration

## Examples

- `/feature "User authentication system"` - Creates complete auth system with login, registration, and security
- `/feature "Shopping cart functionality"` - Develops cart with add/remove items, persistence, and checkout
- `/feature "Admin dashboard"` - Builds comprehensive admin interface with user management and analytics