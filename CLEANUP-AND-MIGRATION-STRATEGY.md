# Cleanup and Migration Strategy

## Overview
This document outlines the complete cleanup process for transforming the existing project and migrating users to the new system.

## Phase 1: Inventory and Classification (Week 1)

### 1.1 File Classification System
Every file in the current project must be classified as:
- **KEEP**: Verified, valuable content to preserve
- **TRANSFORM**: Needs modification for new system
- **ARCHIVE**: Historical value but not active
- **DELETE**: No value, can be removed
- **MIGRATE**: User data that needs migration path

### 1.2 Detailed Inventory Process

#### Commands Analysis (.claude/commands/)
```bash
# For each of 88 commands:
1. Extract core pattern
2. Find evidence sources
3. Classify: KEEP/TRANSFORM/ARCHIVE/DELETE
4. Document in command-inventory.csv
5. Note dependencies on other commands
```

#### Components Analysis (.claude/components/)
```bash
# For each of 96 components:
1. Verify actual functionality
2. Check for duplication
3. Find authoritative sources
4. Classify status
5. Document in component-inventory.csv
```

#### Context Files Analysis
- **Vetted Anti-patterns** → KEEP (move to vetted-context/)
- **Unverified Claims** → ARCHIVE
- **Research Documents** → TRANSFORM (add sources)
- **Generated Reports** → DELETE

### 1.3 Cleanup Actions by Classification

#### KEEP Files
```bash
# Move to new structure preserving value
cp .claude/context/llm-antipatterns.md .claude-context/vetted-context/antipatterns/
cp .claude/context/comprehensive-project-learnings.md .claude-context/vetted-context/
git add .claude-context/
git commit -m "Preserve vetted anti-patterns and learnings"
```

#### TRANSFORM Files
```bash
# Create transformation queue
mkdir -p .transformation-queue
# Move files needing transformation
mv [file] .transformation-queue/
# Track in TRANSFORMATION-LOG.md
```

#### ARCHIVE Files
```bash
# Create archive with clear labeling
mkdir -p .archive/pre-transformation
mv [outdated-files] .archive/pre-transformation/
echo "Archived on $(date)" > .archive/pre-transformation/README.md
git add .archive/
git commit -m "Archive outdated content with timestamp"
```

#### DELETE Files
```bash
# Create deletion log first
echo "[filename] - Reason for deletion" >> .deletion-log.txt
# Then remove
rm [file]
git commit -m "Remove [category] files per cleanup plan"
```

## Phase 2: Data Migration (Week 2-3)

### 2.1 User Configuration Migration
For users with existing setups:

```markdown
## Migration Path for Existing Users

### Your Existing Commands
Located in: .claude/commands/
Action: Run migration analyzer
```bash
/0_verify-migration
```

### Your Custom Patterns
We'll help you:
1. Identify which patterns to keep
2. Find evidence sources for them
3. Transform to new format
4. Preserve your customizations
```

### 2.2 Command Migration Tool
Create `.claude-context/migration/command-migrator.md`:
```yaml
name: command-migrator
description: Analyze and migrate existing commands
process:
  1. Scan existing command
  2. Extract core functionality
  3. Search for evidence sources
  4. Generate new numbered command
  5. Preserve user customizations
```

### 2.3 Settings Migration
```json
// Old settings.json
{
  "experimentalFeatures": true,
  "customCommands": ["array"]
}

// New settings.json
{
  "version": "2.0",
  "researchIntegration": true,
  "evidenceRequirement": "strict",
  "migratedFrom": "1.0",
  "customizations": {
    "preserved": ["list"],
    "adapted": ["list"]
  }
}
```

## Phase 3: Deprecation Strategy (Week 4-5)

### 3.1 Deprecation Warnings
Add to all old commands:
```markdown
---
DEPRECATED: This command will be removed in v2.0
REPLACEMENT: Use /1_research-domain instead
MIGRATION: See MIGRATION-GUIDE.md
---
```

### 3.2 Phased Deprecation
1. **Week 1-2**: Add deprecation notices
2. **Week 3-4**: Provide migration tools
3. **Week 5-6**: Remove deprecated commands
4. **After Release**: Support period for stragglers

