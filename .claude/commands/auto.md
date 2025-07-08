| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /auto - Smart routing for any request

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Intelligent routing with research-first approach and complexity scoring">
  
  <delegation target="modules/patterns/intelligent-routing.md">
    Analyze request → Calculate complexity → Research deeply → Route to optimal command
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Parse request and identify key components with TDD consideration</action>
      <critical_thinking>
        - What exactly is being requested and is it testable?
        - Does this require code changes that need TDD enforcement?
        - What are the components, integrations, and security implications?
        - Should I route to a TDD-enforcing command or research-only?
      </critical_thinking>
      <output_format>REQUEST_ANALYSIS: [type] affecting [components] requiring [approach]</output_format>
      <validation>Request clearly categorized with TDD requirements identified</validation>
      <enforcement>BLOCK if request type unclear or TDD needs unidentified</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Calculate complexity score with TDD overhead consideration</action>
      <critical_thinking>
        - Components×5 + integrations×4 + security×3 = base score
        - Add +2 for each component requiring new tests
        - Add +3 for each integration requiring test coordination
        - Does complexity justify TDD-enforcing vs research commands?
      </critical_thinking>
      <output_format>COMPLEXITY_SCORE: [number] ([base] + [tdd_overhead]) = [total]</output_format>
      <validation>Score calculated including TDD complexity factors</validation>
      <enforcement>VERIFY complexity includes TDD requirements in routing decision</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Research codebase if needed for informed TDD-aware routing</action>
      <critical_thinking>
        - What existing code/tests would be affected?
        - Are there existing test patterns to follow?
        - Do I need to understand current architecture before routing?
        - Would research-first help choose better TDD-enforcing command?
      </critical_thinking>
      <output_format>RESEARCH_STATUS: [NEEDED/COMPLETE] - [findings relevant to TDD approach]</output_format>
      <validation>Research completed if needed, TDD implications understood</validation>
      <enforcement>BLOCK routing until necessary research confirms TDD approach</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Route based on complexity with TDD enforcement priority</action>
      <critical_thinking>
        - ≤2: /query (research-only, no TDD needed)
        - 3-9: /task (single-component TDD enforcement)
        - 10-14: /feature (comprehensive TDD with PRD)
        - ≥15: /swarm (multi-agent TDD coordination)
        - Does the chosen command enforce TDD appropriately?
      </critical_thinking>
      <output_format>ROUTING_DECISION: Score [number] → /[command] (TDD enforcement: [level])</output_format>
      <validation>Route ensures appropriate TDD enforcement for complexity level</validation>
      <enforcement>VERIFY routed command has adequate TDD enforcement capabilities</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Execute routing with TDD-aware module delegation</action>
      <critical_thinking>
        - Does the target command have proper TDD integration?
        - Will the routed command enforce TDD appropriately?
        - Are quality gates properly configured for this routing?
        - Is the execution path optimized for TDD success?
      </critical_thinking>
      <output_format>EXECUTION_DELEGATION: Routing to /[command] with TDD enforcement [confirmed/verified]</output_format>
      <validation>Target command confirmed to have appropriate TDD capabilities</validation>
      <enforcement>BLOCK if target command lacks required TDD enforcement</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <tdd_integration enforcement="MANDATORY">
    <routing_tdd_awareness>Route to TDD-enforcing commands for code changes, research commands for analysis</routing_tdd_awareness>
    <complexity_adjustment>Include TDD overhead in complexity scoring for accurate routing</complexity_adjustment>
    <command_verification>Verify target commands have proper TDD enforcement before routing</command_verification>
    <validation>Reference quality/tdd.md#routing_considerations for TDD-aware routing</validation>
    <blocking_conditions>
      <condition>Routing code changes to non-TDD-enforcing commands</condition>
      <condition>Complexity calculation ignores TDD testing requirements</condition>
      <condition>Target command lacks adequate TDD enforcement capabilities</condition>
      <condition>Research bypassed when TDD approach unclear</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before routing decision</module>
      <module>patterns/intelligent-routing.md - Request analysis and complexity scoring</module>
      <module>quality/tdd.md - TDD-aware routing considerations</module>
      <module>patterns/pattern-library.md - Proven execution patterns</module>
    </core_stack>
    <contextual_modules>
      <conditional module="development/research-analysis.md" condition="research_needed"/>
      <conditional module="quality/error-recovery.md" condition="routing_failures"/>
      <conditional module="patterns/session-management.md" condition="complex_routing"/>
    </contextual_modules>
  </module_execution>
  
  <depends_on>
    patterns/intelligent-routing.md for request analysis and routing
    patterns/pattern-library.md for proven execution patterns
    quality/error-recovery.md for resilient execution
    All commands and modules for dynamic routing decisions
  </depends_on>
  
  <examples>
    /auto "Add user authentication"     → Score ~12 → Routes to /task
    /auto "Build e-commerce platform"   → Score 40+ → Routes to /swarm
    /auto "How does caching work?"      → Score 1 → Routes to /query
    /auto "Create API endpoints"        → Score ~10 → Routes to /feature
  </examples>
  
  <rules>
    <rule>ALWAYS calculate complexity score before routing</rule>
    <rule>ALWAYS research first for informed decisions</rule>
    <rule>NEVER skip complexity scoring algorithm</rule>
  </rules>
  
  <pattern_usage>
    • Uses three_x_rule pattern for routing decisions
    • Implements consequence_mapping for impact analysis
    • Leverages parallel_execution for research operations
    • Applies explicit_validation pattern
    • Uses smart_memoization for cached routing decisions
    • Integrates error_recovery for resilient routing
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/patterns/intelligent-routing.md for full implementation
  </pattern_usage>
  
</command>
```