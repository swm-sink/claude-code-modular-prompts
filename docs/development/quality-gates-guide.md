| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Quality Gates Configuration Guide

────────────────────────────────────────────────────────────────────────────────

## Overview

The Claude Code Framework implements a comprehensive quality gates system that ensures consistent, high-quality software delivery across all development activities. Quality gates are automated checkpoints that validate specific criteria before allowing progression to the next phase of development.

### What Are Quality Gates?

Quality gates are **non-bypassable validation checkpoints** that:
- Automatically enforce quality standards during development
- Block progression when quality criteria aren't met
- Provide clear feedback on what needs to be fixed
- Generate audit trails for compliance and improvement

### Key Benefits

- **Consistent Quality**: Every commit meets the same high standards
- **Early Detection**: Issues caught immediately, not in production
- **Reduced Technical Debt**: Quality built-in from the start
- **Compliance Ready**: Automated evidence collection and audit trails
- **Developer Productivity**: Clear guidance on what's required

## Quality Gate Categories

The framework organizes quality gates into five categories, each serving different aspects of software quality:

### 1. Foundational Gates
Applied to **ALL commands** - basic quality requirements that every operation must satisfy.

- **Critical Thinking Validation**: 30-second minimum analysis with documented alternatives
- **Requirement Clarity**: Clear, testable requirements with measurable success criteria  
- **Module Integration Compliance**: Proper module usage and dependency management
- **Error Handling Completeness**: Comprehensive error scenarios and recovery mechanisms

### 2. Development Gates
Applied to code modification commands (`/task`, `/swarm`, `/feature`, `/protocol`).

- **TDD Cycle Compliance**: Strict RED-GREEN-REFACTOR enforcement
- **Code Quality Standards**: Linting, complexity limits, maintainability
- **Security Requirements**: Threat modeling and vulnerability prevention
- **Performance Validation**: Response time and resource usage requirements

### 3. Coordination Gates
Applied to multi-component commands (`/swarm`, `/feature`, `/protocol`).

- **Multi-Agent Synchronization**: Clear agent boundaries and coordination protocols
- **Session Tracking Completeness**: Progress tracking and context preservation
- **Integration Validation**: End-to-end system validation

### 4. Documentation Gates
Applied to documentation commands (`/docs`) and development with documentation.

- **Documentation Standards Compliance**: Framework 3.0 format and content standards
- **TDD Methodology Documentation**: Proper TDD references and workflow examples

### 5. Analysis Gates
Applied to research commands (`/query`, `/auto` routing decisions).

- **Research Comprehensiveness**: Thorough analysis with evidence-based conclusions
- **Routing Decision Quality**: Sound complexity assessment and command selection

## Command-Specific Gate Configuration

### `/task` Command Gates

**Required Gates**: Foundational + Development  
**Enforcement**: BLOCKING

```xml
<universal_quality_gates enforcement="MANDATORY">
  <gate_set>task_command_gates</gate_set>
  <validation>Reference quality/universal-quality-gates.md#task_command_gates</validation>
  <blocking_conditions>
    <condition>TDD cycle not completed (RED-GREEN-REFACTOR)</condition>
    <condition>Test coverage below 90%</condition>
    <condition>Security threats not mitigated</condition>
    <condition>Performance requirements not met</condition>
  </blocking_conditions>
  <enforcement_sequence>
    <pre_execution>critical_thinking_validation, requirement_clarity</pre_execution>
    <during_execution>tdd_cycle_compliance, code_quality_standards</during_execution>
    <post_execution>security_requirements, performance_validation</post_execution>
  </enforcement_sequence>
</universal_quality_gates>
```

**Example Configuration**:
```bash
# .claude/commands/task.md
<tdd_integration enforcement="MANDATORY">
  <red_phase>Write failing tests BEFORE any implementation</red_phase>
  <green_phase>Minimal code to pass tests</green_phase>
  <refactor_phase>Improve design while maintaining green tests</refactor_phase>
  <coverage_requirement>90% minimum for new code</coverage_requirement>
  <blocking_condition>Implementation without tests blocks completion</blocking_condition>
</tdd_integration>
```

