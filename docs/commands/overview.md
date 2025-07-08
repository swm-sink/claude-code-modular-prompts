| version | last_updated | status |
|---------|--------------|--------|
| 2.4.0   | 2025-07-08   | stable |

# Command Overview - Claude Code Framework 2.4.0

────────────────────────────────────────────────────────────────────────────────

> **Framework Enhancement**: Now powered by the **Module Runtime Engine** with universal quality gates and comprehensive TDD enforcement!

────────────────────────────────────────────────────────────────────────────────

## What's New in 2.4.0

### Module Runtime Engine Integration

All commands now benefit from the deterministic orchestration system that provides:

```xml
<runtime_enhancements>
  <tdd_enforcement>Mandatory RED-GREEN-REFACTOR cycles across all development commands</tdd_enforcement>
  <quality_gates>Universal quality gates with blocking enforcement</quality_gates>
  <critical_thinking>30-second minimum analysis before any action</critical_thinking>
  <parallel_optimization>70% performance improvement through batched operations</parallel_optimization>
  <standardized_patterns>Checkpoint-based thinking patterns for consistent execution</standardized_patterns>
</runtime_enhancements>
```

### Enhanced Command Capabilities

| Enhancement | Description | Impact |
|-------------|-------------|--------|
| **TDD Enforcement** | All development commands enforce strict test-driven development | Higher code quality, comprehensive testing |
| **Quality Gates** | Universal validation framework applied to all commands | Consistent quality standards, error prevention |
| **Parallel Execution** | Tool calls batched for 70% performance improvement | Faster command execution, better user experience |
| **Critical Thinking** | Mandatory analysis and consequence mapping | Better decision making, reduced errors |
| **Session Tracking** | Enhanced GitHub integration for complex work | Better project management, progress visibility |

────────────────────────────────────────────────────────────────────────────────

## Core Commands

### Primary Development Commands

#### `/task` - Single Component Development
**Purpose**: Focused development work with strict TDD enforcement

```bash
/task "Add user authentication validation"
```

**Runtime Behavior:**
- **TDD Enforcement**: Standard RED-GREEN-REFACTOR cycle
- **Quality Gates**: Foundational + Development gates
- **Thinking Pattern**: Understand → RED test → GREEN code → REFACTOR → Validate
- **Module Integration**: critical-thinking → tdd → task-management → production-standards

**Best For:**
- Single file modifications
- Bug fixes with clear scope
- Feature enhancements to existing components
- Refactoring with comprehensive test coverage

---

#### `/feature` - Complete Feature Development  
**Purpose**: Autonomous feature development with PRD generation and MVP planning

```bash
/feature "Shopping cart with payment processing"
```

**Runtime Behavior:**
- **TDD Enforcement**: Full feature TDD with integration testing
- **Quality Gates**: Foundational + Development + Documentation gates
- **Thinking Pattern**: Generate PRD → Tech analysis → Session creation → MVP → TDD cycles → Quality validation
- **Module Integration**: critical-thinking → session-management → feature-workflow → tdd → production-standards

**Best For:**
- New feature implementations
- Complex user stories
- Features requiring multiple components
- Requirements that need PRD clarification

---

#### `/swarm` - Multi-Agent Coordination
**Purpose**: Complex multi-component system changes with parallel development

```bash
/swarm "Migrate authentication system to OAuth2"
```

**Runtime Behavior:**
- **TDD Enforcement**: Multi-agent TDD coordination with isolated worktrees
- **Quality Gates**: ALL gates including coordination validation
- **Thinking Pattern**: Session → Analyze → Worktrees → Parallel Task() → Recovery → Merge
- **Module Integration**: critical-thinking → session-management → multi-agent → tdd → git-operations → production-standards

**Best For:**
- System-wide architectural changes
- Multi-service integrations
- Large refactoring efforts
- Complex feature implementations spanning multiple components

---

### Analysis and Research Commands

#### `/query` - Research and Analysis
**Purpose**: Read-only analysis and understanding with test-aware research

```bash
/query "How does the authentication flow work?"
```

