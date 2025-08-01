# Documentation & Report XML Template

This template provides a simplified XML metadata structure for documentation, reports, and analysis files.

## Template Structure

```xml
<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>{{documentation|report|analysis}}</document_type>
  <ai_consumption_priority>{{high|medium|low}}</ai_consumption_priority>
  <content_structure>{{markdown_body|structured_report|analysis_data}}</content_structure>
  <file_path>{{FULL_FILE_PATH}}</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<document_metadata>
  <document_purpose>{{PURPOSE_DESCRIPTION}}</document_purpose>
  <target_audience>{{USER_TYPE}}</target_audience>
  <content_category>{{CATEGORY_NAME}}</content_category>
  <information_type>{{instructional|reference|analysis|status}}</information_type>
</document_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>{{DISCOVERY_PATH}}</primary_discovery_path>
    <document_role>{{user_guide|technical_reference|project_status|analysis_report}}</document_role>
  </discovery_metadata>
  
  <relationship_map>
    <related_documentation>
      <file type="{{TYPE}}" ref="{{FILE_REFERENCE}}" relation="{{RELATIONSHIP}}"/>
    </related_documentation>
    <covers_topics>
      <topic>{{TOPIC_NAME}}</topic>
    </covers_topics>
  </relationship_map>
  
  <ai_search_optimization>
    <keywords>{{KEYWORD_LIST}}</keywords>
    <semantic_tags>{{SEMANTIC_TAG_LIST}}</semantic_tags>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>{{local|project|global}}</scope_level>
    <context_retention>{{temporary|session|persistent}}</context_retention>
    <memory_priority>{{1-10}}</memory_priority>
  </ai_understanding_scope>
  
  <usage_guidance>
    <when_to_reference>
      <scenario>{{SCENARIO_DESCRIPTION}}</scenario>
    </when_to_reference>
    <information_value>{{INFORMATION_VALUE}}</information_value>
  </usage_guidance>
</context_engineering>
<!-- AI_METADATA_END -->
```

## Document Types

### Primary Document Types
- `documentation`: User-facing guides, setup instructions, usage documentation
- `report`: Analysis reports, assessment results, project status reports
- `analysis`: Technical analysis, performance reports, deep-dive investigations

### Content Categories
- `user_guide`: End-user documentation and instructions
- `technical_reference`: Technical specifications and references
- `project_management`: Project status, planning, and coordination
- `quality_assurance`: Testing, validation, and quality reports
- `architecture`: System design and architectural documentation
- `analysis`: Deep analysis and investigation reports

### Information Types
- `instructional`: Step-by-step guides and how-to documentation
- `reference`: Reference materials and specifications
- `analysis`: Research, analysis, and investigation results
- `status`: Project status, progress reports, and summaries

### Target Audiences
- `end_users`: People using the template library
- `developers`: People customizing or extending the system
- `maintainers`: People responsible for system maintenance
- `researchers`: People studying the system or its patterns
- `stakeholders`: Project stakeholders and decision makers

## Simplified Template for Basic Reports

For simple analysis reports and status files, use this minimal template:

```xml
<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>report</document_type>
  <ai_consumption_priority>low</ai_consumption_priority>
  <content_structure>structured_report</content_structure>
  <file_path>{{FULL_FILE_PATH}}</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<document_metadata>
  <document_purpose>[BRIEF_PURPOSE]</document_purpose>
  <content_category>[CATEGORY]</content_category>
</document_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>[PATH]</primary_discovery_path>
  </discovery_metadata>
  
  <ai_search_optimization>
    <keywords>{{KEYWORD_LIST}}</keywords>
    <semantic_tags>{{SEMANTIC_TAG_LIST}}</semantic_tags>
  </ai_search_optimization>
</ai_navigation>
<!-- AI_METADATA_END -->
```

## Usage Notes

### Priority Guidelines
- `high`: Important user documentation, architectural guides
- `medium`: Technical references, detailed reports
- `low`: Status reports, temporary analysis files

### Memory Priority Guidelines
- `1-3`: Temporary reports and status files
- `4-6`: Technical references and analysis
- `7-10`: Critical user documentation and guides

### Batch Processing Notes
- Use simplified template for reports/ directory files
- Use full template for docs/ directory files
- Group similar file types for consistent tagging
- Focus on discoverability rather than deep analysis