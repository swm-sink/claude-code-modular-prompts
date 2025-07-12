| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

# Session Command - Long-Running Workflow Management

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="session" category="management" enforcement="BLOCKING">
  
  <purpose>
    Execute long-running development sessions with comprehensive GitHub issue tracking, progress management, context preservation, and recovery mechanisms optimized for Claude 4 extended reasoning capabilities.
  </purpose>
  
  <scope>
    <includes>Multi-phase projects, complex features, extended development, progress tracking, context management</includes>
    <excludes>Simple tasks, single-phase work, quick fixes, standalone operations</excludes>
    <boundaries>Projects requiring >10 steps, extended timelines, or comprehensive progress tracking and recovery</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Long-running project description with clear objectives, phases, and success criteria</required_arguments>
    <context_requirements>GitHub repository access, project scope definition, stakeholder requirements, timeline constraints</context_requirements>
    <preconditions>GitHub repository available, issue tracking enabled, project scope approved, timeline established</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Complete project implementation, comprehensive progress tracking, documented milestones, recovery procedures</deliverables>
    <success_criteria>All project phases completed, progress tracked, objectives achieved, documentation complete</success_criteria>
    <artifacts>Project implementation, GitHub issues, progress reports, milestone documentation, recovery procedures</artifacts>
  </output_specification>
