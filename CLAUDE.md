# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Mission:** Deliver exceptional software through intelligent orchestration of native Claude Code capabilities.

## 🌟 Framework v2.0.0 - UNIVERSAL FOUNDATION

This is the Claude Framework v2.0.0 - a world-class modular meta-framework for enhancing Claude Code's capabilities. This revolutionary architecture eliminates redundancy, enables rapid iteration, and provides a composable system for AI development orchestration.

### Core Architecture Principles
- **Single Source of Truth**: This file contains universal requirements for all commands
- **Modular Composition**: Commands dynamically compose specialized modules as needed
- **Zero Redundancy**: Every concept exists in exactly one place
- **Rapid Iteration**: Update any component independently without breaking others
- **Community Ready**: Standardized interfaces enable easy extension and contribution

## 🧠 Critical Thinking Partnership Principles

### BE A CRITICAL PARTNER, NOT A SYCOPHANT
- **Challenge assumptions** - Question unclear requirements and surface hidden complexities
- **Provide alternative perspectives** - Suggest different approaches, even if they contradict initial ideas
- **Disagree constructively** - When something seems suboptimal, explain why and propose better solutions
- **Avoid automatic agreement** - Never simply affirm; always analyze and provide thoughtful feedback

### ACTUALLY RESEARCH - DEEPLY EXPLORE
- **Web search before suggesting** - Always research current best practices and industry standards
- **Verify with evidence** - Back up recommendations with credible sources and real-world examples
- **Cross-reference information** - Don't rely on single sources; triangulate truth
- **Question surface understanding** - Dig deeper into root causes and underlying patterns

### THINK STEP BY STEP - MAP CAUSE AND EFFECT
- **Analyze before acting** - Spend 3x more time thinking than doing
- **Document decision chains** - Explicitly state: "If we do X, then Y will happen, which causes Z"
- **Consider ripple effects** - Think through second and third-order consequences
- **Verify assumptions** - Test each assumption with concrete evidence

## 🛠️ Universal Claude Code Tool Patterns

**ALL commands must follow these native tool optimization patterns:**

### Parallel Execution (2025 Best Practice)
```python
# ALWAYS batch tool calls in single message for maximum efficiency
Read("file1.py")  # These execute in parallel
Read("file2.py")  # Not sequentially
Read("file3.py")
```

### Read-Before-Write Pattern
```python
# MANDATORY: Always read before any modifications
Read("target_file.py")           # Understand current state
Edit("target_file.py", ...)      # Then modify safely
```

### Efficient Search Patterns
```python
# PREFER: Specific targeted searches
Glob("**/*.py")                  # Find Python files
Grep("class.*Service", "**/*.py") # Find service classes

# AVOID: Broad unfocused searches that waste tokens
```

### Progress Tracking
```python
# REQUIRED: Use TodoWrite/TodoRead for task management
TodoWrite([...])                 # Track all multi-step tasks
TodoRead()                       # Check progress frequently
```

### Error Handling
```python
# MANDATORY: Handle all tool failures gracefully
try:
    result = Read("file.py")
except FileNotFoundError:
    # Graceful degradation with clear user communication
```

## 🚀 Framework Commands

### Modular Command Architecture
```
.claude/
├── commands/           # Core slash commands (self-contained)
│   ├── auto.md        # Intelligent routing + module composition
│   ├── task.md        # Development execution + quality modules
│   ├── swarm.md       # Multi-agent + session management
│   ├── query.md       # Research-only operations
│   └── session.md     # GitHub issue integration
├── modules/           # Composable sub-commands
│   ├── security/      # /security/* modules
│   ├── quality/       # /quality/* modules  
│   ├── deploy/        # /deploy/* modules
│   └── patterns/      # Reusable pattern modules
```

### Primary Commands (Research First, Act Second)
- **`/auto`** - Intelligent routing that researches, then composes optimal modules
- **`/task`** - Development execution with dynamic quality module loading
- **`/query`** - Deep research and analysis (zero modifications)
- **`/swarm`** - Multi-agent orchestration with automatic session creation
- **`/session`** - GitHub issue-based context management

