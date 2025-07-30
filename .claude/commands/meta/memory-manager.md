---
name: /memory-manager
description: "MCP-powered persistent memory and learning system for template automation"
usage: /memory-manager <action> [--scope=personal|project|team] [--export-path=<path>]
category: meta-commands  
tools: Read, Write, Edit, MultiEdit, Bash, LS, Glob
---

# MCP Memory Management System

**Persistent memory and intelligent learning for Claude Code template automation.**

## What This Enables (PERSISTENT INTELLIGENCE)

Transform your template library into a learning system that:
1. **Remembers your preferences** across all Claude Code sessions
2. **Learns from your usage patterns** to provide better suggestions
3. **Caches successful work** to avoid repeating similar tasks
4. **Adapts templates** based on your real-world usage data
5. **Shares team knowledge** while respecting privacy boundaries

## Core Memory Operations

### Initialize Memory System
```
/memory-manager init
```
Sets up MCP persistent memory structure with proper privacy controls and data organization.

### View Current Memory State
```
/memory-manager status
```
Shows comprehensive overview of:
- Session history and learning data
- User preferences and patterns
- Template performance metrics
- Cache status and storage usage

### Export Learning Data
```
/memory-manager export --path=./claude-memory-backup.json
```
Creates portable backup of all learning data, user patterns, and template metrics.

### Import Team Patterns
```
/memory-manager import team-standards.json --scope=team
```
Imports shared team patterns, coding standards, and proven template configurations.

## Memory Scopes and Privacy

### Personal Memory (Default)
```yaml
personal_memory:
  user_preferences:
    - preferred_tech_stacks: ["React", "Node.js", "PostgreSQL"]
    - communication_style: "detailed_with_examples"
    - specialist_preferences: ["architecture", "security"]
  
  success_patterns:
    - template_combinations: High-performing template sets
    - customization_patterns: Common modifications you make
    - workflow_preferences: Your typical development sequences
```

### Project Memory
```yaml
project_memory:
  current_project:
    name: "e-commerce-platform"
    type: "fullstack-web-app"
    tech_stack: ["React", "Node.js", "PostgreSQL", "Redis"]
    team_size: 5
    
  adaptation_history:
    - template_customizations: Project-specific template modifications
    - architecture_decisions: Recorded design choices and reasoning
    - performance_benchmarks: Template effectiveness for this project
```

### Team Memory (Shared)
```yaml
team_memory:
  shared_standards:
    code_style: "functional_react_with_hooks"
    testing_approach: "jest_rtl_comprehensive"
    deployment_pipeline: "github_actions_aws"
    
  collective_learning:
    successful_patterns: Team-validated template combinations
    avoided_antipatterns: Known problematic approaches
    quality_benchmarks: Team performance standards
```

## Intelligent Learning Features

### 1. Usage Pattern Recognition
```javascript
// System automatically learns from your behavior
const learnedPatterns = {
  "typical_workflow": [
    "/task 'create user auth'",
    "/api-create UserAuth", 
    "/test-generate auth.js",
    "/security-review auth"
  ],
  "success_indicators": {
    "rarely_modifies_generated_code": true,
    "high_satisfaction_ratings": 4.7,
    "consistent_tech_choices": ["TypeScript", "Jest", "PostgreSQL"]
  }
}
```

### 2. Predictive Suggestions
```
🧠 Based on your patterns, after creating an API endpoint you typically:
   1. Generate comprehensive tests (94% of the time)
   2. Add security validation (87% of the time)  
   3. Update API documentation (76% of the time)
   
   Should I prepare these follow-up commands?
```

### 3. Template Performance Tracking
```yaml
template_metrics:
  "/api-create":
    personal_success_rate: 0.92
    modification_frequency: 0.15
    user_satisfaction: 4.6
    improvement_suggestions:
      - "Add async/await error handling patterns"
      - "Include OpenAPI documentation generation"
```

## Advanced Memory Operations

### Memory Analytics
```
/memory-manager analyze
```
Provides insights like:
- Most effective template combinations for your projects
- Templates that consistently need modification (improvement candidates)
- Workflow patterns that lead to highest satisfaction
- Specialists that provide best results for your use cases

