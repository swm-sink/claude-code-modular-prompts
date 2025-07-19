# Claim Validator (Documentation Accuracy Checker)

**Purpose**: Ensure all documentation claims have corresponding implementations  
**Enforcement**: BLOCKING - No false claims allowed in framework documentation

## Validation Protocol

### For EVERY Documentation Claim

**Step 1: Identify the Claim**
```
Claim: "______________________________________________________"
Location: [file:line number]
Type: [ ] Feature [ ] Enhancement [ ] Capability [ ] Optimization
```

**Step 2: Verify Implementation**
```
Implementation file: @.claude/_________________________________
Relevant code section: Lines _____ to _____
Test coverage file: @.claude/tests/_____________________________
Test coverage percentage: _____%
Working example: [ ] Provided [ ] Verified [ ] None
```

**Step 3: Evidence Assessment**
- [ ] Code exists and matches claim
- [ ] Tests exist and pass
- [ ] Example executes successfully
- [ ] Performance metrics support optimization claims
- [ ] No exaggeration or overselling

### Buzzword Detection & Requirements

**"Intelligent" Claims**
- **Banned unless**: Actual algorithm implementation exists
- **Required proof**: 
  - Algorithm file: ________________________
  - Decision logic: ________________________
  - Learning/adaptation mechanism: __________

**"Enhanced" Claims**
- **Banned unless**: New code added to existing functionality
- **Required proof**:
  - Before state: __________________________
  - After state: ___________________________
  - Enhancement diff: ______________________

**"Automated" Claims**
- **Banned unless**: Manual process replaced by code
- **Required proof**:
  - Manual process documentation: ___________
  - Automation implementation: ______________
  - Human intervention removed: YES / NO

**"Optimized" Claims**
- **Banned unless**: Measurable performance improvement
- **Required proof**:
  - Before metrics: ________________________
  - After metrics: _________________________
  - Improvement percentage: ____%
  - Benchmark code: ________________________

**"Smart/Adaptive/Dynamic" Claims**
- **Banned unless**: Behavior changes based on context
- **Required proof**:
  - Context detection: _____________________
  - Behavior variations: ___________________
  - Adaptation logic: ______________________

## Common False Claim Patterns

### Red Flags to Check

1. **Future Tense Disguised as Present**
   - "Enables auto-fixing" (but doesn't actually do it)
   - "Supports optimization" (but doesn't optimize)
   - "Allows for enhancement" (but isn't enhanced)

2. **Capability vs Implementation**
   - "Can be extended to..." (but isn't)
   - "Framework for..." (but no implementation)
   - "Architecture supports..." (but doesn't do)

3. **Vague Enhancements**
   - "Enhanced with" (but no new code)
   - "Improved" (but no metrics)
   - "Optimized" (but no benchmarks)

4. **Misleading Intelligence**
   - "Intelligent routing" (just if/else)
   - "Smart detection" (basic conditionals)
   - "Adaptive behavior" (static rules)

## Validation Checklist

### Documentation Review
- [ ] Read all command descriptions
- [ ] Check "What This Command Does" sections
- [ ] Review any "Capabilities" sections
- [ ] Examine "Features" or "Enhancements"

### Implementation Verification
- [ ] Locate supposed implementation files
- [ ] Verify code actually exists
- [ ] Confirm code matches claims
- [ ] Check test coverage

### Truth Scoring
```
Total claims reviewed: _____
Claims with valid implementation: _____
False or exaggerated claims: _____
Truth Score: ____% (MUST be 100%)
```

## Blocking Conditions

**IMMEDIATE BLOCK if any of:**
- Claimed feature has no implementation
- "Enhanced" with no actual enhancement
- "Intelligent" with no intelligence
- "Automated" with no automation
- "Optimized" with no optimization proof
- Any marketing language without substance

## Remediation Requirements

**If false claims found:**
1. Document in current-violations.md
2. Choose one:
   - Remove the false claim
   - Implement the claimed feature
   - Reword to "Future Enhancement"
3. Update documentation immediately
4. Add to change-history.log

## Validation Report

**Date**: _________________  
**Validator**: _____________  
**Files Reviewed**: ________

**Results**:
- [ ] PASS - All claims validated (100% truth)
- [ ] FAIL - False claims found:
  1. _____________________________________
  2. _____________________________________
  3. _____________________________________

**Actions Taken**:
_________________________________________
_________________________________________

---

**Remember**: User trust is earned through honesty. Every false claim damages that trust.