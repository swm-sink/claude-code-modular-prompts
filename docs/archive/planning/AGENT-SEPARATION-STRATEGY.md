# Agent Separation Strategy: Transformation vs Framework

## Overview

This document defines the clear separation between transformation agents (Stage 1) and framework agents (Stage 2), ensuring no confusion about their roles and preventing accidental inclusion of transformation tools in the final submodule.

## Transformation Agents (Stage 1 Only)

**Location**: `.transformation/agents/`  
**Lifetime**: Active only during 6-week transformation  
**Distribution**: NEVER included in git submodule  

### 1. transformation-orchestrator.md

**Purpose**: Master coordinator for the entire 6-week transformation process.

**Responsibilities**:
- Track phase progression (Week 1-6)
- Coordinate other transformation agents
- Monitor migration progress
- Ensure cleanup completion
- Generate transformation reports

**Key Functions**:
```yaml
orchestration:
  phases:
    - phase-1: Context engineering foundation
    - phase-2: Command migration (88 → 35)
    - phase-3: Component transformation
    - phase-4: Directory restructuring
    - phase-5: Validation and testing
    - phase-6: Submodule preparation
  
  delegation:
    migration-tasks: migration-specialist
    cleanup-tasks: cleanup-coordinator
    validation-tasks: validation-inspector
```

### 2. migration-specialist.md

**Purpose**: Convert existing commands and components to new framework.

**Responsibilities**:
- Analyze 88 existing commands for patterns
- Transform to 35 framework commands
- Convert components to verified patterns
- Maintain transformation mapping
- Handle deprecation gracefully

**Migration Process**:
```yaml
migration:
  source: .claude/commands/  # 88 commands
  target: .claude/framework/commands/  # 35 commands
  
  transformations:
    - extract-patterns: Identify reusable patterns
    - verify-sources: Find authoritative references
    - create-framework: Build new command structure
    - map-relationships: Document transformations
```

### 3. cleanup-coordinator.md

**Purpose**: Remove obsolete files and reorganize structure.

**Responsibilities**:
- Identify files to remove
- Reorganize directory structure
- Archive deprecated content
- Validate cleanup completeness
- Maintain rollback capability

**Cleanup Strategy**:
```yaml
cleanup:
  phases:
    - identify: Mark obsolete files
    - archive: Move to .archive/
    - restructure: Reorganize directories
    - validate: Ensure nothing lost
    - finalize: Remove transformation artifacts
```

## Framework Agents (Stage 2 - Submodule)

**Location**: `.claude/framework/agents/`  
**Lifetime**: Permanent part of framework  
**Distribution**: INCLUDED in git submodule  

### 1. context-engineer.md

**Purpose**: Help users design and maintain context hierarchies.

**User-Facing Functions**:
- Analyze project structure
- Design optimal context hierarchy
- Create CLAUDE.md navigation hubs
- Implement file hop patterns
- Optimize for token limits

**Example Usage**:
```yaml
context-engineering:
  analyze: Scan project for natural boundaries
  design: Create hierarchical structure
  implement: Generate context files
  optimize: Fit within 200k tokens
  maintain: Update as project evolves
```

### 2. research-validator.md

**Purpose**: Execute web searches and validate sources.

**User-Facing Functions**:
- Perform targeted web searches
- Validate source authority
- Apply VERIFY protocol
- Track evidence chains
- Update pattern library

**Validation Process**:
```yaml
research:
  search: Query for best practices
  validate: Check source credibility
  extract: Pull relevant patterns
  verify: Cross-reference multiple sources
  integrate: Add to pattern library
```

### 3. pattern-extractor.md

**Purpose**: Extract patterns from codebases and generate contexts.

**User-Facing Functions**:
- Analyze codebase patterns
- Extract common structures
- Generate domain contexts
- Build example libraries
- Create anti-patterns

### 4. discovery-navigator.md

**Purpose**: Guide users through framework discovery and usage.

**User-Facing Functions**:
- Help users find relevant commands
- Suggest command sequences
- Guide through setup phases
- Provide contextual help
- Navigate complex workflows

### 5. integration-assistant.md

**Purpose**: Assist with framework integration into projects.

**User-Facing Functions**:
- Configure for parent projects
- Customize framework settings
- Set up git submodule
- Adapt to project needs
- Troubleshoot integration

## Key Differences

### Scope
- **Transformation**: Internal to THIS project's conversion
- **Framework**: External facing for ANY project

### Lifetime
- **Transformation**: 6 weeks only
- **Framework**: Permanent feature

### Distribution
- **Transformation**: Never leaves this repo
- **Framework**: Distributed via submodule

### Context Access
- **Transformation**: Access to old structure
- **Framework**: Access to new structure only

### User Interaction
- **Transformation**: No direct user interaction
- **Framework**: Direct user commands

## Implementation Guidelines

### 1. Clear Naming Convention
```
transformation-*.md  # Transformation agents
*-specialist.md      # Transformation specialists
*-coordinator.md     # Transformation coordinators

# vs

*-engineer.md        # Framework engineers
*-validator.md       # Framework validators
*-assistant.md       # Framework assistants
```

### 2. Directory Enforcement
```bash
# Transformation agents ONLY here
.transformation/agents/

# Framework agents ONLY here
.claude/framework/agents/
```

### 3. Context Loading
```yaml
# Transformation agent
context-sources:
  - .transformation/context/
  - .claude/  # Current structure
  
# Framework agent  
context-sources:
  - ${FRAMEWORK_ROOT}/context/
  - ${PARENT_PROJECT}/.claude/
```

### 4. Command Integration
```yaml
# Transformation commands reference transformation agents
agents:
  - transformation-orchestrator
  - migration-specialist
  
# Framework commands reference framework agents
agents:
  - context-engineer
  - research-validator
```

## Testing Strategy

### Transformation Agent Tests
1. Verify they work on THIS project structure
2. Test migration of actual commands
3. Validate cleanup doesn't break anything
4. Ensure proper archival

### Framework Agent Tests
1. Test in submodule configuration
2. Verify parent project integration
3. Test with various project types
4. Validate user interactions

## Common Pitfalls to Avoid

1. **Don't mix agent types** in the same directory
2. **Don't reference transformation agents** from framework commands
3. **Don't include transformation context** in framework
4. **Don't assume project structure** in framework agents
5. **Don't hardcode paths** in any agent

## Migration Completion Checklist

When transformation is complete:

- [ ] All transformation agents completed their work
- [ ] No framework code references transformation agents
- [ ] `.transformation/` directory can be safely removed
- [ ] Framework agents work in submodule context
- [ ] Documentation updated to reflect separation
- [ ] Tests pass without transformation agents