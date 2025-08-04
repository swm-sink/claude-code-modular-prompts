# XML Tagging Standards for AI Consumption

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>documentation</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/raleigh/docs/xml-schema/xml-tagging-standards.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<document_metadata>
  <document_purpose>XML tagging standards and implementation guidelines</document_purpose>
  <target_audience>developers</target_audience>
  <content_category>technical_reference</content_category>
  <information_type>reference</information_type>
</document_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>xml_schema_documentation</primary_discovery_path>
    <document_role>technical_reference</document_role>
  </discovery_metadata>
  
  <ai_search_optimization>
    <keywords>xml_tagging xml_standards ai_metadata xml_implementation</keywords>
    <semantic_tags>xml_schema technical_standards implementation_guide</semantic_tags>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
</context_engineering>
<!-- AI_METADATA_END -->

## Purpose

This document establishes consistent implementation guidelines for applying XML tags across the Claude Context Architect system. These standards ensure uniform AI consumption patterns and maintainable metadata infrastructure.

## Core Tagging Principles

### 1. AI-Only Visibility
- XML tags are wrapped in HTML comments: `<!-- AI_METADATA_START -->` and `<!-- AI_METADATA_END -->`
- Tags remain invisible to human readers in rendered markdown
- AI parsers specifically look for these delimiters

### 2. Non-Invasive Integration
- XML metadata appears AFTER YAML frontmatter
- Never modify existing YAML structure
- Maintain backward compatibility with current Claude Code

### 3. Consistent Hierarchy
- Document metadata → Component/Command metadata → Navigation metadata → Context metadata
- Each level provides progressively more specific information
- Lower levels can reference higher level IDs

## Tag Placement Standards

### For Commands (.claude/commands/**/*.md)

```markdown
---
command: example-command
description: Command description
allowed-tools:
- Read
- Write
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/absolute/path/to/command.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <!-- Command-specific metadata -->
</command_metadata>

<ai_navigation>
  <!-- Navigation and discovery metadata -->
</ai_navigation>

<context_engineering>
  <!-- Context and workflow metadata -->
</context_engineering>
<!-- AI_METADATA_END -->

# Command Title

[Regular markdown content...]
```

### For Components (.claude/components/**/*.md)

```markdown
# Component Name

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/absolute/path/to/component.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <!-- Component-specific metadata -->
</component_metadata>

<ai_navigation>
  <!-- Navigation and discovery metadata -->
</ai_navigation>
<!-- AI_METADATA_END -->

```
Component implementation details...
```
```

## Naming Conventions

### Element Names
- Use lowercase with underscores: `component_metadata`, `ai_navigation`
- Be descriptive but concise: `assembly_compatibility` not `comp_compat`
- Maintain consistency across all files

### Attribute Names
- Use lowercase, no underscores: `ref`, `type`, `role`
- Boolean attributes: `required`, `enabled`, `deprecated`
- Enumerated values: lowercase with underscores

### ID References
- Component IDs: Match filename without extension: `file-reader`, `data-transformer`
- Command IDs: Match YAML `command` field value
- Use `ref` attribute for cross-references

## Value Standards

### Priority Levels
```xml
<ai_consumption_priority>critical|high|medium|low</ai_consumption_priority>
```
- **critical**: Core commands/components essential for basic functionality
- **high**: Frequently used, important for most workflows
- **medium**: Specialized but valuable for specific use cases
- **low**: Experimental, deprecated, or rarely used

### Complexity Ratings
```xml
<usage_complexity>simple|intermediate|advanced</usage_complexity>
```
- **simple**: No prerequisites, immediate use
- **intermediate**: Some experience required, 5-30 minutes to understand
- **advanced**: Expert knowledge needed, complex configuration

### Relationship Strengths
```xml
<component ref="error-handler" strength="required|strong|medium|weak|incompatible"/>
```
- **required**: Cannot function without this component
- **strong**: Works best with this component
- **medium**: Often used together
- **weak**: Can work together but not common
- **incompatible**: Should not be used together

## Metadata Categories