**Runtime Behavior:**
- **TDD Integration**: Test-aware research and pattern analysis
- **Quality Gates**: Analysis gates only (no modification gates)
- **Thinking Pattern**: Parse → Parallel search → Read → Analyze → Map → Report → NO MODIFICATIONS
- **Module Integration**: critical-thinking → research-analysis → pattern-library → tdd

**Best For:**
- Understanding existing code
- Security analysis and investigation
- Architecture documentation
- Pattern discovery and analysis
- Pre-development research

---

#### `/docs` - Documentation Gateway
**Purpose**: All documentation creation and management with strict gateway enforcement

```bash
/docs generate "API Reference Guide"
```

**Runtime Behavior:**
- **TDD Integration**: TDD methodology documentation and cross-references
- **Quality Gates**: Foundational + Documentation + Standards gates
- **Thinking Pattern**: BLOCK external docs → Parse type → Search/Generate → Standards → Location → Validate → Index
- **Module Integration**: critical-thinking → documentation → intelligent-routing → tdd

**Best For:**
- Creating new documentation
- Updating existing documentation
- Generating structured guides
- Maintaining documentation consistency

---

### Intelligence and Management Commands

#### `/auto` - Intelligent Routing
**Purpose**: TDD-aware intelligent routing with complexity analysis

```bash
/auto "Add user registration with email verification"
```

**Runtime Behavior:**
- **TDD Integration**: Routes to appropriate TDD-enforced commands
- **Quality Gates**: Analysis + Routing gates
- **Thinking Pattern**: Calculate complexity score → Research → Route intelligently → Cache decisions
- **Module Integration**: critical-thinking → intelligent-routing → tdd → pattern-library

**Best For:**
- When uncertain about the right approach
- Complex requests requiring analysis
- Mixed requirements (research + development)
- Learning the framework's decision-making

---

#### `/session` - Session Management
**Purpose**: GitHub issue tracking with TDD progress monitoring

```bash
/session "Multi-component authentication system"
```

**Runtime Behavior:**
- **TDD Integration**: TDD progress tracking and methodology documentation
- **Quality Gates**: Foundational + Progress tracking gates
- **Thinking Pattern**: Type → Create/Update/Complete → Link → Context → Labels → TDD tracking
- **Module Integration**: critical-thinking → session-management → tdd → git-operations

**Best For:**
- Long-running development work
- Complex features requiring tracking
- Multi-session development projects
- Progress monitoring and documentation

---

#### `/protocol` - Production Standards
**Purpose**: Strictest enforcement with comprehensive compliance validation

```bash
/protocol "Payment processing with PCI compliance"
```

**Runtime Behavior:**
- **TDD Enforcement**: Strictest TDD with production compliance testing
- **Quality Gates**: ALL gates with maximum enforcement
- **Thinking Pattern**: Session → Validate → TDD → Threat model → Gates → Compliance → Block on ANY failure
- **Module Integration**: critical-thinking → session-management → production-standards → tdd → threat-modeling → pre-commit

**Best For:**
- Production-critical implementations
- Security-sensitive features
- Compliance-required development
- Maximum quality assurance

────────────────────────────────────────────────────────────────────────────────

## Command Selection Decision Tree

### Quick Decision Matrix

| Scenario | Command | Reasoning |
|----------|---------|-----------|
| **"Fix login bug"** | `/task` | Single component, clear scope |
| **"Add shopping cart feature"** | `/feature` | Complete feature requiring PRD |
| **"Migrate to microservices"** | `/swarm` | Multi-component system change |
| **"How does auth work?"** | `/query` | Research only, no modifications |
| **"Create API docs"** | `/docs` | Documentation creation |
| **"Not sure what to do"** | `/auto` | Intelligent routing and analysis |
| **"Track complex project"** | `/session` | GitHub issue management |
| **"Payment processing"** | `/protocol` | Production-critical with compliance |

### Decision Flow

