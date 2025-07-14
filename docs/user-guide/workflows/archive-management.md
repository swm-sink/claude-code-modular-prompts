| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |


# Archive Management Procedures

**PURPOSE**: Manage deprecated code and documentation with smart dependency analysis


# Overview

The Claude Code framework's enhanced archive management system provides intelligent handling of deprecated modules, outdated documentation, and completed experiments while ensuring no active dependencies are broken.


# Archive Structure

```
/archive/
├── modules/          # Deprecated framework modules
├── commands/         # Outdated command implementations
├── reports/          # Historical analysis and reports
├── experiments/      # Completed experimental code
└── documentation/    # Superseded documentation
```


# Archival Process


# Step 1: Smart Dependency Analysis

Before archiving any file, the system performs comprehensive analysis:

```bash

# Automatic dependency scanning
- Recursive dependency scanning across all file types
- Cross-reference analysis including comments
- Import/export relationship mapping
- Dynamic reference detection (eval, require, etc.)
```


# Step 2: Graduated Archival

```xml
<archival_phases>
  <phase name = "deprecation">
    Mark with warning notices
    Update dependent files
  </phase>
  <phase name = "staging">
    Move to staging area
    Validation period (7 days)
  </phase>
  <phase name = "archival">
    Final move to /archive
    Complete audit trail
  </phase>
</archival_phases>
```


# Step 3: Validation

All archival operations undergo rigorous validation:
- Full test suite execution
- Command validation across modules
- Documentation link verification
- Performance regression testing


# Archival Triggers


# Automatic Triggers

```xml
<triggers>
  <time_based>Files unused for 90+ days</time_based>
  <version_based>Superseded by newer versions</version_based>
  <dependency_based>No active references found</dependency_based>
  <quality_based>Below quality thresholds</quality_based>
</triggers>
```


# Manual Archival

For immediate archival needs:

```bash

# Archive a specific module
/task archive .claude/modules/old-module.md


# Archive with validation
/task archive --validate .claude/commands/deprecated-command.md
```


# Retention Policies

```xml
<retention_periods>
  <code_modules>5 years minimum</code_modules>
  <documentation>3 years minimum</documentation>
  <reports>1 year minimum</reports>
  <experiments>6 months minimum</experiments>
</retention_periods>
```


# Exceptions

- Security-related code: Permanent retention
- Core framework versions: Permanent retention
- User data: Follow data protection regulations


# Recovery Procedures


# Quick Restoration

```bash

# Restore archived file
/task restore /archive/.claude/modules/useful-module.md


# Restore with dependencies
/task restore --with-deps /archive/.claude/modules/feature-set.md
```


# Selective Recovery

```xml
<recovery_options>
  <full>Complete file restoration</full>
  <partial>Specific functions or sections</partial>
  <reference>Read-only access for reference</reference>
  <bridge>Compatibility layer creation</bridge>
</recovery_options>
```


# Best Practices


# Before Archiving

1. **Run dependency check**: Ensure no active code depends on the file
2. **Update references**: Modify any references to point to alternatives
3. **Document reason**: Add archival reason to audit log
4. **Test thoroughly**: Run full test suite after archival


# Archive Organization

```xml
<organization_rules>
  <rule>Maintain original directory structure in archive</rule>
  <rule>Add README.md explaining archival reason</rule>
  <rule>Include timestamp in archived filename</rule>
  <rule>Preserve git history through moves</rule>
</organization_rules>
```


# Monitoring and Metrics


# Archive Health Metrics

```xml
<metrics>
  <size>Total archive size and growth rate</size>
  <access>Frequency of archive access</access>
  <recovery>Number of files restored</recovery>
  <breaks>Dependency breaks detected</breaks>
</metrics>
```


# Automated Monitoring

The system automatically tracks:
- Archive growth patterns
- Access frequency for archived files
- Recovery request patterns
- Broken reference incidents


# Common Scenarios


# Scenario 1: Module Deprecation

```bash

# Old authentication module replaced by new one
1. Mark old module as deprecated
2. Update all imports to new module
3. Run tests to verify compatibility
4. Move to archive after grace period
```


# Scenario 2: Documentation Updates

```bash

# Framework 2.3 docs superseded by 2.4
1. Create new documentation
2. Add forwarding notes in old docs
3. Archive after migration period
4. Maintain redirects for URLs
```


# Scenario 3: Failed Experiments

```bash

# Experimental feature didn't work out
1. Document lessons learned
2. Archive code with explanations
3. Keep for future reference
4. Set 6-month retention
```


# Troubleshooting


# Broken Dependencies After Archival

```bash

# Error: Cannot find module 'archived-module'
Solution:
1. Check archive for the module
2. Restore if actively needed
3. Update imports if alternative exists
4. Create compatibility bridge if needed
```


# Archive Access Issues

```bash

# Error: Permission denied accessing /archive
Solution:
1. Verify archive permissions
2. Check disk space
3. Validate archive integrity
4. Run archive maintenance
```


# Integration with CI/CD


# Pre-Archive Checks

```yaml
archive-check:
  - dependency-scan
  - test-suite
  - documentation-links
  - performance-baseline
```


# Post-Archive Validation

```yaml
post-archive:
  - verify-no-broken-imports
  - check-documentation-links
  - validate-redirects
  - update-archive-index
```


# Future Enhancements

- **AI-powered dependency analysis**: Smarter detection of hidden dependencies
- **Automatic refactoring**: Update code when archiving dependencies
- **Archive search**: Full-text search across archived content
- **Version bridging**: Automatic compatibility layers

**Reference**: See `CLAUDE.md` Enhanced Archive Management section for implementation details

*Smart archival: Preserving the past without breaking the future.*