</command>
```

Long-running session management with GitHub issue tracking.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>Pre-Session Atomic Commit: Create secure rollback point before long-running session begins</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What is the current state that must be preserved before the long-running session?
        - What session changes will be made that need comprehensive rollback capability?
        - How can we ensure instant recovery if the session needs to be restarted?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Safety Question: Is the current state safely preserved before session begins?]
        - [Session Question: What long-running operations need atomic safety protection?]
        - [Recovery Question: Can we rollback session changes if issues arise?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <pre_operation>git add -A && git commit -m "PRE-OP: session - backup state before long-running session"</pre_operation>
      <validation>Session baseline established for comprehensive rollback</validation>
      <rollback_capability>Available via: git reset --hard HEAD~1</rollback_capability>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>Project Scope Analysis and Phase Planning: Comprehensive analysis of project requirements and systematic phase breakdown</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What are the complete project objectives and deliverable requirements?
        - How should the project be broken down into manageable phases?
        - What dependencies and risks require careful planning and mitigation?
      </pre_analysis>
      <critical_thinking minimum_time="60_seconds">
        - [Scope Question: What are the precise project boundaries and deliverable requirements?]
        - [Phase Question: How can the project be optimally divided into trackable phases?]
        - [Dependency Question: What critical dependencies could impact project timeline and execution?]
        - [Risk Question: What project risks require proactive mitigation strategies?]
        - [Resource Question: What resources and capabilities are required for successful completion?]
        - [Timeline Question: How should phases be sequenced for optimal progress and risk management?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this phase breakdown optimize project management and execution?
        - What evidence supports the project scope and timeline feasibility?
        - How does risk mitigation strategy ensure project success and recovery capability?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch project analysis, phase planning, and risk assessment for comprehensive planning</tool_optimization>
      <context_efficiency>Load project requirements, stakeholder input, and resource constraints concurrently</context_efficiency>
      <dependency_analysis>Identify planning steps that can be parallelized vs sequential project structuring</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>SESSION_PLAN: [project_scope] with [phases] requiring [dependencies] and [risk_mitigation]</output_format>
    <validation>Project scope clearly defined, phases logically structured, dependencies mapped, risks identified and mitigated</validation>
    <enforcement>BLOCK session execution until comprehensive project planning validates systematic approach</enforcement>
    <context_transfer>Project scope definition, phase structure, dependency map, risk mitigation plan</context_transfer>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>GitHub Issue Creation and Tracking Setup: Establish comprehensive issue tracking with milestone management</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should GitHub issues be structured for optimal project tracking?
        - What milestone and progress tracking ensures comprehensive project visibility?
        - How can issue organization support effective project management and recovery?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Structure Question: Are GitHub issues optimally organized for project tracking and management?]
        - [Milestone Question: Do milestones provide clear progress indicators and checkpoint validation?]
        - [Tracking Question: Does issue tracking enable effective progress monitoring and recovery?]
        - [Organization Question: Is issue organization supportive of project complexity and coordination?]
        - [Recovery Question: Do tracking mechanisms support effective project recovery and continuation?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this issue structure optimize project tracking and management?
        - What evidence shows effective milestone design for progress monitoring?
        - How does tracking organization support project success and recovery?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch GitHub issue creation, milestone setup, and tracking configuration</tool_optimization>
      <context_efficiency>Configure issue tracking and milestone management concurrently</context_efficiency>
      <dependency_analysis>Identify tracking setup that can be parallelized while maintaining organizational integrity</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>TRACKING_SETUP: [issues_created] with [milestones] enabling [progress_monitoring] and [recovery_capability]</output_format>
    <validation>GitHub issues created, milestones established, progress tracking operational, recovery mechanisms ready</validation>
    <enforcement>BLOCK session start until comprehensive tracking validates project management capability</enforcement>
    <context_transfer>Issue tracking structure, milestone configuration, progress monitoring setup, recovery procedures</context_transfer>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Context Preservation and Session Management: Implement robust context management and session continuity</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How can project context be preserved across extended development sessions?
        - What session management ensures continuity and effective progress tracking?
        - How can context recovery support session interruption and resumption?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Context Question: Is project context comprehensively preserved for session continuity?]
        - [Continuity Question: Does session management support effective long-running development?]
        - [Recovery Question: Can sessions be effectively resumed after interruptions with full context?]
        - [Progress Question: Is progress tracking maintained consistently across session boundaries?]
        - [Quality Question: Does context preservation maintain development quality and consistency?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this context management approach ensure session continuity and quality?
        - What evidence shows effective session management for long-running projects?
        - How does context preservation support development consistency and recovery?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch context preservation, session configuration, and continuity setup</tool_optimization>
      <context_efficiency>Implement context management and session tracking concurrently</context_efficiency>
      <dependency_analysis>Identify context management that can be optimized while ensuring preservation integrity</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>CONTEXT_MANAGEMENT: [preservation_active] with [session_continuity] enabling [recovery_capability] and [progress_maintenance]</output_format>
    <validation>Context preservation active, session management operational, recovery capability confirmed, progress tracking maintained</validation>
    <enforcement>BLOCK phase execution until comprehensive context management validates session continuity</enforcement>
    <context_transfer>Context preservation system, session management configuration, recovery procedures, progress tracking</context_transfer>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Progressive Phase Execution with Checkpoint Management: Execute project phases with systematic checkpoint validation</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should project phases be executed with effective checkpoint management?
        - What progress validation ensures each phase meets quality and completion standards?
        - How can phase execution maintain project momentum while ensuring quality?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Execution Question: Is each project phase executed systematically with proper validation?]
        - [Checkpoint Question: Do checkpoints provide effective validation and progress confirmation?]
        - [Quality Question: Does phase execution maintain consistent quality standards throughout?]
        - [Momentum Question: Is project momentum maintained while ensuring thorough validation?]
        - [Coordination Question: Are phases properly coordinated for optimal project flow?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this phase execution approach ensure project success and quality?
        - What evidence shows effective checkpoint management for progress validation?
        - How does systematic execution maintain project momentum and standards?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Execute project phases with concurrent checkpoint validation and progress tracking</tool_optimization>
      <context_efficiency>Optimize phase execution and quality validation for maximum efficiency</context_efficiency>
      <dependency_analysis>Identify phase execution that can be optimized while maintaining quality and coordination</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>PHASE_EXECUTION: [phases_completed] with [checkpoints_validated] maintaining [quality_standards] and [project_momentum]</output_format>
    <validation>Project phases executed systematically, checkpoints validated, quality maintained, momentum sustained</validation>
    <enforcement>BLOCK completion until systematic phase execution validates comprehensive project progress</enforcement>
    <context_transfer>Phase completion status, checkpoint validation, quality confirmation, momentum assessment</context_transfer>
  </checkpoint>
  
  <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Project Completion and Documentation: Finalize project with comprehensive documentation and handoff</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should project completion be validated and documented comprehensively?
        - What handoff documentation ensures effective knowledge transfer and maintenance?
        - How can project closure provide value for future development and reference?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Completion Question: Is project completion comprehensive with all objectives achieved?]
        - [Documentation Question: Is project documentation thorough and valuable for future reference?]
        - [Handoff Question: Does handoff documentation enable effective knowledge transfer?]
        - [Value Question: Does project closure provide maximum value for ongoing development?]
        - [Legacy Question: Will project outcomes support future development and decision-making?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this completion approach ensure comprehensive project success?
        - What evidence demonstrates effective documentation and knowledge transfer?
        - How does project closure maximize ongoing value and future development support?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch project validation, documentation creation, and handoff preparation</tool_optimization>
      <context_efficiency>Complete project closure and documentation concurrently</context_efficiency>
      <dependency_analysis>Identify completion activities that can be optimized while ensuring comprehensive closure</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>SESSION_COMPLETE: [project_delivered] with [documentation_complete] ensuring [knowledge_transfer] and [future_value]</output_format>
    <validation>Project objectives achieved, documentation comprehensive, knowledge transfer effective, future value ensured</validation>
    <enforcement>BLOCK session closure until comprehensive completion validates project success and value</enforcement>
    <context_transfer>Project completion confirmation, comprehensive documentation, knowledge transfer validation, future value assessment</context_transfer>
  </checkpoint>
  
</thinking_pattern>
```

## Instructions

Execute long-running development session workflow for: $ARGUMENTS

1. **Project Planning**: Analyze scope and break down into manageable phases.
   - **Planning Checkpoint**: Create comprehensive project plan with risk mitigation

2. **GitHub Issue Setup**: Create detailed tracking issues with milestone management.
   - **Tracking Checkpoint**: Establish comprehensive issue tracking and progress monitoring

3. **Context Management**: Implement robust context preservation and session continuity.
   - **Context Checkpoint**: Activate context preservation and recovery mechanisms

