---
name: /generate-context
description: Generate multi-file hierarchical context system for project-specific Claude intelligence
usage: "/generate-context [--phase=technical-analysis|domain-intelligence|complete] [--project-path=path] [--with-validation] [--enhance-claude-md] [--save-state]"
allowed-tools: [Read, Write, Edit, LS, Glob, Grep, TodoWrite]
category: context-generation
version: "1.0"
---

# Generate Context: Create Project-Specific Claude Intelligence

## Purpose
This command generates a comprehensive multi-file hierarchical context system that transforms Claude into a specialized expert for your specific project through systematic context engineering.

## 🎯 Context Generation Phases

### Technical Analysis Phase
Generates deep technical architecture context:
- **Framework Detection**: Identify and document project frameworks and patterns
- **Project Structure**: Map directory organization and file relationships  
- **Development Patterns**: Extract coding conventions and architectural decisions
- **Quality Standards**: Document testing, linting, and quality requirements

### Domain Intelligence Phase  
Extracts business domain knowledge and terminology:
- **Business Domain**: Industry-specific terminology and concepts
- **User Workflows**: How users interact with the application
- **Data Models**: Key entities, relationships, and business logic
- **Integration Patterns**: APIs, services, and external dependencies

### Complete Generation
Full context system with navigation and validation:
- **Navigation System**: Cross-references and file relationships
- **Context Validation**: Before/after effectiveness demonstrations
- **Enhanced CLAUDE.md**: Project memory integration
- **Session State**: Support for future updates and improvements

## 🔧 Implementation

```bash
# Technical Analysis Only
/generate-context --phase=technical-analysis --project-path="."

# Domain Intelligence Only  
/generate-context --phase=domain-intelligence --project-path="."

# Complete Context Generation with Validation
/generate-context --complete --with-validation --enhance-claude-md --project-path="."

# With Session State Saving
/generate-context --complete --save-state --project-path="."
```

## 📁 Generated Context Structure

```
.claude/
├── context/
│   ├── technical-architecture.md      # Framework detection and patterns
│   ├── framework-detection.md         # Specific framework usage patterns
│   ├── project-structure.md          # Directory organization mapping
│   ├── development-patterns.md       # Coding conventions and standards
│   ├── business-domain.md            # Industry terminology and concepts  
│   ├── user-workflows.md             # User interaction patterns
│   ├── data-models.md                # Key entities and relationships
│   ├── integration-patterns.md       # API and service patterns
│   ├── navigation-index.md           # Context file relationships
│   ├── context-hierarchy.md          # Context organization structure
│   ├── cross-references.md           # Inter-file relationships
│   ├── validation-metrics.md         # Context effectiveness measures
│   ├── before-after-examples.md      # Claude response improvements
│   └── effectiveness-tests.md        # Context validation tests
└── context-generation-state.json     # Session state for resume/update
```

## 🎛️ Interactive Approval System

The context generation process includes interactive approval at each step:

1. **Preview Phase**: Show what will be generated before creation
2. **User Approval**: Confirm each context file before writing
3. **Modification Support**: Allow user edits and customizations
4. **Validation Demo**: Show before/after Claude response examples
5. **Final Review**: Complete context system overview and approval

## 🔗 Integration

### Session State Management
- Integrates with `/manage-session-state` for pause/resume
- Saves generation progress to `.claude/context-generation-state.json`
- Supports incremental updates and improvements

### Agent Coordination
- Works with `/coordinate-agents` for specialized analysis
- Each generation phase can be handled by specialized agents
- Supports parallel processing for comprehensive analysis

### Enhanced CLAUDE.md
- Optionally updates project CLAUDE.md with context references
- Adds navigation patterns and context architecture
- Maintains project memory consistency

## 🧪 Context Validation

Generated context includes effectiveness validation:
- **Before/After Examples**: Demonstrate Claude response improvements
- **Validation Metrics**: Measure context impact on task completion
- **Continuous Testing**: Framework for ongoing context validation
- **User Feedback Integration**: Collect and integrate user experience data

## 🚀 Execution Logic

### Phase 1: Project Analysis
1. **Directory Scanning**: Map project structure and file patterns
2. **Framework Detection**: Identify package.json, requirements.txt, etc.
3. **Code Pattern Analysis**: Extract coding conventions and standards
4. **Documentation Review**: Analyze existing documentation patterns

### Phase 2: Context Generation
1. **File Creation**: Generate context files based on analysis
2. **Content Population**: Fill context with project-specific intelligence
3. **Cross-Reference Building**: Create navigation and relationship mapping
4. **Validation Preparation**: Set up effectiveness testing framework

### Phase 3: Integration & Validation
1. **CLAUDE.md Enhancement**: Integrate context with project memory
2. **Session State Saving**: Enable future updates and improvements  
3. **Effectiveness Testing**: Demonstrate context impact on Claude responses
4. **User Approval Workflow**: Interactive confirmation and customization

## 🎯 Success Criteria

Context generation is successful when:
- All required context files are created with project-specific content
- Navigation system enables efficient context discovery
- Claude responses demonstrate clear improvement with context
- User approves final context system and effectiveness validation
- Session state enables future context updates and maintenance

## ⚠️ Error Handling

- **Missing Project Path**: Default to current directory with confirmation
- **Insufficient Project Data**: Generate basic template with user input prompts
- **File Creation Errors**: Graceful fallback with error reporting
- **User Cancellation**: Save partial progress and enable resume
- **Validation Failures**: Provide improvement suggestions and retry options

## 🚀 AUTO-EXECUTION LOGIC

When this command is invoked, the following logic executes automatically:

