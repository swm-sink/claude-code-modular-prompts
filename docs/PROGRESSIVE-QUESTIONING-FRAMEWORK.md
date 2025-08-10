# Progressive Questioning Framework for Claude Code Commands

## Overview

This framework defines how Claude Code commands should ask clarifying questions - minimizing friction while ensuring accuracy. Commands should make intelligent assumptions when possible and only ask questions when truly necessary.

## Core Philosophy

**The 80/20 Rule**: Make intelligent assumptions for 80% of cases, ask questions for the 20% that matter.

## Question Decision Tree

```
START
  ↓
Can I detect this automatically?
  ├─ YES → Use detected value (mention it)
  └─ NO ↓
     Is there a sensible default?
       ├─ YES → Use default (state assumption)
       └─ NO ↓
          Is this high-risk/irreversible?
            ├─ YES → MUST ASK
            └─ NO ↓
               Are there multiple valid approaches?
                 ├─ YES → Ask preference
                 └─ NO → Make best guess
```

## Progressive Disclosure Levels

### Level 0: Silent Detection (No Questions)
**When**: Information is detectable from project files
**How**: Scan and use detected values
**Example**: Framework detection from package.json

```markdown
I detected you're using React with TypeScript. I'll follow those patterns.
```

### Level 1: Stated Assumptions (No Questions)
**When**: Strong conventions exist
**How**: Use defaults and state them clearly
**Example**: Test framework selection

```markdown
I'll use Jest for testing (detected in your package.json).
```

### Level 2: Quick Confirmation (1 Question)
**When**: Multiple reasonable options exist
**How**: Present detected option with easy override
**Example**: Component style preference

```markdown
I'll create a functional component with hooks (your project standard).
→ Different approach needed? Just let me know.
```

### Level 3: Essential Clarification (1-2 Questions)
**When**: Core requirement is ambiguous
**How**: Ask only what's necessary for success
**Example**: Feature scope

```markdown
Quick clarification on the authentication flow:
- Should this support social logins or just email/password?
(I'll handle the rest based on your existing patterns)
```

### Level 4: Guided Exploration (3-5 Questions)
**When**: Complex task with many unknowns
**How**: Progressive questions based on previous answers
**Example**: New project setup

```markdown
Let me understand your project needs:

1. What's the primary purpose? (API/Web app/CLI tool/Library)
   
[Based on answer 1]
2. Who's the target audience? (Internal/Public/Enterprise)

[Based on answers 1-2]  
3. Any specific requirements? (Performance/Security/Scale)

I'll make smart choices for everything else.
```

## Question Templates by Context

### For Code Generation

```markdown
# Minimal Friction (Preferred)
"I'll create a [detected pattern] component. Let me know if you need something different."

# When Ambiguous
"Should this be a [Option A] or [Option B]? 
- Option A: [quick description]
- Option B: [quick description]"

# When Critical
"This will [impact description]. Should I proceed?"
```

### For Refactoring

```markdown
# Safe Changes
"I'll refactor this following your existing patterns."

# Breaking Changes
"This refactoring will affect [X] other files. Continue?"

# Strategy Choice
"Would you prefer:
1. Incremental refactoring (safer, slower)
2. Complete rewrite (cleaner, riskier)"
```

### For Testing

```markdown
# Auto-Detection
"I'll generate tests using [detected framework]."

# Coverage Question
"Basic tests (happy paths) or comprehensive (edge cases too)?"

# Integration Scope
"Should these tests mock external services or use real connections?"
```

### For Analysis

```markdown
# Depth Selection
"Quick overview or detailed analysis?"

# Focus Area
"Any specific concerns? (performance/security/maintainability)"

# Output Format
"Results in terminal or save to file?"
```

## Intelligent Assumption Guidelines

### Always Assume When:
- File naming conventions are consistent
- Code style is uniform across project
- Framework conventions are standard
- Changes are easily reversible
- Risk is low

### Always Ask When:
- Making breaking changes
- Deleting files or data
- Changing security settings
- Modifying production configs
- Affecting multiple systems

### Smart Defaults by Project Type

