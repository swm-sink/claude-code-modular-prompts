# Submodule Command Adaptation Strategy

## Overview

This document explains how commands will detect and adapt to their execution context, working correctly whether they're running in the transformation environment or as a git submodule in a parent project.

## Path Resolution Strategy

### Environment Variables

```bash
# Automatically set by setup process
export CLAUDE_FRAMEWORK_ROOT="${BASH_SOURCE%/*}"  # Framework location
export CLAUDE_PARENT_PROJECT="$(cd ${CLAUDE_FRAMEWORK_ROOT}/../.. && pwd)"  # Parent project
export CLAUDE_EXECUTION_MODE="framework"  # or "transformation"
```

### Mode Detection Logic

Every command includes this detection preamble:

```bash
#!/bin/bash

# Detect execution mode
if [ -f "${BASH_SOURCE%/*}/../../../.transformation/active" ]; then
    # We're in transformation mode
    EXECUTION_MODE="transformation"
    PROJECT_ROOT="$(cd ${BASH_SOURCE%/*}/../../.. && pwd)"
    FRAMEWORK_ROOT="${PROJECT_ROOT}/.claude/framework"
    WORKING_DIR="${PROJECT_ROOT}"
else
    # We're in framework mode (submodule)
    EXECUTION_MODE="framework"
    FRAMEWORK_ROOT="$(cd ${BASH_SOURCE%/*}/../.. && pwd)"
    PROJECT_ROOT="$(cd ${FRAMEWORK_ROOT}/../.. && pwd)"
    WORKING_DIR="${PROJECT_ROOT}"
fi

# Load appropriate configuration
source "${FRAMEWORK_ROOT}/lib/context-loader.sh"
```

## Command Structure Updates

### Example: analyze-project.md

```yaml
---
name: analyze-project
description: Analyze project structure and patterns
allowed-tools: [Read, Glob, Grep, Task]
context-loading:
  dual-mode: true
  transformation:
    contexts:
      - ${FRAMEWORK_ROOT}/../../../.transformation/context/current-state.md
      - ${FRAMEWORK_ROOT}/../../../.transformation/context/migration-progress.md
    agents:
      - migration-specialist
  framework:
    contexts:
      - ${FRAMEWORK_ROOT}/context/templates/analysis-protocol.md
      - ${PROJECT_ROOT}/.claude/CLAUDE.md
    agents:
      - pattern-extractor
      - context-engineer
---

# Load context based on execution mode
if [ "$EXECUTION_MODE" = "transformation" ]; then
    echo "🔄 Analyzing Claude Code Modular Prompts for transformation..."
    ANALYZE_TARGET="$PROJECT_ROOT"
    CONTEXT_MODE="transformation"
else
    echo "🔍 Analyzing parent project structure..."
    ANALYZE_TARGET="$PROJECT_ROOT"
    CONTEXT_MODE="framework"
fi

# Load appropriate context
$CONTEXT_LOADER \
    --mode "$CONTEXT_MODE" \
    --command "analyze-project" \
    --target "$ANALYZE_TARGET"

# Execute analysis with proper scope
/task "Analyze the project at $ANALYZE_TARGET using the loaded context"
```

## Directory Mapping

### Transformation Mode Paths
```
Current Working Directory: /path/to/claude-code-modular-prompts
Framework Root: /path/to/claude-code-modular-prompts/.claude/framework
Project Root: /path/to/claude-code-modular-prompts
Context Sources:
  - .transformation/context/
  - .claude/project/
```

### Framework Mode Paths (Submodule)
```
Current Working Directory: /path/to/parent-project
Framework Root: /path/to/parent-project/.claude-framework/.claude/framework
Project Root: /path/to/parent-project
Context Sources:
  - .claude-framework/.claude/framework/context/
  - .claude/  # Parent project's context
```

## Command Categories and Adaptations

### 1. Analysis Commands (0_verify-*.md, 1_research-*.md)

**Adaptation Strategy**: Target parent project in framework mode

```bash
# Transformation mode: Analyze this framework
# Framework mode: Analyze parent project
ANALYZE_PATH="${EXECUTION_MODE:=framework}_target"
```

### 2. Context Commands (2_context-*.md)

**Adaptation Strategy**: Create context in appropriate location

