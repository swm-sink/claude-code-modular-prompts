<prompt_component>
  <step name="DAG Workflow Orchestration">
    <description>
Advanced Directed Acyclic Graph (DAG) orchestration system for complex workflow coordination. Provides intelligent task dependency modeling, automatic dependency detection, parallel execution optimization, and comprehensive workflow management with real-time monitoring and failure recovery capabilities.
    </description>
  </step>

  <dag_orchestrator>
    <workflow_modeling>
      <!-- Build and validate DAG structures for complex workflows -->
      <dag_construction>
        <task_dependency_modeling>
          Model complex workflows as directed acyclic graphs:
          - Nodes represent individual commands or operations
          - Edges represent dependencies between operations
          - Weights represent execution time estimates
          - Attributes store operation metadata and requirements
          - Priority levels and execution timeouts per task
        </task_dependency_modeling>
        
        <dependency_analysis>
          <automatic_dependency_detection>
            Automatically detect dependencies between operations:
            - File dependency analysis (inputs/outputs)
            - Command prerequisite detection
            - Resource dependency identification
            - Semantic dependency inference from operation descriptions
            - Data flow analysis and type compatibility checking
          </automatic_dependency_detection>
          
          <manual_dependency_specification>
            Allow explicit dependency specification:
            - Sequential dependencies (A must complete before B)
            - Conditional dependencies (B runs only if A succeeds)
            - Resource dependencies (shared resource access)
            - Timing dependencies (delay between operations)
            - Dynamic dependencies based on runtime conditions
          </manual_dependency_specification>
        </dependency_analysis>
      </dag_construction>
      
      <workflow_validation>
        <!-- Validate workflow structure and constraints -->
        <structural_validation>
          Verify DAG structure integrity:
          - Validate DAG acyclic property (no circular dependencies)
          - Check for unreachable tasks and dead ends
          - Identify isolated subgraphs and components
          - Ensure all dependencies can be satisfied
          - Detect redundant or unnecessary dependencies
        </structural_validation>
        
        <semantic_validation>
          Validate workflow logic and compatibility:
          - Task input/output type compatibility
          - Resource requirement feasibility
          - Business logic and workflow semantics
          - Error handling and recovery path completeness
          - Performance constraint satisfaction
        </semantic_validation>
      </workflow_validation>
    </workflow_modeling>
    
    <execution_orchestration>
      <!-- Orchestrate parallel task execution with optimization -->
      <execution_planning>
        <topological_sorting>
          <execution_order_determination>
            Determine optimal execution order using topological sort:
            - Identify operations that can run in parallel
            - Determine critical path for workflow completion
            - Optimize execution order for resource utilization
            - Handle cyclic dependency detection and resolution
            - Generate multiple valid execution sequences
          </execution_order_determination>
          
          <parallelization_opportunities>
            Identify opportunities for parallel execution:
            - Independent operation branches
            - Resource-compatible parallel operations
            - Load balancing across available resources
            - Batch processing opportunities
            - Pipeline parallelism for streaming workflows
          </parallelization_opportunities>
        </topological_sorting>
        
        <resource_scheduling>
          <resource_allocation>
            Schedule operations based on resource availability:
            - Memory-intensive operations scheduling
            - CPU-bound task distribution
            - I/O operation coordination
            - Network bandwidth allocation
            - GPU and specialized resource management
          </resource_allocation>
          
          <priority_based_scheduling>
            Implement priority-based task scheduling:
            - Critical path prioritization
            - Deadline-aware scheduling
            - Fair resource sharing policies
            - Preemption and task migration
            - Quality of service guarantees
          </priority_based_scheduling>
        </resource_scheduling>
      </execution_planning>
      
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
              - Predictive scheduling using historical data
            </performance_based_adaptation>
            
            <failure_recovery>
              Handle failures and recovery gracefully:
              - Automatic retry with exponential backoff
              - Alternative execution path selection
              - Partial workflow recovery and continuation
              - Rollback mechanisms for failed operations
              - Checkpoint-based recovery for long-running workflows
            </failure_recovery>
          </real_time_rescheduling>
          
          <conditional_execution>
            <branch_management>
              Handle conditional workflow branches:
              - Runtime condition evaluation
              - Dynamic branch selection
              - Lazy evaluation of conditional paths
              - Branch prediction and speculative execution
              - Merge point synchronization
            </branch_management>
            
            <loop_handling>
              Support iterative workflow patterns:
              - While-loop and for-loop constructs
              - Dynamic loop unrolling
              - Loop parallelization where possible
              - Convergence detection and early termination
              - Nested loop optimization
            </loop_handling>
          </conditional_execution>
        </adaptive_execution>
      </dynamic_execution>
    </execution_orchestration>
    
    <monitoring_analytics>
      <!-- Comprehensive monitoring and workflow analytics -->
      <real_time_monitoring>
        <execution_tracking>
          Track workflow execution in real-time:
          - Task execution progress and status updates
          - Resource usage and performance metrics
          - Bottleneck detection and analysis
          - Queue depths and wait times
          - Live workflow visualization and dashboards
        </execution_tracking>
        
        <performance_metrics>
          Monitor key performance indicators:
          - Workflow completion times and throughput
          - Task execution duration statistics
          - Resource utilization efficiency
          - Parallelization effectiveness
          - Error rates and recovery success
        </performance_metrics>
      </real_time_monitoring>
      
      <workflow_analytics>
        <optimization_insights>
          <critical_path_analysis>
            Analyze critical path for optimization:
            - Identify bottleneck operations
            - Suggest workflow restructuring
            - Recommend resource reallocation
            - Predict impact of optimizations
            - Historical trend analysis
          </critical_path_analysis>
          
          <pattern_recognition>
            Identify workflow patterns and anomalies:
            - Common execution patterns
            - Performance degradation trends
            - Resource usage patterns
            - Failure pattern analysis
            - Seasonal and cyclical behaviors
          </pattern_recognition>
        </optimization_insights>
        
        <predictive_analytics>
          Use historical data for predictions:
          - Workflow completion time estimation
          - Resource requirement forecasting
          - Failure probability prediction
          - Optimal scheduling recommendations
          - Capacity planning insights
        </predictive_analytics>
      </workflow_analytics>
    </monitoring_analytics>
    
    <integration_capabilities>
      <!-- Integration with Claude Code commands and components -->
      <command_integration>
        <workflow_composition>
          Compose workflows from Claude Code commands:
          - Chain multiple slash commands into workflows
          - Pass data between command executions
          - Handle command-specific dependencies
          - Integrate with component system
          - Support nested workflow composition
        </workflow_composition>
        
        <event_driven_triggers>
          Support event-driven workflow execution:
          - File system event triggers
          - Schedule-based execution
          - Webhook and API triggers
          - Command completion events
          - Custom event definitions
        </event_driven_triggers>
      </command_integration>
      
      <scalability_features>
        <distributed_execution>
          Support distributed workflow execution:
          - Multi-agent task distribution
          - Cross-system workflow coordination
          - Federated resource management
          - Network-aware scheduling
          - Fault-tolerant communication
        </distributed_execution>
        
        <workflow_persistence>
          Persist workflow state and history:
          - Workflow definition versioning
          - Execution history tracking
          - State checkpoint management
          - Audit trail maintenance
          - Performance baseline storage
        </workflow_persistence>
      </scalability_features>
    </integration_capabilities>
  </dag_orchestrator>

  <o>
DAG orchestration system completed with comprehensive workflow capabilities:

**Graph Construction:** Advanced dependency modeling and validation
**Execution Planning:** Intelligent topological sorting and resource scheduling
**Dynamic Adaptation:** Real-time rescheduling and failure recovery
**Monitoring:** Live tracking with performance metrics and analytics
**Optimization:** Critical path analysis and predictive insights
**Integration:** Seamless Claude Code command workflow composition
  </o>
</prompt_component>