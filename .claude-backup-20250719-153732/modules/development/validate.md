| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# /validate - Framework adaptation validation and verification

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Comprehensive framework adaptation validation with quality assurance and performance verification">
  
  <delegation target="modules/getting-started/adaptation-validation.md">
    Analyze configuration → Test functionality → Validate quality gates → Verify performance → Generate validation report
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Configuration analysis and validation strategy</uses_pattern>
    <uses_pattern from="patterns/validation-pattern.md">Comprehensive validation orchestration</uses_pattern>
    <uses_pattern from="patterns/quality-assurance-pattern.md">Quality gate validation and verification</uses_pattern>
    <uses_pattern from="patterns/performance-testing-pattern.md">Performance validation and benchmarking</uses_pattern>
    <uses_pattern from="patterns/error-detection-pattern.md">Issue identification and resolution</uses_pattern>
    <uses_pattern from="patterns/reporting-pattern.md">Validation reporting and documentation</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Analyze framework configuration and adaptation status</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What configuration analysis approach ensures comprehensive validation?
          - What adaptation elements need validation for framework effectiveness?
          - How can analysis identify potential issues and optimization opportunities?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Configuration Question: What framework configuration elements need validation?]
          - [Adaptation Question: What domain-specific adaptations need verification?]
          - [Integration Question: What integration points need testing for compatibility?]
          - [Quality Question: What quality gates need validation for proper function?]
          - [Performance Question: What performance metrics need baseline establishment?]
          - [Security Question: What security configurations need validation?]
          - [Completeness Question: What adaptation completeness indicators need verification?]
          - [Consistency Question: What consistency checks ensure framework integrity?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this configuration analysis optimal for validation planning?
          - What evidence supports the validation scope and approach?
          - How will this analysis ensure comprehensive validation coverage?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can configuration analysis be done with parallel component inspection?</tool_optimization>
        <context_efficiency>How can analysis optimize token usage for validation planning?</context_efficiency>
        <dependency_analysis>What configuration analysis can be done simultaneously vs sequentially?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>CONFIGURATION_ANALYSIS: 
        - Framework Status: [adaptation_status] with [completion_percentage]
        - Domain Configuration: [domain_specific_config] with [alignment_score]
        - Integration Status: [integration_components] with [compatibility_assessment]
        - Quality Gates: [quality_configuration] with [validation_requirements]
        - Performance Baseline: [performance_metrics] with [target_alignment]
        - Security Status: [security_configuration] with [compliance_level]</output_format>
      <validation>Configuration analyzed comprehensively with validation requirements identified</validation>
      <enforcement>BLOCK if configuration analysis insufficient for validation planning</enforcement>
      <context_transfer>Configuration status and validation requirements for functionality testing</context_transfer>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="extended">
      <action>Test framework functionality and component integration</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What functionality testing approach ensures comprehensive validation?
          - What integration testing is needed for component compatibility?
          - How can testing identify issues before they affect productivity?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Functionality Question: What core framework functions need testing?]
          - [Command Question: What command functionality needs verification?]
          - [Module Question: What module integration needs testing?]
          - [Domain Question: What domain-specific functionality needs validation?]
          - [Integration Question: What external tool integration needs testing?]
          - [Error Question: What error handling and recovery needs testing?]
          - [Performance Question: What performance characteristics need measurement?]
          - [Usability Question: What user experience aspects need validation?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this functionality testing optimal for validation effectiveness?
          - What evidence supports the testing scope and methodology?
          - How will this testing ensure framework reliability and usability?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can functionality testing be done with parallel test execution?</tool_optimization>
        <context_efficiency>How can testing optimize context window usage?</context_efficiency>
        <dependency_analysis>What functionality tests can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>FUNCTIONALITY_TESTING: 
        - Core Functions: [function_tests] with [success_rate]
        - Command Tests: [command_validation] with [functionality_score]
        - Module Integration: [module_tests] with [integration_success]
        - Domain Functionality: [domain_tests] with [specialization_score]
        - External Integration: [integration_tests] with [compatibility_score]
        - Error Handling: [error_tests] with [recovery_effectiveness]</output_format>
      <validation>Functionality tested comprehensively with integration verification</validation>
      <enforcement>BLOCK if critical functionality tests fail or integration issues detected</enforcement>
      <context_transfer>Functionality test results and integration status for quality validation</context_transfer>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Validate quality gates and standards compliance</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What quality gate validation ensures standards compliance?
          - What quality standards need verification for domain requirements?
          - How can validation ensure consistent quality enforcement?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Quality Question: What quality gates are properly configured and functional?]
          - [Standards Question: What quality standards are enforced for domain requirements?]
          - [Compliance Question: What compliance requirements are met by quality configuration?]
          - [Enforcement Question: What quality enforcement mechanisms are working correctly?]
          - [Coverage Question: What quality coverage is achieved by configured gates?]
          - [Consistency Question: What quality consistency is maintained across components?]
          - [Reporting Question: What quality reporting is available for monitoring?]
          - [Improvement Question: What quality improvement opportunities are identified?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this quality validation optimal for standards compliance?
          - What evidence supports the quality gate effectiveness?
          - How will this validation ensure consistent quality enforcement?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can quality validation be done with parallel gate testing?</tool_optimization>
        <context_efficiency>How can validation optimize context window usage?</context_efficiency>
        <dependency_analysis>What quality validation can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>QUALITY_VALIDATION: 
        - Quality Gates: [gate_tests] with [enforcement_effectiveness]
        - Standards Compliance: [standards_validation] with [compliance_score]
        - Domain Standards: [domain_quality] with [specialization_compliance]
        - Enforcement Status: [enforcement_mechanisms] with [consistency_score]
        - Coverage Assessment: [quality_coverage] with [completeness_level]
        - Improvement Opportunities: [quality_enhancements] with [priority_ranking]</output_format>
      <validation>Quality gates validated with standards compliance verification</validation>
      <enforcement>VERIFY quality gates meet domain requirements and enforcement standards</enforcement>
      <context_transfer>Quality validation results and compliance status for performance verification</context_transfer>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Verify performance benchmarks and optimization</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What performance verification ensures framework efficiency?
          - What benchmarks need validation for domain requirements?
          - How can verification identify performance optimization opportunities?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Performance Question: What performance metrics meet established benchmarks?]
          - [Efficiency Question: What efficiency gains are achieved through framework adaptation?]
          - [Response Question: What response times are acceptable for domain workflows?]
          - [Resource Question: What resource utilization is optimal for framework operations?]
          - [Scalability Question: What scalability characteristics support domain growth?]
          - [Optimization Question: What optimization opportunities can enhance performance?]
          - [Monitoring Question: What performance monitoring is available for ongoing tracking?]
          - [Baseline Question: What performance baseline is established for future comparison?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this performance verification optimal for framework efficiency?
          - What evidence supports the performance benchmark achievement?
          - How will this verification ensure optimal framework performance?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can performance verification be done with parallel benchmark testing?</tool_optimization>
        <context_efficiency>How can verification optimize context window usage?</context_efficiency>
        <dependency_analysis>What performance tests can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>PERFORMANCE_VERIFICATION: 
        - Benchmark Results: [performance_metrics] with [target_achievement]
        - Efficiency Gains: [efficiency_improvements] with [optimization_success]
        - Response Times: [response_measurements] with [acceptability_score]
        - Resource Utilization: [resource_metrics] with [efficiency_rating]
        - Scalability Assessment: [scalability_tests] with [growth_readiness]
        - Optimization Opportunities: [performance_enhancements] with [impact_potential]</output_format>
      <validation>Performance verified with benchmark achievement and optimization identification</validation>
      <enforcement>BLOCK if performance benchmarks not met or critical optimization needs identified</enforcement>
      <context_transfer>Performance verification results and optimization recommendations for reporting</context_transfer>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Generate comprehensive validation report and recommendations</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What validation reporting provides comprehensive assessment overview?
          - What recommendations optimize framework effectiveness and usage?
          - How can reporting support continuous improvement and monitoring?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Reporting Question: What validation report provides comprehensive assessment?]
          - [Summary Question: What executive summary captures key validation findings?]
          - [Details Question: What detailed findings support validation conclusions?]
          - [Recommendations Question: What actionable recommendations improve framework effectiveness?]
          - [Monitoring Question: What ongoing monitoring recommendations ensure continued validation?]
          - [Improvement Question: What improvement opportunities enhance framework value?]
          - [Documentation Question: What documentation supports validation findings?]
          - [Follow-up Question: What follow-up actions ensure validation effectiveness?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this validation reporting optimal for comprehensive assessment?
          - What evidence supports the validation conclusions and recommendations?
          - How will this reporting support framework effectiveness and improvement?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can validation reporting be done with parallel report generation?</tool_optimization>
        <context_efficiency>How can reporting optimize context window usage?</context_efficiency>
        <dependency_analysis>What reporting components can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>VALIDATION_REPORT: 
        - Executive Summary: [validation_overview] with [key_findings]
        - Configuration Status: [config_assessment] with [completeness_score]
        - Functionality Results: [function_validation] with [success_metrics]
        - Quality Assessment: [quality_validation] with [compliance_rating]
        - Performance Analysis: [performance_results] with [benchmark_achievement]
        - Recommendations: [improvement_actions] with [priority_ranking]</output_format>
      <validation>Validation report generated with comprehensive assessment and actionable recommendations</validation>
      <enforcement>VERIFY validation report is complete and provides actionable guidance</enforcement>
      <context_transfer>Complete validation report and recommendations for framework optimization</context_transfer>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Complete validation with status confirmation and next steps</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What validation completion ensures framework readiness and effectiveness?
          - What status confirmation provides clear validation outcomes?
          - How can completion guide next steps for framework utilization?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Completion Question: Are all validation steps successfully completed?]
          - [Status Question: What validation status indicates framework readiness?]
          - [Readiness Question: Is the framework ready for productive use?]
          - [Issues Question: What outstanding issues need resolution before use?]
          - [Optimization Question: What optimization opportunities should be prioritized?]
          - [Monitoring Question: What ongoing monitoring ensures continued validation?]
          - [Support Question: What support resources are available for framework use?]
          - [Next Steps Question: What immediate next steps optimize framework value?]
        </critical_thinking>
        <decision_reasoning>
          - Why does this validation completion ensure framework readiness?
          - What evidence supports the validation status and recommendations?
          - How will this completion guide effective framework utilization?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can validation completion be done with parallel status verification?</tool_optimization>
        <context_efficiency>How can completion optimize context window usage?</context_efficiency>
        <dependency_analysis>What completion steps can be parallelized?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>VALIDATION_COMPLETE: 
        - Status: [validation_status] with [readiness_level]
        - Framework Ready: [framework_readiness] with [usage_preparation]
        - Outstanding Issues: [remaining_issues] with [resolution_priority]
        - Optimization Priorities: [optimization_ranking] with [implementation_guidance]
        - Monitoring Setup: [monitoring_configuration] with [tracking_readiness]
        - Next Steps: [immediate_actions] with [implementation_timeline]</output_format>
      <validation>Validation completed successfully with framework readiness confirmation</validation>
      <enforcement>CONFIRM all critical validation steps completed and framework ready for use</enforcement>
      <context_transfer>Complete validation confirmation with framework ready for productive use</context_transfer>
    </checkpoint>
  </thinking_pattern>
  
  <validation_framework_integration enforcement="MANDATORY">
    <comprehensive_validation>Configuration, functionality, quality, performance, and usability validation</comprehensive_validation>
    <domain_specific_validation>Domain-appropriate validation criteria and benchmarks</domain_specific_validation>
    <integration_validation>External tool and service integration verification</integration_validation>
    <quality_gate_validation>Quality standard enforcement and compliance verification</quality_gate_validation>
    <performance_benchmarking>Performance target achievement and optimization identification</performance_benchmarking>
    <validation>Reference quality/validation-framework.md for comprehensive validation methodology</validation>
  </validation_framework_integration>
  
  <claude_4_module_execution enforcement="MANDATORY" thinking_mode="interleaved">
    <core_stack order="advanced_sequential" optimization="context_hierarchical">
      <module thinking="enabled" cache="predictive">quality/critical-thinking.md - Enhanced validation analysis and strategy</module>
      <module thinking="enabled" cache="predictive">getting-started/adaptation-validation.md - Comprehensive validation orchestration</module>
      <module thinking="enabled" cache="predictive">quality/universal-quality-gates.md - Quality gate validation and verification</module>
      <module thinking="enabled" cache="predictive">patterns/validation-pattern.md - Validation methodology and best practices</module>
      <module thinking="enabled" cache="predictive">quality/performance-validation.md - Performance benchmarking and optimization</module>
    </core_stack>
    <contextual_modules evaluation="intelligent_conditional" analysis="claude_4_enhanced">
      <conditional module="domains/mobile-validation.md" condition="mobile_domain_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="domains/data-analytics-validation.md" condition="data_analytics_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="domains/fintech-validation.md" condition="fintech_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="domains/devops-validation.md" condition="devops_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="domains/data-engineering-validation.md" condition="data_engineering_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="domains/enterprise-validation.md" condition="enterprise_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="domains/web-development-validation.md" condition="web_development_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="domains/ml-validation.md" condition="ml_validation" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="quality/security-validation.md" condition="security_validation_needed" thinking="adaptive" fallback="quality/general-validation.md"/>
      <conditional module="quality/compliance-validation.md" condition="compliance_validation_needed" thinking="adaptive" fallback="quality/general-validation.md"/>
    </contextual_modules>
    <support_modules order="optimized_parallel" batching="mandatory" speedup="70_percent">
      <module batch_group="testing" tools="validation_tools">quality/comprehensive-testing.md - Parallel functionality testing</module>
      <module batch_group="analysis" tools="Read,Grep,Glob">patterns/configuration-analysis.md - Parallel configuration analysis</module>
      <module batch_group="reporting" tools="Write,MultiEdit">patterns/validation-reporting.md - Parallel validation reporting</module>
    </support_modules>
    <performance_monitoring>
      <metric name="validation_time" target="under_5_minutes"/>
      <metric name="validation_accuracy" target="100_percent_issue_detection"/>
      <metric name="validation_completeness" target="100_percent_coverage"/>
      <metric name="recommendation_quality" target="95_percent_actionable"/>
    </performance_monitoring>
  </claude_4_module_execution>
  
  <depends_on>
    getting-started/adaptation-validation.md for validation orchestration
    quality/universal-quality-gates.md for quality gate validation
    patterns/validation-pattern.md for validation methodology
    quality/performance-validation.md for performance benchmarking
    patterns/configuration-analysis.md for configuration assessment
    quality/comprehensive-testing.md for functionality testing
    patterns/validation-reporting.md for validation reporting
    domains/domain-specific-validation.md for domain-specific validation
    quality/security-validation.md for security validation
    quality/compliance-validation.md for compliance validation
  </depends_on>
  
  <examples>
    /validate                                 → Comprehensive framework validation
    /validate --configuration                 → Configuration validation only
    /validate --functionality                 → Functionality testing only
    /validate --quality-gates                 → Quality gate validation only
    /validate --performance                   → Performance benchmarking only
    /validate --domain=mobile                 → Mobile domain validation
    /validate --domain=data-analytics         → Data analytics validation
    /validate --security                      → Security validation focus
    /validate --compliance                    → Compliance validation focus
    /validate --quick                         → Quick validation summary
    /validate --comprehensive                 → Full comprehensive validation
    /validate --report-only                   → Generate validation report only
    /validate --fix-issues                    → Validate and fix identified issues
  </examples>
  
  <rules>
    <rule>ALWAYS validate configuration before functionality testing</rule>
    <rule>ALWAYS test quality gates for proper enforcement</rule>
    <rule>ALWAYS verify performance benchmarks for domain requirements</rule>
    <rule>ALWAYS generate comprehensive validation report</rule>
    <rule>NEVER skip critical validation steps or quality verification</rule>
    <rule>ALWAYS provide actionable recommendations for improvement</rule>
  </rules>
  
  <pattern_usage>
    • Uses configuration_analysis pattern for comprehensive configuration assessment
    • Implements functionality_testing pattern for component validation
    • Applies quality_validation pattern for standards compliance verification
    • Leverages performance_benchmarking pattern for optimization identification
    • Uses validation_reporting pattern for comprehensive assessment documentation
    • Integrates error_detection pattern for issue identification and resolution
    • Applies domain_validation pattern for domain-specific validation criteria
    • Uses continuous_monitoring pattern for ongoing validation support
    
    See modules/getting-started/adaptation-validation.md for validation orchestration
    See system/quality/universal-quality-gates.md for quality gate validation
    See modules/patterns/validation-pattern.md for validation methodology
  </pattern_usage>
  
  <prompt_construction>
    <assembly_preview>
      VALIDATION WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. Configuration│ → Analyze framework configuration and adaptation
      │   Analysis      │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. Functionality│ → Test framework functionality and integration
      │   Testing       │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. Quality      │ → Validate quality gates and standards
      │   Validation    │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. Performance  │ → Verify performance benchmarks
      │   Verification  │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. Validation   │ → Generate comprehensive validation report
      │   Reporting     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 6. Completion   │ → Complete validation with recommendations
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~16,000
      - Configuration analysis: 2,500
      - Functionality testing: 3,500
      - Quality validation: 3,000
      - Performance verification: 2,500
      - Validation reporting: 2,500
      - Completion confirmation: 2,000
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /validate --comprehensive
      [00:30] 🔍 CONFIG: Framework 98% configured, domain alignment excellent
      [01:15] 🧪 TESTING: All core functions passing, 2 integration warnings
      [02:00] ✅ QUALITY: Quality gates active, 95% compliance achieved
      [02:45] ⚡ PERFORMANCE: Performance targets met, 3 optimization opportunities
      [03:30] 📊 REPORT: Validation report generated with 5 recommendations
      [04:00] 🎉 COMPLETE: Framework validated and ready for productive use
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Executes comprehensive configuration analysis with parallel inspection
      2. Tests framework functionality with concurrent validation operations
      3. Validates quality gates through systematic compliance verification
      4. Verifies performance benchmarks with optimization identification
      5. Generates detailed validation report with actionable recommendations
      6. Completes validation with readiness confirmation and next steps
    </parsing_behavior>

    <decision_points>
      - Configuration validation scope based on adaptation completeness
      - Functionality testing depth based on domain requirements
      - Quality gate validation based on configured standards
      - Performance benchmarking based on domain performance targets
      - Validation reporting based on comprehensive assessment needs
      - Completion confirmation based on framework readiness criteria
    </decision_points>
  </claude_4_interpretation>

</command>
```