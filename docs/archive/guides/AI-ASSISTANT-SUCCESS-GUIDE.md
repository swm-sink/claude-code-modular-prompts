# AI Assistant Success Guide

## Overview
This guide ensures any AI assistant (Claude, GPT, etc.) working on this transformation has everything needed to succeed.

## Core Understanding

### What You're Building
- **NOT** another complex framework
- **NOT** 88 confusing commands
- **IS** a 30-command scaffolding system
- **IS** research-driven with evidence requirements
- **IS** designed to help users build their own Claude Code setups

### Critical Rules
1. **No Trust in AI-Generated Content**: Everything needs web search evidence
2. **No Invented Metrics**: Never create specific numbers without data
3. **No Hallucination**: Use "I don't know" when lacking evidence
4. **Evidence Required**: Every pattern needs 3+ authoritative sources
5. **Anti-Pattern Prevention**: 48 documented patterns to avoid

## File Navigation

### Essential Files to Read First
```markdown
1. TRANSFORMATION-PLAN.md - Your roadmap
2. ANTIPATTERN-PREVENTION-GUIDE.md - What to avoid
3. COMMAND-TEMPLATE-EXAMPLE.md - How commands work
4. IMPLEMENTATION-CHECKLIST.md - Daily tasks
5. START-HERE.md - Day 1 guide
```

### Project Structure You'll Create
```
.claude-context/
├── scaffolding/          # 30 numbered commands
│   ├── 0_verify/        # Verification commands
│   ├── 1_research/      # Research commands
│   ├── 2_context/       # Context engineering
│   ├── 3_agent/         # Agent creation
│   ├── 4_command/       # Command building
│   ├── 5_integrate/     # Integration & validation
│   ├── 6_team/          # Team features
│   └── 7_maintain/      # Maintenance
├── patterns/            # Verified patterns library
├── research/            # Research templates
├── vetted-context/      # Trusted sources only
└── validation/          # VERIFY protocol tools
```

## Command Creation Guide

### Every Command Must Have
```yaml
---
name: [phase]_[category]-{action}  # Numbered format
description: Clear, specific description
usage: |
  /[command-name]
  
  Detailed usage instructions
allowed-tools: [Read, Write, WebSearch, Grep]
requires: [previous-command]  # Dependencies
produces: [output-files]      # What it creates
---

# Command content with:
1. Web search integration (for research commands)
2. Anti-pattern prevention  
3. Evidence requirements
4. VERIFY protocol steps
```

### Research Command Pattern
```markdown
## Step 1: Define Search Queries
- "[topic] best practices 2024 site:official-docs"
- "[topic] patterns github stars:>1000"
- "[topic] anti-patterns production"

## Step 2: Validate Sources (VERIFY)
- V: Validate authority
- E: Evidence required
- R: Reference multiple
- I: Integrate proven only
- F: Fact-check reality
- Y: Yield documentation

## Step 3: Handle Conflicts
When sources disagree, document both views

## Step 4: Create Output
With citations for everything
```

## Daily Workflow

### Morning Checklist
- [ ] Read TRANSFORMATION-LOG.md for context
- [ ] Check IMPLEMENTATION-CHECKLIST.md for today's tasks
- [ ] Review any blocking issues
- [ ] Plan day's priorities

### While Working
- [ ] Follow VERIFY protocol for all claims
- [ ] Update logs as you progress
- [ ] Test each command as created
- [ ] Commit with clear messages

### Evening Checklist
- [ ] Update TRANSFORMATION-LOG.md
- [ ] Mark completed tasks in checklist
- [ ] Note any blockers
- [ ] Push all changes

## Common Pitfalls to Avoid

### 1. Feature Creep
❌ DON'T: Add "nice to have" features
✅ DO: Stick to the 30 planned commands

### 2. Hallucinating Best Practices
❌ DON'T: State "It's common to..." without evidence
✅ DO: Search for evidence, cite sources

### 3. Over-Automation
❌ DON'T: Promise automation Claude Code can't do
✅ DO: Be honest about manual steps

### 4. Metric Invention
❌ DON'T: "Improves performance by 73%"
✅ DO: "May improve performance (source: [URL])"

### 5. Ignoring Conflicts
❌ DON'T: Present one view as truth
✅ DO: Document when experts disagree

## Technical Constraints

### Claude Code Limitations
- **Stateless**: No memory between sessions
- **No Dynamic Loading**: Commands are static markdown
- **Context Window**: 200k tokens maximum
- **File Operations**: Must use allowed-tools

### Git Operations
```bash
# Always work on the transformation branch
git checkout context-engineering-transformation

# Commit frequently with clear messages
git add [files]
git commit -m "feat: Add 1_research-domain command with web search"

# Push at end of each day
git push origin context-engineering-transformation
```

## Quality Standards