```
Request Analysis
      │
      ▼
┌─────────────────┐
│ Single file +   │ YES  ┌─────────┐
│ <50 lines?      │ ──→  │ /task   │
└─────────────────┘      └─────────┘
      │ NO
      ▼
┌─────────────────┐
│ Multiple files + │ YES  ┌─────────┐
│ clear spec?      │ ──→  │ /feature│
└─────────────────┘      └─────────┘
      │ NO
      ▼
┌─────────────────┐
│ System-wide     │ YES  ┌─────────┐
│ changes?        │ ──→  │ /swarm  │
└─────────────────┘      └─────────┘
      │ NO
      ▼
┌─────────────────┐
│ Research/       │ YES  ┌─────────┐
│ understand?     │ ──→  │ /query  │
└─────────────────┘      └─────────┘
      │ NO
      ▼
┌─────────────────┐
│ Documentation?  │ YES  ┌─────────┐
│                 │ ──→  │ /docs   │
└─────────────────┘      └─────────┘
      │ NO
      ▼
┌─────────────────┐
│ Uncertain?      │ YES  ┌─────────┐
│                 │ ──→  │ /auto   │
└─────────────────┘      └─────────┘
```

────────────────────────────────────────────────────────────────────────────────

## Quality Gates and TDD Enforcement

### Universal Quality Gates

All commands now enforce these quality standards:

```xml
<quality_gate_categories>
  <foundational>
    <critical_thinking>30-second minimum analysis with consequence mapping</critical_thinking>
    <requirement_clarity>Clear understanding of goals and constraints</requirement_clarity>
    <module_integration>Proper module dependency resolution</module_integration>
    <error_handling>Comprehensive error recovery protocols</error_handling>
  </foundational>
  
  <development>
    <tdd_compliance>RED-GREEN-REFACTOR cycle enforcement</tdd_compliance>
    <code_quality>90%+ test coverage, clean architecture</code_quality>
    <security_requirements>Threat modeling and vulnerability assessment</security_requirements>
    <performance_validation>Response time and resource usage validation</performance_validation>
  </development>
  
  <coordination>
    <multi_agent_sync>Agent coordination and conflict resolution</multi_agent_sync>
    <session_tracking>GitHub issue integration and progress monitoring</session_tracking>
    <integration_validation>Cross-component compatibility testing</integration_validation>
  </coordination>
  
  <documentation>
    <standards_compliance>Framework documentation standards adherence</standards_compliance>
    <tdd_methodology>TDD process documentation and references</tdd_methodology>
  </documentation>
  
  <analysis>
    <research_comprehensiveness>Thorough investigation and evidence gathering</research_comprehensiveness>
    <routing_decision_quality>Intelligent command selection and justification</routing_decision_quality>
  </analysis>
</quality_gate_categories>
```

### TDD Enforcement Matrix

| Command | TDD Level | Requirements | Blocking Conditions |
|---------|-----------|--------------|-------------------|
| `/task` | **Standard** | Single-component RED-GREEN-REFACTOR | Implementation before tests, <90% coverage |
| `/feature` | **Feature-level** | Multi-component integration testing | Missing feature tests, integration gaps |
| `/swarm` | **Multi-agent** | Isolated worktree testing, coordination | Agent conflicts, integration failures |
| `/protocol` | **Production** | Security + performance + compliance testing | ANY quality gate failure |
| `/query` | **Test-aware** | Pattern analysis, testing methodology research | Attempted modifications |
| `/docs` | **Methodology** | TDD documentation, cross-references | Missing methodology refs |
| `/session` | **Progress** | TDD progress tracking, methodology docs | Incomplete tracking |
| `/auto` | **Routing** | Routes to appropriate TDD enforcement | Routes to non-TDD commands for code |

### Blocking Enforcement

The runtime engine will **HALT** execution for these violations:

- ❌ **Implementation before tests**: Code written without failing tests first
- ❌ **Broken TDD cycles**: GREEN without RED, or REFACTOR without GREEN
- ❌ **Coverage violations**: Less than 90% test coverage for new code
- ❌ **Security issues**: Unaddressed security threats or vulnerabilities
- ❌ **Performance regression**: Response times exceeding 200ms p95
- ❌ **Integration failures**: Multi-component coordination problems
- ❌ **Documentation violations**: Missing TDD methodology references

────────────────────────────────────────────────────────────────────────────────

## Performance Optimizations

### Parallel Execution Benefits

The Module Runtime Engine provides **70% performance improvement** through:

