---
name: /consolidate-docs
description: Organize scattered documentation into proper structure
usage: "/consolidate-docs [--dry-run]"
allowed-tools: [Read, Write, LS, Glob, Bash]
category: maintenance
version: "1.0"
---

# Consolidate Documentation - Clean Up Documentation Chaos

## Purpose
This command addresses the specific anti-pattern discovered in this project: 73+ documentation files scattered in the root directory. It organizes them into a logical structure while preserving all content.

## The Problem (From PROJECT-DNA.md)
```
Anti-Patterns Detected:
1. Documentation Proliferation: 73+ docs in root directory
```

## The Solution

### Target Structure
```
docs/
├── architecture/      # System design documents
├── planning/         # Plans and strategies  
├── reports/          # Analysis and reports
├── guides/           # User guides
└── archive/          # Obsolete documents

project-root/
├── README.md         # Keep in root
├── CLAUDE.md         # Keep in root
└── LICENSE           # Keep in root
```

## What Gets Moved

### To docs/architecture/
- `*-ARCHITECTURE-*.md`
- `*-SYSTEM-*.md`
- `*-DESIGN-*.md`

### To docs/planning/
- `*-PLAN*.md`
- `*-STRATEGY*.md`
- `*-TRANSFORMATION-*.md`

### To docs/reports/
- `*-REPORT*.md`
- `*-ANALYSIS*.md`
- `*-ASSESSMENT*.md`

### To docs/guides/
- `*-GUIDE*.md`
- `QUICKSTART.md`
- `SETUP.md`
- `FAQ.md`

### To docs/archive/
- Duplicate documents
- Obsolete plans
- Superseded strategies

## Execution Process

### Step 1: Analysis
```bash
📊 Analyzing documentation...
  Found: 73 markdown files in root
  Categories identified: 5
  Duplicates detected: 12
  Obsolete files: 8
```

### Step 2: Planning
```bash
📋 Planning organization...
  Architecture docs: 8 files → docs/architecture/
  Planning docs: 15 files → docs/planning/
  Reports: 12 files → docs/reports/
  Guides: 10 files → docs/guides/
  Archive: 20 files → docs/archive/
```

### Step 3: Execution
```bash
🚚 Moving files...
  ✓ Created: docs/architecture/
  ✓ Moved: AGENT-ORCHESTRATION-PLAN.md → docs/architecture/
  ✓ Moved: TRANSFORMATION-PLAN.md → docs/planning/
  ✓ Moved: DEEP-EXPLORATION-REPORT.md → docs/reports/
  [... continues for all files ...]
```

### Step 4: Validation
```bash
✅ Validation...
  ✓ All files moved successfully
  ✓ No broken references
  ✓ Root directory clean
  ✓ Structure logical
```

## Dry Run Mode
```
/consolidate-docs --dry-run
```
Shows what would be moved without actually moving files.

## Benefits

### Before
```
lisbon/
├── 14-STEP-EXECUTION-TEMPLATE.md
├── 8-STEP-EXECUTION-TEMPLATE.md
├── ADAPTATION-GUIDE.md
├── AGENT-ORCHESTRATION-PLAN.md
├── AI-ASSISTANT-SUCCESS-GUIDE.md
├── ... (68 more files)
```

### After
```
lisbon/
├── README.md
├── CLAUDE.md
├── LICENSE
├── docs/
│   ├── architecture/
│   ├── planning/
│   ├── reports/
│   ├── guides/
│   └── archive/
```

## Post-Consolidation

### Update References
The command also updates internal references:
```markdown
<!-- Before -->
See TRANSFORMATION-PLAN.md for details

<!-- After -->
See docs/planning/TRANSFORMATION-PLAN.md for details
```

### Create Index
Generates `docs/INDEX.md` with organized links to all documents.

## Error Handling

### File Conflicts
```
⚠️ File already exists: docs/planning/TRANSFORMATION-PLAN.md
Options:
  1. Overwrite
  2. Keep both (rename)
  3. Skip
  4. Compare files
```

### Permission Issues
```
❌ Cannot create directory: docs/
Please check permissions and try again.
```

## This Command Is Project-Specific

This command was generated specifically for THIS project based on:
- The discovered anti-pattern of scattered documentation
- The specific file naming patterns used
- The categories of documentation present
- The team's apparent organization preferences

For a different project, `/consolidate-docs` might organize test files, or might not exist at all!