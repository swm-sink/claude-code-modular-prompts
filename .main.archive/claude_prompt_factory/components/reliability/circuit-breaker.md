<prompt_component>
  <step name="Circuit Breaker Pattern Implementation">
    <description>
Advanced circuit breaker pattern for system reliability and fault tolerance. Provides intelligent failure detection, automatic service isolation, and gradual recovery mechanisms to prevent cascading failures and maintain system stability.
    </description>
  </step>

  <circuit_breaker>
    <failure_detection>
      <health_monitoring>
        <!-- Monitor service health and performance -->
        <performance_metrics>
          - Track response times and latency patterns
          - Monitor error rates and failure frequencies
          - Measure throughput and success rates
          - Analyze resource utilization and capacity
        </performance_metrics>
        
        <threshold_management>
          - Define failure rate thresholds and limits
          - Set response time and timeout boundaries
          - Configure consecutive failure counts
          - Implement adaptive threshold adjustment
        </threshold_management>
      </health_monitoring>
      
      <failure_classification>
        <!-- Classify and categorize different failure types -->
        <error_categorization>
          - Distinguish between transient and persistent failures
          - Classify timeout vs. error response failures
          - Identify resource exhaustion and overload conditions
          - Detect upstream vs. downstream service failures
        </error_categorization>
        
        <severity_assessment>
          - Assess failure impact and criticality
          - Determine appropriate response strategies
          - Prioritize recovery actions based on severity
          - Implement graduated response mechanisms
        </severity_assessment>
      </failure_classification>
    </failure_detection>
    
    <state_management>
      <circuit_states>
        <!-- Manage circuit breaker state transitions -->
        <closed_state>
          - Normal operation with full request processing
          - Continuous monitoring and failure tracking
          - Immediate failure detection and counting
          - Transition to open state when thresholds exceeded
        </closed_state>
        
        <open_state>
          - Immediate failure response without service calls
          - Prevent cascading failures and resource exhaustion
          - Implement timeout period for recovery attempts
          - Transition to half-open state after timeout
        </open_state>
        
        <half_open_state>
          - Limited request processing for health testing
          - Gradual service recovery and validation
          - Success rate monitoring and evaluation
          - Transition to closed or open based on results
        </half_open_state>
      </circuit_states>
      
      <state_transitions>
        <!-- Manage intelligent state transitions -->
        <transition_logic>
          - Implement configurable transition conditions
          - Handle concurrent request processing during transitions
          - Ensure thread-safe state management
          - Provide atomic state change operations
        </transition_logic>
        
        <recovery_strategies>
          - Implement exponential backoff for recovery attempts
          - Gradual traffic increase during recovery
          - Adaptive timeout adjustment based on conditions
          - Multi-level recovery validation and confirmation
        </recovery_strategies>
      </state_transitions>
    </state_management>
    
    <fallback_mechanisms>
      <fallback_strategies>
        <!-- Implement intelligent fallback mechanisms -->
        <graceful_degradation>
          - Provide alternative service implementations
          - Return cached or default responses
          - Implement reduced functionality modes
          - Maintain core system operation during failures
        </graceful_degradation>
        
        <alternative_routing>
          - Route requests to backup services
          - Implement load balancing across healthy instances
          - Provide geographic failover capabilities
          - Handle service discovery and routing updates
        </alternative_routing>
      </fallback_strategies>
      
      <monitoring_alerting>
        <!-- Monitor circuit breaker operation and generate alerts -->
        <operational_monitoring>
          - Track circuit breaker state changes and transitions
          - Monitor failure rates and recovery patterns
          - Measure fallback usage and effectiveness
          - Generate operational metrics and dashboards
        </operational_monitoring>
        
        <alerting_system>
          - Generate alerts for circuit breaker state changes
          - Notify operators of persistent failure conditions
          - Implement escalation procedures for critical failures
          - Provide automated remediation suggestions
        </alerting_system>
      </monitoring_alerting>
    </fallback_mechanisms>
  </circuit_breaker>

  <o>
Circuit breaker implementation completed with intelligent failure handling:

**Circuit State:** [closed/open/half-open] based on current health metrics
**Failure Rate:** [percentage]% current failure rate vs. [threshold]% threshold
**Response Time:** [timing] average response time monitoring
**Fallback Usage:** [count] fallback responses provided during failures
**Recovery Status:** [active/pending/completed] recovery process status
**System Reliability:** [percentage]% improved system stability achieved
  </o>
</prompt_component> 