# Protocol Command

Production-ready protocol execution with strict quality gates and atomic commits.

## Instructions

Execute production-ready workflow for: $ARGUMENTS

1. **Production Analysis**: Analyze requirements for production deployment.
   - **Atomic Checkpoint**: `git add -A && git commit -m "PROTOCOL ANALYSIS: [operation] - production requirements analyzed and validated"`
   - **Critical Validation**: Ensure all production dependencies and constraints are identified

2. **Threat Modeling**: Identify and address security considerations.
   - **Atomic Checkpoint**: `git add -A && git commit -m "PROTOCOL SECURITY: [threat_model] - security analysis complete and mitigations defined"`
   - **Security Validation**: Complete threat assessment before proceeding
   - **Emergency Rollback**: Security violations trigger immediate rollback to safe state

3. **Quality Gates**: Enforce strict quality standards and validation.
   - **Atomic Checkpoint**: `git add -A && git commit -m "PROTOCOL QUALITY: [quality_checks] - all quality gates passed"`
   - **Coverage Enforcement**: 90%+ coverage validated before commit
   - **Performance Validation**: Benchmarks met and validated before commit

4. **Testing Strategy**: Comprehensive testing including integration and security.
   - **Atomic Checkpoint**: `git add -A && git commit -m "PROTOCOL TESTING: [test_results] - comprehensive testing complete"`
   - **Integration Safety**: Full integration test suite passes before commit
   - **Security Testing**: Security tests pass before production commit

5. **Deployment Validation**: Ensure production readiness and monitoring.
   - **Final Atomic Checkpoint**: `git add -A && git commit -m "PROTOCOL VALIDATED: [operation] - production ready with monitoring enabled"`
   - **Critical Rollback**: Protocol failures trigger immediate rollback with emergency procedures

## Production Standards

- 90%+ test coverage mandatory
- Security threat modeling required
- Performance benchmarks met
- Monitoring and alerting configured
- Rollback procedures defined

## Examples

- `/protocol "Deploy new payment processing"` - Production payment system
- `/protocol "Update user authentication"` - Security-critical updates
- `/protocol "Launch new API endpoints"` - Production API deployment