### Smart Cache Management
```
/memory-manager cache --action=optimize
```
Manages intelligent caching:
- Frequently accessed specialist work
- Reusable project analysis results
- Template customization patterns
- Framework detection results

### Learning Data Cleanup
```
/memory-manager cleanup --older-than=30days --low-confidence=true
```
Maintains memory quality by removing:
- Outdated patterns that no longer apply
- Low-confidence learning data
- Superseded template versions
- Unused cached results

## Memory-Powered Commands

### Context-Aware Template Suggestions
```
/memory-manager suggest "authentication system"

💭 Based on your history with auth systems:
   ✅ JWT + refresh tokens (used in 3 previous projects)
   ✅ PostgreSQL user table (your standard database)
   ✅ Express middleware pattern (matches your API style)
   ✅ Jest + Supertest testing (your testing preference)
   
   Confidence: 94% based on 847 similar decisions
```

### Personalized Command Enhancement
```
// When you run /api-create, memory system provides:
{
  "context_from_memory": {
    "your_typical_api_structure": "RESTful with middleware validation",
    "your_error_handling_pattern": "async/await with try-catch",
    "your_testing_approach": "unit + integration with 90%+ coverage",
    "your_documentation_style": "inline JSDoc + OpenAPI spec"
  }
}
```

### Intelligent Template Evolution
```
🔄 Template Evolution Alert:
   Template: /component-create
   Issue: 67% of users modify the generated PropTypes
   
   Proposed improvement:
   - Switch to TypeScript interfaces (matches your preference)
   - Add default props pattern (you add this 89% of the time)
   - Include accessibility attributes (team standard)
   
   Apply evolution? This will improve the template for everyone.
```

## Memory System Architecture

### Persistent Storage Structure
```
.claude/memory/
├── personal/
│   ├── preferences.json      # User preferences and patterns
│   ├── session-history.json  # Cross-session learning data
│   └── success-metrics.json  # Personal template effectiveness
├── project/
│   ├── context.json          # Current project state
│   ├── adaptations.json      # Project-specific customizations
│   └── architecture.json     # Design decisions and reasoning
├── team/
│   ├── standards.json        # Shared coding standards
│   ├── patterns.json         # Team-validated approaches
│   └── knowledge-base.json   # Collective learning
└── cache/
    ├── framework-analysis/   # Cached project analysis
    ├── specialist-work/      # Reusable specialist outputs
    └── template-results/     # Generated code examples
```

### Privacy and Security Controls
```yaml
privacy_controls:
  data_encryption: "AES-256 for all persistent data"
  access_isolation: "User-specific memory boundaries"
  sharing_controls: "Explicit opt-in for team sharing"
  retention_management: "Configurable data lifecycle"
  export_capability: "Full data portability"
```

## Integration with Template System

### Automatic Context Loading
Every Claude Code session automatically:
1. Loads your personal preferences and patterns
2. Retrieves relevant project context
3. Applies learned customizations to templates
4. Provides personalized suggestions and defaults

### Continuous Learning
System continuously learns from:
- Template usage frequency and satisfaction
- Code modifications you make to generated output
- Specialist combinations that work well for you
- Workflow patterns that lead to successful outcomes

### Quality Improvement Loop
```
User Experience → Usage Data → Learning Analysis → Template Enhancement → Better User Experience
```

## Team Collaboration Features

### Knowledge Sharing
```
/memory-manager share-pattern "React auth implementation" --team
```
Shares successful patterns with team while preserving individual privacy.

### Standard Enforcement
```
/memory-manager enforce-standards --source=team-memory
```
Applies team standards to template generation and validation.

### Collective Intelligence
```
/memory-manager insights --scope=team
```
Provides team-wide insights about template effectiveness and improvement opportunities.

---

## Ready for Intelligent Memory?

Transform your template library from static files into a learning, adapting system that becomes more valuable with every use.

**Example**: `/memory-manager init` to start building your personal AI assistant for development workflows.