```xml
<optimization_features>
  <tool_batching>Multiple Read/Grep/Glob operations executed simultaneously</tool_batching>
  <module_parallelization>Independent modules execute concurrently</module_parallelization>
  <dependency_optimization>Topological sorting minimizes execution time</dependency_optimization>
  <context_preservation>State maintained across module boundaries</context_preservation>
  <intelligent_caching>Command routing decisions cached for reuse</intelligent_caching>
</optimization_features>
```

### Performance Targets

| Operation | Target Time | 2.4.0 Improvement |
|-----------|-------------|------------------|
| Command execution | < 2 minutes typical | 70% faster through batching |
| Module loading | < 10 seconds | Dependency caching |
| Quality gate validation | < 30 seconds | Parallel validation |
| TDD cycle completion | < 5 minutes | Streamlined workflow |
| Tool call batching | 70% reduction | Parallel execution |

────────────────────────────────────────────────────────────────────────────────

## Error Handling and Recovery

### Enhanced Error Recovery

The runtime engine provides comprehensive error handling:

```xml
<error_recovery_protocols>
  <classification>
    <module_errors>Loading failures, execution errors, integration failures</module_errors>
    <tdd_violations>Implementation before tests, coverage failures, cycle violations</tdd_violations>
    <quality_gate_failures>Security issues, performance problems, compliance violations</quality_gate_failures>
    <coordination_failures>Agent conflicts, session issues, communication breakdowns</coordination_failures>
  </classification>
  
  <recovery_mechanisms>
    <graceful_degradation>Continue with reduced functionality for non-critical failures</graceful_degradation>
    <retry_mechanisms>Exponential backoff for transient failures</retry_mechanisms>
    <escalation_paths>Route to appropriate recovery modules or user intervention</escalation_paths>
    <rollback_capabilities>State rollback for critical failures</rollback_capabilities>
  </recovery_mechanisms>
</error_recovery_protocols>
```

### Common Error Scenarios and Solutions

#### TDD Violation: "Implementation before tests"
**Solution:**
```bash
1. Delete implementation code
2. Write failing tests that specify behavior  
3. Verify tests fail for correct reasons
4. Restart with proper RED-GREEN-REFACTOR cycle
```

#### Quality Gate Failure: "Coverage below 90%"
**Solution:**
```bash
1. Identify uncovered code paths
2. Write additional test cases for edge cases
3. Focus on boundary conditions and error scenarios
4. Re-run coverage analysis and proceed when threshold met
```

#### Module Dependency Resolution Failed
**Solution:**
```bash
1. Check module exists in .claude/modules/
2. Verify module structure and metadata
3. Review dependency declarations
4. Use /protocol for enhanced validation
```

────────────────────────────────────────────────────────────────────────────────

## Migration from Previous Versions

### Upgrading from 2.3.x

**Backward Compatibility:**
- All existing commands continue to work
- Enhanced with runtime engine benefits automatically
- No syntax changes required

**New Capabilities:**
- TDD enforcement on all development commands
- Universal quality gates with blocking enforcement
- 70% performance improvement through parallel execution
- Enhanced error recovery and rollback capabilities

**Breaking Changes:**
- None - fully backward compatible

**Recommended Actions:**
1. Update command usage to leverage new TDD enforcement
2. Adopt quality gate validation for higher reliability
3. Use parallel execution for faster development cycles
4. Leverage enhanced error recovery for robust workflows

### Framework Evolution

| Version | Key Enhancement | Impact |
|---------|----------------|--------|
| **2.4.0** | Module Runtime Engine | TDD enforcement, quality gates, 70% performance improvement |
| **2.3.x** | Command standardization | Consistent command behavior |
| **2.2.x** | Module architecture | Modular composition framework |
| **2.1.x** | Quality foundation | Basic quality standards |

────────────────────────────────────────────────────────────────────────────────

## Best Practices for 2.4.0

### Leveraging Runtime Engine Features

1. **Embrace TDD Enforcement**
   ```bash
   # Always start with failing tests
   /task "Add email validation" 
   # Runtime engine ensures RED-GREEN-REFACTOR cycle
   ```

2. **Use Quality Gates Proactively**
   ```bash
   # For production code
   /protocol "Payment processing integration"
   # Maximum quality gate enforcement
   ```

