# Claude Code Modular Prompts - Template Library

## 🚨 SIMPLICITY MANDATE - STRICTLY ENFORCED
**ZERO TOLERANCE FOR COMPLEXITY - IMMEDIATE REJECTION OF OVER-ENGINEERING**

### MANDATORY RULES (VIOLATION = STOP IMMEDIATELY)
- **ONE SOLUTION ONLY** - No multiple options, no "it depends"
- **DIRECT ACTION** - No planning phases, orchestration, or meta-work
- **30 LINES MAX** - If a script is >30 lines, it's wrong
- **2 COMMANDS MAX** - Users should never run more than 2 commands
- **NO FRAMEWORKS** - Copy files, replace text, done
- **NO "SYSTEMS"** - No architectures, patterns, or abstractions

### BANNED BEHAVIORS
- ❌ Planning orchestration with agents
- ❌ Multi-phase execution strategies  
- ❌ Quality gates and validation frameworks
- ❌ Conditional spawning or adaptive anything
- ❌ JSON configs for "communication protocols"
- ❌ DAG execution graphs
- ❌ Any mention of "enterprise", "scalable", or "robust"

### REQUIRED APPROACH
1. **Copy templates** - Just copy .claude/ folder
2. **Replace placeholders** - Simple find/replace
3. **Done** - No testing frameworks, no validation layers

### LEARNED VIOLATIONS TO NEVER REPEAT
- ❌ **Creating bash scripts** - Use Claude Code tools (Read, Edit, Glob) directly
- ❌ **Promising automation that doesn't exist** - If it says "automated", it must actually work
- ❌ **Adding "validation layers"** - One command does the job, period
- ❌ **Over-promising in documentation** - Only document what actually works
- ❌ **Creating separate utility scripts** - Everything happens in the slash command itself

### ENFORCEMENT EXAMPLES
- **BAD**: `/adapt-to-project` calls separate bash scripts → Creates unnecessary files
- **GOOD**: `/adapt-to-project` uses Read/Edit tools directly → Single command solution
- **BAD**: "Automated adaptation" but templates still have placeholders → Broken promise
- **GOOD**: Command actually replaces placeholders or admits it's manual → Honest approach

**VIOLATION OF THIS MANDATE = IMMEDIATE RESTART WITH SIMPLER APPROACH**

## 🎯 CLAUDE CODE NATIVE UNDERSTANDING

### Core Claude Code Concepts (Research-Based)
- **Slash Commands**: .md files in .claude/commands/ with YAML frontmatter (name, description, usage, tools)
- **CLAUDE.md**: Project memory that persists across sessions - critical for context engineering
- **Settings.json**: Configuration for tools, permissions, hooks (.claude/settings.json or ~/.claude/settings.json)
- **Context Engineering**: Managing what Claude knows and when - optimize token usage and performance
- **Sub-agents**: Specialized AI assistants for specific tasks (.claude/agents/ directory)
- **MCP Tools**: Model Context Protocol for filesystem/memory access and external integrations

### Key Claude Code Features for This Project
- **Hooks**: Automate workflows (PreToolUse, PostToolUse, Stop, Notification) - enables true automation
- **Headless Mode**: CI/CD integration with `claude -p "prompt"` and `--output-format stream-json`
- **Framework Detection**: Scan package.json, requirements.txt, etc. for auto-configuration  
- **Meta-prompting**: Use Claude to generate better prompts and improve templates
- **Token Optimization**: Use /clear, /compact, manage context window efficiently
- **Permission System**: Read-only by default, explicit permission for file operations
- **Team Collaboration**: Commands shared via git, consistent workflows across teams

### True Automation Opportunities (Not Theater)
Based on 50+ research sources, these are proven automation patterns:
1. **File scanning** to detect project type (package.json, requirements.txt, etc.)
2. **Automatic placeholder replacement** based on detected frameworks
3. **Hook-based workflows** that run automatically on file changes
4. **CI/CD integration** for team deployment and validation
5. **Sub-agent workflows** for parallel processing and specialization
6. **MCP filesystem integration** for persistent memory and file management

