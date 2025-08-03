# UltraThink: Complete Adaptation Engine Implementation Plan

## Executive Summary

Transform the Claude Code Modular Prompts framework into an **Active Adaptation Engine** that guides users through customizing 6-8 months of prompt engineering knowledge for their specific projects in minutes.

## Phase 1: Core Meta-Commands (Week 1)

### 1.1 `/adapt-to-project` Command
Create the primary adaptation command with dual modes:

**Mode 1: Express Mode (50 Yes/No Questions)**
```markdown
---
name: /adapt-to-project
description: Intelligent project adaptation with 50-question assessment
usage: /adapt-to-project [--express|--guided] [--dry-run]
---

## Express Mode Flow
1. Tech stack detection (auto-detect from package.json, requirements.txt, etc.)
2. 50 rapid-fire yes/no questions covering:
   - Project type (web, data-science, devops, mobile, desktop)
   - Team size and workflow preferences
   - Tool preferences and restrictions
   - Security requirements
   - Performance priorities
   - Domain-specific needs
3. Generate adaptation profile
4. Apply all adaptations in one batch
5. Show readiness score (0-100%)

## Guided Mode Flow
1. Welcome and overview
2. Step-by-step wizard:
   - Project basics (name, domain, description)
   - Tech stack confirmation
   - Tool preferences
   - Workflow customization
   - Component selection
   - Security configuration
3. Preview changes at each step
4. Apply adaptations incrementally
```

### 1.2 Project Configuration System
```xml
<!-- project-config.yaml -->
<project-config version="1.0">
  <metadata>
    <name>[INSERT_PROJECT_NAME]</name>
    <domain>[INSERT_DOMAIN]</domain>
    <created>2025-07-27</created>
    <adaptation-mode>express|guided</adaptation-mode>
    <readiness-score>0</readiness-score>
  </metadata>
  
  <placeholders>
    <!-- Standard placeholders -->
    <placeholder key="PROJECT_NAME" value="[INSERT_PROJECT_NAME]"/>
    <placeholder key="DOMAIN" value="[INSERT_DOMAIN]"/>
    <placeholder key="TECH_STACK" value="[INSERT_TECH_STACK]"/>
    <placeholder key="COMPANY_NAME" value="[INSERT_COMPANY_NAME]"/>
    <placeholder key="TEAM_SIZE" value="[INSERT_TEAM_SIZE]"/>
    <placeholder key="WORKFLOW_TYPE" value="[INSERT_WORKFLOW_TYPE]"/>
    <placeholder key="PRIMARY_LANGUAGE" value="[INSERT_PRIMARY_LANGUAGE]"/>
    <placeholder key="TESTING_FRAMEWORK" value="[INSERT_TESTING_FRAMEWORK]"/>
    <placeholder key="CI_CD_PLATFORM" value="[INSERT_CI_CD_PLATFORM]"/>
    <placeholder key="DEPLOYMENT_TARGET" value="[INSERT_DEPLOYMENT_TARGET]"/>
    
    <!-- Nested placeholders example -->
    <placeholder key="[INSERT_DOMAIN]_CONFIG" value="[INSERT_[INSERT_DOMAIN]_SPECIFIC_CONFIG]"/>
  </placeholders>
  
  <adaptations>
    <applied>
      <!-- Track what's been done -->
    </applied>
  </adaptations>
</project-config>
```

### 1.3 Standard Placeholder Set (15 Core)
1. `[INSERT_PROJECT_NAME]` - Project identifier
2. `[INSERT_DOMAIN]` - web-dev, data-science, devops, mobile
3. `[INSERT_TECH_STACK]` - React+Node, Python+FastAPI, etc.
4. `[INSERT_COMPANY_NAME]` - Organization name
5. `[INSERT_TEAM_SIZE]` - solo, small, medium, large
6. `[INSERT_WORKFLOW_TYPE]` - agile, waterfall, hybrid
7. `[INSERT_PRIMARY_LANGUAGE]` - JavaScript, Python, Go, etc.
8. `[INSERT_TESTING_FRAMEWORK]` - Jest, PyTest, etc.
9. `[INSERT_CI_CD_PLATFORM]` - GitHub Actions, Jenkins, etc.
10. `[INSERT_DEPLOYMENT_TARGET]` - AWS, Azure, on-premise
11. `[INSERT_DATABASE_TYPE]` - PostgreSQL, MongoDB, etc.
12. `[INSERT_API_STYLE]` - REST, GraphQL, gRPC
13. `[INSERT_SECURITY_LEVEL]` - basic, standard, high
14. `[INSERT_PERFORMANCE_PRIORITY]` - balanced, optimized
15. `[INSERT_USER_BASE]` - internal, b2b, b2c, enterprise

## Phase 2: Advanced Meta-Commands (Week 1-2)

### 2.1 Tech Stack Detection
```markdown
---
name: /detect-tech-stack
description: Automatically detect project technology stack
internal: true
---

## Detection Logic
1. Check for package.json → Node.js ecosystem
2. Check for requirements.txt/Pipfile → Python ecosystem
3. Check for go.mod → Go ecosystem
4. Check for Cargo.toml → Rust ecosystem
5. Check for pom.xml/build.gradle → Java ecosystem
6. Check for composer.json → PHP ecosystem
7. Check for Gemfile → Ruby ecosystem

## Confirmation Prompt
"I detected: [DETECTED_STACK]. Is this correct? (y/n)"
```