3. **Optimize with Parallel Execution**
   ```bash
   # Let the runtime engine batch operations
   /auto "Complex feature analysis"
   # 70% faster through intelligent batching
   ```

4. **Leverage Critical Thinking Integration**
   ```bash
   # All commands now include 30-second analysis
   # Trust the framework's consequence mapping
   /swarm "Architecture migration"
   ```

### Command Selection Strategies

1. **Start with `/auto`** for intelligent routing
2. **Use `/query`** for understanding before development
3. **Choose `/task`** for focused, single-component work
4. **Select `/feature`** for complete feature development
5. **Apply `/swarm`** for complex, multi-component changes
6. **Enforce with `/protocol`** for production-critical work

### Session Management

```bash
# For complex work requiring tracking
/session "E-commerce platform overhaul"
# Creates GitHub issue with comprehensive tracking
# Links all related artifacts and progress
# Maintains TDD methodology documentation
```

────────────────────────────────────────────────────────────────────────────────

## Related Documentation

### Core Framework
- **[CLAUDE.md](../../CLAUDE.md)** - Complete framework specification with 2.4.0 enhancements
- **[Module Runtime Engine User Guide](../framework/module-runtime-engine.md)** - Comprehensive practical guide
- **[Command Selection Guide](../COMMAND_SELECTION_GUIDE.md)** - Stop confusion between commands

### Runtime Engine Details
- **[Module Composition Framework](../../.claude/modules/patterns/module-composition-framework.md)** - Technical architecture
- **[Universal Quality Gates](../../.claude/modules/quality/universal-quality-gates.md)** - Gate specifications
- **[TDD Standards](../framework/tdd-standards.md)** - Detailed TDD methodology
- **[Thinking Pattern Template](../../.claude/modules/patterns/thinking-pattern-template.md)** - Standardized patterns

### Development Guides
- **[Getting Started](../GETTING_STARTED.md)** - Framework introduction
- **[Production Standards](../framework/production-standards.md)** - Quality requirements
- **[Critical Thinking Enforcement](../framework/critical-thinking-enforcement.md)** - Analysis requirements
- **[Feature Development Examples](../framework/feature-development-examples.md)** - Real-world scenarios

### Migration and Integration
- **[Migration Guide 2.3 to 2.4](../releases/migration-2.3-to-2.4.md)** - Upgrade instructions
- **[Documentation Index](../DOCUMENTATION_INDEX.md)** - Complete documentation map
- **[GitHub Integration Guide](../framework/claude-code-integration.md)** - Issue tracking setup

────────────────────────────────────────────────────────────────────────────────

## Quick Reference

### The Essential Commands
```bash
/auto "..."     # Smart routing (use when unsure)
/task "..."     # Single component with TDD
/feature "..."  # Complete features with PRD  
/swarm "..."    # Multi-component coordination
/query "..."    # Research only, no modifications
/docs "..."     # Documentation creation/update
/session "..."  # GitHub issue tracking
/protocol "..." # Maximum quality enforcement
```

### Key Principles
- **TDD First**: All development enforces RED-GREEN-REFACTOR
- **Quality Gates**: Universal validation prevents errors
- **Critical Thinking**: 30-second analysis before action
- **Parallel Execution**: 70% performance improvement
- **Session Tracking**: GitHub integration for complex work

### Success Indicators
- ✅ Tests written before implementation
- ✅ Quality gates pass without manual intervention
- ✅ Commands complete faster through parallel execution
- ✅ GitHub issues track complex work automatically
- ✅ Error recovery handles failures gracefully

────────────────────────────────────────────────────────────────────────────────

## See Also

- **[Documentation Index](../DOCUMENTATION_INDEX.md)** - Complete documentation map with 2.4.0 enhancements
- **[Command Selection Guide](../COMMAND_SELECTION_GUIDE.md)** - Quick decision matrix for choosing commands
- **[Getting Started](../GETTING_STARTED.md)** - Framework introduction and basic usage
- **[Module Runtime Engine User Guide](../framework/module-runtime-engine.md)** - Detailed technical guide

────────────────────────────────────────────────────────────────────────────────

**Framework Version 2.4.0**: *Deterministic orchestration with comprehensive TDD enforcement and universal quality gates for reliable, high-performance development workflows.*