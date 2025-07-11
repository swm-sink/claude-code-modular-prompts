| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# Documentation Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="documentation" purpose="MANDATORY gateway for ALL documentation operations">
  
  <metadata>
    <category>development</category>
    <description>Comprehensive documentation system for navigation, search, and generation</description>
  </metadata>
  
  <thinking_pattern enforcement="CRITICAL">
    <step>1. BLOCK any documentation creation outside /docs command</step>
    <step>2. Parse request type (search/generate/validate/index)</step>
    <step>3. For search: Use parallel Grep/Glob for efficiency</step>
    <step>4. For generate: Apply Framework 3.0 standards ALWAYS</step>
    <step>5. Ensure proper location (/docs directory ONLY)</step>
    <step>6. Validate cross-references and consistency</step>
    <step>7. Update DOCUMENTATION_INDEX.md automatically</step>
  </thinking_pattern>
  
  <documentation_strategy>
    <principle name="user_focused">Documentation organized by user needs, not file structure</principle>
    <principle name="intelligent_search">Context-aware search that understands intent</principle>
    <principle name="auto_generation">Generate documentation from actual implementation</principle>
    <principle name="consistency_verification">Ensure docs match reality</principle>
  </documentation_strategy>
  
  <documentation_locations>
    <location type="framework_docs" path="docs/">Main documentation directory</location>
    <location type="framework_guides" path="docs/framework/">Detailed framework guides</location>
    <location type="module_docs" path=".claude/modules/">Module implementation docs</location>
    <location type="command_docs" path=".claude/commands/">Command delegation docs</location>
    <location type="settings_docs" path=".claude/settings/README.md">Settings documentation</location>
    <location type="main_readme" path="README.md">Project overview</location>
    <location type="claude_md" path="CLAUDE.md">Core framework rules</location>
  </documentation_locations>
  
  <search_implementation>
    <approach name="multi_tier_search">
      <tier level="1">Exact title matches in documentation files</tier>
      <tier level="2">Content keyword search with relevance scoring</tier>
      <tier level="3">Semantic search based on topic understanding</tier>
      <tier level="4">Module and command documentation cross-reference</tier>
    </approach>
    
    <search_patterns>
      <pattern type="topic_search">
        <example>Search: "permissions" → Find PERMISSION_GUIDE.md, settings docs</example>
        <implementation>Grep("permissions", "docs/**/*.md"), prioritize by relevance</implementation>
      </pattern>
      <pattern type="command_search">
        <example>Search: "swarm command" → Find swarm.md, multi-agent.md</example>
        <implementation>Read command file, follow delegation, compile full docs</implementation>
      </pattern>
      <pattern type="how_to_search">
        <example>Search: "how to fix permissions" → Find troubleshooting sections</example>
        <implementation>Search for problem-solving patterns, FAQs, guides</implementation>
      </pattern>
    </search_patterns>
  </search_implementation>
  
  <navigation_implementation>
    <navigation_modes>
      <mode name="index_listing">
        <description>Show organized index of all documentation</description>
        <categories>
          <category name="Getting Started">README, GETTING_STARTED, tutorials</category>
          <category name="Commands">/commands documentation</category>
          <category name="Modules">Module implementation guides</category>
          <category name="Framework">Architecture, patterns, standards</category>
          <category name="Troubleshooting">Problem-solving guides</category>
        </categories>
      </mode>
      
      <mode name="contextual_suggestions">
        <description>Suggest relevant docs based on user's current work</description>
        <implementation>Analyze recent commands, suggest related documentation</implementation>
      </mode>
      
      <mode name="breadcrumb_navigation">
        <description>Show documentation hierarchy and relationships</description>
        <implementation>Display: Category > Document > Section navigation</implementation>
      </mode>
    </navigation_modes>
  </navigation_implementation>
  
  <generation_implementation>
    <generation_types>
      <type name="module_documentation">
        <trigger>Request for undocumented module</trigger>
        <process>
          <step>Read module implementation</step>
          <step>Extract purpose, patterns, usage</step>
          <step>Generate structured documentation</step>
          <step>Include examples from actual usage</step>
        </process>
      </type>
      
      <type name="usage_guide">
        <trigger>Request for how-to guide</trigger>
        <process>
          <step>Identify relevant commands and modules</step>
          <step>Extract usage patterns</step>
          <step>Create step-by-step guide</step>
          <step>Include real examples</step>
        </process>
      </type>
      
      <type name="api_documentation">
        <trigger>Request for command/module API docs</trigger>
        <process>
          <step>Parse command structure</step>
          <step>Document parameters and options</step>
          <step>Include delegation information</step>
          <step>Add usage examples</step>
        </process>
      </type>
    </generation_types>
  </generation_implementation>
  
  <consistency_verification>
    <verification_checks>
      <check name="delegation_accuracy">Ensure command docs match actual delegation</check>
      <check name="module_existence">Verify referenced modules exist</check>
      <check name="example_validity">Test that examples actually work</check>
      <check name="version_alignment">Check version numbers match framework</check>
    </verification_checks>
    
    <update_triggers>
      <trigger>Module implementation changes</trigger>
      <trigger>Command structure updates</trigger>
      <trigger>New features added</trigger>
      <trigger>Bug fixes that change behavior</trigger>
    </update_triggers>
  </consistency_verification>
  
  <execution_workflow>
    <phase name="request_analysis">
      <step>Parse user request for documentation needs</step>
      <step>Identify search terms, topics, or generation requirements</step>
      <step>Determine optimal response type</step>
    </phase>
    
    <phase name="documentation_retrieval">
      <step>Search across all documentation locations</step>
      <step>Rank results by relevance and recency</step>
      <step>Follow cross-references and relationships</step>
    </phase>
    
    <phase name="response_formatting">
      <step>Present documentation in clear, navigable format</step>
      <step>Include related documentation links</step>
      <step>Highlight relevant sections</step>
      <step>Provide navigation breadcrumbs</step>
    </phase>
  </execution_workflow>
  
  <quality_standards>
    <standard name="clarity">Documentation must be clear and unambiguous</standard>
    <standard name="completeness">Cover all aspects of functionality</standard>
    <standard name="accuracy">Must match actual implementation</standard>
    <standard name="examples">Include practical, working examples</standard>
    <standard name="maintenance">Keep documentation current with changes</standard>
  </quality_standards>
  
  <common_documentation_queries>
    <query pattern="list all docs">Show organized index of all documentation</query>
    <query pattern="find [topic]">Search for specific topic across all docs</query>
    <query pattern="explain [command]">Show command documentation and usage</query>
    <query pattern="how to [task]">Find guides for specific tasks</query>
    <query pattern="troubleshoot [issue]">Find problem-solving documentation</query>
    <query pattern="generate [type] guide">Create new documentation</query>
  </common_documentation_queries>
  
  <integration_points>
    <integration module="research-analysis">For deep documentation search</integration>
    <integration module="intelligent-routing">For understanding user intent</integration>
    <integration module="documentation-standards">For quality enforcement</integration>
  </integration_points>
  
</module>
```