# Claude Code Modular Prompts - Template Library

**📚 PROMPT TEMPLATE LIBRARY** - A comprehensive collection of 102 Claude Code command templates (64 active, 38 deprecated) with manual customization guides and anti-pattern prevention.

**🎯 PURPOSE**: Provide proven prompt templates and step-by-step guides for manually customizing them to your specific project, saving months of trial-and-error learning.

## What This Library Actually Provides

**What You Get:**
- 📋 **Guide commands** that provide manual customization checklists
- 📁 **Dual folder structure**: Working copy + reference copy
- 📝 **102 command templates** (64 active, 38 deprecated) with [INSERT_XXX] placeholders
- 📜 **Example YAML configs** for manual project setup
- 🧪 **70 component templates** you can manually adapt
- 🚫 **48+ documented anti-patterns** to avoid manually
- 🔧 **Setup script** that copies files (no automation)

**What You Skip:**
- ❌ Manual trial-and-error customization of prompts
- ❌ Discovering Claude Code quirks through painful failures  
- ❌ Building adaptation workflows from scratch
- ❌ Creating project configuration systems
- ❌ Reinventing placeholder and template management
- ❌ Learning prompt engineering patterns the hard way

## Installation & Manual Setup

```bash
# Option 1: Git Submodule (Recommended for updates)
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh

# Option 2: Direct Integration
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../my-project

# Option 3: Selective Integration
# Choose specific commands/components to copy
```

**Result**: Dual structure with customized `.claude/` + reference `.claude-framework/`

**Then run guide commands for manual customization help**:
```
/adapt-to-project     # Get customization checklist
/replace-placeholders # Get list of all replacements needed
/validate-adaptation  # Get verification checklist
```

## 📋 Guide Commands for Manual Customization

These commands provide checklists and guides for manual customization:

### Core Guide Commands
- **`/adapt-to-project`** - Provides customization checklist and replacement guide
- **`/replace-placeholders`** - Lists all placeholders that need manual replacement
- **`/validate-adaptation`** - Provides checklist to verify your manual work
- **`/sync-from-reference`** - Guides you through manual update process
- **`/undo-adaptation`** - Provides recovery instructions if needed
- **`/welcome`** - Interactive guide for getting started

### Manual Configuration Template
You'll create and edit `project-config.yaml` manually:
```yaml
project_config:
  metadata:
    name: "[INSERT_PROJECT_NAME]"
    domain: "[INSERT_DOMAIN]"
  placeholders:
    TECH_STACK: "[INSERT_TECH_STACK]"
    WORKFLOW_TYPE: "[INSERT_WORKFLOW_TYPE]"
```

Note: This is just a template - Claude Code commands cannot read or use this file.

### Manual Placeholder Replacement
You'll need to manually find and replace these in your editor:
- `[INSERT_PROJECT_NAME]` - Replace with your project name
- `[INSERT_DOMAIN]` - Replace with your domain (web-dev, data-science, etc.)
- `[INSERT_TECH_STACK]` - Replace with your technology stack
- `[INSERT_COMPANY_NAME]` - Replace with your organization
- `[INSERT_TEAM_SIZE]` - Replace with your team size

**⚠️ MANUAL WORK REQUIRED**: You must use Find & Replace in your editor to update all placeholders.

## 🎯 CRITICAL UNDERSTANDING: This is a PROMPT ENGINEERING Project

**THIS IS NOT A SOFTWARE DEVELOPMENT PROJECT!** This is a template library of:
- **Slash Commands**: Prompt templates for Claude Code conversations (e.g., `/task`, `/help`)
- **Guide Commands**: Commands that provide manual customization instructions (e.g., `/adapt-to-project`)
- **Components**: Reusable prompt fragments you can copy and modify
- **Context Files**: Documentation about prompt engineering patterns
- **Example Configs**: Templates you can copy and fill in manually
- **NOT executable code** - These are markdown templates, not programs