```yaml
web_app:
  test_framework: "jest"
  component_style: "functional"
  state_management: "hooks/context"
  styling: "css-modules or styled-components"

api:
  test_framework: "jest or mocha"
  architecture: "REST unless GraphQL detected"
  auth: "JWT unless OAuth detected"
  database: "PostgreSQL unless otherwise detected"

cli_tool:
  argument_parsing: "commander or yargs"
  config: "json or yaml"
  output: "console unless --json flag"
```

## Conversation Flow Patterns

### Pattern 1: Zero-Friction Start
```markdown
I'll help you [action]. Based on your project structure, I'll [approach].

[Start working immediately]

*Making these assumptions:*
- [Assumption 1]
- [Assumption 2]
```

### Pattern 2: Single Clarification
```markdown
I need one quick clarification:

**[Specific question]**
- Option A: [Common choice]
- Option B: [Alternative]

Or describe what you need.
```

### Pattern 3: Progressive Detail
```markdown
Let's start simple:

**Main goal?** [User provides answer]

Based on that, I should also ask:
**[Follow-up question relevant to answer]**

That's all I need. I'll handle the rest.
```

### Pattern 4: Complexity Warning
```markdown
This looks like a complex task that could go several ways.

**Quick assessment:**
- Files affected: ~[number]
- Risk level: [low/medium/high]
- Time estimate: [estimate]

**How deep should I go?**
1. Quick solution (5 min)
2. Thorough approach (15 min)
3. Comprehensive overhaul (30+ min)
```

## Anti-Patterns to Avoid

### ❌ The Spanish Inquisition
```markdown
BAD: "What framework? What version? Test framework? Linting rules? 
      Code style? Documentation format? Deployment target?"
```

### ❌ The False Choice
```markdown
BAD: "Do you want good code or fast code?"
(These aren't mutually exclusive)
```

### ❌ The Academic Survey
```markdown
BAD: "On a scale of 1-10, how important is performance?
      How about maintainability? Scalability?"
```

### ❌ The Overwhelming Options
```markdown
BAD: "Choose from these 15 different approaches..."
```

## Implementation Examples

### Example 1: Simple Task (No Questions)
```markdown
/build user-avatar-component

I'll create a React component for user avatars using your existing pattern.

*Creating with:*
- TypeScript (detected)
- Styled-components (your standard)
- Tests with Jest/React Testing Library

[Proceeds immediately]
```

### Example 2: Medium Task (1 Question)
```markdown
/refactor authentication-logic

I found authentication code in 3 files. 

**Should I:**
1. Extract to a custom hook (recommended)
2. Create a context provider
3. Leave as separate utilities

*Either way, I'll maintain backward compatibility.*
```

### Example 3: Complex Task (Progressive Questions)
```markdown
/start

Let me set up Claude Code for your project.

**I detected a Node.js API. Is this correct?**
> Yes

**Great! What's the main purpose?**
> E-commerce backend

**Perfect. One more thing - team size?**
> Just me for now

Got it! I'll create a streamlined setup optimized for solo development 
with e-commerce patterns. 

[Proceeds with appropriate configuration]
```

## Metrics for Success

### Good Question Metrics:
- Average questions per command: < 1.5
- Question relevance: > 90%
- Default accuracy: > 80%
- User override rate: < 20%

### Bad Question Indicators:
- Asking for detectable information
- Multiple questions when one would suffice
- Questions about preferences that don't matter
- Asking the same thing repeatedly

## Testing Progressive Questions

### Test Scenarios:
1. **New user, simple task**: Should work with zero questions
2. **New user, complex task**: Should ask 1-2 essential questions
3. **Experienced user, any task**: Should detect patterns and skip questions
4. **Ambiguous request**: Should ask most important clarification only
5. **High-risk operation**: Should always confirm

### Validation Checklist:
- [ ] Can this be detected? Don't ask.
- [ ] Is there a sensible default? Use it.
- [ ] Will the user care? If not, don't ask.
- [ ] Is it reversible? Proceed with assumption.
- [ ] Multiple valid approaches? Quick preference check.

## Conclusion

The best question is the one you don't have to ask. This framework ensures Claude Code commands are intelligent, efficient, and respectful of user time while maintaining safety and accuracy where it matters most.