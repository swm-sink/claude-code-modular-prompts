| version | last_updated | status |
|---------|--------------|--------|
| 2.6.0   | 2025-07-08   | stable |

# /session - CARE framework session management with context preservation and framework integration

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="CARE framework session management with context preservation and framework integration">
  
  <delegation target="modules/patterns/session-management.md">
    CARE framework → Create context → Execute actions → Track results → Evaluate session → Framework-integrated management
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Apply CARE framework - Analyze Context for session management</action>
      <critical_thinking>
        - What is the comprehensive context for this session management request?
        - What type of session operation is needed (start/update/complete/view)?
        - What framework context should be preserved across the session?
        - How does session context integrate with active frameworks and TDD requirements?
        - What context preservation strategies optimize session continuity?
      </critical_thinking>
      <output_format>CARE_CONTEXT_ANALYSIS:
        - Session type: [start/update/complete/view]
        - Framework context: [frameworks_in_use]
        - TDD requirements: [required/optional/none]
        - Context preservation: [strategy_selected]</output_format>
      <validation>Session context comprehensively analyzed with framework and TDD integration</validation>
      <enforcement>BLOCK if session context incomplete or framework integration unclear</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Apply CARE framework - Define Actions for session operations</action>
      <critical_thinking>
        - What specific actions are required for effective session management?
        - How should framework-aware session operations be structured?
        - What GitHub issue management actions support framework tracking?
        - How do actions integrate TDD compliance with framework context?
        - What action sequence optimizes session effectiveness and framework coordination?
      </critical_thinking>
      <output_format>CARE_ACTIONS_DEFINITION:
        - Session actions: [specific_operations_list]
        - Framework integration: [framework_tracking_actions]
        - GitHub operations: #[number] with framework context
        - TDD coordination: [compliance_tracking_actions]</output_format>
      <validation>Actions clearly defined with framework integration and TDD coordination</validation>
      <enforcement>VERIFY actions support framework context preservation and TDD tracking</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Apply CARE framework - Execute Results tracking and validation</action>
      <critical_thinking>
        - What specific results have been achieved in this session?
        - How do session results align with framework objectives and TDD compliance?
        - What measurable outcomes demonstrate session progress?
        - How should results be documented for framework continuity?
        - What result validation ensures session quality and effectiveness?
      </critical_thinking>
      <output_format>CARE_RESULTS_TRACKING:
        - Session achievements: [measurable_outcomes]
        - Framework progress: [framework_advancement]
        - TDD compliance: [status_with_metrics]
        - Quality validation: [results_verification]</output_format>
      <validation>Results comprehensively tracked with framework alignment and TDD validation</validation>
      <enforcement>ENSURE results demonstrate framework progress and TDD compliance verification</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Apply CARE framework - Perform Evaluation and session assessment</action>
      <critical_thinking>
        - How effectively did the session achieve its framework-aligned objectives?
        - What evaluation criteria best assess session quality and framework integration?
        - What lessons learned improve future framework-aware session management?
        - How does session evaluation inform framework optimization and TDD improvement?
        - What evaluation feedback enhances session management methodology?
      </critical_thinking>
      <output_format>CARE_EVALUATION_ASSESSMENT:
        - Objective achievement: [framework_alignment_success]
        - Quality assessment: [session_effectiveness_metrics]
        - Lessons learned: [framework_optimization_insights]
        - Improvement opportunities: [methodology_enhancements]</output_format>
      <validation>Session comprehensively evaluated with framework integration and methodology improvement</validation>
      <enforcement>BLOCK completion if evaluation insufficient for framework optimization learning</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Finalize CARE framework session with artifact linking and preservation</action>
      <critical_thinking>
        - How should framework context and decisions be preserved for future sessions?
        - What artifacts best demonstrate framework integration and TDD compliance?
        - How can session preservation optimize future framework-aware work?
        - What linking strategies ensure framework continuity across sessions?
        - How does artifact preservation support framework learning and optimization?
      </critical_thinking>
      <output_format>CARE_SESSION_FINALIZATION:
        - Framework preservation: [context_and_decisions_preserved]
        - Artifact linking: [commits_prs_tests_with_framework_evidence]
        - Continuity optimization: [future_session_enhancement]
        - Learning capture: [framework_methodology_insights]</output_format>
      <validation>Session finalized with comprehensive framework preservation and artifact integration</validation>
      <enforcement>VERIFY framework context and TDD evidence preserved for optimal session continuity</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <care_framework_integration enforcement="MANDATORY">
    <context_analysis>Comprehensive session context analysis including framework state and TDD requirements</context_analysis>
    <action_definition>Clear session operation actions with framework integration and coordination</action_definition>
    <results_tracking>Measurable session outcomes with framework progress and quality validation</results_tracking>
    <evaluation_assessment>Session effectiveness evaluation with framework optimization and methodology improvement</evaluation_assessment>
    <session_optimization>Framework-aware session management with context preservation and continuity enhancement</session_optimization>
    <validation>Reference frameworks/care.md for complete CARE framework implementation in session management</validation>
  </care_framework_integration>
  
  <usage_examples>
    <example type="start">/session start "Implement OAuth2 authentication" # Creates #124</example>
    <example type="update">/session update "Completed user model, TDD tests passing"</example>
    <example type="link">/session link PR-456 # Links PR to current session</example>
    <example type="complete">/session complete "OAuth2 fully implemented with 95% coverage"</example>
    <example type="view">/session view 123 # Shows full session history</example>
  </usage_examples>
  
  <github_integration>
    <feature>Creates GitHub issues with AI session template</feature>
    <feature>Manages labels programmatically (ai-session, active, completed)</feature>
    <feature>Links commits and PRs automatically</feature>
    <feature>Provides searchable session history</feature>
    <feature>Zero external dependencies - pure GitHub CLI</feature>
  </github_integration>
  
  <strict_enforcement target="session_tracking">
    <primary_rule>Multi-agent work MUST use session tracking for coordination</primary_rule>
    <verification>Complex tasks automatically prompt for session creation</verification>
    <consequence>Session-less multi-agent work creates coordination failures</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/patterns/session-management.md for complete implementation details including GitHub CLI operations, session templates, workflow integration, and team coordination patterns.
  </reference>
  
  <tdd_integration enforcement="MANDATORY">
    <session_tdd_tracking>Document TDD progress and compliance in all development sessions</session_tdd_tracking>
    <test_artifact_linking>Link test files, coverage reports, and TDD evidence to sessions</test_artifact_linking>
    <methodology_preservation>Preserve TDD methodology decisions and lessons learned</methodology_preservation>
    <validation>Reference quality/tdd.md#session_tracking for TDD session management</validation>
    <blocking_conditions>
      <condition>Development session lacks TDD progress tracking</condition>
      <condition>Session completion without TDD compliance verification</condition>
      <condition>Artifacts missing TDD evidence or test links</condition>
      <condition>Multi-agent coordination without TDD synchronization</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before framework-aware session operations</module>
      <module>frameworks/care.md - CARE framework context, action, result, evaluation for session management</module>
      <module>patterns/session-management.md - Framework-integrated GitHub issue management and tracking</module>
      <module>quality/tdd.md - TDD progress tracking with framework alignment and compliance documentation</module>
      <module>patterns/git-operations.md - Framework-aware artifact linking and version control integration</module>
    </core_stack>
    <contextual_modules>
      <conditional module="frameworks/framework-selector.md" condition="complex_session_requirements"/>
      <conditional module="frameworks/advanced-frameworks.md" condition="specialized_framework_needs"/>
      <conditional module="quality/production-standards.md" condition="development_session"/>
      <conditional module="patterns/multi-agent.md" condition="swarm_coordination"/>
      <conditional module="context/restore-session.md" condition="session_resumption"/>
    </contextual_modules>
  </module_execution>
  
  <pattern_usage>
    • Uses care_framework_integration pattern for systematic session management
    • Implements issue_tracking pattern with framework context preservation
    • Applies explicit_validation for framework-aware session operations
    • Leverages single_responsibility pattern for focused session management
    • Uses graceful_degradation for error handling with framework awareness
    • Integrates framework_selection_intelligence for session optimization
    
    See modules/frameworks/care.md for CARE framework implementation
    See modules/patterns/pattern-library.md for pattern details
    See modules/patterns/session-management.md for framework-integrated implementation
  </pattern_usage>
  

  <prompt_construction>
    <assembly_preview>
      WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. Session     │ → GitHub issue management
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Type        │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. Context     │ → State preservation
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Management  │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. Artifact    │ → Link tracking
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Linking     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. Progress    │ → Status updates
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │    Tracking    │
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~6,000
      - Session operations: 2,000
      - Context preservation: 1,500
      - Artifact linking: 1,500
      - Progress updates: 1,000
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /session create "API refactor"
      [00:15] 🎯 SESSION: GitHub issue #157 created
      [00:30] 💾 CONTEXT: Preserving session state
      [00:45] 🔗 ARTIFACTS: Linking related files and tasks
      [01:00] ✅ COMPLETE: Session ready for development
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Reads checkpoint structure sequentially
      2. Executes critical_thinking questions internally
      3. Formats output according to output_format specifications
      4. Validates against enforcement rules before proceeding
      5. Applies parallel execution optimization where possible
    </parsing_behavior>

    <decision_points>
      - Checkpoint failures trigger enforcement actions
      - Module selection based on contextual conditions
      - Parallel execution for independent operations
      - Quality gate validation at completion boundaries
      - Error recovery through graceful degradation paths
    </decision_points>
  </claude_4_interpretation>

</command>
```