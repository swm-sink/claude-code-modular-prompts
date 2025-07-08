| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-01-08   | stable |

# Context Restoration Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="restore_session" category="context">
  
  <purpose>
    Restore comprehensive context after session breaks with 90% faster context recovery through intelligent state capture and smart summarization.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Session resumption after interruption or timeout</condition>
    <condition type="explicit">User requests context restoration via /session or /protocol commands</condition>
    <condition type="manual">New session needs previous session context</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="context_capture" order="1">
      <requirements>
        Current task state captured with completion percentage
        Recent file changes tracked with modification timestamps
        Active branch information and git status preserved
        Incomplete operations documented with next steps
        Decision artifacts and reasoning preserved
      </requirements>
      <actions>
        Capture current working directory and active files
        Document task progress with specific completion markers
        Record git branch, uncommitted changes, and stash status
        Identify incomplete operations and their current state
        Preserve decision context and architectural choices made
        Save artifact references and their current status
      </actions>
      <validation>
        All critical context elements identified and captured
        Task state documented with actionable next steps
        File system state preserved with change tracking
        Git repository state completely captured
      </validation>
    </phase>
    
    <phase name="smart_summarization" order="2">
      <requirements>
        Intelligent summary of work completed and remaining
        Key decisions and their rationales preserved
        Critical file paths and their current states documented
        Next logical steps identified and prioritized
        Context compressed for efficient token usage
      </requirements>
      <actions>
        Generate concise summary: "You were working on [X], completed [Y], next step is [Z]"
        Extract key decisions with rationales and impacts
        Document critical file modifications and their purposes
        Identify logical next steps based on current progress
        Compress verbose context into essential information
      </actions>
      <validation>
        Summary accurately reflects actual progress and state
        Key information preserved while eliminating redundancy
        Next steps clearly identified and actionable
        Context size optimized for efficient restoration
      </validation>
    </phase>
    
    <phase name="restoration_delivery" order="3">
      <requirements>
        Context presented in immediately actionable format
        Critical information highlighted for quick recognition
        Next steps prioritized and clearly defined
        Supporting details available but not overwhelming
        Restoration completed within 30 seconds maximum
      </requirements>
      <actions>
        Present high-level summary as first priority information
        Highlight critical decisions and their current status
        List immediate next actions in priority order
        Provide detailed context as expandable supporting information
        Verify all essential elements successfully restored
      </actions>
      <validation>
        Context restoration completed rapidly and accurately
        User can immediately continue work without confusion
        All critical information accessible and organized
        Supporting details available without cluttering main view
      </validation>
    </phase>
    
  </implementation>
  
  <context_elements>
    <task_progress>
      <current_objective>Main goal or feature being developed</current_objective>
      <completion_status>Percentage complete with specific milestones achieved</completion_status>
      <active_files>Files currently being modified with their purposes</active_files>
      <blocked_items>Issues preventing progress with resolution paths</blocked_items>
      <next_steps>Immediate actions required to continue progress</next_steps>
    </task_progress>
    
    <technical_state>
      <git_status>Branch, uncommitted changes, stash contents</git_status>
      <build_status>Last successful build, test results, deployment state</build_status>
      <dependencies>Recent installations, updates, or configuration changes</dependencies>
      <environment>Active virtual environments, containers, or services</environment>
      <debug_state>Breakpoints, debug sessions, or diagnostic tools active</debug_state>
    </technical_state>
    
    <decision_context>
      <architectural_choices>Key design decisions made and their rationales</architectural_choices>
      <technology_selections>Frameworks, libraries, or tools chosen with reasons</technology_selections>
      <implementation_approach>Specific patterns or methodologies being followed</implementation_approach>
      <rejected_alternatives>Approaches considered but not chosen with reasons</rejected_alternatives>
      <future_considerations>Known technical debt or planned improvements</future_considerations>
    </decision_context>
    
    <workflow_context>
      <command_history>Recent commands executed with their outcomes</command_history>
      <session_artifacts>GitHub issues, PRs, or tracking items created</session_artifacts>
      <communication_threads>Relevant discussions or decisions made</communication_threads>
      <external_dependencies>Third-party services, APIs, or resources in use</external_dependencies>
      <scheduling_context>Deadlines, milestones, or time-sensitive elements</scheduling_context>
    </workflow_context>
  </context_elements>
  
  <capture_mechanisms>
    <automated_capture>
      <git_integration>Automatic capture of git status, branch, and recent commits</git_integration>
      <file_monitoring>Track file modifications with timestamps and purposes</file_monitoring>
      <command_logging>Log executed commands and their outcomes</command_logging>
      <artifact_tracking>Monitor created artifacts (issues, PRs, documents)</artifact_tracking>
    </automated_capture>
    
    <explicit_checkpoints>
      <milestone_markers>Manual checkpoints at significant progress points</milestone_markers>
      <decision_documentation>Explicit capture of important decisions</decision_documentation>
      <state_snapshots>Manual context snapshots before major changes</state_snapshots>
      <problem_documentation>Capture of issues encountered and resolution attempts</problem_documentation>
    </explicit_checkpoints>
    
    <intelligent_inference>
      <progress_analysis>Infer completion status from file changes and commits</progress_analysis>
      <intent_recognition>Understand ongoing objectives from recent activities</intent_recognition>
      <dependency_mapping>Identify related files and components being worked on</dependency_mapping>
      <pattern_detection>Recognize recurring workflows and optimization opportunities</pattern_detection>
    </intelligent_inference>
  </capture_mechanisms>
  
  <summarization_strategies>
    <hierarchical_summary>
      <level_1>One-sentence summary of current work and immediate next step</level_1>
      <level_2>Paragraph summary with key decisions and progress milestones</level_2>
      <level_3>Detailed context with technical decisions and implementation details</level_3>
      <level_4>Complete context with full decision history and alternatives considered</level_4>
    </hierarchical_summary>
    
    <context_compression>
      <decision_artifacts>Preserve decision rationales in compressed format</decision_artifacts>
      <file_purpose_mapping>Map files to their roles in the current objective</file_purpose_mapping>
      <dependency_graphs>Visual representation of component relationships</dependency_graphs>
      <timeline_compression>Key events and decisions in chronological order</timeline_compression>
    </context_compression>
    
    <priority_weighting>
      <critical_immediate>Information needed to continue work immediately</critical_immediate>
      <important_supporting>Context that influences decisions but isn't blocking</important_supporting>
      <useful_background>Historical information that provides useful perspective</useful_background>
      <archival_detail>Complete information available but not immediately needed</archival_detail>
    </priority_weighting>
  </summarization_strategies>
  
  <restoration_formats>
    <quick_briefing>
      <format>
        🎯 **Current Objective**: [Main goal]
        ✅ **Completed**: [Key milestones achieved]
        🔄 **In Progress**: [Current active work]
        ⚠️ **Blocked**: [Issues preventing progress]
        ➡️ **Next Steps**: [Immediate actions]
      </format>
      <timing>Delivered within 10 seconds for immediate orientation</timing>
    </quick_briefing>
    
    <detailed_context>
      <format>
        ## Current State Summary
        
        ### 🎯 Objective
        [Detailed description of current work and goals]
        
        ### 📊 Progress Status
        - [Milestone 1]: ✅ Complete
        - [Milestone 2]: 🔄 In Progress (X% complete)
        - [Milestone 3]: ⏳ Pending
        
        ### 🔧 Technical State
        - **Branch**: `[current-branch]`
        - **Uncommitted Changes**: [file list with purposes]
        - **Build Status**: [last successful build/test results]
        - **Environment**: [active services, containers, etc.]
        
        ### 🧠 Key Decisions Made
        - [Decision 1]: [Rationale and impact]
        - [Decision 2]: [Rationale and impact]
        
        ### ➡️ Immediate Next Steps
        1. [High priority action with clear outcome]
        2. [Medium priority action with clear outcome]
        3. [Lower priority action with clear outcome]
        
        ### 🔍 Supporting Context
        [Expandable details available on request]
      </format>
      <timing>Delivered within 30 seconds for comprehensive restoration</timing>
    </detailed_context>
    
    <interactive_exploration>
      <capability>Ask specific questions about any aspect of the context</capability>
      <navigation>Drill down into specific decisions, files, or technical details</navigation>
      <clarification>Request elaboration on any summary point</clarification>
      <update>Correct or refine any aspect of the restored context</update>
    </interactive_exploration>
  </restoration_formats>
  
  <performance_optimization>
    <context_indexing>
      <key_artifacts>Index critical files, decisions, and milestones for quick access</key_artifacts>
      <relationship_mapping>Pre-compute relationships between code components</relationship_mapping>
      <change_tracking>Maintain efficient change logs for rapid state reconstruction</change_tracking>
    </context_indexing>
    
    <compression_techniques>
      <semantic_compression>Preserve meaning while reducing token count</semantic_compression>
      <hierarchical_detail>Layer information by importance and immediacy</hierarchical_detail>
      <reference_linking>Use references instead of duplicating information</reference_linking>
    </compression_techniques>
    
    <delivery_optimization>
      <progressive_loading>Deliver critical information first, details on demand</progressive_loading>
      <adaptive_depth>Adjust detail level based on session complexity</adaptive_depth>
      <caching_strategy>Cache frequently accessed context patterns</caching_strategy>
    </delivery_optimization>
  </performance_optimization>
  
  <integration_workflows>
    <session_management>
      <session_start>Automatic context restoration when resuming interrupted work</session_start>
      <session_handoff>Transfer context between different work sessions</session_handoff>
      <session_archival>Preserve context for future reference and learning</session_archival>
    </session_management>
    
    <command_integration>
      <task_command>Restore context for continuing specific task work</task_command>
      <feature_command>Restore context for complex feature development</feature_command>
      <swarm_command>Restore multi-agent coordination context</swarm_command>
      <protocol_command>Restore interrupted workflow protocols</protocol_command>
    </command_integration>
    
    <artifact_preservation>
      <github_sessions>Link to relevant GitHub issues and PRs</github_sessions>
      <decision_registry>Preserve architectural decisions and rationales</decision_registry>
      <code_artifacts>Maintain links to relevant code files and changes</code_artifacts>
      <documentation>Preserve relevant documentation and specifications</documentation>
    </artifact_preservation>
  </integration_workflows>
  
  <error_recovery>
    <incomplete_context>
      <partial_restoration>Provide best available context with gaps identified</partial_restoration>
      <gap_filling>Intelligent inference to fill missing context elements</gap_filling>
      <user_correction>Allow user to provide missing information</user_correction>
    </incomplete_context>
    
    <context_conflicts>
      <version_resolution>Handle conflicts between different context versions</version_resolution>
      <priority_merging>Merge conflicting information with priority weighting</priority_merging>
      <user_arbitration>Allow user to resolve conflicting context elements</user_arbitration>
    </context_conflicts>
    
    <corruption_handling>
      <validation_checks>Verify context integrity during restoration</validation_checks>
      <fallback_mechanisms>Alternative restoration methods when primary fails</fallback_mechanisms>
      <reconstruction>Rebuild context from available artifacts when necessary</reconstruction>
    </corruption_handling>
  </error_recovery>
  
  <usage_examples>
    <quick_restore>
      <trigger>"What was I working on?"</trigger>
      <response>
        🎯 **Current Objective**: Implementing user authentication with JWT
        ✅ **Completed**: Database schema, user model, password hashing
        🔄 **In Progress**: JWT token generation (80% complete)
        ⚠️ **Blocked**: Need to configure token expiration policy
        ➡️ **Next Steps**: Add token refresh endpoint, test token validation
      </response>
    </quick_restore>
    
    <technical_restore>
      <trigger>"What's the current state of the codebase?"</trigger>
      <response>
        **Branch**: `feature/auth-system`
        **Uncommitted**: auth.js (JWT implementation), config/auth.json (token settings)
        **Last Build**: ✅ Successful with 2 test failures in auth module
        **Next Action**: Fix failing tests in test/auth.test.js lines 45-62
      </response>
    </technical_restore>
    
    <decision_restore>
      <trigger>"What decisions have we made about the authentication system?"</trigger>
      <response>
        **JWT vs Sessions**: Chose JWT for stateless authentication
        **Token Storage**: Client-side localStorage (considered httpOnly cookies, rejected for API flexibility)  
        **Refresh Strategy**: Sliding window refresh tokens (7-day expiry)
        **Security**: RSA-256 signing with key rotation every 30 days
      </response>
    </decision_restore>
  </usage_examples>
  
  <context_prime_integration>
    <priming_hooks>
      <pre_restoration>Integrate with project-priming module for enhanced context loading</pre_restoration>
      <intelligent_analysis>Leverage project structure analysis for better context restoration</intelligent_analysis>
      <performance_optimization>Share caching strategies and parallel execution techniques</performance_optimization>
      <security_coordination>Coordinate timeout mechanisms and approval workflows</security_coordination>
    </priming_hooks>
    
    <enhanced_capabilities>
      <project_awareness>Context restoration enhanced with project structure understanding</project_awareness>
      <workflow_integration>Restoration coordinated with active development workflows</workflow_integration>
      <performance_sharing>Shared performance optimizations for <3s loading targets</performance_sharing>
      <security_alignment>Aligned security controls with context-prime mechanisms</security_alignment>
    </enhanced_capabilities>
  </context_prime_integration>
  
  <integration_points>
    <depends_on>
      patterns/context-preservation.md for artifact management and storage
      patterns/session-management.md for session tracking and coordination
      patterns/intelligent-routing.md for context-aware routing decisions
      context/project-priming.md for enhanced context loading capabilities
    </depends_on>
    <provides_to>
      All commands for intelligent context restoration
      patterns/session-management.md for enhanced session continuity
      development/task-management.md for task state preservation
      context/project-priming.md for restoration integration and optimization
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">context_preservation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">intelligent_summarization</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">progressive_disclosure</uses_pattern>
    <implementation_notes>
      Context capture follows context_preservation pattern for consistency
      Summary generation uses intelligent_summarization for optimal compression
      Information delivery implements progressive_disclosure for user experience
      Integration with session management follows established session patterns
    </implementation_notes>
  </pattern_usage>
  
</module>
```