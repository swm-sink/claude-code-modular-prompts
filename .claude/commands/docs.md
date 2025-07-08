| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /docs - Documentation Creation & Management ONLY

────────────────────────────────────────────────────────────────────────────────

> **⚡ Clear Purpose**: Creates, updates, and manages documentation files. Does NOT answer "how does X work" questions - use `/query` for research!

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="MANDATORY gateway for ALL documentation operations">
  
  <delegation target="modules/development/documentation.md">
    Validate request → Search/Generate → Apply standards → Ensure consistency
  </delegation>
  
  <thinking_pattern enforcement="CRITICAL">
    <step>1. BLOCK any documentation creation outside this command</step>
    <step>2. Parse request type (search/generate/validate/index)</step>
    <step>3. For search: Use parallel Grep/Glob for efficiency</step>
    <step>4. For generate: Apply Framework 3.0 standards ALWAYS</step>
    <step>5. Ensure proper location (/docs directory ONLY)</step>
    <step>6. Validate cross-references and consistency</step>
    <step>7. Update DOCUMENTATION_INDEX.md automatically</step>
  </thinking_pattern>
  
  <critical_enforcement>
    <rule priority="MAXIMUM">ONLY /docs can create documentation files</rule>
    <rule priority="MAXIMUM">ALL docs MUST go in /docs directory</rule>
    <rule priority="MAXIMUM">Framework 3.0 format MANDATORY</rule>
    <rule priority="HIGH">Auto-update documentation index</rule>
    <rule priority="HIGH">Validate all cross-references</rule>
  </critical_enforcement>
  
  <depends_on>
    development/documentation.md for documentation workflows
    patterns/pattern-library.md for proven execution patterns
    patterns/intelligent-routing.md for smart search capabilities
  </depends_on>
  
  <pattern_usage>
    • Uses parallel_execution for batch document analysis
    • Applies smart_memoization for cached search results
    • Implements explicit_validation for consistency checks
    • Leverages consequence_mapping for documentation impact
    • Uses single_responsibility for focused documentation
    • ENFORCES documentation gateway pattern
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/documentation.md for full implementation
  </pattern_usage>
  
  <usage_examples>
    /docs search "permission guide"     # Find existing docs to update
    /docs index                         # Browse documentation structure
    /docs generate "API Guide"          # CREATE new documentation
    /docs validate                      # Check docs consistency
    /docs "create setup guide"          # Generate new documentation
    
    <!-- NOT FOR RESEARCH! Use /query for "how does X work" questions -->
  </usage_examples>
  
  <anti_examples>
    ❌ /docs "how does authentication work?"     # Use /query instead!
    ❌ /docs "explain the codebase"              # Use /query instead!
    ❌ /docs "find security issues"              # Use /query instead!
    ✅ /docs generate "Security Guidelines"      # Creates documentation
  </anti_examples>
  
  <capabilities>
    • Smart search across all documentation
    • Auto-generation with framework standards
    • Consistency checks and validation
    • Cross-reference verification
    • Format standardization
  </capabilities>
  
  <subcommands>
    <subcommand name="search">
      <purpose>Search documentation with intelligent matching</purpose>
      <example>/docs search "authentication patterns"</example>
    </subcommand>
    <subcommand name="generate">
      <purpose>Create new documentation following standards</purpose>
      <example>/docs generate "API reference" --format standard</example>
    </subcommand>
    <subcommand name="validate">
      <purpose>Check documentation consistency and completeness</purpose>
      <example>/docs validate --comprehensive</example>
    </subcommand>
    <subcommand name="index">
      <purpose>Browse and navigate documentation structure</purpose>
      <example>/docs index --category framework</example>
    </subcommand>
  </capabilities>
  
  <quality_requirements>
    <requirement name="consistency">All docs follow Framework 3.0 standards</requirement>
    <requirement name="completeness">No gaps in critical documentation</requirement>
    <requirement name="accuracy">All information current and correct</requirement>
    <requirement name="accessibility">Easy to find and navigate</requirement>
  </quality_requirements>
  
</command>
```

────────────────────────────────────────────────────────────────────────────────

## Documentation Standards

```xml
<documentation_standards>
  <format>Framework 3.0 table-based format with version headers</format>
  <structure>Clear sections with horizontal separators</structure>
  <cross_references>Valid links and module dependencies</cross_references>
  <consistency>Uniform formatting and style throughout</consistency>
</documentation_standards>
```

────────────────────────────────────────────────────────────────────────────────

## Smart Documentation Features

```xml
<smart_features>
  <intelligent_search>Context-aware search with semantic matching</intelligent_search>
  <auto_generation>Template-based document creation with standards</auto_generation>
  <consistency_validation>Automated checks for format and content</consistency_validation>
  <cross_reference_checking>Verify all links and dependencies work</cross_reference_checking>
</smart_features>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Delegates to modules/development/documentation.md for complete implementation details including search algorithms, generation templates, and validation procedures.