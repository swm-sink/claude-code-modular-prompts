| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# PRD Core - Shared Product Requirements Concepts

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="prd_core" category="planning">
  
  <purpose>
    Define canonical PRD concepts, templates, and standards shared across all PRD-related modules to ensure consistency and prevent duplication.
  </purpose>
  
  <scope>
    This module provides the single source of truth for:
    - PRD template structure
    - Requirement quality standards
    - Success metrics definitions
    - User story formats
    - Acceptance criteria standards
  </scope>
  
  <prd_template enforcement="standard">
    
    <section name="executive_summary">
      <purpose>High-level overview of feature and business value</purpose>
      <required_content>
        Feature description and business objectives
        Target user segments and use cases
        Expected business impact and success metrics
        High-level implementation timeline
      </required_content>
    </section>
    
    <section name="user_stories">
      <purpose>Detailed user stories with acceptance criteria</purpose>
      <required_content>
        Complete user story mapping with priorities
        Detailed acceptance criteria for each story
        User journey flow and interaction patterns
        Edge cases and error handling scenarios
      </required_content>
      <format>
        As a [user type], I want [functionality] so that [business value]
      </format>
    </section>
    
    <section name="technical_requirements">
      <purpose>Technical specifications and constraints</purpose>
      <required_content>
        Functional requirements and specifications
        Non-functional requirements (performance, security, scalability)
        Integration requirements and dependencies
        Technical constraints and assumptions
      </required_content>
    </section>
    
    <section name="success_metrics">
      <purpose>Measurable success criteria and KPIs</purpose>
      <required_content>
        Key Performance Indicators (KPIs) and metrics
        Success criteria and acceptance thresholds
        Measurement methodology and tools
        Reporting and monitoring requirements
      </required_content>
    </section>
    
    <section name="implementation_strategy">
      <purpose>High-level implementation approach and timeline</purpose>
      <required_content>
        MVP definition and core functionality
        Implementation phases and milestones
        Resource requirements and team allocation
        Risk assessment and mitigation strategies
      </required_content>
    </section>
    
  </prd_template>
  
  <requirement_quality_standards>
    
    <clarity>
      Requirements must be unambiguous and specific
      Use concrete examples where helpful
      Avoid vague terms like "fast", "easy", "intuitive"
      Define all technical terms and acronyms
    </clarity>
    
    <testability>
      Each requirement must have clear pass/fail criteria
      Acceptance criteria must be measurable
      Test scenarios should be derivable from requirements
      Performance targets must include specific metrics
    </testability>
    
    <completeness>
      All user scenarios must be addressed
      Edge cases and error conditions documented
      Integration points clearly specified
      Non-functional requirements included
    </completeness>
    
    <consistency>
      Requirements must not contradict each other
      Terminology used consistently throughout
      Priorities aligned with business objectives
      Technical approach coherent across requirements
    </consistency>
    
  </requirement_quality_standards>
  
  <user_story_standards>
    
    <format_requirements>
      Follow standard format: As a... I want... So that...
      Include clear acceptance criteria for each story
      Specify priority using MoSCoW method
      Link to relevant technical requirements
    </format_requirements>
    
    <acceptance_criteria_format>
      Given [precondition]
      When [action]
      Then [expected result]
      And [additional outcomes]
    </acceptance_criteria_format>
    
    <prioritization_framework>
      MUST have - Core functionality required for launch
      SHOULD have - Important but not critical for MVP
      COULD have - Desirable if time/resources permit
      WON'T have - Out of scope for current iteration
    </prioritization_framework>
    
  </user_story_standards>
  
  <success_metrics_framework>
    
    <metric_categories>
      Business metrics - Revenue, user acquisition, retention
      Performance metrics - Response time, throughput, availability
      Quality metrics - Defect rates, test coverage, user satisfaction
      Operational metrics - Deployment frequency, MTTR, resource usage
    </metric_categories>
    
    <measurement_standards>
      Define baseline measurements before implementation
      Specify measurement frequency and methodology
      Include both leading and lagging indicators
      Set realistic targets based on current performance
    </measurement_standards>
    
  </success_metrics_framework>
  
  <integration_guidelines>
    <instruction>
      Modules implementing PRD functionality MUST reference this module
      for all shared concepts rather than duplicating definitions.
    </instruction>
    <referencing_modules>
      planning/prd-generation.md - Manual PRD workflow
      planning/intelligent-prd.md - Autonomous requirement extraction
      planning/feature-workflow.md - Feature development integration
    </referencing_modules>
  </integration_guidelines>
  
  <implementation>
    <phase name="requirement_gathering">
      <description>Collect and structure requirements using standard templates</description>
      <actions>
        Analyze business objectives and user needs
        Document user stories in standard format
        Define acceptance criteria for each story
        Prioritize requirements using MoSCoW method
      </actions>
    </phase>
    
    <phase name="quality_validation">
      <description>Ensure requirements meet quality standards</description>
      <actions>
        Verify clarity and lack of ambiguity
        Check testability of all requirements
        Ensure completeness of edge cases
        Validate consistency across requirements
      </actions>
    </phase>
    
    <phase name="metrics_definition">
      <description>Define success metrics and measurement approach</description>
      <actions>
        Identify relevant KPIs for each requirement
        Set measurable success thresholds
        Define measurement methodology
        Establish monitoring requirements
      </actions>
    </phase>
  </implementation>
  
</module>
```