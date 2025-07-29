# UltraThink: Adaptation Engine Architecture

## Fundamental Architectural Shift Required

Based on user alignment responses, this project requires transformation from a passive starter framework to an **active adaptation engine** built entirely within Claude Code.

## Key Architectural Requirements

### 1. Meta-Commands System
**Current State**: Static commands users copy and modify
**Required State**: Active adaptation commands that customize framework for specific projects

**Meta-Commands Needed**:
```
/adapt-to-project [project-type] [domain]
/configure-domain [web-dev|data-science|devops|custom]
/setup-project-config [project-name] [tech-stack]
/customize-tools [tool-preferences]
/replace-placeholders [config-file]
/generate-project-structure
```

### 2. Project Configuration XML System
**Purpose**: Central configuration that meta-commands read/write to customize behavior

**Structure**:
```xml
<project-config>
  <name>[INSERT_PROJECT_NAME]</name>
  <domain>[INSERT_DOMAIN]</domain>
  <tech-stack>[INSERT_TECH_STACK]</tech-stack>
  <tools>
    <preferred>[INSERT_PREFERRED_TOOLS]</preferred>
    <blocked>[INSERT_BLOCKED_TOOLS]</blocked>
  </tools>
  <customizations>
    <placeholders>
      <placeholder key="PROJECT_NAME" value="[TO_BE_REPLACED]"/>
      <placeholder key="DOMAIN" value="[TO_BE_REPLACED]"/>
    </placeholders>
  </customizations>
</project-config>
```

### 3. Dual Structure Implementation
**Reference Library**: Original framework commands preserved for ongoing reference
**Working Copy**: User's customized commands adapted to their specific project

**Directory Structure**:
```
user-project/
├── .claude/                    # User's customized working copy
│   ├── commands/              # Adapted for user's project
│   ├── components/            # Customized components
│   ├── context/               # Project-specific context
│   └── config/
│       └── project-config.yaml # User's configuration
├── .claude-framework/         # Reference library (git submodule)
│   ├── commands/              # Original templates with placeholders
│   ├── components/            # Original components
│   └── meta-commands/         # Adaptation commands
└── CLAUDE.md                  # User's project memory
```

### 4. Placeholder Replacement System
**Throughout Framework**: Commands contain standardized placeholders
**Meta-Commands**: Replace placeholders during adaptation process

**Standard Placeholders**:
- `[INSERT_PROJECT_NAME]`
- `[INSERT_DOMAIN]`
- `[INSERT_TECH_STACK]`
- `[INSERT_PREFERRED_TOOLS]`
- `[INSERT_COMPANY_NAME]`
- `[INSERT_TEAM_SIZE]`
- `[INSERT_WORKFLOW_TYPE]`

### 5. Multiple Integration Methods
**Git Submodule** (Recommended): Enables updates from framework
**Direct Clone**: Full copy for heavy customization
**Selective Copy**: Cherry-pick specific commands/components
**Guided Setup**: Interactive meta-commands walk through integration

### 6. Pure Claude Code Native Constraint
**Allowed Scripts**: Only `setup.sh`, `validate-demo.sh`, testing scripts
**Forbidden**: Python orchestration, workflow automation scripts
**Required**: All adaptation workflows as Claude Code slash commands

## Implementation Priority

### Phase 1: Meta-Commands Foundation
1. Create `/adapt-to-project` command with basic project type detection
2. Implement project-config.yaml system
3. Build placeholder replacement command `/replace-placeholders`

### Phase 2: Dual Structure
1. Modify setup.sh to create reference + working copy structure
2. Implement `/sync-from-reference` command for updates
3. Create `/backup-customizations` command

### Phase 3: Domain-Specific Adaptation
1. Build domain-specific adaptation commands (`/adapt-to-web-dev`, etc.)
2. Create component customization commands
3. Implement workflow-specific adaptations

### Phase 4: Community Integration
1. Create `/share-adaptation` command for community contributions
2. Build `/import-community-pattern` command
3. Implement adaptation example sharing system

## Success Metrics

- **User Onboarding**: From git clone to customized framework in <10 minutes
- **Adaptation Coverage**: 80%+ of commands automatically adapted to user's domain
- **Community Growth**: Users sharing adaptation patterns via GitHub
- **Update Compatibility**: Users can pull framework updates without losing customizations
- **Pure Claude Code**: All workflows executable within Claude Code environment

## Architecture Validation

This architecture ensures:
- ✅ Ready-to-use AND adaptable solutions
- ✅ Guided adaptation process built into framework
- ✅ Multiple integration approaches with user flexibility
- ✅ Dual structure: customized working copy + reference library
- ✅ Pure Claude Code native (no workflow scripts)
- ✅ Placeholder system for easy customization
- ✅ Community contribution pathways

---
*Analysis Date: 2025-07-27*
*Status: Architecture Requirements Defined*
*Next: Begin Phase 1 Implementation*