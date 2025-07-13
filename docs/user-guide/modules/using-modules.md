# Using Framework Modules - Practical Guide

> **Unlock the power of 108+ specialized modules that make the framework intelligent**

## 🎯 Understanding Modules

### What Are Modules?
Modules are specialized, self-contained units of functionality that commands orchestrate to accomplish tasks. Think of them as intelligent building blocks that handle specific aspects of development.

### Module Categories

The framework includes 108+ modules organized into categories:

1. **Quality Modules** (`system/quality/`)
   - TDD enforcement
   - Test coverage validation  
   - Code quality gates
   - Security validation

2. **Development Modules** (`development/`)
   - Task management
   - Feature planning
   - Multi-agent coordination
   - Research and analysis

3. **Pattern Modules** (`patterns/`)
   - Intelligent routing
   - Command chaining
   - Thinking patterns
   - Duplication prevention

4. **System Modules** (`system/`)
   - Session management
   - Context preservation
   - Git operations
   - File operations

5. **Domain Modules** (`domain/`)
   - Domain adaptation
   - Template orchestration
   - Wizard functionality

## 🔧 How Modules Work

### Command-Module Relationship

Commands are the interface, modules are the implementation:

```
User Input → Command → Module Orchestration → Result
           ↓
      /task "fix bug" → task-management.md → TDD cycle
                     → quality/tdd.md → enforcement
                     → git/operations.md → commits
```

### Module Composition

Modules work together through standardized interfaces:

```markdown
## Interface Contract
**Input**: What the module expects
**Output**: What the module produces
**Dependencies**: Other required modules
```

## 📚 Practical Module Usage

### Example 1: Quality Enforcement

When you use `/task`, multiple quality modules activate:

```bash
/task "add user validation"
```

**Modules Involved**:
- `quality/tdd.md` - Enforces test-first development
- `quality/test-coverage.md` - Validates 90%+ coverage
- `quality/universal-quality-gates.md` - Runs all quality checks
- `development/task-management.md` - Manages the task workflow

**Result**: Your code automatically follows TDD with quality validation

### Example 2: Research and Analysis

When you use `/query`, research modules activate:

```bash
/query "analyze authentication patterns"
```

**Modules Involved**:
- `development/research-analysis.md` - Research methodology
- `patterns/thinking-pattern-template.md` - Structured analysis
- `patterns/critical-thinking.md` - Deep analysis patterns

**Result**: Comprehensive analysis without code changes

### Example 3: Feature Development

When you use `/feature`, planning modules orchestrate:

```bash
/feature "shopping cart checkout"
```

**Modules Involved**:
- `development/planning/feature-workflow.md` - Feature planning
- `development/planning/prd-template.md` - PRD generation
- `quality/tdd.md` - Test-driven implementation
- `development/documentation.md` - Auto-documentation

**Result**: Complete feature with PRD, tests, and documentation

## 🎨 Module Composition Patterns

### Sequential Composition
Modules execute in order, each building on the previous:

```
research-analysis.md → feature-workflow.md → tdd.md → documentation.md
```

### Parallel Composition
Independent modules execute simultaneously:

```
┌─ security-validation.md
├─ performance-testing.md
└─ code-quality.md
```

### Conditional Composition
Modules activate based on context:

```
if (complexity > threshold):
    → multi-agent.md
else:
    → task-management.md
```

## 🛠️ Direct Module Integration

### Reading Module Documentation

Each module includes:
1. **Purpose Statement** - What it does
2. **Interface Contract** - Inputs/outputs
3. **Usage Examples** - Practical scenarios
4. **Integration Points** - How it connects

Example from `quality/tdd.md`:
```markdown
# Test-Driven Development (TDD) Enforcement

> **Purpose**: Enforce RED→GREEN→REFACTOR cycle for all development

## Interface Contract
**Input**: Development task description
**Output**: Code with tests, following TDD cycle
**Quality Gate**: BLOCKING - no code without tests
```

### Understanding Module Dependencies

Modules declare their dependencies:

