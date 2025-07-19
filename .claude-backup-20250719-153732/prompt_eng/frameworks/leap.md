| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# LEAP Framework Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="leap_framework" category="frameworks">
  
  <purpose>
    LEAP (Listen, Empathize, Analyze, Plan) framework for research-driven analysis and strategic planning.
  </purpose>
  
  <leap_framework>
    <listen>
      <description>Actively listen to requirements, constraints, and stakeholder needs</description>
      <implementation>
        <step>Gather comprehensive requirements from all stakeholders</step>
        <step>Identify explicit and implicit needs and constraints</step>
        <step>Document context, background, and environmental factors</step>
        <step>Clarify ambiguous requirements and assumptions</step>
      </implementation>
      <validation>Requirements completely understood and documented</validation>
    </listen>
    
    <empathize>
      <description>Understand stakeholder perspectives and user experiences</description>
      <implementation>
        <step>Analyze user journeys and pain points</step>
        <step>Understand stakeholder motivations and concerns</step>
        <step>Identify emotional and psychological factors</step>
        <step>Consider accessibility and inclusive design needs</step>
      </implementation>
      <validation>Stakeholder perspectives properly understood</validation>
    </empathize>
    
    <analyze>
      <description>Systematically analyze requirements, constraints, and opportunities</description>
      <implementation>
        <step>Perform comprehensive analysis of requirements</step>
        <step>Identify patterns, dependencies, and relationships</step>
        <step>Analyze constraints, risks, and opportunities</step>
        <step>Evaluate feasibility and implementation approaches</step>
      </implementation>
      <validation>Analysis comprehensive and well-founded</validation>
    </analyze>
    
    <plan>
      <description>Develop strategic plan with clear objectives and implementation approach</description>
      <implementation>
        <step>Define clear objectives and success criteria</step>
        <step>Design implementation strategy and approach</step>
        <step>Create detailed project plan with milestones</step>
        <step>Identify resources, timelines, and dependencies</step>
      </implementation>
      <validation>Plan comprehensive and actionable</validation>
    </plan>
  </leap_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for analysis patterns
      quality/critical-thinking.md for analysis methodology
    </depends_on>
    <provides_to>
      commands/query.md for research framework
      development/research-analysis.md for analysis approach
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">intelligent_analysis</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">systematic_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">strategic_planning</uses_pattern>
    <implementation_notes>
      LEAP framework provides systematic approach to research and analysis
      Intelligent analysis patterns enhance each framework phase
      Strategic planning ensures actionable outcomes
    </implementation_notes>
  </pattern_usage>
  
</module>
```