---
name: /progressive-enhance
description: Progressive enhancement system - reveals features gradually based on usage patterns
usage: "/progressive-enhance [--status|--unlock|--reset]"
allowed-tools: [Read, Write, Glob, Grep]
---

# 🎮 Progressive Enhancement System

I gradually reveal more advanced features as you use Claude Code, preventing overwhelm while ensuring you discover powerful capabilities when you need them.

## How Progressive Enhancement Works

### Starting Simple (Day 1)
You begin with essential commands only:
```
Basic Commands Available:
  /create     - Create files and components
  /test       - Run and create tests
  /help       - Get assistance
  /commit     - Commit changes
```

### Learning Your Patterns (Days 2-7)
As I observe your usage, I unlock relevant features:
```javascript
// You use /create often for components
→ Unlocks: /component, /atom, /molecule specialized commands

// You write many tests
→ Unlocks: /test-coverage, /test-watch, /mock commands

// You refactor frequently
→ Unlocks: /refactor, /extract, /rename commands
```

### Advanced Features (Week 2+)
Once you're comfortable, advanced tools appear:
```
Advanced Commands Unlocked:
  /architect   - System design tools
  /optimize    - Performance optimization
  /analyze     - Code quality analysis
  /migrate     - Large-scale refactoring
```

## The Progression System

### Level 1: Essentials (Hour 1)
```yaml
available_commands:
  - /help         # Always available
  - /create       # Basic file creation
  - /test         # Test running
  - /commit       # Version control
  - /run          # Run scripts

philosophy: "Get productive immediately"
```

### Level 2: Productivity (Day 1-3)
```yaml
unlocked_when:
  - Used basic commands 10+ times
  - Created 3+ files
  - Been active for 1+ hours

new_commands:
  - /component    # Structured creation
  - /debug        # Debugging assistance
  - /explain      # Code explanation
  - /fix          # Error fixing

philosophy: "Accelerate common tasks"
```

### Level 3: Specialization (Day 3-7)
```yaml
unlocked_when:
  - Clear usage patterns emerge
  - Specific framework detected
  - Team patterns identified

new_commands:
  - Framework-specific commands
  - Pattern-based generators
  - Team workflow commands
  - Domain-specific tools

philosophy: "Tailor to your needs"
```

### Level 4: Architecture (Week 2+)
```yaml
unlocked_when:
  - Consistent usage for 1+ week
  - Complex operations attempted
  - Architectural changes detected

new_commands:
  - /architect    # System design
  - /refactor     # Large refactoring
  - /migrate      # Migration tools
  - /scale        # Scaling assistance

philosophy: "Support growth"
```

### Level 5: Expert (Month 1+)
```yaml
unlocked_when:
  - Power user patterns
  - Custom workflow needs
  - Advanced optimizations

new_commands:
  - /meta-command  # Create commands
  - /workflow      # Custom workflows
  - /automate      # Automation tools
  - /integrate     # System integration

philosophy: "Unlimited potential"
```

## Smart Unlock Triggers

### Usage-Based Unlocking
```javascript
trackUsagePatterns() {
  // Component creation pattern
  if (count('/create component') > 5) {
    unlock('/component')
    unlock('/atom', '/molecule', '/organism')
  }
  
  // Testing focus
  if (count('/test') > 10) {
    unlock('/test-watch')
    unlock('/coverage')
    unlock('/mock')
  }
  
  // API development
  if (created('api/') > 3) {
    unlock('/endpoint')
    unlock('/swagger')
    unlock('/postman')
  }
}
```

### Context-Based Unlocking
```javascript
analyzeContext() {
  // Large team detected
  if (contributors > 5) {
    unlock('/team-sync')
    unlock('/code-review')
    unlock('/standards')
  }
  
  // Performance issues detected
  if (bundleSize > threshold) {
    unlock('/optimize')
    unlock('/bundle-analyze')
    unlock('/lazy-load')
  }
  
  // Scaling needs detected
  if (files > 500) {
    unlock('/architect')
    unlock('/modularize')
    unlock('/boundaries')
  }
}
```