### 3.3 Communication Plan
```markdown
1. Announcement email/blog post
2. GitHub repository notice
3. In-tool migration prompts
4. Community forum posts
5. Video migration guide
```

## Phase 4: Repository Cleanup (Week 5)

### 4.1 Git History Preservation
```bash
# Create pre-transformation tag
git tag -a "v1.0-pre-transformation" -m "Last version before context engineering transformation"
git push origin v1.0-pre-transformation
```

### 4.2 Branch Strategy
```bash
# Main development branch
git checkout -b context-engineering-v2

# Keep v1 branch for reference
git checkout -b v1-maintenance

# Archive experimental features
git checkout -b archive/experimental-features
```

### 4.3 File Structure Cleanup
```bash
# Remove empty directories
find . -type d -empty -delete

# Update .gitignore
echo ".transformation-queue/" >> .gitignore
echo ".deletion-log.txt" >> .gitignore

# Clean up test artifacts
rm -rf tests/artifacts/
rm -rf .pytest_cache/
```

### 4.4 Documentation Cleanup
- Remove outdated README sections
- Update all path references
- Fix broken internal links
- Remove aspirational features
- Update command counts

## Phase 5: Performance Optimization

### 5.1 Token Usage Analysis
```markdown
Old System Token Usage:
- Average command: 1,200 tokens
- Full context load: 180k tokens
- Efficiency: 60%

New System Target:
- Average command: 800 tokens  
- Smart context load: 100k tokens
- Efficiency: 85%
```

### 5.2 Context Optimization
- Remove redundant documentation
- Compress verbose descriptions
- Use references instead of duplication
- Implement lazy loading patterns

## Phase 6: Security Review

### 6.1 Sensitive Data Scan
```bash
# Scan for potential secrets
grep -r "api_key\|password\|secret\|token" .
grep -r "[0-9]{16}" . # Credit card patterns
grep -r "sk-[a-zA-Z0-9]{48}" . # API keys

# Check for personal data
grep -r "@.*\.com" . # Email addresses
grep -r "http[s]?://[^/]*:[^/]*@" . # URLs with credentials
```

### 6.2 Security Cleanup Actions
- Remove any found secrets
- Sanitize example data
- Update documentation to use placeholders
- Add security warnings where needed

## Phase 7: Quality Assurance

### 7.1 Link Validation
```bash
# Check all documentation links
find . -name "*.md" -exec grep -l "http" {} \; | \
  xargs -I {} sh -c 'echo "Checking {}" && \
  grep -o "http[s]*://[^\"\'<>]*" {} | \
  xargs -I [] curl -s -o /dev/null -w "%{http_code} []\n" []'
```

### 7.2 Command Reference Validation
- Verify all command references exist
- Check for orphaned dependencies
- Validate YAML frontmatter
- Ensure proper categorization

## Success Criteria

### Cleanup Complete When:
- [ ] All 88 commands classified and processed
- [ ] All 96 components evaluated and migrated
- [ ] Zero broken internal references
- [ ] No sensitive data in repository
- [ ] All deprecated content properly archived
- [ ] Migration path documented and tested
- [ ] User communication sent
- [ ] Git history preserved with tags
- [ ] Performance targets met
- [ ] Security scan passed

## Rollback Plan

If transformation needs reverting:
```bash
# Restore from tag
git checkout v1.0-pre-transformation

# Or restore specific components
git checkout v1.0-pre-transformation -- .claude/

# Communicate rollback
echo "Transformation rolled back due to [reason]" > ROLLBACK-NOTICE.md
```

## Post-Cleanup Validation

Run these checks after cleanup:
```bash
# No orphaned files
find . -name "*.md" -type f | xargs grep -l "404\|not found\|missing"

# No broken YAML
find .claude-context -name "*.md" -exec sh -c 'head -n 20 {} | grep -E "^---$" | wc -l' \; | grep -v "2"

# No large files
find . -size +1M -type f

# Clean git status
git status --porcelain
```

## Timeline

- **Day 1-2**: Complete inventory
- **Day 3-4**: Begin file migration
- **Day 5-7**: Process transformations
- **Week 2**: Migration tools
- **Week 3**: Deprecation notices
- **Week 4**: Repository cleanup
- **Week 5**: Security & QA
- **Week 6**: Final validation