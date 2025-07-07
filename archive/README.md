# Claude Code Framework Archive

**Purpose:** Systematic preservation of historical framework components, deprecated modules, and documentation artifacts

## Archive Structure

```
archive/
├── README.md                      # This file - Archive documentation and guidelines
├── 2025/                         # Year-based organization
│   └── 01/                       # Month-based subdirectories
│       └── orphaned-modules/     # Modules archived during cleanup
│           ├── README.md         # Specific archive documentation
│           ├── patterns/         # Pattern-related modules
│           ├── quality/          # Quality-related modules
│           └── testing/          # Testing-related modules
├── deprecated-commands/          # Archived command implementations
├── legacy-tools/                 # Historical tools and scripts
├── documentation-history/        # Previous documentation versions
└── experimental/                 # Experimental features that didn't make production

```

## Archive Categories

### 1. Orphaned Modules
**Location:** `YYYY/MM/orphaned-modules/`  
**Purpose:** Modules that are no longer referenced by active commands but may contain valuable patterns or implementations for future reference.

### 2. Deprecated Commands
**Location:** `deprecated-commands/`  
**Purpose:** Command implementations that have been superseded or removed from the active framework.

### 3. Legacy Tools
**Location:** `legacy-tools/`  
**Purpose:** Tools, scripts, and utilities that are no longer actively maintained but may be useful for historical reference.

### 4. Documentation History
**Location:** `documentation-history/`  
**Purpose:** Previous versions of documentation that show the evolution of the framework.

### 5. Experimental Features
**Location:** `experimental/`  
**Purpose:** Features that were explored but not integrated into the production framework.

## Archive Principles

### 1. Preservation Over Deletion
- Archive content rather than deleting to maintain historical context
- Preserve implementation patterns that may be useful in the future
- Maintain documentation that shows framework evolution

### 2. Clear Organization
- Use year/month structure for time-based archival
- Maintain category-specific directories for logical grouping
- Include README files in each archive section

### 3. Metadata Documentation
- Document **when** items were archived
- Document **why** items were archived
- Document **what** functionality they provided
- Document **how** to recover if needed

## Archive Process

### When to Archive

1. **Module Orphaning:** When modules are no longer referenced by any active command
2. **Feature Deprecation:** When features are replaced by better implementations
3. **Tool Obsolescence:** When tools are superseded by framework capabilities
4. **Documentation Updates:** When documentation is significantly revised

### How to Archive

1. **Identify Content:** Determine what needs to be archived and why
2. **Choose Location:** Select appropriate archive category and create dated subdirectory
3. **Move Content:** Move files to archive location preserving structure
4. **Document Action:** Create/update README in archive location with:
   - Archive date and reason
   - Original location and purpose
   - Recovery instructions if applicable
   - Related GitHub issues or PRs

### Archive Metadata Template

```markdown
# [Component Name] Archive

**Archive Date:** YYYY-MM-DD  
**Original Location:** /path/to/original/  
**Reason:** Brief explanation of why archived  
**Related Issues:** #XX, #YY

## Summary
Brief description of what was archived and its original purpose.

## Contents
- List of archived files/directories
- Original functionality description

## Recovery Instructions
If this content needs to be recovered:
1. Steps to restore functionality
2. Integration requirements
3. Testing considerations
```

## Archive Maintenance

### Quarterly Review
- Review archive contents for permanent deletion candidates
- Consolidate similar archived items
- Update archive documentation

### Annual Cleanup
- Move items older than 2 years to cold storage
- Create annual archive summary report
- Update archive structure as needed

## Search and Recovery

### Finding Archived Content
1. Check archive README files for descriptions
2. Use `grep -r "search term" archive/` for content search
3. Review archive metadata for categorization

### Recovering Archived Content
1. Locate content in appropriate archive section
2. Review archive documentation for context
3. Extract needed functionality (don't restore wholesale)
4. Integrate following current framework patterns
5. Update tests and documentation

## Archive Best Practices

1. **Never Archive Active Content:** Ensure content is truly unused before archiving
2. **Preserve Context:** Always include documentation about why content was archived
3. **Maintain Structure:** Keep related files together in archive
4. **Document Relationships:** Note dependencies and related components
5. **Enable Discovery:** Use clear naming and comprehensive READMEs

## Archive Statistics

- **Total Archived Modules:** 15 (as of 2025-01-07)
- **Archive Categories:** 5 active categories
- **Oldest Archive:** 2025-01 (orphaned modules)
- **Latest Update:** 2025-01-07

## Contributing to Archive

When adding to the archive:
1. Follow the established structure
2. Create comprehensive documentation
3. Update this README with statistics
4. Link related GitHub issues
5. Notify team of significant archival actions

---

*The archive is a living historical record of the Claude Code Framework's evolution. Treat it with the same care as active code.*