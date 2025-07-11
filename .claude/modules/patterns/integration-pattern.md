| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Integration Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="integration_pattern" category="patterns">
  
  <purpose>
    System connection and coordination between components, ensuring reliable integration points with proper error handling and monitoring.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Connecting different system components</condition>
    <condition type="explicit">Integrating with external services</condition>
    <condition type="explicit">Coordinating between multiple systems</condition>
    <condition type="explicit">API development and consumption</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="define_integration_requirements" order="1">
      <requirements>
        Integration scope must be defined
        Requirements must be gathered
        Constraints must be identified
      </requirements>
      <actions>
        Understand what needs to be connected
        Define data flow and transformation needs
        Establish performance and reliability requirements
        Identify security and compliance constraints
        Plan error handling and recovery needs
      </actions>
      <validation>
        Integration requirements are clearly defined
        Data flows are mapped
        Constraints are identified
      </validation>
    </phase>
    
    <phase name="design_integration_architecture" order="2">
      <requirements>
        Integration requirements must be defined
        Architecture patterns must be available
        Design principles must be established
      </requirements>
      <actions>
        Plan the connection strategy
        Choose communication protocols and formats
        Design authentication and authorization
        Plan data mapping and transformation
        Design error handling and retry logic
      </actions>
      <validation>
        Integration architecture is well-designed
        Communication protocols are appropriate
        Error handling is comprehensive
      </validation>
    </phase>
    
  </implementation>
  
  <integration_points>
    <provides_to>
      patterns/error-recovery-pattern.md for robust integration
    </provides_to>
    <depends_on>
      patterns/critical-thinking-pattern.md for architecture decisions
    </depends_on>
  </integration_points>
  
</module>
```