### Time-Based Unlocking
```javascript
timeBasedProgression() {
  const hoursSinceStart = getHoursSinceFirstUse()
  
  if (hoursSinceStart > 1) unlock('productivity')
  if (hoursSinceStart > 24) unlock('specialization')
  if (hoursSinceStart > 168) unlock('architecture')
  if (hoursSinceStart > 720) unlock('expert')
}
```

## User Control

### Check Current Status
```bash
/progressive-enhance --status

📊 Your Progress:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Level         : 3 (Specialization)
Commands      : 24 available, 8 locked
Usage Time    : 47 hours
Patterns      : React, TypeScript, Jest
Next Unlock   : /architect (in ~3 days)

🔓 Recently Unlocked:
  /component   - 2 days ago
  /api         - 3 days ago
  /refactor    - 5 days ago

🔒 Available to Unlock:
  /optimize    - Use /analyze 3 more times
  /scale       - Reach 100+ components
  /workflow    - Create 5 custom patterns
```

### Manual Unlock (When Ready)
```bash
/progressive-enhance --unlock architect

🤔 Checking readiness...
✓ Usage time: 47 hours (required: 40)
✓ Command mastery: 85% (required: 80%)
✓ Project complexity: High

🔓 Unlocked: Architecture Commands
  /architect   - System design assistance
  /boundaries  - Module boundaries
  /deps        - Dependency analysis
  /diagram     - Architecture diagrams
```

### Reset Progression
```bash
/progressive-enhance --reset

⚠️ This will reset to Level 1 (Essentials)
Are you sure? [y/N]: n
Cancelled.
```

## Smart Suggestions

### Contextual Discovery
When you need something, I suggest it:
```
You: "How do I optimize this bundle?"
Claude: "I notice you're concerned about performance. 
        Would you like me to unlock /optimize and 
        /bundle-analyze commands? They're perfect for this."
```

### Pattern Recognition
When I see repeated actions:
```
Notice: You've manually created 5 similar API endpoints.
Suggestion: Unlock /endpoint command to automate this?
           It follows your exact patterns.
```

### Just-In-Time Learning
Right when you need it:
```
Detected: Large refactoring in progress
Offering: /refactor command can help
          - Safely rename across files
          - Extract shared logic
          - Update imports automatically
Unlock now? [Y/n]
```

## Benefits of Progressive Enhancement

### For Beginners
- Not overwhelmed by 100+ commands
- Learn gradually at their pace
- Discover features when needed
- Build confidence step by step

### For Experts
- Quick access to basics
- Advanced features when ready
- Can unlock manually if needed
- Customizable progression

### For Teams
- Consistent onboarding experience
- New members start simple
- Advanced users get power tools
- Knowledge sharing through progression

## The Philosophy

### Start Where You Are
- No prerequisites
- No mandatory learning
- No feature overload
- Just what you need now

### Grow As You Go
- Features appear when relevant
- Complexity matches expertise
- Learning is integrated
- Progress is natural

### Never Overwhelming
- Cognitive load managed
- Gradual revelation
- Contextual introduction
- Always optional

## Example Progression Story

### Day 1: Sarah Joins Team
```
Available: /help, /create, /test, /commit
Sarah creates her first component with /create
```

### Day 3: Patterns Emerge
```
Unlocked: /component (noticed React usage)
Sarah now creates components faster
```

### Week 2: Comfort Growing
```
Unlocked: /refactor, /analyze
Sarah starts improving existing code
```

### Month 1: Full Productivity
```
Unlocked: /architect, /optimize
Sarah is now designing new features
```

### Month 3: Expert Level
```
Unlocked: /meta-command
Sarah creates team-specific commands
```

## The Result

A personalized journey where:
- Features match your needs
- Complexity matches your expertise
- Discovery feels natural
- Growth is supported

**You're never overwhelmed, never limited, always progressing.**