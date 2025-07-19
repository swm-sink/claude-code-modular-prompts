# Change Impact Analyzer

**Purpose**: Prevent framework degradation by analyzing all changes before implementation  
**Enforcement**: BLOCKING - Changes that fail analysis must not proceed

## Pre-Change Analysis Protocol

### 1. Functionality Impact Assessment

**Current State Analysis**
- [ ] Document all current functionality
- [ ] List all user-facing features
- [ ] Map command relationships and dependencies
- [ ] Capture current user workflows

**Post-Change Projection**
- [ ] List all functionality after change
- [ ] Identify any removed features
- [ ] Assess workflow disruptions
- [ ] Calculate user relearning requirements

**Verdict**
- [ ] NO functionality loss without superior replacement
- [ ] NO workflow disruption without clear benefit
- [ ] NO user confusion increase

### 2. Documentation Truth Verification

**Claim Validation**
- [ ] Every new feature claim has implementation file: ____________
- [ ] Every "enhanced" has concrete code changes: ____________
- [ ] Every "intelligent" has algorithm implementation: ____________
- [ ] Every "automated" has automation logic: ____________
- [ ] Every "optimized" has performance metrics: ____________

**Evidence Requirements**
- Implementation diff showing new code
- Test cases proving functionality
- Usage examples that execute successfully
- Performance benchmarks (if claiming optimization)

### 3. User Experience Impact Score

**Discoverability** (___/100)
- How easily can users find commands?
- Are related commands grouped logically?
- Is the naming convention clear?

**Ease of Use** (___/100)
- How many steps to accomplish tasks?
- Are common workflows streamlined?
- Is the syntax memorable?

**Learning Curve** (___/100)
- How much new knowledge required?
- Are patterns consistent?
- Is help readily available?

**Error Potential** (___/100)
- How likely are user mistakes?
- Are error messages helpful?
- Is recovery straightforward?

**Overall UX Score**: ___/100 (Must be ≥ 80)

### 4. Token Efficiency Analysis

**Current State**
- Total tokens: _______
- Key file tokens:
  - CLAUDE.md: _______
  - Commands total: _______
  - Modules total: _______

**Post-Change Projection**
- Total tokens: _______
- Reduction: _______ tokens (____%)
- Loading time impact: _______

**Cost-Benefit Analysis**
- Token savings percentage: ____%
- UX degradation risk: ____%
- **Worth it?** YES / NO (Must be YES if any UX risk)

### 5. Technical Debt Assessment

**Debt Created**
- [ ] False promises requiring future implementation
- [ ] Increased complexity without clear benefit
- [ ] Inconsistent patterns introduced
- [ ] Maintenance burden increased

**Debt Resolved**
- [ ] Simplified architecture
- [ ] Reduced redundancy
- [ ] Improved consistency
- [ ] Enhanced maintainability

**Net Debt Impact**: POSITIVE / NEGATIVE (Must be POSITIVE)

## BLOCKING CONDITIONS

The following conditions will BLOCK any change:

1. **Functionality Loss**
   - Any feature removal without superior replacement
   - Any workflow disruption without 2x benefit
   - Any command removal reducing capability

2. **False Claims**
   - Documentation of non-existent features
   - "Enhanced" without implementation
   - "Intelligent" without algorithms
   - "Automated" without automation

3. **UX Degradation**
   - Overall UX score < 80
   - Increased user confusion
   - Reduced discoverability
   - Higher error potential

4. **Insufficient Token Benefit**
   - Less than 20% reduction for ANY UX change
   - Less than 10% reduction for internal changes
   - No measurement provided

5. **Trust Violations**
   - Any dishonesty in documentation
   - Hiding complexity or issues
   - Overstating capabilities
   - Misleading users

## Decision Matrix

| Criteria | Score | Required | Pass? |
|----------|-------|----------|-------|
| Functionality Preserved | ___% | 100% | ☐ |
| Documentation Truthful | ___% | 100% | ☐ |
| UX Score | ___/100 | ≥80 | ☐ |
| Token Benefit | ___% | ≥20% | ☐ |
| Net Debt Impact | POS/NEG | POS | ☐ |

## FINAL DECISION

**ALL criteria must pass for change approval**

- [ ] **PROCEED** - All checks passed, change will improve framework
- [ ] **BLOCK** - Failed checks: _________________________________
- [ ] **REVISE** - Modify approach to address: ___________________

## Accountability

**Analyzer**: ________________  
**Date**: ____________________  
**Change ID**: _______________  

## Post-Change Validation

If change proceeds:
1. Verify all promised functionality works
2. Run user workflow tests
3. Measure actual token impact
4. Update system state tracking
5. Document lessons learned

---

**Remember**: This analyzer exists because we made mistakes. Use it to prevent repeating them.