# Migration Guide for Claude Code Template Library Updates

This guide helps users migrate from previous versions of the template library while preserving their customizations and ensuring compatibility with new features.

## Overview

The Claude Code Template Library evolves continuously. This guide provides systematic approaches for updating your customized framework while preserving your project-specific adaptations.

## Version Compatibility Matrix

| Your Version | Target Version | Migration Complexity | Estimated Time |
|--------------|----------------|---------------------|----------------|
| v0.x | v1.0 | High - Major restructure | 4-6 hours |
| v1.0.x | v1.1.x | Medium - Feature additions | 1-2 hours |
| v1.1.x | v1.2.x | Low - Minor updates | 30-60 minutes |

## Pre-Migration Assessment

### Step 1: Backup Current Setup

**Complete Backup**:
```bash
# Create timestamped backup
BACKUP_DATE=$(date +%Y%m%d_%H%M%S)
cp -r .claude .claude-backup-$BACKUP_DATE
cp CLAUDE.md CLAUDE-backup-$BACKUP_DATE.md

# Commit current state
git add .claude CLAUDE.md
git commit -m "Backup before template library migration to v1.0"
```

**Document Current Customizations**:
```bash
# Generate customization summary
/share-adaptation --format=migration-backup > migration-backup-$BACKUP_DATE.yaml

# List all modified commands
find .claude/commands -name "*.md" -newer .claude-backup-$BACKUP_DATE | 
sort > modified-commands-$BACKUP_DATE.txt

# Inventory replaced placeholders
grep -r "\[INSERT_" .claude/commands/ > remaining-placeholders-$BACKUP_DATE.txt || echo "All placeholders replaced"
```

### Step 2: Assess Compatibility

**Check Framework Dependencies**:
```bash
# Identify dependency conflicts
/validate-adaptation --migration-check --target-version=v1.0

# Check for deprecated commands
find .claude/commands/deprecated -name "*.md" | wc -l

# Verify custom commands
find .claude/commands -name "*.md" ! -path "*/deprecated/*" | 
xargs grep -l "INSERT_CUSTOM_" | sort > custom-commands-$BACKUP_DATE.txt
```

**Identify Breaking Changes**:
```markdown
## Common Breaking Changes by Version

### v0.x to v1.0 (Major Migration)
- **Command Structure**: YAML front matter required for all commands
- **Directory Layout**: New organization with deprecated/ folder
- **Placeholder Names**: Standardized placeholder naming convention
- **Guide Commands**: New meta command system for adaptation
- **Context System**: New component-based context architecture

### v1.0.x to v1.1.x (Feature Migration)
- **New Commands**: Additional specialized commands added
- **Enhanced Meta**: Improved guide command functionality
- **Context Optimization**: Better component loading patterns
- **Security Updates**: Enhanced security validation patterns

### v1.1.x to v1.2.x (Maintenance Migration)
- **Bug Fixes**: Resolved placeholder and template issues
- **Performance**: Improved command loading and execution
- **Documentation**: Enhanced customization guides
- **Validation**: Better error detection and recovery
```

## Migration Strategies

### Strategy 1: Clean Migration (Recommended for Major Versions)

**Best For**: v0.x → v1.0, heavily customized frameworks, teams wanting fresh start

**Process**:
```bash
# 1. Setup new framework alongside old
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework-new
cd .claude-framework-new && ./setup.sh --target-dir ../.claude-new

# 2. Run fresh adaptation
cd ..
/adapt-to-project --target-dir .claude-new --import-config migration-backup-$BACKUP_DATE.yaml

# 3. Migrate custom commands selectively
for cmd in $(cat custom-commands-$BACKUP_DATE.txt); do
  echo "Reviewing: $cmd"
  diff .claude/$cmd .claude-new/$cmd || echo "Manual merge needed"
done

# 4. Validate new setup
/validate-adaptation --directory .claude-new --verbose

# 5. Switch to new framework
mv .claude .claude-old
mv .claude-new .claude
```

**Advantages**:
- Clean start with latest best practices
- No legacy configuration debt
- Full access to new features
- Comprehensive validation

**Disadvantages**:
- Requires re-customization effort
- May lose subtle customizations
- Team retraining needed

### Strategy 2: Incremental Migration (Recommended for Minor Versions)

**Best For**: v1.0.x → v1.1.x, lightly customized frameworks, continuous integration

**Process**:
```bash
# 1. Update reference framework
git submodule update --remote .claude-framework

# 2. Identify changes
/sync-from-reference --preview --show-changes

# 3. Merge changes selectively
/sync-from-reference --interactive --preserve-customizations

# 4. Update customizations for new features
/adapt-to-project --incremental --new-features-only

# 5. Validate updated setup
/validate-adaptation --focus=new-features
```

