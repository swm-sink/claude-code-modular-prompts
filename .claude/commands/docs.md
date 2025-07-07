| version | last_updated | status |
|---------|--------------|--------|
| 2.0.0   | 2025-07-07   | stable |

# /docs - Instant documentation access and generation

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Navigate, search, and generate documentation with consistency checks">
  
  <delegation target="modules/development/documentation.md">
    Parse request → Search/Navigate → Display or Generate → Validate consistency
  </delegation>
  
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
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/documentation.md for full implementation
  </pattern_usage>
  
  <usage_examples>
    /docs "permission guide"        → Find specific topic
    /docs "list all"                → Browse documentation
    /docs "explain AWARE"           → Topic explanation
    /docs "create contributor guide" → Generate new docs
    /docs "check consistency"       → Validate documentation
  </usage_examples>
  
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