### `/swarm` Command Gates

**Required Gates**: Foundational + Development + Coordination  
**Enforcement**: BLOCKING

```xml
<universal_quality_gates enforcement="MANDATORY">
  <gate_set>swarm_command_gates</gate_set>
  <validation>Reference quality/universal-quality-gates.md#swarm_command_gates</validation>
  <blocking_conditions>
    <condition>Agent coordination conflicts detected</condition>
    <condition>Integration tests failing</condition>
    <condition>Session tracking incomplete</condition>
    <condition>TDD compliance violations across agents</condition>
  </blocking_conditions>
  <enforcement_sequence>
    <pre_execution>critical_thinking_validation, module_integration_compliance</pre_execution>
    <during_execution>multi_agent_synchronization, tdd_cycle_compliance</during_execution>
    <post_execution>integration_validation, session_tracking_completeness</post_execution>
  </enforcement_sequence>
</universal_quality_gates>
```

**Example Multi-Agent TDD Configuration**:
```bash
# Agent coordination with TDD
<multi_agent_tdd enforcement="MANDATORY">
  <agent_isolation>Each agent maintains independent test suites</agent_isolation>
  <coordination_tests>Integration tests validate agent interactions</coordination_tests>
  <shared_interfaces>Common interface tests prevent breaking changes</shared_interfaces>
  <blocking_condition>Any agent TDD violation blocks entire swarm</blocking_condition>
</multi_agent_tdd>
```

### `/protocol` Command Gates

**Required Gates**: ALL categories (strictest enforcement)  
**Enforcement**: BLOCKING

```xml
<universal_quality_gates enforcement="MANDATORY">
  <gate_set>protocol_command_gates</gate_set>
  <validation>Reference quality/universal-quality-gates.md#protocol_command_gates</validation>
  <blocking_conditions>
    <condition>ANY quality gate failure</condition>
    <condition>Production standards not met</condition>
    <condition>Compliance requirements violated</condition>
    <condition>Security audit findings unresolved</condition>
  </blocking_conditions>
  <enforcement_sequence>
    <pre_execution>ALL foundational gates + security threat model</pre_execution>
    <during_execution>ALL development gates + coordination gates</during_execution>
    <post_execution>ALL validation gates + compliance verification</post_execution>
  </enforcement_sequence>
</universal_quality_gates>
```

## Implementing Quality Gates in New Projects

### Step 1: Configure Core Quality Standards

Create `.claude/project-config.md`:

```markdown
# Project Quality Configuration

## TDD Standards
- **Coverage Requirement**: 90% minimum for production code
- **Test Strategy**: Unit (fast) + Integration (component) + E2E (workflow)
- **Blocking Condition**: No implementation without failing tests first

## Security Standards
- **Threat Modeling**: Required for all external interfaces
- **Vulnerability Scanning**: Zero HIGH severity issues allowed
- **Data Protection**: Encryption at rest and in transit

## Performance Standards  
- **Response Time**: p95 < 200ms for API endpoints
- **Resource Usage**: Memory < 512MB per instance
- **Load Testing**: Required for all user-facing features
```

### Step 2: Set Up TDD Workflow

Create test structure:
```bash
tests/
├── unit/           # Fast, isolated tests
├── integration/    # Component interaction tests  
├── e2e/           # End-to-end workflow tests
└── fixtures/      # Test data and mocks
```

Configure TDD enforcement:
```xml
<tdd_enforcement>
  <red_phase_validation>
    <check>Tests written before implementation</check>
    <check>Tests fail for expected reasons</check>
    <check>All acceptance criteria covered</check>
  </red_phase_validation>
  <green_phase_validation>
    <check>Minimal implementation passes tests</check>
    <check>No premature optimization</check>
    <check>Coverage thresholds met</check>
  </green_phase_validation>
  <refactor_phase_validation>
    <check>Tests remain green throughout</check>
    <check>Code quality improved</check>
    <check>No behavior changes</check>
  </refactor_phase_validation>
</tdd_enforcement>
```