```bash
# Transformation mode: .claude/project/
# Framework mode: ${PROJECT_ROOT}/.claude/
CONTEXT_OUTPUT="${EXECUTION_MODE}_context_path"
```

### 3. Agent Commands (3_agent-*.md)

**Adaptation Strategy**: Reference appropriate agent set

```bash
# Transformation mode: Use transformation agents
# Framework mode: Use framework agents
AGENT_DIR="${EXECUTION_MODE}_agents"
```

### 4. Builder Commands (4_command-*.md)

**Adaptation Strategy**: Build in correct directory

```bash
# Transformation mode: Build in .claude/framework/commands/
# Framework mode: Build in ${PROJECT_ROOT}/.claude/commands/
BUILD_DIR="${EXECUTION_MODE}_build_location"
```

## Integration Patterns

### Pattern 1: Context Loading
```yaml
context-loader:
  framework-mode:
    search-paths:
      - ${PROJECT_ROOT}/.claude/
      - ${FRAMEWORK_ROOT}/context/templates/
      - ${FRAMEWORK_ROOT}/context/patterns/
    merge-strategy: overlay  # Parent overrides framework
```

### Pattern 2: Agent Discovery
```yaml
agent-discovery:
  framework-mode:
    locations:
      - ${FRAMEWORK_ROOT}/agents/  # Framework agents
      - ${PROJECT_ROOT}/.claude/agents/  # Project-specific agents
    priority: project-first
```

### Pattern 3: Command Execution
```yaml
command-execution:
  framework-mode:
    working-directory: ${PROJECT_ROOT}
    context-root: ${PROJECT_ROOT}/.claude/
    framework-reference: ${FRAMEWORK_ROOT}
```

## Submodule Setup Process

### 1. Initial Integration
```bash
# In parent project
git submodule add https://github.com/example/claude-framework .claude-framework
cd .claude-framework
./setup.sh --mode=framework --target=..
```

### 2. Setup Script Actions
```bash
#!/bin/bash
# setup.sh

# Detect if we're a submodule
if [ -d .git ] && [ -f .git ]; then
    SUBMODULE_MODE=true
    PARENT_PROJECT="$(cd .. && pwd)"
fi

# Create framework symlinks
ln -s .claude-framework/.claude/framework/commands .claude/framework-commands

# Set up environment
cat > .claude/.framework-env <<EOF
CLAUDE_FRAMEWORK_ROOT="$(pwd)/.claude/framework"
CLAUDE_PARENT_PROJECT="$PARENT_PROJECT"
CLAUDE_EXECUTION_MODE="framework"
EOF
```

### 3. Parent Project Integration
```bash
# In parent's .claude/CLAUDE.md
## Framework Integration

This project uses the Claude Code Context Engineering Framework via git submodule.

Framework commands available at: .claude/framework-commands/
Framework agents available at: .claude-framework/.claude/framework/agents/
```

## Command Migration Checklist

For each command being migrated:

- [ ] Add mode detection logic
- [ ] Update paths to use variables
- [ ] Add dual-mode context loading
- [ ] Test in transformation mode
- [ ] Test in framework mode
- [ ] Update command metadata
- [ ] Document behavior differences

## Testing Strategy

### 1. Transformation Mode Tests
```bash
# Run from project root
export CLAUDE_EXECUTION_MODE=transformation
./.claude/framework/commands/core/analyze-project.md
# Should analyze THIS project
```

### 2. Framework Mode Tests
```bash
# Run from parent project with submodule
export CLAUDE_EXECUTION_MODE=framework
./.claude-framework/.claude/framework/commands/core/analyze-project.md
# Should analyze PARENT project
```

### 3. Path Resolution Tests
```bash
# Verify all paths resolve correctly
./tests/verify-paths.sh --mode=transformation
./tests/verify-paths.sh --mode=framework
```

## Common Pitfalls

1. **Hardcoded Paths**: Never use absolute paths or assume structure
2. **Mode Confusion**: Always check execution mode before operations
3. **Context Mixing**: Don't load transformation context in framework mode
4. **Agent References**: Use mode-appropriate agent sets
5. **Working Directory**: Always establish correct working directory

## Success Criteria

- [ ] All commands work in both modes
- [ ] No hardcoded paths remain
- [ ] Context loading respects mode
- [ ] Agent references are appropriate
- [ ] Tests pass in both modes
- [ ] Documentation reflects dual behavior