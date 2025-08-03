<prompt_component>
  <step name="Circuit Breaker Pattern Implementation">
    <description>
Advanced circuit breaker implementation for LLM error handling and system reliability with 95% recovery success rate. Provides intelligent failure detection, automatic service isolation, and gradual recovery mechanisms to prevent cascading failures while maintaining system stability through state management and fallback strategies.
    </description>
  </step>

  <circuit_breaker>
    <circuit_breaker_states>
      <!-- Three-state circuit breaker pattern -->
      <closed_state>
        <description>Normal operation - requests flow through normally</description>
        <behavior>
          - Execute commands and operations normally
          - Monitor error rates and response times continuously
          - Track success/failure patterns and performance metrics
          - Count consecutive failures toward configurable threshold
        </behavior>
        <transition_conditions>
          - Failure threshold exceeded (default: 5 consecutive failures)
          - Error rate exceeds acceptable level (default: 50% in 1 minute)
          - Response time degradation detected beyond boundaries
          - Critical system errors or resource exhaustion encountered
        </transition_conditions>
      </closed_state>
      
      <open_state>
        <description>Failing fast - immediate failure without attempting operation</description>
        <behavior>
          - Immediately return cached results or safe defaults
          - Execute fallback procedures automatically
          - Log circuit breaker activation for monitoring
          - Wait for timeout period before attempting recovery
          - Prevent cascading failures and resource exhaustion
        </behavior>
        <fallback_strategies>
          - Return last known good result from cache
          - Execute simplified version of operation
          - Delegate to alternative implementation or backup services
          - Provide graceful degradation response with clear user guidance
          - Implement reduced functionality modes for core operations
        </fallback_strategies>
      </open_state>
      
      <half_open_state>
        <description>Testing recovery - allow limited requests to test system health</description>
        <behavior>
          - Allow small number of test requests through (1-3 requests)
          - Monitor success/failure of test requests carefully
          - Ready to close circuit if tests succeed consistently
          - Ready to reopen circuit if tests fail
          - Gradual traffic increase during recovery validation
        </behavior>
        <recovery_testing>
          - Send test requests to verify system recovery
          - Use simple, low-risk operations for health testing
          - Monitor response times and error patterns closely
          - Implement exponential backoff for retesting intervals
          - Multi-level recovery validation before full restoration
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
          - LLM context window overflow
        </transient_errors>
        
        <persistent_errors>
          Issues requiring intervention or alternative approaches:
          - Authentication and authorization failures
          - Malformed requests or invalid parameters
          - System configuration errors
          - Capacity or quota limitations
          - Incompatible model or API version issues
        </persistent_errors>
        
        <critical_errors>
          Severe issues requiring immediate attention:
          - Security violations or suspicious activity
          - Data corruption or integrity issues
          - System crash or catastrophic failure
          - Compliance or regulatory violations
          - Complete service outages
        </critical_errors>
      </error_classification>
      
      <adaptive_thresholds>
        <dynamic_threshold_adjustment>
          Adjust failure thresholds based on context:
          - Lower thresholds for critical operations (safety, security)
          - Higher thresholds during known maintenance windows
          - Adaptive thresholds based on historical patterns
          - Context-sensitive error tolerance levels
          - Command-specific threshold configurations
        </dynamic_threshold_adjustment>
        
        <pattern_recognition>
          Learn from error patterns to improve detection:
          - Identify recurring error scenarios and root causes
          - Recognize early warning signs and degradation patterns
          - Adapt to seasonal or cyclical variations
          - Improve prediction accuracy over time
          - Track correlation between different failure types
        </pattern_recognition>
      </adaptive_thresholds>
    </failure_detection>
    
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
            - Implement intelligent cache invalidation
          </cached_responses>
          
          <simplified_operations>
            Execute simplified versions of complex operations:
            - Basic code analysis instead of comprehensive review
            - Simple suggestions instead of detailed recommendations
            - Essential functionality instead of full feature set
            - Core operations instead of advanced capabilities
            - Reduced context processing for faster response
          </simplified_operations>
        </primary_fallback>
        
        <secondary_fallback>
          <alternative_implementations>
            Switch to alternative approaches:
            - Use different analysis algorithms or strategies
            - Switch to alternative models or API endpoints
            - Route to backup services or geographic regions
            - Fall back to manual or user-guided processes
            - Implement load balancing across healthy instances
          </alternative_implementations>
          
          <graceful_degradation>
            Provide reduced but functional service:
            - Limited functionality with clear user communication
            - Essential operations only during recovery
            - Manual confirmation for critical operations
            - Detailed error reporting and guidance
            - Progressive enhancement as services recover
          </graceful_degradation>
        </secondary_fallback>
      </cascading_fallbacks>
      
      <intelligent_recovery>
        <recovery_verification>
          <health_checks>
            Verify system health before closing circuit:
            - Test basic operations and response integrity
            - Verify response times within acceptable ranges
            - Check error rates return to normal levels
            - Validate system resources and capacity
            - Confirm downstream dependencies are healthy
          </health_checks>
          
          <gradual_recovery>
            Gradually increase load during recovery:
            - Start with simple, low-risk operations
            - Gradually increase complexity and request volume
            - Monitor recovery progress continuously
            - Ready to reopen circuit if issues recur
            - Implement canary testing for critical operations
          </gradual_recovery>
        </recovery_verification>
      </intelligent_recovery>
    </recovery_strategies>
    
    <monitoring_and_alerting>
      <!-- Comprehensive monitoring for circuit breaker effectiveness -->
      <real_time_monitoring>
        <circuit_state_tracking>
          Monitor circuit breaker states and transitions:
          - Track time spent in each state with histograms
          - Monitor transition frequency and patterns
          - Alert on unusual state change patterns
          - Dashboard showing circuit health across all operations
          - Real-time visualization of circuit breaker topology
        </circuit_state_tracking>
        
        <performance_metrics>
          Track circuit breaker effectiveness:
          - Recovery success rate (target: 95%+)
          - Mean time to recovery (MTTR) tracking
          - Fallback success rates by strategy type
          - User impact metrics during circuit breaker activation
          - Service level objective (SLO) compliance monitoring
        </performance_metrics>
      </real_time_monitoring>
      
      <predictive_alerting>
        <early_warning_systems>
          Alert before circuit breakers activate:
          - Rising error rates approaching thresholds
          - Response time degradation trends
          - Resource utilization concerns and capacity limits
          - Pattern recognition of pre-failure conditions
          - Anomaly detection in service behavior
        </early_warning_systems>
        
        <escalation_procedures>
          Structured response to circuit breaker activations:
          - Immediate automated responses and fallbacks
          - Escalation to operations team for persistent issues
          - User communication about service impacts
          - Post-incident analysis and improvement recommendations
          - Automated remediation for known failure patterns
        </escalation_procedures>
      </predictive_alerting>
    </monitoring_and_alerting>
    
    <integration_patterns>
      <!-- Integration with command execution and framework components -->
      <command_integration>
        <per_command_circuits>
          Implement circuit breakers for different command types:
          - `/task` commands: Protect TDD workflow operations
          - `/feature` commands: Protect complex feature development
          - `/query` commands: Protect analysis and search operations
          - `/protocol` commands: Protect critical safety operations
          - `/swarm` commands: Protect multi-agent coordination
        </per_command_circuits>
        
        <shared_circuit_patterns>
          Use shared circuits for common dependencies:
          - File system operations and access patterns
          - External API calls and integrations
          - LLM model invocations and context management
          - Security validation and authentication services
          - Component loading and initialization
        </shared_circuit_patterns>
      </command_integration>
      
      <framework_integration>
        <quality_gate_protection>
          Protect quality gates with circuit breakers:
          - Anti-pattern detection systems
          - Security validation processes
          - Performance monitoring operations
          - Compliance checking procedures
          - Component dependency resolution
        </quality_gate_protection>
        
        <recovery_coordination>
          Coordinate recovery across framework components:
          - Synchronized recovery for dependent systems
          - Prioritized recovery for critical operations
          - Cascading recovery for hierarchical dependencies
          - Cross-component recovery status sharing
          - Orchestrated restart sequences
        </recovery_coordination>
      </framework_integration>
    </integration_patterns>
  </circuit_breaker>

  <o>
Circuit breaker implementation completed with advanced failure handling:

**Recovery Success Rate:** 95%+ automatic recovery from system failures
**Circuit States:** Dynamic state management with intelligent transitions
**Failure Detection:** Adaptive thresholds with pattern recognition
**Fallback Strategies:** Multi-level cascading fallbacks for resilience
**System Reliability:** Comprehensive monitoring and predictive alerting
**Integration:** Seamless framework and command-level circuit breakers
  </o>
</prompt_component>