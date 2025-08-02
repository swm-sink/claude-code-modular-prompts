# {{COMPONENT_NAME}} Component

**Purpose**: {{Brief description of what this component does and why it exists}}

**Usage**: 
{{Primary usage instructions - what the component actually does}}
{{Secondary usage notes - important behaviors or considerations}}
{{Integration guidance - how it fits into workflows}}

**Compatibility**: 
- **Works with**: {{essential_compatible_components_only}}
- **Requires**: {{required_parameters_only}}
- **Conflicts**: {{known_incompatibilities_if_any}}

**Implementation**:
```{{language_or_pseudocode}}
{{Simple usage example showing how to use this component}}
{{Show typical input and expected output}}
```

**Category**: {{category}} | **Complexity**: {{simple|moderate|complex}} | **Time**: {{implementation_time_estimate}}

---

## Content-First Design Principles

### What This Template Eliminates (From 118 lines to ~15 lines)

**Eliminated XML Bloat**:
- ❌ ai_document_metadata (8 lines) - Claude can infer document metadata
- ❌ ai_navigation blocks (39 lines) - Discovery paths are obvious from content
- ❌ context_engineering (32 lines) - Workflow integration is clear from usage
- ❌ Excessive compatibility matrices (29 lines) - Only essential relationships needed

**Preserved Essential Information**:
- ✅ Component purpose and usage (the actual functionality)
- ✅ Key compatibility relationships (essential integrations only)
- ✅ Required parameters (what users actually need)
- ✅ Practical implementation example (working code)
- ✅ Basic categorization (for discovery and organization)

### Template Usage Instructions

1. **Replace ALL placeholders** with actual content:
   - `{{COMPONENT_NAME}}`: Exact component name
   - `{{Brief description}}`: 1-2 sentences maximum
   - `{{Primary usage}}`: What it does, not how it's structured
   - `{{essential_compatible_components_only}}`: Max 3-5 critical relationships
   - `{{required_parameters_only}}`: Only parameters users must provide
   - `{{language_or_pseudocode}}`: Use appropriate syntax for examples

2. **Content-First Approach**:
   - Start with what the component DOES
   - Focus on practical usage, not metadata
   - Provide working examples, not abstract descriptions
   - Keep compatibility lists short and essential
   - Eliminate all XML ceremony and navigation bloat

3. **Quality Gates**:
   - Total file length: <20 lines maximum
   - Content ratio: >70% actual functional information
   - Reading time: <30 seconds to understand component
   - Searchability: Key functionality obvious from first read

### Expected Results After Conversion

**Quantitative Improvements**:
- File size: 80% reduction (118 lines → ~15 lines)
- XML overhead: 91.4% → <30%
- Content visibility: 8.6% → >70%
- Reading comprehension: 85% time reduction

**Qualitative Improvements**:
- Immediate understanding of component purpose
- Clear integration guidance without bloat
- Practical examples over theoretical descriptions
- Essential information easily discoverable
- Zero XML ceremony or navigation complexity

---

**🎯 Success Criteria**: A developer should understand this component's purpose, usage, and integration within 30 seconds of reading. All XML metadata that doesn't directly support this goal should be eliminated.