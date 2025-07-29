# Template Library vs User Workspace Separation

## Overview
This document defines the clear architectural separation between the template library (reference implementation) and user workspaces (customized implementations).

## Core Concept

### Template Library (This Repository)
**Purpose**: Reference implementation with placeholders for customization
**Location**: `claude-code-modular-prompts` repository
**Usage**: Source of truth for templates and patterns

### User Workspace (Your Project)
**Purpose**: Customized implementation with project-specific values
**Location**: Your project directory
**Usage**: Working copy adapted to your specific needs

## Architectural Separation

### Template Library Structure
```
claude-code-modular-prompts/          # Template library root
├── .claude/                          # Template implementation
│   ├── TEMPLATE-LIBRARY-ARCHITECTURE.md
│   ├── commands/                     # 102 command templates with placeholders
│   │   ├── core/                    # Essential commands
│   │   ├── deprecated/              # 38 archived commands
│   │   ├── development/             # Development workflow
│   │   ├── meta/                    # Guide commands
│   │   └── [other categories]/      # Organized by domain
│   ├── components/                   # 72 reusable components
│   │   ├── security/                # Security components
│   │   ├── context/                 # Context management
│   │   ├── orchestration/           # Workflow components
│   │   └── [other categories]/      # Organized by function
│   ├── context/                     # Framework context files
│   ├── config/                      # Configuration templates
│   ├── docs/                        # Template documentation
│   └── templates/                   # Base templates
├── CLAUDE.md                        # Template library memory
├── setup.sh                         # Integration script
└── tests/                          # Template validation tests
```

### User Workspace Structure (After Setup)
```
your-project/                        # Your project root
├── .claude/                         # Your customized commands
│   ├── commands/                    # Selected & customized commands
│   │   ├── core/                   # Essential commands (customized)
│   │   ├── development/            # Your dev workflow (customized)
│   │   └── [selected categories]/ # Only categories you need
│   ├── components/                  # Your customized components
│   │   ├── security/               # Security components (customized)
│   │   ├── context/                # Context management (customized)
│   │   └── [selected categories]/ # Only components you use
│   ├── context/                    # Your project-specific context
│   └── config/
│       └── project-config.yaml     # Your project configuration
├── .claude-framework/              # Reference library (git submodule)
│   └── [complete template library] # Unchanged reference
├── CLAUDE.md                       # Your project memory
└── tests/                         # Your validation tests
```

## Integration Methods

### Method 1: Git Submodule (Recommended)
**Best for**: Projects that want to stay updated with template improvements
```bash
# Add template library as submodule
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Run setup to copy and customize
cd .claude-framework && ./setup.sh

# Result: Reference library + customized working copy
```

**Benefits**:
- Easy updates from template library
- Clear separation between reference and customization
- Version control of template versions

### Method 2: Direct Integration
**Best for**: Projects that want a one-time copy
```bash
# Clone template library
git clone https://github.com/swm-sink/claude-code-modular-prompts temp-templates

# Copy to your project
cp -r temp-templates/.claude .claude
rm -rf temp-templates

# Customize for your project
# (Manual find & replace of placeholders)
```

**Benefits**:
- Complete ownership of customized templates
- No external dependencies
- Full customization freedom

### Method 3: Selective Integration
**Best for**: Projects that only need specific commands/components
```bash
# Copy only what you need
mkdir -p .claude/commands/core
cp template-library/.claude/commands/core/task.md .claude/commands/core/
cp template-library/.claude/commands/development/dev.md .claude/commands/development/

# Customize selected templates
# (Manual replacement of placeholders)
```

**Benefits**:
- Minimal footprint
- Only include what you need
- Focused customization effort

## Customization Workflow

### Phase 1: Initial Setup
1. **Choose Integration Method** (Submodule, Direct, or Selective)
2. **Run Setup Script** (copies templates to your workspace)
3. **Get Customization Guide** using `/adapt-to-project` command

### Phase 2: Manual Customization
1. **Identify Placeholders** using `/replace-placeholders` command
2. **Create Project Config** (project-config.yaml)
3. **Find & Replace Placeholders** in your editor:
   - `[INSERT_PROJECT_NAME]` → Your project name
   - `[INSERT_DOMAIN]` → Your domain (web-dev, data-science, etc.)
   - `[INSERT_TECH_STACK]` → Your technology stack
   - `[INSERT_COMPANY_NAME]` → Your organization
   - `[INSERT_TEAM_SIZE]` → Your team size

### Phase 3: Validation
1. **Test Customized Commands** in Claude Code conversations
2. **Run Validation** using `/validate-adaptation` command
3. **Remove Unused Commands** and components
4. **Document Your Customizations**

