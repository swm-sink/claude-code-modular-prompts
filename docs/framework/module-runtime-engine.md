| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Module Runtime Engine User Guide

────────────────────────────────────────────────────────────────────────────────

## Overview

The Module Runtime Engine is the deterministic orchestration system that powers Claude Code's modular framework. It ensures consistent command execution through standardized thinking patterns, universal quality gates, and comprehensive TDD enforcement across all development operations.

────────────────────────────────────────────────────────────────────────────────

## What is the Module Runtime Engine?

```xml
<runtime_engine purpose="Deterministic module composition and execution for Claude 4">
  <core_capabilities>
    <thinking_pattern_standardization>Checkpoint-based patterns with critical thinking integration</thinking_pattern_standardization>
    <tdd_enforcement>Mandatory RED-GREEN-REFACTOR cycles across all development commands</tdd_enforcement>
    <quality_gate_integration>Universal quality gates with blocking enforcement</quality_gate_integration>
    <parallel_optimization>70% performance improvement through batched operations</parallel_optimization>
  </core_capabilities>
</runtime_engine>
```

The engine transforms commands from simple delegates into sophisticated orchestration systems that:

- **Enforce TDD compliance** across all development work
- **Apply critical thinking** with 30-second minimum analysis
- **Validate quality gates** at every checkpoint
- **Optimize execution** through parallel operations
- **Maintain consistency** across command implementations

────────────────────────────────────────────────────────────────────────────────

## How Commands Work With the Runtime Engine

### Command-Module Integration

Each command in the framework operates through a three-layer architecture:

```
┌─────────────────┐
│   Command       │ ← User Interface Layer
│   (delegate)    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ Runtime Engine  │ ← Orchestration Layer
│ (orchestrate)   │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│    Modules      │ ← Implementation Layer
│ (implement)     │
└─────────────────┘
```

### Command Runtime Specification

Every command follows this standardized structure:

```xml
<command_runtime>
  <thinking_pattern enforcement="MANDATORY">Checkpoint-based with critical thinking</thinking_pattern>
  <tdd_integration enforcement="MANDATORY">Command-specific TDD requirements</tdd_integration>
  <module_execution enforcement="MANDATORY">Core + contextual + support modules</module_execution>
  <quality_gates enforcement="MANDATORY">Blocking validation at checkpoints</quality_gates>
</command_runtime>
```

────────────────────────────────────────────────────────────────────────────────

## TDD Enforcement Matrix

The runtime engine enforces Test-Driven Development through a comprehensive matrix that adapts to each command's purpose:

### Universal TDD Principles

```xml
<tdd_principles enforcement="BLOCKING">
  <red_phase>ALWAYS write failing tests FIRST before implementation</red_phase>
  <green_phase>Implement minimal code to make tests pass</green_phase>
  <refactor_phase>Improve design while maintaining green tests</refactor_phase>
  <coverage_requirements>≥90% test coverage for all new code</coverage_requirements>
</tdd_principles>
```

### Command-Specific TDD Integration

| Command | TDD Enforcement Level | Key Requirements |
|---------|----------------------|------------------|
| `/task` | **Standard TDD** | Single-component with foundational + development gates |
| `/swarm` | **Multi-agent TDD** | Coordination with isolated worktrees and comprehensive testing |
| `/protocol` | **Strictest TDD** | Production compliance with security and performance testing |
| `/session` | **TDD Tracking** | Progress monitoring and methodology documentation |
| `/auto` | **TDD-aware Routing** | Routes to appropriate TDD enforcement commands |
| `/query` | **TDD Pattern Analysis** | Test-aware research and pattern identification |
| `/docs` | **TDD Documentation** | Methodology documentation and cross-references |

### Blocking Conditions

The runtime engine will **HALT** execution for these TDD violations:

- ❌ Implementation written before tests
- ❌ Tests pass when they should fail  
- ❌ Missing test coverage (<90%)
- ❌ Broken TDD cycle sequence
- ❌ Integration without comprehensive tests

────────────────────────────────────────────────────────────────────────────────

## Quality Gates System

### Universal Quality Gates

The runtime engine applies these gates across all commands:

```xml
<universal_gates>
  <foundational>Critical thinking, requirement clarity, error handling</foundational>
  <development>TDD compliance, code quality, security validation</development>
  <coordination>Multi-agent sync, session tracking, integration checks</coordination>
  <documentation>Standards compliance, TDD methodology references</documentation>
  <analysis>Research depth, routing decision quality</analysis>
</universal_gates>
```

