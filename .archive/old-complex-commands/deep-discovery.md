---
name: deep-discovery
description: Master orchestrator for complete 30-60 minute deep discovery consultation system
usage: "deep-discovery [start|resume|status|phases]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: deep-discovery
version: "1.0"
---

# Deep Discovery Master Orchestrator

## Purpose: Comprehensive 30-60 Minute Consultation Experience

The `/deep-discovery` command serves as the master orchestrator for Claude Context Architect's complete deep discovery consultation system. Unlike failed 30-second "smart onboarding" approaches, this command manages a thorough 30-60 minute journey that produces genuine project intelligence and specialized context.

**Core Philosophy**: Depth over speed, quality over convenience, genuine intelligence over superficial automation.

## Depth vs Speed: Why 30 Seconds Failed

**❌ Failed 30-Second Approach**:
- Zero meaningful questions asked
- Generic template copying
- No project understanding
- Superficial placeholder replacement
- No validation of effectiveness

**✅ Our 30-60 Minute Approach**:
- Deep repository analysis (15-20 minutes)
- Interactive consultation with smart questions (20-30 minutes)
- Context generation with validation (10-15 minutes)
- User approval at every critical decision point
- Session management with pause/resume capability

## Complete Process Overview

### Phase 1: Foundation & Research (15-20 minutes)
```
/deep-discovery start
├── `/discover-project` - Deep project DNA extraction (INTEGRATED)
│   └── Uses .claude-architect/research/ backend components
├── Framework detection and validation
├── `/research-patterns` - Web research of 20+ similar projects
├── Technology stack deep analysis
└── Initial pattern database creation → PROJECT-DNA.md
```

### Phase 2: Interactive Consultation (20-30 minutes)
```
/consult-interactive
├── Domain expertise extraction (What does your project DO?)
├── Team workflow analysis (How do you work together?)
├── Architecture deep dive (Why these technical choices?)
├── Pain point identification (Where do you struggle?)
├── Success pattern recognition (What works well?)
└── Vision alignment (Where are you going?)
```

### Phase 3: Context & Command Generation (10-15 minutes)
```
/generate-context + /generate-commands
├── Multi-file hierarchical context creation
├── CLAUDE.md optimization for your project
├── `/generate-commands` - Custom command generation (INTEGRATED)
│   └── Uses .claude-architect/command-forge/ backend engine
├── Agent specialization planning
└── Effectiveness validation testing
```

### Phase 4: Agent Development (5-10 minutes)
```
/develop-agents
├── Specialized agent creation
├── Agent capability definition
├── Orchestration protocol setup
└── Deployment and monitoring
```

## User Control Points

**Every Major Decision Requires Approval**:
- Technology stack analysis results → User validates/corrects
- Domain expertise extraction → User confirms/expands
- Context architecture design → User approves/modifies
- Agent specialization plan → User reviews/adjusts
- Final system deployment → User authorizes

**Session Management**:
- `deep-discovery pause` - Save current state, resume later
- `deep-discovery resume` - Continue from last checkpoint
- `deep-discovery status` - See progress and next steps
- `deep-discovery phases` - Review all phases and current position

## Integration Architecture

**Command Dependencies (FRONTEND → BACKEND INTEGRATED)**:
```
deep-discovery (orchestrator)
├── discover-project (project DNA extraction)
│   └── INTEGRATED: .claude-architect/research/ backend
├── research-patterns (evidence gathering)
├── consult-interactive (consultation engine)  
├── generate-context (context engineering)
├── generate-commands (command generation)
│   └── INTEGRATED: .claude-architect/command-forge/ backend
└── develop-agents (agent development)
```

**Backend Integration Points**:
- `/discover-project` → `.claude-architect/research/`
  - Uses analysis-framework.md methodology
  - Applies pattern-extraction-engine.md logic
  - Validates with CRAAP framework
  - Stores in research-database.yaml

- `/generate-commands` → `.claude-architect/command-forge/`
  - Uses generation-engine.yaml pipeline
  - Applies pattern-library.yaml templates
  - Follows command-categories.yaml organization
  - Processes templates/ directory

**Data Flow**:
1. **Research Phase** → Pattern Database → Consultation Phase
2. **Consultation Phase** → Project DNA → Context Generation
3. **Context Generation** → Context Architecture → Agent Development
4. **Agent Development** → Specialized Agents → Production System

## Session State Management

**Checkpoint System**:
- After each phase completion
- Before major decision points
- User-initiated pause points
- Error recovery checkpoints

**State Persistence**:
- `.claude-architect/session-state.json` - Current progress
- `.claude-architect/project-dna.md` - Accumulated intelligence
- `.claude-architect/consultation-log.md` - Full conversation record
- `.claude-architect/validation-results.json` - Testing outcomes

## Success Metrics (Quality-Focused)

**Not Speed Metrics** (learned from failures):
- Context effectiveness improvement (before/after Claude response quality)
- Project understanding depth (comprehensive vs superficial)
- User satisfaction with generated context
- Agent specialization accuracy
- Long-term context maintenance success

**Measurable Outcomes**:
- Multi-file context system created and validated
- Specialized agents deployed and functional
- User reports improved Claude interactions
- Project DNA captured comprehensively
- 30-day follow-up shows sustained value

## Usage Examples

### Starting a New Deep Discovery
```bash
/deep-discovery start
# Initiates complete 30-60 minute consultation
# Guides through all phases with user control
# Creates comprehensive project intelligence
```

### Resuming a Paused Session
```bash
/deep-discovery resume
# Continues from last checkpoint
# Reviews previous progress
# Picks up where consultation left off
```

### Checking Progress
```bash
/deep-discovery status
# Shows current phase and progress
# Lists completed checkpoints
# Identifies next steps
```

### Understanding the Journey
```bash
/deep-discovery phases
# Shows all 4 phases in detail
# Estimates time for each phase
# Explains what happens at each step
```

## Quality Assurance

**Before Deployment**:
- All user inputs validated and confirmed
- Context effectiveness tested with sample queries
- Agent capabilities verified through test scenarios
- Integration between commands validated
- Session state management tested with pause/resume

**Continuous Validation**:
- Context effectiveness monitoring
- User feedback integration
- Agent performance tracking
- System improvement identification

## Integration with .claude-architect/ Architecture

**References Architecture Components**:
- 8-phase deep discovery methodology
- Session state management system  
- Multi-agent orchestration patterns
- Context engineering best practices
- User control and approval workflows

**Leverages Infrastructure**:
- Session persistence in `.claude-architect/`
- Pattern databases and research outputs
- Consultation templates and frameworks
- Agent development and deployment tools

## Error Handling & Recovery

**Common Scenarios**:
- User needs to pause mid-consultation → Graceful checkpoint save
- Network interruption during research → Resume from last validated state
- User disagrees with analysis → Correction workflow with re-analysis
- Context generation fails → Diagnostic and retry with user input
- Agent deployment issues → Fallback to manual configuration

**Recovery Protocols**:
- State rollback to last known good checkpoint
- User notification of issues with clear next steps
- Manual override capabilities for all automated decisions
- Complete session restart if corruption detected

---

**Remember**: This is about creating genuine project intelligence through comprehensive consultation, not quick superficial setup. Every step emphasizes understanding over speed, quality over convenience.