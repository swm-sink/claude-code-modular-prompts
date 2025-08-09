# 14-Step Execution Template for Atomic Tasks

## Overview
This template guides the execution of each atomic task with maximum accuracy and thoroughness.

---

## Task: [Task ID and Name]
**Start Time**: [Timestamp]
**Estimated Duration**: [From decomposition]
**Dependencies**: [List any dependencies]
**Critical Path**: [Yes/No]

---

### Step 1: Exploration & Scoping
**Objective**: Define precise boundaries for this task
**Duration**: 15-30 minutes

**Questions to Answer**:
- What exactly needs to be created/modified?
- What are the inputs and outputs?
- What constraints must be respected?
- What quality criteria define success?
- What could go wrong?

**Deliverable**: Clear scope statement with boundaries

---

### Step 2: External Research
**Objective**: Search for best practices relevant to this task
**Duration**: 30-60 minutes

**Research Areas**:
- Official documentation
- Industry best practices
- Similar implementations
- Known pitfalls
- Performance considerations

**Sources to Check**:
- Claude Code documentation
- GitHub examples (stars > 1000)
- Official framework docs
- Expert blog posts (dated 2024-2025)

**Deliverable**: Research notes with citations

---

### Step 3: Initial Plan Formulation
**Objective**: Create detailed plan for task execution
**Duration**: 30-45 minutes

**Plan Components**:
- Step-by-step approach
- Technical decisions with rationale
- Risk mitigation strategies
- Success criteria
- Validation approach

**Deliverable**: Detailed implementation plan

---

### Step 4: Plan Critique
**Objective**: Adversarial review of the plan
**Duration**: 20-30 minutes

**Critique Areas**:
- What assumptions are we making?
- What could fail?
- Are we over-engineering?
- Are we under-engineering?
- What alternatives exist?
- Is this the simplest correct solution?

**Deliverable**: Critique document with concerns

---

### Step 5: Finalized Plan
**Objective**: Battle-hardened final version
**Duration**: 20-30 minutes

**Incorporation**:
- Address all critique points
- Strengthen weak areas
- Simplify complex areas
- Add missing considerations
- Lock down approach

**Deliverable**: Final implementation plan

---

### Step 6: Micro-Task Breakdown
**Objective**: Exhaustive checklist of atomic steps
**Duration**: 15-20 minutes

**Breakdown Level**:
- Each step should take 5-15 minutes
- No step should have substeps
- Each step has clear completion criteria
- Steps are sequentially dependent

**Deliverable**: Numbered checklist

---

### Step 7: Todo Critique
**Objective**: Review todo list for completeness
**Duration**: 10-15 minutes

**Review Questions**:
- Is anything missing?
- Is the order optimal?
- Are dependencies clear?
- Can any steps be combined?
- Can any steps be eliminated?

**Deliverable**: Validated todo list

---

### Step 8: Finalized Todos
**Objective**: Locked-down implementation checklist
**Duration**: 10 minutes

**Format**:
```
- [ ] 1. [Specific action with clear completion criteria]
- [ ] 2. [Next specific action]
- [ ] ...
```

**Deliverable**: Final todo checklist

---

### Step 9: Implementation
**Objective**: Execute todos precisely with logging
**Duration**: [Varies by task]

**Execution Rules**:
- Complete todos in order
- Log any deviations
- Document any discoveries
- Capture any errors
- Note any concerns

**Logging Format**:
```
[Time] Todo #X: [What was done]
[Time] Result: [What happened]
[Time] Note: [Any observations]
```

**Deliverable**: Completed implementation with logs

---

### Step 10: Initial Validation
**Objective**: Verify against success criteria
**Duration**: 20-30 minutes

**Validation Checklist**:
- [ ] All todos completed?
- [ ] Success criteria met?
- [ ] No regressions introduced?
- [ ] Documentation updated?
- [ ] Tests passing?

**Deliverable**: Validation report

---

### Step 11: Corrective Action
**Objective**: Document and perform any fixes
**Duration**: [Varies]

**If Issues Found**:
- Document the issue precisely
- Identify root cause
- Plan correction
- Execute correction
- Re-validate

**Deliverable**: Corrected implementation

---

### Step 12: Final Review
**Objective**: Holistic assessment of completed work
**Duration**: 15-20 minutes

**Review Areas**:
- Does it meet original objectives?
- Is it maintainable?
- Is it well-documented?
- Are there any code smells?
- Would another developer understand it?

**Deliverable**: Final review notes

---

### Step 13: Final Edits
**Objective**: Minor adjustments from review
**Duration**: 10-20 minutes

**Common Edits**:
- Comment improvements
- Variable naming
- Documentation updates
- Code formatting
- Error message clarity

**Deliverable**: Polished implementation

---

### Step 14: Atomic Commit
**Objective**: Git commit with detailed message
**Duration**: 10 minutes

**Commit Message Format**:
```
[Task ID] Complete [task name]

## What Changed
- [Specific file/feature added]
- [Specific modification made]

## Why
- [Business/technical reason]

## Testing
- [How it was validated]

## Notes
- [Any important context]

Task Duration: [Actual time]
Research Sources: [Key citations]
```

**Deliverable**: Committed changes

---

## Task Completion
**End Time**: [Timestamp]
**Actual Duration**: [Calculate]
**Variance**: [Actual vs Estimated]

## Lessons Learned
- What went well?
- What was challenging?
- What would you do differently?
- What knowledge should be preserved?

## Updates Needed
- [ ] Update time estimates?
- [ ] Update dependencies?
- [ ] Update future task plans?
- [ ] Update documentation?