# Progressive Disclosure Architecture Design

## Executive Summary

This document presents a transformative architecture that replaces the current 187-file, 261K-token framework with a progressive 3-tier system that starts at 20 lines and grows only as needed. Based on Phase 1 evidence showing 60% reduction potential and 75% user dropout, this design prioritizes immediate usability while preserving advanced capabilities for power users.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  Progressive Disclosure Tiers                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Tier 1: Framework Lite (Week 1)                           │
│  ├─ 20-line CLAUDE.md                                      │
│  ├─ 8 core commands                                        │
│  ├─ 5-minute setup                                         │
│  └─ ~5K tokens                                             │
│                      ↓ opt-in upgrade                       │
│  Tier 2: Framework Standard (Week 2-3)                     │
│  ├─ MCP integration                                         │
│  ├─ Enhanced patterns                                       │
│  ├─ Team features                                          │
│  └─ ~20K tokens                                            │
│                      ↓ opt-in upgrade                       │
│  Tier 3: Framework Pro (Month 2+)                          │
│  ├─ Full ecosystem                                         │
│  ├─ Meta-framework                                         │
│  ├─ Enterprise features                                     │
│  └─ ~50K tokens (80% reduction)                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Tier 1: Framework Lite (Week 1 Users)

### Core Design Principles
- **Zero Configuration**: Works immediately with sensible defaults
- **Native Integration**: Leverages Claude Code's built-in capabilities
- **Progressive Enhancement**: Each feature is an opt-in addition
- **Token Efficient**: <5K tokens total overhead

### Implementation Structure

```
project/
├── CLAUDE.md          # 20-line config
└── .claude/           # Optional enhancement directory
    └── upgrade.md     # Instructions for next tier
```

### CLAUDE.md Specification (20 lines)

```markdown
# Claude Code Configuration

## Commands
- `/task` - TDD development (test → implement → refactor)
- `/query` - Research and analysis
- `/feature` - Multi-file features with design docs
- `/fix` - Debug and fix issues
- `/docs` - Generate documentation
- `/review` - Code review and suggestions
- `/refactor` - Improve existing code
- `/test` - Add or improve tests

## Project Rules
- Test-first development enforced
- 90% coverage required
- Follow existing code style
- Atomic commits with clear messages

## Quick Start
1. Copy this file to your project root
2. Run: `/task "your first task"`
3. Upgrade: `/upgrade standard` (when ready)
```

### Command Implementations

Each command is a lightweight wrapper around Claude Code's native abilities:

```python
# Pseudo-implementation for /task command
def task_command(description):
    """
    Minimal implementation leveraging Claude's native TDD understanding
    """
    return f"""
    Implement this task using TDD:
    1. Write failing test first
    2. Implement minimal code to pass
    3. Refactor while keeping tests green
    4. Verify 90% coverage
    
    Task: {description}
    """
```

### Key Architectural Decisions

1. **No Module System**: Commands directly invoke Claude's capabilities
2. **No Complex State**: Leverages git for all state management
3. **No Custom Tools**: Uses Claude Code's native tool suite
4. **No Framework Code**: Pure prompt engineering

### Upgrade Mechanism

```markdown
# .claude/upgrade.md
To upgrade to Framework Standard:
1. Run: `/upgrade standard`
2. This will:
   - Install MCP tools for enhanced capabilities
   - Add team collaboration features
   - Enable advanced patterns
3. Rollback: `/downgrade lite`
```

## Tier 2: Framework Standard (Week 2-3 Users)

### Architecture Evolution

```
project/
├── CLAUDE.md              # Enhanced to 100 lines
├── .claude/
│   ├── config.json        # Project preferences
│   ├── patterns/          # Reusable patterns (5 files)
│   └── mcp/              # MCP tool definitions
└── .claude-mcp/          # MCP server configs
```

### Enhanced Features

1. **MCP Integration**
   - Custom tools for project-specific operations
   - Database access patterns
   - API integration templates
   - Build system integration

2. **Pattern Library** (5 essential patterns)
   - `tdd-enhanced.md` - Advanced TDD workflows
   - `review-checklist.md` - Comprehensive review criteria  
   - `performance-optimization.md` - Profiling and optimization
   - `security-patterns.md` - Security best practices
   - `deployment-patterns.md` - CI/CD integration

3. **Team Features**
   - Shared configuration via `.claude/config.json`
   - Consistent commit message formats
   - Code review workflows
   - Knowledge sharing patterns

### MCP Tool Architecture

```javascript
// .claude-mcp/tools/project-tools.js
export const tools = {
  runTests: {
    description: "Run project test suite with coverage",
    inputSchema: { testPattern: "string" },
    handler: async ({ testPattern }) => {
      // Delegates to project test runner
    }
  },
  checkQuality: {
    description: "Run linting, formatting, and quality checks",
    handler: async () => {
      // Integrates project quality tools
    }
  }
}
```

### Configuration Schema

```json
{
  "version": "2.0",
  "project": {
    "type": "typescript",
    "testRunner": "jest",
    "coverageThreshold": 90
  },
  "commands": {
    "task": {
      "enforeTDD": true,
      "autoCommit": true
    }
  },
  "team": {
    "commitFormat": "conventional",
    "reviewRequired": true
  }
}
```