### Step 3: Configure Security Gates

Create security configuration:
```xml
<security_gates>
  <threat_modeling>
    <methodology>STRIDE (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation)</methodology>
    <requirement>Threat model before external interface changes</requirement>
    <validation>Security controls mapped to identified threats</validation>
  </threat_modeling>
  <vulnerability_scanning>
    <tools>SAST, dependency scanning, secrets detection</tools>
    <blocking_threshold>Zero HIGH, max 5 MEDIUM severity issues</blocking_threshold>
    <frequency>Every commit for SAST, daily for dependencies</frequency>
  </vulnerability_scanning>
</security_gates>
```

### Step 4: Set Performance Requirements

Configure performance validation:
```xml
<performance_gates>
  <response_time_requirements>
    <api_endpoints>p50 < 100ms, p95 < 200ms, p99 < 500ms</api_endpoints>
    <web_pages>LCP < 2.5s, FID < 100ms, CLS < 0.1</web_pages>
    <background_tasks>Complete within 30s or provide progress updates</background_tasks>
  </response_time_requirements>
  <resource_requirements>
    <memory>< 512MB sustained, < 1GB peak</memory>
    <cpu>< 80% sustained under normal load</cpu>
    <database>Query timeout 30s, transaction timeout 60s</database>
  </resource_requirements>
</performance_gates>
```

## Common Gate Failures and Solutions

### TDD Violations

**Problem**: Implementation written before tests
```
❌ TDD violation: Implementation written before tests. Restarting with RED phase.
```

**Solution**:
1. Delete the implementation code
2. Write failing tests that specify the expected behavior
3. Verify tests fail for the right reasons
4. Implement minimal code to make tests pass

**Example Fix**:
```javascript
// ❌ Wrong: Implementation first
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// ✅ Correct: Tests first
describe('calculateTotal', () => {
  it('should return 0 for empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });
  
  it('should sum item prices', () => {
    const items = [{price: 10}, {price: 20}];
    expect(calculateTotal(items)).toBe(30);
  });
});

// Then implement minimal code to pass
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

### Security Gate Failures

**Problem**: Missing threat model
```
❌ Security gate failure: Threat model required for external interface changes
```

**Solution**:
1. Identify the external interfaces (APIs, file uploads, user inputs)
2. Apply STRIDE methodology to each interface
3. Document identified threats and mitigations
4. Implement security controls for each threat

**Example Threat Model**:
```markdown
## API Endpoint: POST /api/users

### Threats (STRIDE Analysis)
- **Spoofing**: Attacker impersonates legitimate user
  - *Mitigation*: JWT authentication with proper validation
- **Tampering**: Request/response modified in transit  
  - *Mitigation*: HTTPS with certificate pinning
- **Information Disclosure**: Sensitive user data exposed
  - *Mitigation*: Field-level encryption for PII
- **Denial of Service**: Endpoint overwhelmed with requests
  - *Mitigation*: Rate limiting (100 req/min per IP)
```

### Performance Gate Failures

**Problem**: Response time exceeds requirements
```
❌ Performance gate failure: p95 response time 350ms exceeds 200ms requirement
```

**Solution**:
1. Identify performance bottlenecks through profiling
2. Optimize database queries, caching, or algorithms
3. Add performance tests to prevent regression
4. Re-run benchmarks to verify improvements

**Example Performance Fix**:
```javascript
// ❌ Slow: N+1 query problem
async function getUsersWithPosts() {
  const users = await User.findAll();
  for (const user of users) {
    user.posts = await Post.findAll({ where: { userId: user.id } });
  }
  return users;
}

// ✅ Fast: Single query with joins
async function getUsersWithPosts() {
  return await User.findAll({
    include: [{ model: Post, as: 'posts' }]
  });
}

