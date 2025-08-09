# Context Restructuring Plan: Holistic AI Context Management

## 🎯 Vision: Optimized Context Architecture

Transform from monolithic CLAUDE.md (2009 lines) to a hierarchical, progressive disclosure system optimized for AI consumption and human maintainability.

## 📊 Current vs Proposed Structure

### Current Problems:
- **2009 lines** in single file (token inefficient)
- **No hierarchy** - everything marked CRITICAL
- **Mixed concerns** - vision, tools, debugging together
- **Reactive patches** - sections added as problems arose
- **Poor discoverability** - information buried
- **Duplication** - repeated concepts
- **No progression** - all loaded at once

### Proposed Solution:
```
.claude/
├── CONTEXT.md                    # 100 lines - Essential context only
├── context/
│   ├── 00-quickstart.md         # 50 lines - Immediate orientation
│   ├── 01-architecture.md       # 150 lines - System design
│   ├── 02-workflow.md           # 100 lines - How to work
│   ├── 03-tools.md              # 100 lines - Tool usage
│   ├── 04-troubleshooting.md   # 200 lines - Problem solving
│   ├── 05-antipatterns.md      # 150 lines - What to avoid
│   ├── 06-success-criteria.md  # 100 lines - Definition of done
│   └── 99-reference.md         # 200 lines - Detailed reference
├── session/
│   ├── state.json               # Current session state
│   ├── checkpoint.md            # Progress checkpoint
│   └── handoff.md               # Session transition notes
└── project/
    ├── vision.md                # 50 lines - Project vision
    ├── status.md                # 50 lines - Current status
    └── roadmap.md               # 100 lines - Future direction
```

## 🔄 Implementation Plan

### Phase 1: Information Audit & Categorization
**Objective**: Understand what we have and where it belongs

1. **Extract all directives** from current CLAUDE.md
2. **Categorize by purpose**:
   - Behavioral rules
   - Tool instructions
   - Project specifics
   - Troubleshooting
   - Anti-patterns
   - Success criteria

3. **Identify duplications** and consolidate
4. **Rank by priority** (P0-P3)

### Phase 2: Create New Structure
**Objective**: Build the new context architecture

1. **Create CONTEXT.md** (Essential only):
```markdown
# Claude Context - Essential Information

## 🎯 Project Vision (10 lines)
30-60 minute deep discovery → project-specific commands

## 🏗️ Architecture (10 lines)
- .claude/commands/ = Frontend (user interface)
- .claude-architect/ = Backend (processing logic)
- Integration required for functionality

## ⚠️ Critical Rules (20 lines)
1. Test functionality before claiming complete
2. Integrate, don't duplicate
3. Structure ≠ Functionality
4. Ask when confused

## 📍 Current State (10 lines)
- Phase: 6 of 8
- Status: Integration needed
- Next: Wire commands to backend

## 🔗 Deep Dive
- Architecture: context/01-architecture.md
- Workflow: context/02-workflow.md
- Troubleshooting: context/04-troubleshooting.md

[50 lines total - under 500 tokens]
```

2. **Create context/ hierarchy**:
   - Each file focused on ONE concern
   - Progressive numbering for priority
   - Clear headers and navigation

3. **Implement cross-references**:
   - Link between related concepts
   - Avoid duplication
   - Use "See also" sections

### Phase 3: Behavioral Engineering Layer
**Objective**: Maintain enforcement while improving clarity

Create **context/00-behavioral-rules.md**:
```markdown
# Behavioral Rules - Start Here

## 🛑 Stop Conditions
When to stop and ask for clarification:
1. Conflicting information
2. Can't find expected directories
3. Integration path unclear

## ✅ Always Do
1. Verify directories exist: `ls -la .claude*`
2. Test before claiming complete
3. Check backend before creating new

## ❌ Never Do
1. Create plans instead of implementation
2. Update status without testing
3. Build parallel systems

## 🔄 Decision Tree
├── Need new feature?
│   ├── Check backend first
│   ├── Found? → Integrate it
│   └── Not found? → Ask before creating
└── Updating status?
    ├── Test functionality
    ├── Works? → Update with evidence
    └── Doesn't work? → Fix first
```

### Phase 4: Progressive Disclosure System
**Objective**: Load information as needed