4. **Progressive Execution**: Execute project phases with systematic checkpoint validation.
   - **Execution Checkpoints**: Validate each phase completion with quality standards

5. **Project Completion**: Finalize project with comprehensive documentation and handoff.
   - **Completion Checkpoint**: Validate project success and ensure knowledge transfer

## Critical Rules

- ALWAYS create GitHub issues for projects >10 steps
- NEVER proceed without comprehensive project planning and risk assessment
- Maintain context preservation throughout extended development sessions
- Use systematic checkpoint validation for each project phase
- **SESSION SAFETY**: Implement robust recovery mechanisms for session interruptions
- **PROGRESS TRACKING**: Continuously update GitHub issues with progress status

## Session Management Features

```xml
<session_capabilities>
  <context_preservation>Robust context management across session boundaries</context_preservation>
  <progress_tracking>Comprehensive GitHub issue tracking with milestone management</progress_tracking>
  <recovery_mechanisms>Session interruption recovery with context restoration</recovery_mechanisms>
  <checkpoint_validation>Systematic phase validation with quality gates</checkpoint_validation>
</session_capabilities>
```

## Module Integration

```xml
<module_orchestration>
  <core_modules>
    <module>patterns/thinking/critical-thinking-pattern.md</module>
    <module>system/session/session-management.md</module>
    <module>development/task-management.md</module>
    <module>quality/universal-quality-gates.md</module>
  </core_modules>
  
  <contextual_modules>
    <module condition="multi_component">patterns/multi-agent.md</module>
    <module condition="complex_integration">patterns/integration-pattern.md</module>
    <module condition="security_sensitive">security/threat-modeling.md</module>
    <module condition="performance_critical">patterns/performance-optimization.md</module>
  </contextual_modules>
  
  <support_modules>
    <module>patterns/comprehensive-error-handling.md</module>
    <module>patterns/error-recovery.md</module>
    <module>patterns/context-management-pattern.md</module>
    <module>patterns/validation-pattern.md</module>
    <module>system/git/git-management.md</module>
  </support_modules>
</module_orchestration>
```

## Session Error Handling

```xml
<error_handling framework="session_management" enforcement="COMPREHENSIVE">
  <error_classification_integration>
    <module>patterns/comprehensive-error-handling.md</module>
    <session_specific_patterns>Context preservation failures, progress tracking errors, GitHub integration issues</session_specific_patterns>
  </error_classification_integration>
  
  <graceful_degradation>
    <context_preservation_failures>Maintain partial context, document gaps, implement recovery checkpoints</context_preservation_failures>
    <github_integration_failures>Fall back to local tracking, sync when connection restored</github_integration_failures>
    <progress_tracking_failures>Maintain manual progress log, restore from checkpoints</progress_tracking_failures>
  </graceful_degradation>
  
  <recovery_procedures>
    <context_recovery>Restore from last successful checkpoint, rebuild context from artifacts</context_recovery>
    <progress_restoration>Sync with GitHub issues, reconstruct progress from commits</progress_restoration>
    <session_continuation>Resume from last stable phase, validate continuation points</session_continuation>
  </recovery_procedures>
</error_handling>

## Original Error Handling

```xml
<error_handling>
  <session_failures>
    <context_loss>Restore from preserved context, validate session state, resume from checkpoint</context_loss>
    <progress_interruption>Resume from last GitHub issue checkpoint, validate progress, continue execution</progress_interruption>
    <phase_failure>Rollback to previous phase checkpoint, address issues, restart phase execution</phase_failure>
    <tracking_corruption>Restore GitHub issue state, validate progress records, recreate tracking if needed</tracking_corruption>
  </session_failures>
  
  <escalation_paths>
    <complex_coordination>Use /swarm for multi-component coordination within session</complex_coordination>
    <production_requirements>Route to /protocol for production-critical session phases</production_requirements>
    <research_needs>Use /query for research phases within session workflow</research_needs>
    <documentation_needs>Use /docs for comprehensive documentation phases</documentation_needs>
  </escalation_paths>
  
  <recovery_procedures>
    <session_restoration>Restore context, validate progress, resume from last checkpoint</session_restoration>
    <progress_recovery>Validate GitHub issues, update progress, continue from validated state</progress_recovery>
    <quality_recovery>Re-validate quality gates, address issues, ensure standards compliance</quality_recovery>
    <documentation_recovery>Restore documentation state, validate completeness, update as needed</documentation_recovery>
  </recovery_procedures>
</error_handling>
```

## When to Use

- Projects requiring >10 development steps
- Complex features with multiple integration points
- Extended development requiring progress tracking
- Work needing comprehensive documentation and handoff
- Projects with stakeholder visibility requirements

## Examples

- `/session "Implement complete user management system"` - Comprehensive user management feature
- `/session "Refactor entire authentication system"` - Complex system-wide refactoring
- `/session "Add monitoring to all services"` - Cross-cutting monitoring implementation
- `/session "Migrate database architecture"` - Large-scale system migration
- `/session "Implement payment processing system"` - Complex integration project