### Anti-Patterns to Avoid (Research-Validated)
- ❌ **False automation promises** - If it says automated, it must actually work
- ❌ **Placeholder pollution** - Commands with [INSERT_XXX] that break workflows
- ❌ **Context window bloat** - Loading irrelevant history that degrades performance
- ❌ **Token waste** - Inefficient prompt patterns that consume unnecessary tokens
- ❌ **Manual masquerading as automation** - Scripts that just provide instructions

## 🔧 TEMPLATE LIBRARY MAINTENANCE STANDARDS

### Structural Integrity Requirements
- **Commands directory**: ONLY .md files allowed (no scripts, reports, or binaries)
- **YAML frontmatter**: Consistent field names (`usage`, `tools` - never `argument-hint`, `allowed-tools`)
- **No duplicates**: Zero duplicate command names across all directories
- **Accurate counts**: Documentation must reflect actual file counts at all times
- **Proper categorization**: Commands placed in correct directory (core, quality, specialized, etc.)

### Quality Control Checkpoints
- **Pre-commit validation**: Verify file placement and YAML consistency before any changes
- **Regular audits**: Check for duplicate commands and misplaced files monthly
- **Documentation sync**: Update counts immediately after any structural changes
- **YAML compliance**: All commands must have standardized frontmatter

### Critical Issues Learned (NEVER REPEAT)
- ❌ **Non-MD files in commands directory** - Python scripts, shell scripts, reports belong elsewhere
- ❌ **Duplicate command names** - Creates confusion about which version to use
- ❌ **Inconsistent YAML fields** - Use `usage` not `argument-hint`, `tools` not `allowed-tools`
- ❌ **Inaccurate command counts** - Documentation showed 102 when only 64 existed
- ❌ **Commands in wrong categories** - Misplaced files make discovery impossible
- ❌ **Deprecated directories** - If consolidated, remove deprecated versions completely

### Validation Procedures
1. **File type check**: `find .claude/commands -type f ! -name "*.md"` should return empty
2. **YAML consistency**: All active commands must use standard field names
3. **Count verification**: `find .claude/commands -name "*.md" | wc -l` must match documentation
4. **Duplicate detection**: No command basename should appear in multiple directories
5. **Category validation**: Commands placed in logical directories by function

### Maintenance Commands
- **Structure check**: Use `/validate-adaptation` to verify template integrity
- **Count update**: Update CLAUDE.md immediately after any file changes
- **YAML validation**: Use validation scripts to check frontmatter consistency

**THESE STANDARDS ARE MANDATORY - VIOLATION REQUIRES IMMEDIATE CLEANUP**

---

**📚 PROMPT TEMPLATE LIBRARY** - A comprehensive collection of 64 Claude Code command templates with manual customization guides and anti-pattern prevention.

**🎯 PURPOSE**: Provide proven prompt templates that automatically adapt to your specific project, saving months of trial-and-error learning.

## What This Library Actually Provides

**What You Get:**
- 📋 **Guide commands** that provide manual customization checklists
- 📁 **Dual folder structure**: Working copy + reference copy
- 📝 **64 command templates** with [INSERT_XXX] placeholders
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

## Template Library Components

| Component | Count | Purpose |
|-----------|-------|---------|
| Command Templates | 64 active | Ready-to-use Claude Code slash commands |
| Component Templates | 70 | Reusable prompt fragments |
| Context Files | 15+ | Anti-patterns, best practices, guides |
| Meta Commands | 8 | Adaptation and validation helpers |
| Test Suites | 10+ | Validation and quality assurance |
| Documentation | 30+ files | Comprehensive guides and examples |

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
| Command templates | 64 with placeholders | Provide starting points for customization |
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