### 1. Document Metadata (Required for All)
- `document_type`: Identifies file category
- `ai_consumption_priority`: Helps AI prioritize processing
- `content_structure`: Describes file format
- `file_path`: Absolute path for reference
- `last_modified`: ISO 8601 timestamp
- `ai_index_version`: Schema version tracking

### 2. Component-Specific Metadata
- `component_id`: Unique identifier
- `category`: High-level grouping (atomic, analysis, etc.)
- `subcategory`: Specific functionality group
- `complexity_metrics`: Usage difficulty indicators
- `assembly_compatibility`: Component relationships
- `usage_patterns`: Common use cases

### 3. Command-Specific Metadata
- `command_id`: Unique identifier
- `progressive_disclosure_layer`: 1, 2, or 3
- `component_dependencies`: Required/optional components
- `orchestration_capability`: Command chaining features
- `v2_features`: Version 2.0 enhancements

### 4. Navigation Metadata
- `discovery_metadata`: How AI finds this content
- `relationship_map`: Connections to other files
- `usage_context`: When to use/avoid
- `ai_search_optimization`: Search enhancement data

### 5. Context Engineering
- `ai_understanding_scope`: Local/project/global context
- `knowledge_dependencies`: Required background
- `workflow_integration`: Process positioning
- `ai_learning_markers`: Skill progression tracking

## Validation Requirements

### Structural Validation
1. Well-formed XML (proper nesting, closed tags)
2. Required elements present for document type
3. Valid enumerated values used
4. Cross-references point to existing files

### Semantic Validation
1. Component counts match actual files (91 components)
2. Command counts match actual files (88 commands)
3. Layer assignments align with Progressive Disclosure design
4. Compatibility rules don't create circular dependencies

### Consistency Validation
1. IDs match filenames/YAML values
2. Timestamps use ISO 8601 format
3. File paths are absolute and valid
4. Version numbers follow semantic versioning

## Maintenance Guidelines

### Adding New Files
1. Copy appropriate template based on file type
2. Fill in all required metadata fields
3. Update relationship references in related files
4. Regenerate central AI index
5. Validate with automated tools

### Updating Existing Files
1. Increment `last_modified` timestamp
2. Update any changed relationships
3. Verify compatibility rules still valid
4. Check for orphaned references
5. Test with AI navigation tools

### Deprecation Process
1. Set `deprecation_status` to "deprecated"
2. Add `deprecation_date` timestamp
3. Update `ai_consumption_priority` to "low"
4. Add migration guidance in metadata
5. Maintain for backward compatibility

## Anti-Patterns to Avoid

### 1. Metadata Bloat
❌ Don't add speculative or "might be useful" metadata
✅ Only include metadata that AI actively uses

### 2. Manual Synchronization
❌ Don't manually maintain counts or relationships
✅ Use automated tools to generate and validate

### 3. Breaking Changes
❌ Don't rename IDs or change structures
✅ Version changes, maintain compatibility

### 4. Human-Readable Formatting
❌ Don't format XML for human reading
✅ Optimize for AI parsing efficiency

### 5. Inline Metadata
❌ Don't scatter metadata throughout content
✅ Centralize in designated sections

## Quality Checklist

Before committing XML-tagged files:

- [ ] All required elements present
- [ ] Values conform to enumerated types
- [ ] Cross-references validated
- [ ] Timestamps updated
- [ ] AI index regenerated
- [ ] Automated validation passes
- [ ] Backward compatibility maintained
- [ ] No sensitive information exposed

## Tools and Automation

### Validation Script Usage
```bash
# Validate single file
./scripts/validate-xml-metadata.py .claude/commands/core/task.md

# Validate all files
./scripts/validate-xml-metadata.py --all

# Generate AI index
./scripts/generate-ai-index.py
```

### Pre-commit Hooks
```yaml
- repo: local
  hooks:
    - id: validate-xml-metadata
      name: Validate XML Metadata
      entry: ./scripts/validate-xml-metadata.py
      language: python
      files: \.md$
```

## Version History

- v1.0 (2025-07-31): Initial XML tagging standards
- Future versions will maintain backward compatibility

---

These standards ensure consistent, maintainable, and effective XML metadata implementation across the Claude Code Modular Prompts template library, optimizing AI consumption and navigation capabilities.