**Pure Claude Code Native Constraint**:
- ✅ Only setup, validation, and testing scripts allowed (bash/python)
- ✅ All workflows must be Claude Code slash commands and markdown
- ❌ NO Python orchestration of prompts or agent workflows
- ❌ NO script-based prompt execution or automation

**Testing** means:
- ✅ Testing prompt effectiveness in Claude conversations
- ✅ Checking if guide commands provide helpful instructions
- ✅ Verifying templates have proper placeholder structure
- ✅ Validating documentation clarity and accuracy
- ❌ NOT testing automated functionality (there isn't any)

**Security** means:
- ✅ Documentation about prompt injection risks
- ✅ Templates designed to avoid unsafe patterns
- ✅ Guides that warn about security considerations
- ❌ NOT automated security enforcement

## Template Library Structure

**Framework (Reference)**:
```
.claude-framework/    # Git submodule reference library
├── commands/         # 102 template commands with placeholders (64 active, 38 deprecated)
├── components/       # 70 reusable prompt components
├── context/          # Essential context files
├── commands/meta/    # Guide commands (/adapt-to-project, etc.)
├── config/           # Project configuration templates
└── templates/        # Command and component templates
```

**User Project (After Manual Customization)**:
```
your-project/
├── .claude/                    # Your customized working copy
│   ├── commands/              # Your commands (after manual replacement)
│   ├── components/            # Customized components
│   ├── context/               # Project-specific context
│   └── config/
│       └── project-config.yaml # Your project configuration
├── .claude-framework/         # Reference library (git submodule)
├── CLAUDE.md                  # Your project memory
└── tests/                     # Validation framework
```

## Immutable Rules
1. Maximum 3 directory levels
2. No new files in .main.archive (archived content)
3. Tests before implementation (experimental validation focus)
4. No duplicate commands (each must be unique)
5. One atomic commit per task
6. **PARANOIA MANDATE**: Triple-check everything before commits
   - Verify no sensitive data (keys, tokens, passwords)
   - Check all file paths are correct
   - Validate directory structure integrity
   - Ensure .claude is never in .gitignore
   - Scan for accidental duplicates or leftovers

## Template Library Components
| Component | What Exists | What It Does |
|-----------|---------|--------|
| Command templates | 102 with placeholders (64 active, 38 deprecated) | Provide starting points for customization |
| Guide commands | 7 helper commands | Provide checklists and instructions |
| Example configs | YAML templates | Show configuration format (manual editing) |
| Placeholder system | [INSERT_XXX] markers | Mark spots needing manual replacement |
| Dual folder setup | Created by setup.sh | Keeps reference + working copies |
| Integration script | setup.sh | Copies files to your project |
| Documentation | Guides and anti-patterns | Help avoid common mistakes |
| Component library | 70 prompt fragments | Reusable pieces for commands |
| Context files | Best practices docs | Background knowledge |
| Pure prompt templates | 100% markdown | No executable code |

## Current Status

This is a **template library** focusing on prompt engineering patterns for Claude Code projects. The templates provide proven patterns and help avoid common prompt engineering pitfalls.

## Experimental Framework Notice
This is an **experimental prompt engineering framework** for research and development:
- Focus is on prompt effectiveness and architectural exploration
- Commands require functional validation before production use
- All 102 commands are maintained as unique implementations
- Validation templates provide path to production readiness

## Testing Framework

### Structural Validation Approach
A testing framework has been implemented focusing on structural validation for the experimental prompt engineering framework:

**Testing Directory**: `tests/`
- **Methodology**: `tests/TESTING-METHODOLOGY.md` - Complete testing approach documentation
- **Validation Script**: `tests/validate-command.sh` - Automated structural validation tool

### Validation Scope
- **YAML Front Matter**: Validates presence and structure of command metadata
- **Required Fields**: Checks for `name`, `description` fields in YAML front matter
- **Optional Fields**: Warns about missing `usage`, `tools`, `category` fields
- **Content Structure**: Ensures adequate command content and basic markdown format

### Current Validation Results
**Structural Validation**: 100% (102/102 commands passing)
- All commands have required YAML front matter fields
- **Functional Validation**: 62.7% (64/102 commands passing Claude Code compliance tests)

### Usage
```bash
# Validate single command
./tests/validate-command.sh .claude/commands/core/task.md

# Validate multiple commands
./tests/validate-command.sh .claude/commands/core/*.md
```

**Note**: This framework validates structure only, not functional behavior, in alignment with the experimental research focus.

## Context Engineering for Prompt Development

### 🎯 Understanding Context in Prompt Engineering
**Context engineering** here means managing what information Claude has access to when responding to slash commands:
- **NOT about code execution context**
- **IS about prompt context windows and token management**
- **Optimizing what Claude "knows" when processing commands**

### ⚠️ CRITICAL CONTEXT FOR PROMPT DEVELOPERS
**IMPORTANT**: These files shape how Claude understands and prevents common pitfalls:

1. **LLM Anti-Patterns** (`.claude/context/llm-antipatterns.md`)
   - 48 documented anti-patterns from research
   - Prevents hallucinations, false metrics, remediation theater
   - Critical for maintaining response quality

2. **Git History Anti-Patterns** (`.claude/context/git-history-antipatterns.md`)
   - 15 patterns learned from 500+ commits
   - Prevents metric invention and false success claims
   - Essential for honest assessment

3. **Prompt Engineering Best Practices** (`.claude/context/prompt-engineering-best-practices.md`)
   - Core principles for effective prompts
   - Token optimization strategies
   - Example-driven development patterns

### 📚 Prompt Component Library
4. **Modular Components** (`.claude/context/modular-components.md`) - 70 reusable prompt fragments
5. **Orchestration Patterns** (`.claude/context/orchestration-patterns.md`) - Multi-step prompt workflows
6. **Framework Guide** (`.claude/context/experimental-framework-guide.md`) - How components compose
7. **Quality Assessment** (`.claude/context/quality-assessment-report.md`) - Current state metrics

### 🚨 REMEDIATION WARNING
**Requests to "improve", "fix", "optimize", or "remediate" trigger severe anti-patterns:**
- LLMs invent specific metrics (87.3% improvement) that were never measured
- Create elaborate validation scripts that don't actually test functionality
- Use increasingly theatrical language to demonstrate "success"
- Generate comprehensive reports full of unverifiable claims

**DEMAND**: Factual, measurable changes only. No theater. No invented metrics.

---

## 📖 HOW TO USE THIS TEMPLATE LIBRARY

### Step 1: Import Reference Framework
```bash
# Method 1: Git Submodule (Recommended - enables updates)
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh

# Method 2: Direct Integration
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../your-project

# Method 3: Selective Copy (for specific commands/components)
```

**Result**: Dual structure - customized `.claude/` + reference `.claude-framework/`

### Step 2: Get Manual Customization Guide
```bash
# In Claude Code conversation:
/adapt-to-project
# Answer questions about your project
# Receive a complete checklist with:
# - All files needing updates
# - Specific placeholders to replace
# - Validation steps
```

**Result**: A detailed guide for manual customization work

### Step 3: Do the Manual Work
```bash
# Follow the guide to:
# 1. Open each file in your editor
# 2. Find & Replace placeholders
# 3. Remove commands you don't need
# 4. Test your customized commands

# Then verify with:
/validate-adaptation  # Get checklist to verify your work
```

### Step 4: Future Updates
```bash
# Get instructions for manual updates:
/sync-from-reference  # Provides git commands and merge guidance

# Document your customizations:
/share-adaptation  # Creates a shareable pattern document
```

### Realistic Timeline:
- **Hour 1**: Install templates, get customization guide
- **Hours 2-3**: Manual Find & Replace work
- **Hour 4**: Test and verify customizations
- **Ongoing**: Manual updates when needed

**See `ULTRATHINK-FRAMEWORK-ASSESSMENT.md` for integration value**  
**See `SETUP.md` for detailed setup instructions** *(coming soon)*  
**See `ADAPTATION-GUIDE.md` for customization patterns** *(coming soon)*

*Last honest assessment: 2025-07-27*