### Gate Enforcement Levels

| Level | Behavior | Usage |
|-------|----------|-------|
| **BLOCKING** | Halt execution until resolved | Critical violations |
| **CONDITIONAL** | Alternative paths or degraded functionality | Non-critical issues |
| **WARNING** | Log issue but continue | Advisory feedback |

────────────────────────────────────────────────────────────────────────────────

## Practical Usage Examples

### Example 1: Simple Development Task

```bash
# User request
/task "Add user authentication validation"

# Runtime engine orchestration:
1. ✅ Critical thinking (30-second analysis)
2. ✅ TDD RED phase (write failing tests first)
3. ✅ Development gates (security validation)  
4. ✅ TDD GREEN phase (minimal implementation)
5. ✅ Quality validation (coverage check)
6. ✅ TDD REFACTOR phase (design improvement)
```

### Example 2: Complex Multi-Component Feature

```bash
# User request  
/swarm "Implement shopping cart with payment processing"

# Runtime engine orchestration:
1. ✅ Session creation with GitHub issue tracking
2. ✅ Multi-agent coordination setup
3. ✅ Parallel worktree isolation  
4. ✅ Component-specific TDD cycles
5. ✅ Integration testing coordination
6. ✅ Performance and security validation
7. ✅ Merge with comprehensive testing
```

### Example 3: Documentation Generation

```bash
# User request
/docs "Create API reference guide"

# Runtime engine orchestration:
1. ✅ Gateway enforcement (block external docs)
2. ✅ TDD methodology integration
3. ✅ Content search and discovery
4. ✅ Framework standards application
5. ✅ Cross-reference validation
6. ✅ Location verification (/docs only)
```

────────────────────────────────────────────────────────────────────────────────

## Troubleshooting Common Issues

### Issue: "TDD violation: Implementation before tests"

**Symptoms:**
- Code written without failing tests first
- Runtime engine blocks execution

**Solution:**
```bash
1. Delete implementation code
2. Write failing tests that specify behavior
3. Verify tests fail for correct reasons  
4. Restart with proper RED-GREEN-REFACTOR cycle
```

**Prevention:**
- Always start with `/task` or `/protocol` for TDD enforcement
- Use `/query` for research before coding
- Follow checkpoint validation prompts

### Issue: "Quality gate failure: Coverage below 90%"

**Symptoms:**
- Test coverage metrics insufficient
- Blocked from proceeding to next phase

**Solution:**
```bash
1. Identify uncovered code paths
2. Write additional test cases
3. Focus on edge cases and error conditions
4. Re-run coverage analysis
5. Proceed when threshold met
```

**Prevention:**
- Write comprehensive test scenarios in RED phase
- Include boundary conditions and error cases
- Use TDD to drive coverage naturally

### Issue: "Module dependency resolution failed"

**Symptoms:**
- Command execution hangs or fails
- Missing module references

**Solution:**
```bash
1. Check module exists in .claude/modules/
2. Verify module structure and metadata
3. Review dependency declarations
4. Use /protocol for enhanced validation
```

**Prevention:**
- Keep modules updated with framework versions
- Follow module composition patterns
- Test module integration regularly

### Issue: "Parallel execution timeout"

**Symptoms:**
- Commands taking longer than expected
- Tool calls not completing

**Solution:**
```bash
1. Check system resources and network
2. Break large operations into smaller chunks
3. Use sequential execution for debugging
4. Verify tool call parameters
```

**Prevention:**
- Batch related operations together
- Use appropriate timeouts for operations
- Monitor system performance during execution

────────────────────────────────────────────────────────────────────────────────

## Performance Optimization

### Parallel Execution Benefits

The runtime engine provides **70% performance improvement** through:

```xml
<optimization_patterns>
  <tool_batching>Multiple Read/Grep/Glob operations executed simultaneously</tool_batching>
  <module_parallelization>Independent modules execute concurrently</module_parallelization>
  <dependency_optimization>Topological sorting minimizes execution time</dependency_optimization>
  <context_preservation>State maintained across module boundaries</context_preservation>
</optimization_patterns>
```

### Performance Targets

| Operation | Target Time | Optimization |
|-----------|-------------|--------------|
| Command execution | < 2 minutes typical | Parallel tool calls |
| Module loading | < 10 seconds | Dependency caching |
| Quality gate validation | < 30 seconds | Batched checks |
| TDD cycle completion | < 5 minutes | Streamlined workflow |

