---
name: navigate-context
description: Browse and explore multi-file hierarchical context system for efficient context discovery
usage: "navigate-context [layer|search|map|guide] [query]"
allowed-tools: [Read, LS, Glob, Grep, Write, Edit]
category: context
version: "1.0"
---

# Navigate Context: Intelligent Context Exploration System

## Purpose: Efficient Context Discovery & Exploration

The `/navigate-context` command provides intelligent navigation through your project's multi-file hierarchical context system. Instead of manually searching through context files, this command offers guided exploration, smart search, and contextual mapping to help you quickly find and understand relevant project context.

**Navigation Philosophy**: Guided over random, contextual over flat, efficient over exhaustive, useful over complete.

## 🗺️ Context Navigation Modes

### Layer Explorer Mode
**Usage**: `/navigate-context layer [1-5|foundation|domain|technical|workflow|agents]`

Navigate through the 5-layer context hierarchy with smart filtering and cross-references:

```
Layer 1 - Foundation (CLAUDE.md)
├── Project identity and core standards
├── Critical architectural decisions  
├── Navigation guide to other layers
└── Anti-patterns specific to this project

Layer 2 - Domain Context (.claude/context/domain/)
├── business-rules.md → Core domain logic
├── user-workflows.md → User journey patterns
├── terminology.md → Domain vocabulary
└── data-models.md → Key data structures

Layer 3 - Technical Context (.claude/context/technical/)
├── architecture.md → System architecture
├── frameworks.md → Framework patterns
├── deployment.md → Infrastructure
├── testing.md → Testing strategies
└── performance.md → Performance considerations

Layer 4 - Workflow Context (.claude/context/workflows/)
├── development.md → Dev standards
├── code-review.md → Review processes
├── deployment.md → Deployment procedures
├── troubleshooting.md → Common issues
└── onboarding.md → Team member guide

Layer 5 - Agent Context (.claude/context/agents/)
├── domain-expert.md → Business specialist
├── architect.md → Technical advisor
├── reviewer.md → Code review assistant
└── debugger.md → Troubleshooting specialist
```

### Smart Search Mode
**Usage**: `/navigate-context search "query"` or `/navigate-context search --type [domain|technical|workflow|agent]`

Intelligent context search with relevance ranking and cross-references:

```bash
# Search across all context
/navigate-context search "authentication"
# Returns ranked results from all layers with context

# Search specific context type
/navigate-context search --type technical "deployment"
# Focused search in technical context only

# Search with pattern matching
/navigate-context search --pattern "*.md" "user management"
# Pattern-based file filtering with content search
```

### Context Mapping Mode
**Usage**: `/navigate-context map [full|summary|dependencies]`

Visual context architecture mapping and relationship visualization:

```
Context Architecture Map:
CLAUDE.md (Foundation)
    ├── References: domain/business-rules.md
    ├── References: technical/architecture.md
    ├── References: workflows/development.md
    └── Navigation: All layers accessible

Domain Context (4 files)
    ├── business-rules.md ──→ data-models.md
    ├── user-workflows.md ──→ terminology.md
    └── Cross-references: technical/frameworks.md

Technical Context (5 files)
    ├── architecture.md ──→ deployment.md
    ├── frameworks.md ──→ testing.md
    └── Dependencies: domain/data-models.md

Workflow Context (5 files)
    ├── development.md ──→ code-review.md
    ├── deployment.md ──→ troubleshooting.md
    └── Integration: technical/architecture.md

Agent Context (4 files)
    ├── Specializations mapped to domain expertise
    ├── Technical capabilities mapped to stack
    └── Workflow integration for team processes
```

### Interactive Guide Mode
**Usage**: `/navigate-context guide [beginner|expert|task-focused]`

Guided context exploration based on user experience and current goals:

**Beginner Guide**: Step-by-step context discovery
1. "Start with Foundation context (CLAUDE.md) for project overview"
2. "Explore Domain context for business understanding"
3. "Review Technical context for implementation details"
4. "Check Workflow context for team processes"
5. "Use Agent context for specialized assistance"

**Expert Guide**: Power-user navigation shortcuts
- Quick layer hopping with context breadcrumbs
- Cross-reference following for deep exploration
- Multi-layer search with context intersection
- Custom navigation patterns for frequent workflows

**Task-Focused Guide**: Context relevant to specific tasks
- **Development Task**: Technical → Workflow → Domain
- **Code Review**: Workflow → Technical → Agent (reviewer)
- **Debugging**: Agent (debugger) → Technical → Workflow
- **Onboarding**: Foundation → Domain → Workflow (onboarding)

