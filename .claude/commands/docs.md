| version | last_updated | status |
|---------|--------------|--------|
| 2.6.0   | 2025-07-08   | stable |

# /docs - FOCUS framework documentation creation with intelligent routing and gateway enforcement

────────────────────────────────────────────────────────────────────────────────

> **⚡ Clear Purpose**: Creates, updates, and manages documentation files. Does NOT answer "how does X work" questions - use `/query` for research!

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="FOCUS framework documentation gateway with intelligent routing and mandatory enforcement">
  
  <delegation target="modules/development/documentation.md">
    FOCUS framework → Function analysis → Objective definition → Context evaluation → User needs → Scope management → Documentation creation
  </delegation>
  
  <thinking_pattern enforcement="CRITICAL">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Apply FOCUS framework - Analyze Function and gateway enforcement</action>
      <critical_thinking>
        - What is the specific function of this documentation request?
        - Should this be documentation creation (FOCUS) or research analysis (route to /query)?
        - How does FOCUS framework function analysis guide proper routing decisions?
        - What documentation function best serves the user's actual needs?
        - Is this request aligned with FOCUS framework documentation creation function?
      </critical_thinking>
      <output_format>FOCUS_FUNCTION_ANALYSIS:
        - Request function: [documentation_creation/research_analysis]
        - Gateway decision: [confirmed_docs/redirected_to_query]
        - Function alignment: [focus_framework_appropriate]
        - Routing rationale: [decision_reasoning]</output_format>
      <validation>Documentation function properly analyzed with FOCUS framework and gateway enforcement</validation>
      <enforcement>CRITICAL: Block all documentation creation outside this command and route research to /query</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Apply FOCUS framework - Define Objective and documentation goals</action>
      <critical_thinking>
        - What is the specific objective this documentation should achieve?
        - How does FOCUS framework objective definition guide documentation strategy?
        - What measurable outcomes define successful documentation completion?
        - How do documentation objectives align with user needs and framework requirements?
        - What objective clarity ensures optimal documentation effectiveness?
      </critical_thinking>
      <output_format>FOCUS_OBJECTIVE_DEFINITION:
        - Documentation objective: [specific_goal_with_outcomes]
        - Success criteria: [measurable_completion_metrics]
        - Framework alignment: [focus_framework_integration]
        - TDD integration: [testing_methodology_inclusion]</output_format>
      <validation>Documentation objectives clearly defined with FOCUS framework guidance and success metrics</validation>
      <enforcement>BLOCK if objectives unclear or misaligned with FOCUS framework documentation principles</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Apply FOCUS framework - Evaluate Context and documentation environment</action>
      <critical_thinking>
        - What comprehensive context affects documentation creation and effectiveness?
        - How does FOCUS framework context evaluation guide content strategy?
        - What existing documentation context should inform new content creation?
        - What technical and business context influences documentation approach?
        - How does context analysis optimize documentation relevance and utility?
      </critical_thinking>
      <output_format>FOCUS_CONTEXT_EVALUATION:
        - Documentation context: [existing_content_and_gaps]
        - Technical context: [system_architecture_and_patterns]
        - Business context: [user_needs_and_organizational_requirements]
        - Content strategy: [context_informed_approach]</output_format>
      <validation>Documentation context comprehensively evaluated with FOCUS framework guidance</validation>
      <enforcement>ENSURE context analysis includes existing documentation, TDD practices, and framework requirements</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Apply FOCUS framework - Assess User needs and documentation requirements</action>
      <critical_thinking>
        - Who are the specific users of this documentation and what are their needs?
        - How does FOCUS framework user assessment guide content creation?
        - What user experience considerations optimize documentation effectiveness?
        - How do different user types (developers, stakeholders, etc.) influence approach?
        - What user-centered design principles improve documentation utility?
      </critical_thinking>
      <output_format>FOCUS_USER_ASSESSMENT:
        - Primary users: [target_audience_identification]
        - User needs: [specific_requirements_and_expectations]
        - Experience design: [user_centered_content_strategy]
        - Accessibility considerations: [inclusive_documentation_approach]</output_format>
      <validation>User needs comprehensively assessed with FOCUS framework user-centered approach</validation>
      <enforcement>BLOCK if user assessment incomplete or documentation approach not user-optimized</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Apply FOCUS framework - Define Scope and documentation boundaries</action>
      <critical_thinking>
        - What is the appropriate scope for this documentation to maximize value?
        - How does FOCUS framework scope definition prevent scope creep and ensure focus?
        - What boundaries optimize documentation effectiveness without overwhelming users?
        - How does scope definition align with Framework 3.0 standards and TDD requirements?
        - What scope management ensures documentation remains maintainable and current?
      </critical_thinking>
      <output_format>FOCUS_SCOPE_DEFINITION:
        - Documentation scope: [clear_boundaries_and_coverage]
        - Framework standards: [framework_3_0_compliance]
        - TDD integration: [testing_methodology_inclusion]
        - Maintenance strategy: [scope_sustainability_approach]</output_format>
      <validation>Documentation scope clearly defined with FOCUS framework boundaries and standards compliance</validation>
      <enforcement>CRITICAL: Scope must align with /docs directory placement and Framework 3.0 standards</enforcement>
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
  
  <focus_framework_integration enforcement="MANDATORY">
    <function_analysis>Clear function identification and documentation vs research routing decisions</function_analysis>
    <objective_definition>Specific documentation goals with measurable success criteria and framework alignment</objective_definition>
    <context_evaluation>Comprehensive documentation environment assessment and content strategy optimization</context_evaluation>
    <user_assessment>User-centered documentation design with accessibility and experience optimization</user_assessment>
    <scope_definition>Clear documentation boundaries with Framework 3.0 compliance and maintenance strategy</scope_definition>
    <documentation_optimization>User-focused documentation creation with systematic function and scope management</documentation_optimization>
    <validation>Reference frameworks/focus.md for complete FOCUS framework implementation in documentation</validation>
  </focus_framework_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before FOCUS framework documentation operations</module>
      <module>frameworks/focus.md - FOCUS framework function, objective, context, user, scope for documentation</module>
      <module>development/documentation.md - Framework-integrated core documentation workflows and standards</module>
      <module>patterns/intelligent-routing.md - Framework-aware smart search and discovery capabilities</module>
      <module>quality/tdd.md - TDD documentation standards with FOCUS framework integration</module>
    </core_stack>
    <contextual_modules>
      <conditional module="frameworks/framework-selector.md" condition="complex_documentation_requirements"/>
      <conditional module="frameworks/advanced-frameworks.md" condition="specialized_framework_needs"/>
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
    • Uses focus_framework_integration pattern for user-centered documentation creation
    • Implements parallel_execution for batch document analysis with framework optimization
    • Applies smart_memoization for cached search results with context awareness
    • Uses explicit_validation for consistency checks with framework standards
    • Leverages consequence_mapping for documentation impact with user experience focus
    • Implements single_responsibility for focused documentation with scope management
    • ENFORCES documentation gateway pattern with intelligent routing to /query for research
    • Integrates framework_selection_intelligence for documentation optimization
    
    See modules/frameworks/focus.md for FOCUS framework implementation
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/documentation.md for framework-integrated implementation
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
  

  <prompt_construction>
    <assembly_preview>
      WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. Gateway     │ → Block external docs
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Enforcement │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. Type        │ → Documentation category
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Analysis    │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. Content     │ → Generate or search
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Generation  │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. Standards   │ → Apply formatting rules
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Application │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. Index       │ → Update documentation index
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Update      │
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~12,000
      - Gateway enforcement: 1,000
      - Type analysis: 1,500
      - Content generation: 6,000
      - Standards application: 2,000
      - Index updates: 1,500
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /docs "API documentation"
      [00:15] 🚫 GATEWAY: External doc creation blocked
      [00:30] 🔍 ANALYSIS: API documentation type identified
      [00:45] 📝 GENERATION: Creating comprehensive API docs
      [01:30] 📏 STANDARDS: Applying framework formatting
      [01:45] 📚 INDEX: Updating documentation index
      [02:00] ✅ COMPLETE: API documentation published
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Reads checkpoint structure sequentially
      2. Executes critical_thinking questions internally
      3. Formats output according to output_format specifications
      4. Validates against enforcement rules before proceeding
      5. Applies parallel execution optimization where possible
    </parsing_behavior>

    <decision_points>
      - Checkpoint failures trigger enforcement actions
      - Module selection based on contextual conditions
      - Parallel execution for independent operations
      - Quality gate validation at completion boundaries
      - Error recovery through graceful degradation paths
    </decision_points>
  </claude_4_interpretation>

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