# Protocol Command - Deploy code safely to production

**Description**: Deploy code safely to production

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 98%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/workflow-orchestration-engine.md</delegation_target>
  <orchestration_flow>
    1. Enforce strict production safety standards
    2. Delegate to workflow orchestration engine (production mode)
    3. Execute comprehensive validation and testing
    4. Deploy with safety checks and rollback capability
  </orchestration_flow>
  <production_safety>
    <quality_gates>Strict 100% quality compliance required</quality_gates>
    <security_validation>Comprehensive security and threat assessment</security_validation>
    <rollback_ready>Atomic rollback capability for instant recovery</rollback_ready>
    <compliance_checks>Full compliance with production standards</compliance_checks>
  </production_safety>
</command_orchestration>
```

## Usage

**Production deployment:**
```
/protocol "Deploy user authentication system to production"
```

**Critical fixes:**
```
/protocol "Deploy security patch for authentication vulnerability"
```

**Resume interrupted production work:**
```
/protocol "Continue deployment of payment system"
```

## What This Command Does

- **Production safety**: Enforces strict production deployment standards
- **Quality gates**: Requires 100% quality compliance before deployment
- **Security focus**: Comprehensive security validation and threat assessment
- **Rollback ready**: Atomic rollback capability for instant recovery
- **Compliance**: Full compliance with production standards and regulations

## Examples

- `/protocol "Deploy API changes"` - Deploys with full production safety validation
- `/protocol "Hot fix critical bug"` - Deploys urgent fixes with safety checks
- `/protocol "Update production database"` - Manages database changes safely