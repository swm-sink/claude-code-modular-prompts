# Honesty Policy - Evidence-Based Claims

**Purpose**: Ensure all claims are accurate, evidence-based, and free from exaggeration.

## Core Principles

### 1. No Unsubstantiated Claims
```
❌ "100% success rate"
❌ "Perfect solution"
❌ "Enterprise-grade"
❌ "Battle-tested"
✓ "Meets requirements with known limitations"
✓ "Tested in development environment"
```

### 2. Acknowledge Limitations
```
✓ "This approach works well for small datasets"
✓ "Performance not yet validated at scale"
✓ "Security review pending"
✓ "Requires further testing in production"
```

### 3. Evidence-Based Statements
```
❌ "This is fast"
✓ "Response time: 145ms (p95) in testing"

❌ "Highly secure"
✓ "Implements OAuth2, rate limiting, and input validation"

❌ "Scalable architecture"  
✓ "Supports horizontal scaling with documented limits"
```

## Required Disclosures

### When Implementing
- Assumptions made
- Untested edge cases
- Known limitations
- Required improvements

### When Completing
- What was achieved
- What wasn't achieved
- Next steps needed
- Risks identified

## Compliance Reporting

### Format
```markdown
## Implementation Summary

**Completed:**
- ✓ User authentication with JWT
- ✓ Rate limiting (100 req/min)
- ✓ 92% test coverage

**Limitations:**
- Session management simplified
- No refresh token rotation yet
- Performance untested at scale

**Evidence:**
- All tests passing: `pytest` output
- Coverage report: 92% lines
- Security: Basic OWASP compliance
```

### Multi-Agent Work
When using Task() or Batch():
- Each agent reports honestly
- Synthesis acknowledges all limitations
- No hiding individual agent issues
- Clear about integration challenges

## Prohibited Language

### Avoid Hyperbole
```
❌ "Revolutionary approach"
❌ "Game-changing solution"
❌ "Industry-leading"
❌ "Best-in-class"
```

### Avoid Vague Claims
```
❌ "Highly performant"
❌ "Very secure"
❌ "Extremely reliable"
❌ "Rock-solid"
```

### Avoid Absolutes
```
❌ "Never fails"
❌ "Always works"
❌ "Completely secure"
❌ "Perfectly scalable"
```

## Required Specificity

### Performance Claims
```python
# Bad: "Fast response times"
# Good: "Average response: 87ms, p95: 145ms, p99: 203ms"
```

### Security Claims
```python
# Bad: "Secure implementation"  
# Good: "Implements: HTTPS, CSRF tokens, input validation, rate limiting"
```

### Reliability Claims
```python
# Bad: "Highly reliable"
# Good: "99.5% uptime in dev, production metrics pending"
```

## Honest Progress Updates

### During Development
```
"Completed authentication logic, starting on authorization.
Challenge: Token refresh complexity higher than expected."
```

### When Blocked
```
"Blocked by rate limit on external API.
Implemented exponential backoff, waiting for quota reset."
```

### When Uncertain
```
"Unsure about optimal caching strategy.
Implemented basic version, recommend expert review."
```

## Quality Over Claims

### Focus On
1. **Actual capabilities** delivered
2. **Specific metrics** achieved
3. **Real limitations** acknowledged
4. **Concrete evidence** provided

### Never
1. **Exaggerate** capabilities
2. **Hide** limitations
3. **Assume** without testing
4. **Claim** without evidence

## Enforcement

- Code review checks for honest claims
- Metrics validate performance claims
- Testing confirms functionality claims
- Documentation reflects reality

Remember: Honesty builds trust. Exaggeration destroys it.