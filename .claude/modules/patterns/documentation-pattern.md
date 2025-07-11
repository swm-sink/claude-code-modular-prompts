| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Documentation Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="documentation_pattern" category="patterns">
  
  <purpose>
    Effective knowledge capture and sharing, ensuring comprehensive documentation that serves different audiences and maintains system knowledge.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Code or system needs documentation</condition>
    <condition type="explicit">Knowledge sharing is required</condition>
    <condition type="explicit">Onboarding new team members</condition>
    <condition type="explicit">API or interface documentation needed</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="identify_documentation_needs" order="1">
      <requirements>
        Documentation requirements must be assessed
        Target outcomes must be defined
        Stakeholder needs must be understood
      </requirements>
      <actions>
        Determine what documentation is required
        Identify user documentation and guides
        Define technical documentation and APIs
        Document architecture and design decisions
        Create process and workflow documentation
      </actions>
      <validation>
        Documentation needs are clearly identified
        Requirements are comprehensive
        All stakeholder needs are addressed
      </validation>
    </phase>
    
    <phase name="define_target_audience" order="2">
      <requirements>
        Documentation needs must be identified
        Audience categories must be defined
        Communication preferences must be understood
      </requirements>
      <actions>
        Understand who will use the documentation
        Consider end users and customers
        Address developers and technical staff
        Support system administrators and operators
        Inform stakeholders and decision makers
      </actions>
      <validation>
        Target audience is clearly defined
        Audience needs are understood
        Communication approach is appropriate
      </validation>
    </phase>
    
  </implementation>
  
  <integration_points>
    <provides_to>
      patterns/user-interaction-pattern.md for knowledge sharing
    </provides_to>
    <depends_on>
      patterns/critical-thinking-pattern.md for content analysis
    </depends_on>
  </integration_points>
  
</module>
```