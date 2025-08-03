# Migration Strategy: Current Structure to Dual-Purpose Framework

## Overview

This document outlines the step-by-step migration process to transform the current Claude Code Modular Prompts structure into the dual-purpose framework that supports both transformation and submodule usage.

## Current State Analysis

### Existing Structure
```
claude-code-modular-prompts/
├── .claude/
│   ├── commands/         # 88 existing commands
│   ├── components/       # 96 components
│   ├── context/         # Context files
│   ├── docs/            # Documentation
│   └── ...
├── docs/
├── reports/
├── scripts/
└── ...
```

### Target Structure
```
claude-code-modular-prompts/
├── .transformation/      # NEW - Transformation tools
├── .claude/             
│   ├── framework/       # NEW - Submodule components
│   └── project/         # NEW - This project's context
├── .submodule/          # NEW - Integration helpers
└── [existing dirs]
```

## Migration Phases

### Phase 1: Preparation (Day 1)

#### 1.1 Create Migration Branches
```bash
# Create branches for safety
git checkout -b migration-backup
git checkout -b dual-purpose-migration

# Tag current state
git tag pre-migration-v1.0
```

#### 1.2 Create Transformation Infrastructure
```bash
# Create transformation directory
mkdir -p .transformation/{agents,commands,context,scripts}

# Create marker file
echo "active" > .transformation/active

# Create transformation context
cat > .transformation/context/migration-state.md << EOF
# Migration State Tracking

## Current Phase: Preparation
## Started: $(date)
## Status: Active

### Inventory
- Total Commands: 88
- Total Components: 96
- Migration Target: 35 commands
EOF
```

#### 1.3 Initialize Migration Tracking
```bash
# Create migration manifest
cat > .transformation/MIGRATION-MANIFEST.yaml << EOF
migration:
  version: 1.0
  started: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
  source_structure:
    commands: 88
    components: 96
  target_structure:
    framework_commands: 35
    transformation_agents: 3
    framework_agents: 5
  
  phases:
    - preparation: in_progress
    - restructuring: pending
    - command_migration: pending
    - agent_creation: pending
    - validation: pending
    - cleanup: pending
EOF
```

### Phase 2: Directory Restructuring (Day 2)

#### 2.1 Create New Directory Structure
```bash
# Create framework structure
mkdir -p .claude/framework/{agents,commands/{core,advanced},context/{templates,patterns,discovery}}
mkdir -p .claude/project/{domains,examples,memory}

# Create submodule helpers
mkdir -p .submodule/{templates,scripts}
```

#### 2.2 Move Project-Specific Content
```bash
# Move current CLAUDE.md to project-specific location
mv .claude/CLAUDE.md .claude/project/CLAUDE.md

# Create new framework CLAUDE.md
cat > .claude/framework/CLAUDE.md << EOF
# Claude Code Context Engineering Framework

This is the framework documentation for the git submodule distribution.
For project-specific context, see .claude/project/CLAUDE.md
EOF
```

#### 2.3 Set Up Dual-Path System
```bash
# Create path configuration
cat > .claude/framework/lib/paths.sh << EOF
#!/bin/bash

# Path resolution for dual-mode operation
get_framework_root() {
    echo "$(cd ${BASH_SOURCE%/*}/.. && pwd)"
}

get_project_root() {
    local framework_root=$(get_framework_root)
    if [ -f "$framework_root/../../.transformation/active" ]; then
        echo "$(cd $framework_root/../.. && pwd)"
    else
        echo "$(cd $framework_root/../../.. && pwd)"
    fi
}

get_execution_mode() {
    if [ -f "$(get_framework_root)/../../.transformation/active" ]; then
        echo "transformation"
    else
        echo "framework"
    fi
}
EOF
```

### Phase 3: Command Migration (Days 3-4)

#### 3.1 Analyze Existing Commands
```bash
# Run analysis agent
.transformation/agents/migration-specialist.md << EOF
Analyze all 88 commands in .claude/commands/
Identify patterns and group by function
Map to 35 target framework commands
Create migration plan for each command
EOF
```

