# Template Library Architecture

## Overview
This document defines the clear separation between the template library (reference) and user workspace (customized).

## Directory Structure

### Template Library (Reference)
```
.claude/                          # Template library root
├── TEMPLATE-LIBRARY-ARCHITECTURE.md  # This file
├── commands/                     # 102 command templates
│   ├── core/                    # 4 essential commands
│   ├── deprecated/              # 38 archived commands (organized)
│   ├── development/             # 12 development workflow commands
│   ├── devops/                  # 4 DevOps automation commands
│   ├── meta/                    # 8 guide/helper commands
│   ├── quality/                 # 10 testing & quality commands
│   ├── security/                # 4 security commands
│   ├── specialized/             # 3 specialized domain commands
│   ├── database/                # 4 database commands
│   ├── monitoring/              # 2 monitoring commands
│   ├── testing/                 # 2 dedicated testing commands
│   ├── web-dev/                 # 1 web development command
│   ├── data-science/            # 1 data science command
│   └── [root-level]/            # 13 orchestration & utility commands
├── components/                   # 72 reusable components (organized)
│   ├── actions/                 # 2 action components
│   ├── analysis/                # 2 analysis components
│   ├── constitutional/          # 5 safety & alignment components
│   ├── context/                 # 7 context management components
│   ├── git/                     # 2 git workflow components
│   ├── intelligence/            # 2 AI coordination components
│   ├── interaction/             # 2 user interaction components
│   ├── learning/                # 2 learning components
│   ├── meta/                    # 1 meta component
│   ├── optimization/            # 8 prompt optimization components
│   ├── orchestration/           # 7 workflow orchestration components
│   ├── performance/             # 2 performance components
│   ├── planning/                # 1 planning component
│   ├── quality/                 # 3 quality assurance components
│   ├── reasoning/               # 4 reasoning components
│   ├── reliability/             # 2 reliability components
│   ├── reporting/               # 1 reporting component
│   ├── security/                # 10 security components
│   ├── testing/                 # 3 testing components
│   ├── validation/              # 1 validation component
│   └── workflow/                # 4 workflow components
├── context/                     # Essential context files
├── config/                      # Configuration templates
├── docs/                        # Documentation
└── templates/                   # Command & component templates
```

### User Workspace (After Customization)
```
your-project/
├── .claude/                     # Customized working copy
│   ├── commands/               # Your selected & customized commands
│   ├── components/             # Your customized components
│   ├── context/                # Project-specific context
│   └── config/
│       └── project-config.yaml # Your project configuration
├── .claude-framework/          # Reference library (git submodule)
├── CLAUDE.md                   # Your project memory
└── tests/                      # Validation framework
```

## Key Architectural Principles

### 1. Clear Separation
- **Template Library**: Reference implementation with placeholders
- **User Workspace**: Customized copy with project-specific values

### 2. Organized Categories
- **Commands**: Grouped by functional domain (development, security, etc.)
- **Components**: Grouped by technical concern (context, security, etc.)
- **Deprecated**: Cleanly archived with preservation of functionality

### 3. Naming Conventions
- **Commands**: `/command-name` format, descriptive names
- **Components**: Technical domain prefixes, clear functionality names
- **Files**: Kebab-case naming throughout

### 4. Template vs Workspace Workflow
1. **Import**: Copy template library to project
2. **Customize**: Replace placeholders with project values
3. **Validate**: Verify customizations work
4. **Update**: Sync from reference when needed

## Component Organization Logic

### Functional Grouping
Components are organized by technical concern:
- **Context**: Managing Claude's understanding
- **Security**: Protection and validation
- **Orchestration**: Multi-step workflows
- **Optimization**: Performance and efficiency
- **Quality**: Testing and validation
- **Intelligence**: AI coordination patterns

### Usage Patterns
- **Single-use**: Components used in one context
- **Cross-cutting**: Components used across multiple domains
- **Framework**: Components that provide structure

## Template Library Maintenance

### Version Control
- Template library is version controlled
- User workspaces track template version
- Update process preserves customizations

### Quality Standards
- All templates have placeholder markers
- All components have clear interfaces
- All deprecated items are cleanly archived

---
*Architecture Version: 1.0*
*Last Updated: 2025-07-29*