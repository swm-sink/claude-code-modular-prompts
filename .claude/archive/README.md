# Framework Archive

<archive_status>
  <last_reviewed>2025-07-06</last_reviewed>
  <status>Clean - No redundant content</status>
  <reviewer>Phase 5 Archive Review</reviewer>
</archive_status>

## Purpose

This directory serves as a holding area for framework components that:
1. Have historical value but are superseded by current modules
2. Are being evaluated for potential reintegration
3. Represent experimental features not yet ready for production

## Archive Principles

<principles>
  <principle name="zero_redundancy">Nothing archived if identical content exists in active modules</principle>
  <principle name="historical_value">Preserve only content with unique historical or developmental significance</principle>
  <principle name="clear_rationale">Every archived item must have documented preservation reasoning</principle>
  <principle name="regular_review">Archive reviewed during each major framework version</principle>
</principles>

## Recent Archive History

### Phase 5 Review (2025-07-06)

**Action**: Complete cleanup of redundant archive content

**Removed Files**:
- `rules/aware-framework.md` → Redundant with CLAUDE.md cognitive process
- `rules/claude-code-integration.md` → Redundant with modules/patterns/tool-usage.md
- `rules/critical-thinking-enforcement.md` → Redundant with modules/quality/critical-thinking.md
- `rules/honesty-policy.md` → Redundant with modules/quality/honesty-policy.md
- `rules/native-patterns.md` → Redundant with modules/patterns/multi-agent.md
- `rules/production-standards.md` → Redundant with modules/quality/production-standards.md
- `rules/tdd-standards.md` → Redundant with modules/quality/tdd.md

**Rationale**: All 7 files contained content that exists identically in the current active framework modules. Maintaining these duplicates violated the framework's core "zero redundancy" principle and created potential for inconsistency.

**Evidence**: Side-by-side comparison confirmed 100% content overlap with current modules.

## Archive Guidelines

### When to Archive

<guidelines>
  <archive_when>
    <scenario>Module being replaced but has unique historical implementation</scenario>
    <scenario>Experimental feature being temporarily shelved</scenario>
    <scenario>Deprecated approach that may inform future decisions</scenario>
  </archive_when>
  
  <never_archive>
    <scenario>Content identical to active modules</scenario>
    <scenario>Broken or non-functional code</scenario>
    <scenario>Outdated information with no historical value</scenario>
  </never_archive>
</guidelines>

### Archive Structure

When items are archived, they should follow this structure:
```
archive/
├── README.md (this file)
├── deprecated/          # Superseded but historically valuable
├── experimental/        # Shelved experiments
└── legacy/             # Old implementations with historical value
```

## Framework Integration

The archive is:
- **NOT** loaded by any commands or modules
- **NOT** referenced in active framework code
- **ONLY** for historical reference and development context
- **REVIEWED** during major framework updates

## Next Review

The archive should be reviewed again during:
- Framework version 3.0.0 development
- Major architectural changes
- Annual framework health audits

---

*This archive maintains framework integrity by preventing redundancy while preserving valuable development history.*