## 🔍 Advanced Navigation Features

### Context Breadcrumbs
Track your navigation path through context hierarchy:
```
Navigation Path: Foundation → Domain → business-rules.md → data-models.md
Quick Actions: [Back] [Up Level] [Jump to Technical] [Search Related]
```

### Cross-Reference Following
Intelligent link following between context files:
```
Current: technical/architecture.md
Cross-References Found:
├── domain/data-models.md (Referenced 3 times)
├── workflows/deployment.md (Referenced 2 times)
└── agents/architect.md (Specialization link)
Actions: [Follow Reference] [Show Context] [Add to Path]
```

### Context Intersection
Find context overlap and relationships:
```bash
/navigate-context search --intersect "authentication" "user management"
# Shows context files that contain both concepts

/navigate-context map --intersect domain technical
# Shows cross-references between domain and technical layers
```

### Navigation History
Track frequently accessed context for optimization:
```
Most Accessed Context (Last 7 days):
1. technical/architecture.md (12 visits)
2. domain/business-rules.md (8 visits)
3. workflows/development.md (6 visits)

Suggested Shortcuts: [Pin Favorites] [Create Custom Path] [Export History]
```

## 💡 Smart Navigation Patterns

### Hub-and-Spoke Navigation
Central navigation from Foundation context with efficient access to all specialized areas.

### Dependency-First Navigation  
Navigate through context based on dependency relationships rather than hierarchy.

### Task-Oriented Navigation
Context paths optimized for common development tasks and workflows.

### Progressive Disclosure Navigation
Start with high-level context and progressively drill down to specific details.

## 📊 Navigation Analytics

### Context Usage Metrics
- **Access Patterns**: Which context files are used most frequently
- **Path Analysis**: Common navigation routes through context hierarchy
- **Search Queries**: Most frequent context searches and their effectiveness
- **Cross-Reference Usage**: How often links between context files are followed

### Navigation Optimization
- **Shortcut Suggestions**: Recommend custom navigation paths based on usage
- **Context Prioritization**: Surface most relevant context first
- **Missing Links**: Identify gaps in cross-references between related context
- **Load Time Optimization**: Cache frequently accessed context for faster navigation

## 🔧 Integration with Context System

### Session State Integration
Navigation state persists across Claude Code sessions:
```json
{
  "current_path": ["foundation", "domain", "business-rules"],
  "navigation_history": [...],
  "pinned_context": [...],
  "search_history": [...]
}
```

### Context Generation Integration
Navigation patterns inform context architecture improvements:
- **Usage Analytics** → Context file organization
- **Search Patterns** → Cross-reference optimization
- **Navigation Paths** → Hierarchy refinement
- **Access Frequency** → Loading priority optimization

### Command Integration
Navigation seamlessly integrates with other context commands:
- `/test-context` can validate discovered context effectiveness
- `/update-context` can modify context found through navigation
- `/optimize-context` uses navigation analytics for improvements
- `/context-status` includes navigation health metrics

## 🚀 Usage Examples

### Quick Context Overview
```bash
/navigate-context layer
# Shows all context layers with file counts and descriptions
```

### Find Authentication Context
```bash
/navigate-context search "authentication"
# Searches all context files for authentication-related content
# Returns ranked results with file locations and relevant excerpts
```

### Explore Technical Architecture
```bash
/navigate-context layer technical
# Lists all technical context files with descriptions
# Shows cross-references to other layers
# Provides quick access actions for each file
```

### Map Context Dependencies
```bash
/navigate-context map dependencies
# Shows visual map of context file dependencies
# Identifies critical context files with many references
# Suggests optimization opportunities
```

### Beginner Context Tour
```bash
/navigate-context guide beginner
# Provides step-by-step context exploration
# Explains each layer and its purpose
# Gives recommendations for next steps
```

## 🎯 Success Metrics

**Navigation Efficiency**:
- Time to find relevant context (target: <30 seconds)
- Navigation path optimization (shortest path to goal)
- Context discovery success rate (find what you're looking for)
- User satisfaction with navigation experience

**Context Utilization**:
- Coverage of context files (how much context is actually accessed)
- Cross-reference usage (are relationships being utilized)
- Context freshness (are users finding up-to-date information)
- Navigation pattern effectiveness (do common paths work well)

---

**Remember**: Context navigation should feel intuitive and efficient. The goal is to help users quickly find the exact context they need without getting lost in the hierarchy or overwhelmed by information.