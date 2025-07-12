| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Error Recovery Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="error_recovery_pattern" category="patterns">
  
  <purpose>
    Systematic handling of failures and recovery strategies, providing resilient error management with appropriate recovery mechanisms and monitoring.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Errors or failures occur during execution</condition>
    <condition type="explicit">System stability needs improvement</condition>
    <condition type="explicit">Recovery mechanisms need implementation</condition>
    <condition type="explicit">Fault tolerance is required</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="detect_and_classify_error" order="1">
      <requirements>
        Error detection mechanism must be active
        Classification criteria must be defined
        Logging system must be operational
      </requirements>
      <actions>
        Identify the type and severity of the error
        Classify as fatal errors requiring immediate stop
        Identify recoverable errors allowing retry
        Categorize warning conditions needing attention
        Detect transient issues that may resolve
      </actions>
      <validation>
        Error is properly detected and logged
        Classification is accurate and consistent
        Severity level is appropriately assigned
        Error context is captured
      </validation>
    </phase>
    
    <phase name="assess_impact_and_context" order="2">
      <requirements>
        Error classification must be completed
        System state must be assessable
        Impact assessment framework must be available
      </requirements>
      <actions>
        Understand the scope and consequences
        Identify what systems or processes are affected
        Assess how critical the failed operation is
        Determine what data or state might be compromised
        Identify who needs to be notified
      </actions>
      <validation>
        Impact scope is clearly defined
        Critical operations are identified
        Data integrity status is assessed
        Stakeholder notification requirements are clear
      </validation>
    </phase>
    
    <phase name="choose_recovery_strategy" order="3">
      <requirements>
        Impact assessment must be completed
        Recovery strategies must be defined
        Strategy selection criteria must be established
      </requirements>
      <actions>
        Select appropriate recovery approach
        Consider automatic retry with backoff
        Evaluate fallback to alternative approach
        Assess graceful degradation of service
        Determine if manual intervention is required
      </actions>
      <validation>
        Recovery strategy is appropriate for error type
        Strategy selection is justified
        Recovery approach is feasible
        Resources for recovery are available
      </validation>
    </phase>
    
    <phase name="execute_recovery" order="4">
      <requirements>
        Recovery strategy must be selected
        System must be in recoverable state
        Recovery resources must be available
      </requirements>
      <actions>
        Implement the chosen recovery strategy
        Clean up any partial state
        Restore system to known good state
        Implement alternative approach
        Monitor recovery progress
      </actions>
      <validation>
        Recovery strategy is executed properly
        System state is cleaned up
        Alternative approach is working
        Recovery progress is monitored
      </validation>
    </phase>
    
    <phase name="verify_recovery" order="5">
      <requirements>
        Recovery execution must be completed
        System functionality must be testable
        Verification criteria must be defined
      </requirements>
      <actions>
        Confirm system is working correctly
        Test affected functionality
        Verify data integrity
        Check system performance
        Confirm user experience
      </actions>
      <validation>
        System functionality is restored
        Data integrity is verified
        Performance is acceptable
        User experience is confirmed
      </validation>
    </phase>
    
  </implementation>
  
  <recovery_strategies>
    <strategy name="immediate_retry">For transient failures</strategy>
    <strategy name="exponential_backoff">For resource contention</strategy>
    <strategy name="circuit_breaker">For cascading failures</strategy>
    <strategy name="fallback_service">For service unavailability</strategy>
    <strategy name="graceful_degradation">For partial failures</strategy>
  </recovery_strategies>
  
  <monitoring>
    <metric>Error rate tracking</metric>
    <metric>Recovery success metrics</metric>
    <metric>System health indicators</metric>
    <metric>User impact measurements</metric>
  </monitoring>
  
  <integration_points>
    <provides_to>
      patterns/implementation-pattern.md for robust code
      development/documentation.md for incident records
    </provides_to>
    <depends_on>
      ../../prompt_eng/../../prompt_eng/patterns/thinking/critical-thinking-pattern.md for failure analysis
      patterns/quality-validation-pattern.md with resilience testing
    </depends_on>
  </integration_points>
  
  <examples>
    <example name="api_timeout_recovery">
      <description>API timeout handling with retry logic</description>
      <code>
        DETECT: API timeout error detected
        ASSESS: Non-critical operation, retry possible
        STRATEGY: Exponential backoff retry
        EXECUTE: Retry with 1s, 2s, 4s delays
        VERIFY: Successful response received
      </code>
      <expected_output>
        Successful API response after recovery
        Minimal user impact from transient failure
        Proper logging of recovery process
      </expected_output>
    </example>
  </examples>
  
</module>
```