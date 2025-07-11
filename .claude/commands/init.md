| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# /init - Project initialization and domain detection

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Project initialization with intelligent domain detection and framework customization">
  
  <delegation target="modules/getting-started/project-initialization.md">
    Analyze project structure → Detect domain and tech stack → Configure framework → Validate setup → Generate documentation
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Project analysis and domain detection</uses_pattern>
    <uses_pattern from="patterns/research-analysis-pattern.md">Codebase investigation and understanding</uses_pattern>
    <uses_pattern from="patterns/setup-orchestration-pattern.md">Framework configuration and validation</uses_pattern>
    <uses_pattern from="patterns/error-recovery-pattern.md">Setup failure handling and rollback</uses_pattern>
    <uses_pattern from="patterns/context-management-pattern.md">Initial context establishment</uses_pattern>
    <uses_pattern from="patterns/user-guidance-pattern.md">Interactive setup guidance</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Analyze project structure and detect technology stack</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What project structure patterns indicate domain and tech stack?
          - What files and directories are most informative for domain detection?
          - How can I efficiently analyze the project without overwhelming the user?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Structure Question: What directory structure suggests the project type (web, mobile, data, etc.)?]
          - [Files Question: What key files indicate programming language and framework choices?]
          - [Dependencies Question: What package managers and dependency files reveal technology stack?]
          - [Patterns Question: What architectural patterns are evident from the codebase structure?]
          - [Scale Question: What indicators suggest project size and complexity?]
          - [Team Question: What artifacts suggest team size and development methodology?]
          - [Domain Question: What domain-specific patterns or terminology are present?]
          - [Integration Question: What existing tools and services are already integrated?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this analysis approach optimal for domain detection?
          - What evidence supports the technology stack identification?
          - How will this analysis inform framework customization?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can project analysis be done with parallel file system operations?</tool_optimization>
        <context_efficiency>How can analysis optimize token usage while being comprehensive?</context_efficiency>
        <dependency_analysis>What project analysis can be done simultaneously vs sequentially?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>PROJECT_ANALYSIS: 
        - Tech Stack: [languages] with [frameworks] and [tools]
        - Structure: [project_type] with [architecture_pattern]
        - Domain: [domain_category] with [subdomain_indicators]
        - Scale: [size_indicator] with [complexity_level]
        - Team: [methodology_indicators] with [collaboration_patterns]
        - Integration: [existing_tools] with [service_dependencies]</output_format>
      <validation>Project analyzed across all relevant dimensions for domain detection</validation>
      <enforcement>BLOCK if insufficient project analysis for domain classification</enforcement>
      <context_transfer>Project characteristics for domain detection and framework selection</context_transfer>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="extended">
      <action>Classify domain and recommend framework configuration</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What domain classification criteria apply to this project?
          - How do the project characteristics map to available domain templates?
          - What customization requirements are suggested by the analysis?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Domain Question: Which primary domain best fits the project characteristics?]
          - [Subdomain Question: What subdomain specializations are relevant?]
          - [Framework Question: Which frameworks are most appropriate for this domain?]
          - [Quality Question: What quality gates should be configured for this domain?]
          - [Workflow Question: What development workflows are optimal for this project?]
          - [Integration Question: How should the framework integrate with existing tools?]
          - [Team Question: What team collaboration features are needed?]
          - [Evolution Question: How should the framework evolve with the project?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this domain classification optimal for the project?
          - What evidence supports the recommended framework configuration?
          - How will this configuration align with project needs and team workflows?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can domain classification be done with parallel template evaluation?</tool_optimization>
        <context_efficiency>How can classification optimize context window usage?</context_efficiency>
        <dependency_analysis>What classification steps can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>DOMAIN_CLASSIFICATION: 
        Primary=[domain] Secondary=[subdomain] Confidence=[percentage]
        Recommended=[framework_config] Quality=[quality_gates] Workflow=[development_patterns]</output_format>
      <validation>Domain classified with high confidence and appropriate framework recommendations</validation>
      <enforcement>BLOCK if domain classification lacks sufficient confidence or justification</enforcement>
      <context_transfer>Domain classification and framework recommendations for configuration</context_transfer>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="standard">
      <action>Configure framework for domain-specific requirements</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What configuration steps are required for the identified domain?
          - What templates and modules need to be customized?
          - What validation is needed to ensure proper configuration?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Configuration Question: What specific configuration changes are needed for this domain?]
          - [Template Question: Which domain templates should be applied?]
          - [Module Question: What modules need to be enabled or configured?]
          - [Quality Question: What quality gates need domain-specific configuration?]
          - [Command Question: What command customizations are appropriate?]
          - [Integration Question: How should existing tools be integrated?]
          - [Validation Question: What validation ensures configuration success?]
          - [Documentation Question: What documentation needs to be generated?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this configuration approach optimal for the domain?
          - What evidence supports the specific configuration choices?
          - How will this configuration enhance development workflow?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can configuration steps be batched for performance improvement?</tool_optimization>
        <context_efficiency>How can configuration optimize token usage?</context_efficiency>
        <dependency_analysis>What configuration steps can be done in parallel?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>CONFIGURATION_STATUS: 
        - Domain Templates: [applied_templates]
        - Modules: [configured_modules]
        - Quality Gates: [quality_configuration]
        - Commands: [command_customizations]
        - Integration: [tool_integrations]</output_format>
      <validation>Framework configured for domain-specific requirements with validation</validation>
      <enforcement>VERIFY configuration matches domain requirements and project needs</enforcement>
      <context_transfer>Configuration status and validation results for setup completion</context_transfer>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Validate framework integration and functionality</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What validation tests are needed to ensure proper framework integration?
          - What functionality should be tested before completing initialization?
          - How can validation catch potential issues early?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Integration Question: Are all framework components properly integrated?]
          - [Functionality Question: Do all configured features work as expected?]
          - [Performance Question: Does the framework perform within acceptable limits?]
          - [Compatibility Question: Are there any compatibility issues with existing tools?]
          - [Security Question: Are there any security considerations or vulnerabilities?]
          - [Usability Question: Is the framework setup user-friendly for the team?]
          - [Completeness Question: Are all required setup steps completed?]
          - [Documentation Question: Is sufficient documentation generated for the team?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this validation approach comprehensive for framework integration?
          - What evidence supports successful framework setup?
          - How will this validation prevent future issues?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can validation tests be run in parallel for faster completion?</tool_optimization>
        <context_efficiency>How can validation optimize context window usage?</context_efficiency>
        <dependency_analysis>What validation steps can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>VALIDATION_RESULTS: 
        - Integration: [status] with [issues_found]
        - Functionality: [test_results] with [success_rate]
        - Performance: [metrics] within [acceptable_limits]
        - Compatibility: [compatibility_check] with [conflicts_resolved]
        - Security: [security_assessment] with [recommendations]</output_format>
      <validation>Framework integration validated with comprehensive testing and issue resolution</validation>
      <enforcement>BLOCK completion if critical validation failures are not resolved</enforcement>
      <context_transfer>Validation results and resolved issues for setup completion</context_transfer>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Generate setup documentation and next steps</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What documentation is needed for successful team onboarding?
          - What next steps should be recommended for optimal framework usage?
          - How can documentation ensure long-term success with the framework?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Documentation Question: What essential documentation should be generated?]
          - [Onboarding Question: What information does the team need to get started?]
          - [Usage Question: What are the most important commands and workflows to highlight?]
          - [Customization Question: What customization options should be documented?]
          - [Troubleshooting Question: What common issues and solutions should be included?]
          - [Evolution Question: How should the framework evolve with the project?]
          - [Support Question: What support resources are available?]
          - [Feedback Question: How can the team provide feedback for framework improvement?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this documentation approach optimal for team success?
          - What evidence supports the recommended next steps?
          - How will this documentation ensure continued framework value?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can documentation generation be done with parallel content creation?</tool_optimization>
        <context_efficiency>How can documentation optimize token usage while being comprehensive?</context_efficiency>
        <dependency_analysis>What documentation can be generated in parallel?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>DOCUMENTATION_GENERATED: 
        - Setup Guide: [project_specific_guide]
        - Command Reference: [domain_customized_commands]
        - Quality Gates: [configured_quality_standards]
        - Troubleshooting: [common_issues_and_solutions]
        - Next Steps: [recommended_workflow_actions]</output_format>
      <validation>Documentation generated with comprehensive coverage and actionable guidance</validation>
      <enforcement>VERIFY documentation is complete and accessible to the team</enforcement>
      <context_transfer>Complete setup documentation and next step recommendations</context_transfer>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Complete initialization with success confirmation</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What final checks ensure successful initialization completion?
          - What confirmation should be provided to the user?
          - How can success be measured and tracked?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Completion Question: Are all initialization steps successfully completed?]
          - [Success Question: What metrics indicate successful framework setup?]
          - [Readiness Question: Is the framework ready for productive use?]
          - [Team Question: Is the team prepared to use the framework effectively?]
          - [Performance Question: Are performance benchmarks met?]
          - [Quality Question: Are quality standards properly configured?]
          - [Support Question: Are support resources properly configured?]
          - [Future Question: Is the framework set up for future growth and adaptation?]
        </critical_thinking>
        <decision_reasoning>
          - Why does this completion approach ensure initialization success?
          - What evidence supports framework readiness for productive use?
          - How will this completion set the stage for effective framework utilization?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can final checks be done with parallel validation operations?</tool_optimization>
        <context_efficiency>How can completion optimize context window usage?</context_efficiency>
        <dependency_analysis>What completion steps can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>INITIALIZATION_COMPLETE: 
        - Status: [success_status] with [completion_percentage]
        - Framework: [configured_for_domain] with [quality_gates_active]
        - Team: [onboarding_ready] with [documentation_available]
        - Next: [recommended_first_commands]</output_format>
      <validation>Initialization completed successfully with framework ready for productive use</validation>
      <enforcement>CONFIRM all critical initialization steps are completed successfully</enforcement>
      <context_transfer>Complete initialization confirmation with framework ready for use</context_transfer>
    </checkpoint>
  </thinking_pattern>
  
  <claude_4_module_execution enforcement="MANDATORY" thinking_mode="interleaved">
    <core_stack order="advanced_sequential" optimization="context_hierarchical">
      <module thinking="enabled" cache="predictive">quality/critical-thinking.md - Enhanced project analysis before initialization</module>
      <module thinking="enabled" cache="predictive">getting-started/project-initialization.md - Domain detection and framework configuration</module>
      <module thinking="enabled" cache="predictive">getting-started/domain-classification.md - Intelligent domain classification system</module>
      <module thinking="enabled" cache="predictive">getting-started/framework-configurator.md - Domain-specific framework customization</module>
      <module thinking="enabled" cache="predictive">quality/universal-quality-gates.md - Quality gate configuration for domain</module>
    </core_stack>
    <contextual_modules evaluation="intelligent_conditional" analysis="claude_4_enhanced">
      <conditional module="domains/mobile-development.md" condition="mobile_project_detected" thinking="adaptive" fallback="domains/web-development.md"/>
      <conditional module="domains/data-analytics.md" condition="data_project_detected" thinking="adaptive" fallback="domains/data-engineering.md"/>
      <conditional module="domains/financial-technology.md" condition="fintech_project_detected" thinking="adaptive" fallback="domains/enterprise-tools.md"/>
      <conditional module="domains/devops-platform.md" condition="infrastructure_project_detected" thinking="adaptive" fallback="domains/enterprise-tools.md"/>
      <conditional module="domains/data-engineering.md" condition="data_pipeline_detected" thinking="adaptive" fallback="domains/data-analytics.md"/>
      <conditional module="domains/enterprise-tools.md" condition="enterprise_project_detected" thinking="adaptive" fallback="domains/web-development.md"/>
      <conditional module="domains/web-development.md" condition="web_project_detected" thinking="adaptive" fallback="domains/enterprise-tools.md"/>
      <conditional module="domains/machine-learning.md" condition="ml_project_detected" thinking="adaptive" fallback="domains/data-analytics.md"/>
      <conditional module="getting-started/migration-helper.md" condition="existing_framework_detected" thinking="adaptive" fallback="getting-started/fresh-setup.md"/>
      <conditional module="getting-started/team-setup.md" condition="team_project_detected" thinking="adaptive" fallback="getting-started/individual-setup.md"/>
    </contextual_modules>
    <support_modules order="optimized_parallel" batching="mandatory" speedup="70_percent">
      <module batch_group="analysis" tools="Read,Glob,LS">patterns/codebase-analysis.md - Parallel project structure analysis</module>
      <module batch_group="validation" tools="quality_gates">quality/setup-validation.md - Concurrent setup validation</module>
      <module batch_group="documentation" tools="Write,MultiEdit">development/documentation.md - Parallel documentation generation</module>
    </support_modules>
    <performance_monitoring>
      <metric name="initialization_time" target="under_5_minutes"/>
      <metric name="detection_accuracy" target="95_percent_domain_classification"/>
      <metric name="configuration_success" target="100_percent_functional_framework"/>
      <metric name="user_satisfaction" target="90_percent_positive_feedback"/>
    </performance_monitoring>
  </claude_4_module_execution>
  
  <depends_on>
    getting-started/project-initialization.md for initialization orchestration
    getting-started/domain-classification.md for intelligent domain detection
    getting-started/framework-configurator.md for domain-specific configuration
    domains/*.md for domain-specific templates and configuration
    quality/universal-quality-gates.md for quality gate configuration
    patterns/codebase-analysis.md for project structure analysis
    patterns/setup-orchestration-pattern.md for setup workflow coordination
    development/documentation.md for setup documentation generation
    quality/setup-validation.md for initialization validation
    patterns/error-recovery-pattern.md for setup failure handling
  </depends_on>
  
  <examples>
    /init                           → Full initialization with domain detection
    /init --domain=mobile          → Initialize with mobile development domain
    /init --analyze-only           → Analyze project without configuration
    /init --validate               → Validate existing framework configuration
    /init --team-setup             → Initialize for team collaboration
    /init --migrate                → Migrate from existing framework
    /init --domain=data-analytics  → Initialize for data analytics domain
    /init --quick                  → Quick initialization with defaults
    /init --custom                 → Custom initialization with advanced options
  </examples>
  
  <rules>
    <rule>ALWAYS analyze project structure before domain classification</rule>
    <rule>ALWAYS validate framework configuration before completion</rule>
    <rule>ALWAYS generate team-ready documentation</rule>
    <rule>NEVER skip domain detection or framework customization</rule>
    <rule>ALWAYS provide rollback options for configuration changes</rule>
    <rule>ALWAYS confirm successful initialization before completion</rule>
  </rules>
  
  <pattern_usage>
    • Uses project_analysis pattern for codebase understanding
    • Implements domain_classification pattern for intelligent categorization
    • Applies setup_orchestration pattern for configuration management
    • Leverages validation_gates pattern for initialization verification
    • Uses documentation_generation pattern for team onboarding
    • Integrates error_recovery pattern for setup failure handling
    • Applies user_guidance pattern for interactive setup experience
    • Uses performance_monitoring pattern for initialization tracking
    
    See modules/getting-started/project-initialization.md for initialization details
    See modules/getting-started/domain-classification.md for domain detection
    See modules/patterns/setup-orchestration-pattern.md for setup coordination
  </pattern_usage>
  
  <prompt_construction>
    <assembly_preview>
      INITIALIZATION WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. Project     │ → Analyze structure, detect tech stack and patterns
      │   Analysis     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. Domain      │ → Classify domain and recommend configuration
      │   Detection    │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. Framework   │ → Configure framework for domain-specific needs
      │   Configuration│
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. Validation  │ → Validate integration and functionality
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. Documentation│ → Generate setup docs and next steps
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 6. Completion  │ → Confirm success and provide guidance
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~15,000
      - Project analysis: 3,000
      - Domain detection: 2,500
      - Framework configuration: 3,500
      - Validation testing: 2,000
      - Documentation generation: 2,500
      - Completion confirmation: 1,500
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /init
      [00:30] 🔍 ANALYSIS: Python web app detected (Flask, SQLAlchemy, React frontend)
      [01:00] 🎯 DOMAIN: Web Development (85% confidence) with data analytics components
      [01:30] ⚙️ CONFIG: Applied web-dev templates, configured quality gates
      [02:00] ✅ VALIDATION: All components working, performance within limits
      [02:30] 📚 DOCS: Generated team guide and command reference
      [03:00] 🎉 COMPLETE: Framework ready for productive use
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Executes comprehensive project analysis with parallel file operations
      2. Applies domain classification algorithms with confidence scoring
      3. Configures framework components based on domain requirements
      4. Validates configuration through functional testing
      5. Generates comprehensive documentation for team onboarding
      6. Confirms successful initialization with performance metrics
    </parsing_behavior>

    <decision_points>
      - Domain classification based on project analysis evidence
      - Framework configuration choices based on domain best practices
      - Validation thresholds for successful initialization
      - Documentation generation based on team needs
      - Success confirmation based on functional testing results
    </decision_points>
  </claude_4_interpretation>

</command>
```