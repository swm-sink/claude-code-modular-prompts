| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Command System Guide - Two-Tier Architecture

## Overview

The Claude Code Framework implements a **two-tier command system** designed to serve users at different experience levels and project complexity requirements:

1. **Simplified Commands** (Onboarding Tier) - `.claude/commands-simplified/`
2. **Full Framework Commands** (Production Tier) - `.claude/commands/`

---

## Two-Tier Architecture

### Simplified Commands (Onboarding Tier)

**Location**: `.claude/commands-simplified/`
**Purpose**: Framework onboarding and learning
**Target Users**: New users, personal projects, quick tasks

**Key Characteristics**:
- Self-contained logic without complex dependencies
- Simple workflow descriptions (no complex XML)
- Basic quality checks without blocking enforcement
- Fast execution with minimal overhead
- Clear, actionable output

**Available Commands**:
- `/context-prime` - Project context establishment
- `/task` - Single task execution
- `/research` - Research & analysis
- `/feature` - Feature development
- `/review` - Code review & quality analysis
- `/debug` - Debugging & troubleshooting
- `/test` - Testing workflows
- `/refactor` - Code refactoring
- `/docs` - Documentation generation
- `/deploy` - Deployment workflows

### Full Framework Commands (Production Tier)

**Location**: `.claude/commands/`
**Purpose**: Production-grade development with advanced features
**Target Users**: Advanced users, complex projects, production systems

**Key Characteristics**:
- Complete framework integration with meta-prompting
- Advanced XML configuration and module orchestration
- Universal quality gates with blocking enforcement
- Multi-agent coordination capabilities
- Self-improving adaptive intelligence

**Available Commands**:
- `/auto` - Intelligent routing with TDD awareness
- `/task` - Single component work with strict TDD enforcement
- `/feature` - Complete feature with PRD & MVP
- `/swarm` - Complex multi-component coordination
- `/query` - Research-only with test-aware analysis
- `/docs` - Documentation with FOCUS framework integration
- `/session` - Session management with GitHub integration
- `/protocol` - Production standards enforcement

---

## User Journey & Progression

### Learning Path

**Phase 1: Onboarding (Simplified Commands)**
- Start with simplified commands to learn framework concepts
- Focus on core development workflows
- Build confidence with real projects
- Understand framework principles

**Phase 2: Skill Development**
- Use simplified commands for personal projects
- Experiment with different workflows
- Identify patterns and preferences
- Recognize when advanced features are needed

**Phase 3: Production Readiness (Full Framework)**
- Graduate to full framework for production systems
- Leverage advanced quality gates and TDD enforcement
- Utilize multi-agent coordination for complex projects
- Benefit from meta-prompting and adaptive capabilities

### Migration Indicators

**Use Simplified Commands When**:
- Learning the framework for the first time
- Working on personal projects or prototypes
- Performing straightforward development tasks
- Wanting faster, more direct execution
- Preferring simpler workflows

**Graduate to Full Framework When**:
- Working on production systems
- Needing strict quality gates and TDD enforcement
- Requiring multi-agent coordination
- Wanting meta-prompting and adaptive intelligence
- Managing complex module dependencies
- Needing advanced security and threat modeling

---

## Command Selection Guide

### By Project Type

**Personal Projects & Prototypes**
- Use: Simplified commands
- Why: Faster execution, less overhead, easier to understand

**Production Systems**
- Use: Full framework commands
- Why: Advanced quality gates, comprehensive testing, security validation

**Learning & Education**
- Use: Simplified commands
- Why: Gentle introduction, core concepts, immediate value

**Complex Enterprise Projects**
- Use: Full framework commands
- Why: Multi-agent coordination, advanced orchestration, production standards

### By Experience Level

**New to Framework**
- Start: Simplified commands
- Progress: Learn concepts → Build confidence → Identify needs → Graduate

**Experienced Framework User**
- Choose: Based on project needs
- Mix: Can use both tiers as appropriate

**Production Engineer**
- Primary: Full framework commands
- Secondary: Simplified for quick tasks

---

## Technical Architecture

### Simplified Commands Architecture

**Structure**: Self-contained command files
**Dependencies**: Minimal external dependencies
**Quality**: Basic quality checks
**Execution**: Direct workflow execution
**Output**: Clear, actionable results

**Example Structure**:
```
/commands-simplified/
├── context-prime.md    # Project context establishment
├── task.md            # Single task execution
├── feature.md         # Feature development
└── README.md          # Onboarding documentation
```

### Full Framework Architecture

**Structure**: Command-module delegation pattern
**Dependencies**: 108+ modules organized by domain
**Quality**: Universal quality gates with blocking enforcement
**Execution**: Module runtime engine with meta-prompting
**Output**: Comprehensive results with advanced analytics

**Example Structure**:
```
/commands/
├── auto.md           # Intelligent routing
├── task.md           # TDD-enforced development
├── swarm.md          # Multi-agent coordination
└── /modules/         # 108+ supporting modules
```

---

## Integration & Compatibility

### Shared Principles
- Both tiers follow same core development principles
- Consistent code quality standards
- Compatible output formats
- Shared documentation patterns

### Flexible Usage
- Can mix simplified and full commands as needed
- Smooth transition between tiers
- Knowledge gained applies to both systems
- No lock-in to either tier

### Framework Evolution
- Simplified commands serve as onboarding foundation
- Full framework provides production capabilities
- Both tiers evolve together
- Migration path preserved across versions

---

## Best Practices

### For New Users
1. **Start Simple**: Begin with simplified commands
2. **Learn Concepts**: Focus on understanding framework principles
3. **Build Projects**: Use simplified commands for real development
4. **Identify Needs**: Recognize when advanced features are needed
5. **Graduate Gradually**: Move to full framework when ready

### For Experienced Users
1. **Choose Appropriately**: Use the right tier for the task
2. **Mix Strategically**: Combine both tiers as needed
3. **Teach Others**: Help new users with onboarding tier
4. **Provide Feedback**: Improve both tiers based on usage

### For Project Teams
1. **Define Standards**: Establish when to use each tier
2. **Train Team**: Ensure everyone understands both systems
3. **Support Progression**: Help team members graduate when ready
4. **Maintain Quality**: Ensure both tiers meet project standards

---

## Support & Resources

### Documentation
- **Simplified Commands**: `.claude/commands-simplified/README.md`
- **Full Framework**: `.claude/README.md`
- **Framework Guide**: `docs/framework/README.md`
- **Getting Started**: `docs/GETTING_STARTED.md`

### Command References
- **Simplified**: Individual command documentation in `.claude/commands-simplified/`
- **Full Framework**: Individual command documentation in `.claude/commands/`
- **Selection Guide**: `docs/COMMAND_SELECTION_GUIDE.md`

### Community
- **Issues**: GitHub issues for questions and improvements
- **Discussions**: Framework evolution and best practices
- **Examples**: Real-world usage examples and patterns

---

## Future Evolution

### Planned Enhancements
- **Improved Onboarding**: Enhanced learning materials and tutorials
- **Better Progression**: Clearer migration paths and indicators
- **Advanced Features**: New capabilities in both tiers
- **Performance**: Continued optimization and efficiency improvements

### Feedback Integration
- **User Experience**: Continuous improvement based on usage patterns
- **Feature Requests**: Community-driven enhancement priorities
- **Best Practices**: Evolving recommendations and patterns
- **Documentation**: Ongoing improvement and expansion

The two-tier command system represents a mature approach to framework design, balancing accessibility for new users with powerful capabilities for production systems.