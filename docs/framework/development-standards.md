| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-08   | stable |

# Development Standards: TDD & Critical Thinking

────────────────────────────────────────────────────────────────────────────────

> **Comprehensive Guide**: Test-Driven Development standards and critical thinking enforcement for quality software development.

────────────────────────────────────────────────────────────────────────────────

## Overview

This guide establishes mandatory development practices that ensure quality, prevent disasters, and maintain framework integrity through disciplined TDD and critical thinking.

**Canonical Implementations**:
- TDD Standards: `.claude/modules/quality/tdd.md`
- Critical Thinking: `.claude/modules/quality/critical-thinking.md`

## Critical Thinking Enforcement

### The Problem We're Solving

Critical thinking rules were established after a catastrophic framework refactor that created:
- **262+ duplicate files** in shadow directories
- **Contradictory claims** of simplification while adding complexity
- **Broken references** throughout the system
- **Lost critical capabilities** without understanding impact

### Core Enforcement Points

1. **THINK DEEPLY** - Minimum 30-second analysis before any action
2. **DRY PRINCIPLE** - Zero tolerance for duplication
3. **FORENSIC VERIFICATION** - Every claim must be verified with evidence

### Critical Thinking Process

Before any significant action:

```
1. ANALYZE: What are the real impacts?
2. VERIFY: What evidence supports this approach?
3. ASSESS: What could go wrong?
4. REASON: Why is this the best solution?
5. EVALUATE: How will we measure success?
```

### Historical Disaster Examples

**❌ What Went Wrong**:
- **Claim**: "Simplifying from 157 to 35 files"  
  **Reality**: Created 262 duplicate files in shadow directories

- **Claim**: "Making the framework cleaner"  
  **Reality**: Left test code scattered throughout src/

**✅ What We Do Now**:
- Mandatory pre-action analysis checklists
- DRY principle enforcement with duplication scanning
- Forensic verification protocols
- Integration with AWARE framework
- Session documentation requirements

## Test-Driven Development Standards

### Core TDD Cycle

#### 🔴 RED Phase - Test First
```
1. Write failing test that defines behavior
2. Run test and confirm it fails
3. Commit the failing test
4. NO implementation code yet
5. Update session: "RED phase - Test written"
```

#### 🟢 GREEN Phase - Minimal Pass
```
1. Write ONLY enough code to pass
2. No extra features or optimization
3. Run test and confirm it passes
4. Commit the passing code
5. Update session: "GREEN phase - Tests passing"
```

#### 🔄 REFACTOR Phase - Clean Code
```
1. Improve code structure
2. Keep all tests passing
3. No behavior changes
4. Commit improvements
5. Update session: "REFACTOR complete"
```

### Test Quality Standards

#### Coverage Requirements
- **Line Coverage**: 90% minimum
- **Branch Coverage**: 85% minimum  
- **Critical Paths**: 100% required
- **Error Handling**: 100% required

#### Test Characteristics
```python
# Good Test Example
def test_user_cannot_login_with_invalid_password():
    """Test describes expected behavior clearly"""
    # Arrange
    user = create_test_user(email="test@example.com")
    
    # Act
    result = login(email="test@example.com", password="wrong")
    
    # Assert
    assert result.status_code == 401
    assert result.error == "Invalid credentials"
    assert not result.token
```

## Development Patterns

### Feature Development
```
1. RED: Test the feature requirement
2. GREEN: Implement minimally
3. RED: Test edge case
4. GREEN: Handle edge case
5. REFACTOR: Clean up code
6. Repeat for each aspect
```

### Bug Fixing
```
1. RED: Test that reproduces bug
2. GREEN: Fix the bug minimally
3. RED: Test related edge cases
4. GREEN: Handle edge cases
5. REFACTOR: Improve solution
```

### Refactoring
```
1. Ensure tests exist and pass
2. Make small changes
3. Run tests after each change
4. Commit frequently
5. Never change behavior
```

## Multi-Agent TDD

### When Using Multiple Agents
```python
# Each agent maintains TDD discipline
Task("Frontend Dev", "Create login form with validation")
# → Writes failing component tests first
# → Updates session: "Frontend: RED phase"

Task("Backend Dev", "Create login endpoint") 
# → Writes failing API tests first
# → Updates session: "Backend: RED phase"

Task("Security Expert", "Add rate limiting")
# → Writes failing security tests first
# → Updates session: "Security: RED phase"
```

### Coordination Rules
1. Each agent completes full TDD cycle
2. Integration tests verify agent work
3. No skipping phases in any agent
4. All tests green before merge

## Anti-Patterns to Avoid

### ❌ Writing Code First
```python
# WRONG: Implementation before test
def calculate_tax(amount):
    return amount * 0.08

# Then writing test - NO!
```

### ❌ Testing Implementation
```python
# WRONG: Testing HOW not WHAT
def test_uses_multiplication():
    # Don't test internal implementation
```

