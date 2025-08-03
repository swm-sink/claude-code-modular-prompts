# Command Context Loading Example

## Overview
This example shows how scaffolding commands will load context from the Claude Code context engineering structure and work with agents.

## Enhanced Command Structure

### Before: Static Command
```markdown
---
name: 1_research-framework
description: Research framework-specific best practices
allowed-tools: [Read, Write, WebSearch]
---

# Static command content...
```

### After: Context-Aware Command with Agent Integration
```markdown
---
name: 1_research-framework
description: Research framework-specific best practices through web search
allowed-tools: [Read, Write, WebSearch, Grep]
context-loading:
  primary: .claude/context/research-protocols.md
  secondary: 
    - .claude/context/verify-protocol.md
    - .claude/context/source-validation-standards.md
  domain: .claude/domains/technical/framework-patterns.md
  memory: .claude/memory/research-history.md
  examples: .claude/examples/research-outputs/
agents:
  research-validator: Primary research execution
  quality-guardian: Anti-pattern prevention
  memory-keeper: Decision tracking
---

# Framework Pattern Research Command

## 🧠 Context Loading Phase
$CONTEXT_LOADER_START$
Loading research context from:
- Research protocols: Understanding how to conduct evidence-based research
- Domain patterns: Existing framework knowledge in technical domain
- Memory: Previous research decisions and learnings
$CONTEXT_LOADER_END$

## 🤖 Agent Delegation
@research-validator: Please conduct framework-specific research following loaded protocols

## Step 1: Framework Detection (Enhanced)
Using context from technical domain:
$LOAD_CONTEXT: .claude/domains/technical/framework-detection.md$

[Framework detection logic using loaded patterns]

## Step 2: Research Execution
@research-validator will:
1. Use queries from: $CONTEXT: .claude/research/query-templates/framework-queries.md$
2. Validate sources per: $CONTEXT: verify-protocol$
3. Track findings in: $MEMORY: research-history$

## Step 3: Anti-Pattern Prevention
@quality-guardian: Validate research results against:
$LOAD_CONTEXT: .claude/context/llm-antipatterns.md$

## Step 4: Memory Update
@memory-keeper: Track in memory system:
- Decision rationale: Why these patterns were selected
- Sources found: All validated sources
- Conflicts resolved: How disagreements were handled

## Output Generation (Context-Aware)
Generate output using templates from:
$LOAD_CONTEXT: .claude/context/output-templates/research-report.md$

Create files in:
- `.claude/research/framework-patterns.md` (with citations)
- `.claude/domains/technical/validated-patterns.md` (for reuse)
- `.claude/memory/framework-decisions.md` (rationale)
```

## Context Loading Mechanism

### How $CONTEXT_LOADER$ Works
When a command includes context-loading in YAML frontmatter:
1. Agent reads the context-loading specification
2. Loads files in order (primary → secondary → domain → memory)
3. Makes content available to command execution
4. Tracks what context was used

### Dynamic Context Loading
```yaml
# During command execution
$LOAD_CONTEXT: path/to/specific/context.md$
# Loads context inline when needed

$CONTEXT: context-key$
# References pre-loaded context by key
```

### Memory Integration
```yaml
$MEMORY: memory-key$
# Reads from memory system

$UPDATE_MEMORY: memory-key$
# Writes to memory system
```

## Agent Integration Patterns

### Pattern 1: Sequential Delegation
```markdown
## Workflow
1. @context-engineer: Set up required structures
2. @research-validator: Conduct research  
3. @quality-guardian: Validate quality
4. @memory-keeper: Track decisions
```

### Pattern 2: Parallel Coordination
```markdown
## Parallel Tasks
@research-validator + @quality-guardian:
- Research executes while quality monitors
- Real-time anti-pattern prevention
- Immediate feedback loop
```

### Pattern 3: Hierarchical Orchestration
```markdown
## Orchestration
@transformation-orchestrator:
  ├── @context-engineer: Phase setup
  ├── @command-builder: Create commands
  │   ├── @research-validator: Evidence
  │   └── @quality-guardian: Validation
  └── @memory-keeper: Track everything
```

## Real-World Example: Creating a Testing Command

### Step 1: Orchestrator Initiates
```markdown
@transformation-orchestrator: Create testing research command for Phase 1
```

### Step 2: Command Builder Responds
```markdown
@command-builder: 
Loading templates from: .claude/context/command-templates/research-template.md
Creating: 1_research-testing.md
```

### Step 3: Context Integration
```yaml
context-loading:
  primary: .claude/context/testing-best-practices.md
  domain: .claude/domains/technical/testing-patterns.md
  antipatterns: .claude/context/testing-antipatterns.md
```

### Step 4: Research Integration
```markdown
@research-validator:
Searching for: "jest best practices 2024", "react testing library patterns"
Validating sources...
Found: 5 authoritative sources
```

### Step 5: Quality Validation
```markdown
@quality-guardian:
✓ No hallucination detected
✓ All claims have sources
✓ Anti-patterns prevented
✓ Naming convention followed
```

### Step 6: Memory Update
```markdown
@memory-keeper:
Logged: Testing command creation
Rationale: Jest + RTL standard for React
Sources: [5 sources tracked]
```

## Benefits of Context-Aware Commands

1. **Consistency**: All commands use the same context
2. **Reusability**: Context updates benefit all commands
3. **Traceability**: Know what context influenced decisions
4. **Quality**: Multiple validation layers
5. **Learning**: System improves through memory
6. **Efficiency**: No context duplication

## Implementation Notes

### For AI Assistant
When implementing commands:
1. Always include context-loading in frontmatter
2. Use $CONTEXT_LOADER$ markers for clarity
3. Delegate to appropriate agents
4. Update memory after significant actions
5. Load only necessary context (token efficiency)

### For Users
When using the system:
1. Agents handle complexity automatically
2. Context loads based on your task
3. Quality is enforced throughout
4. Decisions are tracked for transparency
5. System learns and improves

This context-aware approach transforms static commands into intelligent, adaptive tools that leverage the full power of Claude Code's context engineering system.