### Phase 4: Maintenance
1. **Update from Reference** using `/sync-from-reference` command
2. **Merge Updates** with your customizations
3. **Test After Updates**
4. **Share Patterns** using `/share-adaptation` command

## Placeholder System

### Standard Placeholders
All templates use consistent placeholder markers:
- `[INSERT_PROJECT_NAME]` - Your project's name
- `[INSERT_DOMAIN]` - Your project domain (web-dev, data-science, enterprise, etc.)
- `[INSERT_TECH_STACK]` - Your primary technology stack
- `[INSERT_COMPANY_NAME]` - Your organization name
- `[INSERT_TEAM_SIZE]` - Your team size (solo, small, medium, large)
- `[INSERT_WORKFLOW_TYPE]` - Your workflow type (agile, waterfall, continuous, etc.)

### Context-Specific Placeholders
Some commands have specialized placeholders:
- `[INSERT_DATABASE_TYPE]` - Database technology
- `[INSERT_CLOUD_PROVIDER]` - Cloud platform
- `[INSERT_CI_PLATFORM]` - CI/CD platform
- `[INSERT_MONITORING_TOOL]` - Monitoring solution

### Configuration File Template
```yaml
# .claude/config/project-config.yaml
project_config:
  metadata:
    name: "[INSERT_PROJECT_NAME]"
    domain: "[INSERT_DOMAIN]"
    tech_stack: "[INSERT_TECH_STACK]"
    company: "[INSERT_COMPANY_NAME]"
    team_size: "[INSERT_TEAM_SIZE]"
    workflow_type: "[INSERT_WORKFLOW_TYPE]"
  
  placeholders:
    PROJECT_NAME: "[INSERT_PROJECT_NAME]"
    DOMAIN: "[INSERT_DOMAIN]"
    TECH_STACK: "[INSERT_TECH_STACK]"
    COMPANY_NAME: "[INSERT_COMPANY_NAME]"
    TEAM_SIZE: "[INSERT_TEAM_SIZE]"
    WORKFLOW_TYPE: "[INSERT_WORKFLOW_TYPE]"
    DATABASE_TYPE: "[INSERT_DATABASE_TYPE]"
    CLOUD_PROVIDER: "[INSERT_CLOUD_PROVIDER]"
    CI_PLATFORM: "[INSERT_CI_PLATFORM]"
    MONITORING_TOOL: "[INSERT_MONITORING_TOOL]"
```

**Note**: This configuration file is for documentation only. Claude Code commands cannot read YAML files - all customization must be done through manual find & replace.

## Update Management

### Staying Current with Template Library
When using git submodule method:
```bash
# Update reference library
cd .claude-framework
git pull origin main

# Get update guidance
/sync-from-reference

# Follow manual merge process
# (Commands provide step-by-step instructions)
```

### Handling Conflicts
When template updates conflict with your customizations:
1. **Review Changes** in reference library
2. **Identify Conflicts** with your customizations
3. **Merge Manually** keeping your project-specific values
4. **Test Thoroughly** after merge
5. **Document Changes** for future reference

## Best Practices

### Customization Guidelines
1. **Keep Reference Clean** - Never modify `.claude-framework/`
2. **Document Changes** - Track your customizations
3. **Test Regularly** - Validate commands work in your context
4. **Version Control** - Commit your customizations
5. **Share Patterns** - Document reusable customization patterns

### Workspace Organization
1. **Separate Concerns** - Keep templates and customizations separate
2. **Minimal Selection** - Only include commands you need
3. **Clear Naming** - Use consistent naming conventions
4. **Regular Cleanup** - Remove unused commands and components

### Update Strategy
1. **Regular Updates** - Stay current with template improvements
2. **Test Before Merge** - Always test updates in isolation
3. **Gradual Migration** - Update incrementally, not all at once
4. **Backup First** - Always backup before major updates

## Troubleshooting

### Common Issues
1. **Placeholder Not Replaced** - Use global find & replace in your editor
2. **Command Not Working** - Check placeholder replacements are complete
3. **Update Conflicts** - Follow conflict resolution process
4. **Missing Components** - Check component dependencies

### Support Resources
- **Guide Commands**: `/adapt-to-project`, `/validate-adaptation`, `/sync-from-reference`
- **Documentation**: Template library docs and context files
- **Examples**: Reference implementations in template library
- **Community**: Share patterns and solutions

---
*Documentation Version: 1.0*
*Last Updated: 2025-07-29*
*Template Library: claude-code-modular-prompts*