### ❌ Skipping RED
```python
# WRONG: Writing passing test
def test_always_passes():
    assert True  # Useless test
```

### ❌ Surface-Level Thinking
```
# WRONG: Quick action without analysis
"This should work" → immediate implementation

# RIGHT: Deep analysis first
30-second minimum analysis → verify assumptions → then act
```

## Enforcement Mechanisms

### Automatic Checks
- Pre-commit hooks verify test coverage
- CI/CD enforces TDD evidence
- Code review checks for TDD cycle
- Metrics track TDD compliance
- Duplication scanning prevents redundancy

### Evidence Requirements
```bash
# Each PR must show:
- Commit with failing test (RED)
- Commit with minimal pass (GREEN)  
- Commit with refactoring (REFACTOR)
- All tests passing
- Coverage requirements met
- Session showing TDD cycle progress
- Critical thinking analysis documented
```

### Session Integration
```bash
# TDD phases tracked in sessions:
- RED commits linked to session
- GREEN commits show progression
- REFACTOR commits complete cycle
- Session documents TDD compliance
- Critical thinking checkpoints recorded
```

## Test Structure Standards

### Directory Organization
```bash
tests/
├── unit/           # Fast, isolated tests
├── integration/    # Component interaction tests  
├── e2e/           # End-to-end workflow tests
└── fixtures/      # Test data and mocks
```

**Test Distribution**: 70% unit, 20% integration, 10% E2E

### Naming Conventions
```python
# Test file naming
test_feature_name.py
test_component_behavior.py
test_error_handling.py

# Test method naming
def test_should_return_error_when_invalid_input():
def test_should_create_user_when_valid_data():
def test_should_prevent_duplicate_emails():
```

## Quality Metrics

### TDD Compliance Tracking
- Percentage of features developed with TDD
- Test coverage trends
- RED-GREEN-REFACTOR cycle completion rates
- Time spent in each phase

### Critical Thinking Metrics
- Pre-action analysis completion rate
- Duplication prevention success rate
- Decision reversal frequency
- Framework stability metrics

## Common Scenarios

### Adding New Features
1. **Critical Thinking**: Analyze impact on existing system
2. **RED**: Write failing acceptance tests
3. **GREEN**: Implement minimal feature
4. **RED**: Add edge case tests
5. **GREEN**: Handle edge cases
6. **REFACTOR**: Clean up and optimize

### Fixing Bugs
1. **Critical Thinking**: Understand root cause
2. **RED**: Write test that reproduces bug
3. **GREEN**: Fix the specific issue
4. **RED**: Test related scenarios
5. **GREEN**: Handle related cases
6. **REFACTOR**: Improve overall solution

### Framework Changes
1. **Critical Thinking**: MANDATORY deep analysis
2. **Impact Assessment**: What breaks? What improves?
3. **Verification**: Prove claims with evidence
4. **TDD**: Test new framework behavior
5. **Incremental**: Small, verifiable changes
6. **Documentation**: Update all affected docs

## Integration with Framework

### Command Integration
All development commands (`/task`, `/swarm`, `/feature`, `/protocol`) enforce:
- Critical thinking checkpoints
- TDD cycle compliance
- Quality gate validation
- Session documentation

### Module Integration
Development standards integrate with:
- Quality gates for enforcement
- Session management for tracking
- Error recovery for resilience
- Pattern library for consistency

## Benefits

### TDD Benefits
1. **Design**: Tests drive better design
2. **Documentation**: Tests document behavior
3. **Confidence**: Safe refactoring
4. **Quality**: Fewer bugs in production
5. **Speed**: Faster long-term development

### Critical Thinking Benefits
1. **Prevention**: Avoid catastrophic mistakes
2. **Quality**: Better decisions through analysis
3. **Efficiency**: Less rework from poor planning
4. **Learning**: Build better judgment over time
5. **Framework Integrity**: Maintain system stability

## Best Practices

### Daily Development
- Start each session with critical thinking
- Follow TDD cycle religiously
- Document decisions and reasoning
- Verify claims with evidence
- Update sessions continuously

### Code Reviews
- Verify TDD evidence in commits
- Check critical thinking documentation
- Validate test quality and coverage
- Ensure no anti-patterns present
- Confirm session tracking completeness

### Team Collaboration
- Share TDD cycle progress in standups
- Review critical thinking analyses together
- Learn from past mistakes and successes
- Maintain high standards consistently
- Support each other's development discipline

## Remember

- **TDD is not optional** - It's how we ensure quality
- **Critical thinking prevents disasters** - Every framework change affects everything
- **A moment of careless action creates hours of cleanup work**
- **The standards exist to protect the framework and team**

For detailed implementation, see:
- **TDD Module**: `.claude/modules/quality/tdd.md`
- **Critical Thinking Module**: `.claude/modules/quality/critical-thinking.md`
- **Quality Gates**: `docs/framework/quality-and-production-standards.md`

────────────────────────────────────────────────────────────────────────────────

**Excellence is a habit.** - Make TDD and critical thinking your default approach.