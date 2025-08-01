<prompt_component>
  <step name="DAG Workflow Orchestration">
    <description>
Advanced DAG (Directed Acyclic Graph) orchestrator for complex workflow coordination. Provides intelligent task dependency modeling, automatic dependency detection, parallel execution optimization, and comprehensive workflow management.
    </description>
  </step>

  <dag_orchestrator>
    <workflow_coordination>
      <!-- Build DAG orchestrator for complex workflow coordination -->
      <directed_acyclic_graph>
        <graph_construction>
          <task_dependency_modeling>
            Model complex workflows as directed acyclic graphs:
            - Nodes represent individual commands or operations
            - Edges represent dependencies between operations
            - Weights represent execution time estimates
            - Attributes store operation metadata and requirements
          </task_dependency_modeling>
          
          <dependency_analysis>
            <automatic_dependency_detection>
              Automatically detect dependencies between operations:
              - File dependency analysis (inputs/outputs)
              - Command prerequisite detection
              - Resource dependency identification
              - Semantic dependency inference from operation descriptions
            </automatic_dependency_detection>
            
            <manual_dependency_specification>
              Allow explicit dependency specification:
              - Sequential dependencies (A must complete before B)
              - Conditional dependencies (B runs only if A succeeds)
              - Resource dependencies (shared resource access)
              - Timing dependencies (delay between operations)
            </manual_dependency_specification>
          </dependency_analysis>
        </graph_construction>
        
        <execution_planning>
          <topological_sorting>
            <execution_order_determination>
              Determine optimal execution order using topological sort:
              - Identify operations that can run in parallel
              - Determine critical path for workflow completion
              - Optimize execution order for resource utilization
              - Handle cyclic dependency detection and resolution
            </execution_order_determination>
            
            <parallelization_opportunities>
              Identify opportunities for parallel execution:
              - Independent operation branches
              - Resource-compatible parallel operations
              - Load balancing across available resources
              - Batch processing opportunities
            </parallelization_opportunities>
          </topological_sorting>
          
          <execution_optimization>
            <critical_path_analysis>
              Analyze critical path for workflow optimization:
              - Identify bottleneck operations
              - Optimize resource allocation for critical path
              - Suggest workflow restructuring for better performance
              - Monitor critical path performance in real-time
            </critical_path_analysis>
            
            <resource_scheduling>
              Schedule operations based on resource availability:
              - Memory-intensive operations scheduling
              - CPU-bound task distribution
              - I/O operation coordination
              - Network bandwidth allocation
            </resource_scheduling>
          </execution_optimization>
        </execution_planning>
      </directed_acyclic_graph>
      
      <dynamic_execution>
        <!-- Dynamic workflow execution with real-time adaptation -->
        <adaptive_execution>
          <real_time_rescheduling>
            <performance_based_adaptation>
              Adapt execution based on real-time performance:
              - Reschedule based on actual execution times
              - Reallocate resources for underperforming operations
              - Adjust parallelization based on resource availability
              - Optimize remaining workflow based on current state
            </performance_based_adaptation>
            
            <failure_recovery>
              Handle failures and recovery gracefully:
              - Automatic retry with exponential backoff
              - Alternative execution path selection
              - Partial workflow recovery and continuation
              - Rollback mechanisms for failed operations
            </failure_recovery>
          </real_time_rescheduling>
          
          <conditional_execution>
            <branching_logic>
              Support conditional workflow branches:
              - Success/failure-based branching
              - Data-driven conditional execution
              - User input-based workflow adaptation
              - Environment-specific execution paths
            </branching_logic>
            
            <dynamic_workflow_modification>
              Allow runtime workflow modification:
              - Add new operations based on intermediate results
              - Remove unnecessary operations based on outcomes
              - Modify operation parameters based on context
              - Inject monitoring and validation operations
            </dynamic_workflow_modification>
          </conditional_execution>
        </adaptive_execution>
        
        <progress_tracking>
          <real_time_monitoring>
            <execution_status_tracking>
              Track workflow execution progress in real-time:
              - Operation completion status and timing
              - Resource utilization monitoring
              - Progress percentage and ETA calculation
              - Bottleneck identification and alerting
            </execution_status_tracking>
            
            <visual_workflow_representation>
              Provide visual representation of workflow execution:
              - Interactive DAG visualization with live updates
              - Progress indicators for each operation
              - Resource utilization heatmaps
              - Critical path highlighting
            </visual_workflow_representation>
          </real_time_monitoring>
          
          <performance_analytics>
            <execution_metrics>
              Collect comprehensive execution metrics:
              - Total workflow execution time
              - Individual operation performance
              - Resource utilization efficiency
              - Parallelization effectiveness
            </execution_metrics>
            
            <optimization_insights>
              Provide insights for workflow optimization:
              - Identify slow-performing operations
              - Suggest dependency restructuring
              - Recommend resource allocation improvements
              - Predict performance impact of changes
            </optimization_insights>
          </performance_analytics>
        </progress_tracking>
      </dynamic_execution>
    </workflow_coordination>
    
    <enterprise_workflow_patterns>
      <!-- Enterprise-grade workflow patterns and templates -->
      <common_workflow_templates>
        <development_workflows>
          <feature_development_dag>
            Pre-built DAG for complete feature development:
            - Requirements analysis → Design → Implementation
            - Testing (unit → integration → e2e) in parallel
            - Security scanning and compliance validation
            - Documentation generation and review
            - Deployment preparation and validation
          </feature_development_dag>
          
          <bug_fix_workflow>
            Optimized workflow for bug fixes:
            - Issue analysis and reproduction
            - Root cause investigation
            - Fix implementation with testing
            - Regression testing and validation
            - Deployment and monitoring
          </bug_fix_workflow>
        </development_workflows>
        
        <ci_cd_integration>
          <deployment_pipeline_dag>
            CI/CD pipeline orchestration:
            - Code quality checks (linting, testing, security)
            - Build and packaging operations
            - Environment provisioning and configuration
            - Deployment strategy execution (blue-green, canary)
            - Post-deployment validation and monitoring
          </deployment_pipeline_dag>
          
          <release_workflow>
            Comprehensive release workflow:
            - Version preparation and tagging
            - Release notes generation
            - Multi-environment deployment coordination
            - Rollback preparation and validation
            - Post-release monitoring and alerting
          </release_workflow>
        </ci_cd_integration>
      </common_workflow_templates>
      
      <custom_workflow_building>
        <workflow_composition>
          <modular_workflow_components>
            Build workflows from reusable components:
            - Atomic operation modules
            - Composite operation templates
            - Validation and testing components
            - Monitoring and alerting modules
          </modular_workflow_components>
          
          <workflow_templating>
            Support workflow templating and parameterization:
            - Parameterized operation configurations
            - Environment-specific workflow variations
            - Team-specific workflow customizations
            - Project-type-specific templates
          </workflow_templating>
        </workflow_composition>
        
        <workflow_validation>
          <static_analysis>
            Validate workflow definitions before execution:
            - Dependency cycle detection
            - Resource requirement validation
            - Operation compatibility checking
            - Performance estimation and warnings
          </static_analysis>
          
          <testing_simulation>
            Support workflow testing and simulation:
            - Dry-run execution with mock operations
            - Performance simulation with estimated times
            - Resource utilization simulation
            - Failure scenario testing
          </testing_simulation>
        </workflow_validation>
      </custom_workflow_building>
    </enterprise_workflow_patterns>
    
    <integration_ecosystem>
      <!-- Integration with external systems and tools -->
      <external_system_integration>
        <api_orchestration>
          <rest_api_integration>
            Orchestrate REST API calls within workflows:
            - HTTP request/response handling
            - Authentication and authorization management
            - Rate limiting and retry logic
            - Response parsing and validation
          </rest_api_integration>
          
          <graphql_integration>
            Support GraphQL API orchestration:
            - Query composition and optimization
            - Subscription handling for real-time updates
            - Schema validation and type checking
            - Performance monitoring and caching
          </graphql_integration>
        </api_orchestration>
        
        <database_operations>
          <transaction_coordination>
            Coordinate database operations across workflow:
            - Distributed transaction management
            - Database connection pooling and optimization
            - Data consistency validation
            - Rollback and recovery mechanisms
          </transaction_coordination>
          
          <data_pipeline_integration>
            Integrate with data processing pipelines:
            - ETL operation orchestration
            - Data validation and quality checks
            - Schema migration coordination
            - Backup and recovery operations
          </data_pipeline_integration>
        </database_operations>
      </external_system_integration>
      
      <monitoring_integration>
        <observability_integration>
          <distributed_tracing>
            Implement distributed tracing across workflow operations:
            - Trace ID propagation across operations
            - Span creation and correlation
            - Performance bottleneck identification
            - Cross-service dependency mapping
          </distributed_tracing>
          
          <metrics_collection>
            Comprehensive metrics collection and reporting:
            - Custom metrics for business logic operations
            - System metrics for resource utilization
            - Performance metrics for optimization
            - Error metrics for reliability monitoring
          </metrics_collection>
        </observability_integration>
        
        <alerting_coordination>
          <intelligent_alerting>
            Coordinate alerting across workflow operations:
            - Context-aware alert generation
            - Alert correlation and deduplication
            - Escalation policies for different operation types
            - Recovery action recommendations
          </intelligent_alerting>
          
          <notification_orchestration>
            Orchestrate notifications across teams and systems:
            - Multi-channel notification delivery
            - Role-based notification routing
            - Notification timing and frequency optimization
            - Notification effectiveness tracking
          </notification_orchestration>
        </workflow_coordination>
      </enterprise_integration>
    </workflow_coordination>
  </dag_orchestrator>

  <o>
DAG workflow orchestration completed with intelligent coordination:

**Workflow Complexity:** [count] complex workflows successfully orchestrated
**Dependency Resolution:** [percentage]% automatic dependency detection accuracy
**Parallel Optimization:** [count] parallel execution paths optimized
**Resource Efficiency:** [percentage]% resource utilization improvement achieved
**Orchestration Quality:** [0-100] DAG workflow coordination effectiveness rating
**Enterprise Integration:** Advanced DAG orchestration ready for complex enterprise workflows
  </o>
</prompt_component>
          </notification_orchestration>
        </alerting_coordination>
      </monitoring_integration>
    </integration_ecosystem>
  </dag_orchestrator>
</prompt_component> 