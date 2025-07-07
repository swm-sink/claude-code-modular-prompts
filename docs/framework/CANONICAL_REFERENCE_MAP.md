# Canonical Reference Map - Framework 3.0

| version | created | purpose |
|---------|---------|---------|
| 1.0.0   | 2025-07-07 | Single source of truth for all framework concepts |

## Purpose

This document maps all framework concepts to their canonical (authoritative) sources, preventing duplication and ensuring consistency.

## Core Concepts

### Critical Thinking
- **Canonical Source**: `.claude/modules/quality/critical-thinking.md`
- **References**:
  - `CLAUDE.md` - Brief mention in rules
  - `docs/framework/critical-thinking-enforcement.md` - Historical context only
- **Purpose**: Enforce forensic-level thinking to prevent framework disasters

### AWARE Process
- **Canonical Source**: `docs/framework/aware-framework.md`
- **References**:
  - `CLAUDE.md` - Brief 5-phase summary with link to full docs
- **Purpose**: Unified cognitive process for all AI operations

### TDD (Test-Driven Development)
- **Canonical Source**: `.claude/modules/quality/tdd.md`
- **References**:
  - `CLAUDE.md` - Quality gates mention
  - `docs/framework/tdd-standards.md` - Examples and patterns (references module)
- **Purpose**: Enforce RED-GREEN-REFACTOR cycle for all development

### Session Management
- **Canonical Source**: `.claude/modules/patterns/session-management.md`
- **References**:
  - Various commands reference session integration
  - `CLAUDE.md` - GitHub workflow section mentions sessions
- **Purpose**: Intelligent GitHub issue tracking for complex work

### Multi-Agent Coordination
- **Canonical Source**: `.claude/modules/patterns/multi-agent.md`
- **References**:
  - `/swarm` command delegates to this module
  - Various modules reference multi-agent triggers
- **Purpose**: Orchestrate parallel agent work for complex systems

### Git Operations
- **Canonical Source**: `.claude/modules/patterns/git-operations.md`
- **References**:
  - Various commands use git patterns
- **Purpose**: Intelligent git workflows and conventional commits

### Tool Usage Patterns
- **Canonical Source**: `.claude/modules/patterns/pattern-library.md`
- **References**:
  - `CLAUDE.md` - Brief tool patterns section
- **Purpose**: Proven patterns for efficient tool usage

### Production Standards
- **Canonical Source**: `.claude/modules/quality/production-standards.md`
- **References**:
  - Various modules depend on production standards
- **Purpose**: Enforce production-ready code quality

### Threat Modeling
- **Canonical Source**: `.claude/modules/security/threat-modeling.md`
- **References**:
  - `CLAUDE.md` - Security quality gate
- **Purpose**: Security-first development approach

## Module Categories

### Quality Modules
- `critical-thinking.md` - Thinking enforcement
- `tdd.md` - Test-driven development
- `production-standards.md` - Production readiness
- `feature-validation.md` - Feature quality gates

### Security Modules
- `threat-modeling.md` - Security analysis
- `audit.md` - Security auditing
- `financial-compliance.md` - Financial security

### Development Modules
- `task-management.md` - Single-component tasks
- `research-analysis.md` - Research workflows
- `documentation.md` - Documentation standards

### Pattern Modules
- `multi-agent.md` - Agent coordination
- `session-management.md` - GitHub sessions
- `intelligent-routing.md` - Smart command routing
- `git-operations.md` - Git workflows
- `pattern-library.md` - Proven patterns

### Planning Modules
- `feature-workflow.md` - Feature development
- `prd-generation.md` - PRD creation
- `intelligent-prd.md` - Smart PRD patterns
- `mvp-strategy.md` - MVP planning

### Testing Modules
- `auto-testing.md` - Automated testing
- `iterative-testing.md` - Test iteration

## Command Delegation

### Core Commands
- `/auto` → `patterns/intelligent-routing.md`
- `/task` → `development/task-management.md`
- `/feature` → `planning/feature-workflow.md`
- `/swarm` → `patterns/multi-agent.md`
- `/query` → `development/research-analysis.md`
- `/session` → `patterns/session-management.md`

## Reference Rules

1. **Single Source**: Each concept has ONE canonical implementation
2. **Clear References**: All other mentions must reference the canonical source
3. **No Duplication**: Implementation details exist in only one place
4. **Documentation Pattern**: 
   - Modules contain implementation
   - Docs provide context, examples, and reference modules
   - CLAUDE.md provides brief summaries with references

## Validation

Run `python validate.py` to check:
- All module references are valid
- No circular dependencies
- No duplicate implementations
- All canonical sources exist

## Maintenance

When adding new concepts:
1. Choose appropriate module category
2. Create module with full implementation
3. Update this map with canonical source
4. Add references in CLAUDE.md if core concept
5. Create docs only for additional context/examples