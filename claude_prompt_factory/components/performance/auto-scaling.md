<prompt_component>
  <auto_scaling>
    <enterprise_scalability>
      <!-- Implement auto-scaling patterns for command execution -->
      <horizontal_scaling>
        <load_distribution>
          <intelligent_load_balancing>
            Distribute commands across execution instances:
            - Route simple commands to lightweight instances
            - Direct complex operations to high-performance instances
            - Balance load based on current system utilization
            - Implement sticky sessions for stateful operations
          </intelligent_load_balancing>
          
          <command_routing_strategy>
            <complexity_based_routing>
              Route commands based on complexity assessment:
              - `/query` commands: Route to analysis-optimized instances
              - `/task` commands: Route to development-focused instances
              - `/feature` commands: Route to high-memory instances
              - `/protocol` commands: Route to security-hardened instances
            </complexity_based_routing>
            
            <resource_aware_routing>
              Consider resource requirements for routing:
              - Memory-intensive operations to high-RAM instances
              - CPU-intensive tasks to compute-optimized instances
              - I/O-heavy operations to storage-optimized instances
              - Network-intensive tasks to bandwidth-optimized instances
            </resource_aware_routing>
          </command_routing_strategy>
        </load_distribution>
        
        <dynamic_scaling>
          <demand_prediction>
            <usage_pattern_analysis>
              Analyze usage patterns for proactive scaling:
              - Track daily/weekly command execution patterns
              - Identify peak usage hours and seasonal trends
              - Predict resource needs based on historical data
              - Anticipate scaling needs for large operations
            </usage_pattern_analysis>
            
            <workload_forecasting>
              Forecast workload requirements:
              - Analyze command complexity trends over time
              - Predict resource needs for upcoming features
              - Account for team growth and adoption patterns
              - Consider project lifecycle phases and scaling needs
            </workload_forecasting>
          </demand_prediction>
          
          <scaling_triggers>
            <performance_based_triggers>
              Scale based on performance metrics:
              - Response time exceeding acceptable thresholds
              - Queue depth indicating backlog buildup
              - CPU/memory utilization reaching capacity limits
              - Error rates indicating system stress
            </performance_based_triggers>
            
            <predictive_triggers>
              Scale proactively based on predictions:
              - Anticipated load increases from usage patterns
              - Scheduled high-impact operations or releases
              - Team onboarding and adoption curve predictions
              - Seasonal or cyclical usage pattern expectations
            </predictive_triggers>
          </scaling_triggers>
        </dynamic_scaling>
      </horizontal_scaling>
      
      <vertical_scaling>
        <resource_optimization>
          <adaptive_resource_allocation>
            Adjust resources based on command requirements:
            - Increase memory for large codebase analysis
            - Boost CPU for complex code generation tasks
            - Expand storage for extensive documentation operations
            - Optimize network bandwidth for API-heavy workflows
          </adaptive_resource_allocation>
          
          <performance_tuning>
            <context_window_optimization>
              Optimize context usage for better performance:
              - Dynamically adjust context size based on operation needs
              - Implement intelligent context chunking and caching
              - Use hierarchical loading for large codebases
              - Optimize token usage for cost and speed balance
            </context_window_optimization>
            
            <execution_optimization>
              Optimize command execution patterns:
              - Parallel execution for independent operations
              - Batch processing for similar commands
              - Streaming responses for long-running operations
              - Caching for frequently accessed information
            </execution_optimization>
          </performance_tuning>
        </resource_optimization>
        
        <cost_optimization>
          <intelligent_resource_management>
            <cost_aware_scaling>
              Balance performance with cost efficiency:
              - Use cost-effective instances for routine operations
              - Scale up only when performance gains justify costs
              - Implement automatic scale-down during low usage
              - Optimize resource allocation for budget constraints
            </cost_aware_scaling>
            
            <efficiency_monitoring>
              Monitor and improve resource efficiency:
              - Track cost per command execution
              - Identify opportunities for optimization
              - Monitor resource utilization patterns
              - Implement cost alerts and budgeting controls
            </efficiency_monitoring>
          </intelligent_resource_management>
        </cost_optimization>
      </vertical_scaling>
    </enterprise_scalability>
    
    <performance_monitoring>
      <!-- Comprehensive performance monitoring and optimization -->
      <real_time_metrics>
        <execution_performance>
          <response_time_tracking>
            Monitor command execution performance:
            - Average response time by command type
            - 95th and 99th percentile response times
            - Response time distribution analysis
            - Performance trend analysis over time
          </response_time_tracking>
          
          <throughput_monitoring>
            Track system throughput and capacity:
            - Commands processed per minute/hour
            - Concurrent execution capacity
            - Queue processing rates
            - System saturation points
          </throughput_monitoring>
        </execution_performance>
        
        <resource_utilization>
          <system_resource_tracking>
            Monitor system resource usage:
            - CPU utilization across all instances
            - Memory usage patterns and peaks
            - Storage I/O and capacity utilization
            - Network bandwidth and latency
          </system_resource_tracking>
          
          <application_resource_tracking>
            Monitor application-specific resources:
            - Context window utilization
            - Token consumption patterns
            - Cache hit rates and effectiveness
            - Component loading and execution times
          </application_resource_tracking>
        </resource_utilization>
      </real_time_metrics>
      
      <performance_optimization>
        <automatic_optimization>
          <adaptive_performance_tuning>
            Automatically optimize based on performance data:
            - Adjust context window sizes for optimal performance
            - Optimize component loading strategies
            - Tune caching parameters for better hit rates
            - Adapt execution strategies based on workload patterns
          </adaptive_performance_tuning>
          
          <bottleneck_detection>
            Identify and address performance bottlenecks:
            - Detect slow-performing operations and components
            - Identify resource constraints and optimization opportunities
            - Analyze execution patterns for efficiency improvements
            - Recommend architectural changes for better performance
          </bottleneck_detection>
        </automatic_optimization>
        
        <performance_recommendations>
          <optimization_suggestions>
            Provide actionable performance recommendations:
            - Suggest optimal instance types for workload patterns
            - Recommend scaling strategies based on usage trends
            - Identify cost optimization opportunities
            - Suggest architectural improvements for scalability
          </optimization_suggestions>
          
          <capacity_planning>
            Help with long-term capacity planning:
            - Predict future resource needs based on growth trends
            - Recommend infrastructure investments
            - Suggest optimization roadmaps
            - Plan for seasonal or cyclical demand patterns
          </capacity_planning>
        </performance_recommendations>
      </performance_optimization>
    </performance_monitoring>
    
    <enterprise_integration>
      <!-- Integration with enterprise infrastructure and workflows -->
      <infrastructure_integration>
        <cloud_platform_support>
          <multi_cloud_deployment>
            Support deployment across multiple cloud platforms:
            - AWS: EC2, ECS, Lambda for different scaling patterns
            - Azure: Virtual Machines, Container Instances, Functions
            - GCP: Compute Engine, Cloud Run, Cloud Functions
            - Kubernetes: Container orchestration for hybrid deployments
          </multi_cloud_deployment>
          
          <platform_optimization>
            Optimize for specific cloud platform features:
            - Use cloud-native scaling services (Auto Scaling Groups, etc.)
            - Leverage managed services for reduced operational overhead
            - Implement platform-specific monitoring and alerting
            - Use cloud provider optimization recommendations
          </platform_optimization>
        </cloud_platform_support>
        
        <enterprise_services>
          <monitoring_integration>
            Integrate with enterprise monitoring systems:
            - Export metrics to Prometheus, Grafana, DataDog
            - Send alerts to PagerDuty, Slack, or SIEM systems
            - Integrate with APM tools for distributed tracing
            - Support custom enterprise dashboards and reporting
          </monitoring_integration>
          
          <compliance_integration>
            Support enterprise compliance requirements:
            - Integrate with enterprise logging and audit systems
            - Support compliance frameworks (SOX, HIPAA, GDPR)
            - Implement data residency and sovereignty requirements
            - Support enterprise security and governance policies
          </compliance_integration>
        </enterprise_services>
      </infrastructure_integration>
      
      <operational_excellence>
        <automation_integration>
          <ci_cd_integration>
            Integrate scaling with CI/CD pipelines:
            - Automatic scaling for deployment and testing phases
            - Performance testing integration with scaling validation
            - Blue-green deployment support with traffic shifting
            - Rollback capabilities with automatic scaling adjustments
          </ci_cd_integration>
          
          <gitops_integration>
            Support GitOps workflows for scaling configuration:
            - Infrastructure as Code for scaling configuration
            - Version control for scaling policies and thresholds
            - Automated deployment of scaling configuration changes
            - Audit trail for scaling configuration modifications
          </gitops_integration>
        </automation_integration>
        
        <disaster_recovery>
          <resilience_patterns>
            Implement resilience patterns for enterprise reliability:
            - Multi-region deployment for disaster recovery
            - Data backup and replication for stateful components
            - Circuit breakers for graceful degradation
            - Chaos engineering for resilience testing
          </resilience_patterns>
          
          <business_continuity>
            Ensure business continuity during scaling events:
            - Zero-downtime scaling operations
            - Graceful handling of in-flight requests during scaling
            - Automatic failover to backup systems if needed
            - Priority routing for critical business operations
          </business_continuity>
        </disaster_recovery>
      </operational_excellence>
    </enterprise_integration>
  </auto_scaling>
</prompt_component> 