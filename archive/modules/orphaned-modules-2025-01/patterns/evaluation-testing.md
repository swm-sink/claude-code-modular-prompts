<module name="evaluation_testing" category="patterns">
  
  <purpose>
    Comprehensive testing framework for multi-agent prompt evaluation system, validating all components from parallel agent execution to final report generation.
  </purpose>
  
  <test_scenarios>
    
    <scenario name="basic_evaluation_workflow" complexity="simple">
      <description>Test basic single prompt evaluation with all four agents</description>
      <test_prompt>
        You are a helpful assistant. Please help me write code for a web application. 
        Make it good and efficient. Use best practices. Thank you.
      </test_prompt>
      <expected_outcomes>
        <clarity_score>Expected: 4-6/10 (vague requirements, unclear scope)</clarity_score>
        <efficiency_score>Expected: 3-5/10 (redundant phrases, low information density)</efficiency_score>
        <model_recommendation>Expected: Claude Sonnet (suitable for general requests)</model_recommendation>
        <improvement_generated>Expected: Enhanced version with specific requirements and context</improvement_generated>
      </expected_outcomes>
      <validation_criteria>
        All four evaluator agents complete successfully
        Scores fall within expected ranges with detailed justification
        Enhanced prompt significantly improves clarity and specificity
        Report generation completes without errors
      </validation_criteria>
    </scenario>
    
    <scenario name="high_quality_prompt_evaluation" complexity="simple">
      <description>Test evaluation of already high-quality prompt</description>
      <test_prompt>
        You are a senior Python developer specializing in FastAPI and PostgreSQL. 
        Create a complete user authentication system with the following specifications:
        
        1. JWT token-based authentication using PyJWT library
        2. Password hashing with bcrypt (minimum 12 rounds)
        3. PostgreSQL database with SQLAlchemy ORM
        4. API endpoints: /register, /login, /refresh, /logout, /profile
        5. Role-based access control with 'user' and 'admin' roles
        6. Input validation using Pydantic models
        7. Comprehensive error handling with appropriate HTTP status codes
        8. Unit tests with pytest covering all endpoints
        9. OpenAPI documentation generation
        10. Environment-based configuration for development and production
        
        Follow PEP 8 conventions, include type hints, and add comprehensive docstrings.
        Ensure all security best practices are implemented including rate limiting.
      </test_prompt>
      <expected_outcomes>
        <clarity_score>Expected: 9-10/10 (extremely clear and specific)</clarity_score>
        <efficiency_score>Expected: 8-9/10 (detailed but well-organized)</efficiency_score>
        <model_recommendation>Expected: Claude Opus (complex implementation requirements)</model_recommendation>
        <improvement_generated>Expected: Minor enhancements or confirmation of quality</improvement_generated>
      </expected_outcomes>
      <validation_criteria>
        High scores accurately reflect prompt quality
        Model recommendation matches complexity requirements
        Minimal or no improvements suggested for already excellent prompt
        Evaluation justifications are detailed and accurate
      </validation_criteria>
    </scenario>
    
    <scenario name="ambiguous_prompt_evaluation" complexity="moderate">
      <description>Test evaluation of highly ambiguous and unclear prompt</description>
      <test_prompt>
        Do something with the thing. Make it work better. You know what I mean.
        Fix the issues and improve performance. Make it fast and good.
        Add features that users want. Thanks.
      </test_prompt>
      <expected_outcomes>
        <clarity_score>Expected: 1-2/10 (extremely unclear and ambiguous)</clarity_score>
        <efficiency_score>Expected: 2-3/10 (multiple redundancies and vague terms)</efficiency_score>
        <model_recommendation>Expected: Claude Haiku (simple clarification needed)</model_recommendation>
        <improvement_generated>Expected: Completely restructured prompt with specific requirements</improvement_generated>
      </expected_outcomes>
      <validation_criteria>
        Low scores accurately identify severe clarity issues
        Detailed feedback explains specific ambiguity problems
        Enhanced prompt transforms vague request into actionable instructions
        All evaluator agents identify and address different aspects of problems
      </validation_criteria>
    </scenario>
    
    <scenario name="parallel_agent_coordination" complexity="complex">
      <description>Test multi-agent parallel execution and coordination</description>
      <test_setup>
        Execute evaluation with all four agents simultaneously
        Monitor execution timing and coordination
        Validate no sequential dependencies between agents
        Confirm session creation and progress tracking
      </test_setup>
      <validation_criteria>
        All agents begin execution simultaneously (within 1 second)
        No agent waits for another agent's completion
        Session created automatically for coordination tracking
        All agents complete within expected timeframe (30 seconds)
        Results aggregated successfully without conflicts
      </validation_criteria>
    </scenario>
    
    <scenario name="consensus_mechanism_validation" complexity="complex">
      <description>Test consensus and conflict resolution between evaluator agents</description>
      <test_prompt>
        Create a machine learning model for predicting customer churn using Python.
        Use scikit-learn, pandas, and matplotlib. Include data preprocessing,
        feature engineering, model training, evaluation, and visualization.
        Make sure the code is well-documented and follows best practices.
      </test_prompt>
      <expected_conflicts>
        Efficiency vs Clarity: Detailed requirements vs conciseness
        Model selection: Complexity suitable for different Claude models
        Improvement focus: Multiple valid enhancement directions
      </expected_conflicts>
      <validation_criteria>
        Conflicts identified and documented when scores differ significantly
        Consensus mechanism produces reasonable compromise scores
        Final recommendations incorporate insights from all evaluators
        Conflict resolution rationale clearly documented
      </validation_criteria>
    </scenario>
    
    <scenario name="version_comparison_testing" complexity="complex">
      <description>Test prompt version comparison functionality</description>
      <test_versions>
        <version_1>Help me code something</version_1>
        <version_2>Help me write Python code for a web scraper</version_2>
        <version_3>Create a Python web scraper using BeautifulSoup and requests to extract product data from e-commerce sites</version_3>
        <version_4>Create a Python web scraper using BeautifulSoup and requests library to extract product information (name, price, description, availability) from e-commerce websites. Include error handling, rate limiting, and CSV export functionality. Follow ethical scraping practices with robots.txt compliance.</version_4>
      </test_versions>
      <validation_criteria>
        All versions evaluated in parallel for comparison
        Clear progression of improvement across versions identified
        Comparison matrix accurately reflects relative quality
        Best version recommendation matches highest quality
        Evolution analysis shows improvement patterns
      </validation_criteria>
    </scenario>
    
  </test_scenarios>
  
  <test_execution_workflow>
    
    <phase name="test_preparation" order="1">
      <requirements>
        Test environment configured with evaluation modules
        Sample prompts prepared across quality spectrum
        Expected outcomes defined for validation
        Session tracking enabled for test coordination
      </requirements>
      <actions>
        Load prompt-evaluation.md module and dependencies
        Prepare test prompts with varying quality levels
        Define expected score ranges and outcomes
        Initialize session for test execution tracking
      </actions>
      <validation>
        All evaluation modules properly loaded and functional
        Test prompts cover full quality spectrum
        Expected outcomes clearly defined for comparison
        Session properly configured for test tracking
      </validation>
    </phase>
    
    <phase name="parallel_execution_testing" order="2">
      <requirements>
        All evaluator agents execute simultaneously
        No sequential dependencies between agent tasks
        Session provides real-time coordination tracking
        Performance metrics collected for analysis
      </requirements>
      <actions>
        Execute Task() calls for all evaluator agents in single message
        Monitor execution timing and coordination effectiveness
        Track session updates from all agents in real-time
        Collect performance metrics for execution analysis
      </actions>
      <validation>
        All agents execute in true parallel coordination
        Execution timing meets performance requirements
        Session successfully tracks all agent progress
        Performance metrics within acceptable ranges
      </validation>
    </phase>
    
    <phase name="result_validation" order="3">
      <requirements>
        All evaluator results collected and validated
        Scores match expected ranges for test prompts
        Consensus mechanism functions correctly
        Report generation completes successfully
      </requirements>
      <actions>
        Collect and validate all evaluator agent results
        Compare actual scores against expected ranges
        Verify consensus mechanism handles conflicts appropriately
        Generate complete evaluation reports for review
      </actions>
      <validation>
        All evaluator results successfully collected
        Scores align with expected ranges and justifications
        Consensus mechanism produces reasonable outcomes
        Reports generated completely and accurately
      </validation>
    </phase>
    
  </test_execution_workflow>
  
  <performance_benchmarks>
    <execution_speed>
      <target>Complete evaluation within 30 seconds</target>
      <measurement>Time from initialization to final report</measurement>
      <tolerance>50% variance acceptable for complex prompts</tolerance>
    </execution_speed>
    
    <accuracy_consistency>
      <target>95% consistency across repeated evaluations</target>
      <measurement>Score variance for identical prompts</measurement>
      <tolerance>Maximum 0.5 point difference in repeated evaluations</tolerance>
    </accuracy_consistency>
    
    <coverage_completeness>
      <target>100% evaluation criteria coverage</target>
      <measurement>All criteria addressed in every evaluation</measurement>
      <tolerance>No missing criteria in any evaluation</tolerance>
    </coverage_completeness>
  </performance_benchmarks>
  
  <error_handling_tests>
    <malformed_prompt_handling>
      <test_case>Empty prompt string</test_case>
      <expected_behavior>Graceful error handling with helpful message</expected_behavior>
      <validation>Error reported clearly without system failure</validation>
    </malformed_prompt_handling>
    
    <agent_failure_recovery>
      <test_case>Simulated evaluator agent failure</test_case>
      <expected_behavior>Remaining agents continue, partial results reported</expected_behavior>
      <validation>System resilience maintained with degraded functionality</validation>
    </agent_failure_recovery>
    
    <consensus_deadlock_resolution">
      <test_case>Complete disagreement between all evaluators</test_case>
      <expected_behavior>Fallback to weighted average with uncertainty notation</expected_behavior>
      <validation>Deadlock resolved with transparent uncertainty acknowledgment</validation>
    </consensus_deadlock_resolution>
  </error_handling_tests>
  
  <integration_tests>
    <session_management_integration>
      <test_requirement>Automatic session creation for evaluation tracking</test_requirement>
      <validation_criteria>
        Session created automatically when evaluation begins
        All evaluator progress tracked in session updates
        Final results documented in session completion
        Session URL accessible for coordination and review
      </validation_criteria>
    </session_management_integration>
    
    <dashboard_integration>
      <test_requirement>Evaluation results feed into dashboard system</test_requirement>
      <validation_criteria>
        Evaluation data properly formatted for dashboard consumption
        Historical tracking captures all evaluation results
        Trend analysis updates with new evaluation data
        Statistical calculations reflect updated dataset
      </validation_criteria>
    </dashboard_integration>
    
    <quality_gates_integration>
      <test_requirement>Evaluation system integrates with quality standards</test_requirement>
      <validation_criteria>
        Benchmark compliance checked against production standards
        Quality alerts triggered for scores below thresholds
        Automated improvement recommendations generated
        Integration with continuous improvement workflows
      </validation_criteria>
    </quality_gates_integration>
  </integration_tests>
  
  <test_automation>
    <automated_test_suite>
      <daily_smoke_tests>
        Basic functionality validation with standard test prompts
        Performance benchmark verification
        Integration point health checks
        Error handling capability verification
      </daily_smoke_tests>
      
      <weekly_comprehensive_tests>
        Full test scenario execution across all complexity levels
        Consensus mechanism stress testing with edge cases
        Dashboard integration and data flow validation
        Historical data consistency and trend analysis verification
      </weekly_comprehensive_tests>
      
      <monthly_performance_analysis>
        Detailed performance trend analysis over extended period
        Accuracy consistency measurement across large sample size
        System scalability testing with high evaluation volumes
        Optimization opportunity identification and implementation
      </monthly_performance_analysis>
    </automated_test_suite>
    
    <continuous_validation>
      <real_time_monitoring>
        Live evaluation performance tracking
        Immediate alerts for performance degradation
        Automatic fallback activation for system issues
        Quality metric trending and anomaly detection
      </real_time_monitoring>
      
      <feedback_integration>
        User feedback collection on evaluation accuracy
        Continuous improvement based on evaluation effectiveness
        Model accuracy tuning based on real-world usage
        System optimization driven by performance data
      </feedback_integration>
    </continuous_validation>
  </test_automation>
  
  <test_reporting>
    <test_execution_report>
      <summary_metrics>
        Total tests executed and pass/fail rates
        Performance benchmark compliance status
        Integration test results across all modules
        Error handling effectiveness validation
      </summary_metrics>
      
      <detailed_analysis>
        Individual test scenario results with scoring analysis
        Performance trend analysis and optimization recommendations
        Integration point health assessment with improvement suggestions
        Quality assurance validation with benchmark compliance review
      </detailed_analysis>
    </test_execution_report>
    
    <quality_assessment>
      <evaluation_accuracy>
        Comparison of evaluation results against known quality benchmarks
        Analysis of evaluator agent consistency and reliability
        Consensus mechanism effectiveness measurement
        Improvement recommendation quality assessment
      </evaluation_accuracy>
      
      <system_reliability">
        Uptime and availability metrics for evaluation system
        Error rate analysis and recovery effectiveness
        Performance consistency across different load conditions
        Integration stability with dependent modules
      </system_reliability>
    </quality_assessment>
  </test_reporting>
  
  <integration_points>
    <depends_on>
      patterns/prompt-evaluation.md for core evaluation functionality
      patterns/evaluation-dashboard.md for result visualization
      patterns/session-management.md for coordination tracking
      quality/production-standards.md for benchmark validation
    </depends_on>
    <provides_to>
      All evaluation modules for quality assurance validation
      Development teams for evaluation system reliability confirmation
      Quality gates for automated testing integration
    </provides_to>
  </integration_points>
  
</module>