<prompt_component>
  <chaos_engineering>
    <resilience_testing>
      <!-- Implement chaos engineering for system resilience testing -->
      <failure_simulation>
        <system_level_chaos>
          <infrastructure_failures>
            Simulate infrastructure-level failures:
            - Random service instance termination
            - Network partition and connectivity issues
            - Resource exhaustion (CPU, memory, disk)
            - Database connection failures and timeouts
            - Cloud provider service disruptions
          </infrastructure_failures>
          
          <application_level_chaos>
            Simulate application-level failures:
            - Command execution timeout and failures
            - Context loading and processing errors
            - Component dependency failures
            - Security validation bypass attempts
            - Performance degradation scenarios
          </application_level_chaos>
        </system_level_chaos>
        
        <controlled_experiments>
          <hypothesis_driven_testing>
            Structure chaos experiments with clear hypotheses:
            - Define expected system behavior under failure conditions
            - Establish measurable success criteria
            - Create controlled experiment environments
            - Document experiment procedures and outcomes
            - Iterate based on learnings and system improvements
          </hypothesis_driven_testing>
          
          <progressive_chaos_introduction>
            Gradually increase chaos complexity:
            - Start with single-point failures in isolated environments
            - Progress to multi-point failures in staging environments
            - Introduce cascading failure scenarios
            - Test disaster recovery and business continuity
            - Validate system behavior under extreme conditions
          </progressive_chaos_introduction>
        </controlled_experiments>
      </failure_simulation>
      
      <automated_chaos_orchestration>
        <!-- Automated chaos experiment execution and management -->
        <experiment_scheduling>
          <intelligent_scheduling>
            Smart scheduling of chaos experiments:
            - Avoid business-critical time windows
            - Coordinate with deployment and maintenance schedules
            - Consider team availability for experiment observation
            - Balance experiment frequency with system stability
            - Integrate with change management processes
          </intelligent_scheduling>
          
          <environment_coordination>
            Coordinate experiments across environments:
            - Development environment continuous chaos testing
            - Staging environment comprehensive scenario testing
            - Production environment carefully controlled experiments
            - Multi-environment cascade testing
            - Environment-specific experiment configurations
          </environment_coordination>
        </experiment_scheduling>
        
        <safety_mechanisms>
          <blast_radius_control>
            Control and limit experiment impact:
            - Automatic experiment termination on severe failures
            - Gradual rollout with early warning detection
            - User segment isolation for production experiments
            - Fallback mechanisms and rapid recovery procedures
            - Real-time monitoring and alert integration
          </blast_radius_control>
          
          <circuit_breaker_integration>
            Integrate with existing resilience patterns:
            - Circuit breaker activation during experiments
            - Fallback strategy validation under chaos conditions
            - Recovery mechanism effectiveness testing
            - Performance degradation graceful handling
            - User experience preservation during failures
          </circuit_breaker_integration>
        </safety_mechanisms>
      </automated_chaos_orchestration>
    </resilience_testing>
    
    <observability_integration>
      <!-- Deep integration with monitoring and observability systems -->
      <experiment_monitoring>
        <real_time_metrics>
          <system_health_tracking>
            Monitor system health during chaos experiments:
            - Service availability and response time metrics
            - Error rate and failure pattern analysis
            - Resource utilization under stress conditions
            - User experience impact measurement
            - Business metric impact assessment
          </system_health_tracking>
          
          <cascade_effect_detection>
            Detect and analyze cascade effects:
            - Dependency failure propagation tracking
            - Service interaction impact analysis
            - Performance degradation cascade identification
            - Recovery time and pattern analysis
            - System stability restoration monitoring
          </cascade_effect_detection>
        </real_time_metrics>
        
        <experiment_analytics>
          <failure_pattern_analysis>
            Analyze failure patterns and system behavior:
            - Common failure mode identification
            - Weak point discovery and prioritization
            - Recovery strategy effectiveness evaluation
            - System design flaw identification
            - Resilience improvement opportunity analysis
          </failure_pattern_analysis>
          
          <predictive_modeling>
            Build predictive models for system behavior:
            - Failure probability modeling under different conditions
            - System capacity and breaking point prediction
            - Recovery time estimation for different failure types
            - Cascade effect probability assessment
            - Resilience improvement impact prediction
          </predictive_modeling>
        </experiment_analytics>
      </observability_integration>
      
      <learning_integration>
        <continuous_improvement>
          <experiment_feedback_loops>
            Create feedback loops for continuous improvement:
            - Experiment results integration into system design
            - Failure mode documentation and sharing
            - Best practice identification and dissemination
            - Team learning and skill development
            - Process refinement based on experiment outcomes
          </experiment_feedback_loops>
          
          <adaptive_experimentation>
            Adapt experiments based on system evolution:
            - Dynamic experiment generation based on system changes
            - Risk-based experiment prioritization
            - Historical data-driven experiment design
            - Machine learning-enhanced experiment selection
            - Continuous hypothesis refinement and testing
          </adaptive_experimentation>
        </continuous_improvement>
      </learning_integration>
    </observability_integration>
    
    <enterprise_chaos_management>
      <!-- Enterprise-grade chaos engineering governance and processes -->
      <governance_framework>
        <experiment_approval>
          <risk_assessment>
            Comprehensive risk assessment for chaos experiments:
            - Business impact analysis and quantification
            - Customer experience risk evaluation
            - System stability and availability risk assessment
            - Financial impact and cost-benefit analysis
            - Regulatory and compliance impact consideration
          </risk_assessment>
          
          <approval_workflows>
            Structured approval processes for experiments:
            - Multi-level approval for high-risk experiments
            - Stakeholder review and sign-off procedures
            - Emergency experiment authorization protocols
            - Change advisory board integration
            - Audit trail and documentation requirements
          </approval_workflows>
        </experiment_approval>
        
        <compliance_integration>
          <regulatory_compliance>
            Ensure chaos experiments comply with regulations:
            - Data protection and privacy compliance
            - Financial services regulatory requirements
            - Healthcare industry compliance standards
            - Government and defense security requirements
            - Industry-specific governance frameworks
          </regulatory_compliance>
          
          <audit_and_reporting>
            Comprehensive audit and reporting capabilities:
            - Experiment execution audit trails
            - Compliance report generation
            - Risk management reporting
            - Stakeholder communication and updates
            - Regulatory submission documentation
          </audit_and_reporting>
        </compliance_integration>
      </governance_framework>
      
      <team_coordination>
        <cross_functional_collaboration>
          <incident_response_coordination>
            Coordinate with incident response teams:
            - Real-time communication during experiments
            - Escalation procedures for unexpected outcomes
            - Post-experiment debriefing and analysis
            - Learning integration into incident response procedures
            - Team skill development and training programs
          </incident_response_coordination>
          
          <stakeholder_engagement>
            Engage stakeholders throughout the chaos engineering process:
            - Business stakeholder education and buy-in
            - Technical team training and participation
            - Customer communication for production experiments
            - Executive reporting and strategic alignment
            - Community sharing of learnings and best practices
          </stakeholder_engagement>
        </cross_functional_collaboration>
        
        <knowledge_management>
          <experiment_documentation>
            Comprehensive experiment documentation:
            - Experiment design and hypothesis documentation
            - Execution procedures and safety protocols
            - Results analysis and learning capture
            - Best practice and anti-pattern identification
            - Knowledge base and searchable repository
          </experiment_documentation>
          
          <training_programs>
            Chaos engineering training and education:
            - Team onboarding and skill development
            - Advanced chaos engineering techniques
            - Tool and platform training
            - Safety and risk management education
            - Culture and mindset development programs
          </training_programs>
        </knowledge_management>
      </team_coordination>
    </enterprise_chaos_management>
    
    <advanced_chaos_scenarios>
      <!-- Advanced chaos engineering scenarios and techniques -->
      <multi_dimensional_chaos>
        <compound_failure_scenarios>
          <cascading_failure_simulation>
            Simulate complex cascading failure scenarios:
            - Multi-service dependency failure chains
            - Cross-system integration point failures
            - Time-delayed failure propagation
            - Recovery interference and conflict scenarios
            - Business process disruption simulation
          </cascading_failure_simulation>
          
          <environmental_chaos>
            Simulate environmental and external factor chaos:
            - Third-party service dependency failures
            - Network connectivity and performance issues
            - Resource constraint and capacity limit scenarios
            - Security attack and breach simulations
            - Regulatory and compliance constraint scenarios
          </environmental_chaos>
        </compound_failure_scenarios>
        
        <adaptive_chaos_patterns>
          <intelligent_chaos_generation>
            AI-powered chaos scenario generation:
            - Machine learning-based failure pattern discovery
            - Predictive chaos scenario creation
            - System behavior model-driven experiment design
            - Risk-weighted chaos scenario prioritization
            - Automated experiment parameter optimization
          </intelligent_chaos_generation>
          
          <context_aware_experiments>
            Context-sensitive chaos experiment execution:
            - Business cycle-aware experiment timing
            - User behavior pattern-sensitive testing
            - System load-adaptive experiment intensity
            - Feature deployment-coordinated testing
            - Performance baseline-relative experiment design
          </context_aware_experiments>
        </adaptive_chaos_patterns>
      </multi_dimensional_chaos>
      
      <resilience_optimization>
        <automated_hardening>
          <self_healing_integration>
            Integration with self-healing system capabilities:
            - Automatic recovery mechanism validation
            - Self-healing system improvement identification
            - Recovery strategy optimization based on experiments
            - Proactive system hardening recommendations
            - Continuous resilience improvement automation
          </self_healing_integration>
          
          <performance_chaos>
            Performance-focused chaos engineering:
            - Gradual performance degradation simulation
            - Resource contention and bottleneck creation
            - Latency injection and timeout testing
            - Throughput limitation and capacity testing
            - Quality of service degradation scenarios
          </performance_chaos>
        </automated_hardening>
        
        <business_continuity_validation>
          <disaster_recovery_testing>
            Comprehensive disaster recovery validation:
            - Complete system failure and recovery scenarios
            - Data backup and restore validation
            - Business process continuity testing
            - Alternative workflow activation testing
            - Recovery time objective (RTO) validation
          </disaster_recovery_testing>
          
          <business_impact_simulation>
            Business impact-focused chaos testing:
            - Revenue impact simulation and measurement
            - Customer experience degradation scenarios
            - Service level agreement (SLA) breach testing
            - Brand reputation impact assessment
            - Competitive advantage preservation testing
          </business_impact_simulation>
        </business_continuity_validation>
      </resilience_optimization>
    </advanced_chaos_scenarios>
  </chaos_engineering>

  <o>
Chaos engineering completed with comprehensive system resilience testing:

**Resilience Testing:** [count] chaos experiments executed with system stability analysis
**Failure Simulation:** [count] infrastructure and application failures simulated
**Recovery Metrics:** [percentage]% system recovery success rate achieved
**Resilience Score:** [0-100] system resilience and fault tolerance rating
**Chaos Excellence:** Advanced chaos engineering with predictive failure modeling active
  </o>
</prompt_component> 