1. **Implement loading strategy**:
```python
# Pseudo-code for context loading
def load_context(task_type):
    contexts = ["CONTEXT.md"]  # Always load
    
    if task_type == "troubleshooting":
        contexts.append("context/04-troubleshooting.md")
        contexts.append("context/05-antipatterns.md")
    elif task_type == "implementation":
        contexts.append("context/02-workflow.md")
        contexts.append("context/06-success-criteria.md")
    elif task_type == "new_session":
        contexts.append("context/00-quickstart.md")
        contexts.append("session/state.json")
    
    return contexts
```

2. **Create context triggers**:
```markdown
# In CONTEXT.md
## Context Loading Triggers
- 🔧 Implementing? Load: workflow.md, success-criteria.md
- 🐛 Debugging? Load: troubleshooting.md, antipatterns.md
- 🆕 New session? Load: quickstart.md, state.json
- 🏗️ Architecture questions? Load: architecture.md
```

### Phase 5: State Management System
**Objective**: Maintain continuity across sessions

Create **session/state.json**:
```json
{
  "session_id": "2024-12-19-001",
  "workspace": "lisbon",
  "current_phase": 6,
  "last_action": "Updated CLAUDE.md with antipatterns",
  "next_priority": "Wire /discover-project to backend",
  "blockers": [],
  "verified_functionality": {
    "deep-discovery": false,
    "discover-project": false,
    "generate-commands": false
  },
  "integration_status": {
    "discover-project": {
      "reads_backend": false,
      "uses_templates": false,
      "saves_to_backend": false
    }
  }
}
```

### Phase 6: Quality Gates
**Objective**: Ensure context effectiveness

1. **Token efficiency test**:
   - Essential context < 500 tokens
   - Full context < 5000 tokens
   - Measure and optimize

2. **Discoverability test**:
   - Can find any information in < 3 hops
   - Clear navigation paths
   - Effective search terms

3. **Effectiveness test**:
   - New session startup < 2 minutes
   - Problem resolution improved
   - Fewer clarification requests

## 📊 Migration Strategy

### Step 1: Backup Current State
```bash
cp CLAUDE.md CLAUDE.md.backup-$(date +%Y%m%d)
```

### Step 2: Extract and Categorize
- Pull out each section
- Categorize by new structure
- Remove duplications

### Step 3: Create New Files
- Start with CONTEXT.md (essential only)
- Build context/ hierarchy
- Implement session management

### Step 4: Test New Structure
- Load only CONTEXT.md
- Verify can navigate to details
- Test progressive disclosure

### Step 5: Validate Effectiveness
- New session onboarding time
- Task completion accuracy
- Reduced confusion/questions

## 🎯 Success Metrics

### Quantitative:
- **Token reduction**: 2009 → <500 (essential)
- **Load time**: Instant for essential context
- **Navigation**: Any info in <3 clicks
- **Duplication**: 0% repeated content

### Qualitative:
- **Clarity**: Immediate understanding of project state
- **Discoverability**: Easy to find information
- **Maintainability**: Simple to update
- **Effectiveness**: Fewer AI confusion moments

## 📅 Implementation Timeline

### Day 1: Analysis & Planning
- Audit current CLAUDE.md
- Categorize all content
- Design new structure

### Day 2: Build Core
- Create CONTEXT.md
- Build context/ hierarchy
- Implement cross-references

### Day 3: Session Management
- Create session/ structure
- Implement state management
- Build handoff protocols

### Day 4: Testing & Validation
- Test new structure
- Measure effectiveness
- Optimize token usage

### Day 5: Migration & Documentation
- Migrate to new structure
- Update references
- Document new system

## 🚨 Risk Mitigation

### Risk 1: Information Loss
**Mitigation**: Keep backup, validate all content migrated

### Risk 2: Broken References
**Mitigation**: Systematic update of all links

### Risk 3: Reduced Effectiveness
**Mitigation**: A/B test with current structure

### Risk 4: Session Continuity
**Mitigation**: Careful state management design

## 📝 Post-Implementation

### Monitoring:
- Track clarification requests
- Measure task completion time
- Monitor token usage
- Gather feedback

### Continuous Improvement:
- Weekly context optimization
- Monthly structure review
- Quarterly major updates

---

## Summary

This restructuring will transform our monolithic 2009-line CLAUDE.md into a hierarchical, progressive disclosure system that:

1. **Reduces cognitive load** - Essential info only at start
2. **Improves discoverability** - Clear navigation paths
3. **Optimizes tokens** - 75% reduction in initial load
4. **Maintains enforcement** - Behavioral rules preserved
5. **Enables continuity** - Session state management
6. **Supports scaling** - Modular, extensible structure

The new structure follows all 50 best practices identified, creating a context management system optimized for both AI consumption and human maintenance.