**Advantages**:
- Preserves existing customizations
- Minimal disruption to team
- Gradual adoption of new features
- Lower time investment

**Disadvantages**:
- May accumulate technical debt
- Complex conflict resolution
- Limited access to structural improvements

### Strategy 3: Hybrid Migration (Balanced Approach)

**Best For**: Teams with extensive customizations wanting new features

**Process**:
```bash
# 1. Clean migration for core commands
/migrate --clean --category=core,meta --preserve-config

# 2. Incremental for customized commands
/migrate --incremental --category=development,quality,infrastructure

# 3. Manual review for heavily modified commands
/migrate --manual-review --high-customization-commands

# 4. Comprehensive validation
/validate-adaptation --comprehensive --migration-report
```

## Command-Specific Migration Patterns

### Core Commands Migration

**`/task` Command Evolution**:
```markdown
## v0.x → v1.0 Migration for /task

### Breaking Changes
- YAML front matter now required
- Standardized placeholder names
- Enhanced argument handling

### Migration Steps
1. **Add YAML front matter**:
```yaml
---
name: /task
description: "Execute focused development task for [INSERT_PROJECT_NAME]"
argument-hint: "[task_description]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---
```

2. **Update placeholder names**:
```bash
# Old → New placeholder mapping
s/\[PROJECT_NAME\]/[INSERT_PROJECT_NAME]/g
s/\[TECH_STACK\]/[INSERT_TECH_STACK]/g
s/\[DOMAIN\]/[INSERT_DOMAIN]/g
```

3. **Preserve customizations**:
```markdown
# Your custom workflow steps remain the same
1. **Analysis**: Understand requirements...
2. **Design**: Plan implementation...
# (Keep your custom process)
```
```

### Meta Commands Migration

**New Guide System**:
```markdown
## Guide Commands (New in v1.0)

### Migration Impact
- `/adapt-to-project` replaces manual customization workflow
- `/validate-adaptation` provides systematic validation
- `/sync-from-reference` handles future updates

### Adoption Strategy
1. **Try new guide commands** with existing setup
2. **Compare results** with your manual customizations
3. **Gradually adopt** guide-based workflow
4. **Train team** on new meta command system
```

### Infrastructure Commands Migration

**Security Command Updates**:
```markdown
## Security Commands Evolution

### v1.0 Enhancements
- Enhanced compliance validation
- Industry-specific security patterns
- Automated vulnerability scanning integration

### Migration Steps
1. **Review security requirements**:
```bash
# Check current security customizations
grep -r "security\|compliance" .claude/commands/security/

# Compare with new security patterns
diff .claude/commands/security/ .claude-framework/commands/security/
```

2. **Update compliance configurations**:
```yaml
# Enhanced security configuration
security_config:
  compliance_frameworks: ["PCI DSS", "GDPR", "SOX"]
  vulnerability_scanning: "automated"
  security_review_required: true
  penetration_testing: "quarterly"
```
```

## Domain-Specific Migration Guidance

### E-commerce Platform Migration

**Business Logic Preservation**:
```markdown
## E-commerce Migration Checklist

### Critical Customizations to Preserve
- [ ] Payment processing workflows
- [ ] Inventory management logic
- [ ] Customer authentication patterns
- [ ] Order fulfillment processes
- [ ] Compliance requirements (PCI DSS)

### New Features to Adopt
- [ ] Enhanced security validation for payment data
- [ ] Performance optimization for high-traffic scenarios
- [ ] A/B testing framework integration
- [ ] Advanced monitoring for business metrics

### Migration Command Sequence
```bash
# 1. Backup payment processing commands
cp -r .claude/commands/specialized/payment-* /backup/

# 2. Migrate with payment processing preservation
/migrate --preserve-business-logic --focus=payment-processing

# 3. Validate payment workflow integrity
/validate-adaptation --category=payment --compliance=pci-dss
```
```

### Data Science Platform Migration

**ML Workflow Preservation**:
```markdown
## ML Platform Migration Checklist

### Critical Customizations to Preserve
- [ ] Model training pipelines
- [ ] Data validation workflows
- [ ] Experiment tracking integration
- [ ] Model deployment patterns
- [ ] Compliance requirements (GDPR)

### New Features to Adopt
- [ ] Enhanced model monitoring
- [ ] Automated bias detection
- [ ] MLOps pipeline improvements
- [ ] Advanced experiment management

### Migration Command Sequence
```bash
# 1. Backup ML-specific commands
cp -r .claude/commands/data-science/ /backup/

# 2. Migrate with ML workflow preservation
/migrate --preserve-ml-workflows --maintain-experiment-tracking

# 3. Validate ML pipeline integrity
/validate-adaptation --category=ml --compliance=gdpr
```
```

