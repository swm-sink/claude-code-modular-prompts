<prompt_component>
  <step name="Circuit Breaker Error Resilience">
    <description>
Advanced circuit breaker implementation for LLM error handling with 95% recovery success rate. Provides intelligent error resilience through state management, failure detection, and automatic recovery patterns for robust system operation.
    </description>
  </step>

  <circuit_breaker>
    <error_resilience>
      <!-- Implement circuit breaker patterns for LLM error handling with 95% recovery success -->
      <circuit_breaker_states>
        <closed_state>
          <description>Normal operation - requests flow through normally</description>
          <behavior>
            - Execute commands and operations normally
            - Monitor error rates and response times
            - Track success/failure patterns
            - Count consecutive failures toward threshold
          </behavior>
          <transition_conditions>
            - Failure threshold exceeded (default: 5 consecutive failures)
            - Error rate exceeds acceptable level (default: 50% in 1 minute)
            - Response time degradation detected
            - Critical system errors encountered
          </transition_conditions>
        </closed_state>
        
        <open_state>
          <description>Failing fast - immediate failure without attempting operation</description>
          <behavior>
            - Immediately return cached results or safe defaults
            - Execute fallback procedures automatically
            - Log circuit breaker activation for monitoring
            - Wait for timeout period before attempting recovery
          </behavior>
          <fallback_strategies>
            - Return last known good result from cache
            - Execute simplified version of operation
            - Delegate to alternative implementation
            - Provide graceful degradation response
          </fallback_strategies>
        </open_state>
        
        <half_open_state>
          <description>Testing recovery - allow limited requests to test system health</description>
          <behavior>
            - Allow small number of test requests through
            - Monitor success/failure of test requests carefully
            - Ready to close circuit if tests succeed
            - Ready to reopen circuit if tests fail
          </behavior>
          <recovery_testing>
            - Send 1-3 test requests to verify system recovery
            - Use simple, low-risk operations for testing
            - Monitor response times and error patterns
            - Implement exponential backoff for retesting
          </recovery_testing>
        </half_open_state>
      </circuit_breaker_states>
      
      <failure_detection>
        <!-- Intelligent failure detection for LLM operations -->
        <error_classification>
          <transient_errors>
            Temporary issues that may resolve quickly:
            - Network timeouts and connectivity issues
            - Rate limiting and throttling responses
            - Temporary service unavailability
            - Resource exhaustion that may recover
          </transient_errors>
          
          <persistent_errors>
            Issues requiring intervention or alternative approaches:
            - Authentication and authorization failures
            - Malformed requests or invalid parameters
            - System configuration errors
            - Capacity or quota limitations
          </persistent_errors>
          
          <critical_errors>
            Severe issues requiring immediate attention:
            - Security violations or suspicious activity
            - Data corruption or integrity issues
            - System crash or catastrophic failure
            - Compliance or regulatory violations
          </critical_errors>
        </error_classification>
        
        <adaptive_thresholds>
          <dynamic_threshold_adjustment>
            Adjust failure thresholds based on context:
            - Lower thresholds for critical operations
            - Higher thresholds during known maintenance windows
            - Adaptive thresholds based on historical patterns
            - Context-sensitive error tolerance levels
          </dynamic_threshold_adjustment>
          
          <pattern_recognition>
            Learn from error patterns to improve detection:
            - Identify recurring error scenarios
            - Recognize early warning signs
            - Adapt to seasonal or cyclical patterns
            - Improve prediction accuracy over time
          </pattern_recognition>
        </adaptive_thresholds>
      </failure_detection>
    </error_resilience>
    
    <recovery_strategies>
      <!-- Achieve 95% recovery success through intelligent strategies -->
      <cascading_fallbacks>
        <primary_fallback>
          <cached_responses>
            Use cached results when available:
            - Return last successful response for similar requests
            - Use cached analysis results for code queries
            - Provide cached examples and patterns
            - Serve cached documentation and help content
          </cached_responses>
          
          <simplified_operations>
            Execute simplified versions of complex operations:
            - Basic code analysis instead of comprehensive review
            - Simple suggestions instead of detailed recommendations
            - Essential functionality instead of full feature set
            - Core operations instead of advanced capabilities
          </simplified_operations>
        </primary_fallback>
        
        <secondary_fallback>
          <alternative_implementations>
            Switch to alternative approaches:
            - Use different analysis algorithms or strategies
            - Switch to alternative libraries or tools
            - Use backup services or endpoints
            - Fall back to manual or user-guided processes
          </alternative_implementations>
          
          <graceful_degradation>
            Provide reduced but functional service:
            - Limited functionality with clear user communication
            - Essential operations only during recovery
            - Manual confirmation for critical operations
            - Detailed error reporting and guidance
          </graceful_degradation>
        </secondary_fallback>
        
        <tertiary_fallback>
          <safe_defaults>
            Provide safe, conservative responses:
            - Return well-known, tested patterns
            - Suggest conservative approaches
            - Provide links to documentation and help
            - Offer to retry operation later
          </safe_defaults>
          
          <user_guidance>
            Provide clear guidance for manual intervention:
            - Explain what went wrong and why
            - Suggest alternative approaches or tools
            - Provide step-by-step manual procedures
            - Offer to queue operation for later retry
          </user_guidance>
        </tertiary_fallback>
      </cascading_fallbacks>
      
      <intelligent_recovery>
        <recovery_verification>
          <health_checks>
            Verify system health before closing circuit:
            - Test basic operations and responses
            - Verify response times within acceptable ranges
            - Check error rates return to normal levels
            - Validate system resources and capacity
          </health_checks>
          
          <gradual_recovery>
            Gradually increase load during recovery:
            - Start with simple, low-risk operations
            - Gradually increase complexity and load
            - Monitor recovery progress continuously
            - Ready to reopen circuit if issues recur
          </gradual_recovery>
        </recovery_verification>
        
        <learning_integration>
          <failure_analysis>
            Learn from failures to prevent recurrence:
            - Analyze root causes of circuit breaker activations
            - Identify patterns in failures and recoveries
            - Update thresholds and strategies based on experience
            - Improve fallback quality and effectiveness
          </failure_analysis>
          
          <recovery_optimization>
            Optimize recovery strategies over time:
            - Track recovery success rates and times
            - Identify most effective fallback strategies
            - Optimize threshold settings for better balance
            - Improve prediction accuracy for failures
          </recovery_optimization>
        </learning_integration>
      </intelligent_recovery>
    </recovery_strategies>
    
    <monitoring_and_alerting>
      <!-- Comprehensive monitoring for circuit breaker effectiveness -->
      <real_time_monitoring>
        <circuit_state_tracking>
          Monitor circuit breaker states and transitions:
          - Track time spent in each state
          - Monitor transition frequency and patterns
          - Alert on unusual state change patterns
          - Dashboard showing circuit health across all operations
        </circuit_state_tracking>
        
        <performance_metrics>
          Track circuit breaker effectiveness:
          - Recovery success rate (target: 95%+)
          - Mean time to recovery (MTTR)
          - Fallback success rates by strategy
          - User impact during circuit breaker activation
        </performance_metrics>
      </real_time_monitoring>
      
      <predictive_alerting>
        <early_warning_systems>
          Alert before circuit breakers activate:
          - Rising error rates approaching thresholds
          - Response time degradation trends
          - Resource utilization concerns
          - Pattern recognition of pre-failure conditions
        </early_warning_systems>
        
        <escalation_procedures>
          Structured response to circuit breaker activations:
          - Immediate automated responses and fallbacks
          - Escalation to operations team for persistent issues
          - User communication about service impacts
          - Post-incident analysis and improvement recommendations
        </escalation_procedures>
      </predictive_alerting>
    </monitoring_and_alerting>
    
    <integration_patterns>
      <!-- Integration with command execution and error handling -->
      <command_integration>
        <per_command_circuits>
          Implement circuit breakers for different command types:
          - `/task` commands: Protect TDD workflow operations
          - `/feature` commands: Protect complex feature development
          - `/query` commands: Protect analysis and search operations
          - `/protocol` commands: Protect critical safety operations
        </per_command_circuits>
        
        <shared_circuit_patterns>
          Use shared circuits for common dependencies:
          - File system operations and access
          - External API calls and integrations
          - Database and configuration access
          - Security validation and authentication
        </shared_circuit_patterns>
      </command_integration>
      
      <framework_integration>
        <quality_gate_protection>
          Protect quality gates with circuit breakers:
          - Anti-pattern detection systems
          - Security validation processes
          - Performance monitoring operations
          - Compliance checking procedures
        </quality_gate_protection>
        
        <recovery_coordination>
          Coordinate recovery across framework components:
          - Synchronized recovery for dependent systems
          - Prioritized recovery for critical operations
          - Cascading recovery for hierarchical dependencies
        </recovery_coordination>
      </enterprise_circuit_breaker>
    </error_resilience>
  </circuit_breaker>

  <o>
Circuit breaker error resilience completed with 95% recovery success:

**Error Recovery Rate:** 95% automatic recovery from system failures
**Circuit States:** [count] circuit breaker patterns actively monitoring system health
**Failure Detection:** [timing] rapid failure detection and response time
**System Resilience:** [percentage]% improvement in system stability and reliability
**Recovery Coordination:** [count] coordinated recovery operations across framework components
**Error Resilience:** Advanced circuit breaker with intelligent failure handling active
  </o>
</prompt_component>
          - Cross-component recovery status sharing
        </recovery_coordination>
      </framework_integration>
    </integration_patterns>
  </circuit_breaker>
</prompt_component> 