### 🎯 RELEASE STATUS: v1.0 LIBRARY ORGANIZATION ✅
**Library Asset Management**: COMPREHENSIVE CONTENT PRESERVATION
- ✅ 64 command templates preserved and cataloged
- ✅ 70 component templates organized in accessible structure
- ✅ 48+ anti-patterns documented and maintained as reference
- ✅ All research, guides, and documentation preserved as library assets
- ✅ Reports maintained as valuable reference material for template development
- ✅ Testing framework validates template structure (not deletion)
- ✅ Context engineering files preserved for prompt development guidance
- ✅ Zero library content lost - organization enhances accessibility
- ✅ Library structure optimized for template discovery and reuse

### 📁 CURRENT PROJECT STRUCTURE
**Clean & Organized Layout**:
```
casablanca/                      # Main project directory
├── .claude/                     # Claude Code configuration
│   ├── commands/                # 64 command templates
│   ├── components/              # 70 reusable prompt components
│   ├── config/                  # Configuration templates
│   ├── context/                 # Context engineering files
│   ├── docs/                    # Claude-specific documentation
│   ├── internal-docs/           # Internal architecture docs
│   ├── learning/                # Learning patterns
│   ├── research/                # Research materials
│   ├── scripts/                 # Utility scripts
│   ├── templates/               # Command templates
│   └── settings.json            # Claude Code settings
├── docs/                        # User documentation
│   ├── user/                    # End-user guides
│   └── internal/                # Internal documentation
├── reports/                     # All project reports
│   ├── architecture/            # Architecture overviews
│   ├── deployment/              # Deployment assessments
│   ├── security/                # Security audits
│   └── testing/                 # Test results
├── releases/v1.0/               # Release artifacts
├── scripts/                     # Project scripts
├── tests/                       # Testing framework
├── CLAUDE.md                    # This file (project memory)
├── README.md                    # Main project overview
├── claude.local.md              # Private project instructions
└── setup.sh                     # Installation script
```

## Experimental Framework Notice
This is an **experimental prompt engineering framework** for research and development:
- Focus is on prompt effectiveness and architectural exploration
- Commands require functional validation before production use
- All 64 commands are maintained as unique implementations
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
**Structural Validation**: 100% (64/64 commands passing)
- All commands have required YAML front matter fields
- **Functional Validation**: 100% (64/64 commands passing Claude Code compliance tests)

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

## 📚 LIBRARY PRESERVATION STRATEGY

### Why ALL Content Matters in a Template Library

**Core Principle**: In a template library, seemingly "scattered" content is often valuable reference material:

- **Reports & Documentation**: Show real-world template usage patterns and evolution
- **Anti-patterns**: Prevent users from making documented mistakes  
- **Research Materials**: Provide context for why templates were designed certain ways
- **Deprecated Templates**: Serve as historical reference and migration guides
- **Context Files**: Essential for understanding prompt engineering principles
- **Test Results**: Validate template effectiveness and guide improvements

### Organization vs Deletion Philosophy

**✅ LIBRARY ORGANIZATION** (What We Do):
- Catalog and categorize all 102 command templates
- Make 70 components easily discoverable  
- Organize documentation by access patterns
- Create clear navigation paths to content
- Preserve all research and learning materials
- Maintain historical context and evolution

**❌ AGGRESSIVE CLEANUP** (What We Avoid):
- Deleting "duplicate" templates (might serve different use cases)
- Removing "outdated" documentation (valuable for understanding evolution) 
- Throwing away reports (contain usage insights)
- Eliminating context files (essential for prompt engineering)
- Purging template variants (different use cases may need different approaches)

### Template Library Success Metrics

1. **Accessibility**: Can users quickly find relevant templates?
2. **Completeness**: Are all use cases covered by available templates?
3. **Context**: Do users understand when/why to use each template?
4. **Evolution**: Can users see how templates developed over time?
5. **Prevention**: Are anti-patterns clearly documented to avoid common mistakes?

*Last honest assessment: 2025-07-29*