### Best Practices for Performance

1. **Use parallel-friendly commands**: `/task`, `/swarm`, `/query`
2. **Batch related operations**: Group file reads, searches together  
3. **Leverage intelligent routing**: Let `/auto` optimize command selection
4. **Monitor execution**: Watch for bottlenecks and timeouts
5. **Keep modules focused**: Single responsibility for better parallelization

────────────────────────────────────────────────────────────────────────────────

## Advanced Usage Patterns

### Session-Based Development

For complex features requiring multiple TDD cycles:

```bash
/session "Multi-component authentication system"
# Creates GitHub issue, tracks progress
# Coordinates multiple /task operations  
# Maintains TDD compliance across sessions
# Links artifacts and documentation
```

### Protocol-Driven Development

For production-critical implementations:

```bash
/protocol "Payment processing with PCI compliance"
# Strictest TDD enforcement
# Security threat modeling
# Performance benchmarking
# Compliance validation
# Complete audit trail
```

### Research-First Development

For unknown or complex domains:

```bash
/query "How does OAuth2 work in this codebase?"
# Read-only analysis and understanding
# Pattern identification and documentation
# No modifications or implementation
# Prepares for informed development

# Follow with:
/task "Implement OAuth2 refresh token handling"
# Armed with research insights
# TDD-driven implementation
# Quality gate validation
```

────────────────────────────────────────────────────────────────────────────────

## Framework Integration

### Module Dependencies

The runtime engine integrates with key framework modules:

```xml
<framework_integration>
  <thinking_patterns>patterns/thinking-pattern-template.md</thinking_patterns>
  <composition_framework>patterns/module-composition-framework.md</composition_framework>
  <quality_gates>quality/universal-quality-gates.md</quality_gates>
  <tdd_enforcement>quality/tdd.md</tdd_enforcement>
  <critical_thinking>quality/critical-thinking.md</critical_thinking>
</framework_integration>
```

### Command Selection Decision Tree

When uncertain about which command to use:

```
Complex task? → /swarm (multi-agent coordination)
    ↓ no
Single component? → /task (standard TDD)
    ↓ no  
Need research? → /query (read-only analysis)
    ↓ no
Documentation? → /docs (gateway enforcement)
    ↓ no
Uncertain? → /auto (intelligent routing)
```

### Version Compatibility

| Framework Version | Runtime Engine | Compatibility |
|------------------|----------------|---------------|
| 2.4.0+ | Native integration | Full support |
| 2.3.x | Backward compatible | Limited features |
| 2.2.x | Manual orchestration | Basic support |

────────────────────────────────────────────────────────────────────────────────

## Monitoring and Metrics

### Runtime Metrics

The engine tracks key performance indicators:

```xml
<runtime_metrics>
  <execution_metrics>Module load time, command completion, success rates</execution_metrics>
  <quality_metrics>TDD compliance, quality gate pass rates, coverage</quality_metrics>
  <performance_metrics>Parallel efficiency, resource usage, throughput</performance_metrics>
  <error_metrics>Failure rates, recovery success, escalation frequency</error_metrics>
</runtime_metrics>
```

### Continuous Improvement

The runtime engine evolves through:

- **Pattern refinement** based on usage analytics
- **Performance optimization** from execution metrics  
- **Quality enhancement** through gate effectiveness
- **User feedback** integration for workflow improvement

────────────────────────────────────────────────────────────────────────────────

## Related Documentation

### Core Framework
- [CLAUDE.md](../../CLAUDE.md) - Complete framework specification
- [TDD Standards](./tdd-standards.md) - Detailed TDD methodology
- [Critical Thinking Enforcement](./critical-thinking-enforcement.md) - Analysis requirements

### Command References  
- [Command Selection Guide](../COMMAND_SELECTION_GUIDE.md) - Choosing the right command
- [Getting Started](../GETTING_STARTED.md) - Framework introduction
- [Documentation Index](../DOCUMENTATION_INDEX.md) - Complete documentation map

### Implementation Details
- [Module Composition Framework](.claude/modules/patterns/module-composition-framework.md) - Technical architecture
- [Universal Quality Gates](.claude/modules/quality/universal-quality-gates.md) - Gate specifications
- [Thinking Pattern Template](.claude/modules/patterns/thinking-pattern-template.md) - Standardized patterns

────────────────────────────────────────────────────────────────────────────────

*This guide provides comprehensive coverage of the Module Runtime Engine for practical development usage. For technical implementation details, see the module documentation referenced above.*