#### 3.2 Create Command Migration Script
```python
#!/usr/bin/env python3
# .transformation/scripts/migrate-command.py

import yaml
import os
import re

def migrate_command(source_path, target_category):
    """Migrate a single command to framework structure"""
    
    # Read source command
    with open(source_path, 'r') as f:
        content = f.read()
    
    # Parse YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not yaml_match:
        return False
    
    frontmatter = yaml.safe_load(yaml_match.group(1))
    body = yaml_match.group(2)
    
    # Add dual-mode support
    frontmatter['context-loading'] = {
        'dual-mode': True,
        'transformation': {
            'contexts': ['${FRAMEWORK_ROOT}/../../.transformation/context/'],
            'agents': ['migration-specialist']
        },
        'framework': {
            'contexts': ['${FRAMEWORK_ROOT}/context/templates/'],
            'agents': ['context-engineer']
        }
    }
    
    # Add mode detection to body
    mode_detection = '''
# Detect execution mode
source "${BASH_SOURCE%/*}/../../lib/paths.sh"
EXECUTION_MODE=$(get_execution_mode)
PROJECT_ROOT=$(get_project_root)
FRAMEWORK_ROOT=$(get_framework_root)

# Load appropriate context
$CONTEXT_LOADER --mode "$EXECUTION_MODE"
'''
    
    # Reconstruct command
    new_content = f"---\n{yaml.dump(frontmatter)}---\n{mode_detection}\n{body}"
    
    # Write to target
    target_path = f".claude/framework/commands/{target_category}/{os.path.basename(source_path)}"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    with open(target_path, 'w') as f:
        f.write(new_content)
    
    return True

# Migration mapping
migration_map = {
    'core': ['task.md', 'help.md', 'project.md', ...],
    'advanced': ['analyze.md', 'generate.md', ...]
}

# Execute migration
for category, commands in migration_map.items():
    for command in commands:
        source = f".claude/commands/{command}"
        if os.path.exists(source):
            migrate_command(source, category)
            print(f"Migrated {command} to {category}")
```

#### 3.3 Migrate Commands Batch
```bash
# Run migration for all commands
python .transformation/scripts/migrate-command.py

# Verify migration
find .claude/framework/commands -name "*.md" | wc -l
# Should show 35
```

### Phase 4: Agent Creation (Day 5)

#### 4.1 Create Transformation Agents
```bash
# Create transformation orchestrator
cat > .transformation/agents/transformation-orchestrator.md << 'EOF'
---
name: transformation-orchestrator
description: Coordinates the 6-week transformation process
allowed-tools: [Read, Write, Task, Bash]
---

I am the transformation orchestrator. My role is to:
1. Track migration progress through all phases
2. Coordinate other transformation agents
3. Ensure no data loss during migration
4. Validate each transformation step
5. Generate progress reports

Current phase: $(cat .transformation/context/migration-state.md | grep "Current Phase" | cut -d: -f2)
EOF

# Create other transformation agents...
```

#### 4.2 Create Framework Agents
```bash
# Create context engineer
cat > .claude/framework/agents/context-engineer.md << 'EOF'
---
name: context-engineer
description: Helps design and maintain context hierarchies
allowed-tools: [Read, Write, Edit, Glob]
context-aware: true
---

I help users design optimal context hierarchies for their projects.

In framework mode, I:
1. Analyze the parent project structure
2. Design hierarchical CLAUDE.md files
3. Implement file hop patterns
4. Optimize for token limits
5. Create bidirectional navigation
EOF

# Create other framework agents...
```

### Phase 5: Validation (Day 6)

#### 5.1 Create Validation Suite
```bash
# Validation script
cat > .transformation/scripts/validate-migration.sh << 'EOF'
#!/bin/bash

echo "🔍 Validating Migration..."

# Check directory structure
echo "Checking directory structure..."
required_dirs=(
    ".transformation/agents"
    ".claude/framework/agents"
    ".claude/framework/commands/core"
    ".claude/framework/commands/advanced"
    ".claude/project"
    ".submodule"
)

for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir exists"
    else
        echo "❌ $dir missing"
        exit 1
    fi
done

# Check command count
framework_commands=$(find .claude/framework/commands -name "*.md" | wc -l)
if [ "$framework_commands" -eq 35 ]; then
    echo "✅ Framework commands: $framework_commands"
else
    echo "❌ Expected 35 commands, found $framework_commands"
    exit 1
fi

# Check agent count
trans_agents=$(find .transformation/agents -name "*.md" | wc -l)
frame_agents=$(find .claude/framework/agents -name "*.md" | wc -l)

echo "✅ Transformation agents: $trans_agents"
echo "✅ Framework agents: $frame_agents"

# Test mode detection
echo "Testing mode detection..."
source .claude/framework/lib/paths.sh
mode=$(get_execution_mode)
if [ "$mode" = "transformation" ]; then
    echo "✅ Mode detection: transformation"
else
    echo "❌ Mode detection failed"
    exit 1
fi

echo "✅ Migration validation complete!"
EOF

chmod +x .transformation/scripts/validate-migration.sh
.transformation/scripts/validate-migration.sh
```

