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
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>BLOCK any documentation creation outside this command</action>
      <critical_thinking>
        - Is this request for documentation creation vs research/analysis?
        - Should this be routed to /query for understanding existing code?
        - Am I being asked to document TDD practices or testing strategies?
        - Is this documentation request or code analysis?
      </critical_thinking>
      <output_format>GATEWAY_ENFORCEMENT: Documentation request [confirmed/redirected to /query]</output_format>
      <validation>Documentation creation properly routed through /docs gateway</validation>
      <enforcement>CRITICAL: Block all documentation creation outside this command</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Parse request type with TDD documentation awareness</action>
      <critical_thinking>
        - What type of documentation is needed (search/generate/validate/index)?
        - Does this involve documenting TDD practices or testing workflows?
        - Should I include TDD methodology in the documentation?
        - Are there existing TDD docs that need updating?
      </critical_thinking>
      <output_format>REQUEST_TYPE: [search/generate/validate/index] (TDD content: [yes/no/update])</output_format>
      <validation>Request type identified with TDD documentation requirements</validation>
      <enforcement>VERIFY request type clear and TDD needs identified</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Execute search operations with TDD-aware content discovery</action>
      <critical_thinking>
        - Should I search existing TDD documentation and testing guides?
        - Are there test files or TDD patterns I should reference?
        - Do parallel Grep/Glob operations include test-related content?
        - What TDD documentation already exists that I should build upon?
      </critical_thinking>
      <output_format>SEARCH_EXECUTION: Parallel operations including TDD content [discovered/referenced]</output_format>
      <validation>Comprehensive search including TDD and testing documentation</validation>
      <enforcement>ENSURE search covers TDD practices when generating development docs</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Apply Framework 3.0 standards with TDD methodology integration</action>
      <critical_thinking>
        - Are Framework 3.0 standards being applied correctly?
        - Should I include TDD principles in development documentation?
        - Does this documentation need testing workflow information?
        - Are TDD examples and best practices included where relevant?
      </critical_thinking>
      <output_format>STANDARDS_APPLICATION: Framework 3.0 applied with TDD methodology [integrated/referenced]</output_format>
      <validation>Standards applied with appropriate TDD methodology inclusion</validation>
      <enforcement>MANDATORY: Framework 3.0 format with TDD awareness where applicable</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Validate location and cross-references including TDD resources</action>
      <critical_thinking>
        - Is documentation going in proper /docs directory?
        - Do cross-references include relevant TDD modules and guides?
        - Are links to testing documentation and examples working?
        - Is documentation structure consistent with TDD workflow docs?
      </critical_thinking>
      <output_format>VALIDATION_COMPLETE: Location verified, TDD cross-references [validated/updated]</output_format>
      <validation>Proper location with comprehensive TDD resource linking</validation>
      <enforcement>CRITICAL: /docs directory ONLY with valid TDD cross-references</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <critical_enforcement>
    <rule priority="MAXIMUM">ONLY /docs can create documentation files</rule>
    <rule priority="MAXIMUM">ALL docs MUST go in /docs directory</rule>
    <rule priority="MAXIMUM">Framework 3.0 format MANDATORY</rule>
    <rule priority="HIGH">Auto-update documentation index</rule>
    <rule priority="HIGH">Validate all cross-references</rule>
  </critical_enforcement>
  
  <tdd_integration enforcement="MANDATORY">
    <documentation_tdd_awareness>Include TDD methodology in all development-related documentation</documentation_tdd_awareness>
    <testing_workflow_docs>Document TDD workflows, testing patterns, and quality standards</testing_workflow_docs>
    <tdd_cross_references>Link to relevant TDD modules and testing examples in documentation</tdd_cross_references>
    <validation>Reference quality/tdd.md#documentation_standards for TDD documentation practices</validation>
    <blocking_conditions>
      <condition>Development documentation missing TDD methodology references</condition>
      <condition>Testing workflow documentation incomplete or outdated</condition>
      <condition>Documentation created outside /docs gateway enforcement</condition>
      <condition>Cross-references to TDD resources missing or broken</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before documentation operations</module>
      <module>development/documentation.md - Core documentation workflows and standards</module>
      <module>patterns/intelligent-routing.md - Smart search and discovery capabilities</module>
      <module>quality/tdd.md - TDD documentation standards and practices</module>
    </core_stack>
    <contextual_modules>
      <conditional module="patterns/pattern-library.md" condition="pattern_documentation"/>
      <conditional module="quality/production-standards.md" condition="quality_documentation"/>
      <conditional module="security/threat-modeling.md" condition="security_documentation"/>
    </contextual_modules>
  </module_execution>
  
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