# AI Navigation Reference for Claude Code Modular Prompts

## Overview

This document provides comprehensive guidance for AI systems to effectively navigate and utilize the XML metadata infrastructure to build modular prompts from components. It focuses on practical navigation workflows and component assembly strategies.

## Navigation Principles

### 1. Progressive Discovery
AI should navigate content in order of decreasing abstraction:
1. **Start with user intent** → Identify appropriate Progressive Disclosure layer
2. **Find relevant commands** → Use layer-specific discovery paths
3. **Analyze dependencies** → Examine component requirements
4. **Assemble components** → Build workflow from compatible parts
5. **Validate assembly** → Ensure compatibility and completeness

### 2. Priority-Based Processing
```xml
<ai_consumption_priority>critical</ai_consumption_priority>
```
- **Always process `critical` files first** - Core functionality
- **Then `high` priority** - Common workflows
- **Consider `medium` for specialized needs**
- **Skip `low` unless specifically needed**

## Navigation Workflows

### Workflow 1: User Request to Command Selection

```
User: "I need to validate API responses"
↓
AI Process:
1. Parse intent: validation + API + responses
2. Search commands with keywords: "validate", "API", "response"
3. Check progressive_disclosure_layer:
   - Layer 1: /quick-command for auto-generation
   - Layer 2: /build-command for customization
   - Layer 3: /assemble-command for complex assembly
4. Select based on user expertise and complexity
```

### Workflow 2: Component Discovery for Command

```xml
<!-- From command metadata -->
<component_dependencies>
  <required_components>
    <component ref="input-validation" role="request_validation"/>
    <component ref="api-caller" role="api_interaction"/>
    <component ref="response-validator" role="response_checking"/>
  </required_components>
</component_dependencies>
```

AI should:
1. Extract all required components
2. Check each component's availability
3. Verify compatibility between components
4. Identify optional enhancements

### Workflow 3: Component Compatibility Checking

```xml
<!-- From component metadata -->
<assembly_compatibility>
  <compatible_components>
    <component ref="error-handler" strength="strong"/>
    <component ref="output-formatter" strength="medium"/>
  </compatible_components>
  <incompatible_components>
    <component ref="file-writer" reason="conflicting_io_operations"/>
  </incompatible_components>
</assembly_compatibility>
```

Compatibility rules:
- **Never combine incompatible components**
- **Prioritize "required" and "strong" relationships**
- **Consider "medium" for enhanced functionality**
- **"Weak" relationships are optional optimizations**

## Component Assembly Strategies

### Strategy 1: Template-Based Assembly
For common workflows, use pre-defined templates:

```xml
<assembly_templates>
  <template name="security-audit">
    <component_sequence>
      <step order="1" component="input-validation" required="true"/>
      <step order="2" component="path-validation" required="true"/>
      <step order="3" component="security-scan" required="true"/>
      <step order="4" component="report-generation" required="true"/>
    </component_sequence>
  </template>
</assembly_templates>
```

### Strategy 2: Dynamic Assembly
For custom workflows, build from components:

1. **Identify workflow stages**: input → processing → validation → output
2. **Select components for each stage**:
   - Input: file-reader, parameter-parser, input-validation
   - Processing: data-transformer, format-converter
   - Validation: response-validator, error-handler
   - Output: output-formatter, file-writer, report-generation

3. **Verify compatibility matrix**:
   ```
   file-reader → data-transformer ✓ (compatible)
   data-transformer → output-formatter ✓ (compatible)
   file-reader → file-writer ✗ (incompatible - conflicting I/O)
   ```

### Strategy 3: Layer-Specific Navigation

#### Layer 1 (Auto-Generation)
```xml
<progressive_disclosure_layer>1</progressive_disclosure_layer>
```
- Focus on command types: search, analyze, transform, validate, report
- Use intelligent templates for instant generation
- No component selection needed - handled automatically

#### Layer 2 (Guided Customization)
```xml
<progressive_disclosure_layer>2</progressive_disclosure_layer>
```
- Present 3-5 configuration options maximum
- Filter components by relevance
- Provide smart defaults

#### Layer 3 (Professional Assembly)
```xml
<progressive_disclosure_layer>3</progressive_disclosure_layer>
```
- Full access to all 91 components
- Support complex multi-component workflows
- Enable advanced orchestration patterns

