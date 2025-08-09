# Dual Workflow Documentation

This document explains the two distinct workflows for the Claude Code Context Engineering Framework:
1. **Transformation Workflow**: Converting THIS project from prompt library to framework
2. **Usage Workflow**: Using the framework as a git submodule in OTHER projects

## Workflow 1: Transformation (For Framework Developers)

### Purpose
Transform the Claude Code Modular Prompts project from a 88-command prompt library into a 35-command context engineering framework.

### Timeline
6 weeks of systematic transformation using specialized agents.

### Prerequisites
- Access to the full claude-code-modular-prompts repository
- Understanding of the current 88-command structure
- Commitment to 6-week transformation process

### Step-by-Step Transformation Workflow

#### Week 1: Foundation and Preparation
```bash
# Day 1-3: Context Engineering Foundation
/transformation-orchestrator "Begin Phase -1 context engineering setup"

# The orchestrator will:
# - Create .transformation/ directory structure
# - Set up transformation agents
# - Initialize migration tracking
# - Build context engineering foundation

# Day 4-5: Analysis and Cleanup Planning  
/migration-specialist "Analyze all 88 commands and 96 components"

# The specialist will:
# - Inventory existing commands
# - Identify reusable patterns
# - Plan migration to 35 commands
# - Create deprecation list
```

#### Week 2-5: Active Transformation
```bash
# Daily transformation routine
/transformation-orchestrator "Check daily progress"

# Week 2: Core Commands
/migration-specialist "Migrate Phase 0-1 commands"
/cleanup-coordinator "Archive migrated originals"

# Week 3: Context Engineering  
/migration-specialist "Migrate Phase 2-3 commands"
/context-engineer "Validate framework contexts"

# Week 4: Builders and Integration
/migration-specialist "Migrate Phase 4-5 commands"
/pattern-extractor "Extract verified patterns"

# Week 5: Team Features
/migration-specialist "Migrate Phase 6-7 commands"
/cleanup-coordinator "Final structure cleanup"
```

#### Week 6: Validation and Packaging
```bash
# Validate transformation
.transformation/scripts/validate-migration.sh

# Test dual-mode operation
/transformation-orchestrator "Run comprehensive tests"

# Package for submodule distribution
.submodule/package.sh

# Generate final reports
/transformation-orchestrator "Generate completion report"
```

### Transformation Agent Commands

```yaml
# Available during transformation only
transformation-agents:
  - /transformation-orchestrator  # Master coordinator
  - /migration-specialist        # Command migration
  - /cleanup-coordinator        # Structure cleanup
  
# These agents are NOT available after transformation
```

### Key Transformation Milestones

1. **Context Foundation Complete** (Week 1)
   - .claude/ restructured
   - Transformation tracking active
   - All agents operational

2. **Command Migration 50%** (Week 3)
   - Core commands migrated
   - Dual-mode testing begun
   - Pattern extraction started

3. **Framework Structure Complete** (Week 5)
   - All 35 commands migrated
   - Agents validated
   - Cleanup completed

4. **Submodule Ready** (Week 6)
   - Transformation artifacts removed
   - Package validated
   - Documentation complete

---

## Workflow 2: Usage (For End Users)

### Purpose
Use the Claude Code Context Engineering Framework to build research-driven, context-aware Claude Code setups for your projects.

### Prerequisites
- A project where you want to use Claude Code
- Git installed
- Basic command line knowledge

### Installation Workflow

#### Step 1: Add Framework as Submodule
```bash
# In your project root
git submodule add https://github.com/example/claude-framework .claude-framework
git submodule init
git submodule update

# Run setup
cd .claude-framework
./setup.sh --target=..
cd ..
```

#### Step 2: Initialize Context Engineering
```bash
# Start with environment verification
/.claude-framework/0_verify-environment

# Research your domain
/.claude-framework/1_research-domain

# The framework will guide you through:
# - Project analysis
# - Context hierarchy design  
# - Pattern extraction
# - Agent configuration
```

#### Step 3: Build Your Context Hierarchy
```bash
# Let the context engineer help
/context-engineer "Design optimal context structure for my project"

# This will:
# - Analyze your project structure
# - Create hierarchical CLAUDE.md files
# - Set up navigation patterns
# - Optimize for token limits
```