### Step 1: Project Analysis
```bash
# Analyze project structure and detect frameworks
project_path="${1:-.}"
echo "🔍 Analyzing project at: $project_path"

# Create .claude/context directory
mkdir -p "$project_path/.claude/context"

# Detect project type
if [ -f "$project_path/package.json" ]; then
    framework="Node.js/JavaScript"
elif [ -f "$project_path/requirements.txt" ] || [ -f "$project_path/pyproject.toml" ]; then
    framework="Python"
elif [ -f "$project_path/pom.xml" ] || [ -f "$project_path/build.gradle" ]; then
    framework="Java"
else
    framework="Generic"
fi

echo "📦 Detected framework: $framework"
```

### Step 2: Generate Context Files
```bash
# Generate technical architecture context
cat > "$project_path/.claude/context/technical-architecture.md" << 'EOF'
# Technical Architecture Context

## Project Framework
- **Primary Framework**: [DETECTED_FRAMEWORK]
- **Language**: [DETECTED_LANGUAGE]
- **Architecture Pattern**: [DETECTED_PATTERN]

## Key Technical Decisions
- Framework choice rationale
- Architecture patterns used
- Performance considerations
- Scalability approach

## Development Environment
- Build tools and processes
- Testing framework and approach
- Deployment strategy
- Quality assurance tools
EOF

# Generate framework detection context
cat > "$project_path/.claude/context/framework-detection.md" << 'EOF'
# Framework Detection Context

## Detected Frameworks
- **Primary**: [FRAMEWORK_NAME]
- **Version**: [FRAMEWORK_VERSION]
- **Dependencies**: [KEY_DEPENDENCIES]

## Framework-Specific Patterns
- Code organization conventions
- Testing patterns
- Configuration management
- Build and deployment patterns
EOF

# Generate project structure context
cat > "$project_path/.claude/context/project-structure.md" << 'EOF'
# Project Structure Context

## Directory Organization
```
[PROJECT_ROOT]/
├── [KEY_DIRECTORIES]
├── [SOURCE_DIRECTORIES]  
├── [TEST_DIRECTORIES]
└── [CONFIG_DIRECTORIES]
```

## File Patterns
- Source code patterns
- Test file patterns
- Configuration file patterns
- Documentation patterns
EOF

# Generate development patterns context
cat > "$project_path/.claude/context/development-patterns.md" << 'EOF'
# Development Patterns Context

## Coding Conventions
- Naming conventions
- Code organization patterns
- Error handling patterns
- Logging patterns

## Quality Standards
- Code style requirements
- Testing requirements
- Documentation requirements
- Performance requirements
EOF
```

### Step 3: Generate Navigation System
```bash
# Generate navigation index
cat > "$project_path/.claude/context/navigation-index.md" << 'EOF'
# Context Navigation Index

## Context File Organization
- **Technical Context**: technical-architecture.md, framework-detection.md
- **Project Context**: project-structure.md, development-patterns.md
- **Business Context**: business-domain.md, user-workflows.md
- **Integration Context**: integration-patterns.md, data-models.md

## Context Relationships
- Technical → Project: Architecture influences structure
- Business → Integration: Domain drives integration patterns
- All contexts → Navigation: Cross-referenced for discovery
EOF

# Generate context hierarchy
cat > "$project_path/.claude/context/context-hierarchy.md" << 'EOF'
# Context Hierarchy

## Layer 1: Technical Foundation
- Framework detection and architecture
- Development environment and tools

## Layer 2: Project Organization  
- Structure and file patterns
- Coding conventions and standards

## Layer 3: Business Domain
- Domain terminology and concepts
- User workflows and requirements

## Layer 4: Integration Layer
- API patterns and data models
- External service integrations
EOF

# Generate cross-references
cat > "$project_path/.claude/context/cross-references.md" << 'EOF'
# Context Cross-References

## Reference Map
- technical-architecture.md → framework-detection.md
- project-structure.md → development-patterns.md
- business-domain.md → user-workflows.md
- data-models.md → integration-patterns.md

## Navigation Patterns
- Hub-and-spoke: navigation-index.md as central hub
- Hierarchical: context-hierarchy.md for layered access
- Cross-linked: cross-references.md for relationship discovery
EOF
```

### Step 4: Session State Integration
```bash
# Save context generation state
cat > "$project_path/.claude/context-generation-state.json" << 'EOF'
{
  "generation_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "project_path": "$project_path",
  "detected_framework": "$framework",
  "phases_completed": ["technical-analysis"],
  "files_generated": [
    "technical-architecture.md",
    "framework-detection.md", 
    "project-structure.md",
    "development-patterns.md",
    "navigation-index.md",
    "context-hierarchy.md",
    "cross-references.md"
  ],
  "next_phase": "domain-intelligence",
  "validation_status": "pending"
}
EOF

echo "✅ Context generation complete!"
echo "📁 Generated context files in: $project_path/.claude/context/"
echo "🔄 Session state saved for future updates"
```

### Step 5: Interactive Approval (Simulated)
```bash
echo "🎯 Context Generation Summary:"
echo "- Technical architecture context: ✅ Generated"
echo "- Framework detection context: ✅ Generated"  
echo "- Project structure context: ✅ Generated"
echo "- Development patterns context: ✅ Generated"
echo "- Navigation system: ✅ Generated"
echo "- Session state: ✅ Saved"
echo ""
echo "📋 Next Steps:"
echo "1. Review generated context files"
echo "2. Customize content for your specific project"
echo "3. Run /generate-context --phase=domain-intelligence for business context"
echo "4. Use /validate-context to test effectiveness"
```