## Search Optimization Techniques

### 1. Keyword-Based Discovery
```xml
<ai_search_optimization>
  <keywords>task execution development workflow automation testing</keywords>
  <semantic_tags>implementation coding productivity quality_assurance</semantic_tags>
</ai_search_optimization>
```

Search strategy:
- Extract key terms from user request
- Match against keywords and semantic_tags
- Rank by relevance score

### 2. Functionality Vector Matching
```xml
<functionality_vectors>[0.8, 0.2, 0.6, 0.9, 0.3]</functionality_vectors>
```
Vectors represent: [automation, analysis, transformation, validation, reporting]

### 3. Context-Aware Navigation
```xml
<usage_context>
  <when_to_use>
    <scenario>user_needs_focused_task_execution</scenario>
    <scenario>development_workflow_automation</scenario>
  </when_to_use>
  <when_not_to_use>
    <scenario>simple_one_liner_operations</scenario>
  </when_not_to_use>
</usage_context>
```

## Relationship Navigation

### Understanding File Relationships
```xml
<relationship_map>
  <upstream_dependencies>
    <file type="component" ref="file-reader"/>
    <file type="context" ref="prompt-engineering-best-practices"/>
  </upstream_dependencies>
  <downstream_consumers>
    <file type="command" ref="quick-test"/>
    <file type="workflow" ref="data-pipeline-template"/>
  </downstream_consumers>
  <peer_alternatives>
    <file type="command" ref="quick-task" similarity="0.85"/>
  </peer_alternatives>
</relationship_map>
```

Navigation patterns:
- **Upstream**: What this file depends on
- **Downstream**: What depends on this file
- **Peers**: Similar alternatives (similarity > 0.8)

## Context Management

### 1. Scope Levels
```xml
<ai_understanding_scope>
  <scope_level>project</scope_level>
  <context_retention>persistent</context_retention>
  <memory_priority>8</memory_priority>
</ai_understanding_scope>
```

- **Local**: Current command/component only
- **Project**: Entire template library context
- **Global**: Cross-project patterns

### 2. Knowledge Dependencies
```xml
<knowledge_dependencies>
  <required_context>
    <context_file ref="llm-antipatterns.md" importance="critical"/>
    <context_file ref="git-history-antipatterns.md" importance="high"/>
  </required_context>
</knowledge_dependencies>
```

Always load critical context before processing commands.

## Performance Optimization

### 1. Caching Strategy
- Cache frequently used component metadata
- Store validated component assemblies
- Maintain relationship graph in memory

### 2. Lazy Loading
- Load component details only when needed
- Start with metadata, expand to full content
- Prioritize by ai_consumption_priority

### 3. Batch Processing
- Group similar operations
- Process compatible components together
- Validate assemblies in bulk

## Error Recovery

### Common Navigation Errors

1. **Missing Component**
   - Fallback to alternative components
   - Suggest Layer 2 customization
   - Provide manual assembly guidance

2. **Incompatible Assembly**
   - Show specific incompatibility reasons
   - Suggest compatible alternatives
   - Offer to split into sub-workflows

3. **Ambiguous Intent**
   - Present top 3 matching commands
   - Show Progressive Disclosure options
   - Request clarification with examples

## Success Metrics

Track navigation effectiveness:
- Time to find relevant command: < 3 steps
- Component assembly success rate: > 90%
- Compatibility validation accuracy: > 95%
- Context preservation across sessions: 100%

## Quick Reference: Navigation Paths

### By User Intent
- **"I want to..."** → Layer 1 (/quick-command)
- **"Help me customize..."** → Layer 2 (/build-command)
- **"I need a complex workflow..."** → Layer 3 (/assemble-command)

### By Expertise Level
- **Beginner**: Start with Layer 1 commands
- **Intermediate**: Explore Layer 2 options
- **Expert**: Direct to Layer 3 assembly

### By Time Available
- **30 seconds**: Layer 1 auto-generation
- **5 minutes**: Layer 2 guided customization
- **15-30 minutes**: Layer 3 professional assembly

---

This reference enables AI systems to efficiently navigate the Claude Code Modular Prompts template library, leveraging XML metadata to build effective modular prompts from the available 91 components and 88 commands.