#### Step 4: Generate Specialized Agents
```bash
# Create project-specific agents
/3_agent-architect "Design agents for [your domain]"

# Examples:
# - Code review agent for your standards
# - Testing agent for your framework
# - Security agent for your requirements
# - Performance agent for your metrics
```

#### Step 5: Create Custom Commands
```bash
# Build workflow-specific commands
/4_command-workflow "Create command for [your workflow]"

# The builder will:
# - Use your researched patterns
# - Integrate with your context
# - Add anti-pattern prevention
# - Include your team standards
```

### Daily Usage Workflow

#### Morning Setup
```bash
# 1. Update research if needed
/research-validator "Check for new [framework] patterns"

# 2. Load your project context
/context-engineer "Load today's working context"

# 3. Start with your custom workflow
/my-custom-workflow "Begin daily development"
```

#### During Development
```yaml
# Your custom commands use the framework
available-commands:
  framework:
    - /0_verify-*      # Environment checks
    - /1_research-*    # Research tools
    - /2_context-*     # Context management
    - /3_agent-*       # Agent creation
    - /4_command-*     # Command building
  
  your-project:
    - /code-review     # Your standards
    - /test-suite      # Your testing
    - /deploy-check    # Your deployment
    - /team-update     # Your reporting
```

#### Continuous Improvement
```bash
# Weekly: Update patterns
/7_maintain-update "Refresh framework patterns"

# Monthly: Analyze usage
/7_maintain-analyze "Review command effectiveness"

# Quarterly: Major updates
git submodule update --remote
/.claude-framework/setup.sh --update
```

### Framework Agent Interactions

```yaml
# Always available framework agents
framework-agents:
  - /context-engineer      # Context optimization
  - /research-validator    # Pattern validation  
  - /pattern-extractor    # Code analysis
  - /discovery-navigator  # Feature discovery
  - /integration-assistant # Setup help

# Your project agents
project-agents:
  - /your-reviewer        # Your code standards
  - /your-tester         # Your test patterns
  - /your-documenter     # Your doc style
```

### Common Usage Patterns

#### Pattern 1: New Feature Development
```bash
# 1. Research best practices
/1_research-framework "New patterns for [feature type]"

# 2. Update context
/2_context-rules "Add new patterns to context"

# 3. Generate implementation
/your-feature-builder "Create [feature] using new patterns"
```

#### Pattern 2: Code Review Workflow
```bash
# 1. Load review context
/context-engineer "Load code review context"

# 2. Run specialized review
/your-reviewer "Review changes with [standards]"

# 3. Update patterns
/pattern-extractor "Extract new patterns from review"
```

#### Pattern 3: Team Onboarding
```bash
# 1. Generate onboarding
/6_team-onboarding "Create onboarding for [new member]"

# 2. Customize for role
/your-role-guide "Specialize for [role]"

# 3. Track progress
/your-progress-tracker "Monitor onboarding"
```

## Key Differences Summary

| Aspect | Transformation Workflow | Usage Workflow |
|--------|------------------------|----------------|
| **Purpose** | Convert THIS project | Use in YOUR project |
| **Duration** | 6 weeks | Ongoing |
| **Agents** | Transformation-specific | Framework + your agents |
| **Commands** | Migration focused | Development focused |
| **Directory** | Full repository | Submodule only |
| **Context** | Project transformation | Your project needs |
| **End Goal** | Create framework | Build better software |

## Workflow Transition

### From Transformation to Usage
When transformation completes:

1. **Remove Transformation Artifacts**
   ```bash
   rm -rf .transformation/
   rm .transformation/active
   ```

2. **Package Framework**
   ```bash
   .submodule/package.sh
   ```

3. **Test as Submodule**
   ```bash
   # In a test project
   git submodule add ./dist/claude-framework
   ```

4. **Document Changes**
   - Update README for users
   - Archive transformation docs
   - Publish framework version

### Success Indicators

**Transformation Success**:
- ✅ 35 framework commands working
- ✅ Dual-mode operation verified
- ✅ No data loss from original
- ✅ Clean separation achieved

**Usage Success**:
- ✅ Context hierarchy established
- ✅ Custom agents created
- ✅ Workflow commands built
- ✅ Team adoption successful

## Support Resources

### For Transformation
- Transformation orchestrator agent
- Migration progress tracking
- Daily standup logs
- Rollback procedures

### For Usage  
- Framework documentation
- Example implementations
- Community patterns
- Integration guides