### Command Quality Checklist
- [ ] Follows naming convention
- [ ] YAML frontmatter valid
- [ ] Clear usage instructions
- [ ] Evidence requirements stated
- [ ] Anti-patterns documented
- [ ] Output files specified
- [ ] Dependencies listed
- [ ] Tested successfully

### Documentation Standards
- Clear, concise language
- Examples for everything
- No jargon without explanation
- Links to sources
- Honest about limitations

## Success Metrics You're Aiming For

### Quantitative
- 30 commands implemented (not 31, not 29)
- 100% have web search integration where needed
- 100% have anti-pattern prevention
- 0 hallucinated features
- 3+ sources per pattern

### Qualitative
- Commands are clear and usable
- Research produces real value
- Setup process feels thorough
- Anti-patterns actually prevented
- Users can build their own systems

## Getting Unstuck

### When You Don't Know Something
1. Check existing documentation first
2. Look at COMMAND-TEMPLATE-EXAMPLE.md
3. Use web search to find evidence
4. Document what you couldn't find
5. Use "I don't know" if needed

### When Tests Fail
1. Read error message carefully
2. Check TESTING-STRATEGY.md
3. Verify command structure
4. Test with minimal example
5. Document issue in log

### When Confused About Requirements
1. Re-read TRANSFORMATION-PLAN.md
2. Check phase objectives
3. Look at success criteria
4. Follow the numbered progression
5. Ask for clarification in log

## Resource Management

### Token Usage
- Keep commands under 800 tokens average
- Use references instead of duplication
- Compress verbose descriptions
- Test token counts regularly

### Time Management
- Week 1: Foundation (don't rush)
- Week 2-5: Steady progress on commands
- Week 6: Polish and testing
- Daily: Update logs and checklist

## Working with Agent Orchestration

### Understanding the Agent System
The transformation uses specialized AI agents to orchestrate the process:

```markdown
.claude/agents/
├── transformation-orchestrator.md  # Master coordinator
├── context-engineer.md            # Context structure specialist
├── command-builder.md             # Command generation
├── research-validator.md          # Evidence validation
├── quality-guardian.md            # Anti-pattern prevention
└── memory-keeper.md               # Decision tracking
```

### Agent Creation Pattern
When creating agents (Week 1, Day 1):
```yaml
---
name: agent-name
description: Clear purpose and specialization
tools: [Read, Write, Edit, WebSearch]  # Only needed tools
---

## Context Loading
Specify what context this agent needs:
- Primary: .claude/context/[specific-context].md
- Domain: .claude/domains/[relevant-domain]/
- Memory: .claude/memory/[tracking-file].md
```

### Agent Communication
Agents communicate through:
1. **Shared Context**: `.claude/context/` files all agents can read
2. **Memory System**: `.claude/memory/` for tracking decisions
3. **Command Invocation**: Using @ notation to delegate
4. **File Updates**: Coordinated changes to shared files

### Using Agents in Commands
Every scaffolding command should specify which agents to use:
```yaml
---
name: 1_research-framework
agents:
  research-validator: Primary research execution
  quality-guardian: Anti-pattern prevention
  memory-keeper: Decision tracking
context-loading:
  primary: .claude/context/research-protocols.md
  domain: .claude/domains/technical/framework-patterns.md
---
```

### Agent Delegation Pattern
```markdown
## Step 1: Orchestrator Initiates
@transformation-orchestrator: Begin Phase 1 research commands

## Step 2: Delegation Chain
@context-engineer: Set up research context structure
@command-builder: Create 1_research-framework.md from template
@research-validator: Add web search queries
@quality-guardian: Validate against anti-patterns
```

### Self-Building System
The agents work together to:
- Build the transformation commands themselves
- Validate quality at each step
- Track all decisions in memory
- Learn from the process
- Maintain the system post-transformation

### Agent Testing
Test each agent:
1. Can it load its required context?
2. Can it invoke its allowed tools?
3. Does it communicate with other agents?
4. Does it update memory correctly?
5. Does it prevent anti-patterns?

## Final Reminders

1. **You're building a tool to help users**, not showing off complexity
2. **Evidence beats opinion** every time
3. **Working code beats perfect documentation**
4. **30 good commands beat 88 confusing ones**
5. **Research takes time** - that's intentional
6. **Anti-patterns are learned from failure** - respect them
7. **Users will judge by results** not promises

## Success Looks Like

At the end of 6 weeks:
- ✅ 30 well-researched, evidence-based commands
- ✅ Clear progression from verification → research → building
- ✅ Users can create tailored Claude Code setups
- ✅ Every pattern traced to authoritative sources
- ✅ Anti-patterns actively prevented
- ✅ Git submodule ready for easy integration
- ✅ Comprehensive documentation
- ✅ All tests passing

## Your North Star

**Help users build evidence-based Claude Code setups for their specific projects through systematic research and verification, not AI hallucinations.**

---

Remember: The goal is transformation to something better, not just change for change's sake. Make every command count, every pattern verified, and every user successful.