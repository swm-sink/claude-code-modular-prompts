<prompt_component>
  <step name="Integration Testing Framework">
    <description>
Comprehensive integration testing system that validates component interactions, service communications, and system integrations. Ensures proper data flow, API contracts, and system reliability across all integration points.
    </description>
  </step>

  <integration_testing>
    <component_integration>
      <interaction_testing>
        <!-- Test component-to-component interactions -->
        <interface_validation>
          - Verify API contract compliance between components
          - Test data exchange formats and protocols
          - Validate error handling across component boundaries
          - Check integration point performance and reliability
        </interface_validation>
        
        <dependency_testing>
          - Test component dependency resolution
          - Validate circular dependency detection
          - Check version compatibility across components
          - Ensure graceful degradation when dependencies fail
        </dependency_testing>
      </interaction_testing>
      
      <system_integration>
        <!-- Test system-level integrations -->
        <external_services>
          - Test external API integrations and responses
          - Validate database connections and operations
          - Check file system access and permissions
          - Test network communications and protocols
        </external_services>
        
        <environment_integration>
          - Test across different deployment environments
          - Validate configuration management across environments
          - Check environment-specific behavior and settings
          - Ensure consistent functionality across platforms
        </environment_integration>
      </system_integration>
    </component_integration>
    
    <data_flow_testing>
      <data_transformation>
        <!-- Test data flow and transformation -->
        <pipeline_testing>
          - Validate data processing pipelines
          - Test data transformation accuracy
          - Check data validation and sanitization
          - Ensure data integrity throughout processing
        </pipeline_testing>
        
        <state_management>
          - Test state transitions and persistence
          - Validate session management and continuity
          - Check data consistency across operations
          - Ensure proper cleanup and resource management
        </state_management>
      </data_transformation>
    </data_flow_testing>
    
    <performance_integration>
      <load_testing>
        <!-- Test integration performance under load -->
        <throughput_testing>
          - Measure system throughput under various loads
          - Test concurrent user scenarios
          - Validate resource utilization and scaling
          - Check system stability under stress conditions
        </throughput_testing>
        
        <latency_testing>
          - Measure end-to-end response times
          - Test network latency impact
          - Validate caching effectiveness
          - Check performance degradation patterns
        </latency_testing>
      </load_testing>
    </performance_integration>
  </integration_testing>

  <o>
Integration testing completed with comprehensive validation of system interactions:

**Component Integrations:** [count] integration points tested successfully
**API Contracts:** [percentage]% contract compliance verified
**Data Flow:** [count] data pipelines validated with [percentage]% accuracy
**Performance:** [timing] average integration response time
**External Services:** [count] external integrations tested and verified
**Overall Integration Health:** [healthy/warning/critical] system status
  </o>
</prompt_component> 