// Add performance test
test('getUsersWithPosts should complete within 100ms', async () => {
  const start = Date.now();
  await getUsersWithPosts();
  const duration = Date.now() - start;
  expect(duration).toBeLessThan(100);
});
```

### Code Quality Gate Failures

**Problem**: Complexity too high
```
❌ Code quality gate failure: Cyclomatic complexity 15 exceeds limit of 10
```

**Solution**:
1. Break large functions into smaller, focused functions
2. Extract complex conditional logic into separate functions
3. Use early returns to reduce nesting
4. Apply appropriate design patterns

**Example Refactoring**:
```javascript
// ❌ High complexity (15)
function processOrder(order) {
  if (order && order.items && order.items.length > 0) {
    if (order.customer && order.customer.isVip) {
      if (order.total > 1000) {
        // Apply VIP + large order discount
        order.discount = order.total * 0.2;
      } else if (order.total > 500) {
        // Apply VIP discount
        order.discount = order.total * 0.1;
      } else {
        // Apply small VIP discount
        order.discount = order.total * 0.05;
      }
    } else {
      if (order.total > 1000) {
        // Apply large order discount
        order.discount = order.total * 0.1;
      } else {
        order.discount = 0;
      }
    }
    
    // Calculate tax, shipping, etc.
    // ... more complex logic
  }
  return order;
}

// ✅ Lower complexity (3 per function)
function processOrder(order) {
  if (!isValidOrder(order)) return order;
  
  order.discount = calculateDiscount(order);
  order.tax = calculateTax(order);
  order.shipping = calculateShipping(order);
  
  return order;
}

function isValidOrder(order) {
  return order && order.items && order.items.length > 0;
}

function calculateDiscount(order) {
  if (order.customer?.isVip) {
    return calculateVipDiscount(order.total);
  }
  return calculateRegularDiscount(order.total);
}

function calculateVipDiscount(total) {
  if (total > 1000) return total * 0.2;
  if (total > 500) return total * 0.1;
  return total * 0.05;
}

function calculateRegularDiscount(total) {
  return total > 1000 ? total * 0.1 : 0;
}
```

## Best Practices and Recommendations

### 1. Start with TDD
Always begin with failing tests. This practice:
- Forces clear thinking about requirements
- Creates comprehensive test coverage naturally
- Prevents over-engineering
- Provides immediate feedback on design decisions

### 2. Layer Your Testing Strategy
```
E2E Tests (Few)     - Complete user workflows
Integration Tests   - Component interactions  
Unit Tests (Many)   - Individual functions
```

**Test Distribution**: 70% unit, 20% integration, 10% E2E

### 3. Security by Design
- Threat model early in development
- Use security scanning tools in CI/CD
- Apply principle of least privilege
- Encrypt sensitive data at all layers

### 4. Performance from the Start
- Set performance budgets before implementation
- Use performance tests as acceptance criteria
- Monitor real-world performance continuously
- Optimize based on actual usage patterns

### 5. Quality Gate Customization
Adjust gate criteria based on your context:

```xml
<!-- For legacy systems -->
<tdd_integration relaxed="true">
  <coverage_requirement>70% minimum (gradually increase)</coverage_requirement>
  <legacy_code_exception>Wrapper tests acceptable for legacy integration</legacy_code_exception>
</tdd_integration>

<!-- For high-security systems -->
<security_gates strict="true">
  <vulnerability_threshold>Zero HIGH, zero MEDIUM</vulnerability_threshold>
  <penetration_testing>Required for all external interfaces</penetration_testing>
  <compliance_frameworks>SOX, PCI-DSS, HIPAA</compliance_frameworks>
</security_gates>

<!-- For high-performance systems -->
<performance_gates strict="true">
  <response_time>p95 < 50ms</response_time>
  <throughput>10,000 requests/second minimum</throughput>
  <resource_efficiency>CPU < 50%, Memory < 256MB</resource_efficiency>