#### 5.2 Test Dual-Mode Operation
```bash
# Test transformation mode
export CLAUDE_EXECUTION_MODE=transformation
.claude/framework/commands/core/analyze-project.md

# Simulate framework mode
mv .transformation/active .transformation/active.bak
export CLAUDE_EXECUTION_MODE=framework
.claude/framework/commands/core/analyze-project.md
mv .transformation/active.bak .transformation/active
```

### Phase 6: Cleanup and Finalization (Day 7)

#### 6.1 Archive Old Structure
```bash
# Create archive of old structure
mkdir -p .archive/pre-migration
mv .claude/commands .archive/pre-migration/
mv .claude/components .archive/pre-migration/

# Keep archive reference
cat > .archive/pre-migration/README.md << EOF
# Pre-Migration Archive

This directory contains the original structure before dual-purpose migration.
- Original Commands: 88
- Original Components: 96
- Migration Date: $(date)

These files are preserved for reference and rollback capability.
EOF
```

#### 6.2 Create Submodule Package
```bash
# Create submodule distribution script
cat > .submodule/package.sh << 'EOF'
#!/bin/bash

# Package framework for submodule distribution
echo "📦 Packaging framework for submodule..."

# Create distribution directory
mkdir -p dist/claude-framework

# Copy framework files only
cp -r .claude/framework/* dist/claude-framework/
cp -r .submodule/* dist/claude-framework/
cp README-FRAMEWORK.md dist/claude-framework/README.md

# Create .gitignore for submodule
cat > dist/claude-framework/.gitignore << IGNORE
.transformation/
.claude/project/
.archive/
IGNORE

echo "✅ Framework packaged in dist/claude-framework/"
EOF

chmod +x .submodule/package.sh
```

#### 6.3 Final Documentation
```bash
# Create migration completion report
cat > .transformation/MIGRATION-COMPLETE.md << EOF
# Migration Completion Report

## Summary
- Started: [start date]
- Completed: $(date)
- Duration: 7 days

## Results
- ✅ Directory structure reorganized
- ✅ 35 framework commands created from 88 originals  
- ✅ 3 transformation agents created
- ✅ 5 framework agents created
- ✅ Dual-mode operation validated
- ✅ Submodule packaging ready

## Next Steps
1. Remove .transformation/active to test framework mode
2. Test as git submodule in sample project
3. Update main README with new structure
4. Tag release v2.0-dual-purpose

## Rollback Instructions
If needed, rollback is available:
\`\`\`bash
git checkout pre-migration-v1.0
\`\`\`
EOF
```

## Post-Migration Tasks

### 1. Update Git Configuration
```bash
# Update .gitignore
echo ".transformation/active" >> .gitignore

# Create submodule-specific gitignore
cat > .gitignore-submodule << EOF
.transformation/
.claude/project/
.archive/
*.log
*.tmp
EOF
```

### 2. Test Submodule Integration
```bash
# Create test project
mkdir ../test-project
cd ../test-project
git init

# Add as submodule
git submodule add ../claude-code-modular-prompts .claude-framework
cd .claude-framework
./.submodule/setup.sh --target=..

# Test framework commands
../.claude-framework/.claude/framework/commands/core/help.md
```

### 3. Create Release
```bash
# Tag dual-purpose release
git add -A
git commit -m "Complete dual-purpose migration"
git tag v2.0-dual-purpose

# Create release branch
git checkout -b release/v2.0
```

## Success Metrics

- [ ] All 35 framework commands work in both modes
- [ ] No data lost from original 88 commands
- [ ] Transformation agents only active during migration
- [ ] Framework agents work in submodule context
- [ ] Documentation reflects new structure
- [ ] Tests pass in both modes
- [ ] Submodule integration successful

## Rollback Plan

If migration fails at any point:

1. **Immediate**: `git checkout pre-migration-v1.0`
2. **Partial**: Restore from `.archive/pre-migration/`
3. **Full**: Clone from migration-backup branch

## Long-term Maintenance

1. **Transformation cleanup**: After 6 weeks, remove `.transformation/`
2. **Archive cleanup**: After validation, optional removal of `.archive/`
3. **Documentation update**: Ensure all docs reflect final structure
4. **Version management**: Maintain framework version separately