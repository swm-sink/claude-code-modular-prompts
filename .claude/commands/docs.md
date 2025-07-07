<command purpose="Documentation navigation, search, and generation for the Claude Code framework">
  
  <delegation target="modules/development/documentation.md">
    This command delegates ALL implementation to the documentation module which provides intelligent navigation, search capabilities, and documentation generation for the Claude Code framework.
  </delegation>
  
  <module_integration>
    <primary_module>modules/development/documentation.md</primary_module>
    <supporting_modules>
      <module>modules/development/research-analysis.md</module>
      <module>modules/quality/documentation-standards.md</module>
      <module>modules/patterns/intelligent-routing.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="navigation">/docs "Show me the permission guide"</example>
    <example type="search">/docs "Find all TDD documentation"</example>
    <example type="index">/docs "List all documentation"</example>
    <example type="specific">/docs "Explain the AWARE framework"</example>
    <example type="generate">/docs "Create a guide for new contributors"</example>
  </usage_examples>
  
  <trigger_conditions>
    <condition type="documentation_search">Finding specific documentation topics</condition>
    <condition type="documentation_navigation">Browsing available documentation</condition>
    <condition type="documentation_generation">Creating new documentation based on framework state</condition>
    <condition type="documentation_update">Updating existing documentation to match current state</condition>
  </trigger_conditions>
  
  <documentation_capabilities>
    <capability name="smart_search">Intelligent search across all documentation</capability>
    <capability name="contextual_navigation">Navigate based on user needs</capability>
    <capability name="auto_generation">Generate documentation from code and modules</capability>
    <capability name="consistency_check">Verify documentation matches implementation</capability>
    <capability name="format_support">Markdown, JSON, and structured formats</capability>
  </documentation_capabilities>
  
  <reference>
    See modules/development/documentation.md for complete implementation details including search algorithms, navigation patterns, and generation templates.
  </reference>
  
</command>