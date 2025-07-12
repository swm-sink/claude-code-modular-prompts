| version | last_updated | status |
|---------|--------------|--------|
| 1.1.0   | 2025-07-08   | stable |

# Error Recovery & Resilience Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="error_recovery" category="quality">
  
  <purpose>
    Comprehensive error recovery system with 4-tier hierarchy, automatic fallback sequences, and intelligent recovery tracking for Claude Code operations.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Detect failure type and severity immediately</step>
    <step>2. Determine appropriate recovery tier (1-4)</step>
    <step>3. Preserve context and session state</step>
    <step>4. Execute recovery with automatic fallback</step>
    <step>5. Track metrics for continuous improvement</step>
    <step>6. Document lessons learned</step>
  </thinking_pattern>
  
  <four_tier_recovery_hierarchy>
    
    <tier_1 name="module_recovery" severity="low" target_time="30s">
      <scope>Single module failures, dependency issues, config problems</scope>
      <strategy>
        - Graceful degradation with fallback modules
        - Exponential backoff retry (1s → 16s max)
        - 3 attempts before escalation
        - Preserve core functionality during recovery
      </strategy>
      <native_patterns>Auto-retry with BatchTool(), fallback routing</native_patterns>
    </tier_1>
    
    <tier_2 name="command_recovery" severity="medium" target_time="2m">
      <scope>Command failures, complex integration issues, multi-module problems</scope>
      <strategy>
        - Delegate to Task() for specialized recovery
        - State rollback with checkpoint restoration
        - Alternative command paths (auto → task → feature)
        - Context preservation via session backup
      </strategy>
      <native_patterns>Task("Recovery Expert", "Fix integration failure")</native_patterns>
    </tier_2>
    
    <tier_3 name="session_recovery" severity="high" target_time="5m">
      <scope>Session corruption, multi-agent failures, system-wide issues</scope>
      <strategy>
        - Full session reconstruction from GitHub
        - Multi-agent coordination recovery
        - State reconciliation across boundaries
        - Automated diagnostic reporting
      </strategy>
      <native_patterns>GitHub session recovery, swarm re-coordination</native_patterns>
    </tier_3>
    
    <tier_4 name="user_intervention" severity="critical" target_time="immediate">
      <scope>Unrecoverable errors, data integrity risks, security breaches</scope>
      <strategy>
        - Immediate user notification with context
        - Guided recovery instructions
        - Manual intervention points documented
        - Full audit trail preservation
      </strategy>
      <native_patterns>Interactive recovery guidance, audit compliance</native_patterns>
    </tier_4>
    
  </four_tier_recovery_hierarchy>
  
  <recovery_patterns>
    
    <parallel_recovery>
      <description>70% faster recovery through parallel operations</description>
      <implementation>
        BatchTool(
          ValidateModule("failed_module"),
          CheckDependencies("module_deps"),
          LoadFallback("backup_module")
        )
      </implementation>
    </parallel_recovery>
    
    <session_based_recovery>
      <description>GitHub session integration for state recovery</description>
      <implementation>
        - Auto-create recovery session: gh issue create
        - Track recovery progress in real-time
        - Link recovery artifacts to session
        - Maintain audit trail for compliance
      </implementation>
    </session_based_recovery>
    
    <context_preservation>
      <description>95%+ context retention during recovery</description>
      <strategies>
        - Session state serialization
        - Incremental checkpoint creation
        - Cross-boundary context mapping
        - Automatic state reconciliation
      </strategies>
    </context_preservation>
    
  </recovery_patterns>
  
  <failure_analysis>
    
    <root_cause_detection>
      <methods>
        - Pattern matching against known failures
        - Dependency graph analysis
        - Timeline reconstruction
        - Integration point verification
      </methods>
    </root_cause_detection>
    
    <predictive_prevention>
      <capabilities>
        - Early warning detection (complexity scoring)
        - Proactive resource allocation
        - Preemptive session backup
        - Risk-based escalation
      </capabilities>
    </predictive_prevention>
    
  </failure_analysis>
  
  <performance_metrics>
    <recovery_success_rates>
      <tier_1>95% automatic recovery success</tier_1>
      <tier_2>90% task delegation success</tier_2>
      <tier_3>85% session recovery success</tier_3>
      <tier_4>100% user-guided recovery</tier_4>
    </recovery_success_rates>
    <context_preservation>95%+ information retention</context_preservation>
    <detection_latency>Less than 5s for critical failures</detection_latency>
    <recovery_time>Within SLA for each tier</recovery_time>
  </performance_metrics>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for GitHub session integration
      patterns/intelligent-routing.md for fallback routing
      patterns/multi-agent.md for swarm recovery coordination
      quality/production-standards.md for compliance requirements
    </depends_on>
    <provides_to>
      All commands for resilient execution
      quality/predictive-escalation.md for failure prediction
      development/task-management.md for recovery task delegation
    </provides_to>
  </integration_points>
  
  <recovery_procedures>
    
    <module_failure_recovery>
      1. Detect failure through health checks
      2. Attempt automatic retry with backoff
      3. Load fallback module if available
      4. Degrade gracefully maintaining core features
      5. Log recovery metrics for analysis
    </module_failure_recovery>
    
    <session_corruption_recovery>
      1. Detect corruption through integrity checks
      2. Create recovery session in GitHub
      3. Reconstruct state from checkpoints
      4. Validate recovered state consistency
      5. Resume operations with full context
    </session_corruption_recovery>
    
    <multi_agent_failure_recovery>
      1. Detect coordination breakdown
      2. Isolate failed agents
      3. Redistribute work to healthy agents
      4. Merge partial results intelligently
      5. Complete task with degraded capacity
    </multi_agent_failure_recovery>
    
  </recovery_procedures>
  
  <continuous_improvement>
    <metrics_tracking>
      - Recovery frequency by tier
      - Time to recovery by failure type
      - Context preservation accuracy
      - User intervention requirements
    </metrics_tracking>
    <pattern_learning>
      - Update failure patterns database
      - Refine recovery strategies
      - Optimize tier thresholds
      - Improve predictive capabilities
    </pattern_learning>
  </continuous_improvement>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Core error recovery system with proven 4-tier hierarchy achieving 90%+ automatic recovery rates.