### 2.2 Validation & Scoring
```markdown
---
name: /validate-adaptation
description: Check adaptation completeness and calculate readiness score
usage: /validate-adaptation [--verbose]
---

## Validation Checks
1. Unreplaced placeholders (each -5%)
2. Missing project-config.yaml (-20%)
3. Incomplete command selection (-10%)
4. No domain customization (-15%)
5. Default security settings (-10%)

## Readiness Score
- 0-40%: Framework imported but not adapted
- 41-70%: Basic adaptation complete
- 71-90%: Well-adapted for your project
- 91-100%: Fully customized and optimized
```

### 2.3 Undo & Recovery
```markdown
---
name: /undo-adaptation
description: Revert adaptations to previous state
usage: /undo-adaptation [--last|--to-snapshot <id>]
---

## Undo Capabilities
1. Snapshot before each adaptation
2. Restore to any previous state
3. Selective undo (specific changes only)
4. Dry-run preview before reverting
```

## Phase 3: Community Features (Week 2)

### 3.1 Shareable Adaptation Patterns
```json
{
  "pattern": {
    "name": "E-commerce Web Dev Pattern",
    "author": "community",
    "version": "1.0",
    "base-domain": "web-dev",
    "specialization": "e-commerce",
    "placeholders": {
      "TECH_STACK": "React+Node+PostgreSQL",
      "API_STYLE": "GraphQL",
      "TESTING_FRAMEWORK": "Jest+Cypress",
      "PAYMENT_PROVIDER": "[INSERT_PAYMENT_PROVIDER]"
    },
    "command-selection": ["checkout", "inventory", "user-auth"],
    "custom-commands": ["payment-flow", "cart-management"]
  }
}
```

### 3.2 Update Synchronization
```markdown
---
name: /sync-from-reference
description: Pull framework updates while preserving customizations
usage: /sync-from-reference [--preview] [--approve-all]
---

## Sync Strategy
1. Never modify user's customized commands
2. Add new commands from framework
3. Update unchanged reference commands
4. Show changelog for review
5. Require approval for overwrites
```

## Phase 4: User Experience Polish (Week 2-3)

### 4.1 First-Run Experience
When user first enters Claude Code after setup:
```
Welcome to Claude Code Adaptation Engine! 🚀

You've imported 6-8 months of prompt engineering knowledge.
Let's customize it for your project in just 5 minutes.

Choose your adaptation style:
1. Express Mode - Answer 50 quick yes/no questions
2. Guided Mode - Step-by-step customization wizard
3. Manual Mode - I'll adapt it myself later

Type /adapt-to-project --express or --guided to begin!
```

### 4.2 Progress Indicators
Throughout adaptation:
```
[████████░░░░░░░░░░] 45% Complete
✅ Project name set
✅ Tech stack detected
✅ Domain configured
⏳ Replacing placeholders...
⏭️ Component selection
⏭️ Security configuration
```

### 4.3 Dry-Run Mode
All meta-commands support --dry-run:
```
/adapt-to-project --express --dry-run

This would:
- Set PROJECT_NAME to "MyAwesomeApp"
- Configure for web-dev domain
- Replace 247 placeholders across 79 files
- Select 45 commands for your tech stack
- Configure medium security level

No changes made. Remove --dry-run to apply.
```

## Phase 5: Implementation Approach (Week 3)

### 5.1 Directory Structure Updates
```bash
# setup.sh modifications
#!/bin/bash

# Create dual structure
mkdir -p "$TARGET/.claude"
mkdir -p "$TARGET/.claude-adaptations/history"
mkdir -p "$TARGET/.claude-adaptations/patterns"
mkdir -p "$TARGET/.claude-adaptations/backups"

# Copy as git submodule or regular directory
if [ "$1" == "--submodule" ]; then
    git submodule add $REPO_URL .claude-framework
else
    cp -r . "$TARGET/.claude-framework"
fi

# Make framework read-only
chmod -R a-w "$TARGET/.claude-framework"

# Initialize project-config.yaml
cp templates/project-config.yaml "$TARGET/.claude/config/"
```

### 5.2 Meta-Command Implementation Strategy
Since we must be Claude Code native (no Python orchestration):
1. Meta-commands are Claude Code slash commands (.md files)
2. They guide Claude to perform adaptations using available tools
3. State tracked in XML/JSON files
4. Validation through Claude's analysis capabilities

### 5.3 Complete Adaptation Flow
```markdown
---
name: /complete-adaptation
description: Run entire adaptation flow for new users
usage: /complete-adaptation [--mode express|guided|auto]
---

## Auto Mode (Default)
1. Detect tech stack
2. Infer domain from file patterns
3. Set sensible defaults
4. Apply standard adaptation
5. Show summary and readiness score

## Express Mode
- Triggers 50-question assessment
- Batch applies all changes
- 5-minute process

## Guided Mode
- Interactive wizard
- Explains each choice
- 15-minute process
```

## Success Metrics

1. **Adaptation Time**: <5 minutes from import to 80%+ readiness
2. **Placeholder Coverage**: 100% replacement in adapted files
3. **User Satisfaction**: Clear guidance at every step
4. **Flexibility**: Support all project types and workflows
5. **Safety**: Full undo capability and dry-run previews
6. **Community**: Easy pattern sharing and updates

## Implementation Priority

**Week 1**: 
- Core meta-commands (/adapt-to-project dual mode)
- Project config system
- Basic placeholder replacement

**Week 2**:
- Validation and scoring
- Undo capability
- Tech stack detection

**Week 3**:
- Community features
- Sync from reference
- Polish and testing

This plan ensures users can go from zero to a fully customized Claude Code environment in minutes, with the flexibility to adapt further as their project evolves.

---
*Plan Created: 2025-07-27*
*Estimated Implementation: 3 weeks*
*Readiness Target: Production-ready adaptation engine*