## Post-Migration Validation

### Comprehensive Testing

**Functional Validation**:
```bash
# Test core workflow commands
/task "implement user authentication" --test-mode
/dev format --dry-run
/test unit "src/" --preview

# Test meta commands
/adapt-to-project --dry-run --validate-config
/validate-adaptation --comprehensive

# Test domain-specific commands
/api-design "user-profile" "GET" --preview
/deploy staging --dry-run --validation-only
```

**Team Validation**:
```bash
# Team acceptance testing
echo "Team Validation Checklist:"
echo "[ ] Core commands work as expected"
echo "[ ] Customizations preserved correctly"
echo "[ ] New features accessible and useful"
echo "[ ] Documentation reflects changes"
echo "[ ] Team training completed"
```

### Performance Validation

**Command Performance**:
```bash
# Benchmark command execution
time /task "sample task" --benchmark-mode
time /analyze-code comprehensive --performance-test
time /test all --timing-analysis

# Compare with pre-migration performance
echo "Performance comparison:"
echo "Pre-migration average: X seconds"
echo "Post-migration average: Y seconds"
echo "Performance change: Z% improvement/degradation"
```

## Rollback Procedures

### Emergency Rollback

**Immediate Rollback**:
```bash
# Quick rollback to previous version
mv .claude .claude-failed-migration
mv .claude-backup-$BACKUP_DATE .claude
cp CLAUDE-backup-$BACKUP_DATE.md CLAUDE.md

# Verify rollback success
/validate-adaptation --quick-check
git add .claude CLAUDE.md
git commit -m "Emergency rollback from failed migration"
```

### Partial Rollback

**Selective Command Rollback**:
```bash
# Rollback specific command category
cp -r .claude-backup-$BACKUP_DATE/commands/development .claude/commands/

# Rollback individual command
cp .claude-backup-$BACKUP_DATE/commands/core/task.md .claude/commands/core/

# Validate partial rollback
/validate-adaptation --category=development
```

## Migration Troubleshooting

### Common Issues and Solutions

**Issue 1: Placeholder Conflicts**
```bash
# Problem: Old and new placeholder formats mixed
grep -r "\[PROJECT_NAME\]" .claude/commands/  # Old format
grep -r "\[INSERT_PROJECT_NAME\]" .claude/commands/  # New format

# Solution: Systematic replacement
/replace-placeholders --migrate-format --old-to-new
```

**Issue 2: Missing Dependencies**
```bash
# Problem: New commands reference tools not in your stack
grep -r "MISSING_TOOL" .claude/commands/

# Solution: Update tool references
/adapt-to-project --fix-tool-references --current-stack-only
```

**Issue 3: Broken Customizations**
```bash
# Problem: Custom logic doesn't work with new structure
/validate-adaptation --find-broken-customizations

# Solution: Merge custom logic with new patterns
/migrate --merge-custom-logic --interactive-review
```

### Recovery Strategies

**Configuration Recovery**:
```bash
# Recover configuration from backup
cp migration-backup-$BACKUP_DATE.yaml .claude/config/
/import-pattern migration-backup-$BACKUP_DATE.yaml --merge-mode

# Rebuild configuration from scratch
/adapt-to-project --guided --import-previous-answers
```

**Team Knowledge Transfer**:
```markdown
## Post-Migration Team Training

### Training Schedule
- **Week 1**: Introduction to new features and changes
- **Week 2**: Hands-on practice with migrated commands
- **Week 3**: Team feedback and refinement
- **Week 4**: Full adoption and knowledge sharing

### Training Materials
- Migration change log and impact summary
- Updated command documentation
- Hands-on exercises with real project scenarios
- Q&A sessions and feedback collection
```

## Version-Specific Migration Notes

### v0.x to v1.0 Migration

**Major Changes**:
- Complete directory restructure
- Introduction of guide command system
- Standardized placeholder naming
- Enhanced component architecture

**Migration Time**: 4-6 hours for full migration
**Recommended Approach**: Clean migration with selective customization preservation

### v1.0.x to v1.1.x Migration

**Changes**:
- Additional specialized commands
- Enhanced meta command functionality
- Improved context loading
- Security pattern updates

**Migration Time**: 1-2 hours
**Recommended Approach**: Incremental migration with feature adoption

### Future Migration Preparation

**Best Practices for Easier Future Migrations**:
1. **Document Customizations**: Use `/share-adaptation` regularly
2. **Centralize Configuration**: Keep project-specific settings in config files
3. **Minimize Hard-Coding**: Prefer placeholder-based customization
4. **Regular Updates**: Don't skip minor versions
5. **Team Training**: Keep team updated on framework changes

---

*This migration guide ensures smooth transitions between template library versions while preserving your valuable customizations and team investment.*