<prompt_component>
  <meta_prompting_system>
    <self_improvement_pipeline>
      <!-- Implement DSPy-style automated prompt refinement -->
      <performance_tracking>
        <command_effectiveness>
          Track effectiveness metrics for each command execution:
          - Task completion success rate: ${metrics.success_rate}%
          - User satisfaction indicators: ${metrics.satisfaction_score}/10
          - Execution efficiency: ${metrics.efficiency_score}%
          - Error rate and recovery: ${metrics.error_recovery_rate}%
        </command_effectiveness>
        
        <improvement_opportunities>
          <if condition="metrics.success_rate &lt; 90">
            <trigger>Command effectiveness below threshold</trigger>
            <action>Initiate prompt optimization pipeline</action>
            <priority>high</priority>
          </if>
          <if condition="metrics.satisfaction_score &lt; 8">
            <trigger>User satisfaction below target</trigger>
            <action>Analyze user feedback and adapt approach</action>
            <priority>medium</priority>
          </if>
        </improvement_opportunities>
      </performance_tracking>
      
      <automated_optimization>
        <!-- DSPy-inspired iterative refinement -->
        <refinement_cycle>
          <step_1_analyze>
            Analyze current prompt performance against success metrics:
            - Identify failure patterns and root causes
            - Examine user feedback and correction patterns
            - Compare performance across different command variants
          </step_1_analyze>
          
          <step_2_hypothesize>
            Generate improvement hypotheses:
            - Alternative prompt structures that might perform better
            - Additional context that could improve outcomes
            - Different approach patterns based on successful cases
          </step_2_hypothesize>
          
          <step_3_test>
            Test prompt variations through:
            - A/B comparison with current version
            - Simulation of common use cases
            - Evaluation against success criteria
          </step_3_test>
          
          <step_4_adapt>
            Implement improvements that demonstrate measurable gains:
            - Update prompt structure based on testing results
            - Incorporate successful patterns from variations
            - Document lessons learned for future optimization
          </step_4_adapt>
        </refinement_cycle>
      </automated_optimization>
    </self_improvement_pipeline>
    
    <learning_mechanisms>
      <!-- Continuous learning from user interactions -->
      <pattern_recognition>
        <success_patterns>
          Identify and reinforce patterns that lead to successful outcomes:
          - Command sequences that work well together
          - Context combinations that improve accuracy
          - User interaction patterns that indicate satisfaction
          - Problem-solving approaches that consistently succeed
        </success_patterns>
        
        <failure_analysis>
          Learn from failures to prevent recurrence:
          - Common error patterns and their triggers
          - User correction patterns indicating misunderstanding
          - Context situations that lead to poor performance
          - Command limitations and appropriate boundaries
        </failure_analysis>
      </pattern_recognition>
      
      <adaptive_behavior>
        <personalization>
          Adapt to individual user preferences and patterns:
          - Preferred communication styles and detail levels
          - Common workflow patterns and shortcuts
          - Technical depth preferences and expertise level
          - Project-specific conventions and standards
        </personalization>
        
        <context_adaptation>
          Evolve understanding of project context over time:
          - Architectural patterns and design decisions
          - Code style preferences and conventions
          - Development workflow and tool preferences
          - Domain-specific knowledge and requirements
        </context_adaptation>
      </adaptive_behavior>
    </learning_mechanisms>
    
    <meta_command_evolution>
      <!-- Self-modifying command capabilities -->
      <command_optimization>
        <performance_driven_updates>
          Commands automatically evolve based on performance data:
          - Successful patterns get reinforced and expanded
          - Problematic approaches get modified or replaced
          - New capabilities emerge from user needs and patterns
          - Efficiency improvements get incorporated systematically
        </performance_driven_updates>
        
        <intelligent_defaults>
          Develop smarter defaults based on accumulated experience:
          - Context loading strategies based on command type
          - Tool selection patterns for different scenarios
          - Error handling approaches that work best
          - User interaction patterns that increase satisfaction
        </intelligent_defaults>
      </command_optimization>
      
      <meta_learning_integration>
        <cross_command_learning>
          Share learnings across the entire command ecosystem:
          - Successful patterns in one command inform others
          - Error patterns discovered anywhere improve all commands
          - User preferences learned in one context apply globally
          - Efficiency improvements propagate across the system
        </cross_command_learning>
        
        <system_evolution>
          The entire framework evolves based on collective learning:
          - New command needs identified from usage patterns
          - Framework architecture adapts to user workflows
          - Component relationships optimize based on actual usage
          - Documentation evolves to reflect real user needs
        </system_evolution>
      </meta_learning_integration>
    </meta_command_evolution>
    
    <quality_assurance>
      <!-- Ensure improvements don't degrade performance -->
      <regression_prevention>
        <performance_validation>
          Before implementing any changes, validate against baseline:
          - Run test suite against previous performance benchmarks
          - Verify no degradation in core functionality
          - Confirm improvements actually provide measurable benefit
          - Test edge cases to ensure robustness maintained
        </performance_validation>
        
        <rollback_capability>
          Maintain ability to revert changes if issues arise:
          - Version control for prompt modifications
          - Performance monitoring with automatic alerts
          - Quick rollback procedures for problematic changes
          - Gradual deployment with monitoring and validation
        </rollback_capability>
      </regression_prevention>
    </quality_assurance>
  </meta_prompting_system>
</prompt_component> 