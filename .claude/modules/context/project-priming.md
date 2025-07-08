| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Project Priming Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="project_priming" category="context">
  
  <purpose>
    Intelligent project context establishment with performance optimization, security controls, and workflow integration for maximum development efficiency.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze project structure and current development state</step>
    <step>2. Load recent commits, branches, and architectural decisions</step>
    <step>3. Identify active development patterns and workflows</step>
    <step>4. Prime context with performance optimization and security controls</step>
    <step>5. Integrate with existing development workflows and commands</step>
    <step>6. Validate priming effectiveness and optimize for sustained productivity</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="explicit">User requests context priming via /context-prime command</condition>
    <condition type="automatic">New development session requiring comprehensive context establishment</condition>
    <condition type="performance">Context loading optimization needed for workflow efficiency</condition>
    <condition type="integration">Workflow integration requiring project understanding</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="project_analysis" order="1">
      <requirements>
        Project structure comprehensively analyzed with architecture recognition
        Recent development activity tracked with commit and branch analysis
        Active patterns identified with workflow recognition
        Performance requirements established with optimization targets
      </requirements>
      <actions>
        Analyze directory structure with architecture pattern recognition
        Examine recent commits for development context and decision history
        Identify active branches and their development purposes
        Recognize development patterns, frameworks, and workflow conventions
        Establish performance baselines with <3s loading and memory optimization
      </actions>
      <validation>
        Project structure completely analyzed with architectural understanding
        Recent activity comprehensively tracked with decision context
        Active patterns identified with workflow integration requirements
        Performance targets established with optimization strategy
      </validation>
    </phase>
    
    <phase name="context_loading" order="2">
      <requirements>
        Context loaded with <3s performance target and memory optimization
        Security controls activated with timeout and approval mechanisms
        Workflow integration established with existing command compatibility
        Quality assurance applied with TDD methodology awareness
      </requirements>
      <actions>
        Load project context with parallel execution for 70% performance improvement
        Activate security controls with 5-minute timeout and approval workflows
        Integrate with session management and intelligent routing systems
        Apply TDD methodology awareness with quality standards integration
        Optimize memory usage for 200k token context window efficiency
      </actions>
      <validation>
        Context loading completed within <3s performance target
        Security controls functioning with timeout and approval mechanisms
        Workflow integration confirmed with existing command compatibility
        Quality standards met with TDD methodology integration
      </validation>
    </phase>
    
    <phase name="priming_optimization" order="3">
      <requirements>
        Context priming optimized for immediate development productivity
        Performance benchmarks achieved with sustained efficiency
        Security validation completed with emergency controls
        Integration testing confirmed with workflow compatibility
      </requirements>
      <actions>
        Optimize context priming for immediate development workflow effectiveness
        Validate performance benchmarks with continuous monitoring
        Test security controls with emergency mechanisms and approval workflows
        Confirm integration compatibility with existing development commands
        Establish monitoring and feedback loops for continuous improvement
      </actions>
      <validation>
        Context priming optimized for maximum development efficiency
        Performance benchmarks consistently achieved with monitoring
        Security controls validated with emergency mechanisms functional
        Integration compatibility confirmed with all development workflows
      </validation>
    </phase>
    
  </implementation>
  
  <intelligent_analysis>
    <project_structure_recognition>
      <directory_analysis>
        <pattern_detection>Identify common project structures (monorepo, microservices, MVC, etc.)</pattern_detection>
        <architecture_inference>Recognize architectural patterns from directory organization</architecture_inference>
        <framework_identification>Detect frameworks, libraries, and technology stacks in use</framework_identification>
        <build_system_analysis>Understand build tools, scripts, and deployment configurations</build_system_analysis>
      </directory_analysis>
      
      <file_importance_scoring>
        <core_files>Configuration files, main entry points, critical business logic</core_files>
        <recent_activity>Files with recent commits, active development focus</recent_activity>
        <architectural_impact>Files affecting system architecture and design decisions</architectural_impact>
        <documentation_relevance>READMEs, architectural docs, decision records</documentation_relevance>
      </file_importance_scoring>
      
      <dependency_mapping>
        <internal_dependencies>Component relationships and module interactions</internal_dependencies>
        <external_dependencies>Third-party libraries, services, and integrations</external_dependencies>
        <configuration_dependencies>Environment settings, deployment requirements</configuration_dependencies>
        <development_dependencies>Tools, testing frameworks, development workflows</development_dependencies>
      </dependency_mapping>
    </project_structure_recognition>
    
    <development_context_analysis>
      <git_history_analysis>
        <recent_commits>Last 10 commits with authors, messages, and change analysis</recent_commits>
        <branch_analysis>Active branches with purposes and development status</branch_analysis>
        <merge_history>Recent merges and their impact on project evolution</merge_history>
        <contributor_patterns>Developer activity patterns and collaboration indicators</contributor_patterns>
      </git_history_analysis>
      
      <active_work_detection>
        <uncommitted_changes>Working directory changes and their development context</uncommitted_changes>
        <stash_analysis>Stashed changes and their relationship to current work</stash_analysis>
        <branch_relationships>Feature branches and their integration status</branch_relationships>
        <conflict_identification>Potential merge conflicts and resolution strategies</conflict_identification>
      </active_work_detection>
      
      <decision_context_reconstruction>
        <commit_message_analysis>Extract decisions and rationales from commit messages</commit_message_analysis>
        <code_comment_analysis>Architectural decisions documented in code comments</code_comment_analysis>
        <documentation_scanning>Design decisions in README, docs, and decision records</documentation_scanning>
        <issue_integration>Link to GitHub issues and their resolution context</issue_integration>
      </decision_context_reconstruction>
    </development_context_analysis>
    
    <workflow_pattern_recognition>
      <development_methodology>
        <tdd_detection>Identify TDD practices and testing patterns in use</tdd_detection>
        <ci_cd_analysis>Continuous integration and deployment workflow analysis</ci_cd_analysis>
        <code_review_patterns>Pull request and code review workflow recognition</code_review_patterns>
        <release_management>Release branching and version management strategies</release_management>
      </development_methodology>
      
      <coding_conventions>
        <style_guide_detection>Identify coding standards and style preferences</style_guide_detection>
        <naming_conventions>Recognize naming patterns and conventions in use</naming_conventions>
        <architectural_patterns>Detect design patterns and architectural approaches</architectural_patterns>
        <testing_strategies>Understand testing approaches and quality assurance methods</testing_strategies>
      </coding_conventions>
      
      <tooling_integration>
        <ide_configuration>Development environment setup and configuration</ide_configuration>
        <build_tools>Build systems, task runners, and automation tools</build_tools>
        <quality_tools>Linting, formatting, and code quality tools</quality_tools>
        <deployment_tools>Deployment scripts, containerization, and infrastructure</deployment_tools>
      </tooling_integration>
    </workflow_pattern_recognition>
  </intelligent_analysis>
  
  <performance_optimization>
    <parallel_execution>
      <concurrent_analysis>
        <file_system_scanning>Parallel directory traversal and file analysis</file_system_scanning>
        <git_operations>Concurrent git log, branch, and status operations</git_operations>
        <content_analysis>Parallel file content parsing and pattern recognition</content_analysis>
        <dependency_resolution>Concurrent package.json, requirements.txt, etc. analysis</dependency_resolution>
      </concurrent_analysis>
      
      <performance_targets>
        <loading_time>Complete context loading in <3 seconds</loading_time>
        <memory_efficiency>Optimize for 200k token context window</memory_efficiency>
        <cache_utilization>Leverage caching for repeated context operations</cache_utilization>
        <incremental_updates>Update context incrementally rather than full reload</incremental_updates>
      </performance_targets>
      
      <optimization_techniques>
        <lazy_loading>Load detailed context only when needed</lazy_loading>
        <content_prioritization>Load critical information first, supporting details later</content_prioritization>
        <compression_strategies>Compress verbose information while preserving meaning</compression_strategies>
        <smart_caching>Cache frequently accessed patterns and structures</smart_caching>
      </optimization_techniques>
    </parallel_execution>
    
    <memory_management>
      <token_optimization>
        <context_compression>Compress verbose information while preserving essential meaning</context_compression>
        <hierarchical_detail>Layer information by importance and immediacy</hierarchical_detail>
        <reference_linking>Use references instead of duplicating information</reference_linking>
        <selective_loading>Load only relevant context based on development focus</selective_loading>
      </token_optimization>
      
      <context_efficiency>
        <structured_summaries>Organized summaries with expandable detail levels</structured_summaries>
        <pattern_recognition>Recognize and reuse common project patterns</pattern_recognition>
        <decision_artifacts>Preserve key decisions in compressed format</decision_artifacts>
        <workflow_shortcuts>Create shortcuts for frequently accessed context</workflow_shortcuts>
      </context_efficiency>
      
      <adaptive_loading>
        <complexity_awareness>Adjust loading strategy based on project complexity</complexity_awareness>
        <user_preferences>Adapt to user's preferred level of detail and focus areas</user_preferences>
        <session_context>Consider ongoing work and immediate development needs</session_context>
        <integration_requirements>Load context appropriate for planned command usage</integration_requirements>
      </adaptive_loading>
    </memory_management>
    
    <caching_strategies>
      <persistent_cache>
        <project_structure>Cache project structure analysis for reuse</project_structure>
        <git_metadata>Cache git log and branch information with incremental updates</git_metadata>
        <dependency_graphs>Cache dependency relationships and architectural patterns</dependency_graphs>
        <pattern_recognition>Cache recognized patterns and framework configurations</pattern_recognition>
      </persistent_cache>
      
      <intelligent_invalidation>
        <change_detection>Invalidate cache based on file system changes</change_detection>
        <git_awareness>Update cache based on git operations and commits</git_awareness>
        <dependency_updates>Refresh cache when dependencies change</dependency_updates>
        <time_based_expiry>Expire cache entries based on age and usage patterns</time_based_expiry>
      </intelligent_invalidation>
      
      <performance_monitoring>
        <cache_hit_rates>Monitor cache effectiveness and optimization opportunities</cache_hit_rates>
        <loading_performance>Track context loading times and identify bottlenecks</loading_performance>
        <memory_usage>Monitor memory consumption and optimize for efficiency</memory_usage>
        <user_satisfaction>Track user feedback and adjust caching strategies</user_satisfaction>
      </performance_monitoring>
    </caching_strategies>
  </performance_optimization>
  
  <security_controls>
    <timeout_mechanisms>
      <operation_timeouts>
        <context_loading>5-minute timeout for comprehensive context operations</context_loading>
        <file_analysis>30-second timeout for individual file analysis operations</file_analysis>
        <git_operations>60-second timeout for git history and branch operations</git_operations>
        <cache_operations>10-second timeout for cache read/write operations</cache_operations>
      </operation_timeouts>
      
      <emergency_controls>
        <kill_switch>Immediate termination of context priming operations</kill_switch>
        <pause_mechanism>Temporary suspension of context loading with resume capability</pause_mechanism>
        <resource_limits>Memory and CPU usage limits with automatic throttling</resource_limits>
        <progress_monitoring>Real-time monitoring of operation progress and status</progress_monitoring>
      </emergency_controls>
      
      <user_intervention>
        <approval_workflows>User approval required for sensitive context operations</approval_workflows>
        <progress_feedback>Real-time feedback on context loading progress and status</progress_feedback>
        <cancellation_options>User can cancel operations at any checkpoint</cancellation_options>
        <customization_controls>User can customize timeout and approval settings</customization_controls>
      </user_intervention>
    </timeout_mechanisms>
    
    <safe_execution>
      <command_validation>
        <input_sanitization>Sanitize all input parameters and file paths</input_sanitization>
        <permission_checks>Verify file system permissions before operations</permission_checks>
        <path_validation>Validate all file paths and prevent directory traversal</path_validation>
        <resource_monitoring>Monitor resource usage and prevent system overload</resource_monitoring>
      </command_validation>
      
      <isolation_controls>
        <sandbox_execution>Execute analysis operations in isolated environment</sandbox_execution>
        <file_access_limits>Limit file system access to project directory</file_access_limits>
        <network_restrictions>Prevent network access during context operations</network_restrictions>
        <system_protection>Protect system resources and prevent interference</system_protection>
      </isolation_controls>
      
      <audit_logging>
        <operation_logging>Log all context priming operations with timestamps</operation_logging>
        <security_events>Log security-related events and potential issues</security_events>
        <performance_metrics>Log performance metrics and optimization opportunities</performance_metrics>
        <user_actions>Log user interactions and approval decisions</user_actions>
      </audit_logging>
    </safe_execution>
    
    <risk_assessment>
      <operation_classification>
        <low_risk>Basic file reading and structure analysis</low_risk>
        <medium_risk>Git operations and commit history analysis</medium_risk>
        <high_risk>External dependency analysis and configuration parsing</high_risk>
        <critical_risk>System-wide analysis and environment detection</critical_risk>
      </operation_classification>
      
      <approval_thresholds>
        <automatic_approval>Low-risk operations proceed without user intervention</automatic_approval>
        <notification_approval>Medium-risk operations with user notification</notification_approval>
        <explicit_approval>High-risk operations require explicit user approval</explicit_approval>
        <administrative_approval>Critical operations require administrative approval</administrative_approval>
      </approval_thresholds>
      
      <mitigation_strategies>
        <progressive_disclosure>Start with basic context and expand based on approval</progressive_disclosure>
        <graceful_degradation>Provide reduced context if full analysis is blocked</graceful_degradation>
        <alternative_approaches>Offer alternative context loading methods</alternative_approaches>
        <user_education>Explain risks and benefits of different context levels</user_education>
      </mitigation_strategies>
    </risk_assessment>
  </security_controls>
  
  <workflow_integration>
    <command_compatibility>
      <session_management>
        <session_context>Integrate with /session command for context preservation</session_context>
        <session_handoff>Transfer primed context to new development sessions</session_handoff>
        <session_restoration>Restore context after interruption or timeout</session_restoration>
        <session_archival>Preserve context for future reference and learning</session_archival>
      </session_management>
      
      <intelligent_routing>
        <context_aware_routing>Enhance /auto command with primed context awareness</context_aware_routing>
        <framework_selection>Improve framework selection based on project context</framework_selection>
        <complexity_assessment>Better complexity scoring with project understanding</complexity_assessment>
        <optimization_opportunities>Identify optimization opportunities based on context</optimization_opportunities>
      </intelligent_routing>
      
      <development_commands>
        <task_integration>Enhance /task command with project context awareness</task_integration>
        <feature_integration>Improve /feature command with architectural understanding</feature_integration>
        <swarm_integration>Optimize /swarm command with project coordination context</swarm_integration>
        <protocol_integration>Enhance /protocol command with project standards awareness</protocol_integration>
      </development_commands>
    </command_compatibility>
    
    <workflow_enhancement>
      <development_acceleration>
        <context_shortcuts>Provide shortcuts to frequently accessed project areas</context_shortcuts>
        <pattern_suggestions>Suggest patterns and approaches based on project context</pattern_suggestions>
        <decision_support>Support decision-making with historical context and rationales</decision_support>
        <workflow_optimization>Identify and suggest workflow optimization opportunities</workflow_optimization>
      </development_acceleration>
      
      <quality_integration>
        <tdd_awareness>Integrate TDD methodology with project context understanding</tdd_awareness>
        <quality_standards>Apply project-specific quality standards and conventions</quality_standards>
        <testing_context>Understand testing approaches and quality assurance methods</testing_context>
        <compliance_requirements>Identify compliance and regulatory requirements</compliance_requirements>
      </quality_integration>
      
      <collaboration_support>
        <team_context>Understand team structure and collaboration patterns</team_context>
        <communication_integration>Integrate with communication and documentation systems</communication_integration>
        <knowledge_sharing>Share context and insights across team members</knowledge_sharing>
        <onboarding_support>Support new team member onboarding with context</onboarding_support>
      </collaboration_support>
    </workflow_enhancement>
    
    <continuous_improvement>
      <feedback_collection>
        <user_feedback>Collect user feedback on context priming effectiveness</user_feedback>
        <performance_monitoring>Monitor performance metrics and optimization opportunities</performance_monitoring>
        <usage_analytics>Analyze usage patterns and improvement opportunities</usage_analytics>
        <success_metrics>Track success metrics and development productivity improvements</success_metrics>
      </feedback_collection>
      
      <adaptive_optimization>
        <learning_algorithms>Learn from usage patterns and optimize context loading</learning_algorithms>
        <personalization>Adapt context priming to individual user preferences</personalization>
        <project_adaptation>Adapt to project-specific patterns and requirements</project_adaptation>
        <continuous_tuning>Continuously tune performance and effectiveness parameters</continuous_tuning>
      </adaptive_optimization>
      
      <evolution_support>
        <pattern_evolution>Evolve context patterns based on project development</pattern_evolution>
        <technology_adaptation>Adapt to new technologies and framework patterns</technology_adaptation>
        <methodology_integration>Integrate new development methodologies and practices</methodology_integration>
        <tool_integration>Integrate with new tools and development environments</tool_integration>
      </evolution_support>
    </continuous_improvement>
  </workflow_integration>
  
  <context_delivery_formats>
    <structured_summary>
      <project_overview>
        <format>
          🏗️ **Project Structure**: [architecture_pattern] with [key_technologies]
          📈 **Recent Activity**: [recent_commits] with focus on [development_areas]
          🔧 **Active Work**: [current_branches] with [development_status]
          📋 **Patterns**: [development_methodologies] with [quality_standards]
          🎯 **Next Steps**: [immediate_actions] for [development_objectives]
        </format>
        <timing>Delivered within 3 seconds for immediate orientation</timing>
      </project_overview>
      
      <detailed_context>
        <format>
          ## Project Context Summary
          
          ### 🏗️ Architecture & Structure
          - **Pattern**: [architectural_pattern] with [component_organization]
          - **Technologies**: [primary_stack] with [supporting_tools]
          - **Dependencies**: [key_dependencies] with [version_constraints]
          
          ### 📈 Development Activity
          - **Recent Commits**: [commit_summary] with [change_analysis]
          - **Active Branches**: [branch_list] with [development_purposes]
          - **Patterns**: [workflow_patterns] with [team_practices]
          
          ### 🔧 Current State
          - **Working Directory**: [uncommitted_changes] with [development_context]
          - **Build Status**: [build_state] with [test_results]
          - **Environment**: [development_environment] with [configuration_status]
          
          ### 🧠 Key Decisions
          - [Decision 1]: [rationale] with [impact_analysis]
          - [Decision 2]: [rationale] with [impact_analysis]
          
          ### 🎯 Development Focus
          - **Immediate**: [high_priority_tasks] with [success_criteria]
          - **Short-term**: [medium_priority_tasks] with [completion_targets]
          - **Long-term**: [strategic_objectives] with [milestone_planning]
          
          ### 🔍 Supporting Details
          [Expandable details available on request]
        </format>
        <timing>Delivered within 3 seconds for comprehensive context</timing>
      </detailed_context>
    </structured_summary>
    
    <interactive_exploration>
      <capability>Ask specific questions about any aspect of the project context</capability>
      <navigation>Drill down into specific files, decisions, or technical details</navigation>
      <clarification>Request elaboration on any context summary point</clarification>
      <customization>Customize context focus and detail levels</customization>
    </interactive_exploration>
    
    <progressive_disclosure>
      <level_1>Essential project overview for immediate development start</level_1>
      <level_2>Detailed context with architectural and workflow understanding</level_2>
      <level_3>Comprehensive context with full decision history and alternatives</level_3>
      <level_4>Expert-level context with deep technical analysis and optimization opportunities</level_4>
    </progressive_disclosure>
  </context_delivery_formats>
  
  <integration_points>
    <depends_on>
      context/restore-session.md for context restoration integration
      patterns/intelligent-routing.md for routing enhancement
      patterns/context-preservation.md for state management
      development/research-analysis.md for project analysis
      quality/tdd.md for TDD methodology integration
      patterns/session-management.md for session integration
    </depends_on>
    <provides_to>
      commands/context-prime.md for intelligent context priming
      commands/auto.md for enhanced routing with context awareness
      commands/session.md for improved session management
      commands/task.md for project-aware task execution
      commands/feature.md for context-aware feature development
      commands/swarm.md for project-aware multi-agent coordination
    </provides_to>
  </integration_points>
  
  <usage_examples>
    <basic_priming>
      <trigger>Project context establishment for new development session</trigger>
      <response>
        🏗️ **Project Structure**: React/Node.js monorepo with microservices architecture
        📈 **Recent Activity**: 15 commits this week focused on authentication system
        🔧 **Active Work**: feature/auth-system branch 75% complete
        📋 **Patterns**: TDD with Jest, CI/CD with GitHub Actions
        🎯 **Next Steps**: Complete JWT implementation, add refresh tokens
      </response>
    </basic_priming>
    
    <architecture_focus>
      <trigger>Context priming with architectural focus</trigger>
      <response>
        **Architecture**: Clean Architecture with DDD patterns
        **Layers**: API Gateway → Services → Domain → Infrastructure
        **Patterns**: CQRS for commands, Repository for data access
        **Decisions**: Chose PostgreSQL over MongoDB for ACID compliance
        **Next**: Implement event sourcing for audit trails
      </response>
    </architecture_focus>
    
    <workflow_integration>
      <trigger>Context priming for workflow optimization</trigger>
      <response>
        **Methodology**: TDD with 95% coverage requirement
        **Quality**: ESLint + Prettier, pre-commit hooks, automated testing
        **Deployment**: Docker containers with Kubernetes orchestration
        **Monitoring**: Prometheus metrics, ELK stack for logging
        **Optimization**: Identified 3 performance bottlenecks for resolution
      </response>
    </workflow_integration>
  </usage_examples>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">intelligent_analysis</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">performance_optimization</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">security_controls</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">workflow_integration</uses_pattern>
    <implementation_notes>
      Project analysis follows intelligent_analysis pattern for comprehensive understanding
      Performance optimization uses caching and parallel execution for <3s loading
      Security controls implement timeout mechanisms and approval workflows
      Workflow integration ensures compatibility with existing development commands
    </implementation_notes>
  </pattern_usage>
  
</module>
```