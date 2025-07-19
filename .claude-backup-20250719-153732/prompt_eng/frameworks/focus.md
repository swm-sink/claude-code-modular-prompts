| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# FOCUS Framework Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="focus_framework" category="frameworks">
  
  <purpose>
    FOCUS (Frame, Organize, Clarify, Understand, Synthesize) framework for documentation and knowledge management.
  </purpose>
  
  <focus_framework>
    <frame>
      <description>Frame the context, purpose, and scope of documentation</description>
      <implementation>
        <step>Define documentation purpose and target audience</step>
        <step>Establish scope and boundaries of content</step>
        <step>Identify key objectives and success criteria</step>
        <step>Set context and background information</step>
      </implementation>
      <validation>Context and scope clearly defined</validation>
    </frame>
    
    <organize>
      <description>Organize information in logical structure and hierarchy</description>
      <implementation>
        <step>Create logical information hierarchy</step>
        <step>Group related concepts and topics</step>
        <step>Design navigation and information flow</step>
        <step>Establish consistent formatting and structure</step>
      </implementation>
      <validation>Information properly organized and structured</validation>
    </organize>
    
    <clarify>
      <description>Clarify complex concepts and eliminate ambiguity</description>
      <implementation>
        <step>Identify and define key terms and concepts</step>
        <step>Eliminate jargon and ambiguous language</step>
        <step>Provide clear examples and illustrations</step>
        <step>Ensure consistent terminology throughout</step>
      </implementation>
      <validation>Content clear and unambiguous</validation>
    </clarify>
    
    <understand>
      <description>Ensure content is understandable to target audience</description>
      <implementation>
        <step>Validate content against audience knowledge level</step>
        <step>Provide sufficient context and background</step>
        <step>Include learning aids and support materials</step>
        <step>Test comprehension with target users</step>
      </implementation>
      <validation>Content appropriate for target audience</validation>
    </understand>
    
    <synthesize>
      <description>Synthesize information into cohesive, actionable documentation</description>
      <implementation>
        <step>Integrate all content into coherent whole</step>
        <step>Ensure logical flow and connections</step>
        <step>Provide summary and key takeaways</step>
        <step>Create actionable next steps and references</step>
      </implementation>
      <validation>Documentation comprehensive and actionable</validation>
    </synthesize>
  </focus_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for documentation patterns
      documentation/auto-docs.md for documentation automation
    </depends_on>
    <provides_to>
      commands/docs.md for documentation framework
      development/documentation.md for documentation approach
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">template_systems</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">progressive_disclosure</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">automated_generation</uses_pattern>
    <implementation_notes>
      FOCUS framework provides systematic approach to documentation
      Template systems enable consistent documentation structure
      Progressive disclosure ensures appropriate information depth
    </implementation_notes>
  </pattern_usage>
  
</module>
```