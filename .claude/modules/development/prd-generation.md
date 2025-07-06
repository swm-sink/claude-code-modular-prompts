<module name="prd_generation" category="development">
  
  <purpose>
    Generate comprehensive Product Requirements Documents with automated requirement extraction, user story mapping, and stakeholder alignment ensuring clear feature definition before development.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Feature development workflow Step 1 - PRD Generation</condition>
    <condition type="explicit">User requests PRD creation or requirements analysis</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="requirement_discovery" order="1">
      <purpose>Extract and analyze comprehensive requirements from user input</purpose>
      <requirements>
        User intent clearly understood and documented
        Business value proposition identified
        Technical constraints and assumptions captured
        Success criteria and KPIs defined
      </requirements>
      <actions>
        Apply critical thinking analysis to understand true user needs
        Research similar features and industry best practices
        Identify implicit requirements and edge cases
        Document assumptions requiring stakeholder validation
      </actions>
      <validation>
        Requirements comprehensive and unambiguous
        Business value clearly articulated
        Technical feasibility initially assessed
        Success criteria measurable and specific
      </validation>
    </phase>
    
    <phase name="user_story_mapping" order="2">
      <purpose>Transform requirements into detailed user stories with acceptance criteria</purpose>
      <requirements>
        User stories follow standard format (As a... I want... So that...)
        Acceptance criteria clearly defined for each story
        Story prioritization using MoSCoW method
        User journey mapped end-to-end
      </requirements>
      <actions>
        Create user personas based on requirements analysis
        Map complete user journey from start to finish
        Write detailed user stories with acceptance criteria
        Prioritize stories using MoSCoW (Must, Should, Could, Won't) framework
      </actions>
      <validation>
        All user stories follow standard format
        Acceptance criteria specific and testable
        Story priorities aligned with business value
        User journey complete and logical
      </validation>
    </phase>
    
    <phase name="technical_analysis" order="3">
      <purpose>Assess technical feasibility and define architectural approach</purpose>
      <requirements>
        Technical feasibility assessed and documented
        Architecture approach defined and validated
        Integration requirements identified
        Performance and scalability considerations addressed
      </requirements>
      <actions>
        Research current codebase architecture and patterns
        Identify technical dependencies and constraints
        Design high-level technical approach
        Assess performance and scalability implications
      </actions>
      <validation>
        Technical approach feasible with current architecture
        Integration points clearly identified
        Performance requirements realistic and achievable
        Scalability considerations properly addressed
      </validation>
    </phase>
    
    <phase name="stakeholder_alignment" order="4">
      <purpose>Obtain stakeholder approval and alignment on requirements</purpose>
      <requirements>
        PRD document comprehensive and professional
        Stakeholder review process completed
        Feedback integrated and documented
        Final approval obtained before development
      </requirements>
      <actions>
        Generate comprehensive PRD document
        Present requirements to stakeholders for review
        Integrate feedback and resolve conflicts
        Obtain formal approval before proceeding
      </actions>
      <validation>
        PRD document complete with all required sections
        Stakeholder feedback properly integrated
        No unresolved conflicts or ambiguities
        Formal approval documented
      </validation>
    </phase>
    
  </implementation>
  
  <prd_template enforcement="standard">
    
    <section name="executive_summary">
      <purpose>High-level overview of feature and business value</purpose>
      <content>
        Feature description and business objectives
        Target user segments and use cases
        Expected business impact and success metrics
        High-level implementation timeline
      </content>
    </section>
    
    <section name="user_stories">
      <purpose>Detailed user stories with acceptance criteria</purpose>
      <content>
        Complete user story mapping with priorities
        Detailed acceptance criteria for each story
        User journey flow and interaction patterns
        Edge cases and error handling scenarios
      </content>
    </section>
    
    <section name="technical_requirements">
      <purpose>Technical specifications and constraints</purpose>
      <content>
        Functional requirements and specifications
        Non-functional requirements (performance, security, scalability)
        Integration requirements and dependencies
        Technical constraints and assumptions
      </content>
    </section>
    
    <section name="success_metrics">
      <purpose>Measurable success criteria and KPIs</purpose>
      <content>
        Key Performance Indicators (KPIs) and metrics
        Success criteria and acceptance thresholds
        Measurement methodology and tools
        Reporting and monitoring requirements
      </content>
    </section>
    
    <section name="implementation_strategy">
      <purpose>High-level implementation approach and timeline</purpose>
      <content>
        MVP definition and core functionality
        Implementation phases and milestones
        Resource requirements and team allocation
        Risk assessment and mitigation strategies
      </content>
    </section>
    
  </prd_template>
  
  <research_integration enforcement="mandatory">
    <requirement name="industry_best_practices">Research current industry standards and best practices</requirement>
    <requirement name="competitive_analysis">Analyze similar features in competitive products</requirement>
    <requirement name="technical_standards">Research relevant technical standards and frameworks</requirement>
    <requirement name="user_experience">Study user experience patterns and accessibility guidelines</requirement>
  </research_integration>
  
  <quality_gates enforcement="strict">
    <gate name="requirement_completeness" requirement="All requirements identified and documented"/>
    <gate name="user_story_quality" requirement="User stories complete with testable acceptance criteria"/>
    <gate name="technical_feasibility" requirement="Technical approach validated and feasible"/>
    <gate name="stakeholder_approval" requirement="Formal stakeholder approval obtained"/>
    <gate name="success_metrics" requirement="Measurable success criteria defined"/>
  </quality_gates>
  
  <output_standards>
    <standard name="professional_documentation">PRD document professional quality suitable for stakeholder presentation</standard>
    <standard name="comprehensive_coverage">All aspects of feature requirements covered systematically</standard>
    <standard name="actionable_content">All requirements actionable and implementable by development team</standard>
    <standard name="measurable_outcomes">Success criteria specific, measurable, and achievable</standard>
  </output_standards>
  
  <integration_points>
    <depends_on>
      quality/critical-thinking.md for requirement analysis methodology
      patterns/session-management.md for stakeholder collaboration
    </depends_on>
    <provides_to>
      development/feature-workflow.md for Step 1 PRD generation
      development/mvp-strategy.md for MVP definition input
      quality/feature-validation.md for validation criteria
    </provides_to>
  </integration_points>
  
</module>