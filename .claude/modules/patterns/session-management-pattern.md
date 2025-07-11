| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Session Management Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="session_management_pattern" category="patterns">
  
  <purpose>
    Coordination and tracking of long-running tasks, ensuring proper session lifecycle management and progress tracking across complex workflows.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Complex tasks requiring multiple steps</condition>
    <condition type="automatic">Long-running development sessions</condition>
    <condition type="explicit">Multi-phase project coordination</condition>
    <condition type="explicit">Progress tracking is needed</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="initialize_session" order="1">
      <requirements>
        Session framework must be available
        Tracking mechanisms must be configured
        Communication channels must be established
      </requirements>
      <actions>
        Set up session tracking and coordination
        Create session identifier and context
        Define objectives and success criteria
        Set up progress tracking mechanisms
        Establish communication channels
      </actions>
      <validation>
        Session is properly initialized
        Tracking mechanisms are operational
        Success criteria are defined
      </validation>
    </phase>
    
    <phase name="track_progress" order="2">
      <requirements>
        Session must be initialized
        Progress tracking must be active
        Milestone definitions must be available
      </requirements>
      <actions>
        Monitor task completion and milestones
        Track task completion status
        Monitor time and effort spent
        Document issues and blockers encountered
        Validate quality metrics and validation
      </actions>
      <validation>
        Progress is accurately tracked
        Milestones are monitored
        Issues are documented
      </validation>
    </phase>
    
  </implementation>
  
  <integration_points>
    <provides_to>
      patterns/context-management-pattern.md for coordination
    </provides_to>
    <depends_on>
      patterns/user-interaction-pattern.md for communication
    </depends_on>
  </integration_points>
  
</module>
```