```markdown
**Dependencies**:
- quality/test-coverage.md (for coverage validation)
- system/git/conventional-commits.md (for commit standards)
- patterns/critical-thinking.md (for design decisions)
```

## 🔄 Common Module Workflows

### Quality-First Development
```
1. critical-thinking.md - Analyze approach
2. tdd.md - Write failing tests  
3. task-management.md - Implement solution
4. test-coverage.md - Validate coverage
5. quality-gates.md - Final validation
```

### Research-Driven Development
```
1. research-analysis.md - Understand problem
2. pattern-analysis.md - Identify patterns
3. feature-workflow.md - Plan approach
4. multi-agent.md - Coordinate implementation
```

### Production Deployment
```
1. security-validation.md - Security checks
2. performance-testing.md - Performance validation
3. production-safety.md - Safety verification
4. rollback-procedures.md - Prepare rollback
```

## 💡 Module Best Practices

### 1. Let Commands Orchestrate
Don't try to invoke modules directly. Commands handle orchestration:
- ✅ Use: `/task "implement feature"`
- ❌ Don't: Try to call modules manually

### 2. Understand Module Categories
- **Quality**: Ensuring code standards
- **Development**: Building features
- **Patterns**: Reusable approaches
- **System**: Infrastructure and tooling

### 3. Trust Module Intelligence
Modules include sophisticated logic:
- Automatic dependency resolution
- Intelligent error handling
- Context-aware execution
- Quality enforcement

### 4. Leverage Module Composition
Complex tasks use multiple modules:
- Feature = Planning + TDD + Documentation
- Swarm = Multi-agent + Coordination + Git worktrees
- Protocol = All quality gates + Safety + Rollback

## 🔍 Exploring Available Modules

### Finding Modules
```bash
# List all module categories
ls .claude/modules/

# Explore specific category
ls .claude/modules/quality/

# Read module documentation
cat .claude/modules/development/task-management.md
```

### Module Categories Overview

**Quality Assurance** (`.claude/system/quality/`)
- `tdd.md` - Test-driven development
- `test-coverage.md` - Coverage enforcement
- `code-review.md` - Review standards
- `security-validation.md` - Security checks

**Development Tools** (`.claude/modules/development/`)
- `task-management.md` - Task execution
- `feature-workflow.md` - Feature development
- `multi-agent.md` - Complex coordination
- `research-analysis.md` - Code analysis

**Pattern Library** (`.claude/modules/patterns/`)
- `intelligent-routing.md` - Smart command routing
- `thinking-pattern-template.md` - Reasoning patterns
- `command-chaining.md` - Workflow composition
- `duplication-prevention.md` - DRY enforcement

**System Operations** (`.claude/system/`)
- `session-management.md` - Context preservation
- `git/operations.md` - Version control
- `rollback-procedures.md` - Recovery mechanisms
- `performance-monitoring.md` - Optimization

## 🚀 Advanced Module Usage

### Creating Module Chains
```bash
# Research → Plan → Execute chain
/chain "analyze and improve authentication system"
# Automatically chains: query → feature → task modules
```

### Module-Aware Commands
```bash
# Tell commands which modules to emphasize
/auto "improve performance" --focus=performance
# Prioritizes performance-related modules
```

### Custom Module Integration
See [Extending Framework](../../advanced/extending-framework.md) for creating custom modules that integrate with existing ones.

## ❓ Module FAQ

**Q: Can I modify existing modules?**
A: Yes, but test thoroughly. Modules are interdependent.

**Q: How do modules communicate?**
A: Through standardized interfaces and the module runtime engine.

**Q: Which modules are most important?**
A: Quality modules (TDD, coverage) and core development modules (task, feature).

**Q: How do I know which modules are active?**
A: Commands report their module usage. Use `/query` to analyze module activation.

---

**Next Steps**:
- Explore [Command-Module Integration](../commands/overview.md)
- Learn about [Module Composition Patterns](../../advanced/framework-architecture.md)
- Create [Custom Modules](../../advanced/extending-framework.md)