### Composable Modules (Dynamically Loaded)
- **`/security/*`** - Security patterns (audit, compliance, threat-model)
- **`/quality/*`** - Quality enforcement (tdd, review, performance)
- **`/deploy/*`** - Deployment operations (fastapi, protocol, commit)
- **`/patterns/*`** - Reusable patterns (multi-agent, sessions, tools)

## Cognitive Process - AWARE

All operations MUST follow the AWARE framework:

1. **Assess & Analyze** - Understand request, context, constraints
2. **Watch for Assumptions** - Challenge assumptions, verify with evidence
3. **Architect the Approach** - Design solution, determine single vs multi-agent
4. **Run with Verification** - Execute systematically, verify outcomes
5. **Evaluate & Evolve** - Learn from results, document patterns

## Multi-Agent Patterns

The framework leverages Claude Code's native capabilities for powerful parallel execution:

### Task() Pattern - Specialized Expertise
```python
# Multiple Task() calls in ONE message for true parallelism
# Auto-creates session for complex multi-agent work
Task("Frontend Architect", "Design the React component architecture with state management")
Task("Backend Architect", "Design the FastAPI microservices with authentication")
Task("Database Architect", "Design the PostgreSQL schema with optimization")
Task("Security Specialist", "Implement OAuth2 and comprehensive threat model")
Task("DevOps Engineer", "Design Kubernetes deployment with monitoring")
# Session #123 created automatically, agents update progress
```

### Batch() Pattern - Distributed Work
```python
# Single Batch() call for similar tasks
Batch([
    "Refactor UserService to SOLID principles with tests",
    "Refactor ProductService to SOLID principles with tests",
    "Refactor OrderService to SOLID principles with tests"
])
```

### Intelligent Pattern Selection
- **Heterogeneous work** → Task() for specialized agents
- **Homogeneous work** → Batch() for distributed execution
- **Complex workflows** → Hybrid patterns combining both

Multi-agent work (≥3 components) automatically creates GitHub issue sessions.

## Quality Standards

Every execution enforces:
- **Evidence-Based Decisions**: Research and verify before implementing
- **TDD Discipline**: Mandatory RED-GREEN-REFACTOR cycle
- **Security First**: Threat modeling before implementation
- **Performance**: <200ms response time (95th percentile)
- **Test Coverage**: Minimum 90% with quality assertions
- **Documentation**: Comprehensive and current
- **Critical Analysis**: Challenge assumptions and map consequences

### TDD Requirements
- RED-GREEN-REFACTOR cycle mandatory
- Write failing tests first
- 90% test coverage minimum
- Run tests before any commit

### Security Standards
- Threat model before implementation
- No secrets in code or commits
- Input validation on all boundaries
- Security review for data handling
- Financial-grade patterns (PCI DSS, SOX) via `/security`

### Performance Standards
- <200ms p95 response time
- Benchmark critical paths
- Profile before optimization

### Done Criteria
- [ ] All tests passing
- [ ] 90%+ test coverage
- [ ] Security review completed
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] Session completed with outcomes documented

## Common Development Tasks

Since this is a framework repository without traditional source code:

```bash
# Framework validation
python -m pytest tests/unit/test_github_actions_workflow.py -v

# Security checks (if implementing features)
bandit -r src/ -f json
safety check

# Documentation linting
# No specific command - framework uses markdown files
```

## AI Session Management

### Using GitHub Issues for Context Tracking
We use GitHub Issues to track AI coding sessions, providing seamless integration with our development workflow. Sessions are automatically created for complex tasks and multi-agent work.

#### Automatic Session Creation
- **`/swarm`** commands always create a session
- **`/auto`** creates sessions for complex autonomous work
- **`/task`** prompts for sessions on multi-step tasks
- **Multi-agent patterns** (Task(), Batch()) auto-create sessions

#### Starting a Session
1. Create a new issue using the "AI Coding Session" template
2. Add relevant labels: `ai-session`, `active`, and context labels
3. Reference the issue in commits: `git commit -m "feat: implement auth [#123]"`

#### During Development
- Update the issue with progress and key decisions
- Link related PRs and commits
- Add comments for important context changes