</performance_gates>
```

### 6. Continuous Improvement
- Monitor gate effectiveness metrics
- Adjust thresholds based on team capabilities
- Add new gates as requirements evolve
- Gather developer feedback on gate friction

### 7. Team Onboarding
- Provide quality gates training for new team members
- Create examples and templates for common scenarios
- Document project-specific customizations
- Establish clear escalation paths for gate failures

## Integration with CI/CD

### Pre-Commit Hooks
```bash
#!/bin/bash
# .git/hooks/pre-commit

# TDD Validation
echo "Validating TDD compliance..."
if ! ./scripts/validate-tdd.sh; then
  echo "❌ TDD validation failed"
  exit 1
fi

# Security Scanning
echo "Running security scans..."
if ! ./scripts/security-scan.sh; then
  echo "❌ Security scan failed"
  exit 1
fi

# Performance Tests
echo "Running performance tests..."
if ! ./scripts/performance-test.sh; then
  echo "❌ Performance tests failed"
  exit 1
fi

echo "✅ All quality gates passed"
```

### GitHub Actions Integration
```yaml
name: Quality Gates
on: [push, pull_request]

jobs:
  quality-gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: TDD Validation
        run: ./scripts/validate-tdd.sh
        
      - name: Security Scanning
        run: ./scripts/security-scan.sh
        
      - name: Performance Testing
        run: ./scripts/performance-test.sh
        
      - name: Generate Quality Report
        run: ./scripts/generate-quality-report.sh
        
      - name: Upload Evidence
        uses: actions/upload-artifact@v3
        with:
          name: quality-evidence
          path: evidence/
```

## Monitoring and Metrics

### Quality Metrics Dashboard
Track these key metrics:
- **Gate Pass Rate**: Percentage of executions passing each gate
- **Time to Resolution**: Average time to fix gate failures
- **Quality Trends**: Quality improvements over time
- **Developer Productivity**: Impact of gates on development velocity

### Example Metrics Collection
```javascript
// Quality metrics tracking
const qualityMetrics = {
  gatePassRate: {
    tdd: 0.95,
    security: 0.88,
    performance: 0.92,
    overall: 0.90
  },
  meanTimeToResolution: {
    tdd: "15 minutes",
    security: "2 hours", 
    performance: "45 minutes"
  },
  trendAnalysis: {
    qualityScore: "improving",
    defectRate: "decreasing",
    velocityImpact: "minimal"
  }
};
```

## Troubleshooting Common Issues

### Gate Bypassing Attempts
**Problem**: Developers trying to skip quality gates

**Solution**: 
- Make gates truly non-bypassable at the infrastructure level
- Provide clear guidance on fixing gate failures
- Escalate persistent bypass attempts to team leads
- Track bypass attempts for process improvement

### False Positives
**Problem**: Gates failing due to tool configuration issues

**Solution**:
- Regularly review and tune gate thresholds
- Provide easy override mechanisms with justification required
- Maintain gate configuration documentation
- Collect feedback on gate accuracy

### Performance Impact
**Problem**: Quality gates slowing down development

**Solution**:
- Optimize gate execution time (parallel execution, faster tools)
- Cache results where appropriate
- Provide fast feedback for common issues
- Balance thoroughness with speed

## Conclusion

Quality gates are essential for maintaining consistent, high-quality software delivery. By implementing the practices and configurations outlined in this guide, development teams can:

- Ensure every commit meets quality standards
- Catch issues early when they're cheaper to fix
- Build quality into the development process
- Generate audit trails for compliance
- Improve developer skills through immediate feedback

Remember: Quality gates should enhance productivity, not hinder it. Start with core gates and gradually add more sophisticated validation as your team matures.

For implementation support, refer to:
- **TDD Module**: `.claude/modules/quality/tdd.md`
- **Production Standards**: `.claude/modules/quality/production-standards.md` 
- **Universal Quality Gates**: `.claude/modules/quality/universal-quality-gates.md`
- **Framework Documentation**: `docs/framework/`

────────────────────────────────────────────────────────────────────────────────

**Quality is not an act, but a habit.** - Build it into every step of your development process.