## Tier 3: Framework Pro (Month 2+ Power Users)

### Full Ecosystem Architecture

```
project/
├── CLAUDE.md                    # Full configuration
├── .claude/
│   ├── config.json             # Advanced configuration
│   ├── patterns/               # 20 specialized patterns
│   ├── mcp/                    # Extended MCP tools
│   ├── workflows/              # Complex workflows
│   ├── meta/                   # Self-improving components
│   └── analytics/              # Usage analytics
└── .claude-mcp/               # Multiple MCP servers
    ├── tools/
    ├── memory/
    └── context/
```

### Advanced Capabilities

1. **Meta-Framework Features**
   - Self-optimizing prompts based on usage
   - Automated pattern extraction
   - Performance monitoring and optimization
   - Custom command creation

2. **Enterprise Integration**
   - JIRA/GitHub integration via MCP
   - Slack notifications
   - CI/CD pipeline integration
   - Compliance automation

3. **Advanced Workflows**
   - Multi-agent coordination
   - Parallel development branches
   - Automated refactoring campaigns
   - Architecture evolution tracking

### Token Optimization Strategy

Even at full capacity, the framework maintains efficiency:
- Lazy loading of patterns (load only when needed)
- Context-aware module selection
- Intelligent caching via MCP memory
- Total overhead: ~50K tokens (80% reduction from current)

## Migration Strategy

### Phase 1: Core Extraction (Week 1)
1. Extract 8 essential commands from current 20
2. Simplify each command to pure prompt
3. Remove all module dependencies
4. Create minimal CLAUDE.md

### Phase 2: Pattern Identification (Week 2)
1. Analyze usage patterns from current framework
2. Identify top 5 most-used patterns
3. Rewrite as standalone prompt templates
4. Package for Standard tier

### Phase 3: MCP Integration (Week 3)
1. Convert complex tools to MCP servers
2. Create project-specific tool definitions
3. Implement memory and context servers
4. Enable progressive loading

### Phase 4: Meta-Framework (Month 2)
1. Implement usage analytics
2. Create self-optimization pipeline
3. Enable custom command creation
4. Full ecosystem activation

## Integration Points

### Tier Boundaries
Each tier has clear integration contracts:

```typescript
interface TierUpgrade {
  from: 'lite' | 'standard' | 'pro';
  to: 'standard' | 'pro';
  preserves: string[];  // What carries forward
  adds: string[];       // New capabilities
  rollback: () => void; // Downgrade function
}
```

### Data Preservation
- Git history preserves all work
- Configuration migrates forward
- Patterns are additive, never destructive
- MCP tools are optional enhancements

### Rollback Mechanism
Every tier upgrade is reversible:

```bash
# Upgrade
/upgrade standard  # Lite → Standard
/upgrade pro      # Standard → Pro

# Downgrade  
/downgrade lite   # Any → Lite
/downgrade standard # Pro → Standard
```

## Performance Targets

### Framework Lite
- Setup: <5 minutes (copy one file)
- Command execution: <2 seconds
- Token overhead: <5K
- Learning curve: <10 minutes

### Framework Standard  
- Setup: <15 minutes (with MCP)
- Command execution: <3 seconds
- Token overhead: <20K
- Learning curve: <30 minutes

### Framework Pro
- Setup: <30 minutes (full ecosystem)
- Command execution: <5 seconds
- Token overhead: <50K
- Learning curve: 2-3 hours

## Implementation Roadmap

### Week 1: Framework Lite
- [ ] Create minimal CLAUDE.md
- [ ] Implement 8 core commands
- [ ] Test 5-minute setup
- [ ] Document upgrade path

### Week 2: Command Migration
- [ ] Convert patterns to prompts
- [ ] Create MCP tool definitions
- [ ] Implement configuration system
- [ ] Add team features

### Week 3: Integration Testing
- [ ] Test upgrade/downgrade flows
- [ ] Validate token efficiency
- [ ] Ensure data preservation
- [ ] Performance benchmarking

### Week 4: Pro Features
- [ ] Implement meta-framework
- [ ] Add analytics pipeline
- [ ] Create advanced workflows
- [ ] Complete documentation

## Success Metrics

1. **Adoption Rate**: 90% users complete Lite setup (vs 25% currently)
2. **Time to Value**: <5 minutes to first command (vs 4+ hours)
3. **Token Efficiency**: 80% reduction at Pro tier
4. **User Satisfaction**: Progressive complexity matches user growth
5. **Performance**: All commands execute <5 seconds

## Risk Mitigation

1. **Feature Parity**: Ensure Lite tier handles 80% of use cases
2. **Migration Friction**: Automated tooling for existing users
3. **Documentation**: Clear, progressive documentation at each tier
4. **Support**: Graceful degradation if advanced features fail
5. **Rollback**: Every change is reversible via git

## Conclusion

This Progressive Disclosure Architecture transforms an over-engineered 187-file framework into a elegant system that starts at 20 lines and grows only as needed. By leveraging Claude Code's native capabilities and modern MCP architecture, we achieve:

- 95% reduction in initial complexity
- 80% reduction in token usage
- 5-minute setup (from 4+ hours)
- Full feature preservation for power users
- Clear upgrade/downgrade paths

The architecture is ready for immediate implementation with atomic rollback points at each stage.