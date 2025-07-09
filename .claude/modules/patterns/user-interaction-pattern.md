| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# User Interaction Pattern Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="user_interaction_pattern" category="patterns">
  
  <purpose>
    Effective communication and feedback with users, ensuring clear understanding, appropriate expectations, and collaborative engagement throughout development workflows.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">User input needs clarification</condition>
    <condition type="automatic">Progress updates are required</condition>
    <condition type="explicit">Feedback or approval is needed</condition>
    <condition type="explicit">Communication problems occur</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="understand_user_intent" order="1">
      <requirements>
        User input must be available
        Clarification techniques must be ready
        Communication channel must be established
      </requirements>
      <actions>
        Clarify what the user actually wants
        Ask clarifying questions
        Rephrase requirements back to user
        Identify assumptions and constraints
        Confirm understanding before proceeding
      </actions>
      <validation>
        User intent is clearly understood
        Requirements are confirmed
        Assumptions are identified
        Understanding is validated
      </validation>
    </phase>
    
    <phase name="provide_clear_communication" order="2">
      <requirements>
        User intent must be understood
        Communication principles must be established
        Message structure must be planned
      </requirements>
      <actions>
        Communicate effectively with the user
        Use clear, jargon-free language
        Structure information logically
        Provide concrete examples
        Anticipate user questions
      </actions>
      <validation>
        Communication is clear and understandable
        Information is logically structured
        Examples are concrete and helpful
        User questions are anticipated
      </validation>
    </phase>
    
    <phase name="set_expectations" order="3">
      <requirements>
        Clear communication must be established
        Expectation framework must be defined
        Success criteria must be available
      </requirements>
      <actions>
        Establish clear expectations about outcomes
        Provide timeline and effort estimates
        Define success criteria and deliverables
        Identify potential risks and limitations
        Outline next steps and dependencies
      </actions>
      <validation>
        Expectations are clearly established
        Timeline is realistic
        Success criteria are defined
        Risks and limitations are identified
      </validation>
    </phase>
    
    <phase name="gather_feedback" order="4">
      <requirements>
        Expectations must be set
        Feedback mechanisms must be available
        User engagement must be maintained
      </requirements>
      <actions>
        Collect user input and validation
        Present options for user choice
        Ask for specific feedback on results
        Validate understanding with examples
        Adjust based on user preferences
      </actions>
      <validation>
        User feedback is collected
        Options are presented clearly
        Understanding is validated
        Preferences are incorporated
      </validation>
    </phase>
    
    <phase name="maintain_engagement" order="5">
      <requirements>
        Feedback must be gathered
        Communication channels must be maintained
        Engagement strategies must be active
      </requirements>
      <actions>
        Keep user informed and involved
        Provide regular progress updates
        Report problems transparently
        Enable collaborative decision making
        Maintain proactive communication
      </actions>
      <validation>
        User engagement is maintained
        Progress is regularly communicated
        Problems are reported transparently
        Collaboration is effective
      </validation>
    </phase>
    
  </implementation>
  
  <communication_styles>
    <style name="technical">For developer-to-developer communication</style>
    <style name="business">For stakeholder and management updates</style>
    <style name="educational">For teaching and explanation</style>
    <style name="collaborative">For joint problem solving</style>
  </communication_styles>
  
  <feedback_mechanisms>
    <mechanism name="confirmation_questions">Verify understanding</mechanism>
    <mechanism name="option_presentation">Enable informed choices</mechanism>
    <mechanism name="progress_updates">Maintain visibility</mechanism>
    <mechanism name="result_validation">Confirm satisfaction</mechanism>
  </feedback_mechanisms>
  
  <integration_points>
    <provides_to>
      patterns/session-management-pattern.md for coordination
      patterns/documentation-pattern.md for knowledge sharing
    </provides_to>
    <depends_on>
      patterns/critical-thinking-pattern.md for user needs analysis
    </depends_on>
  </integration_points>
  
</module>
```