#### Completing a Session
1. Update labels: change `active` to `completed`
2. Add outcome labels: `outcome:successful`, `outcome:partial`, or `outcome:blocked`
3. Document lessons learned and follow-up tasks

#### Session Integration Examples
```bash
# Auto-creates session for complex work
/swarm "Implement real-time notifications"
# → Creates session #123 automatically
# → Updates progress as agents work
# → Links all commits and PRs

# Manual session for focused work
/session start "Optimize database queries"
/task "Add query caching"
# → Work is linked to session #124
```

## GitHub Integration

The framework integrates with GitHub through:
- **Workflow**: `.github/workflows/claude.yml` supports three modes:
  - `claude-standard` - Basic Claude Code integration
  - `claude-framework` - Full framework capabilities
  - `claude-maintenance` - Nightly health checks
- **Session Management**: Complex tasks create GitHub issues for tracking
- **Issue Templates**: `.github/ISSUE_TEMPLATE/ai-session.md`

## 🏗️ Revolutionary Modular Architecture

```
.claude/
├── CLAUDE.md              # THIS FILE: Universal foundation (single source of truth)
├── commands/              # Self-contained core commands
│   ├── auto.md           # Intelligent routing + composition
│   ├── task.md           # Development with module loading
│   ├── swarm.md          # Multi-agent + auto-sessions
│   ├── query.md          # Research-only operations
│   └── session.md        # GitHub issue management
├── modules/              # Composable specialized modules
│   ├── security/         # Security patterns library
│   │   ├── audit.md     # Security auditing patterns
│   │   ├── compliance.md # Compliance enforcement
│   │   └── threat-model.md # Threat modeling
│   ├── quality/         # Quality enforcement library
│   │   ├── tdd.md       # Test-driven development
│   │   ├── review.md    # Code review patterns
│   │   └── performance.md # Performance standards
│   ├── deploy/          # Deployment operations library
│   │   ├── fastapi.md   # FastAPI deployment
│   │   ├── protocol.md  # Production protocols
│   │   └── commit.md    # Git operations
│   └── patterns/        # Reusable pattern library
│       ├── multi-agent.md # Task()/Batch() patterns
│       ├── session-mgmt.md # Session integration
│       └── tool-usage.md # Claude Code optimization
└── archive/             # Migration reference
    └── rules/           # Old structure preserved
```

### World-Class Principles
- **Zero Redundancy**: Every concept exists in exactly one location
- **Rapid Iteration**: Update any module independently, changes propagate instantly
- **Modular Composition**: Commands dynamically load only needed modules
- **Token Optimized**: Each module <5k tokens, total system scalable
- **Community Ready**: Standardized interfaces enable easy contribution
- **Reality-Based**: Only proven Claude Code capabilities, no theoretical features
- **Session-Aware**: Intelligent automatic session creation for complex work

## Getting Started

1. **Simple tasks**: Use `/task` for most development work
2. **Research**: Use `/query` to understand before changing
3. **Complex work**: Use `/swarm` for multi-component features (auto-creates session)
4. **Let it decide**: Use `/auto` when unsure
5. **Track progress**: Use `/session` to manage AI development context

## Framework Capabilities

### Proven Patterns (Battle-Tested)
- **3x faster development** with multi-agent coordination
- **94.4% success rate** on enterprise systems
- **Zero-configuration** intelligent pattern selection
- **Context-aware** execution with 60% trigger management
- **Self-improving** through continuous learning

### Integration Features
- GitHub CLI automation (`gh`)
- CI/CD pipeline generation
- Extended thinking for complex problems
- Automated quality enforcement
- Real-time progress tracking

## Important Notes

1. **No Traditional Source Code**: This framework contains configuration and documentation only
2. **Command Usage**: Use `/auto` when unsure which command to use
3. **Session Creation**: Automatic for multi-agent work or use `/session`
4. **Legacy Support**: Old commands work via `/auto` with 90-day deprecation
5. **Token Limits**: Framework optimized for efficiency, responses limited appropriately

---

*Remember: Be a critical thinking partner. Research deeply. Challenge assumptions. Map cause and effect. Follow AWARE, leverage native capabilities, and let intelligent orchestration handle the complexity.*